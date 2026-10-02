# 用户指定 29 篇：稿件风格由具体来源决定

## 先解决现有 skill 的失配

原入口把 RA-L 排除，而用户提供的 R12、R22 的 PDF 明确写出已接受 RA-L。把所有来源先压成“Transactions 通用规范”，会丢掉最需要的紧凑稿节奏。另一个失配是只有图例和摘要卡，没有逐篇章节占比、段落操作、来源位置和版本边界。由此生成的论文可以符合 IEEE 的一般格式，却不像用户选择的这些论文。

使用 [稿件指纹索引](manuscript_profiles/INDEX.md) 和 `manuscript_profiles/profiles.json` 选择来源。每篇都有原始章节位置、自动测量的文本占比、三处人工复核的段落操作、具体组织蓝图和不可迁移项。完整原文块及几何位于 `manuscript_profiles/source_blocks.json`，p 为 PDF 物理页码（1 起），b 为该页提取块索引（0 起）。读样本时务必使用文件 SHA-256 对应的本地 PDF。

## 两个字段不能混为一谈

定位中的 `b` 精确指 `source_blocks.json` 该页 `blocks` 列表的零起索引：提取器使用 `get_text('dict')`，过滤图像块并保持原顺序。其他 API 或 `sort=True` 的 fresh 提取可能重新分块/排序，不能按其新编号判断原定位错误。先用归档块的文字、bbox 与 PDF 页核对；更换提取版本或重建后若块内容改变，重新审阅该定位。

- `article_form` 是发表形式和出处证据。R12/R22 为 PDF 明示的 Letter；R03 为 PDF 明示的 IROS 2022；R29 为出版社明示的 Nature Communications Article。R04/R05 为官方 arXiv 作者 metadata 的 Transactions 接受声明，R14 为提交 T-RO 声明，不能把 submitted 改成 accepted。R10 只证实 accepted journal dates，未识别具体刊名。其余没有明示出处的保留 UNVERIFIED。
- `morphology` 是这份文件的可见稿件组织：IEEE_COMPACT、IEEE_EXTENDED、SINGLE_COLUMN_PREPRINT、AUTHOR_YEAR_TWO_COLUMN 或 NATURE_RESULT_LED。它帮助选篇幅与叙述节奏，不证明刊物归属。R09 的 23 页含 15 页补充；R26 的 22 页含参考文献及附录；R28 的 22 页含 14 页左右附录，不能据页数归入 Transactions。

如需报告具体出版社的最新发表信息，另行查官方记录；不要用未经核实的期刊名替换本文的证据状态。取风格时锁定这里的作者 PDF 版本，而不是网页上的后续版本。

## 每个新稿先固定一个主稿件来源

写作前产生一个短的 `MANUSCRIPT_STYLE_CONTRACT`，嵌入当前已有蓝图文件即可，无需另外制造流程文档：

```yaml
article_form: LETTER | TRANSACTIONS | CONFERENCE | UNDECIDED
primary_manuscript_donor: Rxx
primary_donor_pdf_sha256: exact hash
form_donor: R12 | R22 | R04 | R05 | none
mechanism_donor: Rxx | none
visual_donor_cases: [actual case ids]
preserve:
  - source section functions and order
  - source relative emphasis, adapted to available evidence
  - selected paragraph moves at exact p/b locators
adapt:
  - module names, method dependencies, task and symbols from project
  - experiments, reference list and all numerical claims from project
excluded:
  - source technical results, unsupported theory and unavailable hardware
```

主来源决定稿件骨架；形式来源只校准 Letter/Transactions 的讲解颗粒度；机制来源补一处需要的接口叙述。不要把三个骨架平均成一份模板。若项目只有研究方案，来源告诉你需要哪些证据，把未完成实验保留为设计；它不能替你生成结果。

选择首先看机制和证据链，再看形式。一个有完整机构设计与操作验证的稿子应看 R16/R29，不能因含控制器就强套 R20 的纯策略方法大节。有学习模块的 R05/R12 是高层决策，R15/R20/R23/R25 是直接或视觉策略；R22 监督估计、R24/R26/R28 零样本推理和 R27 扩散规划不会因为“有网络”而变成 RL 写作。

## 可以直接选择的来源组织

| 项目机制 | 优先主来源 | 要保留的章节组织 | 另一来源只补什么 |
|---|---|---|---|
| 层级 RL 配置已有规划器 | [R12](manuscript_profiles/R12.md) | 问题→层级 Framework→外环学习→训练设置→比较/实飞 | R05 补高层决策与轨迹接口；不复制其捕获末端约束 |
| 学习决策与终端约束耦合 | [R05](manuscript_profiles/R05.md) | Problem Statement→决策→初值→终端优化→实验 | R12 补紧凑 Letter 的压缩尺度 |
| 局部编队优化 | [R02](manuscript_profiles/R02.md) | 新度量→优化→Benchmark→实机/模拟 | R04 补仅项目真实拥有的重组织或全局一致性 |
| 完整分布式编队系统 | [R04](manuscript_profiles/R04.md) | Overview→度量→局部求解→重组织→一致性→五种能力 Benchmark→实机 | R21 补数量适应的受控比较边界 |
| 几何空间或走廊创新 | [R03](manuscript_profiles/R03.md)、[R17](manuscript_profiles/R17.md)择一 | 前者已有后端预备/新前端，后者表示建图/跨平面轨迹 | 两者图形任务不同，不能合成同一几何故事 |
| 动态跟踪与接触两任务 | [R11](manuscript_profiles/R11.md) | 共享预备→两任务机制→共同优化→模拟细分→实机 | R01/R06 补跟踪事件解读颗粒度 |
| 缆绳负载规划加控制 | [R14](manuscript_profiles/R14.md) | 耦合模型→安全/可行约束→优化→分布式控制→实验 | R05 补紧凑动态任务的约束引出方法 |
| 直接控制 RL | [R20](manuscript_profiles/R20.md)、[R15](manuscript_profiles/R15.md)择一 | 训练策略主导或感知表示主导的 Methodology→Evaluation | R25 补安全训练/部署分工；不是所有稿都要 CBF |
| RGB 跨域视觉策略 | [R23](manuscript_profiles/R23.md) | Training Pipeline→Transfer→消融→差距可视化→真实飞行 | R15 补感知表示受控实验逻辑 |
| 高动态监督估计+MPC | [R22](manuscript_profiles/R22.md) | 短 Formulation→双模块及伪代码→端到端/数据/额外量化/限制 | R10 补多频率接口说明，不引入端边决策问题 |
| 图结构建图与优化 | [R18](manuscript_profiles/R18.md) | Overview→前处理→BA→同类PGO合节→七种研究→证明附录 | R08 补推导路线的段首导航 |
| 零样本语义导航/协作 | [R24](manuscript_profiles/R24.md)、[R26](manuscript_profiles/R26.md)、[R28](manuscript_profiles/R28.md)择一 | 分层表示/视频动作/异构协作各有自己的章节 | 用 R12/R22 校准 Letter；R26/R28 的格式不是 IEEE |
| 可变形或全驱动机构 | [R19](manuscript_profiles/R19.md)、[R16](manuscript_profiles/R16.md)择一 | 形变状态/规划控制或机构设计/控制/物理能力测试 | R29 补大图叙事和任务-曲线配对，Methods 顺序需改回 IEEE |
| 扩散轨迹生成 | [R27](manuscript_profiles/R27.md) | 编码→截断采样→后处理→损失/数据→指标/定量 | R03 补前后端接口叙述；不能改写为 RL |

其他局部任务可用 R07 空地协作消息链、R09 网捕获/运输物理约束、R13 图稀疏的理论条件/规模实验、R21 变数量与窄缝分离评价，按其个别指纹读取。

## R02 与 R04：紧凑稿怎样扩成系统长文

这两篇属于相关研究线，不能作为两次独立出现来统计一条“普遍风格”。它们恰好揭示篇幅变化的原因：

| 位置 | R02 紧凑组织 | R04 扩展组织 | 迁移到新稿的条件 |
|---|---|---|---|
| 总览 | 新图度量之前没有独立大 Overview | System Overview 从 p3 b3 开始，包含平台、分布式局部优化和重组织/一致性接口 | 项目确有多个运行层和部署约束，才给系统总览独立篇幅 |
| 新度量 | p2 b7 一节直接进入定义 | p5 b1 独立描述含定义、度量、位置序列 | 扩展要补不同对象或性质，不能重复同一公式解释 |
| 轨迹优化 | p3 b22，表示/问题两层展开 | p6 b19 后另外给约束转写、代价梯度、解质量讨论 | 有新约束、求解或分析证据才拆子节 |
| 协调 | 以分布式优化为主 | p8 b33 重组织，p10 b12 一致性，均独立成节 | 每新增节对应可说明的系统失效模式 |
| 实验 | p5 b15 Benchmark，然后 p5 b23 实机/仿真 | p11 b11 Benchmark 分适应、预测、弹性、韧性、效率；p15 b13 再部署 | 新的能力维度要与模块和实验一一对应 |
| 收束 | p6 b14 简短结束，p7 文献 | p17 b9 结束，p18 附录与文献 | 长稿附录承载推导，不能以补充材料凑正文篇幅 |

这里不能把 R02 叫成“已证 Letter”，其期刊形式未明示。能确定的是紧凑/扩展的结构关系，以及 R04 官方作者 metadata 的 Transactions 接受声明。

## 已证 Letter 与 Transactions：压缩的是展开层级

R12 的 RA-L 虽然紧凑，也保留了八个编号一级节。Letter 不等于固定五节：它把 Framework、外环策略和训练实现分别写短，使动作接口和复现条件清楚。R22 以一个 Network 节含估计/MPC 两子节，保留两个算法框。R05 的 Transactions 则为决策、初始轨迹和终端优化各设一级方法节。R04/R11/R14 的长系统稿为新增约束、协议、解质量和不同能力测试展开。

因此，把一份稿件压成 Letter 时先合并相同目标的解释层、删重复背景、引用可靠的已有骨干细节，将长推导移到允许的补充；保留新动作/状态、训练或求解实现、可复现比较条件和核心机制消融。扩成长文则补真实问题的模型、机制、分析和能力维度；不可把短句扩成同义长句。目标期刊当前模板和页限优先于来源作者 PDF 的长度，不在本库硬编码当前投稿页限。

## 句段仿写用动作，不用套句

摘要、Introduction及“像说明书”的文字修订，继续读 [PROSE_ARGUMENT_PLAYBOOK.md](PROSE_ARGUMENT_PLAYBOOK.md)、[SENTENCE_CRAFT_PLAYBOOK.md](SENTENCE_CRAFT_PLAYBOOK.md) 与 [writing_moves/INDEX.md](writing_moves/INDEX.md) 中所选主范本的卡。逐篇微观单元还分析相邻句的主语、谓语、信息次序、条件范围、数字比较和证据强度；章节统计和下面三处样本不能代替实际原文检查。宏观论证与句内选择共同修订，方法及结果也适用。

对每个主要子节选该来源的一处真实样本，执行以下三条记录：`source locator → source moves → project replacements`。例如 R12 p3 b19 的动作是“固定速度限制缺陷→联合优化理由→辅助动作定义”。新稿必须先给自己的被调参数及限制，再解释自己的接口，随后才写自己的策略分解。引用或术语不能只替换原文名词后保留整段。

来源样本已经给出了不同论文的具体动作；不要把每篇都统一成“背景→gap→方法→实验”。R03 p6 b5 披露重建环境限制；R21 p9 b5 明确基线不支持变数量，因此单独控制比较；R16 p7 b5 用两段姿态命令解释动态响应；R18 p4 b3 用算法相似性决定哪些章节合并。写作观感来自这些具体阅读路线。

摘要与引言应复制功能比例和推进顺序，不能复制来源的技术承诺或夸张措辞。R12 的单主贡献连续段落是有效例外；不要把现有“二到四条编号贡献”规则机械盖在它上面。没有证据时只写研究方案和待验证命题。

## 排版预算必须落到试排结果

各 profile 的字号、列数、正文块宽、段块长度和章节文本占比是从精确 PDF 版本测出的代理。先把主来源的相对角色占比作为初始预算（intro / related / setup / method / implementation / evidence / closing），再按项目是否有对应内容调整。方法和证据不能因为背景过长被挤掉。实际双栏页数通过目标模板编译后测量，不能把 PDF 块词数等同于页面积，也不能用补充/参考文献页数扩大正文。

成稿检查至少对照三种证据：章节/子节树，主图与正文/图注位置，典型一页的文字/方程/图表密度。选择源页时用主来源的实际方法页和实验页。用户希望“观感几乎一样”，这里指这些可见层级和阅读节奏；科学内容、实验数字、参考文献来源和术语均必须重新依据项目。

## 交付检查：风格是否真的被实例化

| 检查对象 | 应展示的具体证据 | 未通过时修哪里 |
|---|---|---|
| 骨架像所选来源 | 章节功能及顺序映射，来源 p/b，新增/合并理由 | 调整蓝图；不再追加通用写作建议 |
| 段落推进相似 | 至少引言收束、机制开篇、实验解读各一处动作映射 | 改每段任务和衔接，避免只换词 |
| Letter/Trans 颗粒度合适 | 形式证据与机制章节大小，真实试排页数 | 合并解释层或增加实际分析 |
| 大图与章节相互对应 | 具体视觉 donor case 与源页；新图子模块有正文家 | 回到视觉库实际裁图模仿 |
| 方程/算法承载新机制 | profile 中来源密度作比较，项目真实定义/推导作依据 | 删除装饰性公式或补缺失接口 |
| 实验可复现且不冒称 | 实验 profile 的条件/指标/证据范围与新稿实验表 | 补实验或标记待做；不能借来源结果填空 |
| 引用格式及位置合理 | 新稿自己的引用核验，源段落的引用功能类比 | 核验 bibliography；不复用 donor 列表 |

重建：`python scripts/build_preferred_manuscript_profiles.py --pdf-dir <exact-source-folder>`。默认使用安装 skill 内的 `papers/preferred_29`；校验 SHA 后才发布。源文字块提取需要 PyMuPDF。脚本是统计工具，`reviewed_notes.py` 是人工来源判断；更换 PDF 版本先重审，不静默沿用旧 locators。
