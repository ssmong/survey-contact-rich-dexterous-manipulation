### 5.10 IndustReal

**完整标题:** IndustReal: Transferring Contact-Rich Assembly Tasks from Simulation to Reality

**作者:** Bingjie Tang, Michael A. Lin, Iretiayo Akinola, Ankur Handa, Gaurav S. Sukhatme, Fabio Ramos, Dieter Fox, Yashraj Narang (NVIDIA NVLabs)

**发表venue/年份:** RSS 2023

**K/D如何确定:** 固定(手动调节)。IndustReal使用固定阻抗控制器作为底层执行器。RL智能体(PPO)学习由阻抗控制器以恒定K和D跟踪的期望位姿。阻抗参数针对特定装配任务手动调节。核心贡献不是阻抗学习，而是固定阻抗下接触丰富装配的仿真到现实迁移。

**输出内容:** RL策略生成的期望末端执行器位姿(位置目标)。阻抗控制器中的刚度K和阻尼D是固定常数，不是学习策略的输出。

**机器人平台:** Franka Emika Panda + 平行夹爪。无灵巧手。

**任务:** 工业装配任务：NIST轴孔插入(圆形、方形、三角形)、齿轮啮合、PCB连接器插入。这些是标准化的接触丰富装配基准测试。

**核心方法:** IndustReal通过结合三种技术来解决接触丰富装配的仿真到现实迁移：(1) IsaacGym中基于SDF的接触仿真以实现逼真的接触建模，(2) 柔顺感知策略训练，RL智能体使用与部署中相同的阻抗控制器进行训练，(3) 使用标准化NIST装配板的自动化真实世界评估。固定阻抗控制器在仿真和现实之间提供一致的接口，减少接触丰富任务的仿真-现实差距。RL智能体学习利用阻抗控制器的柔顺性进行插入(如由横向柔顺性实现的螺旋搜索模式)。

**架构/参数:** IsaacGym中GPU并行化环境的PPO训练策略。策略MLP：~256-256。动作空间：6D期望末端执行器位姿。固定笛卡尔阻抗控制器(手动调节K, D)。基于SDF的接触仿真。在Franka Panda配NIST装配板上进行真实机器人评估。

**主要贡献:**
- 使用RL + 固定阻抗控制展示了接触丰富工业装配的成功仿真到现实迁移
- IsaacGym中基于SDF的接触仿真提高了装配任务的接触建模保真度
- 使用标准化NIST装配基准的自动化真实世界评估框架
- 开源代码和训练的RL策略(github.com/NVlabs/industreallib)

**局限/空白:**
- 固定K和D(手动调节)——阻抗未学习或适配
- 无灵巧手——Franka + 夹爪
- 每种装配类型需要任务特定的阻抗调节
- RL策略范围窄：按任务训练，无跨任务泛化
- 未展示可变阻抗；柔顺有用但是静态的

**实验结果:** IndustReal在NIST装配任务的仿真到现实迁移中取得了高成功率：圆形轴孔插入>90%，齿轮啮合>85%，零真实世界训练数据。固定阻抗控制器对成功的仿真到现实迁移至关重要——位置控制基线因接触敏感性而失败。代码和RL策略见github.com/NVlabs/industreallib。

## 推理/部署

- **推理延迟:** 未明确报告。RL策略是标准MLP(~256-256)，每次前向传播<1ms。训练使用GPU并行化IsaacGym环境。
- **部署硬件:** Franka Emika Panda用于真实机器人评估。在NVIDIA GPU上的IsaacGym中训练。MLP策略足够轻量，可部署在任何计算平台上。
- **可实时运行?** 是。MLP策略以高频生成期望末端执行器位姿，固定笛卡尔阻抗控制器以Franka原生1 kHz控制率运行。在NIST装配任务上成功演示了真实机器人部署。

## 数据集/数据采集

- **使用的数据集:** 无预采集数据集。仿真中的纯RL——所有训练数据通过基于SDF接触建模的GPU并行化IsaacGym仿真生成。零真实世界训练数据。
- **采集方法:** IsaacGym中基于SDF接触仿真的纯RL(PPO)。无人类示教。在Franka Panda配NIST装配板上评估仿真到现实迁移。柔顺感知策略训练在仿真和部署中使用相同的阻抗控制器。
- **数据规模:** IsaacGym中的大规模并行RL训练。未报告具体回合数。在标准化NIST装配基准(圆形、方形、三角形轴；齿轮啮合；PCB连接器插入)上评估。
- **遥操作设备:** 不适用(纯RL，无示教)。
- **数据格式:** 不适用(在线RL，无离线数据集)。
- **公开可用?** 是——代码和训练的RL策略见https://github.com/NVlabs/industreallib
