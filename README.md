# ieee-trans-skill

A portable Codex skill for planning, drafting, auditing, and revising long-form IEEE Transactions manuscripts in UAV autonomy, robotics, navigation and planning, trajectory optimization, reinforcement learning, multi-agent decision making, and control.

The repository contains the skill, its derived Knowledge and Exemplar resources, and the **29 user-preferred source PDFs** in [papers/preferred_29](papers/preferred_29). These PDFs total about 249 MiB and match the versions used in the figure-reading records. The older 120-paper corpus remains separate.

## 中文快速使用

本技能可根据论文、方法思路或题目，规划完整图组，生成可绘制的机制/场景图，并为数据尚缺的结果图提供布局和详细执行说明。无人机作图优先采用用户选定的 29 篇范本；学习记录、风格规则、布局草图以及这 29 篇原始 PDF 均随仓库分发。图例卡片可直接打开原 PDF，页面图片和提取文本可在需要时重新生成。

安装后，在 Codex 中明确调用：

```text
使用 $ieee-trans-skill。
我的论文/材料在：[文件路径]；或我的题目/思路是：[内容]。
请优先模仿 preferred_29 中相关范本，规划并制作整套论文图片。
交付图组清单、PAPER_FIGURE_DESCRIPTION.md、可以实际生成的图和可编辑文件/代码。
缺数据的图给布局草图与采集字段；只有题目时明确设计假设，不编造结果。
```

只需一张图时说明图的任务，例如“只设计方法框图，写清策略动作、训练/部署边界和安全过滤器接口”。更完整的用例见 [题目驱动示例](examples/preferred_uav_rl/PAPER_FIGURE_DESCRIPTION.md)，范本入口见 [29 篇图例索引](references/preferred_29/INDEX.md)。

未安装也可在本地任务中要求 Codex 读取本仓库的 `SKILL.md` 并按其中流程执行。网页版使用 [图片规划协议](references/WEB_GPT_FIGURE_PLANNER.md)，随手稿上传；如需重新检查参考原图，还要提供相应 PDF/图页。

## Install on Windows

```powershell
$dest = Join-Path $env:USERPROFILE ".agents\skills\ieee-trans-skill"
New-Item -ItemType Directory -Force -Path (Split-Path -Parent $dest) | Out-Null
git clone https://github.com/CloudWave818/ieee-trans-skill.git $dest
```

Codex detects installed skills automatically; restart if the skill does not appear. Keep the entire repository folder, including references, resources, templates and scripts. Then invoke it explicitly, for example:

```text
Use $ieee-trans-skill to design the claim-evidence architecture for my T-RO paper.
```

## Update

```powershell
$dest = Join-Path $env:USERPROFILE ".agents\skills\ieee-trans-skill"
git -C $dest pull
```

## Verify

```powershell
$dest = Join-Path $env:USERPROFILE ".agents\skills\ieee-trans-skill"
python "$dest\scripts\run_synthetic_tests.py"
```

Expected result: all synthetic routing cases pass.

## Data layout

- `SKILL.md`: skill entry point and operating contract.
- `resources/IEEE_TRANS_KNOWLEDGE`: generalized rules and profiles.
- `resources/IEEE_TRANS_EXEMPLARS`: bounded teaching cards and routing metadata.
- `workflows`, `audits`, and `templates`: task execution assets.
- `scripts`: deterministic router and validation tools.

Preferred source PDFs are in `papers/preferred_29`; see [the source index](papers/preferred_29/README.md) for paper-to-file links. Routine planning can use the derived records; open the PDF for exact visual or text verification. Rendered page images and extracted full text remain local caches rather than duplicate repository assets.

## Visually inspected figure cases

For UAV figure design, start with the **user-preferred 29 papers** in `references/preferred_29/INDEX.md`: 337 PDF pages reviewed, 281 figure-level AI reading records, and 12 detailed key designs with editable SVG layout studies. Read `STYLE_PLAYBOOK.md` for the preferred colors, pictograms, grouping and connectors, and `RL_FIGURE_PLAYBOOK.md` for learning curves, policy interfaces and deployment evidence. Figure-level reading is not full transcription or certification of every axis/statistic. The 29 originals are in `papers/preferred_29`. Rendered images and extracted text remain in the sibling local `USER_PREFERRED_VISUAL_LIBRARY`; its `index.html` pairs source pages with the notes. To recreate that optional gallery, run the following from the repository root (requires PyMuPDF and Poppler `pdftoppm`):

```powershell
python scripts/prepare_preferred_papers.py --source papers/preferred_29 --output ../USER_PREFERRED_VISUAL_LIBRARY/source_pages
python scripts/build_preferred_library.py
```

Rendering does not constitute a new visual review. Existing records retain their review scope and PDF identity checks.

`python scripts/query_visual_cases.py "safety training"` now searches preferred figures first; `--source legacy` accesses the prior collection. A title-only worked example, editable mechanism diagram and empty behavior layout are in `examples/preferred_uav_rl/`. They are provisional design artifacts, not empirical results.

The older supplemental collection has 20 AI-reviewed case groups covering 38 specified figures from 20 A-level papers. Each card separates original observations, caption/body support, limitations, transferable design and collection requirements. This is selected-figure review, not full visual coverage of those papers or the 100-paper corpus.

Start at `references/visual_cases/INDEX.md`. Retrieve with `python scripts/query_visual_cases.py "uncertainty mechanism"`. Source page images and extracted context remain in the separate local `IEEE_TRANS_VISUAL_LIBRARY` folder. Rebuild from local source PDFs with `scripts/prepare_visual_review.py --mapping <CORPUS_MAPPING.csv> --selection references/visual_cases/selection.json --output <local-source-pages>`; this utility requires PyMuPDF and pdftoppm and does not certify review.

Validate the portable records with `python scripts/validate_visual_cases.py`; add `--local-sources` in the original workspace to verify images, context and PDF digests. These checks validate provenance/retrieval, not finished-figure quality. Manuscript-derived designs are allowed with scientific justification even without a matching corpus rule. Actual render/inspection/handoff results are reported separately.
