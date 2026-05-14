# 第3节：力感知VLA / 触觉VLA -- 概述

> 融合力/力矩或触觉感知以完成接触丰富任务的模型。本节涵盖使用VLM/VLA主干网络或语言条件化，并结合力/触觉模态的系统。不含VLM主干网络的力/阻抗聚焦系统见第5节。

## 本节论文

| # | 论文 | 力/触觉输入 | 力输出 | 机器人 | VLA? |
|---|------|------------|--------|--------|------|
| 3.1 | [ForceVLA](forcevla.md) | 六轴力/力矩 | 否（仅位置） | Flexiv Rizon 4 | 是 |
| 3.2 | [ForceVLA2](forcevla2.md) | 六轴力/力矩（300 Hz） | 是（完整力旋量） | Flexiv Rizon 4s | 是 |
| 3.3 | [FD-VLA](fd_vla.md) | 蒸馏力/力矩 | 否（仅位置） | UR5e | 是 |
| 3.4 | [FAVLA](favla.md) | 双六轴力/力矩 | 否（仅位置） | Monte双臂系统（X-ARM） | 是 |
| 3.5 | [HapticVLA](hapticvla.md) | 蒸馏触觉 | 否（仅位置） | LeRobot SO-101 | 是 |
| 3.6 | [DreamTacVLA](dreamtacvla.md) | 视觉触觉（V-JEPA2） | 否（仅位置） | Dobot Xtrainer | 是 |
| 3.7 | [OmniVTLA](omnivtla.md) | 视觉触觉 + 力触觉 | 否（仅位置） | 夹爪 + 灵巧手 | 是 |
| 3.8 | [Tactile-VLA](tactile_vla.md) | 触觉传感器 | 是（部分：混合位置-力） | 未指定 | 是 |
| 3.9 | [TaF-VLA](taf_vla.md) | GelSight + 六轴力/力矩 | 否（仅位置） | Franka FR3 | 是 |
| 3.10 | [TA-VLA](ta_vla.md) | 关节力矩（电机电流） | 辅助力矩预测 | Cobot Magic ALOHA | 是 |
| 3.11 | [CRAFT](craft.md) | 力传感 | 否（仅位置） | Franka Panda | 是 |
| 3.12 | [VLA-Touch](vla_touch.md) | GelSight触觉 | 否（残差修正） | 机械臂 + 夹爪 + GelSight | 是 |
| 3.13 | [FoAR](foar.md) | 六轴力/力矩 | 否（仅位置） | Flexiv Rizon | 否 |
| 3.14 | [FACTR](factr.md) | 关节力矩（电机电流） | 否（仅位置） | Franka Panda | 是 |
| 3.15 | [ForceMimic](forcemimic.md) | 捕获的交互力旋量 | 是（完整力旋量） | Flexiv Rizon | 否 |
| 3.16 | [Reactive Diffusion Policy](reactive_diffusion_policy.md) | GelSight Mini触觉 | 否（仅位置，类阻抗） | Flexiv Rizon 4 | 是 |
| 3.17 | [ACP](acp.md) | 六轴力/力矩（ATI） | 是（部分：标量刚度） | UR5e | 否 |
| 3.18 | [TacDiffusion](tacdiffusion.md) | 触觉传感器 | 是（完整力旋量：6D） | 夹爪 + 触觉 | 是 |
| 3.19 | [FARM](farm.md) | GelSight Mini触觉 | 是（部分：抓取力） | 改进型UMI夹爪 | 是 |
| 3.20 | [T-DEX](tdex.md) | DIGIT视觉触觉 | 否（仅位置） | Allegro Hand（16自由度）+ Kinova Jaco | 否 |

## 跨领域观察

### 1. 输入模态与输出模态的不对称性

20篇论文中一个显著的模式是力/触觉输入与力输出之间的不对称性。虽然所有20篇论文都使用力或触觉信息作为输入，但只有6篇产生了某种形式的力/阻抗输出。其余14篇仅将力/触觉作为输入来改善位置动作生成。这表明社区在力感知操作的"感知"方面已取得很大进展，但"执行"方面——主动命令力——仍然发展不足。

**力输出细分：**
- **完整力旋量输出（6D力 + 力矩）：** ForceVLA2、ForceMimic、TacDiffusion
- **部分力输出：** Tactile-VLA（混合位置-力）、FARM（仅抓取力）、ACP（仅标量刚度）

### 2. 传感器类型碎片化

这些论文涵盖了广泛的力/触觉传感器类型：六轴力/力矩传感器（ForceVLA、ForceVLA2、FAVLA、TaF-VLA、FoAR、ACP）、GelSight视觉触觉传感器（TaF-VLA、VLA-Touch、Reactive Diffusion Policy、FARM）、DIGIT类触觉传感器、来自电机电流的关节力矩（TA-VLA、FACTR）以及蒸馏/虚拟力（FD-VLA、HapticVLA）。目前没有关于哪种力/触觉模态最优的标准化结论，而且很少有论文进行跨传感器类型的比较。TaF-VLA是唯一融合两种力模态（GelSight + F/T）的论文，但它没有与使用其他传感器组合的论文进行比较。

### 3. 蒸馏趋势

三篇论文（FD-VLA、HapticVLA，以及部分包含辅助力矩预测的TA-VLA）探索了在训练时使用力/触觉数据但在推理时不需要传感器的方法。这种"力蒸馏"范式为在低成本机器人上部署力感知策略提供了一条实用路径，但从根本上限制了系统只能通过视觉推断接触——它无法对仅通过力/触觉感知才能观察到的真正意外接触事件做出反应。

### 4. 任务评估仍然狭窄

尽管横跨20篇论文，任务类型主要集中在插入任务（插头、USB、充电器、连接器）、擦拭/清洁和剥离。只有少数论文在更多样化的任务上进行了评估：TA-VLA（10项任务）、TaF-VLA（8项任务）、ForceVLA/ForceVLA2（各5项任务）。各论文使用的接触丰富任务基准不统一，使得直接比较变得困难。

### 5. 灵巧手缺口

T-DEX是唯一一篇在灵巧手（Allegro）上评估力/触觉操作并完成非简单接触丰富任务的论文。然而，T-DEX使用非参数最近邻策略，没有语言条件化——它不是VLA。目前没有任何具有语言条件化的VLA在多指灵巧手上针对简单抓放之外的接触丰富任务进行过评估（OmniVTLA除外）。

### 6. 时间尺度挑战

力和触觉信号的工作频率（100-1000 Hz）远高于典型的VLA推理速率（5-20 Hz）。各论文以不同方式处理这种不匹配：ForceVLA2在300 Hz F/T数据上使用时序卷积，Reactive Diffusion Policy使用慢-快双架构，FACTR使用力注意力Transformer层配合课程训练，大多数其他论文则简单地将力信号降采样以匹配VLA频率。弥合这些时间尺度的最优方法仍是一个开放问题。

### 7. 可复现性差异显著

在20篇论文中，约10篇公开发布了代码：ForceVLA、FoAR、FACTR、ForceMimic、Reactive Diffusion Policy、VLA-Touch、TacDiffusion、DreamTacVLA、T-DEX和FARM。其中，只有Reactive Diffusion Policy和VLA-Touch同时发布了代码和模型检查点。其余约10篇论文没有公开代码，限制了可复现性和后续研究的开展。

关于ForceVLA的说明：公开发布的主要是HuggingFace上的ForceVLA-Data数据集（244条轨迹）。模型代码（而非仅数据）是否公开可用应独立验证。

### 8. 机器人平台集中

Flexiv Rizon平台出现在20篇论文中的5篇（ForceVLA、ForceVLA2、FoAR、ForceMimic、Reactive Diffusion Policy），反映了其内置六轴力/力矩感知和柔顺控制能力。Franka Panda/FR3出现在3篇论文中（TaF-VLA、FACTR、CRAFT）。集中于少数平台限制了力感知VLA方法跨平台泛化的证据。

### 9. 力感知VLA在更广泛VLA领域中的定位

将第3节与第6节中的VLA基础模型进行比较，主要的VLA系列（pi0、GR00T N1、OpenVLA、Octo、RDT-1B）均不包含力/触觉输入或力输出。力感知VLA仍然是建立在这些基础模型之上或受其启发的专业化细分领域，而非集成到基础模型本身中。这表明力/触觉模态尚未被视为VLA预训练的必要组成部分，尽管它们对接触丰富任务非常重要。

### 10. 从反应式到预测式力推理

大多数论文以反应式方式使用力/触觉输入——根据当前接触状态调整动作。DreamTacVLA是一个值得注意的例外，它引入了一个触觉世界模型来预测未来的接触状态，并利用这些预测主动调整动作。这种预测方法对于预期力控制（例如，在预期碰撞前调整抓取力）很有前景，但除了这篇论文之外基本上未被探索。
