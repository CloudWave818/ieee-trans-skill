# 从 29 篇范本继承实验、表格、图注和引用组织

本文件补足“画得像、写得像”背后的证据结构。先读最接近新稿的 [evidence_profiles/INDEX.md](evidence_profiles/INDEX.md) 中的一至两张卡，再阅读本文件适用部分。不要默认把 29 篇叠加为一份庞大的实验清单。

**证据边界：** 29 篇均阅读了实验或 Results 的相关页；8 张代表性原始页面直接检查了表格或文献版式。`profiles.json` 明确记录逐篇阅读范围和未知项。这里的页码是给定 PDF 的文件页码。范本行为是 `SOURCE_OBSERVATION`，迁移建议是 `TRANSFER_RULE`，二者不是期刊官方规定。原始文献信息未作外部逐字段核验。

## 1. 先选文章形态，再选机制，不要只按关键词匹配

新稿先锁定 `article form + method role + principal claim + available evidence`。文章形态来自给定源文件的实际排版，而不是单凭总页数猜测发表期刊。R12/R22 可见 RA-L 预印本页眉，R24 在结论中自称 letter；其他文件的最终发表形态需要另行确认。

| 新稿主问题 | 首选证据母版 | 应继承的实验链 | 不可顺带继承的结论 |
|---|---|---|---|
| 紧凑的跟踪/意图预测系统 | [R01](evidence_profiles/R01.md)、[R06](evidence_profiles/R06.md) | 分模块误差 → 相同目标事件的轨迹/可见性 → 实景验证 | 模块输入使用真值或广播目标状态时，不能宣称端到端感知鲁棒性 |
| 长篇跟踪与动态栖停 | [R11](evidence_profiles/R11.md) | 跟踪总比较 → 典型遮挡事件 → 栖停及视野消融 → 多场景实机 | 不把栖停、跟踪和定位混成同一个 success rate |
| 走廊与高速局部规划 | [R03](evidence_profiles/R03.md) | 速度×障碍密度 → 前端/优化/重用策略替换 → 分段延时 → 飞行约束 | 文献抄录的 baseline 数值不等于在相同硬件重跑 |
| 集群编队长篇方法 | [R04](evidence_profiles/R04.md) | 形状/旋转/尺度公平指标 → 逐项贡献试验 → 群规模/延时 → 实机事件 | 四十余机仿真扩展不能写成同等规模实飞 |
| 图稀疏化、编队规模或成员变化 | [R13](evidence_profiles/R13.md)、[R21](evidence_profiles/R21.md) | 图连接/人数变化 → 误差与速度权衡 → 机制移除 → 恢复及通信 | 与固定人数方法比较时，不能让比较组单独承担不支持的成员变化 |
| 学习仅调整规划器速度或捕获时间 | [R12](evidence_profiles/R12.md)、[R05](evidence_profiles/R05.md) | 相同低层 backbone → 高层策略/训练阶段变体 → task 成功与执行速度 → 实机 | 高层策略不能画成或描述成直接输出电机指令 |
| 点云/RGB直接控制、仿真迁移 | [R15](evidence_profiles/R15.md)、[R23](evidence_profiles/R23.md) | 表征/训练预算 → 未见场景统计 → 域对齐机制 → 真正物理成功与失败 | 特征混合、reward 上升不是实机迁移成功率 |
| 安全层与高动态控制 | [R25](evidence_profiles/R25.md)、[R20](evidence_profiles/R20.md) | 训练/奖励 → 部件移除 → 动态与速度应力 → 约束/失败 → 实机 | 理论安全集有假设，不能凭少量成功飞行写无条件安全 |
| Doppler预测与MPC | [R22](evidence_profiles/R22.md) | 同条件导航 → 在线调参消融 → 独立预测数据集 → 嵌入式资源 → 感知失败传播 | 真值 bounding boxes 不能写成实际检测性能 |
| 多会话SLAM/地图融合长篇 | [R18](evidence_profiles/R18.md) | 子模块 → 完整定位 → 地图几何 → 回环 → 消融 → 会话规模 → 内存/时间 | 无真值代理指标、切分会话和同时多机器人运行不是同一证据 |
| 空地/边缘计算协作 | [R07](evidence_profiles/R07.md)、[R10](evidence_profiles/R10.md) | 单体任务 → 支援/调度变体 → 数量与通信/计算限制 → 实体闭环 | 自感知UGV与盲UGV不同信息条件，必须说明参考角色 |
| 形变、负载及硬件操作能力 | [R19](evidence_profiles/R19.md)、[R14](evidence_profiles/R14.md)、[R16](evidence_profiles/R16.md) | 硬件/约束 → 规划质量 → 控制误差/负载扰动 → 空间操作任务 | 成本函数“能量”不是自动获得的电池能耗测量 |
| Diffusion初始化 + 优化后端 | [R27](evidence_profiles/R27.md) | Claim1多样性/延时 → Claim2编码消融 → Claim3经典规划 → 限制 | 必须计入优化后处理时间，不能把网络推理当总规划延时 |
| 语义场景图/多模态导航 | [R24](evidence_profiles/R24.md)、[R28](evidence_profiles/R28.md)、[R26](evidence_profiles/R26.md) | 受控同栈 baseline → 任务可靠性 → 完成时间/步骤 → 语义与grounding诊断 | 生成视频、仿真交互、能力勾选表不能标成实机统计 |

选择一个主母版，最多一个针对缺失证据问题的补充母版。同一文章形态没有机制近邻时，明确分别记录“排版母版”和“机制证据母版”：例如长篇直接控制RL可借长篇的分节/篇幅组织，但实验对照仍从R15/R25的相同策略层继承；不能为凑长篇而生成不存在的硬件、理论或实验结果。R02 和 R04 属相关研究线，不能算两份独立方法证据。R09 的主文章为 PDF pp.1–8，p.9 起是补充材料；总计 23 页不代表 23 页主文。R26/R28/R29 有各自不同的排版/引文家族，选它们的研究逻辑时不要自动导入其投稿格式。

## 2. 继承的不是实验名字，而是“贡献—比较—测量”的关系

**SOURCE_OBSERVATION：** R04 的 benchmark 小节以 adaptability、predictability、reorganization、resilience、efficiency 等实际方法性质组织，各自对应不同对照（pp.11–15）。R18 将模块BA、整体定位、地图几何、回环、消融、扩展、资源拆开（pp.9–15）。R27 则直接写出 Claim 1/2/3，并逐项回答（pp.6–7）。

**TRANSFER_RULE：** 把母版实验小节改名之前，先生成以下对应关系：

| 新稿主张 | 母版中的证据角色/页 | 新稿可检验变量 | baseline角色 | 输入与控制 | 测量/分母 | 数据状态 |
|---|---|---|---|---|---|---|
| 使用作者提供的真实主张 | 例如 R27 Claim2 / p.7 | 实际新增模块、接口或参数 | 外部系统 / 部件移除 / 等效替换 / 质量参照 | 哪些条件一致、哪些差异保留 | 单次任务/轨迹/对象/场景；统计方式 | AVAILABLE / NEEDS_EXPERIMENT |

每个实验仅回答一项主要问题；共享场景可复用，但不能把同一张总成功表自动当作所有模块有效性的独立证明。相同任务、数据划分、运行预算、初值、动态约束、传感器视野/频率和计算平台，应按具体因果问题控制。系统级比较可以保留原生观测/架构差异，必须明确其作用；模块优越性通常需要进一步保持同一个 backbone。

范本中有可直接迁移的公平性设计：

- R01 只比较 planner 时给两者同样目标真值未来轨迹，从预测差异中隔离规划器（p.6）。
- R03 替换 Gao 的优化器和 RHC，再与自身前端组合比较，避免“全系统胜出即所有新模块有效”的跳跃（pp.6–7）。
- R08 去掉 baseline 的匿名性因素，使对照聚焦时间偏移处理（p.5）。
- R13 把所有图生成方法接到相同编队规划问题上，complete graph 同时是精度参照和资源对照（p.6）。
- R21 比较固定人数方法时禁用成员变化；另开试验验证人数适应性（p.9）。
- R28 固定感知、grounding、机器人描述和低层规划，仅更换几何/语义目标选择（p.6）。

**未知项要显式保留。** 试验章节没有找到随机种子、重复次数或CPU型号，不等于作者未做/未使用。逐篇卡记录“未定位”，新稿需要该事实时标记 `MISSING_INPUT` 或 `NEEDS_EXPERIMENT`，不要填入范本常见值。

## 3. 各类方法的最小可继承证据包

以下是从案例归纳的设计路由，不是要求每篇包含同样数量的试验。

### 高层学习与直接控制要拆开

R12：相同 EGO backbone，固定速度限制的 success–speed 曲线形成参照，策略位于安全/速度权衡上，训练阶段移除解释学到的行为（pp.6–7）。R05：planning SR 和 catching SR 分开，决策误差用定义明确的 OTR，高层策略算法与低层轨迹动态分别评估（pp.7–9）。

R15/R23：表征维数、批大小、训练资源影响学习，reward 曲线必须携带预算信息；视觉对齐需定量指标且最终仍需 task success。R20：静态任务与优化器公平比较，移动目标压力另开试验；直接控制没有独立 trajectory-tracking 误差，应注明不适用。R25：训练 soft shaping 与部署 hard shield 分别移除，并报告实际速度、成功、介入比例及失效条件。

迁移时先问“新策略实际改变哪一层”。该层的对照保持其他层尽可能一致；图、方法、实验和引用都采用同一接口定义。

### 规划与控制要分别证明

R14 的 planner 成功/长度/耗时不替代载荷控制的 RMSE/MAXE、质量偏差、力补偿以及动态极限（pp.12–17）。R19 的固定大小对照回答形变规划价值；同一 figure-eight 的旧/新 controller 回答扰动补偿价值（pp.6–7）。R16 的模式切换、姿态响应、倾斜间隙和接触操作分别证明硬件能力（pp.6–7）。

新稿若提出的是新硬件，可沿用“能力任务 + 可测状态”的证据组织；若还主张算法优越性，需要公平的算法对照。照片只证明照片中发生的操作，不能代替统计成功或精度。

### 规模与资源要用实际瓶颈组织

R04：robot count 对 optimizer runtime；R13：graph connection 对 error/runtime；R18：loop density 与窗口BA/全局BA的时间和内存；R21：point count 对两节点传播延时；R22：tracked object count 对推理频率和CPU占用；R10：计算/通信约束对真实任务完成时间。

选择新方法增长最快的变量，记录 operation、hardware、batch/parallelization、warm-up、timing boundaries。平均网络推理时间、优化迭代时间、完整 planning latency 和端到端任务时间不能合并。R18 全局BA为可运行而聚合 frames，R03 文献 baseline 与自身 thrust limit 有差异，都在比较条件中披露；继承这种披露方式。

## 4. 指标要带定义、条件和分母

从范本迁移以下“指标语义”，不要照搬其数值或试验规模：

| 指标类型 | 需要锁定的语义 | 具体母版 |
|---|---|---|
| success | 完成到何处、何时终止、碰撞/动态约束是否都判失败、试验总数 | R03 p.6；R25 pp.5–7；R28 p.6 |
| speed/time | 全部试验或成功子集、完成时间还是规划时间、失败时如何处理 | R12 p.6；R28 pp.6–7 |
| formation error | 是否允许旋转/尺度/位置对齐，按路径长度或时间平均 | R02 p.5；R04 pp.11–12；R13 p.5 |
| visibility | FoV、遮挡、太近等失败事件是否分开，失效后指标还是否有意义 | R11 pp.11–12 |
| prediction/localization | ground truth、对齐方式、距离/角度单位、预测步长/频率 | R08 pp.5–6；R18 pp.9–13；R22 pp.6–7 |
| model-derived score | 是目标函数、代理精度、分类表现还是独立测量，误差方向 | R19 pp.5–7；R23 p.6 |
| diversity | 候选之间什么对象的相似度、候选数、质量是否同时满足 | R27 pp.6–7 |
| subjective model quality | 谁评分、评分规约、独立样本和一致性；不能当实机完成率 | R26 p.6 |

R12/R28 的速度或完成时间仅对成功试验统计，因此必须同图或同表呈现 SR。失败/不适用可以分别写 `FAIL`/`N/A`，在图注、表注或正文解释；不要把它们都替换成0。相对于baseline的百分比改进必须说明分母，success 百分点变化与相对变化不要混写。源文件中的明显单位或聚合冲突需纠正或标记：例如 R20 表II态度误差列符号与正文角度单位不一致；R21 PAAS 表注称 maximum 而正文称 average。

## 5. 表格按母版的证据分组，而不是按默认美化习惯

已直接检查：[R04 PDF p.13](../../papers/preferred_29/2210.04048v2.pdf#page=13)、[R18 p.12](../../papers/preferred_29/2505.10018v4.pdf#page=12)、[R22 p.6](../../papers/preferred_29/2512.00375v3.pdf#page=6)、[R26 p.6](../../papers/preferred_29/2602.09765v1.pdf#page=6)。

| 表格角色 | 观察到的排布 | 迁移时保持 |
|---|---|---|
| 多场景×多方法 | R04：scenario/variant按行分组，formation type按列分组，组间细横线 | 读者先看实验条件再看方法；宽表横跨正文两栏 |
| 模块资源表 | R03：mapping/planning为method下子行；mean/std/total相邻 | 计时边界与总成本；desktop和onboard明确区分 |
| 数据集精度表 | R18：数据/方法按行，单位与↑↓在metric表头；best cells加粗 | 相同测量定义、同一序列对齐；失败符号解释 |
| 动态环境表 | R22：obstacle count分块，块内metric为行，方法为列；局部浅紫色高亮 | 不将每个数字都强调；浅色编码必须有确定意义 |
| 学习组件表 | R25：每个speed下成对SR/Vel；baseline和消融分开 | 成功分母和实际速度成对，避免只看漂亮的高速数值 |
| 能力覆盖表 | R17/R24/R28：Boolean capability单列，另有数值结果 | 明确这是property inventory，不能宣称同条件性能排名 |
| 生成模型表 | R26：source/closed-source组头，task类别内重复metric，caption在下 | 此母版为单栏预印本，不能当IEEE表格的通用caption位置 |

IEEE形态的代表表通常以黑色横线、衬线字、紧凑数据列、粗体最优值呈现，基本无竖线；R04的表标题在上方且带罗马号，R18/R22还可见 `TABLE V:`/`TABLE I:` 一类变体。**先看所选原页，再继承线条、组头、强调和caption位置。** 不默认加彩色标题带、圆角卡片、阴影或交替大色块。不要把源表的过小文字、怪异小数精度、重复信息和排版错误一并复制。

计划表格必须先有数据字段与组关系，再设置宽度、列距和字号。把数值替换成新稿真实数据后仍应保持组间结构、指标单位和可读性；不足一栏就用一栏，确实需要对照多条件再横跨双栏。

## 6. 图注/表注：继承解读顺序，不补写不存在的结果

观察到三种可复用层级：

1. **简单机制图：** 一句指出图展示的对象/过程，关键箭头或符号解释放在需要处。R01 Fig.2 很短，不能由此规定所有framework图注都很短。
2. **受控比较：** 先说明比较什么，再定义方法/颜色/条件，最后给指标、统计或失败定义。R03 Fig.10逐条定义组件组合；R11 Fig.11把轨迹、Docc阈值、遮挡时刻和距离曲线关联。
3. **系统证据复合图：** 先总问题，再按(a)…顺序解释实景、地图、传感器/尺寸、测量曲线；明确 measured/desired、独立试验合成和图像加工。R05 Fig.6、R14 Fig.9、R29 Fig.4/6/8有这种组织。

可用于新稿的**结构样例**（方括号是待填字段，不能直接成为结果）：

> Comparison under [controlled condition]. (a) [scene/trajectory view]. (b) [metric and unit] across [variable]. Colors identify [methods], and [line/marker] denotes [constraint or event]. Statistics aggregate [trial unit and count]; [failure/N/A handling].

> Physical validation of [capability]. (a) [ordered event sequence]. (b) [map or reference/actual trajectory]. (c) [measured state] and [desired state], with [constraint]. [Registration, image composition or measurement source, when applicable].

它们只给信息顺序，不规定字数。读所选母版精确caption，保留其短/长、panel命名、同一实验对应和证据对象。图注中不能插入正文/数据无法支持的最高速度、成功率、鲁棒性或最佳结论。图中的代表性成功case应标为representative，不假装是全体结果。

## 7. 引用模仿的是论证位置与格式家族

### 先辨认家族

| 源文件 | 文内方式 | 文末观察 | 适用迁移 |
|---|---|---|---|
| R01–R25、R27的主体 | `[n]`，可有成组或连续编号；baseline表头/行也带编号 | 编号悬挂缩进，常见作者首字母、引号内题名、斜体venue、vol./no./pp./year | 新稿目标为IEEE时的主要候选；以实际目标模板验证 |
| R03 / R26 | 同样numeric brackets | full author names或period-separated title，R26为单栏URL条目；不完全相同于常见IEEE条目 | 不把“[n]”当成同一BibTeX style的充分证据 |
| R28 | narrative/parenthetical author–year | alphabetic unnumbered list，姓名分号、年份前置、venue斜体 | 学术论证逻辑可迁移；IEEE目标通常另用其要求的numeric bibliography |
| R29 | superscript numerical references | 无方括号编号，journal缩写、volume、括号年份 | 该publisher形态只在相同目标格式中继承 |

直接检查过 [R01 p.7](../../papers/preferred_29/2011.03968v1.pdf#page=7)、[R03 p.8](../../papers/preferred_29/2202.12177v2.pdf#page=8)、[R28 p.8](../../papers/preferred_29/2607.29009v2.pdf#page=8)、[R29 p.16](../../papers/preferred_29/s41467-026-68967-3.pdf#page=16)。不要照抄源文的重复条目、作者缩写混用、预印本过时年份或卷年冲突。R09 主文和supplement有各自参考文献，不要把两套编号合并错位。

### 文内引用的可继承位置

- **提出相关方法类别后引用其来源。** 接着明确局限适用条件；下一句解释新机制处理哪一缺口。不要用一个reference bundle支持整段互不相同的批评。
- **借用数学/算法对象时靠近首次操作。** 例如动态模型、MINCO参数化、solver、map entropy、GSI、SPL定义等各自需来源；自己的新公式不能整段伪装成范本文献内容。
- **baseline第一次完整介绍要引用。** 简写随后一致。表格/图中保留母版同等密度的baseline ID，但新稿的编号必须由自己的bibliography生成。
- **数据集、软件、硬件各按其实际角色引用。** R18把dataset与MapEval在实验设置/指标处引用，R12/R15常用硬件网页脚注。数据集版本和paper source不混淆；脚注URL不是结果证据。
- **改造baseline写在设置段或表注。** R02加避障、R11替换perception cost、R10把EDF接到相同PDD等做法，必须连着引用和改造说明。

引用句式结构可模仿，但其中的方法名称、缺陷、条件和新稿承诺必须来自真实证据。给定研究主题后，应先找到相关primary sources并核验BibTeX字段，不能把范本的reference list整套搬过去，也不能制造不存在的编号或DOI。

## 8. 从主题/方案输入到可交付输出

仅有主题或研究方案时，交付的是“可执行的实验继承稿”，不是假想完成的 Results：

1. 记录主/辅母版、实际文章形态、对应PDF页、选择理由和排除的格式。
2. 写贡献到试验的映射，并把母版条件逐项标为 `INHERIT / CHANGE / NOT_APPLICABLE`。
3. 列数据、输入、控制组、相关baseline、metric定义、重复/seed计划、计算与物理条件、失败分析和预期图/表字段。重复数按资源和统计目的决定，范本计数仅是现成参考。
4. 每张证据图表附 `source data + aggregation + caption fields + actual claim`；没有结果则标 `NEEDS_EXPERIMENT`，可以生成空schema或明确标注的示意稿。
5. 对已给真实结果，先检查分母/单位/聚合/计时范围，再按母版相同阅读顺序写实验段和解读。结果的幅度、方向、显著性和失败原因都不能由母版提供。

最终交付附简短“继承与改变记录”：主母版的哪些实验逻辑、表格布局、图注顺序、引用家族得到保留；新方法为什么更改某项对照或试验；哪些数据仍未知。这使“几乎一样的观感”能被核查，也保证论文讲的仍是作者实际完成的研究。
