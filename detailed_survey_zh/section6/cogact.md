### CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation

**完整标题：** CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation

**作者：** Qixiu Li, Yaobo Liang, Zeyu Wang, Lin Luo, Xi Chen, Mozheng Liao, Fangyun Wei, Yu Deng, Sicheng Xu, Yizhong Zhang, Xiaofan Wang, Bei Liu, Jianlong Fu, Jianmin Bao, Dong Chen, Yuanchun Shi, Jiaolong Yang, Baining Guo (Microsoft Research)

**发表期刊/年份：** arXiv 2024

**架构：** CogACT将VLA显式分为认知和动作阶段。认知模块是VLM（InternVL2，基于InternViT-300M + InternLM2-1.8B），处理视觉观测和语言指令以产生潜在"认知计划"。动作模块是基于扩散的解码器，将认知计划转换为连续机器人动作。这种分离允许每个模块独立优化，并支持动作生成的迭代细化。

**动作空间：** 7D（6自由度EEF增量 + 夹爪），通过扩散解码加动作块化生成连续值。

**灵巧手支持？** ✗ --- 仅夹爪评估。

**力/阻抗输出？** ✗ --- 仅位置目标。

**核心方法论：** CogACT论证现有VLA将两个根本不同的任务——语义理解和精确运动控制——混合在单一自回归解码过程中，这降低了两者的质量。通过显式分离认知（VLM推理）和动作（扩散生成），每个模块可以使用最适合其任务的架构。认知计划作为扩散动作头的压缩、语义丰富的条件信号，避免token化动作的信息瓶颈。

**训练数据：** 在OXE跨具身数据上预训练。在SimplerEnv和真实机器人操作任务上微调。

**主要贡献：**
- 提出*在单一端到端VLA架构内*显式的认知-动作分离，VLM生成潜在计划，扩散头生成精确动作。（注：之前的工作如SayCan以不同方式分离推理和动作执行——在系统层面，语言模型从固定的预训练技能集中选择。CogACT的贡献在于将两个阶段集成到单一可微架构中，认知计划是学习的潜在表示，而非离散技能选择。）
- 证明这种分离相比整体式VLA改善了语言理解和动作精度。
- 在发表时达到SimplerEnv基准的最高报告结果。

**定量结果：**

| 基准/任务 | CogACT | OpenVLA | RT-2-X | 备注 |
|---|---|---|---|---|
| *（请查阅arXiv论文获取SimplerEnv和真实机器人评估的逐任务结果。论文报告发表时SimplerEnv最高性能。）* | | | | |

**局限性/差距：**
- 两阶段架构增加整体模型复杂性，可能在认知和动作之间引入延迟。
- 仅在7D动作的基于夹爪的系统上评估。
- 无力/柔顺感知。
- 预训练权重未公开发布。

**开放权重/代码：** ✅ 代码：[GitHub](https://github.com/microsoft/CogACT)。✗ 模型权重未公开。

## 推理/部署

- **推理延迟：** 未明确基准测试。两阶段架构（VLM认知 + 扩散动作）两个阶段都引入延迟：InternVL2 VLM（约2B参数）处理视觉/语言输入，然后扩散解码器在多个去噪步骤中生成动作。估计约5-15 Hz，取决于扩散步数和硬件。
- **部署硬件：** 未报告。约2B参数的VLM骨干需要GPU用于实时推理（如A100或RTX 4090级别）。
- **可实时运行？** 有限。两阶段流水线相比整体式VLA增加延迟。扩散动作头需要多个去噪步骤。适合中速操作但对高频灵巧控制可能太慢。

## 数据集/数据收集

- **使用的数据集：** Open X-Embodiment（OXE）用于跨具身预训练。在SimplerEnv和真实机器人操作任务上微调。
- **收集方法：** 从OXE聚合的跨具身数据。微调演示来自标准操作基准。
- **数据规模：** OXE预训练规模（与OpenVLA相当）。微调任务特定演示数量未报告。
- **遥操作设备：** 因OXE组成数据集而异。
- **数据格式：** RLDS（OXE标准）。
- **是否公开？** OXE数据公开。CogACT模型权重未发布。

---
