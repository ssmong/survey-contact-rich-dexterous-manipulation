### RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control

**完整标题：** RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control

**作者：** Anthony Brohan, Noah Brown, Justice Carbajal, Yevgen Chebotar, Xi Chen, Krzysztof Choromanski, Tianli Ding, Danny Driess, Avinava Dubey, Chelsea Finn, Pete Florence, Chuyuan Fu, Montse Gonzalez Arenas, Keerthana Gopalakrishnan, Kehang Han, Karol Hausman, Alexander Herzog, Jasmine Hsu, Brian Ichter, Alex Irpan, Nikhil Joshi, Ryan Julian, Dmitry Kalashnikov, Yuheng Kuang, Isabel Leal, Lisa Lee, Tsang-Wei Edward Lee, Sergey Levine, Yao Lu, Henryk Michalewski, Igor Mordatch, Karl Pertsch, Kanishka Rao, Krista Reymann, Michael Ryoo, Grecia Salazar, Pannag Sanketi, Pierre Sermanet, Jaspiar Singh, Anikait Singh, Radu Soricut, Huong Tran, Vincent Vanhoucke, Quan Vuong, Ayzaan Wahid, Stefan Welker, Paul Wohlhart, Jialin Wu, Fei Xia, Ted Xiao, Peng Xu, Sichun Xu, Tianhe Yu, Brianna Zitkovich (Google DeepMind)

**发表期刊/年份：** CoRL 2023

**架构：** RT-2对大型视觉-语言模型（PaLI-X 55B或PaLM-E 12B）进行协同微调，使其输出机器人动作作为文本token与自然语言并列。VLM骨干为PaLI-X（55B参数，ViT-22B视觉编码器）或PaLM-E（12B参数）。没有独立的动作头；动作被token化为[0, 255]范围内的整数，作为语言输出序列的一部分自回归解码。

**动作空间：** RT-2机器人为7D（6自由度末端执行器姿态增量 + 夹爪开合），每个维度离散化为256个分箱。动作表示为VLM输出词汇表中的文本字符串（如"1 128 91 241 5 101 127"）。

**灵巧手支持？** ✗ --- 专为配备平行爪夹爪的单臂移动操作器设计。

**力/阻抗输出？** ✗ --- 仅位置目标。

**核心方法论：** RT-2证明预训练的视觉-语言模型可以通过将动作表示为VLM现有词汇表中的token序列来直接微调输出机器人动作。关键洞察是网络规模的视觉和语义知识可以迁移到机器人操作：该模型展现出涌现能力，如对新物体的推理、遵循复杂指令和执行初步的思维链规划——这些能力在机器人训练数据中并不存在。这确立了利用互联网规模VLM预训练进行机器人控制的VLA范式。

**训练数据：** 来自RT-2机器人舰队的机器人数据：Google移动操作器上约700个任务的约130K个episode。与PaLI-X或PaLM-E预训练语料库的网络规模视觉-语言数据协同微调。

**主要贡献：**
- 确立了VLA范式：表明在机器人数据上协同微调VLM可以产生用于操作的涌现语义推理和泛化能力。
- 证明了从网络规模数据到机器人控制的正迁移，55B PaLI-X变体在新物体和指令泛化方面显著优于12B PaLM-E变体。
- 引入机器人操作的思维链推理，VLM在动作token之前生成中间推理步骤。

**定量结果：**

| 评估类别 | RT-2 (PaLI-X 55B) | RT-2 (PaLM-E 12B) | RT-1基线 | 备注 |
|---|---|---|---|---|
| *（结果未经独立验证——arXiv页面无法获取。论文报告在已见任务上优于RT-1，在新物体/指令泛化上有显著提升。请查阅CoRL 2023论文获取逐类别成功率。）* | | | | |

**局限性/差距：**
- 极大的模型（55B），推理缓慢（约1-3 Hz），不适用于实时灵巧控制。
- 闭源：无权重、代码或训练数据发布。严重限制可复现性和社区扩展。
- 仅限于Google特定的机器人具身；无跨具身能力。
- 自回归动作token化引入量化误差和顺序解码延迟。

**开放权重/代码：** ✗ --- 完全封闭。无公开权重、代码或数据。

## 推理/部署

- **推理延迟：** RT-2（PaLI-X 55B）由于庞大的55B参数模型和顺序自回归动作token解码（7个token逐一解码），运行频率约为1-3 Hz。较小的PaLM-E 12B变体更快但仍限于约3-5 Hz。每个动作需要通过完整VLM解码7个顺序token。
- **部署硬件：** 55B模型使用Google内部TPU基础设施。PaLM-E 12B变体可能在高端GPU上运行但仍需大量计算。无法在边缘设备上部署。
- **可实时运行？** 对灵巧操作不可行。在1-3 Hz（55B）或3-5 Hz（12B）下，RT-2对于需要>10 Hz控制的任务来说太慢。7D动作的自回归逐token解码本质上是顺序的，无法并行化。仅适用于Google移动操作器上的慢速、粗糙操作任务。

## 数据集/数据收集

- **使用的数据集：** Google内部机器人舰队数据（约700个任务的约130K个episode），与PaLI-X或PaLM-E的网络规模视觉-语言预训练语料库协同微调。
- **收集方法：** 在Google移动操作器舰队上遥操作。机器人数据与互联网规模的图文对组合用于VLM骨干的协同微调。
- **数据规模：** 约700个任务的约130K个机器人episode。网络规模VLM预训练数据（PaLI-X/PaLM-E的数十亿图文对）。
- **遥操作设备：** 未指定。Google移动操作器内部遥操作设置。
- **数据格式：** 未披露（Google内部格式）。
- **是否公开？** 否。完全封闭——无机器人数据、权重或代码发布。

---
