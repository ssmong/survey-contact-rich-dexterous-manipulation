# 9.5 Genesis

- **全称：** Genesis: A Universal and Generative Physics Engine for Robotics and Beyond
- **作者：** Genesis-Embodied-AI团队（多机构合作）
- **发表venue/年份：** 2024年12月（预印本，2025年1月发布性能基准报告）
- **仿真平台：** 自研多物理引擎
- **灵巧手支持：** 任意基于URDF的手部模型；支持刚体、可变形体和流体交互
- **物理求解器：** 刚体动力学、MPM（物质点法）、SPH（光滑粒子流体动力学）、FEM（有限元法）、PBD（基于位置的动力学）、Stable Fluid
- **性能：** 在单张RTX 4090上仿真Franka机械臂超过4300万FPS

## 核心方法/设计

Genesis被设计为通用物理平台，在单一API下统一了六种不同的物理求解器。它面向通用机器人和具身智能应用，同时作为物理引擎、机器人仿真平台、照片级渲染系统和生成式数据引擎。系统设计为完全可微（目前MPM和Tool Solver已支持，其他求解器计划中）。支持跨平台执行，包括CPU、NVIDIA/AMD GPU和Apple Metal。

## 主要贡献

- 统一的多物理引擎，在单一API下集成刚体、软体、流体和布料仿真
- 高仿真速度（刚体4300万+ FPS），通过GPU并行计算实现
- 可微仿真支持操作任务的基于梯度优化
- 跨平台支持（Linux、macOS、Windows），多种GPU后端可选
- 支持多种机器人类型（机械臂、足式机器人、无人机、软体机器人）和文件格式（.xml、.urdf、.obj、.glb、.ply、.stl）

## 局限性/不足

- 可微性目前仅限于MPM和Tool Solver；刚体和FEM求解器尚不可微
- 平台较新，社区采用度和预构建任务环境少于MuJoCo或Isaac Lab
- 灵巧操作的接触动力学精度尚未与成熟仿真器进行充分基准对比
- 照片级渲染能力已声明但尚未在仿真到真实视觉迁移中广泛验证

## 覆盖缺口

| 标准 | 是否覆盖？ |
|------|-----------|
| 力/力矩评估指标 | 否（尽管支持物理计算，但无标准化的力评估指标） |
| 可变形物体任务 | 是（MPM、FEM、PBD求解器支持可变形交互） |
| 触觉传感 | 否（无触觉传感器仿真模块） |
| 多阶段/长时程任务 | 否（无预构建的长时程任务套件；平台支持自定义任务） |
| 多手协调 | 否 |

## 开源状态

开源。通过 `pip install genesis-world` 安装。GitHub: [Genesis-Embodied-AI/Genesis](https://github.com/Genesis-Embodied-AI/genesis)
