### 7.2 Dactyl (OpenAI)

**完整标题：** Learning Dexterous In-Hand Manipulation

**作者：** Marcin Andrychowicz, Bowen Baker, Maciek Chociej, Rafal Jozefowicz, Bob McGrew, Jakub Pachocki, Arthur Petron, Matthias Plappert, Glenn Powell, Alex Ray, Jonas Schneider, Szymon Sidor, Josh Tobin, Peter Welinder, Lilian Weng, Wojciech Zaremba (OpenAI)

**发表venue/年份：** arXiv 2018 (1808.00177)；扩展版本发表于IJRR 2020

**arXiv：** https://arxiv.org/abs/1808.00177

**RL算法：** PPO（分布式，与OpenAI Five相同系统）；LSTM策略 + 非对称Actor-Critic（Critic中使用特权信息）

**手部硬件：** Shadow Dexterous Hand（24自由度）安装在固定底座上

**仿真平台：** MuJoCo（OpenAI定制仿真环境）

**仿真到真实？** 是。对50+物理参数（摩擦、质量、重力、执行器增益、观测噪声等）进行大规模自动域随机化（ADR）。完全在仿真中训练的策略零样本迁移到真实Shadow Hand。基于视觉的变体使用随机化视觉外观进行感知的仿真到真实迁移。

**任务：** 手内物体重定向：旋转立方体以达到目标面朝向。方块必须重定向以匹配随机采样的目标姿态序列。

**核心方法论：** 在仿真中训练循环RL策略（LSTM + PPO），跨物理参数、视觉外观和观测噪声进行广泛自动域随机化。关键洞见是充分的仿真参数随机化可产生足够鲁棒的策略用于零样本仿真到真实迁移。LSTM从交互历史隐式执行系统辨识，适应真实世界动力学而无需显式校准。

**主要贡献：**
- 首次在物理拟人手（Shadow Hand）上展示灵巧手内操作的仿真到真实RL
- 引入自动域随机化（ADR）作为高自由度操作的可扩展仿真到真实方法论
- 展示纯RL学习的涌现灵巧行为（手指步态、手指枢转、多指协调），无需演示
- 建立仿真到真实域随机化作为高自由度灵巧操作的可行方法论，影响后续工作（Hora、DeXtreme、DexPBT等）

**定量结果：**

| 指标 | 数值 |
|---|---|
| 连续成功旋转 | 连续50次（真实） |
| 面重定向成功 | 训练目标集~100%（仿真）；除50次连续旋转演示外未明确报告定量真实世界成功率。 |
| 域随机化参数 | 50+随机化维度 |
| 手部自由度 | 24（Shadow Dexterous Hand） |
| 训练 | ~100年仿真经验（分布式） |

**局限性/差距：**
- **力控：** 无力/扭矩传感或阻抗控制；仅位置驱动
- **VLA/语言：** 无视觉-语言集成；纯基于状态或基于视觉的RL
- **仿真到真实：** 需要大量计算用于域随机化；ADR不保证覆盖所有真实世界条件
- **代码：** 未公开发布；Shadow Hand硬件昂贵（~$100K+），限制可复现性
- **任务范围：** 仅限方块旋转；不泛化至多样物体或功能性操作
- **传感：** 无触觉反馈；依赖指尖位置传感和（可选的）RGB视觉
- 仅在单一立方体上训练；无物体形状泛化
- 需要大量分布式计算（~100年仿真经验，~6000 CPU核）；大多数实验室无法复现
- Shadow Hand成本~$100K+，限制复现

## 推理 / 部署

- **推理延迟：** 未明确报告。LSTM策略每次前向传播（含循环状态更新）<5ms。系统在Shadow Hand上以实时控制速率运行。
- **部署硬件：** Shadow Dexterous Hand（24自由度）固定底座。策略在MuJoCo中以大规模分布式计算训练；通过ADR零样本仿真到真实迁移部署。
- **支持实时？** 是。在物理Shadow Hand上展示了实时手内物体旋转。LSTM策略支持Shadow Hand原生伺服速率的实时控制。
