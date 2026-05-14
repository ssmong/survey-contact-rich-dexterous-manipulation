### 2.5 Grasp as You Say

**全称：** Grasp as You Say: Language-Guided Dexterous Grasp Generation

**作者：** Yi-Lin Wei, Jian-Jian Jiang, Chengyi Xing, Xian-Tuo Tan, Xiao-Ming Wu, Hao Li, Mark Cutkosky, Wei-Shi Zheng（中山大学, iSEE 实验室）

**发表venue/年份：** NeurIPS 2024

**arXiv：** [2405.19291](https://arxiv.org/abs/2405.19291)

**手部硬件：** Shadow Dexterous Hand（仿真）；Allegro Hand（28自由度）+ Flexiv Rizon 4 机械臂（真实世界部署）

**任务：**
- 语言引导的灵巧抓取姿态生成（例如"通过杯柄抓住杯子"、"从顶部拿起瓶子"）
- 部位感知抓取：生成针对语言指定的特定物体区域的抓取
- 在多个物体类别上使用多样化抓取意图进行评估

**核心方法：** Grasp as You Say 基于自然语言描述生成灵巧抓取姿态，描述指定物体应如何被抓取。系统接收3D物体表征（点云或网格）和描述期望抓取方式的语言指令（例如要抓取的部位、抓取风格）作为输入。语言编码器处理指令以产生条件化向量，引导生成模型生成实现所描述抓取的 Shadow Hand 关节配置和腕部位姿。该方法弥合了语义抓取意图（以语言表达）与灵巧手高维配置空间之间的差距。

**架构/参数：**
- 语言编码器：预训练语言模型用于指令编码
- 抓取生成：在灵巧手配置空间上的条件生成模型（仿真：Shadow Hand；真实世界：Allegro Hand 28自由度 + 腕部位姿）
- 条件化机制：语言嵌入调制抓取生成过程
- 具体模型规模/参数量在摘要层面未公开详述

**主要贡献：**
- 提出语言条件化灵巧抓取生成，据作者称此前未被研究的问题，实现对24自由度手的抓取意图（部位、风格）语义指定
- 证明自然语言可有效条件化高维灵巧抓取合成，生成符合语言描述的物理合理抓取
- 部位感知抓取能力：系统可区分"通过杯柄抓住杯子"与"通过杯身抓住杯子"，为每种情况生成不同的手部配置

**局限性/不足：**
- 仅限抓取生成：产生静态抓取姿态，不生成完整操作轨迹或抓取后动作
- 仿真使用 Shadow Hand；真实世界部署使用 Allegro Hand（28自由度）——除此配对外无跨本体评估
- 无力或触觉反馈；抓取通过几何评估和仿真评估，而非真实世界接触动力学
- 仅限通过语言表达的抓取意图；不处理多步任务指令或超越初始抓取的操作
- 未展示所生成抓取的仿真到真实迁移

**结果：**

**数据集规模：** 1,800个家用物体类别中的50,000个抓取-指令对。

**抓取成功率（仿真，Isaac Gym）：**

| 方法 | 成功率 | Q1 抓取质量 |
|---|---|---|
| GraspCVAE | 29.12% | 0.054 |
| GraspTTA | 43.46% | 0.071 |
| DGTR | 51.91% | 0.078 |
| SceneDiffuser | 62.24% | 0.083 |
| **DexGYSGrasp（本文）** | **63.31%** | **0.083** |

**意图一致性（基于 FID，越低越好）：**

| 方法 | FID | P-FID | Chamfer Distance |
|---|---|---|---|
| GraspCVAE | 31.26 | 29.02 | 3.138 |
| DGTR | 23.31 | 15.77 | 2.895 |
| SceneDiffuser | 20.44 | 7.932 | 1.679 |
| **DexGYSGrasp（本文）** | **6.538** | **5.595** | **1.198** |

**抓取多样性（每个条件8个样本）：**

| 指标 | DexGYSGrasp | DGTR | SceneDiffuser |
|---|---|---|---|
| 平移标准差 (delta_t) | 6.118 | 2.037 | 0.346 |
| 旋转标准差 (delta_r) | 55.68 | 14.01 | 3.455 |
| 关节角标准差 (delta_q) | 6.118 | 4.299 | 0.387 |

**穿透深度：** 0.223 cm（DexGYSGrasp）vs. 0.163 cm（DGTR）。

- 在1,800个物体类别上使用50,000个抓取-指令对进行评估
- 真实世界部署使用 Allegro Hand（28自由度）+ Flexiv Rizon 4 机械臂 + Intel RealSense D415
- 代码发布于 [GitHub](https://github.com/iSEE-Laboratory/Grasp-as-You-Say)

## 推理 / 部署

- **推理延迟：** 未报告。论文未公开抓取生成时间或推理延迟。
- **部署硬件：** 训练在单块 RTX 4090 GPU 上进行。真实世界实验使用 Allegro Hand + Flexiv Rizon 4 机械臂 + Intel RealSense D415 相机。推理 GPU 未单独指定。
- **是否支持实时？** 在传统意义上不适用——系统生成静态抓取姿态（非闭环控制）。抓取生成速度未表征。系统产生单一抓取配置而非连续控制策略。

## 数据集 / 数据采集

- **使用的数据集：** DexGYS（随本工作发布的自定义数据集）。另利用 OakInk 3D 物体网格和来自北京大学的 Shadow Hand MJCF 模型。
- **采集方法：** 手-物体交互重定向策略用于高效抓取标注，结合 LLM 辅助的语言引导标注系统生成自然语言抓取描述。
- **数据规模：** 未明确报告。提供训练和测试分割（train_with_guide_v2.1.json、test_with_guide_v2.1.json）。
- **遥操作设备：** 不适用（抓取标注通过重定向和基于 LLM 的标注生成，而非遥操作）。
- **数据格式：** JSON 文件（附语言引导的训练/测试分割）。包含3D物体网格（来自 OakInk）、Shadow Hand MJCF 模型以及匹配的抓取结果。
- **是否公开可用？** 是。数据集在 HuggingFace 上提供（[datasets/wyl2077/DexGYS](https://huggingface.co/datasets/wyl2077/DexGYS/tree/main)）。代码位于 [GitHub](https://github.com/iSEE-Laboratory/Grasp-as-You-Say)。
