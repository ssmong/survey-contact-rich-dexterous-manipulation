# 9.2 MuJoCo Playground

- **全称：** MuJoCo Playground
- **作者：** Google DeepMind MuJoCo团队（Kevin Zakka、Baruch Tabanpour及合作者）
- **发表venue/年份：** RSS 2025（系统演示方向）
- **仿真平台：** MuJoCo MJX（JAX加速的MuJoCo）
- **灵巧手支持：** 包含LEAP Hand任务；通过MuJoCo标准模型库可使用Shadow Hand变体
- **任务：** 运动控制、灵巧操作（手内重定向、方块旋转）、全身控制；单GPU上可在数分钟内完成训练

## 核心方法/设计

MuJoCo Playground利用MuJoCo MJX（MuJoCo物理引擎的JAX编译版本），实现完全在GPU/TPU上运行的大规模并行仿真。它提供了一组精选的环境，包含奖励函数和训练脚本，展示了如何在数分钟而非数小时内从零开始训练策略。系统强调利用MuJoCo精确的接触动力学实现零样本仿真到真实迁移。

## 主要贡献

- 证明了精确的接触物理（MuJoCo）结合JAX编译可在消费级硬件上数分钟内训练灵巧策略
- 预构建的LEAP Hand操作环境，附带零样本仿真到真实迁移结果
- 基于浏览器的可视化和交互式环境探索

## 局限性/不足

- 与ManiSkill3或Isaac Lab相比，任务多样性较窄；侧重于展示速度而非全面基准测试
- 无内置触觉仿真或可变形物体支持
- 相比成熟平台，文档和社区采用度仍在增长中

## 覆盖缺口

| 标准 | 是否覆盖？ |
|------|-----------|
| 力/力矩评估指标 | 否 |
| 可变形物体任务 | 否 |
| 触觉传感 | 否 |
| 多阶段/长时程任务 | 否（专注于单目标任务如方块旋转） |
| 多手协调 | 否 |

## 开源状态

基于Apache 2.0协议开源。通过 `pip install playground` 安装。GitHub: [google-deepmind/mujoco_playground](https://github.com/google-deepmind/mujoco_playground)
