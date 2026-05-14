### Diffusion Policy: Visuomotor Policy Learning via Action Diffusion

**完整标题：** Diffusion Policy: Visuomotor Policy Learning via Action Diffusion

**作者：** Cheng Chi, Siyuan Feng, Yilun Du, Zhenjia Xu, Eric Cousineau, Benjamin Burchfiel, Shuran Song (Columbia University)

**发表期刊/年份：** RSS 2023

**架构：** Diffusion Policy将去噪扩散概率模型（DDPM）适配于机器人动作生成。提出两种架构变体：(1) 基于CNN的变体，在动作序列上使用1D时间卷积（类似1D U-Net），(2) 基于transformer的变体，transformer解码器关注观测特征并去噪动作token。两者都以视觉观测（来自ResNet或ViT编码器）作为条件输入。模型轻量级：CNN变体约25M参数；transformer变体约40M。

**动作空间：** 连续，可变维度。通常从2D（平面推动）到7D（6自由度EEF + 夹爪）。关键创新是"动作块化"——在单次去噪过程中预测T个未来动作（通常T=8-16），然后仅执行前几步后重新规划。这种时间动作抽象实现平滑、时间连贯的行为。

**灵巧手支持？** ✗ --- 为基于夹爪的操作设计和评估。然而，连续动作空间和动作块化框架已被后续灵巧手策略（DP3, iDP3）采用。

**力/阻抗输出？** ✗ --- 仅位置目标。后续工作（TacDiffusion, Reactive Diffusion Policy）已将扩散框架扩展到力域输出。

**核心方法论：** Diffusion Policy将视觉运动策略学习视为条件去噪问题：给定视觉观测，策略通过迭代将随机噪声向量去噪为连贯的动作轨迹。这种公式化方法自然处理动作分布中的多模态性（例如从左侧或右侧绕过障碍物），这是基于MSE的行为克隆的关键失败模式。动作块化机制生成时间连贯的动作序列，避免单步策略的抖动行为。去噪过程在推理时使用DDPM的10-100个扩散步骤，DDIM加速可将其减少到5-10步。

**训练数据：** 从头开始在任务特定演示数据集上训练。原始论文使用Push-T（200个episode）、robomimic任务和真实机器人桌面操作演示。通常每个任务需要50-500个演示。

**主要贡献：**
- 将扩散模型引入机器人动作生成，建立了自然处理多模态动作分布的视觉运动策略学习新范式。
- 为扩散策略提出动作块化，实现时间连贯的行为和稳定的闭环控制。
- 证明扩散策略在仿真和真实操作任务上均显著优于行为克隆、基于能量的模型和单步策略。

**定量结果：**

| 基准/任务 | Diffusion Policy（CNN） | Diffusion Policy（Transformer） | BC基线 | 备注 |
|---|---|---|---|---|
| *（请查阅RSS 2023论文获取Push-T、robomimic和真实机器人基准上的逐任务结果。论文报告相比行为克隆和基于能量的模型基线有显著改进。）* | | | | |

**局限性/差距：**
- 多步去噪引入推理延迟（每个动作块10-100ms，取决于扩散步数），对高频灵巧控制可能造成问题。
- 基础模型无语言条件化（仅任务特定训练）。
- 需要从头进行任务特定训练；原始公式化方案无跨任务或跨具身泛化。
- 无力/柔顺感知。

**开放权重/代码：** ✅ 代码：[GitHub](https://github.com/real-stanford/diffusion_policy)。✗ 无预训练权重（每个任务需从头训练）。

## 推理/部署

- **推理延迟：** 每个动作块10-100ms，取决于扩散步数。使用DDIM加速（5-10步而非100步），CNN变体（约25M参数）在桌面GPU（RTX 3090级别）上达约10-20 Hz。Transformer变体（约40M参数）略慢。动作块化（预测8-16个未来步骤）降低了有效推理频率需求。
- **部署硬件：** 桌面GPU（NVIDIA RTX 3090/4090或同级）用于实时推理。轻量级模型大小（25-40M参数）使消费级硬件部署成为可能。未报告边缘设备（Jetson）基准数据，但小模型大小暗示可行性。
- **可实时运行？** 是，使用DDIM加速。在5-10个去噪步骤下达10-20 Hz，Diffusion Policy支持典型操作任务的实时控制。使用完整100步DDPM时推理太慢（约1-5 Hz）。动作块化进一步降低所需推理频率。

## 数据集/数据收集

- **使用的数据集：** 任务特定演示数据集。Push-T（200个episode）、robomimic基准任务（lift, can, square, transport）和自定义真实机器人桌面操作演示。
- **收集方法：** 通过遥操作或脚本策略收集的人类演示。Push-T：脚本化。Robomimic：人类遥操作（SpaceMouse）。真实机器人：在UR5或Franka上使用SpaceMouse/键盘遥操作。
- **数据规模：** 每个任务50-500个演示。Push-T：200个episode。Robomimic：标准数据集大小（每个任务200-300个episode）。从头开始的任务特定训练（无跨任务预训练）。
- **遥操作设备：** 真实机器人演示使用SpaceMouse和键盘。Robomimic使用其标准的熟练人类（PH）和多人类（MH）演示集。
- **数据格式：** HDF5（robomimic格式）和zarr（Diffusion Policy原生格式）。
- **是否公开？** 是。Push-T和robomimic数据集公开可用。Diffusion Policy代码在 https://github.com/real-stanford/diffusion_policy 。

---
