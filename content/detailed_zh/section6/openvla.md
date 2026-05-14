### OpenVLA: An Open-Source Vision-Language-Action Model

**完整标题：** OpenVLA: An Open-Source Vision-Language-Action Model

**作者：** Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, Ted Xiao, Ashwin Balakrishna, Suraj Nair, Rafael Rafailov, Ethan Foster, Grace Lam, Pannag Sanketi, Quan Vuong, Thomas Kollar, Benjamin Burchfiel, Russ Tedrake, Dorsa Sadigh, Sergey Levine, Percy Liang, Chelsea Finn

**发表期刊/年份：** CoRL 2024

**架构：** 7B参数VLA，基于Prismatic VLM骨干构建（SigLIP + DinoV2双视觉编码器融合到Llama 2 7B语言模型中）。动作通过自回归解码作为离散token输出，遵循RT-2范式。无独立动作头；LLM的输出词汇表扩展了每维256个动作分箱。

**动作空间：** 7D（6自由度末端执行器增量 + 夹爪），每维离散化为256个分箱，作为文本token解码。

**灵巧手支持？** ✗ --- 仅单臂夹爪系统。

**力/阻抗输出？** ✗ --- 仅位置目标。

**核心方法论：** OpenVLA提供RT-2 VLA范式的首个完全开源复现。它在Open X-Embodiment（OXE）数据集——一个大规模跨具身机器人数据集上训练，并使用参数高效方法（LoRA）在下游任务上微调。双视觉编码器（SigLIP用于语义 + DinoV2用于空间特征）提供互补的视觉表示。OpenVLA作为社区基线，实现VLA方法的直接比较和扩展。

**训练数据：** 在来自Open X-Embodiment（OXE）数据集的970K机器人episode上预训练，涵盖22种机器人具身。OXE混合数据包括Bridge V2、RT-1、DROID和众多其他数据集。微调使用任务特定演示数据（通常50-500个episode）。

**主要贡献：**
- 首个被广泛采用的开源VLA（Apache 2.0），性能与RT-2具有竞争力，推动社区研究。
- 证明预训练VLA的LoRA微调可以用少至50个演示适配到新任务。
- 建立了具有标准化评估协议的可复现VLA基线。

**定量结果：**

| 基准/任务 | OpenVLA (7B) | RT-2-X | 备注 |
|---|---|---|---|
| *（结果未经独立验证——arXiv页面无法获取。论文报告在Bridge V2和SimplerEnv基准上与RT-2-X具有竞争力的性能。请查阅CoRL 2024论文获取逐任务成功率。）* | | | |

**局限性/差距：**
- 自回归单token动作解码缓慢（约4-6 Hz），限制动作表达能力。
- 7D动作空间对双臂或灵巧系统具有限制性。
- 将连续动作量化为256个分箱引入精度损失，特别是对精细操作。
- 基础模型无多视角图像支持。

**开放权重/代码：** ✅ 完全开放，Apache 2.0。[GitHub](https://github.com/openvla/openvla), [HuggingFace](https://huggingface.co/openvla/openvla-7b)。

## 推理/部署

- **推理延迟：** OpenVLA在单块A100 GPU上运行频率约为4-6 Hz。通过完整7B参数LLM的7个动作token顺序自回归解码是瓶颈——每个动作维度逐一解码，每个动作步骤需要7次完整前向传播。
- **部署硬件：** 需要高端GPU（NVIDIA A100或同等）用于推理。可量化（4位、8位）以在消费级GPU（RTX 3090/4090）上部署。可在消费级GPU上通过LoRA微调。由于7B参数占用，无法在边缘设备上部署。
- **可实时运行？** 勉强。在4-6 Hz下，OpenVLA可用于慢速桌面操作，但对需要10+ Hz控制的接触丰富或灵巧任务来说太慢。OpenVLA-OFT通过并行动作解码实现26倍推理加速来解决此瓶颈。

## 数据集/数据收集

- **使用的数据集：** Open X-Embodiment（OXE）数据集——跨22种机器人具身的970K机器人episode。OXE混合数据包括Bridge V2、RT-1、DROID和众多其他社区贡献数据集。
- **收集方法：** 从多个来源聚合，收集方法多样：遥操作（VR控制器、SpaceMouse、主从式）、脚本策略和人类演示，涵盖22种不同机器人平台。微调使用任务特定演示（通常50-500个episode）。
- **数据规模：** 970K机器人episode跨22种具身用于预训练。微调：每个任务50-500个演示。
- **遥操作设备：** 因组成数据集而异——Meta Quest VR控制器（DROID）、SpaceMouse（Bridge V2）、主从式（ALOHA）等。
- **数据格式：** RLDS（TensorFlow Datasets）格式，遵循Open X-Embodiment标准。
- **是否公开？** 是。OXE数据集完全公开。模型权重在 https://huggingface.co/openvla/openvla-7b （Apache 2.0）。

---
