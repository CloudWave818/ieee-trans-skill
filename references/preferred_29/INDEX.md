# 用户优先范本：29 篇逐图学习库

29 篇，337 页，281 条逐图记录，12 张关键图的细化方案和 SVG 布局草图。
这不是训练模型权重，而是后续任务可检索、可追溯的项目知识。全部条目是 AI 阅读记录；小字/统计定义未全量转录。原 PDF、页面与全文保留在本地库。

[风格与模仿规则](STYLE_PLAYBOOK.md) · [强化学习图组](RL_FIGURE_PLAYBOOK.md)

检索：`python scripts/query_visual_cases.py "safety training"`；优先检索本库，无相关匹配再查旧库。

|论文|主题/故事|图数|学习类型|
|---|---|---:|---|
|[R01 Fast-Tracker: A Robust Aerial System for Tracking Agile Target in Cluttered Environments](cards/R01-F1.md)|先用场景和系统闭环定位问题，再拆解预测、搜索和重规划，最后用实飞及追踪响应支撑鲁棒性。|9|NOT_RL|
|[R02 Distributed Swarm Trajectory Optimization for Formation Flight in Dense Environments](cards/R02-F1.md)|用空间编队约束解释优化，再以密集场景、多机轨迹和队形误差说明保持形状与避障的平衡；与 R04 属相关研究线，不能当独立重复证据。|6|NOT_RL|
|[R03 Bubble Planner: Planning High-speed Smooth Quadrotor Trajectories using Receding Corridors](cards/R03-F1.md)|气泡/走廊几何是方法核心，局部剖面和连续规划过程比笼统框图更能说明可行域与高速平滑运动。|12|NOT_RL|
|[R04 Robust and Efficient Trajectory Planning for Formation Flight in Dense Environments](cards/R04-F1.md)|几何和优化机制逐层展开，最后将真实飞行、地图轨迹、队形变化和误差合成事件对应的证据；与 R02 有复用内容。|17|NOT_RL|
|[R05 Catch Planner: Catching High-Speed Targets in the Flight](cards/R05-F1.md)|策略选择捕获时间，优化器产生可飞轨迹；网兜尺寸、动态约束和真实捕获过程共同解释任务可行性，不能把策略动作画成电机指令。|8|RL_HIGH_LEVEL|
|[R06 Intention-Aware Planner for Robust and Safe Aerial Tracking](cards/R06-F1.md)|先估计运动意图、再预测目标、最后联合可见性和安全优化；局部几何图解释每项代价怎样改变跟踪行为。|10|NOT_RL|
|[R07 ColAG: A Collaborative Air-Ground Framework for Perception-Limited UGVs’ Navigation](cards/R07-F1.md)|无人机补足地面车感知，信息交换和路径协作连接到地面导航收益；本 PDF 未定位到 Fig.2，不补造。|8|NOT_RL|
|[R08 Simultaneous Time Synchronization and Mutual Localization for Multi-robot System](cards/R08-F1.md)|测量与时钟关系先画清，再用定位轨迹和同步误差分别验证两个耦合目标。|7|NOT_RL|
|[R09 Collaborative Planning for Catching and Transporting Objects in Unstructured Environments](cards/R09-F1.md)|多机捕获到运输的任务链，需要几何/受力、协同规划和任务过程配套；附录重新编号的三图单列 S1–S3。|9|NOT_RL|
|[R10 Edge Accelerated Robot Navigation With Collaborative Motion Planning](cards/R10-F1.md)|端边信息流与网络/计算开销并列，导航轨迹和时间指标说明卸载是否值得；正文 Fig.14 引用未对应到原图。|13|NOT_RL|
|[R11 Adaptive Tracking and Perching for Quadrotor in Dynamic Scenarios](cards/R11-F1.md)|跟踪和栖停共享可见性、安全与动力约束，但终端条件不同；通过成对机制图和分阶段实验讲清适应性。|21|NOT_RL|
|[R12 Learning Speed Adaptation for Flight in Clutter](cards/R12-F1.md)|学习速度约束而非直接姿态控制；安全/速度权衡与实飞体现策略作用，不能把速度—成功率曲线当训练曲线。|10|RL_HIGH_LEVEL|
|[R13 Sparse-Graph-Enabled Formation Planning for Large-Scale Aerial Swarms](cards/R13-F1.md)|稀疏图如何保留形状信息是机制，机器人数量—时间/性能关系才是可扩展性证据。|10|NOT_RL|
|[R14 Safe and Agile Transportation of Cable-Suspended Payload via Multiple Aerial Robots](cards/R14-F1.md)|负载、绳索和多机动力耦合先几何化，轨迹、张力和状态约束配合运输事件验证安全敏捷性；未定位正文提到的 Fig.14。|13|NOT_RL|
|[R15 Flying on Point Clouds with Reinforcement Learning](cards/R15-F1.md)|点云编码直接服务飞行控制，以编码器/训练配置比较、未见环境和真实飞行连接表示学习与部署；训练阴影定义未确认。|6|RL_DIRECT_CONTROL|
|[R16 FLOAT Drone: A Fully-actuated Coaxial Aerial Robot for Close-Proximity Operations](cards/R16-F1.md)|机构赋予独立力/姿态能力，分解硬件与控制，再用近距离操作和接触响应验证；不能只学普通四旋翼图标。|9|NOT_RL|
|[R17 Efficient Trajectory Generation Based on Traversable Planes in 3D Complex Architectural Spaces](cards/R17-F1.md)|建筑空间中的可通行平面与连接关系决定搜索结构；效率结果要和场景复杂度一起读。|8|NOT_RL|
|[R18 LEMON-Mapping: Loop-Enhanced Large-Scale Multi-Session Point Cloud Merging and Optimization for Globally Consistent Mapping](cards/R18-F1.md)|多会话合并和回环优化通过全局地图、局部放大与误差证据逐层展示；漂亮大地图不足以证明一致性。|18|NOT_RL|
|[R19 Shape-Adaptive Planning and Control for a Deformable Quadrotor](cards/R19-F1.md)|构型改变可穿越空间及动力学，机构、可行域、轨迹与形变状态必须关联。|8|NOT_RL|
|[R20 Reactive Aerobatic Flight via Reinforcement Learning](cards/R20-F1.md)|偏置重置与状态扩展改变训练分布，动作意图和飞行状态进入策略；共同初态/原始奖励下评价以避免奖励修改造成假优势。|5|RL_DIRECT_CONTROL|
|[R21 Number Adaptive Formation Flight Planning via Affine Deformable Guidance in Narrow Environments](cards/R21-F1.md)|数量变化与仿射队形引导对应窄通道中的形状重构；用分阶段队形和误差解释重组而非单纯多条彩线。|10|NOT_RL|
|[R22 DPNet: Doppler LiDAR Motion Planning for Highly-Dynamic Environments](cards/R22-F1.md)|多普勒测量、神经卡尔曼估计和 MPC 接口连接动态障碍预测与规划；有网络不等于强化学习。|7|SUPERVISED_NOT_RL|
|[R23 Flying in Clutter on Monocular RGB by Learning in 3D Radiance Fields with Domain Adaptation](cards/R23-F1.md)|训练用特权深度 critic 与域分类器，部署只用 RGB actor；域适应的反向梯度和实/仿真数据路径必须显式。|7|RL_ASYMMETRIC|
|[R24 USS-Nav: Unified Spatio-Semantic Scene Graph for Lightweight UAV Zero-Shot Object Navigation](cards/R24-F1.md)|统一几何语义图支撑轻量零样本导航，核心是图构建和决策接口；固定语言模型调用不要求 PPO 奖励曲线。|7|ZERO_SHOT_NOT_RL|
|[R25 High-Speed Vision-Based Flight in Clutter with Safety-Shielded Reinforcement Learning](cards/R25-F1.md)|训练奖励中的 CBF 与部署 HOCBF 过滤器是两个位置的机制，必须区分；训练成功率不能代替部署安全与速度评估。|6|RL_ASYMMETRIC_SHIELDED|
|[R26 NavDreamer: Video Models as Zero-Shot 3D Navigators](cards/R26-F1.md)|视频采样、语言评分、尺度恢复和航点执行组成零样本导航链；固定模型采样不画新训练曲线。|15|ZERO_SHOT_NOT_RL|
|[R27 Primitive-based Truncated Diffusion for Efficient Trajectory Generation of Differential Drive Mobile Manipulators](cards/R27-F1.md)|基元与截断扩散改变采样成本/多样性，关键点表示连接全机体约束；本 PDF 的仿真结果不冒称实机。|6|SUPERVISED_DIFFUSION_NOT_RL|
|[R28 D-VLC: Decentralized Vision-Language Collaboration for Heterogeneous Embodied Multi-Robot Systems in Unknown Environments](cards/R28-F1.md)|能力感知、局部视觉记忆和异步协作连接到实际任务事件；初始化任务分解不等于全程中央控制，本 PDF 是仿真。|8|ZERO_SHOT_NOT_RL|
|[R29 Hand-like autonomous flying robot for airborne grasping and interaction](cards/R29-F1.md)|手式机构、任务规划、形变与控制形成完整操作链；实景事件与误差/外力/舵机状态对应，Nature 风格可以迁移到 IEEE 图。|8|NOT_RL|

## 关键构图
- [R04-F14：实飞事件—地图—队形误差的一致证据](cards/R04-F14.md)
- [R05-F4：高层强化学习选择捕获时间](cards/R05-F4.md)
- [R06-F2：意图改变预测，再改变可见性约束下的规划](cards/R06-F2.md)
- [R11-F2：用任务×约束矩阵解释共有困难与不同终端条件](cards/R11-F2.md)
- [R15-F4：训练资源/编码器对学习过程的影响](cards/R15-F4.md)
- [R20-F2：偏置重置和状态扩展如何改变训练分布](cards/R20-F2.md)
- [R20-F3：动作是否学会与为何更易学会成对展示](cards/R20-F3.md)
- [R23-F3：特权 critic 与域对抗支路的训练/部署边界](cards/R23-F3.md)
- [R25-F1：训练奖励塑形与部署安全过滤器是两处不同机制](cards/R25-F1.md)
- [R25-F2：训练成功率与训练场景一起交代](cards/R25-F2.md)
- [R29-F2：硬件—软件—动力学统一机制总图](cards/R29-F2.md)
- [R29-F6：连续操作的事件编号贯穿实景与状态曲线](cards/R29-F6.md)

## 全部图索引
- R01：[1 / p1](cards/R01-F1.md) · [2 / p2](cards/R01-F2.md) · [3 / p3](cards/R01-F3.md) · [4 / p4](cards/R01-F4.md) · [5 / p4](cards/R01-F5.md) · [6 / p5](cards/R01-F6.md) · [7 / p5](cards/R01-F7.md) · [8 / p5](cards/R01-F8.md) · [9 / p6](cards/R01-F9.md)
- R02：[1 / p1](cards/R02-F1.md) · [2 / p3](cards/R02-F2.md) · [3 / p5](cards/R02-F3.md) · [4 / p5](cards/R02-F4.md) · [5 / p6](cards/R02-F5.md) · [6 / p6](cards/R02-F6.md)
- R03：[1 / p1](cards/R03-F1.md) · [2 / p1](cards/R03-F2.md) · [3 / p3](cards/R03-F3.md) · [4 / p4](cards/R03-F4.md) · [5 / p4](cards/R03-F5.md) · [6 / p5](cards/R03-F6.md) · [7 / p5](cards/R03-F7.md) · [8 / p6](cards/R03-F8.md) · [9 / p6](cards/R03-F9.md) · [10 / p7](cards/R03-F10.md) · [11 / p7](cards/R03-F11.md) · [12 / p8](cards/R03-F12.md)
- R04：[1 / p1](cards/R04-F1.md) · [2 / p4](cards/R04-F2.md) · [3 / p5](cards/R04-F3.md) · [4 / p9](cards/R04-F4.md) · [5 / p9](cards/R04-F5.md) · [6 / p10](cards/R04-F6.md) · [7 / p12](cards/R04-F7.md) · [8 / p13](cards/R04-F8.md) · [9 / p14](cards/R04-F9.md) · [10 / p14](cards/R04-F10.md) · [11 / p15](cards/R04-F11.md) · [12 / p15](cards/R04-F12.md) · [13 / p15](cards/R04-F13.md) · [14 / p16](cards/R04-F14.md) · [15 / p17](cards/R04-F15.md) · [16 / p17](cards/R04-F16.md) · [17 / p17](cards/R04-F17.md)
- R05：[1 / p1](cards/R05-F1.md) · [2 / p2](cards/R05-F2.md) · [3 / p3](cards/R05-F3.md) · [4 / p5](cards/R05-F4.md) · [5 / p6](cards/R05-F5.md) · [6 / p8](cards/R05-F6.md) · [7 / p9](cards/R05-F7.md) · [8 / p9](cards/R05-F8.md)
- R06：[1 / p1](cards/R06-F1.md) · [2 / p2](cards/R06-F2.md) · [3 / p3](cards/R06-F3.md) · [4 / p3](cards/R06-F4.md) · [5 / p5](cards/R06-F5.md) · [6 / p5](cards/R06-F6.md) · [7 / p6](cards/R06-F7.md) · [8 / p6](cards/R06-F8.md) · [9 / p7](cards/R06-F9.md) · [10 / p7](cards/R06-F10.md)
- R07：[1 / p1](cards/R07-F1.md) · [3 / p3](cards/R07-F3.md) · [4 / p4](cards/R07-F4.md) · [5 / p4](cards/R07-F5.md) · [6 / p5](cards/R07-F6.md) · [7 / p5](cards/R07-F7.md) · [8 / p6](cards/R07-F8.md) · [9 / p6](cards/R07-F9.md)
- R08：[1 / p1](cards/R08-F1.md) · [2 / p3](cards/R08-F2.md) · [3 / p5](cards/R08-F3.md) · [4 / p6](cards/R08-F4.md) · [5 / p6](cards/R08-F5.md) · [6 / p6](cards/R08-F6.md) · [7 / p6](cards/R08-F7.md)
- R09：[1 / p1](cards/R09-F1.md) · [2 / p4](cards/R09-F2.md) · [3 / p5](cards/R09-F3.md) · [4 / p5](cards/R09-F4.md) · [5 / p6](cards/R09-F5.md) · [6 / p7](cards/R09-F6.md) · [S1 / p15](cards/R09-FS1.md) · [S2 / p17](cards/R09-FS2.md) · [S3 / p18](cards/R09-FS3.md)
- R10：[1 / p1](cards/R10-F1.md) · [2 / p3](cards/R10-F2.md) · [3 / p7](cards/R10-F3.md) · [4 / p7](cards/R10-F4.md) · [5 / p8](cards/R10-F5.md) · [6 / p8](cards/R10-F6.md) · [7 / p9](cards/R10-F7.md) · [8 / p9](cards/R10-F8.md) · [9 / p9](cards/R10-F9.md) · [10 / p10](cards/R10-F10.md) · [11 / p10](cards/R10-F11.md) · [12 / p10](cards/R10-F12.md) · [13 / p11](cards/R10-F13.md)
- R11：[1 / p1](cards/R11-F1.md) · [2 / p4](cards/R11-F2.md) · [3 / p5](cards/R11-F3.md) · [4 / p6](cards/R11-F4.md) · [5 / p7](cards/R11-F5.md) · [6 / p7](cards/R11-F6.md) · [7 / p8](cards/R11-F7.md) · [8 / p10](cards/R11-F8.md) · [9 / p11](cards/R11-F9.md) · [10 / p12](cards/R11-F10.md) · [11 / p13](cards/R11-F11.md) · [12 / p14](cards/R11-F12.md) · [13 / p14](cards/R11-F13.md) · [14 / p14](cards/R11-F14.md) · [15 / p15](cards/R11-F15.md) · [16 / p15](cards/R11-F16.md) · [17 / p16](cards/R11-F17.md) · [18 / p16](cards/R11-F18.md) · [19 / p17](cards/R11-F19.md) · [20 / p18](cards/R11-F20.md) · [21 / p19](cards/R11-F21.md)
- R12：[1 / p1](cards/R12-F1.md) · [2 / p3](cards/R12-F2.md) · [3 / p4](cards/R12-F3.md) · [4 / p5](cards/R12-F4.md) · [5 / p6](cards/R12-F5.md) · [6 / p6](cards/R12-F6.md) · [7 / p6](cards/R12-F7.md) · [8 / p6](cards/R12-F8.md) · [9 / p7](cards/R12-F9.md) · [10 / p7](cards/R12-F10.md)
- R13：[1 / p1](cards/R13-F1.md) · [2 / p2](cards/R13-F2.md) · [3 / p3](cards/R13-F3.md) · [4 / p4](cards/R13-F4.md) · [5 / p5](cards/R13-F5.md) · [6 / p5](cards/R13-F6.md) · [7 / p6](cards/R13-F7.md) · [8 / p6](cards/R13-F8.md) · [9 / p7](cards/R13-F9.md) · [10 / p7](cards/R13-F10.md)
- R14：[1 / p1](cards/R14-F1.md) · [2 / p4](cards/R14-F2.md) · [3 / p5](cards/R14-F3.md) · [4 / p10](cards/R14-F4.md) · [5 / p10](cards/R14-F5.md) · [6 / p13](cards/R14-F6.md) · [7 / p13](cards/R14-F7.md) · [8 / p14](cards/R14-F8.md) · [9 / p15](cards/R14-F9.md) · [10 / p15](cards/R14-F10.md) · [11 / p15](cards/R14-F11.md) · [12 / p16](cards/R14-F12.md) · [13 / p18](cards/R14-F13.md)
- R15：[1 / p1](cards/R15-F1.md) · [2 / p3](cards/R15-F2.md) · [3 / p4](cards/R15-F3.md) · [4 / p5](cards/R15-F4.md) · [5 / p6](cards/R15-F5.md) · [6 / p7](cards/R15-F6.md)
- R16：[1 / p1](cards/R16-F1.md) · [2 / p2](cards/R16-F2.md) · [3 / p3](cards/R16-F3.md) · [4 / p3](cards/R16-F4.md) · [5 / p4](cards/R16-F5.md) · [6 / p4](cards/R16-F6.md) · [7 / p5](cards/R16-F7.md) · [8 / p6](cards/R16-F8.md) · [9 / p7](cards/R16-F9.md)
- R17：[1 / p1](cards/R17-F1.md) · [2 / p2](cards/R17-F2.md) · [3 / p3](cards/R17-F3.md) · [4 / p5](cards/R17-F4.md) · [5 / p5](cards/R17-F5.md) · [6 / p5](cards/R17-F6.md) · [7 / p6](cards/R17-F7.md) · [8 / p6](cards/R17-F8.md)
- R18：[1 / p1](cards/R18-F1.md) · [2 / p4](cards/R18-F2.md) · [3 / p4](cards/R18-F3.md) · [4 / p5](cards/R18-F4.md) · [5 / p7](cards/R18-F5.md) · [6 / p8](cards/R18-F6.md) · [7 / p8](cards/R18-F7.md) · [8 / p9](cards/R18-F8.md) · [9 / p10](cards/R18-F9.md) · [10 / p11](cards/R18-F10.md) · [11 / p12](cards/R18-F11.md) · [12 / p12](cards/R18-F12.md) · [13 / p12](cards/R18-F13.md) · [14 / p13](cards/R18-F14.md) · [15 / p14](cards/R18-F15.md) · [16 / p14](cards/R18-F16.md) · [17 / p15](cards/R18-F17.md) · [18 / p16](cards/R18-F18.md)
- R19：[1 / p1](cards/R19-F1.md) · [2 / p2](cards/R19-F2.md) · [3 / p3](cards/R19-F3.md) · [4 / p5](cards/R19-F4.md) · [5 / p6](cards/R19-F5.md) · [6 / p6](cards/R19-F6.md) · [7 / p7](cards/R19-F7.md) · [8 / p7](cards/R19-F8.md)
- R20：[1 / p1](cards/R20-F1.md) · [2 / p4](cards/R20-F2.md) · [3 / p6](cards/R20-F3.md) · [4 / p7](cards/R20-F4.md) · [5 / p7](cards/R20-F5.md)
- R21：[1 / p1](cards/R21-F1.md) · [2 / p3](cards/R21-F2.md) · [3 / p4](cards/R21-F3.md) · [4 / p5](cards/R21-F4.md) · [5 / p5](cards/R21-F5.md) · [6 / p7](cards/R21-F6.md) · [7 / p7](cards/R21-F7.md) · [8 / p7](cards/R21-F8.md) · [9 / p8](cards/R21-F9.md) · [10 / p8](cards/R21-F10.md)
- R22：[1 / p1](cards/R22-F1.md) · [2 / p2](cards/R22-F2.md) · [3 / p3](cards/R22-F3.md) · [4 / p5](cards/R22-F4.md) · [5 / p6](cards/R22-F5.md) · [6 / p7](cards/R22-F6.md) · [7 / p7](cards/R22-F7.md)
- R23：[1 / p1](cards/R23-F1.md) · [2 / p3](cards/R23-F2.md) · [3 / p4](cards/R23-F3.md) · [4 / p5](cards/R23-F4.md) · [5 / p6](cards/R23-F5.md) · [6 / p7](cards/R23-F6.md) · [7 / p8](cards/R23-F7.md)
- R24：[1 / p1](cards/R24-F1.md) · [2 / p4](cards/R24-F2.md) · [3 / p4](cards/R24-F3.md) · [4 / p5](cards/R24-F4.md) · [5 / p6](cards/R24-F5.md) · [6 / p7](cards/R24-F6.md) · [7 / p7](cards/R24-F7.md)
- R25：[1 / p3](cards/R25-F1.md) · [2 / p5](cards/R25-F2.md) · [3 / p6](cards/R25-F3.md) · [4 / p7](cards/R25-F4.md) · [5 / p7](cards/R25-F5.md) · [6 / p8](cards/R25-F6.md)
- R26：[1 / p2](cards/R26-F1.md) · [2 / p4](cards/R26-F2.md) · [3 / p5](cards/R26-F3.md) · [4 / p8](cards/R26-F4.md) · [5 / p8](cards/R26-F5.md) · [6 / p13](cards/R26-F6.md) · [7 / p14](cards/R26-F7.md) · [8 / p14](cards/R26-F8.md) · [9 / p15](cards/R26-F9.md) · [10 / p15](cards/R26-F10.md) · [11 / p18](cards/R26-F11.md) · [12 / p19](cards/R26-F12.md) · [13 / p20](cards/R26-F13.md) · [14 / p21](cards/R26-F14.md) · [15 / p22](cards/R26-F15.md)
- R27：[1 / p1](cards/R27-F1.md) · [2 / p3](cards/R27-F2.md) · [3 / p4](cards/R27-F3.md) · [4 / p5](cards/R27-F4.md) · [5 / p6](cards/R27-F5.md) · [6 / p7](cards/R27-F6.md)
- R28：[1 / p2](cards/R28-F1.md) · [2 / p4](cards/R28-F2.md) · [3 / p4](cards/R28-F3.md) · [4 / p6](cards/R28-F4.md) · [5 / p7](cards/R28-F5.md) · [6 / p11](cards/R28-F6.md) · [7 / p12](cards/R28-F7.md) · [8 / p13](cards/R28-F8.md)
- R29：[1 / p3](cards/R29-F1.md) · [2 / p4](cards/R29-F2.md) · [3 / p5](cards/R29-F3.md) · [4 / p6](cards/R29-F4.md) · [5 / p8](cards/R29-F5.md) · [6 / p9](cards/R29-F6.md) · [7 / p10](cards/R29-F7.md) · [8 / p12](cards/R29-F8.md)
