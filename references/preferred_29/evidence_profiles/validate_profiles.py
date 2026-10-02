"""Validate source identity/page witnesses and optionally render focused evidence cards.

No scientific fact extraction is performed here. profiles.json contains manually
reviewed observations; this checker only tests provenance, coverage, and locators.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from pathlib import Path


def normalized(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).lower()
    value = re.sub(r"-\s*\n\s*", "", value)
    return re.sub(r"\s+", "", value)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path)
    parser.add_argument("--render-cards", action="store_true")
    parser.add_argument("--no-cache", action="store_true", help="Test portable operation using only bundled PDFs")
    args = parser.parse_args()
    here = Path(__file__).resolve().parent
    workspace = args.workspace or here.parents[3]
    skill_root = here.parents[2]
    dataset = json.loads((here / "profiles.json").read_text(encoding="utf-8"))
    papers = json.loads((here.parent / "papers.json").read_text(encoding="utf-8"))
    papers = {p["paper"]: p for p in papers}
    profiles = dataset["profiles"]
    errors: list[str] = []
    ids = [p["paper_id"] for p in profiles]
    if len(ids) != len(set(ids)) or set(ids) != set(papers):
        errors.append("Profile IDs are not a unique, complete match for papers.json")
    witness_count = 0
    page_count = 0
    hash_count = 0
    for profile in profiles:
        pid = profile["paper_id"]
        source = papers[pid]
        pdf = skill_root / "papers" / "preferred_29" / source["filename"]
        if not pdf.is_file():
            errors.append(f"{pid}: missing bundled supplied source PDF {pdf}")
        elif hashlib.sha256(pdf.read_bytes()).hexdigest() != source["sha256"]:
            errors.append(f"{pid}: supplied source SHA256 does not match papers.json")
        else:
            hash_count += 1
        cache = workspace / "USER_PREFERRED_VISUAL_LIBRARY" / "source_pages" / pid
        document = None
        def page_text(page: int) -> str | None:
            nonlocal document
            cached_page = cache / f"p{page:02}.txt"
            if not args.no_cache and cached_page.is_file():
                return cached_page.read_text(encoding="utf-8")
            if not pdf.is_file():
                return None
            if document is None:
                try:
                    import pymupdf
                    document = pymupdf.open(pdf)
                except ImportError:
                    try:
                        from pypdf import PdfReader
                        document = PdfReader(pdf)
                    except ImportError as exc:
                        raise RuntimeError("Raw PDF validation requires PyMuPDF or pypdf when optional cache is unavailable") from exc
            if hasattr(document, "load_page"):
                return document.load_page(page - 1).get_text("text")
            return document.pages[page - 1].extract_text()
        for page in sorted(set(profile["evidence_pages"] + profile["reference_pages"])):
            if not 1 <= page <= source["pdf_pages"]:
                errors.append(f"{pid}: invalid one-based PDF page {page}")
            if page_text(page) is None:
                errors.append(f"{pid}: cannot read PDF page {page}")
            else:
                page_count += 1
        for page in profile["visual_reviewed_pages"]:
            if not 1 <= page <= source["pdf_pages"]:
                errors.append(f"{pid}: invalid visually reviewed PDF page {page}")
        for anchor in profile["verification_anchors"]:
            witness_text = page_text(anchor["page"])
            if witness_text and normalized(anchor["text"]) in normalized(witness_text):
                witness_count += 1
            else:
                errors.append(f"{pid} p{anchor['page']}: source witness not found: {anchor['text']!r}")
        if args.render_cards:
            render_card(here, profile, source)
        if hasattr(document, "close"):
            document.close()
    if args.render_cards:
        render_index(here, profiles, papers)
    report = {
        "profiles": len(profiles), "matching_pdf_hashes": hash_count,
        "valid_page_text_locators": page_count, "matching_source_witnesses": witness_count,
        "visually_reviewed_pages": sum(len(p["visual_reviewed_pages"]) for p in profiles),
        "errors": errors,
        "limits": "Checks prove source identity/locators, not correctness of every interpretation. Metrics and baseline descriptions remain manual observations, with transfer boundaries recorded per paper."
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return bool(errors)


def render_card(here: Path, profile: dict, source: dict) -> None:
    pid = profile["paper_id"]
    pdf_link = "../../../papers/preferred_29/" + source["filename"]
    lines = [f"# {pid} — {source['title']}", "", "**Status:** SOURCE_OBSERVATION; supplied PDF version, not final-venue validation.", "",
             f"Source: [{source['filename']}]({pdf_link}); SHA256 `{source['sha256']}`.", "",
             f"Article form: `{profile['article_form']}`. Method families: " + ", ".join(f"`{m}`" for m in profile["method_family"]) + ".", "",
             "Experiment/result page locators: " + ", ".join(f"[PDF p.{p}]({pdf_link}#page={p})" for p in profile["evidence_pages"]) + ".", ""]
    labels = [
        ("experiment_order", "Observed evidence order"),
        ("baseline_groups", "Actual comparison roles"),
        ("metrics", "Actual metrics and aggregation"),
        ("controls_and_sampling", "Controls and sampling"),
        ("mechanism_and_stress_tests", "Mechanism and stress tests"),
        ("compute_and_physical_evidence", "Compute and physical evidence"),
        ("presentation_inheritance", "Presentation to inherit"),
        ("transfer_boundary", "Do not generalize"),
        ("citation_profile", "Citation and bibliography observations")
    ]
    for field, label in labels:
        lines.extend([f"## {label}", ""])
        content = profile[field]
        if isinstance(content, list):
            lines.extend(f"- {item}" for item in content)
        else:
            lines.append(content)
        lines.append("")
    lines.extend(["## Review limits", "", "PDF page numbers are one-based file pages. Text was read for the evidence narrative; every small axis and statistic was not independently remeasured. Unlocated details are unknown, not absence. Citation metadata has not been externally verified.", "",
                  "Reference pages: " + ", ".join(str(p) for p in profile["reference_pages"]) + ".",
                  "Rendered pages inspected in this evidence pass: " + (", ".join(str(p) for p in profile["visual_reviewed_pages"]) or "none; text/context only") + ".", "",
                  "The source PDF is bundled with the skill. The workspace's `USER_PREFERRED_VISUAL_LIBRARY` text/images were an optional review cache; the portable card does not depend on it.", "",
                  "This card is generated from `profiles.json`; maintain observations there and rerun `validate_profiles.py --render-cards`.", ""])
    (here / f"{pid}.md").write_text("\n".join(lines), encoding="utf-8")


def render_index(here: Path, profiles: list[dict], papers: dict) -> None:
    lines = ["# Evidence profiles for all 29 supplied papers", "", "Read the closest method/form card, then [EVIDENCE_AND_CITATION_PLAYBOOK.md](../EVIDENCE_AND_CITATION_PLAYBOOK.md). Selective loading is expected; do not load all cards for one manuscript.", "",
             "Each card contains actual experiment order, comparison roles, metric definitions, controls, stress tests, hardware/physical scope, table/caption inheritance and transfer limits. Page numbers refer to the supplied PDF file. These are observations, not official venue rules.", "",
             "| Card | Form | Method | Experiment pages |", "|---|---|---|---|"]
    for p in profiles:
        pid = p["paper_id"]
        lines.append(f"| [{pid} — {papers[pid]['title']}]({pid}.md) | {p['article_form']} | {', '.join(p['method_family'])} | {', '.join(str(x) for x in p['evidence_pages'])} |")
    lines.extend(["", "Canonical machine-readable file: [profiles.json](profiles.json), schema 1.0, root key `profiles`; join `paper_id` to `papers.json` field `paper` for title/source SHA256.", "",
                  "Validation: `python validate_profiles.py --render-cards`; add `--no-cache` to verify using only bundled PDFs (requires PyMuPDF or pypdf). `--workspace <root>` optionally selects an existing review cache. Checks cover source hashes, PDF-page locators and short source witnesses; they do not certify scientific correctness or final publication metadata.", ""])
    (here / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    raise SystemExit(main())
