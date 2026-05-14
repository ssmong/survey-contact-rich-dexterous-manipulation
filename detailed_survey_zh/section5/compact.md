### 5.1 Comp-ACT

**完整标题:** Compliance-Aware Action Chunking with Transformers for Contact-Rich Manipulation

**作者:** Tatsuya Kamijo, Kei Ota, Devesh K. Jha, Masayoshi Tomizuka (OMRON SINIC X / University of Tokyo)

**发表venue/年份:** IROS 2024

**K/D如何确定:** 通过ACT风格的Transformer策略进行模仿学习(IL)，基于VR遥操作示教训练。策略学习从示教数据中同时预测位置轨迹和刚度参数。刚度通过Cholesky分解参数化，以确保预测的刚度矩阵始终是对称正定的。不预测阻尼——阻尼通过固定阻尼比从刚度导出。

**输出内容:** 12D刚度输出：6x6笛卡尔刚度矩阵K参数化为下三角Cholesky因子(6D笛卡尔空间的12个独立元素，确保K = L L^T为SPD)。策略同时输出位置动作块(遵循ACT框架)。阻尼D不独立预测。

**机器人平台:** 双UR5e机械臂 + 平行夹爪。无灵巧手。

**任务:** Robosuite/MuJoCo仿真中的双手接触丰富装配和操作：轴孔插入、齿轮啮合、带柔顺的物体传递以及需要变化刚度曲线的多步装配序列。

**核心方法:** Comp-ACT通过添加柔顺预测头扩展了Action Chunking with Transformers (ACT)框架。Transformer编码器-解码器处理视觉观测和本体感觉，解码器输出动作块(时间范围内的位置轨迹)和刚度矩阵。Cholesky参数化至关重要：通过预测下三角因子L而非直接预测K，系统保证得到的刚度矩阵K = L L^T始终是对称正定的，这是稳定阻抗控制的物理要求。VR遥操作示教捕获位置轨迹和用户的意图柔顺性(从遥操作者的行为中推断)。

**架构/参数:** ACT架构(CVAE + Transformer编码器-解码器)。视觉编码器(ResNet-18或类似)用于图像观测。动作块大小遵循ACT惯例(~100步)。额外线性头用于12D Cholesky因子预测。基于Robosuite中采集的VR示教数据集训练。

**主要贡献:**
- 将学习型可变刚度预测集成到ACT模仿学习框架中
- Cholesky参数化保证物理有效(SPD)的刚度矩阵，避免退化或不稳定的阻抗预测
- 证明从示教中协同学习位置和刚度比仅位置ACT或固定刚度基线提高了接触丰富任务成功率

**局限/空白:**
- 无灵巧手——仅双UR5e配夹爪
- 阻尼不独立学习；通过固定比率从刚度导出
- 主要在仿真(Robosuite)中评估；真实机器人验证有限
- VR遥操作示教可能无法捕获真实期望刚度——"意图柔顺性"是推断的，非直接测量
- 不扩展到高自由度系统(如多指手)

**实验结果:** Comp-ACT在Robosuite的接触丰富装配任务上优于仅位置ACT和固定刚度ACT基线。学习到的刚度曲线显示出定性合理的模式(如搜索/对准阶段较低刚度，插入阶段较高刚度)。代码见github.com/omron-sinicx/CompACT。

## 推理/部署

- **推理延迟:** 未明确报告。架构遵循ACT (Action Chunking with Transformers)，额外线性头用于12D Cholesky因子预测，在标准ACT推理基础上增加的开销可忽略。ACT风格策略通常在桌面GPU上以10-50 Hz运行。
- **部署硬件:** 双UR5e臂。在Robosuite/MuJoCo仿真中训练和评估。策略推理的具体GPU未报告。
- **可实时运行?** 是，可能。轻量级ACT架构(ResNet-18编码器 + Transformer解码器)加上小型柔顺头应支持在典型操作频率(10-50 Hz)下的实时控制。动作分块进一步降低了推理频率要求。

## 数据集/数据采集

- **使用的数据集:** 在仿真(Robosuite/MuJoCo)中为双手任务采集的自定义遥操作示教，以及在双UR5e上采集的真实世界单臂和双手任务示教。
- **采集方法:** 使用HTC Vive Cosmos Elite控制器进行VR遥操作，配触觉反馈(振动触觉力反馈映射到控制器振动)。PyOpenVR以90 Hz进行位姿跟踪。机器人腕部力/力矩传感器测量提供触觉反馈。每次示教捕获笛卡尔轨迹、力/力矩传感器数据、柔顺参数(刚度值)、相机图像和夹爪指令。
- **数据规模:** 每个任务20-30次示教。仿真(双手擦拭)：30次示教。真实世界单臂和双手任务：各20-30次示教。共6个任务(1个仿真，5个真实世界)。
- **遥操作设备:** HTC Vive Cosmos Elite VR控制器配振动触觉反馈。
- **数据格式:** 未明确指定。包含笛卡尔末端执行器位姿、夹爪指令和每时间步期望柔顺度。
- **公开可用?** 代码见https://github.com/omron-sinicx/CompACT。示教数据集未明确发布。
