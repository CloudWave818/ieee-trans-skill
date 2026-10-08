# ieee-trans-skill

A portable Codex skill for source-matched IEEE Transactions and Letter papers in UAV autonomy, robotics, planning, reinforcement learning, multi-agent decision making and control.

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

只想规划真实实验、不直接画图时，可这样调用：

```text
使用 $ieee-trans-skill。我的手稿/研究方案在：[路径]。
请根据论文主张和29篇真实实验范本，给一份完整的真实实验场景与展示说明。
写清室内还是室外、障碍物有无及具体位置、几架无人机怎样飞、关键阶段、从哪里拍，
用几张图、算法怎么分面、轨迹/叠影/透明度怎么呈现、单栏或跨栏及最终毫米宽高。
场景要有真实实验摄影观感：展开地面/建筑/植被材质、光照阴影、镜头透视和无人机尺度。
先给我易读说明，再给可直接交给另一模型的完整长提示词，不做摘要式压缩；
关键物体位置、飞行过程、叠影和排版全部写入复制块，已有事实与拟议条件分开。
这次只写说明，不画图。
```

新[场景索引](references/preferred_29/real_world_scenes/INDEX.md)覆盖29篇、74个场景、77个展示记录；已查看89个关键PDF页及附近实验文字。它区分真实飞行、其他实机、录制数据、仿真与渲染，也区分同次飞行叠影、真实多机和多次试验后注册。[专用工作流](workflows/14_REAL_WORLD_SCENE_AND_CAPTURE.md)交付填满的场景说明与自包含提示词，允许明确拟议的场景示意；真实论文证据组装另依赖实际照片/帧与日志。说明完成不等于实验或图片已完成。源记录可用 `python scripts/validate_real_world_scenes.py` 核查。

[写实与完整交接指南](references/preferred_29/real_world_scenes/PHOTOGRAPHIC_HANDOFF.md)分别处理室内、自然绿化和建筑场景，并将摄影底图、时序叠影、数据与文字分层交接。模型提示词按当前场景充分展开，不用“真实/8K”或范本编号替代具体描述；实际画面仍需出图后检查。

方法框架图现在接入用户提供的 [ieee-trans-framework-style 子模块](modules/ieee-trans-framework-style/README.md)，包含原始参考图片、内容提炼规则、节点—连线规格和绘图提示模板。主技能遇到方法框架图、网络/系统结构图或算法总览图时会读取它；实验数据图和实物图仍使用各自规范。可以直接这样请求：

```text
使用 $ieee-trans-skill 的 ieee-trans-framework-style 子模块，
阅读我的方法文字，按其参考图风格绘制方法框架图。
提炼真实输入、核心机制、分支和输出，保持连线准确。
```

子模块也可单独读取 [SKILL.md](modules/ieee-trans-framework-style/SKILL.md) 使用。2026-10-02 已改为先选真实论文原图，再锁定布局、字体、配色、机制小图与连线。历史单张参考图保留为可选范本，不统一覆盖所有图。

全文工作从 [范本匹配流程](workflows/13_REFERENCE_MATCHED_PRODUCTION.md) 开始。已加入 [29 篇稿件指纹](references/preferred_29/manuscript_profiles/INDEX.md)、[写作组织指南](references/preferred_29/MANUSCRIPT_STYLE_PLAYBOOK.md)、[实验与引用指南](references/preferred_29/EVIDENCE_AND_CITATION_PLAYBOOK.md) 和 [8 个原图锚点](references/preferred_29/framework_anchors/INDEX.md)。RA-L/Letter 使用紧凑来源和本地路由；文章形态与预印本页数分开判断。

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
