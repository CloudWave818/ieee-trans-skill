#!/usr/bin/env python3
"""Prepare source-faithful framework crops and measured cards from preferred PDFs.

Requires PyMuPDF and Pillow. Reads the maintained recipes, verifies original PDF
hashes against cases.json, and renders crops directly; no source graphic is
recreated or styled by this script. All paths recorded in the manifest are
relative to the skill root so the library remains portable.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import statistics
from pathlib import Path

import pymupdf as fitz
from PIL import Image, ImageDraw, ImageFont


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalized(box: list[float], crop: list[float]) -> list[float]:
    w, h = crop[2] - crop[0], crop[3] - crop[1]
    return [round((box[0] - crop[0]) / w, 5), round((box[1] - crop[1]) / h, 5),
            round((box[2] - crop[0]) / w, 5), round((box[3] - crop[1]) / h, 5)]


def sample_rgb(im: Image.Image, point: list[float], crop: list[float], dpi: int) -> list[int]:
    x = round((point[0] - crop[0]) * dpi / 72)
    y = round((point[1] - crop[1]) * dpi / 72)
    pixels = [im.getpixel((xx, yy))[:3]
              for xx in range(max(0, x - 2), min(im.width, x + 3))
              for yy in range(max(0, y - 2), min(im.height, y + 3))]
    if not pixels:
        raise ValueError(f"Color probe is outside crop: {point}")
    return [int(statistics.median(p[c] for p in pixels)) for c in range(3)]


def card_text(a: dict) -> str:
    lines = [f"# {a['anchor_id']} — 原图外观锚点", "",
             f"**{a['title']}**", "",
             f"- 原 PDF：[{a['filename']}](../../../{a['source_pdf']}#page={a['pdf_page']})；Fig. {a['figure']}；PDF 第 {a['pdf_page']} 页（1-based）。",
             f"- SHA256：`{a['source_sha256']}`。",
             f"- 本图：**SOURCE_FAITHFUL_CROP**，直接裁自原 PDF，不是重绘、AI 生成图或旧布局草图。",
             f"- 裁框（PDF pt，左上原点）：`{a['crop_bbox_pt']}`；宽高比 `{a['aspect_ratio']}`；{a['render_dpi']} dpi；{a['crop_pixels'][0]}×{a['crop_pixels'][1]} px。",
             f"- 测量依据：{a['geometry_evidence']}", "",
             f"![{a['anchor_id']} actual source crop](crops/{a['anchor_id']}.png)", "",
             "## 选择与外观特征", "", f"家族：`{a['family']}`。", ""]
    lines += [f"- {x}" for x in a["distinctive_features"]]
    lines += ["", "## 分区与几何", "",
              "坐标为相对当前裁图的归一化 `[x0,y0,x1,y1]`。它描述外观，不强制新方法具有源论文的模块。", "",
              "| 区域 | 父区域 | 归一化边界 | 原图形状 |", "|---|---|---|---|"]
    lines += [f"| {z['id']} ({z['role']}) | {z.get('parent') or '—'} | `{z['bbox_normalized']}` | {z['shape']} |" for z in a["zones"]]
    lines += ["", "## 配色、字体与线条", "",
              "颜色样本是该 PDF 以所列分辨率渲染后的 RGB 近似；包含色彩管理、透明叠色和抗锯齿影响。vector_rgb/opacity 是 PDF 图形中的数值，不能把原始 fill 直接当最终显示色。", "",
              "| 部位 | 渲染样本 | 源 fill / opacity（若可取得） | 证据 |", "|---|---|---|---|"]
    for p in a["palette_probes"]:
        raw = f"`{p['vector_hex']}` / {p.get('opacity', 1)}" if "vector_hex" in p else "raster / 不可反推源颜色"
        lines.append(f"| {p['name']} | `{p['rendered_hex']}` | {raw} | {p['evidence']} |")
    t = a["typography"]
    lines += ["", f"字体证据：{t['status']}。{t['observed']}", "", t["transfer"]]
    if a.get("stroke_grammar"):
        lines += ["", f"源图线条参数：`{json.dumps(a['stroke_grammar'], ensure_ascii=False)}`。"]
    lines += ["", "## 连线与机制小图", "", a["arrows"]["grammar"], "", a["arrows"]["routing"], "",
              a["arrows"]["source_labels"], "", f"源图小图：{a['pictograms']['source_content']}", "", a["pictograms"]["transfer"],
              "", "## 可迁移边界与失败模式", "", a["transfer_boundary"], "", f"避免：{a['failure_to_avoid']}", "",
              "## 使用时的视觉核验", "",
              "同时打开本原图裁图和新稿渲染。先对照整体比例/分区占比，再对照嵌套层级、模块形状、颜色透明度、字体层级、机制小图和箭头语法。旧 sketches/*.svg 仅是结构分析草图，不参与原图外观验收。", "",
              "新稿需保留可编辑文字与矢量模块；源图裁图是参考材料，不能作为冒充原创方法图或实验结果的输出。", ""]
    return "\n".join(lines)


def contact_sheet(out: Path, anchors: list[dict]) -> Path:
    width, cell_w, cell_h = 1440, 720, 440
    rows = (len(anchors) + 1) // 2
    canvas = Image.new("RGB", (width, rows * cell_h), "white")
    draw = ImageDraw.Draw(canvas)
    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except OSError:
        font = ImageFont.load_default(size=22)
    for i, a in enumerate(anchors):
        col, row = i % 2, i // 2
        ox, oy = col * cell_w, row * cell_h
        draw.text((ox + 20, oy + 12), f"{a['anchor_id']}  |  actual PDF crop", fill="black", font=font)
        im = Image.open(out / "crops" / f"{a['anchor_id']}.png").convert("RGB")
        im.thumbnail((cell_w - 40, cell_h - 65), Image.Resampling.LANCZOS)
        canvas.paste(im, (ox + (cell_w - im.width) // 2, oy + 55 + (cell_h - 65 - im.height) // 2))
    path = out / "CONTACT_SHEET.png"
    canvas.save(path)
    return path


def prepare(root: Path, dpi: int) -> None:
    out = root / "references/preferred_29/framework_anchors"
    recipes = json.loads((out / "anchor_recipes.json").read_text(encoding="utf-8"))
    cases = {x["case_id"]: x for x in json.loads((root / "references/preferred_29/cases.json").read_text(encoding="utf-8"))}
    (out / "crops").mkdir(parents=True, exist_ok=True)
    anchors = []
    for recipe in recipes["anchors"]:
        a = dict(recipe)
        case = cases[a["case_id"]]
        pdf = root / case["source_pdf"]
        if digest(pdf) != case["source_sha256"]:
            raise ValueError(f"Source hash mismatch: {a['anchor_id']}")
        a.update({k: case[k] for k in ["source_pdf", "source_sha256", "pdf_page", "filename", "title", "figure"]})
        a["artifact_kind"] = "SOURCE_FAITHFUL_CROP"
        a["coordinate_system"] = recipes["coordinate_system"]
        crop = a["crop_bbox_pt"]
        with fitz.open(pdf) as doc:
            page = doc[a["pdf_page"] - 1]
            rect = fitz.Rect(crop)
            if not page.rect.contains(rect) or rect.width <= 0 or rect.height <= 0:
                raise ValueError(f"Invalid crop: {a['anchor_id']}")
            path = out / "crops" / f"{a['anchor_id']}.png"
            page.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72), clip=rect,
                            colorspace=fitz.csRGB, alpha=False).save(path)
        im = Image.open(path).convert("RGB")
        a["render_dpi"] = dpi
        a["crop_pixels"] = list(im.size)
        a["aspect_ratio"] = round(rect.width / rect.height, 5)
        a["crop_path"] = path.relative_to(root).as_posix()
        a["crop_sha256"] = digest(path)
        a["card_path"] = (out / f"{a['anchor_id']}.md").relative_to(root).as_posix()
        for zone in a["zones"]:
            zone["bbox_normalized"] = normalized(zone["bbox_pt"], crop)
        for probe in a["palette_probes"]:
            probe["rendered_rgb"] = sample_rgb(im, probe["point_pt"], crop, dpi)
            probe["rendered_hex"] = "#" + "".join(f"{v:02X}" for v in probe["rendered_rgb"])
            if "vector_rgb" in probe:
                probe["vector_hex"] = "#" + "".join(f"{round(v * 255):02X}" for v in probe["vector_rgb"])
        (out / f"{a['anchor_id']}.md").write_text(card_text(a), encoding="utf-8")
        anchors.append(a)
    (out / "anchors.json").write_text(json.dumps(anchors, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    contact_sheet(out, anchors)
    index = ["# Preferred framework appearance anchors", "",
             "本库保存真实 PDF 框架图裁图及量化外观卡。旧 `sketches/*.svg` 是结构分析草图，不能充当外观范本。", "",
             "选择匹配方法复杂度和表现语法的一个主锚点，最多一个辅助锚点。先看原图裁图，后写视觉规范；不用六类风格混合成通用流程图。", "",
             "![Actual framework contact sheet](CONTACT_SHEET.png)", "",
             "| Anchor | Family | Ratio | Actual source |", "|---|---|---:|---|"]
    related = []
    if (out / "SELECTION_AND_CRITIQUE.md").is_file():
        related.append("[原图区别、优势与选型诊断](SELECTION_AND_CRITIQUE.md)")
    if (root / "references/preferred_29/mechanism_patterns/INDEX.md").is_file():
        related.append("[局部机制画法原型](../mechanism_patterns/INDEX.md)")
    if related:
        index[6:6] = ["；".join(related), ""]
    index += [f"| [{a['anchor_id']}]({a['anchor_id']}.md) | {a['family']} | {a['aspect_ratio']:.2f} | [{a['filename']}](../../../{a['source_pdf']}#page={a['pdf_page']}) Fig. {a['figure']}, PDF p. {a['pdf_page']} |" for a in anchors]
    index += ["", "## 复现与核验", "",
              "`python scripts/prepare_framework_anchors.py --skill-root .` 从 hash 匹配的原 PDF 重建 300 dpi 裁图、配色采样、坐标归一化和卡片。", "",
              "`python scripts/prepare_framework_anchors.py --skill-root . --check` 验证来源 hash、裁框、图片 hash/尺寸、非空性、区域坐标与图注排除。", "",
              "JSON 只给测量过的外观规范；没有宣称这些论文共用某个唯一 IEEE 风格。R29 为 Nature Communications 图例，完整竖图与 software 子图须区别使用。", "",
              "颜色为渲染近似值；字体分为 PDF 文本可提取与 raster/outlined 视觉观察；内部 raster 边界保留测量容差。", ""]
    (out / "INDEX.md").write_text("\n".join(index), encoding="utf-8")
    validate(root)


def validate(root: Path) -> None:
    out = root / "references/preferred_29/framework_anchors"
    anchors = json.loads((out / "anchors.json").read_text(encoding="utf-8"))
    if len({a["anchor_id"] for a in anchors}) != len(anchors):
        raise ValueError("Duplicate anchor ids")
    for a in anchors:
        if digest(root / a["source_pdf"]) != a["source_sha256"]:
            raise ValueError(f"Source hash mismatch: {a['anchor_id']}")
        path = root / a["crop_path"]
        if digest(path) != a["crop_sha256"]:
            raise ValueError(f"Crop hash mismatch: {a['anchor_id']}")
        if not (root / a["card_path"]).exists():
            raise ValueError(f"Missing card: {a['anchor_id']}")
        crop = a["crop_bbox_pt"]
        if a.get("caption_start_y_pt") and crop[3] >= a["caption_start_y_pt"]:
            raise ValueError(f"Caption overlaps crop: {a['anchor_id']}")
        im = Image.open(path).convert("RGB")
        if list(im.size) != a["crop_pixels"]:
            raise ValueError(f"Crop size mismatch: {a['anchor_id']}")
        colors = im.resize((128, 128)).getcolors(maxcolors=16384) or []
        if len(colors) < 25 or max(count for count, _ in colors) > 16300:
            raise ValueError(f"Blank or almost blank crop: {a['anchor_id']}")
        for zone in a["zones"]:
            box = zone["bbox_normalized"]
            if not (0 <= box[0] < box[2] <= 1 and 0 <= box[1] < box[3] <= 1):
                raise ValueError(f"Zone outside crop: {a['anchor_id']}/{zone['id']}")
            if normalized(zone["bbox_pt"], crop) != box:
                raise ValueError(f"Incorrect normalized box: {a['anchor_id']}/{zone['id']}")
        with fitz.open(root / a["source_pdf"]) as doc:
            if not doc[a["pdf_page"] - 1].rect.contains(fitz.Rect(crop)):
                raise ValueError(f"Crop outside PDF: {a['anchor_id']}")
    print(f"PASS: {len(anchors)} source-faithful anchors; original hashes, crops, coordinate measurements and cards verified.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--dpi", type=int, default=300)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.dpi < 72:
        parser.error("--dpi must be at least 72")
    if args.check:
        validate(args.skill_root.resolve())
    else:
        prepare(args.skill_root.resolve(), args.dpi)


if __name__ == "__main__":
    main()
