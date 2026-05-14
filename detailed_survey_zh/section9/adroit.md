# 9.4 Adroit

- **全称：** Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations
- **作者：** Aravind Rajeswaran, Vikash Kumar, Abhishek Gupta, Giulia Vezzani, John Schulman, Emanuel Todorov, Sergey Levine
- **发表venue/年份：** RSS 2018
- **仿真平台：** MuJoCo
- **灵巧手支持：** Shadow Hand（24自由度）仿真模型（称为ADROIT手）
- **任务：** 4个经典任务——笔旋转、开门、锤击、球体转移
- **演示数据：** 每个任务25个通过CyberGlove收集的人类演示

## 核心方法/设计

Adroit提出了DAPG（Demo Augmented Policy Gradient，演示增强策略梯度）算法，将少量人类演示与强化学习微调相结合，解决复杂的灵巧操作任务。MuJoCo中的Shadow Hand模型成为灵巧强化学习基准测试的事实标准。人类演示通过CyberGlove遥操作接口收集，用于初始化策略，克服了高维灵巧动作空间的探索挑战。

## 主要贡献

- 建立了灵巧强化学习的经典基准，包含4个至今广泛使用的任务（笔、门、锤子、球）
- DAPG算法证明少量人类演示可显著加速高自由度手部的强化学习
- 开源的MuJoCo 24自由度Shadow Hand模型，成为社区标准

## 局限性/不足

- 仅4个任务且接触模式相对简单；未覆盖多阶段或工具使用操作
- Shadow Hand模型缺少触觉传感仿真
- 当时MuJoCo仅支持CPU；现已被GPU加速替代方案超越用于大规模训练，但仍是标准评估目标
- 原始工作未解决仿真到真实的差距问题

## 覆盖缺口

| 标准 | 是否覆盖？ |
|------|-----------|
| 力/力矩评估指标 | 否 |
| 可变形物体任务 | 否 |
| 触觉传感 | 否 |
| 多阶段/长时程任务 | 否（每个任务为单阶段目标） |
| 多手协调 | 否 |

## 开源状态

完全开源。通过 `pip install gymnasium-robotics` 获取（Gymnasium-Robotics提供维护的Adroit环境）。原始代码：[GitHub](https://github.com/aravindr93/hand_dapg)
