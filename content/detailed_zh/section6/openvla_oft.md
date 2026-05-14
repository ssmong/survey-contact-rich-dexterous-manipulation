### OpenVLA-OFT: Open Vision-Language-Action Model with Optimal Fine-Tuning

**完整标题：** Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success

**作者：** Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, Suraj Nair, Ashwin Balakrishna, Sergey Levine, Percy Liang, Chelsea Finn

**发表期刊/年份：** RSS 2025

**架构：** 基于OpenVLA 7B进行三项关键修改：(1) 用并行动作解码替换顺序自回归生成，(2) 用连续动作输出替换离散token分箱，(3) 在VLM骨干后附加轻量级FiLM条件化动作头。VLM骨干保持为Prismatic（SigLIP + DinoV2 + Llama 2 7B）。

**动作空间：** 7D或14D（用于双臂ALOHA：双6自由度臂 + 2个夹爪），现以连续值并行解码，而非顺序离散token。支持动作块化（每次前向传播多个未来时间步）。

**灵巧手支持？** ✗ --- 专为单臂夹爪和双臂ALOHA夹爪设置设计。

**力/阻抗输出？** ✗ --- 仅位置目标。

**核心方法论：** OpenVLA-OFT通过用并行连续动作预测替换顺序token解码来解决自回归VLA的推理速度瓶颈。FiLM条件化动作头处理VLM的输出嵌入，同时生成所有动作维度。结合动作块化和微调方案优化（学习率调度、数据增强），实现比OpenVLA快26倍的推理，同时提高任务成功率。该工作证明RT-2和OpenVLA使用的自回归动作token化是次优的。

**训练数据：** 与OpenVLA相同的OXE预训练。在Bridge V2和ALOHA双臂任务上评估微调。

**主要贡献：**
- 通过消除顺序动作解码，实现比OpenVLA快26倍的推理。
- 证明连续并行动作输出在速度和精度上均优于离散token化动作。
- 提供了VLA微调方案的系统研究，确定了最优学习率、增强策略和动作表示选择。

**定量结果：**

| 指标 | OpenVLA-OFT | OpenVLA | 加速比 | 备注 |
|---|---|---|---|---|
| *（结果未经独立验证——请查阅RSS 2025论文获取Bridge V2和ALOHA双臂基准上的逐任务成功率。论文报告26倍推理加速且成功率提升。）* | | | | |

**局限性/差距：**
- 仍限于基于夹爪的系统；7/14D动作空间不能扩展到灵巧手。
- 依赖相同的Prismatic VLM骨干，继承其单视角限制。
- 无力/柔顺感知。

**开放权重/代码：** ✅ 完全开放。[GitHub](https://github.com/moojink/openvla-oft), [HuggingFace](https://huggingface.co/openvla/openvla-7b-oft)。

## 推理/部署

- **推理延迟：** OpenVLA-OFT通过用并行连续动作预测替换顺序自回归解码，实现比OpenVLA快26倍的推理。这对应于动作头解码约100-150 Hz（尽管总系统吞吐量取决于图像编码）。结合动作块化，有效控制率显著高于每次推理频率。
- **部署硬件：** 与OpenVLA相同的7B参数VLM骨干，需要GPU（A100或消费级RTX 4090级别）用于推理。并行动作头是轻量级的（FiLM条件化MLP），因此加速来自消除顺序token解码而非模型尺寸缩减。
- **可实时运行？** 是。26倍加速使推理达到适合实时操作控制的水平。结合动作块化，系统可以在适合操作的频率下保持平滑控制。这是实际VLA部署的关键改进。

## 数据集/数据收集

- **使用的数据集：** 与OpenVLA相同的OXE预训练（970K episode，22种具身）。在Bridge V2和ALOHA双臂任务上评估微调。
- **收集方法：** 与OpenVLA相同——从OXE聚合的跨具身遥操作数据。微调演示通过各自的遥操作系统收集（Bridge V2使用SpaceMouse，ALOHA使用主从式）。
- **数据规模：** 970K episode（预训练，继承自OpenVLA）。微调规模因任务而异。
- **遥操作设备：** 继承自OXE组成数据集。
- **数据格式：** OXE预训练数据使用RLDS（TensorFlow Datasets）。
- **是否公开？** 是。与OpenVLA相同——OXE是公开的。OFT权重在 https://huggingface.co/openvla/openvla-7b-oft 。

---
