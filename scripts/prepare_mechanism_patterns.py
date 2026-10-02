#!/usr/bin/env python3
"""Render reference mechanism patches directly from hash-verified bundled PDFs.

These PNGs are source-study material. They are never original-method drawings or
new experimental evidence. Requires PyMuPDF and Pillow; paths stay skill-relative.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import pymupdf as fitz
from PIL import Image, ImageChops, ImageDraw, ImageFont


LIBRARY = Path("references/preferred_29/mechanism_patterns")
ANCHORS = Path("references/preferred_29/framework_anchors/anchors.json")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inside(inner: list[float], outer: list[float]) -> bool:
    return (len(inner) == 4 and all(math.isfinite(x) for x in inner)
            and inner[0] < inner[2] and inner[1] < inner[3]
            and outer[0] <= inner[0] and outer[1] <= inner[1]
            and inner[2] <= outer[2] and inner[3] <= outer[3])


def load_recipe(root: Path, require_visual: bool = False) -> tuple[dict, dict]:
    recipe = json.loads((root / LIBRARY / "recipes.json").read_text(encoding="utf-8"))
    anchors = json.loads((root / ANCHORS).read_text(encoding="utf-8"))
    anchor_map = {a["anchor_id"]: a for a in anchors}
    assert len(anchor_map) == len(anchors), "Duplicate source anchor id"
    ids = [p["id"] for p in recipe["patterns"]]
    assert len(set(ids)) == len(ids), "Duplicate mechanism pattern id"
    for p in recipe["patterns"]:
        assert p["anchor"] in anchor_map, f"Unknown anchor: {p['anchor']}"
        a = anchor_map[p["anchor"]]
        assert inside(p["bbox_pt"], a["crop_bbox_pt"]), f"Crop exceeds source anchor: {p['id']}"
        assert set(p["source_zones"]) <= {z["id"] for z in a["zones"]}, f"Unknown zone: {p['id']}"
        assert p["new_method_must_provide"] and p["redraw_steps"] and p["transfer_boundary"]
        assert p["visual_review"] in {"Pending", "Viewed"}, f"Unknown visual-review status: {p['id']}"
        if require_visual:
            assert p["visual_review"] == "Viewed", f"Visual inspection pending: {p['id']}"
    return recipe, anchor_map


def require_source(root: Path, a: dict) -> Path:
    source = root / a["source_pdf"]
    assert source.is_file(), f"Missing source PDF: {source}"
    assert sha(source) == a["source_sha256"], f"Source hash mismatch: {a['anchor_id']}"
    return source


def require_nonempty(path: Path) -> tuple[int, int]:
    with Image.open(path) as im:
        im = im.convert("RGB")
        assert im.width > 100 and im.height > 100, f"Crop unexpectedly small: {path}"
        assert ImageChops.difference(im, Image.new("RGB", im.size, "white")).getbbox(), f"Blank crop: {path}"
        return im.size


def contact_sheet(out: Path, patterns: list[dict]) -> None:
    cols, cell_w, cell_h = 3, 800, 510
    canvas = Image.new("RGB", (cols * cell_w, math.ceil(len(patterns) / cols) * cell_h), "white")
    draw = ImageDraw.Draw(canvas)
    try:
        font = ImageFont.truetype("arial.ttf", 25)
    except OSError:
        font = ImageFont.load_default(size=25)
    for i, p in enumerate(patterns):
        x, y = (i % cols) * cell_w, (i // cols) * cell_h
        draw.text((x + 20, y + 12), p["id"], fill="#1A1A1A", font=font)
        draw.text((x + 20, y + 45), f"{p['anchor']} / PDF p{p['page']} / SOURCE PATCH", fill="#555555", font=font)
        with Image.open(out / "crops" / f"{p['id']}.png") as source:
            im = source.convert("RGB")
        im.thumbnail((cell_w - 40, cell_h - 105), Image.Resampling.LANCZOS)
        canvas.paste(im, (x + (cell_w - im.width) // 2, y + 90 + (cell_h - 105 - im.height) // 2))
        draw.line([(x + 10, y + cell_h - 4), (x + cell_w - 10, y + cell_h - 4)], fill="#DDDDDD", width=1)
    canvas.save(out / "contact_sheet.png")


def index_text(patterns: list[dict], selection_review: dict) -> str:
    count = len(patterns)
    papers = len({p["source_pdf"] for p in patterns})
    anchor_count = len({p["anchor"] for p in patterns})
    review_count = len(selection_review["viewed_source_anchors"])
    lines = ["# 机制小图原型：从真实原图学习如何表达中间量", "",
             f"本库的 {count} 个局部直接渲染自 {papers} 篇论文、{anchor_count} 个主锚点。它补充整体布局锚点，重点研究卡片内的科学信息、接口和线型。它没有穷尽 29 篇论文或全部 281 个图例。", "",
             f"抽样记录：{selection_review['date']} 的本次选择实际查看了 {review_count} 个原图锚点（完整清单见 manifest 的 selection_review）。此记录不代表未来新增条目已经查看。", "",
             "**这些是原图局部学习材料，不是可以直接贴入新论文的素材，也不是新方法结果。** 外观相似来自正确的表达对象与关系，不能靠重复曲线、填满空卡片或添加不存在的算法。源图中的数字、公式、网络、地图、硬件、功能和实验快照均属于源论文。", "",
             "先选整图主范本，再按当前研究的真实机制选择至多几个局部原型。每个局部须说明哪些输入资料已具备、哪些缺失；缺失的科学定义不要用源内容补齐。实验快照必须用作者的数据与平台输出，方案示意应明示其性质。", "",
             f"![{count} 个原图局部联系表](contact_sheet.png)", "",
             "| 编号 | 要表达的作用 | 适用条件 | 来源 |", "|---|---|---|---|"]
    for p in patterns:
        lines.append(f"| [{p['id']}](#{p['id']}) | {p['title']} | {p['applicable_when']} | [{p['anchor']}，PDF p{p['page']}](../../../{p['source_pdf']}#page={p['page']}) |")
    for p in patterns:
        lines.extend(["", f"<a id=\"{p['id']}\"></a>", f"## {p['id']} · {p['title']}", "", p["role"], "",
                      f"适用条件：{p['applicable_when']}", "", f"![{p['id']} 原图局部](crops/{p['id']}.png)", "",
                      "新方法必须提供：" + "；".join(p["new_method_must_provide"]) + "。", "", "重画步骤：", ""])
        lines.extend(f"{i}. {step}" for i, step in enumerate(p["redraw_steps"], 1))
        lines.extend(["", f"迁移边界：{p['transfer_boundary']}", "",
                      f"来源：`{p['anchor']}`，PDF p{p['page']}；裁框（左上原点 PDF pt）`{p['bbox_pt']}`。哈希、路径和渲染信息见 `manifest.json`。", ""])
    lines.extend(["## 更新与核验", "",
                  "配方保存在 `recipes.json`。对照真实 PDF 和原图锚点调整边界后重新生成；裁框必须位于所记录锚点内。先检查每幅独立裁图的标签、外围上下文和接口，再将 `visual_review` 记为 `Viewed`。", "",
                  "```powershell", "python scripts/prepare_mechanism_patterns.py", "python scripts/prepare_mechanism_patterns.py --check", "```", "",
                  "核验包括：唯一编号、源 PDF 哈希与页码、锚点内边界、已知 zone、裁图大小/非空、配方一致性及 PNG 哈希。`--check` 不生成或修改文件。已实际查看裁图只确认裁边和来源，不证明新图的科学内容或外观质量。", ""])
    return "\n".join(lines)


def prepare(root: Path, recipe: dict, anchors: dict) -> None:
    out = root / LIBRARY
    (out / "crops").mkdir(parents=True, exist_ok=True)
    patterns = []
    for p in recipe["patterns"]:
        a = anchors[p["anchor"]]
        source = require_source(root, a)
        path = out / "crops" / f"{p['id']}.png"
        with fitz.open(source) as doc:
            assert 1 <= a["pdf_page"] <= len(doc), f"Invalid source page: {p['id']}"
            page = doc[a["pdf_page"] - 1]
            assert inside(p["bbox_pt"], list(page.rect)), f"Crop exceeds page: {p['id']}"
            pix = page.get_pixmap(clip=fitz.Rect(p["bbox_pt"]), dpi=recipe["render_dpi"], alpha=False)
            pix.save(path)
        pixels = require_nonempty(path)
        m = dict(p)
        m.update(source_pdf=a["source_pdf"], sha256=a["source_sha256"], page=a["pdf_page"],
                 source_anchor_bbox_pt=a["crop_bbox_pt"], render_dpi=recipe["render_dpi"],
                 crop_path=str(LIBRARY / "crops" / path.name).replace("\\", "/"),
                 crop_pixels=list(pixels), crop_sha=sha(path), artifact_kind="SOURCE_FAITHFUL_MECHANISM_PATCH")
        patterns.append(m)
    contact_sheet(out, patterns)
    manifest = dict(schema_version=1, artifact_kind="SOURCE_FAITHFUL_MECHANISM_PATCHES", patterns=patterns,
                    selection_review=recipe["selection_review"],
                    contact_sheet_path=str(LIBRARY / "contact_sheet.png").replace("\\", "/"),
                    contact_sheet_sha=sha(out / "contact_sheet.png"),
                    coverage=f"{len(patterns)} selected source patches from {len({p['source_pdf'] for p in patterns})} papers and {len({p['anchor'] for p in patterns})} anchors; not exhaustive")
    (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out / "INDEX.md").write_text(index_text(patterns, recipe["selection_review"]), encoding="utf-8")
    print(f"Prepared {len(patterns)} source patches directly from verified PDFs.")


def check(root: Path, recipe: dict, anchors: dict) -> None:
    out = root / LIBRARY
    manifest = json.loads((out / "manifest.json").read_text(encoding="utf-8"))
    entries = manifest["patterns"]
    actual = {p["id"]: p for p in entries}
    assert len(actual) == len(entries), "Duplicate manifest id"
    assert set(actual) == {p["id"] for p in recipe["patterns"]}, "Recipe/manifest ids differ"
    for p in recipe["patterns"]:
        m = actual[p["id"]]
        a = anchors[p["anchor"]]
        require_source(root, a)
        for key, value in p.items():
            assert m[key] == value, f"Stale recipe field {key}: {p['id']}"
        assert m["sha256"] == a["source_sha256"] and m["source_pdf"] == a["source_pdf"]
        assert m["page"] == a["pdf_page"] and m["source_anchor_bbox_pt"] == a["crop_bbox_pt"]
        with fitz.open(root / a["source_pdf"]) as doc:
            assert 1 <= m["page"] <= len(doc)
            assert inside(m["bbox_pt"], list(doc[m["page"] - 1].rect))
        path = root / m["crop_path"]
        assert path.resolve() == (out / "crops" / f"{p['id']}.png").resolve(), "Unexpected crop path"
        assert list(require_nonempty(path)) == m["crop_pixels"]
        assert sha(path) == m["crop_sha"], f"Crop hash mismatch: {p['id']}"
        assert m["render_dpi"] == recipe["render_dpi"]
    assert sha(root / manifest["contact_sheet_path"]) == manifest["contact_sheet_sha"], "Contact sheet hash mismatch"
    assert manifest["selection_review"] == recipe["selection_review"], "Selection-review metadata is stale"
    assert (out / "INDEX.md").read_text(encoding="utf-8") == index_text(entries, recipe["selection_review"]), "Index is stale"
    print(f"PASS: {len(entries)} source hashes, page locators, anchor bounds, nonempty crops, unique ids and crop hashes.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    recipe, anchors = load_recipe(root, require_visual=args.check)
    if args.check:
        check(root, recipe, anchors)
    else:
        prepare(root, recipe, anchors)


if __name__ == "__main__":
    main()
