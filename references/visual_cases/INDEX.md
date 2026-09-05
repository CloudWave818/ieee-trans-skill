# 已检查原图案例索引

首批20篇A-level论文的38张指定图，20个图组案例；不是20篇全文逐图精读，也不是1163张图全部确认。选择为目的性抽样：覆盖无人机控制/规划/RL/多智能体、关键机制和实机证据；不代表总体比例。原自动目录保持原状态。

每个案例包含可打开的本地原页、图注/正文定位、面板和编码、科学用途、局限、采集要求及迁移草图。`VISUAL_AND_CONTEXT_REVIEWED`由Codex AI完成，不是人工复核。未读的图、未查清的统计定义和原图问题均不自动升级。

## 按科学关系检索

| 案例 | 论文图号 / PDF页 | 科学关系与画法 | 检索词 |
|---|---|---|---|
| [VC-P001](VC-P001.md) | Fig.2 / p.9 | 把控制示例、超参数与误差分布组织成证据组 | control, sensitivity, distribution |
| [VC-P006](VC-P006.md) | Fig.2,3,4 / p.7 | 姿态试验台照片与状态—残差配对 | hardware, tracking, control |
| [VC-P010](VC-P010.md) | Fig.5,6 / p.7 | 轨迹安全必须落到距离—阈值比较 | swarm, safety, time_series |
| [VC-P017](VC-P017.md) | Fig.5,6 / p.13 | 扰动—控制响应—误差共享事件带 | disturbance, control, uncertainty, time_series |
| [VC-P020](VC-P020.md) | Fig.1 / p.4 | 把前向训练与奖励演化回路分开 | architecture, feedback, rl |
| [VC-P021](VC-P021.md) | Fig.9 / p.10 | 单种子训练曲线与多种子区间各司其职 | rl, learning_curve, uncertainty |
| [VC-P027](VC-P027.md) | Fig.4,5,6 / p.7 | 不确定性学习的时间响应、集合与占据区闭环 | uncertainty, prediction, mechanism |
| [VC-P028](VC-P028.md) | Fig.4,5 / p.12 | 方法为行、相同关键时间为列的协调行为矩阵 | multi_agent, comparison, synchronization |
| [VC-P031](VC-P031.md) | Fig.14,15 / p.14 | 实地安全集叠图与运行时间分布分别验证部署 | hardware, runtime, safe_set |
| [VC-P033](VC-P033.md) | Fig.5 / p.12 | 大量策略轨迹比较的用途与密度上限 | flocking, ablation, trajectory |
| [VC-P034](VC-P034.md) | Fig.9,10,11 / p.9 | 控制模式切换需要行为序列与群体状态配套 | swarm, switching, failure_recovery |
| [VC-P045](VC-P045.md) | Fig.7,8 / p.9 | 外部录像与机载感知小窗串起任务事件 | physical, perception, event_sequence |
| [VC-P048](VC-P048.md) | Fig.1,2 / p.3 | 总体闭环之外，展开路由选择的具体操作 | exploration, mechanism, graph |
| [VC-P051](VC-P051.md) | Fig.8 / p.6 | 故障补偿差异藏在重叠状态曲线时用局部放大 | fault_tolerance, tracking, inset |
| [VC-P059](VC-P059.md) | Fig.14,15,16,17 / p.11 | 真实飞行照片、三维轨迹、速度和姿态互补 | flight, hardware, tracking |
| [VC-P063](VC-P063.md) | Fig.2 / p.5 | 群体不变性要画出实体聚合与时间聚合 | attention, marl, mechanism |
| [VC-P069](VC-P069.md) | Fig.8,9 / p.8 | 安全参数通过几何占据改变规划可行域 | uncertainty, mpc, risk_parameter |
| [VC-P077](VC-P077.md) | Fig.2 / p.3 | 从输入不确定集到保守动作选择的机制链 | robust_rl, mechanism, geometry |
| [VC-P082](VC-P082.md) | Fig.12,13 / p.15 | 每个硬件任务用实证过程与间距曲线成对呈现 | hardware, safety, distribution, swarm |
| [VC-P088](VC-P088.md) | Fig.8,9 / p.8 | 历史路径、当前缆绳和拓扑事件必须分开编码 | tethered_uav, topology, failure_mechanism |

## 使用与扩充

先选1–3个真正匹配科学关系的案例，读取原图观察、正文定位和边界，再写本稿设计。只有统计编号不能支持布局决策；没有匹配案例可以作MANUSCRIPT_DERIVED设计。

原页在工作区IEEE_TRANS_VISUAL_LIBRARY，未放入Skill分发包。selection.json可供scripts/prepare_visual_review.py重建；需要Python/PyMuPDF与pdftoppm。脚本只生成RENDERED_NOT_REVIEWED素材，不能自动证明视觉确认。原文上下文只保留在本地。

下一批应补充本稿实际需要的图，而不是追求覆盖率数字。原论文的其他图仍需逐张查看；真实新手稿的规划质量另作验证。

本地可视浏览页可用 `python scripts/export_visual_gallery.py --output-dir ../IEEE_TRANS_VISUAL_LIBRARY` 重建。该命令生成HTML并链接现有原页，不把论文图片打包进Skill。
