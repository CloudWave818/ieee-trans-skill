#!/usr/bin/env python3
"""Rebuild source-anchored manuscript fingerprints for the exact preferred 29 PDFs.

Extraction is evidence, not a venue classifier or style recommendation. Human-reviewed
section boundaries, form evidence and rhetorical annotations live in review.json.
Only material belonging to this profile library is written by this script.
"""
import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
import runpy
import statistics

import fitz

ROOT = Path(__file__).resolve().parents[1]
REF = ROOT / "references" / "preferred_29"
OUT = REF / "manuscript_profiles"
WORD = re.compile(r"[A-Za-z]+(?:[-’'][A-Za-z]+)*|\d+(?:\.\d+)?")


def clean(s):
    return re.sub(r"\s+", " ", s.replace("\u00ad", "")).strip()


def extract(pdf_dir):
    OUT.mkdir(parents=True, exist_ok=True)
    papers = json.loads((REF / "papers.json").read_text(encoding="utf-8"))
    result = []
    for p in papers:
        pdf = pdf_dir / p["filename"]
        digest = hashlib.sha256(pdf.read_bytes()).hexdigest()
        if digest != p["sha256"]:
            raise ValueError(f"Source changed for {p['paper']}: reconcile the reviewed profile")
        doc = fitz.open(pdf)
        pages = []
        for i, page in enumerate(doc):
            blocks = []
            for block in page.get_text("dict")["blocks"]:
                if block["type"] != 0:
                    continue
                lines = []
                sizes = []
                fonts = Counter()
                for line in block["lines"]:
                    line_text = clean("".join(s["text"] for s in line["spans"]))
                    if line_text:
                        lines.append(line_text)
                    for s in line["spans"]:
                        sizes.append(s["size"])
                        fonts[s["font"]] += len(s["text"])
                text = "\n".join(lines)
                blocks.append({"bbox": [round(v, 2) for v in block["bbox"]],
                               "text": text, "words": len(WORD.findall(text)),
                               "font_sizes": sorted(set(round(x, 2) for x in sizes)),
                               "fonts": dict(fonts)})
            # Column-order is NOT guessed: retain source block ids/bboxes and
            # require explicit section start locators in the reviewed registry.
            pages.append({"page": i + 1, "width_pt": round(page.rect.width, 2),
                          "height_pt": round(page.rect.height, 2), "blocks": blocks})
        result.append({**p, "pdf_metadata": doc.metadata, "pages": pages})
        doc.close()
    (OUT / "source_blocks.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return result


def prose_candidate(block):
    t = block["text"]
    return (block["words"] >= 40 and
            len(re.findall(r"[A-Za-z]", t)) / max(1, len(t)) >= .60 and
            not re.match(r"^(?:Fig\.?\s|Figure\s|TABLE\s|Table\s|Algorithm\s|IEEE ROBOTICS|arXiv:)", t))


def heading_offset(heading, text):
    """Honor a heading merged at the end of a previous paragraph block."""
    chars = [(c.lower(), i) for i, c in enumerate(text) if c.isascii() and c.isalnum()]
    key = "".join(c.lower() for c in heading if c.isascii() and c.isalnum())
    found = "".join(c for c, _ in chars).find(key)
    if found < 0:
        if heading not in {"Introduction (unheaded)", "Overview / Experiment Details"}:
            raise ValueError(f"Reviewed section heading absent: {heading}")
        return 0
    pos = chars[found][1]
    return text.rfind("\n", 0, pos) + 1 if pos > 80 else 0


def segment(flat, start, start_offset, end, end_offset):
    members = []
    for n in range(start, min(end + 1, len(flat))):
        page, index, block = flat[n]
        t = block["text"]
        if n == end:
            t = t[:end_offset]
        if n == start:
            t = t[start_offset:]
        if t.strip():
            members.append((page, index, {**block, "text": t, "words": len(WORD.findall(t))}))
    return members


def publish(records):
    notes = runpy.run_path(str(OUT / "reviewed_notes.py"))
    sections_review = notes["SECTIONS"]
    if set(sections_review) != {p["paper"] for p in records}:
        raise ValueError("Reviewed coverage must equal the source inventory")
    profiles = []
    for p in records:
        pid = p["paper"]
        flat = [(q["page"], i, b) for q in p["pages"] for i, b in enumerate(q["blocks"])]
        lookup = {(page, i): b for page, i, b in flat}
        order = {(page, i): n for n, (page, i, b) in enumerate(flat)}
        reviewed = sections_review[pid]
        locators = [(page, block) for title, page, block, role in reviewed]
        if any(loc not in lookup for loc in locators) or locators != sorted(locators):
            raise ValueError(f"Invalid section locator sequence for {pid}")
        offsets = [heading_offset(title, lookup[(page, block)]["text"]) for title, page, block, role in reviewed]
        measured = []
        for n, (heading, page, block, role) in enumerate(reviewed):
            start = order[(page, block)]
            end = order[locators[n + 1]] if n + 1 < len(locators) else len(flat)
            end_offset = offsets[n + 1] if n + 1 < len(locators) else 0
            members = segment(flat, start, offsets[n], end, end_offset)
            measured.append({"heading": heading, "role": role,
                             "start": {"page": page, "block": block, "char_offset": offsets[n]},
                             "last_content_page": members[-1][0] if members else page,
                             "extracted_tokens": sum(b["words"] for _, _, b in members),
                             "prose_candidate_tokens": sum(b["words"] for _, _, b in members if prose_candidate(b))})
        main_roles = {"intro", "related", "setup", "method", "implementation", "evidence", "closing"}
        denominator = sum(s["prose_candidate_tokens"] for s in measured if s["role"] in main_roles)
        for s in measured:
            s["main_prose_share_pct"] = round(100 * s["prose_candidate_tokens"] / denominator, 1) if s["role"] in main_roles and denominator else None
        main_end_n = next(n for n, (_, _, _, role) in enumerate(reviewed) if role in {"references", "appendix", "backmatter", "supplement"})
        main_end = order[locators[main_end_n]]
        main_start = order[locators[0]]
        body = segment(flat, main_start, offsets[0], main_end, offsets[main_end_n])
        candidate_blocks = [b for _, _, b in body if prose_candidate(b)]
        dims = [(q["width_pt"], q["height_pt"]) for q in p["pages"]]
        fonts = Counter()
        sizes = Counter()
        for b in candidate_blocks:
            fonts.update(b["fonts"])
            if b["font_sizes"]:
                sizes[max(b["font_sizes"])] += b["words"]
        widths = [b["bbox"][2] - b["bbox"][0] for b in candidate_blocks]
        column_ratio = statistics.median(widths) / dims[0][0] if widths else None
        columns = "single_column" if column_ratio and column_ratio > .60 else "two_column" if column_ratio else "unknown"
        eq = []
        for page, block, b in body:
            for line in b["text"].splitlines():
                # Only trailing display labels are counted, not inline Eq. references.
                # Nature's damaged font map uses eth characters instead of parentheses.
                pattern = r"(?:\(|ð)(\d{1,3})([a-f]?)(?:\)|Þ)\s*$"
                for number, suffix in re.findall(pattern, line):
                    eq.append({"number": int(number), "suffix": suffix, "page": page, "block": block})
        unique_eq = sorted({x["number"] for x in eq})
        algorithms = []
        for page, block, b in body:
            # Caption/title, NOT prose such as 'Algorithm 1, which is ...'.
            m = re.match(r"^Algorithm\s+(\d+)[: ]\s*([^\n]+)", b["text"])
            if m and not re.match(r"(?:which|summarizes|is|shows|illustrates|presents)\b", m[2], re.I):
                algorithms.append({"number": int(m[1]), "page": page, "block": block, "title": m[2]})
        sample_records = []
        for page, block, kind, moves in notes["SAMPLES"][pid]:
            if (page, block) not in lookup:
                raise ValueError(f"Missing sample locator {pid} p{page} b{block}")
            b = lookup[(page, block)]
            sample_records.append({"page": page, "block": block, "kind": kind,
                                   "source_block_tokens": b["words"], "moves": moves,
                                   "bbox": b["bbox"]})
        main_end_page = body[-1][0]
        for s in measured:
            span = s["last_content_page"] - s["start"]["page"] + 1
            s["pdf_page_span_count"] = span
            s["main_pdf_page_coverage_pct_nonadditive"] = round(100 * span / main_end_page, 1) if s["role"] in main_roles else None
        role_tokens = Counter()
        for s in measured:
            if s["role"] in main_roles:
                role_tokens[s["role"]] += s["prose_candidate_tokens"]
        metrics = {"pdf_pages": p["pdf_pages"], "main_text_last_page": main_end_page,
                   "page_size_pt": list(dims[0]), "layout_columns": columns,
                   "median_prose_block_width_pt": round(statistics.median(widths), 2) if widths else None,
                   "predominant_prose_fonts": fonts.most_common(3), "modal_prose_max_font_size_pt": sizes.most_common(1)[0][0] if sizes else None,
                   "main_prose_candidate_tokens": denominator,
                   "median_prose_block_tokens": round(statistics.median(b["words"] for b in candidate_blocks), 1) if candidate_blocks else None,
                   "prose_block_token_iqr": [round(x, 1) for x in statistics.quantiles([b["words"] for b in candidate_blocks], n=4)[::2]] if len(candidate_blocks) >= 4 else None,
                   "role_prose_share_pct": {r: round(100 * v / denominator, 1) for r, v in role_tokens.items()} if denominator else {},
                   "detected_unique_display_equation_labels": unique_eq,
                   "equation_label_locators": eq, "display_equation_label_count_proxy": len(unique_eq),
                   "equation_labels_per_main_pdf_page_proxy": round(len(unique_eq) / main_end_page, 2),
                   "algorithms": algorithms,
                   "measurement_limits": "Section spans use source PDF block order, not semantic reading order; merged late headings have reviewed-text char offsets. Prose candidates are >=40 extracted tokens with >=60% Latin letters and exclude recognized captions. PDF blocks may merge/split paragraphs. Shares are extracted-prose proxies, not typeset page-area fractions or exact word quotas. Display-label detection can miss unnumbered equations or damaged fonts; algorithm count covers recognized main-body captions only."}
        form = notes["FORMS"].get(pid, {"value": "UNVERIFIED", "venue": "UNKNOWN", "status": "unverified", "confidence": "no_venue_confirmation", "evidence": "Local PDF has no explicit confirmed venue masthead; length and IEEE-shaped layout do not establish Letter/Transactions form."})
        morphology = "NATURE_RESULT_LED" if pid == "R29" else "SINGLE_COLUMN_PREPRINT" if pid == "R26" else "AUTHOR_YEAR_TWO_COLUMN" if pid == "R28" else "IEEE_EXTENDED" if pid in notes["EXTENDED"] else "IEEE_COMPACT"
        profile = {"schema_version": 1, "paper_id": pid, "title": p["title"],
                   "source": {"pdf_filename": p["filename"], "sha256": p["sha256"]},
                   "article_form": form, "morphology": morphology, "learning_type": p["learning_type"],
                   "metrics": metrics, "sections": measured, "rhetorical_samples": sample_records,
                   "blueprint": notes["BLUEPRINTS"][pid],
                   "caution": notes["CAUTIONS"].get(pid, "只迁移来源中的结构、句段功能与证据组织；新稿内容及数字必须来自项目。"),
                   "review_scope": "All source pages extracted; main section boundaries and three source text blocks reviewed manually. Font/geometry metrics are automatic proxies. Source figure aesthetics require the separate visual case library."}
        profiles.append(profile)
        text = [f"# {pid} — {p['title']}", "", f"Source: `{p['filename']}` · SHA-256 `{p['sha256']}`", "",
                f"Article form: **{form['value']}** · {form['venue']} · {form['status']}",
                f"Evidence: {form['evidence']} ({form['confidence']}).", ""]
        if form.get("url"):
            text += [f"External metadata: [{pid} official arXiv record]({form['url']}) (checked {form['checked']}; author-reported venue, local PDF remains the fingerprint source).", ""]
        text += [f"Morphology: `{morphology}`. {profile['caution']}", "", "## Copyable manuscript architecture", "", profile["blueprint"], "",
                 "## Measured source structure", "", "PDF pages count references and attachments; the table's overlapping page intervals are locator ranges, not additive page budgets. Prose share uses the measured main-body candidate-token denominator.", "",
                 "| Source section | Role | PDF locator span | Candidate tokens | Main prose share |", "|---|---|---|---:|---:|"]
        for s in measured:
            ratio = str(s["main_prose_share_pct"]) + "%" if s["main_prose_share_pct"] is not None else "excluded"
            text.append(f"| {s['heading']} | {s['role']} | p{s['start']['page']} b{s['start']['block']} → p{s['last_content_page']} | {s['prose_candidate_tokens']} | {ratio} |")
        font = ", ".join(x[0] for x in metrics["predominant_prose_fonts"][:2])
        text += ["", f"Layout: {columns}; page {dims[0][0]} × {dims[0][1]} pt; median prose-block width {metrics['median_prose_block_width_pt']} pt. Predominant prose font(s): {font}; modal maximum size in candidate blocks {metrics['modal_prose_max_font_size_pt']} pt.", "",
                 f"Main prose proxy: {denominator} tokens; median source prose block {metrics['median_prose_block_tokens']} tokens, IQR {metrics['prose_block_token_iqr']}. This is a rhythm diagnostic: one PDF block is not guaranteed to equal one paragraph.", "",
                 f"Detected numbered-equation labels in main text: {len(unique_eq)} distinct base numbers ({metrics['equation_labels_per_main_pdf_page_proxy']} per main PDF page); sublabels share a base number. Main-body algorithm captions: {len(algorithms)}.", "", "## Three source-grounded rhetorical samples", ""]
        for s in sample_records:
            text += [f"- **{s['kind']} — p{s['page']} b{s['block']}**, {s['source_block_tokens']} extracted tokens: {s['moves']}"]
        text += ["", "## Source boundary", "", "Instantiate the source-specific blueprint and moves above using the [manuscript donor contract](../MANUSCRIPT_STYLE_PLAYBOOK.md). Prose shares, equation detection and PDF paragraph blocks are measured proxies; exact layout and paragraph boundaries require inspecting the donor pages. Never use the source's results as project evidence.", "", "Exact block text/bboxes/fonts: `source_blocks.json`; reviewed judgments: `reviewed_notes.py`; all metrics, nonadditive page-span coverage and equation locators: `profiles.json`. p/b locators refer to the PDF hash recorded above.", ""]
        (OUT / f"{pid}.md").write_text("\n".join(text), encoding="utf-8")
    (OUT / "profiles.json").write_text(json.dumps(profiles, ensure_ascii=False, indent=2), encoding="utf-8")
    rows = ["# Preferred 29 manuscript fingerprint index", "", "Article form and manuscript morphology are separate fields. UNVERIFIED never means Letter or Transactions. Open only the chosen profiles, then inspect their exact source locators.", "", "| Paper | Article form | Morphology | PDF/main ending page | Method / evidence prose share | Profile |", "|---|---|---|---|---|---|"]
    for p in profiles:
        shares = p["metrics"]["role_prose_share_pct"]
        rows.append(f"| {p['paper_id']} | {p['article_form']['value']} | {p['morphology']} | {p['metrics']['pdf_pages']} / {p['metrics']['main_text_last_page']} | {shares.get('method',0)}% / {shares.get('evidence',0)}% | [{p['paper_id']}]({p['paper_id']}.md) |")
    (OUT / "INDEX.md").write_text("\n".join(rows) + "\n", encoding="utf-8")
    print(f"Published {len(profiles)} reviewed manuscript profiles")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pdf-dir", type=Path, default=ROOT / "papers" / "preferred_29")
    ap.add_argument("--extract-only", action="store_true")
    ap.add_argument("--reuse-extraction", action="store_true", help="Reuse cached source blocks after rechecking every PDF SHA-256")
    args = ap.parse_args()
    if args.reuse_extraction:
        records = json.loads((OUT / "source_blocks.json").read_text(encoding="utf-8"))
        inventory = json.loads((REF / "papers.json").read_text(encoding="utf-8"))
        if {(p["paper"], p["filename"], p["sha256"]) for p in records} != {(p["paper"], p["filename"], p["sha256"]) for p in inventory}:
            raise ValueError("Cached source inventory differs; re-extract and reconcile")
        for p in records:
            if hashlib.sha256((args.pdf_dir / p["filename"]).read_bytes()).hexdigest() != p["sha256"]:
                raise ValueError(f"Cached source changed: {p['paper']}")
    else:
        records = extract(args.pdf_dir)
    if not args.extract_only:
        publish(records)
    print(f"Extracted {len(records)} exact-source PDFs to {OUT}")


if __name__ == "__main__":
    main()
