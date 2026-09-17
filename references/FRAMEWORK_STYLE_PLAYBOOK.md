# Framework Style Playbook — Pastel Layered Architecture

Style ID: `PASTEL_LAYERED_FRAMEWORK`

Version: 1.0 · 2026-09-17

Scope: method / network / system architecture rendered as `VECTOR_SCHEMATIC`.

## 1. 来源、适用范围与优先级

本规范来自用户于 2026-09-17 提供并明确要求借鉴的框架图。该图具有横向阶段、浅色分区、虚线组框、衬线标题、嵌套模块、局部特征示意和细黑箭头。参考图可见标题包括 Robot Feature、Embedding、Gated Transformer Encoder、Actor-Critic Architecture；这些名称仅用于辨认参考，不是本稿应当具有的组件。原论文作者、题名和出版信息未核实，不登记为已核实 corpus 文献。这里只保留视觉规则，不随规范发布参考截图。

**默认适用**：整体方法框架、网络架构、学习与决策架构、规划与控制系统框架，以及复合图中明确承担这些功能的面板。

**不默认适用**：Introduction 动机图、卡通叙事图、几何证明图、纯算法流程图、统计结果图、训练曲线、轨迹数据图、硬件照片与实飞证据。保留这些图原有的规范，不为了统一而全部改成浅色盒子。

优先顺序：科学与证据真实性、实际投稿模板的硬约束不可让步；满足这些条件后，当前任务明确指定的参考/版式 > 本框架图默认样式 > preferred-29 一般视觉偏好 > 通用美化建议。已有经用户锁定的图，不因新增默认样式被自动重画。非架构型机制图与纯流程图仍按其真实关系选型。

本页的颜色、字号、线宽和比例都是**设计起点，不是 IEEE 统一强制规范**。字体外观接近 Times 不等于已核实参考图使用 Times New Roman；以下字体是我们选定的实现方案。

## 2. 核心画法：大分区 + 小机制，不是大盒子串联

一张主框架图优先横向阅读：具体输入 → 表示/预处理 → 核心机制 → 决策/输出。通常可分成 3–5 个有实际意义的阶段，但阶段数由算法决定；两阶段方法不能硬补四阶段。

图中保持三个层次：

1. **阶段层**：整齐对齐的浅色功能区，细虚线边界，标题置于框上方。
2. **模块层**：区内用细实线圆角矩形表示实际运算；并行、分支、融合、递推用真实拓扑表达。
3. **表示层**：必要时在模块内或旁边放小型向量、图结构、候选轨迹、集合、约束或分布示意，解释到底处理什么。

重点模块获得更多空间，标准模块收敛表达。核心贡献必须显示至少一个具体改变的运算/信息接口，不能只把“Proposed Module”放大或涂深。用“输入什么、改变什么、输出什么”检查每个分区。说明性小图不按数量凑配额；纯代数模块用简式/接口也可以。

## 3. 版式与字体参数

| 项目 | 默认设计起点 | 调整边界 |
|---|---|---|
| 画布 | 白底，横向；不含图注的宽高比约 2.5–3.0:1 | 真实闭环或并行结构可改变比例，不拉伸对象 |
| 列宽 | 密集主框架优先双栏；例如最终宽约 178 mm | 以实际模板为准；单栏应重新排布或减细节，不直接缩小密图 |
| 阶段宽度 | 四区示例：18% / 26% / 32% / 24%，按可用内容宽度分配 | 只是草图起点，不能限制核心模块；其他阶段数重新分配 |
| 外部留白 | 外边距约 2–3 mm，阶段间距约 2–4 mm | 图例另预留位置，不能事后塞入大块右侧空白 |
| 内部留白 | 模块与组框约 2 mm 以上，信号走廊单独保留 | 保证文字、箭头端口、边界互不碰撞 |
| 字体 | Times New Roman；不可用时用 Liberation Serif 等衬线替代并记录 | 数学符号用协调的数学字体；中文说明用兼容中文字体，不能混乱回退 |
| 阶段标题 | 最终约 10–11 pt、粗体；放在组框上方 | 标题长度由内容决定，避免堆成多行大标题 |
| 模块标签 | 最终约 8–9 pt，常规字重；通常 1–4 个词、至多两行 | 保留 canonical name，不为短而擅自改术语 |
| 信号/图例 | 最终约 7.5–8.5 pt | 不把低于 7.5 pt 作为解决拥挤的常规办法 |
| 图注 | 放在论文排版层，不画进图像 | 示意图内只留必要短标签，不粘贴参考图图注 |

用最终物理尺寸核算，而不是只看 2000 像素大图：

`final_font_pt = svg_font_units × final_width_mm / viewBox_width × 72 / 25.4`

这个换算假设字体所在对象没有额外缩放；存在 transform 时应计入缩放或直接检查最终导出。空间不足时先删次要标签、扩大关键区或拆伴随机制图，不先缩字体。

## 4. 配色与边界

以下是为复现参考图气质选定的**近似配色**，不是从论文源文件提取的精确色值。

| 用途 | 建议色值 |
|---|---|
| 全局背景 | `#FFFFFF` |
| 输入/上下文分区 | `#F0F0F0` 浅灰 |
| 表示/编码分区 | `#FBE6DC` 浅桃 |
| 核心处理分区 | `#EAF0F6` 浅蓝灰 |
| 决策/输出分区 | `#FFF4CF` 浅黄 |
| 局部模块可选色 | `#E3EEDC` 浅绿；`#DDE8F4` 浅蓝；`#F3CDD2` 浅粉；`#EAD7E9` 浅紫 |
| 文字与主箭头 | `#202020` |
| 次要边界/注释 | `#666666` |

大区用低饱和浅底，小模块适度加深但保持黑字清楚。已有跨图语义色典优先保持一致；不得把别处代表 proposed method 的蓝色在这里无说明地改成 baseline。功能区颜色和算法曲线颜色属于不同语义层时必须说明。

外组框：矩形或极小圆角，最终约 0.7–0.9 pt 的短虚线；起点 dash/gap 约 3/2 pt。内部模块：小圆角，约 0.6–0.8 pt 实线；圆角半径约 1–2 mm。嵌套容器最多保持必要的两三级，不做套娃装饰。

禁止高饱和大色块、黑底霓虹、玻璃效果、渐变模块底、厚重阴影、粗大发光箭头。表示真实矩阵/密度的连续色标不属于装饰渐变，但必须满足第 6 节的数据边界。

## 5. 连线语法与训练/执行边界

主前向数据流用细黑实线箭头，约 0.7–0.9 pt；辅助连线约 0.6–0.7 pt。优先正交短线，使用明确的输入/输出端口。箭头不得穿过文字或无关模块；交叉无连接时不画连接点，真实汇合才画点或定义运算符。

组框虚线仅表示**功能分组**。训练专用边用另一层编码，例如有图例的彩色虚线并标 `training only`；不能把所有虚线组框默认解释成训练区域。在线闭环反馈仍用实线，沿外围返回并标清反馈量；时间递推要区分上一时刻与当前时刻。

跨阶段的重要接口标信号名，单位/坐标系在动作接口或 brief 中写明。不要每根微小层间箭头都塞长文本。残差、拼接、加法、采样、梯度不能互相替代；运算符必须与论文/实现一致。

同时出现训练与部署时：明确哪些模块仅训练存在、哪些参数被冻结、执行时可获得哪些输入。不得让训练用真实目标、未来状态、特权观测或评价指标流入部署策略。梯度箭头须有真实损失和可微路径支持；经过不可微采样/环境的路径不能仅为模仿参考图而画成普通反向传播。

## 6. 局部机制图形：用图解释运算

| 真实对象/运算 | 可采用的局部表示 | 不得暗示的内容 |
|---|---|---|
| 输入状态/主体 | 风格统一的小图标 + 状态符号/向量 | 未配备的传感器、不存在的实物平台 |
| 特征/嵌入 | 紧凑 token/向量格，颜色与图例对应 | 未实现的位置编码、类型编码或特征维度 |
| 图交互 | 少量节点、边、聚合方向 | 没有使用的 GNN 或通信拓扑 |
| 递推/时序 | 记忆单元、已定义的时间索引、外围回路 | 凭空添加 GRU、LSTM 或高阶推理 |
| 重复层/候选集合 | 轻微错位层叠或集合括号 | 未知的层数、共享权重或并行执行 |
| 路径/规划 | 候选曲线、障碍、约束集合、选择操作 | 伪造的实验轨迹或性能差距 |
| 概率输出 | 有定义的符号分布或解析模型示意 | 未测得的 posterior、热图、概率大小或收敛结果 |
| 多头输出 | 从实际共享节点分叉到不同输出 | 原文没有的 actor/critic、多任务 head |

层叠用于真实重复/集合关系，不用于阴影。`×N` 的 N 必须来自手稿或代码；缺失时标 `NEEDS_AUTHOR_DECISION`，或者在不影响主张时省略次数并登记省略项。

解释性轨迹/分布可以是明确标注 `schematic` 的符号示意，不得表现为测得的结果。需要实际采样点、标尺、概率值、对比曲线、误差条或定量热图时，为该 inset 单独声明 `DATA_PLOT` 与数据/解析模型来源；不能因外框是 `VECTOR_SCHEMATIC` 就绕过数据要求。

参考图中的机器人/行人小图只是输入具象化的范例；本稿是无人机就用一致的四旋翼图标，不混成六旋翼，也不把示意图伪装为实飞照片。

## 7. 冻结科学内容，再做视觉优化

从实际手稿/代码/作者说明中提取节点和边。已有足够资料时直接完成这一步，不为形式额外要求用户确认。资料不足时可按原 Skill 生成明确标注的 provisional 草图，不补成既有事实。

在 brief 内记录 `FROZEN_STORYBOARD`：

- `style_id` 与适用图/面板；
- 核心问题、真实方法主链、核心贡献及其来源位置；
- 阶段标题、模块 ID、标签、分组、输入/输出端口、节点对应手稿/代码来源；
- 边的起点/终点、信号、方向、训练/部署属性、特殊运算；
- 允许出现的小图形及其 `schematic` / `DATA_PLOT` 属性；
- 参考图借用的视觉元素；明确不继承的模块、变量和故事；
- 最终宽度、字号、颜色语义、留白与图例位置；
- 已知事实、设计假设、缺失信息，不能改变的内容。

随后执行 `RENDER_LOCK`：只能调整几何位置、配色深浅、字体、留白、对齐、走线和不改变含义的图形简化。不能以“更好看”为由增删边、改变运算顺序、改变角色、生成新 loss/head、改变量或补充结论。真正需要改科学内容时先修订 storyboard 并留下原因。

最终采用 `原理核对 → 布局草图 → 细化 → 最终尺寸检查 → 源文件核对`，不是“套一个漂亮架构图，再找地方安放方法”。

## 8. 可直接交接的绘图 Prompt

填满以下方括号后交给绘图工具；不要把不完整占位符冒充可执行规格。交接给不能访问本仓库的系统时，把本页第 2–7 节中适用参数与完整 storyboard 一并附上。

```text
Create a publication-oriented academic method architecture diagram in the
PASTEL_LAYERED_FRAMEWORK style.

SCIENTIFIC CONTENT LOCK
Use only this frozen storyboard: [exact stages, node IDs, node labels,
node-source mapping, ports, directed edges, signals, operations, and
training/deployment boundaries].
The central mechanism is [implemented change and its actual output].
Borrow only visual grammar from the supplied reference; do not borrow its
Transformer, GRU, embedding, actor-critic, loss, sampling or robot/human
story unless explicitly present in the frozen storyboard.

VISUAL DESIGN
Use a white horizontal canvas at [final width and aspect ratio]. Organize
actual stages left to right in aligned pale-gray, pale-peach, pale-blue-gray
and pale-yellow groups, adapting the palette to the locked semantic dictionary.
Place bold serif stage headings above thin dashed group borders. Inside each
group, use small-radius, thin-solid-border modules with short canonical labels.
Prefer Times New Roman or a recorded serif substitute. Use [final font sizes]
and [physical line widths]. Keep black/charcoal orthogonal arrows, explicit
ports, uncluttered signal corridors, and readable whitespace.
Show [approved local pictograms] to explain representations and operations.
Show stacked layers, recurrence, multi-head branches, feedback and gradients
only where declared in the storyboard. Make the actual proposed mechanism
visually explicit; do not hide it inside a generic large colored box.

NEGATIVE CONSTRAINTS
No glossy presentation style, saturated group backgrounds, decorative 3-D,
heavy shadows, thick arrows, full sentences in modules, ornamental networks,
unsupported layers, new modules, fake measurements or invented causal edges.
Keep group-boundary dashes distinct from training-only edge notation.
Keep all training-only privileged information outside the deployment path.
Do not convert a data inset into an invented illustrative result.

DELIVERABLES AND QA
Return an editable vector source with real text and individually editable
nodes/edges, plus a preview and a concise label/edge verification record.
Inspect at the stated final physical width. Preserve the figure caption
outside the artwork. If only a raster draft is produced, label it a draft;
do not claim it is editable vector output or that final-size QA is complete.
```

## 9. 交付与验收状态

保留实际生成的编辑源文件（例如含真实文本和独立图元的 SVG，或其他实际可编辑格式）以及预览。需要投稿导出时再按实际模板提供相应格式；只有 PNG 的文件不能因被放入 SVG/PPT 容器而声称可编辑。不要附带或分发字体文件。

区分 `SPEC_READY`、`DRAFT_RENDERED`、`VISUALLY_CHECKED` 与 `INDEPENDENT_HANDOFF_TESTED`。本规范被写入 Skill、文本检查通过或节点表齐全，都不等于真实图已被绘制/目检。没有样图时只报告规范级完成。

## 10. 框架图专项审核

- [ ] 图型确属架构，非为了套风格而误把动机图/数据图改成架构。
- [ ] 当前参考、默认样式与已有锁定图的优先级已处理；适用范围明确。
- [ ] 每个阶段/模块/主要接口有真实内容来源，核心运算不是通用黑盒。
- [ ] 大区浅底细虚线、小模块细实线、衬线标题和留白形成清晰层次。
- [ ] 局部图形表达实际对象/运算，而不是装饰网络、无关热图或假照片。
- [ ] 层叠/次数、状态递推、并行/共享、拼接/加法均与方法一致。
- [ ] 前向、反馈、训练梯度和训练专用区域不会混淆；无特权信息泄漏。
- [ ] 所有边与标签和 frozen storyboard 一致，无漏线、反向、假连接。
- [ ] quantitative inset 有来源和独立绘图路线；示意内容明确而不冒充结果。
- [ ] 最终尺寸下字号、箭头端点、符号和图例可读，无碰撞、裁切和杂乱交叉。
- [ ] 编辑源中的文字与节点可编辑；预览与源文件内容一致。
- [ ] 验收状态有对应证据，未把规范检查报告成视觉验收。

科学内容被污染、造数、训练部署泄漏或错误边导致错误方法解释，按 `BLOCKER` 处理。明显偏离用户指定风格、纯通用盒子掩盖核心机制或最终不可读，按 `MAJOR` 处理。轻微间距、对齐和色差为 `MINOR`；没有渲染证据时视觉项记 `NOT_EXECUTED`，不能勾选通过。
