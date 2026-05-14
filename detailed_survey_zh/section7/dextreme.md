### 7.2 DeXtreme

**完整标题：** DeXtreme: Transfer of Agile In-Hand Manipulation from Simulation to Reality

**作者：** Ankur Handa, Arthur Allshire, Viktor Makoviychuk, Aleksei Petrenko, Ritvik Singh, Jingzhou Liu, Denys Makoviichuk, Karl Van Wyk, Alexander Zook, Yashraj Narang, Jean-Francois Lafleche, Dieter Fox, Gavriel State

**发表venue/年份：** ICRA 2023（arXiv 2022）

**RL算法：** PPO（IsaacGym中大规模并行训练）；使用自动域随机化（ADR），在训练期间动态扩展随机化范围

**手部硬件：** Allegro Hand（16自由度）

**仿真平台：** IsaacGym

**仿真到真实？** 是；用于仿真到真实迁移的自动域随机化（ADR）（真实）。ADR在策略性能足够时自适应增加随机化范围，推动策略走向更广泛的鲁棒性。辅以随机化视觉观测

**物体数量：** 立方体及其他简单物体；关注迁移质量而非物体多样性

**任务：** 手内立方体旋转至目标姿态（基于OpenAI魔方系列）

**核心方法论：** 将NVIDIA基于IsaacGym的训练扩展到Allegro Hand，配合自动域随机化（ADR）。ADR从窄随机化范围开始，随着策略学习逐步加宽，避免了过于挑战性的初始随机化阻碍学习的问题。系统在大规模（数千并行环境）下训练，实现鲁棒仿真到真实迁移而无需手动域随机化调优。

**主要贡献：**
- 自动域随机化（ADR）消除了手动调节随机化范围的需求
- 首次在Allegro Hand上展示仿真到真实手内操作（真实）（先前工作使用Shadow Hand）
- 大规模并行训练基础设施支持快速策略迭代

**局限性/差距：** 仅限简单物体（主要是立方体）；仅Allegro Hand；无触觉传感；ADR训练计算成本高；仅限重定向任务，无平移或功能性操作目标

## 推理 / 部署

- **推理延迟：** 未明确报告。MLP策略每次前向传播 <1ms，支持高频控制。
- **部署硬件：** Allegro Hand（16自由度）。策略在IsaacGym中大规模训练；通过ADR零样本仿真到真实迁移部署。
- **支持实时？** 是。基于MLP的RL策略可轻松实现实时灵巧控制。已在真实Allegro Hand上验证。

## 数据集 / 数据收集

- **使用的数据集：** 无预收集数据集。纯RL（PPO）+ 自动域随机化（ADR）——所有数据在仿真中生成。
- **收集方法：** IsaacGym中大规模纯RL（数千并行环境）。ADR随策略性能提升自适应加宽随机化范围。无演示。Allegro Hand上零样本仿真到真实迁移。
- **数据规模：** 大规模并行训练。立方体和简单物体用于训练/评估。
- **遥操作设备：** 不适用（纯RL，无演示）。
- **数据格式：** 不适用（在线RL，无离线数据集）。
- **是否公开？** 代码发布状态未报告。
