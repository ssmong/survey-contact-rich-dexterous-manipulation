### SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model

**完整标题：** SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model

**作者：** Delin Qu, Haoming Song, Qizhi Chen, Yuanqi Yao, Xinyi Ye, Yan Ding, Zhigang Wang, JiaYuan Gu, Bin Zhao, Dong Wang, Xuelong Li (上海人工智能实验室、复旦大学、上海交通大学、浙江大学、上海科技大学、西北工业大学)

**发表期刊/年份：** RSS 2025

**架构：** 3.5B参数VLA，基于PaliGemma2 VLM骨干构建。视觉编码器为SigLIP，语言模型为Gemma 2。SpatialVLA在此骨干上引入两个空间模块：(1) Ego3D位置编码，通过相机反投影和正弦编码+可学习MLP将单目深度（来自ZoeDepth）与2D语义特征集成，将3D空间感知注入视觉token；(2) 自适应动作网格，使用高斯拟合非均匀网格（8,194个词汇条目）将连续7D动作离散化为3个空间token（平移+旋转+夹爪），替换标准的每步7token线性分箱。

**动作空间：** 7D（3D平移 + 3D旋转 + 夹爪），通过自适应动作网格离散化为每步3个空间token。网格分区根据每维高斯动作分布拟合，在动作密集处集中分辨率。微调时，网格可通过token嵌入的三线性插值重新适配。

**灵巧手支持？** ✗ --- 仅夹爪（单臂）评估。

**力/阻抗输出？** ✗ --- 仅位置目标。

**核心方法论：** SpatialVLA解决标准VLA缺乏显式3D空间理解从而限制精确操作的问题。Ego3D位置编码将以自我为中心的3D坐标注入视觉token，无需外部3D传感器——仅需RGB+单目深度估计。自适应动作网格将每步动作token从7个减少到3个，同时通过在动作统计密集处集中离散化分箱来保持精度，改善推理速度和动作质量。模型在1.1M真实世界机器人episode上预训练，支持零样本迁移和LoRA微调。

**训练数据：** 在来自Open X-Embodiment（OXE）子集和RH20T混合数据的1.1M真实世界机器人episode上预训练。在包括Google Fractal、BridgeData V2和LIBERO（每个任务50个演示）的下游任务上微调。训练：64块A100 GPU上10天，批次大小2,048。

**主要贡献：**
- 引入Ego3D位置编码，将单目深度衍生的3D空间信息注入VLA视觉token，无需测试时使用深度传感器即可改善空间推理。
- 提出自适应动作网格，通过分布感知非均匀离散化将动作token从每步7个减少到3个同时保持精度，实现约20 Hz推理。
- 在3.5B参数及以下的模型中实现SimplerEnv基准上最高的零样本和微调分数（截至RSS 2025），与15倍更大的模型（RT-2-X 55B）具有竞争力。

**定量结果：**

| 基准/任务 | SpatialVLA（零样本） | SpatialVLA（微调） | OpenVLA | Octo | 备注 |
|---|---|---|---|---|---|
| SimplerEnv Google Robot（视觉匹配） | 71.9% | 75.1% | 约49% | — | 零样本比RoboVLM高+15.6% |
| SimplerEnv Google Robot（变体聚合） | 68.8% | 70.7% | — | — | |
| SimplerEnv WidowX（零样本） | 34.4% | 42.7% | — | — | 微调后茄子任务100% |
| LIBERO平均（微调） | — | 78.1% | 76.5% | 75.1% | 排名第1；LIBERO-Spatial：88.2% |
| 推理速度 | 约20 Hz (RTX 4090, 8.5 GB) | | 约5 Hz | | |

**局限性/差距：**
- 动作网格的高斯拟合对具有极端单轴运动的分布次优，可能导致网格聚集和能力丧失。
- 自回归解码在高频控制方面本质上比基于扩散的动作头更慢。
- 无历史/时间上下文机制；依赖单帧观测，限制长时域任务性能（在LIBERO-Long上表现困难）。
- OXE数据集中质量参差不齐影响训练效率；需要数据整理/蒸馏。
- 仅夹爪；无灵巧手或力感知评估。

**开放权重/代码：** ✅ 代码和权重：[项目页面](https://spatialvla.github.io/)。作者声明所有代码和细节已开源。

## 数据集/数据收集

- **使用的数据集：** Open X-Embodiment（OXE）子集 + RH20T用于预训练。BridgeData V2、Google Fractal、LIBERO用于微调。
- **收集方法：** 从OXE聚合的跨具身数据。微调演示来自标准操作基准。
- **数据规模：** 1.1M真实世界机器人episode用于预训练。微调：每个任务50个演示（LIBERO），6个episode（Fractal）。
- **遥操作设备：** 因OXE组成数据集而异。
- **数据格式：** RLDS（OXE标准）。
- **是否公开？** OXE和RH20T公开。模型权重通过项目页面提供。

---
