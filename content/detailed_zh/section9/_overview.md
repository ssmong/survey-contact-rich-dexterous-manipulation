# 第9节：仿真基准与平台

仿真环境是灵巧操作研究的基础设施。它们支持大规模并行强化学习训练、安全的策略评估以及仿真到真实的迁移流程。本节综述了专门支持多指手操作或提供与灵巧任务相关的可微接触物理的平台。

## 条目

| 条目 | 平台 | 灵巧手支持 | 核心优势 |
|------|------|-----------|---------|
| [ManiSkill3](maniskill3.md) | SAPIEN / PhysX 5 | Allegro、DClaw、任意URDF | GPU并行加速（430倍）、统一的RL/IL/VLA基线 |
| [MuJoCo Playground](mujoco_playground.md) | MuJoCo MJX (JAX) | LEAP Hand、Shadow Hand | 分钟级训练、零样本仿真到真实迁移 |
| [MuJoCo Manipulus](mujoco_manipulus.md) | MuJoCo | 多指工具操作 | 首个专用灵巧工具使用基准（16个任务） |
| [Adroit](adroit.md) | MuJoCo | Shadow Hand（24自由度） | 经典强化学习基准（笔、门、锤子、球） |
| [Genesis](genesis.md) | 自研多物理引擎 | 任意URDF | 统一多物理引擎（6个求解器）、4300万+ FPS |
| [DiffTactile](difftactile.md) | 自研可微引擎 | 仅平行夹爪 | 基于FEM的可微触觉仿真 |
| [TeleOpBench](teleopbench.md) | Isaac Sim | 3种人形体 | 首个双臂灵巧遥操作基准（30个任务） |
| [Isaac Lab](isaac_lab.md) | Isaac Sim (PhysX 5) | Allegro、Shadow、任意URDF | IsaacGym继任者；GPU并行、RTX渲染、模块化API |
| [TACTO](tacto.md) | PyBullet + PyRender | 夹爪（DIGIT/GelSight传感器仿真） | 基于视觉的触觉传感器图像仿真 |

## 观察

灵巧操作的仿真生态正沿三个轴线分化：(1) **速度** -- GPU并行引擎（ManiSkill3、MuJoCo Playground、Genesis）现在可在数分钟内训练策略；(2) **物理保真度** -- 可微引擎（Genesis、DiffTactile）支持通过接触进行基于梯度的优化；(3) **任务覆盖** -- 专用基准（Manipulus用于工具使用、TeleOpBench用于遥操作、Adroit用于强化学习基线）针对特定的能力缺口。目前尚无单一平台能同时融合GPU并行速度、可微接触物理、高保真触觉仿真和全面的灵巧任务套件。DiffTactile提供了最详细的触觉物理但缺乏GPU并行性；ManiSkill3提供了最佳的并行强化学习基础设施但触觉支持极少。Genesis致力于统一但仍在成熟中。尽管已有近十年历史，Adroit仍是默认的强化学习评估目标，这既体现了标准化基准的价值，也反映了社区向新平台迁移的缓慢。
