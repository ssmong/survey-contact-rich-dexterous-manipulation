# 9.9 TACTO

- **全称：** TACTO: A Fast, Flexible and Open-source Simulator for High-Resolution Vision-based Tactile Sensors
- **作者：** Shaoxiong Wang, Mike Lambeta, Po-Wei Chou, Roberto Calandra
- **机构：** Meta FAIR（Facebook AI Research）
- **发表venue/年份：** IEEE Robotics and Automation Letters (RA-L) 2022
- **仿真平台：** PyBullet（物理）+ PyRender（触觉渲染）
- **传感器模型：** DIGIT、OmniTact、GelSight风格的视觉触觉传感器
- **任务：** 抓取、滚动、带触觉反馈的物体操作

## 核心方法/设计

TACTO通过从接触几何渲染合成触觉图像来仿真视觉触觉传感器。TACTO并不尝试物理精确的接触变形仿真，而是专注于快速、视觉上可信的触觉图像生成。当物体接触仿真传感器时，TACTO使用PyRender以适当的光照和凝胶表面属性渲染接触区域，生成类似于真实DIGIT或GelSight传感器的RGB触觉图像。物理仿真（刚体动力学、碰撞检测）由PyBullet处理，而TACTO仅负责触觉渲染流程。这种分离使TACTO可以集成到任何基于PyBullet的操作环境中。

## 主要贡献

- 首个专门针对DIGIT和OmniTact视觉触觉传感器的高分辨率合成触觉图像开源仿真器
- 快速渲染支持使用触觉观测进行强化学习训练（显著快于基于FEM的替代方案如DiffTactile）
- 模块化设计：传感器几何形状和光学属性通过YAML文件可配置
- 通过轻量API层简便集成到现有PyBullet环境
- 支持无头渲染（EGL/OSMESA），用于服务器端训练

## 在综述论文中的使用

TACTO或其触觉仿真方法被本综述中多项工作引用：
- **Sparsh**（第12节）：使用仿真和真实DIGIT数据训练/评估触觉编码器
- **RotateIt**（第7节）：使用触觉仿真进行手内旋转
- 其他使用DIGIT/GelSight的触觉操作论文受益于TACTO风格的仿真数据进行预训练或数据增强

## 局限性/不足

- 明确非物理精确："不旨在提供物理精确的接触动力学（如变形、摩擦）"——接触力和变形为近似处理
- PyBullet后端限制了仿真速度，与GPU并行引擎（IsaacGym、ManiSkill3）相比较慢
- 无可微渲染：无法通过触觉图像生成进行梯度反向传播
- 仅限视觉触觉传感器（DIGIT、OmniTact、GelSight）；不仿真电阻式、电容式或气压式触觉传感器
- 未开箱包含多指灵巧手环境（示例集中在平行夹爪）
- PyBullet和PyRender在macOS上存在一些可视化问题

## 覆盖缺口

| 标准 | 是否覆盖？ |
|------|-----------|
| 力/力矩评估指标 | 否（触觉图像为视觉信息，非力标定） |
| 可变形物体任务 | 否（仅通过PyBullet实现刚体物理） |
| 触觉传感 | 是（核心贡献——合成触觉图像生成） |
| 多阶段/长时程任务 | 否 |
| 多手协调 | 否 |

## 开源状态

基于MIT许可证开源。通过 `pip install tacto` 安装。GitHub: [facebookresearch/tacto](https://github.com/facebookresearch/tacto)
