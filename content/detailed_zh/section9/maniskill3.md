# 9.1 ManiSkill3

- **全称：** ManiSkill3: GPU Parallelized Robotics Simulation and Benchmark with Enhanced Visual and Contact-Rich Environments
- **作者：** Stone Tao, Fanbo Xiang, Arth Shukla, Yuzhe Qin, Xander Gao, Hao Su 及合作者（UCSD、Stanford等）
- **发表venue/年份：** RSS 2025（arXiv 2410.00425，2024年10月）
- **仿真平台：** SAPIEN，搭载GPU并行物理引擎（PhysX 5）和渲染
- **灵巧手支持：** Allegro Hand、DClaw；可扩展至任意URDF手部模型
- **任务：** 20+任务族，涵盖刚体、可变形体和流体操作；包含灵巧手内重定向和多指抓取环境
- **性能：** 比前代ManiSkill版本快达430倍；单GPU支持数千个并行环境

## 核心方法/设计

ManiSkill3重新设计了仿真循环，充分利用GPU并行性进行物理步进和视觉渲染。它封装了SAPIEN的PhysX 5后端，可同时运行数千个环境，使以往需要数天的强化学习训练在数分钟内完成。该框架提供统一的Gym兼容API，内置RL（PPO、SAC）、模仿学习和VLA评估的基线。

## 主要贡献

- GPU并行仿真在刚体任务上实现相比ManiSkill2的430倍加速，在软体和流体任务上也有显著提升
- 统一基准，涵盖RL、IL（Diffusion Policy、ACT）和VLA（RT-2、Octo）基线，便于标准化比较
- 增强的接触丰富环境，改进了碰撞检测和摩擦建模，适用于灵巧操作任务

## 局限性/不足

- 触觉传感仿真有限；不原生支持高分辨率触觉传感器模型（如GelSight、DIGIT）
- 软体仿真虽支持，但比刚体慢且灵巧任务的基准测试不够充分
- 灵巧手任务的仿真到真实迁移结果在论文中未做充分验证

## 覆盖缺口

| 标准 | 是否覆盖？ |
|------|-----------|
| 力/力矩评估指标 | 否 |
| 可变形物体任务 | 是（包含软体和流体任务，但灵巧手场景基准测试较少） |
| 触觉传感 | 否（无原生触觉传感器模型） |
| 多阶段/长时程任务 | 部分（有一些多步骤任务，但无系统的长时程任务套件） |
| 多手协调 | 否 |

## 开源状态

完全开源。通过 `pip install mani-skill` 安装。GitHub: [haosulab/ManiSkill](https://github.com/haosulab/ManiSkill)
