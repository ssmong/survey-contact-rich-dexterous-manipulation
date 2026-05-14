# 9.8 Isaac Lab

- **全称：** Isaac Lab（前身为Orbit）: A Unified and Modular Framework for Robot Learning
- **开发者：** NVIDIA（Isaac Sim团队）；从Orbit（Mittal等，IEEE RA-L 2023）演化而来，取代已弃用的IsaacGym（Preview 4）
- **发表venue/年份：** IEEE RA-L 2023（Orbit论文）；Isaac Lab品牌重塑和重大更新2024年
- **仿真平台：** 基于NVIDIA Isaac Sim构建，由PhysX 5驱动（GPU加速）
- **灵巧手支持：** Allegro Hand、Shadow Hand及任意基于URDF/MJCF的手部模型；开箱即用支持铰接手部环境
- **物理引擎：** PhysX 5，支持GPU并行刚体和可变形体仿真
- **性能：** 单GPU支持数千个并行环境；速度可比IsaacGym，API设计更优

## 核心方法/设计

Isaac Lab是NVIDIA的统一机器人学习框架，基于Isaac Sim构建，设计为IsaacGym（Preview 4之后弃用）和早期Orbit框架的继任者。它提供模块化、可扩展的API用于创建GPU并行化的机器人学习环境。框架支持强化学习、模仿学习和仿真到真实迁移工作流。与IsaacGym的独立Python API不同，Isaac Lab与完整的Isaac Sim生态系统集成，提供照片级渲染（RTX光线追踪）、领域随机化、传感器仿真（相机、LiDAR）和资产管理。环境API遵循gymnasium兼容接口，支持向量化（并行）执行。

## 主要贡献

- 取代已弃用的IsaacGym（Preview 4），成为NVIDIA维护的机器人学习仿真框架
- 通过PhysX 5实现GPU并行环境执行，单GPU可运行数千个同步环境
- 模块化设计：通过配置实现可互换的机器人、传感器、任务和奖励函数
- 通过RTX实现照片级渲染，用于视觉仿真到真实迁移
- 内置灵巧手平台（Allegro、Shadow）支持，附带预配置环境
- 兼容主流强化学习库（rl_games、RSL-rl、SKRL、Stable Baselines3）

## 在综述论文中的使用

Isaac Lab（或其前身Isaac Sim / IsaacGym）是本综述中多个系统的仿真平台：
- **GR00T-Dexterity**（第7节）：在Isaac Lab中进行Allegro Hand强化学习训练
- **DextrAH-G/RGB**（第7节）：在Isaac Lab中使用Allegro Hand + Kuka及几何结构
- **CHIP**（第5节）：在Isaac Sim中进行人形阻抗策略训练
- **GR00T N1**（第6节）：在Isaac Lab中进行策略评估和仿真到真实迁移
- **TeleOpBench**（第9节）：基于Isaac Sim构建的遥操作基准

## 与IsaacGym的关系

IsaacGym（Preview 1-4）是NVIDIA的独立GPU并行强化学习仿真库，广泛用于灵巧操作研究（手内旋转、DexPBT、HORA等）。IsaacGym现已弃用且不再维护。Isaac Lab以更模块化的架构取代它，基于完整的Isaac Sim平台构建。主要区别：
- IsaacGym：独立Python库，渲染有限，无传感器仿真
- Isaac Lab：完整Isaac Sim集成，RTX渲染，相机/LiDAR仿真，领域随机化
- 迁移：大多数IsaacGym环境可通过API更改移植到Isaac Lab；NVIDIA提供迁移指南

## 局限性/不足

- 需要NVIDIA GPU（不支持AMD/Intel）；绑定NVIDIA专有的Isaac Sim平台
- 安装占用空间大于MuJoCo或Genesis（需要Isaac Sim，多GB级别）
- 闭源物理引擎（PhysX）：接触不可微（不同于Genesis或DiffTactile）
- 无内置触觉传感器仿真（需要外部插件）
- 学习曲线：API比IsaacGym的简单独立接口更复杂
- 完整功能仅支持Linux（Windows支持部分功能）

## 覆盖缺口

| 标准 | 是否覆盖？ |
|------|-----------|
| 力/力矩评估指标 | 否（力传感可用但无标准化力评估） |
| 可变形物体任务 | 是（PhysX 5支持软体） |
| 触觉传感 | 否（无内置触觉仿真；需要外部插件） |
| 多阶段/长时程任务 | 部分（基于管理器的任务API支持多阶段，但预构建示例较少） |
| 多手协调 | 部分（可实现双臂设置但基准测试不充分） |

## 开源状态

基于BSD-3-Clause许可证开源。通过 `pip install isaaclab` 安装（需要Isaac Sim）。GitHub: [isaac-sim/IsaacLab](https://github.com/isaac-sim/IsaacLab)。文档：[isaac-sim.github.io/IsaacLab](https://isaac-sim.github.io/IsaacLab/)
