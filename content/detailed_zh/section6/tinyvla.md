### TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation

**完整标题：** TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation

**作者：** Junjie Wen, Yichen Zhu, Jinming Li, Minjie Zhu, Kun Wu, Zhiyuan Xu, Ning Liu, Ran Cheng, Chaomin Shen, Yaxin Peng, Feifei Feng, Jian Tang (华东师范大学、美的集团AI实验室上海、Syracuse University、北京人形机器人创新中心、上海大学)

**发表期刊/年份：** AAAI 2025

**架构：** 紧凑型VLA，有三种大小变体：TinyVLA-S（422M，101M可训练）、TinyVLA-B（740M，138M可训练）和TinyVLA-H（1.3B，143M可训练）。骨干遵循LLaVA训练流程，使用Pythia作为语言模型和视觉编码器。动作头是基于去噪扩散概率模型（DDPM）的扩散策略解码器，在VLM特征条件下生成连续动作。微调使用LoRA适配器作用于注意力Q/K/V权重，将可训练参数限制在transformer的约5%。关键设计选择是从预训练多模态模型初始化策略骨干而非从头训练，无需大规模机器人预训练。

**动作空间：** 7D连续（3D位置 + 3D旋转 + 夹爪宽度），通过带动作块化的扩散解码生成。扩散头使用自适应池化、层归一化、与本体感受状态的拼接和3层MLP进行条件嵌入。

**灵巧手支持？** ✗ --- 仅在单臂夹爪和双臂夹爪（UR5）系统上评估。

**力/阻抗输出？** ✗ --- 仅位置目标。

**核心方法论：** TinyVLA证明如果VLA骨干从强预训练视觉-语言模型初始化，则大规模机器人预训练（如在OXE的970K episode上）是不必要的。通过将紧凑型VLM骨干（1.3B）与扩散策略解码器耦合并应用LoRA微调，TinyVLA在匹配或超越7B OpenVLA的性能的同时，模型小5.5倍、推理快20倍。扩散解码器在VLM潜在表示条件下生成动作块，实现平滑、时间连贯的动作，无需自回归逐token解码。

**训练数据：** 无大规模机器人预训练。直接在任务特定演示上微调：真实机器人实验每个任务100个遥操作轨迹。MetaWorld仿真任务用于额外评估。

**主要贡献：**
- 证明从预训练VLM初始化并使用LoRA + 扩散解码器微调的1.3B VLA可以匹配7B OpenVLA的性能，无需任何机器人预训练阶段，挑战了大规模机器人数据预训练必不可少的假设。
- 实现比OpenVLA快20倍的推理（14ms对292ms每个动作），参数减少5.5倍，使消费级硬件上的实时部署成为可能。
- 尽管模型紧凑、训练数据有限，仍展示了跨语言指令、新物体、未见位置、外观/背景变化和环境变化的强泛化能力。

**定量结果：**

| 基准/任务 | TinyVLA-H (1.3B) | OpenVLA (7B) | Diffusion Policy | 备注 |
|---|---|---|---|---|
| 真实世界单臂平均（5个任务） | 94.0% | 68.3% | — | 比OpenVLA高+25.7% |
| 双臂UR5平均 | 44.5% | 0% | — | OpenVLA完全失败 |
| MetaWorld 50任务平均（仿真） | 31.6% | — | 10.5% | |
| 推理延迟 | 14 ms | 292 ms | — | 20倍加速 |
| 参数（总/可训练） | 1.3B / 143M | 7.2B / — | — | 小5.5倍 |

> **注意：** 此比较使用作者自己的5个真实世界单臂任务，而非社区标准化基准。OpenVLA使用相同协议微调（100个演示）。结果应谨慎解读，因为任务选择可能有利于TinyVLA的设计。

**局限性/差距：**
- OpenVLA在极端分布外空间泛化上略优于TinyVLA，可能因为OXE预训练提供了更广泛的数据多样性。
- 仅在基于夹爪的系统上评估；无灵巧手评估。
- 无力/柔顺感知。
- MetaWorld仿真结果（31.6%）在绝对值上仍然不高。
- 论文中GitHub仓库和模型权重可用性不明确；项目页面在 https://tiny-vla.github.io/ 。

**开放权重/代码：** 项目页面：[tiny-vla.github.io](https://tiny-vla.github.io/)。论文中未确认明确的GitHub链接或模型权重下载。

## 数据集/数据收集

- **使用的数据集：** 无大规模预训练数据集。任务特定遥操作演示用于微调（每个任务100个轨迹）。MetaWorld仿真用于仿真评估。
- **收集方法：** 真实机器人任务使用遥操作。
- **数据规模：** 每个任务100个演示（真实）。无OXE规模预训练。
- **遥操作设备：** 论文中未指定。
- **数据格式：** 未指定。
- **是否公开？** 项目页面存在但明确的数据/权重发布状态不明确。

---
