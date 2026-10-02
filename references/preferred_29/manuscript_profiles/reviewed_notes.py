"""Human source review. Page numbers are 1-based, block indices are 0-based.

These annotations describe rhetorical operations, never reusable technical claims.
Confirmed local form is distinguished from external author metadata and unknown form.
"""

# Format: section heading, PDF page, source text block, role.
SECTIONS = {
"R01": [("INTRODUCTION",1,3,"intro"),("RELATED WORK",2,1,"related"),("INTENT-FREE TARGET MOTION PREDICTION",2,4,"method"),("SAFE TRACKING TRAJECTORY PLANNING",3,7,"method"),("RESULTS",5,37,"evidence"),("CONCLUSION",6,13,"closing"),("REFERENCES",7,0,"references")],
"R02": [("INTRODUCTION",1,3,"intro"),("RELATED WORKS",2,1,"related"),("A DIFFERENTIABLE FORMATION SIMILARITY METRIC",2,7,"method"),("SPATIAL-TEMPORAL TRAJECTORY OPTIMIZATION FOR FORMATION FLIGHT",3,22,"method"),("BENCHMARK",5,15,"evidence"),("REAL WORLD AND SIMULATION EXPERIMENTS",5,23,"evidence"),("CONCLUSIONS AND FUTURE WORK",6,14,"closing"),("REFERENCES",7,0,"references")],
"R03": [("INTRODUCTION",1,4,"intro"),("RELATED WORKS",2,1,"related"),("PRELIMINARIES",3,1,"setup"),("PLANNER",4,1,"method"),("EXPERIMENTS",6,5,"evidence"),("CONCLUSION AND FUTURE WORK",7,65,"closing"),("REFERENCES",8,24,"references")],
"R04": [("INTRODUCTION",1,5,"intro"),("RELATED WORKS",2,8,"related"),("SYSTEM OVERVIEW",3,3,"setup"),("ADAPTIVE DESCRIPTION OF SWARM FORMATION",5,1,"method"),("SPATIAL-TEMPORAL TRAJECTORY OPTIMIZATION FOR FORMATION FLIGHT",6,19,"method"),("SWARM REORGANIZATION METHOD",8,33,"method"),("SWARM AGREEMENT METHOD",10,12,"method"),("BENCHMARK",11,11,"evidence"),("REAL WORLD EXPERIMENTS AND SIMULATION",15,13,"evidence"),("CONCLUSION AND FUTURE WORK",17,9,"closing"),("APPENDIX",18,2,"appendix"),("REFERENCES",18,70,"references")],
"R05": [("INTRODUCTION",1,5,"intro"),("RELATED WORK",2,27,"related"),("PROBLEM STATEMENT",3,2,"setup"),("LEARNING-BASED SEQUENTIAL DECISION MAKING",4,7,"method"),("MOTION PRIMITIVE TRAJECTORY GENERATION",4,26,"method"),("TERMINAL-FLEXIBLE TRAJECORY OPTIMIZATION",5,62,"method"),("EXPERIMENTS",7,16,"evidence"),("CONCLUSION",10,2,"closing"),("ACKNOWLEDGMENT",10,4,"backmatter"),("REFERENCES",10,6,"references")],
"R06": [("INTRODUCTION",1,3,"intro"),("RELATED WORK",2,19,"related"),("SYSTEM OVERVIEW",2,21,"setup"),("TARGET INTENTION PREDICTION",3,17,"method"),("INTENTION-DRIVEN TARGET MOTION PREDICTION",4,9,"method"),("INTENTION-AWARE TRAJECTORY OPTIMIZATION",5,12,"method"),("EXPERIMENTS",6,49,"evidence"),("CONCLUSION",8,1,"closing"),("REFERENCES",8,3,"references")],
"R07": [("INTRODUCTION",1,5,"intro"),("RELATED WORKS",2,2,"related"),("THE COLAG FRAMEWORK",3,1,"method"),("EXPERIMENT",5,24,"evidence"),("CONCLUSION",6,37,"closing"),("REFERENCES",7,1,"references")],
"R08": [("INTRODUCTION",1,3,"intro"),("RELATED WORKS",2,1,"related"),("RELATIVE LOCALIZATION WITH TIME OFFSET ESTIMATION",2,7,"method"),("RELAXATION AND ITERATIVE OPTIMIZATION",3,34,"method"),("EXPERIMENTS",5,5,"evidence"),("CONCLUSIONS AND FUTURE WORK",6,78,"closing"),("REFERENCES",7,0,"references")],
"R09": [("INTRODUCTION",1,3,"intro"),("RELATED WORK",2,2,"related"),("COLLABORATIVE TRAJECTORIES OPTIMIZAITON",2,5,"method"),("COLLABORATIVELY CATCHING AND TRANSPORTING OBJECTS",4,12,"method"),("EVALUATION AND EXPERIMENTS",6,63,"evidence"),("CONCLUSION",8,1,"closing"),("REFERENCES",8,3,"references"),("Supplementary Materials",9,0,"supplement")],
"R10": [("INTRODUCTION",1,3,"intro"),("RELATED WORK",2,5,"related"),("TIGHTLY COUPLED DECISION-MAKING AND MOTION PLANNING",2,9,"method"),("ALGORITHM DESIGNS FOR DECISION-MAKING AND MOTION PLANNING",4,6,"method"),("EXPERIMENTS",6,48,"evidence"),("CONCLUSION",11,5,"closing"),("REFERENCES",11,7,"references")],
"R11": [("INTRODUCTION",1,5,"intro"),("RELATED WORKS",2,4,"related"),("SYSTEM OVERVIEW AND PRELIMINARIES",3,5,"setup"),("VISIBILITY-AWARE TRACKING PLANNING",5,19,"method"),("AGGRESSIVE AND FLEXIBLE PERCHING PLANNING",6,52,"method"),("SPATIAL-TEMPORAL TRAJECTORY OPTIMIZATION",9,12,"method"),("SIMULATION AND BENCHMARK",11,25,"evidence"),("REAL WORLD EXPERIMENTS",16,18,"evidence"),("CONCLUSION",17,30,"closing"),("ACKNOWLEDGEMENT",18,25,"backmatter"),("REFERENCES",18,27,"references")],
"R12": [("INTRODUCTION",1,5,"intro"),("RELATED WORK",2,2,"related"),("PROBLEM FORMULATION",2,6,"setup"),("FRAMEWORK",3,7,"method"),("REINFORCEMENT LEARNING FOR THE OUTER-LOOP POLICY",4,3,"method"),("TRAINING SETUP AND IMPLEMENTATION",5,11,"implementation"),("EXPERIMENTS",6,10,"evidence"),("CONCLUSION",8,2,"closing"),("REFERENCES",8,4,"references")],
"R13": [("INTRODUCTION",1,3,"intro"),("RELATED WORKS",2,0,"related"),("PRELIMINARY AND OVERVIEW",2,13,"setup"),("SPARSIFICATION OF COMPLETE GRAPHS",3,37,"method"),("GOOD SPARSE GRAPH CONSTRUCTION METHOD",4,1,"method"),("SIMULATION AND BENCHMARK",5,24,"evidence"),("CONCLUSIONS AND FUTURE WORK",8,1,"closing"),("REFERENCES",8,3,"references")],
"R14": [("INTRODUCTION",1,5,"intro"),("RELATED WORKS",2,4,"related"),("SYSTEM OVERVIEW AND PRELIMINARIES",3,5,"setup"),("PLANNING FOR SAFE AND AGILE TRANSPORTATION",6,3,"method"),("SPATIAL-TEMPORAL TRAJECTORY OPTIMIZATION",9,113,"method"),("CONTROL SCHEME FOR AGILE TRANSPORTATION",11,57,"method"),("BENCHMARKS AND SIMULATIONS",12,55,"evidence"),("REAL WORLD EXPERIMENTS",14,24,"evidence"),("CONCLUSION",17,17,"closing"),("REFERENCES",17,19,"references")],
"R15": [("INTRODUCTION",1,6,"intro"),("RELATED WORK",2,3,"related"),("SIM-TO-REAL RL FOR FLYING ON POINT CLOUDS",3,2,"method"),("SYSTEM AND IMPLEMENTATION",5,2,"implementation"),("RESULTS",5,6,"evidence"),("CONCLUSION, LIMITATIONS AND FUTURE WORK",7,5,"closing"),("REFERENCES",7,7,"references")],
"R16": [("INTRODUCTION",1,4,"intro"),("RELATED WORK",2,4,"related"),("DESIGN",2,12,"method"),("DYNAMICS AND CONTROL",4,11,"method"),("EXPERIMENTS",6,7,"evidence"),("CONCLUSION",8,1,"closing"),("ACKNOWLEDGEMENT",8,2,"backmatter"),("REFERENCES",8,3,"references")],
"R17": [("INTRODUCTION",1,3,"intro"),("RELATED WORK",2,1,"related"),("TRAVERSABLE PLANE GRAPH CONSTRUCTION",2,4,"method"),("TRAJECTORY GENERATION",3,2,"method"),("EXPERIMENTS",5,1,"evidence"),("CONCLUSION",6,15,"closing"),("REFERENCES",7,0,"references")],
"R18": [("INTRODUCTION",1,10,"intro"),("RELATED WORKS",3,6,"related"),("SYSTEM OVERVIEW",3,9,"setup"),("LOOP PROCESSING MODULE",4,4,"method"),("SPATIAL BUNDLE ADJUSTMENT",5,6,"method"),("TWO-STEP POSE GRAPH OPTIMIZATION",8,3,"method"),("EXPERIMENTS",9,7,"evidence"),("CONCLUSION AND FUTURE WORK",15,7,"closing"),("APPENDIX: PROOF OF LEMMA",16,3,"appendix"),("REFERENCES",17,25,"references")],
"R19": [("INTRODUCTION",1,13,"intro"),("RELATED WORK",2,15,"related"),("DYNAMIC MODEL",3,1,"setup"),("METHODOLOGY",3,15,"method"),("EXPERIMENTS",5,35,"evidence"),("CONCLUSIONS",8,11,"closing"),("REFERENCES",8,13,"references")],
"R20": [("INTRODUCTION",1,5,"intro"),("RELATED WORK",2,4,"related"),("METHODOLOGY",2,6,"method"),("EVALUATIONS",5,25,"evidence"),("CONCLUSION",8,2,"closing"),("REFERENCES",8,4,"references")],
"R21": [("INTRODUCTION",1,4,"intro"),("RELATED WORK",2,3,"related"),("SYSTEM OVERVIEW",3,70,"setup"),("NUMBER AFFINE ADAPTIVE DEFORMABLE GUIDANCE",4,2,"method"),("BENCHMARKS AND EXPERIMENTS",6,39,"evidence"),("CONCLUSION AND FUTURE WORK",10,7,"closing"),("REFERENCES",10,9,"references")],
"R22": [("INTRODUCTION",1,6,"intro"),("RELATED WORK",2,6,"related"),("PROBLEM FORMULATION",2,30,"setup"),("DOPPLER PLANNING NETWORK",3,9,"method"),("EXPERIMENTS",5,17,"evidence"),("CONCLUSION",8,6,"closing"),("REFERENCES",8,7,"references")],
"R23": [("INTRODUCTION",1,27,"intro"),("RELATED WORK",2,2,"related"),("TRAINING PIPELINE FOR RGB NAVIGATION TASK",2,8,"method"),("SIM-TO-REAL TRANSFER",4,51,"method"),("EVALUATIONS",5,7,"evidence"),("CONCLUSION AND FUTURE WORK",7,17,"closing"),("REFERENCES",8,1,"references")],
"R24": [("INTRODUCTION",1,7,"intro"),("RELATED WORK",2,5,"related"),("SYSTEM OVERVIEW",3,4,"setup"),("UNIFIED SPATIO-SEMANTIC SCENE GRAPH",3,5,"method"),("SEMANTIC-AWARE HIERARCHICAL EXPLORATION AND PLANNING",5,13,"method"),("EXPERIMENTS",6,5,"evidence"),("CONCLUSION",8,1,"closing"),("REFERENCES",8,3,"references")],
"R25": [("INTRODUCTION",1,4,"intro"),("RELATED WORK",2,1,"related"),("METHODOLOGY",2,7,"method"),("EXPERIMENTS",5,0,"evidence"),("CONCLUSION",7,30,"closing"),("REFERENCES",8,5,"references")],
"R26": [("Introduction",1,6,"intro"),("Related Work",3,2,"related"),("Methods",3,7,"method"),("Experiments",5,17,"evidence"),("Conclusion",8,10,"closing"),("Limitation",9,0,"closing"),("References",9,2,"references"),("Overview / Experiment Details",13,0,"appendix")],
"R27": [("INTRODUCTION",1,3,"intro"),("RELATED WORKS",2,4,"related"),("PLANNING FRAMEWORK",3,59,"method"),("IMPLEMENTATION DETAILS",5,28,"implementation"),("RESULTS",6,33,"evidence"),("CONCLUSION & LIMITATIONS",8,0,"closing"),("REFERENCES",8,2,"references")],
"R28": [("Introduction",1,5,"intro"),("Related Work",3,1,"related"),("Method",3,6,"method"),("Experiments",5,11,"evidence"),("Conclusion",7,20,"closing"),("References",8,1,"references"),("Appendix",9,1,"appendix")],
"R29": [("Introduction (unheaded)",1,3,"intro"),("Results",2,2,"evidence"),("Discussion",11,2,"closing"),("Methods",11,4,"method"),("Data availability",16,1,"backmatter"),("References",16,3,"references")]
}

# Each sample has a real locator and a paraphrase of the moves in that source block.
SAMPLES = {
"R01": [(1,9,"引言后段","搜索接口→走廊→后端优化→多相机实机→比较结果→贡献入口；按闭环次序写，不先列一串模块名。"),(3,5,"机制段","回扣引言中目标丢失问题→说明通常的恢复路线→引出操作步骤；每个机制先解释触发条件。"),(5,39,"实现段","平台→目标与检测→相机视野的行为后果→规划朝向→总耗时与更新频率→参数引用；硬件事实必须解释为什么影响方法。")],
"R02": [(2,0,"贡献收束","依次列几何度量、联合优化、仿真及实机；三项呈现机制→求解→验证，而非三个同义性能形容词。"),(2,8,"模型段","定义机器人图→解释顶点和边的物理含义→交代全连接通信假设→定义权重；先对象后符号后适用假设。"),(5,16,"比较段","说明比较目的与基线→披露自行加入避障→指出基线不允许尺度和旋转变化→构造公平度量；公平性解释在数据前。")],
"R03": [(1,21,"引言聚焦","解释不良前端如何让后端无可行解→区分后端难点→交代采用已有 MINCO→明确创新在前端；主动界定已有模块。"),(4,12,"算法段","输入与整体算法→逐行解释初始化、局部目标、迭代终止→后端初始化接口→转入采样子机制；算法说明与伪代码行号对齐。"),(6,5,"基准设置","基线类别→共同森林场景→明确原始环境不可用→按其描述重建随机过程→传感输入；复现限制先于性能比较。")],
"R04": [(2,6,"扩展问题链","旧方案在初始位置/分配不当时失效→重组织→一致性策略→整体队形引导→平台集成→贡献入口；每新增机制对应一个失效模式。"),(10,12,"系统协调段","先说明为何局部规划不能恢复队形→引入全局策略→解释通信收益→指出延迟循环依赖；长文为系统层冲突留独立论证。"),(11,12,"度量段","先提出公平评估队形变形的需求→求最优相似变换→归一化误差；评价定义承接方法允许的自由度。")],
"R05": [(2,23,"引言收束","终端状态/时间耦合→轻量约束转写→已有稀疏参数化与新消元协同→验证→贡献；用问题约束解释模块必要性。"),(4,10,"策略接口","列策略可用状态→输出捕获时间变量→PPO选择及依据→优化目标；动作接口先于学习公式。"),(7,19,"实机设置","网兜位置→计算平台→同机基线→场地/定位→状态估计→控制器；先说明物理捕获和计算比较的可复现条件。")],
"R06": [(2,18,"贡献收束","预测意图→预测运动→意图感知约束→模拟/实机验证；三个动词逐级推进预测到行动。"),(5,12,"增量机制段","明确沿用已发表可见性区域与路径初始化→指向其细节→说明新增意图约束；已有方法写短，新约束写长。"),(7,5,"条件与事件","固定初态/目标轨迹→给速度和加速度条件→随机急转试验→定位某次转弯图→解释提前避让；数据解读依赖具体事件。")],
"R07": [(2,0,"挑战段","传感成本→空地互补→一个感知 UAV 支援多个盲 UGV 的明确问题→定位/地图规划/调度三难点→指出基础设施假设边界。"),(3,1,"总览段","援助者/接收者关系→感知与定位→地图共享→碰撞预测和请求→UAV调度；输出通过消息回到下一个输入。"),(5,30,"仿真设置","动态约束→从实机测得的里程计噪声→观测与共享距离→密度和车数变化→评价指标；实验变量对应协作负担。")],
"R08": [(2,0,"贡献收束","指出大时间偏差使恒速假设失效→粗到细迭代→实证→三项贡献；先解释新增迭代为什么必要。"),(2,8,"推导路线","交代已有仅方位定位输入→加入时间偏差→恒速假设与新误差→连续优化→最小二乘→Schur 消元；段首给读者推导地图。"),(5,6,"实验路线","区分非迭代/迭代版本→解释时间偏差容忍度→对比无同步基线→移除不相关匿名假设以公平比较→实机与单核求解实现。")],
"R09": [(2,0,"任务约束链","连续捕获建模→队形适配→网尺寸/拓扑安全→稀疏变量和在线求解→仿真实机；任务物理条件贯穿论证。"),(4,34,"协作约束","先解释支撑网的运输目标→区分尺寸安全与拓扑安全→邻居距离限制→公式；约束从可理解的物理失败引出。"),(6,66,"比较解读","相同 Hybrid A* 初值→补充材料定位→机器人数量及多种效率指标→表格→解释稠密决策变量导致成本；不从单个时间数直接跳到优越结论。")],
"R10": [(2,0,"双层方法段","集中回答资源/通信挑战→CMP/MPS→资源约束下切换收益→上层整数决策→下层条件避障→并行求解→ROS/CARLA/实机；两层各有输出和证据。"),(3,1,"频率接口","本地/边缘规划器定义→决策低频、规划高频→先规划式再切换式的阅读路线；异步接口不藏在图注。"),(6,50,"实施段","软件和仿真连接→消息共享→场景→工作站→真实机器人传感/计算；端边方法要同时交代模拟与部署栈。")],
"R11": [(2,2,"挑战到贡献","接触安全几何→高阶动态可行性→统一时空优化→嵌入式部署→高速事件验证→贡献；模型复杂度由物理任务逼出。"),(5,20,"约束组开篇","回扣稳定跟踪需求→从典型失效归纳距离/角度/遮挡→宣布度量、惩罚、梯度→统一符号；读者先看三类失败再看数学。"),(11,28,"基线协议","按是否考虑可见性组织三基线→保持开源实现→同参数/目标轨迹→定义投影遮挡指标→共同环境；评价指标贴合被测机制。")],
"R12": [(2,1,"单主贡献","层级策略分解→已有规划器作为内环→相关范式定位→一个系统级主贡献→比较/实机→奖励设计难点；此例用连续段落，不强塞编号贡献。"),(3,19,"层级机制","固定保守速度限制的缺点→联合速度/轨迹优化动机→定义辅助动作和策略分解；用接口明确学习改变什么。"),(6,12,"实验控制","所提策略加同规划骨干→固定速度骨干→手工代价自适应基线→共享参数一致→比较与消融；不把不同骨干收益归因于策略。")],
"R13": [(1,8,"理论问题段","最少边全局刚性未解→任意删边损害队形→精确定义好稀疏图→子矩阵选择→NP难与启发式→复杂度和证据；理论约束引导算法选择。"),(3,38,"命题段","完整图和稀疏图对象→保持顶点、边为子集→给出刚性命题条件；数学承诺先限定对象。"),(6,1,"尺度评价","连接率和无人机数共同变化→共享硬件/环境→完整图误差为基准→相对误差定义；性能与计算缩放同时比较。")],
"R14": [(2,2,"长文机制链","重新参数化去除运动学约束→完整耦合平坦映射→实时规划与分组件安全→缆绳向量消元→不依赖载荷观测的分布式控制；方法篇幅来自不同科学接口。"),(6,52,"表示段","说明平坦映射避免动态积分→以多维多项式表示平坦输出→定义维数、段数和阶数→公式；每个表示参数先给任务含义。"),(13,7,"基准协议","说明所选 SOTA 与求解库→三障碍密度→共同起终点几何与多路径→约束一致性；比较条件比结果段更具体。")],
"R15": [(2,0,"传感选择论证","部署差距→传感器/表示也是设计变量→占据融合会丢细障碍的机制→激光雷达直接量测优势→结合 RL 的具体系统；动机不只说学习更快。"),(3,6,"表示构造","历史点云变换到当前机体坐标→角度分区→分辨率/维度→每区最近距离；图解释与可实现步骤配对。"),(5,13,"表示消融","定义占据图比较对象与分辨率→三维/二维编码器和相同特征维度→固定环境分布→训练配置变化→曲线；表示收益需要控制训练因素。")],
"R16": [(2,0,"硬件创新段","近距离干扰需求→翼面横向力原理→同轴紧凑构型→动力学/双模式控制→分别验证幕布、狭缝、倾斜悬停；机构属性逐个变为任务测试。"),(3,2,"几何度量","相同悬停效率下比较→定义尺寸用最小外接圆面积并说明规划含义→引用功率关系；设计指标不能随意选。"),(7,5,"动态响应试验","评价目的→悬停时连续姿态指令→变化率和幅度→前半保持、后半连续变化→两阶段意义→误差→任务含义；写事件设计再写数字。")],
"R17": [(1,7,"空间抽象段","原始点云/网格难→高度图单层局限→多层连续轨迹目标→可通行近平面洞见→建图→坐标表示与搜索→贡献；核心抽象从环境结构得到。"),(2,5,"算法接口","指向伪代码→输入全局点云→输出平面、变换、ESDF、相邻连线→坐标记号；先讲算法返回了什么。"),(3,3,"搜索机制","将起点投影到平面→连接该平面顶点→边代价入图→终点同处理→广度搜索连通路径；按可执行顺序解释。")],
"R18": [(3,1,"引言收束","先用地图精度与可扩展性指向首图，再引出贡献；系统结果承担进入方法的桥。"),(4,3,"总览段","Fig.2→两大模块与章节→第一模块的输入/输出→第二模块三步优化→相同 PGO 合并叙述、空间 BA 独立；章节划分由算法同异决定。"),(9,9,"多数据设置","统一 C++/ROS→公开和自采数据→如何切成未知相对变换会话→参数表→每数据的初始里程计来源；数据预处理属于比较协议。")],
"R19": [(2,13,"构型联合论证","动力变化和负载→形状感知规划→扩维前端→联合连续优化→抓物体积扩展→控制补偿；形变是状态变量，不只是示意图变化。"),(3,17,"搜索状态","固定尺寸点质量近似不合适→将半径形变纳入状态→解释避障/续航平衡→状态式；抽象变更在方程前说清。"),(6,37,"结果归因","指向多次规划均值和定义位置→解释最大尺寸不能利用通行性→最小尺寸持续收缩的代价；比较围绕构型权衡。")],
"R20": [(2,1,"端到端动机","数据驱动范式→意图/状态直达命令→避免显式模块的理由→轻量快速响应→固定初态难学→训练策略必要性；不把泛化宣言当创新。"),(5,26,"评价开篇","先课程消融→轨迹基线最优性/响应→动态航点速度→实机→训练/部署硬件；证据顺序按训练机制到执行收益展开。"),(5,0,"算法承载","训练重置策略独立伪代码承载；复用偏置重置的讲述位置，新的初态分布与学习规则必须来自项目。")],
"R21": [(2,1,"问题递进","变形指导不足→局部反应和恢复困难→多数工作不处理数量变化→新系统→DVS；先拆出数量与环境两个轴。"),(4,4,"分配段","数量变化时保持形状目标→下洗安全间距→按高度切片→按面积分配代理数→求和约束→近似原形；每步有物理或几何原因。"),(9,5,"能力边界","比较窄通道效率→三种基线→同环境初态约束→明确本比较不改变数量，因为基线无重新分配能力；不同能力分别验证。")],
"R22": [(2,1,"双模块创新","Doppler估计与结构化 RNN→碰撞预测驱动 MPC 调参→求解策略→端到端/跟踪/敏感性证据；网络与规划各有直接证据。"),(3,10,"方法开篇","一个模块降低状态预测不确定性、另一模块实时调安全距离→集成图→输入点云、输出动作；两模块分别回答两个量的误差。"),(5,18,"评价设置","ROS/CARLA及动态场景→基线/消融/敏感性→真实数据跟踪与受限平台→明确用真值框分组点云→训练数据规模；上游真值辅助须披露。")],
"R23": [(2,0,"两难点","视觉分布偏移→已有光流/随机化的代价→端到端几何线索→高保真训练与域适应→3DGS并行训练瓶颈；训练方法由部署失败倒推。"),(3,0,"实现改造","RL 大批量需求→改 3DGS pruning→解释椭圆与方框 tile 差异→重要性分数；优化实现要写计算原因。"),(5,8,"训练协议","并行环境/rollout→三阶段图→明确视觉 DR 与始终启用的动力随机化区别；实验缩写避免混淆两个被控因素。")],
"R24": [(2,0,"表示/计算双挑战","占据图缺语义、场景图缺几何记忆、语义值图缺长期能力→板载限制→几何/区域/对象逐层构图→分层探索；引言与框架分区互相对应。"),(3,5,"增量方法段","板载全局稀疏需求→引用空间骨架→指出全局批处理不适合局部增量→多面体增长与边界面→术语表；引用之后立刻说明新增差异。"),(6,6,"评价路线","地面平台方案迁移 UAV 的动态/视角困难→高保真任务→SOTA比较→消融→部署；实验需要解释迁移难点。")],
"R25": [(1,6,"混合机制引言","模块化成本→学习低延迟→安全/分布外限制→混合思路→训练模型奖励→部署安全机制；两处安全作用不能并成一个泛框。"),(2,9,"问题表示","定义 MDP tuple→状态到动作→控制步长与频率→子节阅读路线；架构描述先给实时接口。"),(5,1,"评价路线","训练奖励配置→未见环境部署消融→规划/学习基线→实机比较→室外高速；训练收益与执行安全分开验证。")],
"R26": [(3,1,"贡献收束","零样本导航系统→五维 benchmark→设计选择消融；此例含资源贡献，不把三项都写成网络机制。"),(3,8,"方法接口","图像/指令→视频采样→VLM选择→固定间隔图像→逆模型航点；引用工具沿接口顺序出现。"),(5,18,"研究问题开篇","四个明确问题：模型对比、动作提取、现实迁移、采样/提示可靠性；每个问题随后必须有相应实验。")],
"R27": [(2,0,"双设计轴","多样初值缓解局部最优→编码器的关键点与点云融合→截断扩散偏置分布→仿真效率/多样性→运行图→贡献；表示和训练框架两轴分开。"),(3,62,"编码接口","先声明预处理/编码/融合三部分→在图中定位→坐标变换→起终态符号与旋转矩阵；图位置是阅读导航。"),(6,35,"场景协议","引用机器人平台与自由度→三类环境→随机空间、几何体数→真实感数据裁切；仿真场景差异先于结果。")],
"R28": [(2,21,"能力到证据","机器人特定高层动作→已有学习无关专家执行→三类仿真场景→多模型无专门训练→收益→贡献；能力和训练范围先限定。"),(3,12,"分散状态接口","带发送者/时标更新→融合本地观测→候选去重与避让队友目标→不要求瞬时状态相同→定义高层动作；一致性含义具体化。"),(5,11,"异构协议","Unity/ROS实现→硬件→两个 UAV 和一个操作机器人→感知/交互能力非对称；比较须保留相同机器人能力。")],
"R29": [(2,1,"机制到叙述","硬件集成→飞行与形变规划分开→速度后果→状态反馈→变化负载和扰动→估计补偿→总图；系统叙述使用因果而非模块清单。"),(2,2,"结果主导开篇","仿生构型→结构原因→掌/指任务与子图→抓取范围→大/小物体例；先可观测能力，再逐项机制解释。"),(11,2,"讨论边界","整体能力与用途→外部定位/累积漂移限制→下一步自主性问题；限制具体指向当前依赖，不能照搬宏大应用宣言。")]
}

BLUEPRINTS = {
"R01": "目标跟踪系统短文：预测独立一节，搜索/优化合一节；Results先实现再事件实飞再基准。首图给追踪任务，方法图给丢失恢复闭环。借其事件叙述，不复制相机配置或性能。",
"R02": "紧凑编队优化：先唯一新度量，再两小节轨迹优化，Benchmark与实机/仿真分节。省略独立大 System Overview。与R04配对看哪些系统扩展值得独立篇幅。",
"R03": "前端几何创新：已有后端放Preliminaries；新前端细分球体、生成算法、重规划复用；实验按比较/消融/耗时/实机排列。全篇围绕两设计，不把已有MINCO写成贡献。",
"R04": "完整编队系统长文：System Overview后分别讲度量、局部优化、重组织、一致性；Benchmark五种能力对应四方法模块和效率，再大规模实飞。新增章节必须有独立失败情形与证据。",
"R05": "学习加规划Transactions：Problem Statement先固定捕获任务与动力学；高层时间决策、前端初值、终端柔性优化各独立一节。实机证据先行、模拟扩展随后；不强制所有论文模拟先行。",
"R06": "意图跟踪短文：总览很短，意图预测、运动预测、优化三个方法节按信息流排列；来源算法写引用，新增约束展开；急转和直行等事件分别解释安全/视野变化。",
"R07": "空地协作短文：一个Framework容纳定位、地图、地车规划、UAV调度四子节；实验变化环境密度与UGV数量；硬件收益要通过协作成本和任务成功验证。",
"R08": "估计推导短文：新联合误差一节、松弛与迭代求解一节；时间偏差和测量噪声分别扫变量；伪代码只给迭代过程，实机证明时间/位姿双目标。",
"R09": "协作任务正文加补充：正文先单体轨迹框架再协同捕获/运输约束，再Benchmark/实机；详细解释和比较补充放单独材料。23页PDF不能当23页正文模板。",
"R10": "端边协同长文：Formulation与Algorithm Designs分节，二层接口及不同频率明确；实验按基准、单机、多机、挑战赛、实机递进。通信/计算代价随任务结果一起写。",
"R11": "双任务统一长文：Overview/模型先共用；跟踪可见性和栖停接触机制各独立；共同优化再统一；模拟比较、事件案例、消融后实飞。既有会议版本扩展需要明确新增内容。",
"R12": "已证RA-L层级学习：Problem Formulation、Framework、外环RL、Training Setup、Experiments各短节；一个主贡献连续叙述。策略改变速度限制，已有内环不假装重造。",
"R13": "稀疏图机制短文：预备定义和架构→刚性命题→可计算图构造→效率/性能/消融；把规模数N和连接率一起实验。无实机段不能从此例推出已部署。",
"R14": "规划控制系统长文：动力学/参数化→安全与可行约束→求解→控制→比较/消融→真实运输。总览划清无人机/缆绳/载荷变量，公式多也须有对应几何解释。",
"R15": "感知到控制RL短文：一个Sim-to-Real方法大节与短Implementation；Results先表示受控消融再既有导航系统再实机；Conclusion把limitations连写，避免补不存在理论公式。",
"R16": "硬件短文：Design四子节逐层从构型到力再执行与硬件，Dynamics/Control随后；五种物理行为试验，连续响应和任务演示互补。首图展示真实机构能力。",
"R17": "空间表示短文：平面图构造与跨平面轨迹两节；定义输入输出及坐标变换；实验先复杂环境模拟、再基准、再实车。方法图重点是环境抽象，不套神经网络框。",
"R18": "建图系统长文：Overview→Loop Processing→Spatial BA→Two-step PGO；Experiments独立七类研究从单机、多机到机制消融/扩展性；证明单列Appendix。地图视觉与量化误差相配。",
"R19": "形变联合短文：Dynamic Model先行，Methodology四子节覆盖扩维搜索、联合优化、适应控制、舵机；实验必须区分固定大/小和自适应的权衡，不只展示穿洞视频。",
"R20": "直接控制RL短文：Methodology里动力学、问题、优化、迁移四子节；Evaluation先训练策略消融再动态响应再实机。伪代码为重置训练机制；不画不存在的传统轨迹规划接口。",
"R21": "数量适应编队中篇：系统接口单列，主要方法集中Deformable Guidance；数量变化与窄缝基准分开；实机和点云广播为两个部署证据。不要让基线承担其没有的数量适应能力。",
"R22": "已证RA-L监督估计加MPC：短Formulation→双模块Network→分别有两伪代码→Experiments四子节含真实数据、更多定量和限制；真实数据评估不自动等于自主实机飞行。",
"R23": "视觉RL短文：Training Pipeline与Sim-to-Real Transfer分节；先环境/RL再DA/DR；评价先消融再可视化差距再实飞。多阶段训练图不可变成部署期必需网络。",
"R24": "零样本语义导航短文：极短Overview→层次图构建→分层探索→实验；相关工作三子类与表示/策略问题对应。零样本不用RL训练曲线；源文Fig.x是待修错误，不模仿。",
"R25": "安全RL短文：Methodology四子节按问题、网络、奖励、HOCBF；Experiments从训练因素到未见场景到实飞。训练安全奖励与执行校正保留两个位置和两种证据。",
"R26": "视频导航单栏预印本：Methods三子節接口式展开，Experiments按四问题组织；Conclusion后Limitation、再References、再Appendix。模仿问题/证据路线，IEEE成稿须改回目标双栏模板。",
"R27": "扩散规划短文：Framework三子节编码器/截断扩散/后处理，Implementation两子节损失与采样；Results先协议和指标再定量；正文仿真充分但不虚构实机。",
"R28": "VLM协作双栏预印本：无编号一级标题，Method内信息流/初始化/记忆/探索/决策/规划；Experiments含受控同栈比较和模块剖析；大量prompt放Appendix。IEEE引用和编号需转换。",
"R29": "Nature Article叙事：无标题引言→Results按机构/控制/任务逐级→Discussion→Methods→可用性/References；迁移IEEE时保留照片-机制-曲线配对，将技术Methods前置并转换引用。不要照搬Nature顺序。"
}

FORMS = {
"R03": {"value":"CONFERENCE","venue":"IEEE/RSJ IROS 2022","status":"accepted","confidence":"explicit_pdf","evidence":"p1 b2 acceptance banner"},
"R04": {"value":"TRANSACTIONS","venue":"IEEE Transactions on Robotics","status":"accepted_author_report","confidence":"official_arxiv_author_metadata","evidence":"arXiv v2 Comments states accepted","url":"https://arxiv.org/abs/2210.04048v2","checked":"2026-10-02"},
"R05": {"value":"TRANSACTIONS","venue":"IEEE/ASME Transactions on Mechatronics","status":"accepted_author_report","confidence":"official_arxiv_author_metadata","evidence":"arXiv v2 Comments states accepted","url":"https://arxiv.org/abs/2302.04387v2","checked":"2026-10-02"},
"R10": {"value":"JOURNAL_UNSPECIFIED","venue":"UNKNOWN","status":"accepted","confidence":"explicit_pdf_dates_only","evidence":"p1 b4 manuscript received/revised/accepted; venue not given"},
"R12": {"value":"LETTER","venue":"IEEE Robotics and Automation Letters","status":"accepted_preprint","confidence":"explicit_pdf","evidence":"p1 b0 masthead and p1 b6 publication footnote"},
"R14": {"value":"TRANSACTIONS_SUBMISSION","venue":"IEEE Transactions on Robotics","status":"submitted_author_report","confidence":"official_arxiv_author_metadata","evidence":"arXiv v1 Comments states submitted, not accepted","url":"https://arxiv.org/abs/2501.15272v1","checked":"2026-10-02"},
"R22": {"value":"LETTER","venue":"IEEE Robotics and Automation Letters","status":"accepted_preprint","confidence":"explicit_pdf","evidence":"p1 b0 masthead and p1 b7 manuscript dates"},
"R26": {"value":"PREPRINT","venue":"UNKNOWN","status":"work_in_progress","confidence":"explicit_pdf","evidence":"p1 b10 says Work in progress; single-column morphology is separately measured"},
"R28": {"value":"PREPRINT_UNSPECIFIED","venue":"UNKNOWN","status":"unverified","confidence":"no_venue_confirmation","evidence":"local PDF is author-year, unnumbered-heading two-column manuscript; venue unstated"},
"R29": {"value":"NATURE_ARTICLE","venue":"Nature Communications","status":"published","confidence":"explicit_pdf_publisher","evidence":"p1 b0 Article and p1 b9 publisher banner; PDF subject DOI 10.1038/s41467-026-68967-3"}
}

EXTENDED = {"R04","R05","R10","R11","R14","R18","R21"}
CAUTIONS = {
"R02":"与R04是同一研究线的紧凑/扩展稿，不能计作独立风格共识，也不能仅由页长认定此文RA-L。",
"R04":"与R02的共同模型需成对阅读；外部接受声明不把本地作者版升级成出版社终版。",
"R09":"正文p1–8；p9–23是补充说明。Supplement出现重新编号图和大量说明，不混入正文页预算。",
"R11":"p2 b3明确整合先前会议文及新增内容；局部PDF未明示期刊名。官方arXiv相关DOI含TRO，不能仅以DOI前缀判定出版社终版。",
"R13":"标题及实验主要讨论大规模仿真与benchmark；本文不能作为所有编队工作必须实飞的证据。",
"R15":"未检出编号方程并不代表所有RL稿无需数学；本例是表示和系统证据主导。",
"R18":"证明在p16–17附录，与正文机制及实验分开；未从长文版式推定具体期刊。",
"R22":"真实Doppler数据与CARLA端到端评估分开；来源披露真值框用于点云分组。",
"R24":"源稿System Overview含Fig.x占位，不把源稿失误当风格规则。",
"R26":"正文至p9 Limitation；p9–12参考文献；p13–22附录。22页不是IEEE双栏22页预算。",
"R27":"本PDF实验以仿真为主，不能把真实感场景措辞改成机器人实机验证。",
"R28":"正文到p8开头；p8–9文献；p9–22附录。作者年引用及无编号一级标题只用于认知风格，IEEE格式必须重排。",
"R29":"Nature版正文与Methods顺序和参考文献格式不是IEEE格式；大图、图中文字编码异常使自动计数只能作代理。"
}
