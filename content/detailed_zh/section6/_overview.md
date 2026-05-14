# 6. VLA基础模型：版本历史

本节提供了主要视觉-语言-动作（VLA）模型系列和视觉运动策略的详细条目，这些条目在主表中进行了调查。每个条目涵盖架构、动作表示、训练数据、贡献以及与接触丰富灵巧操作相关的差距。

**符号说明：** ✅ = 可用/支持, ✗ = 不可用/不支持, — = 未报告或不适用。

## 文件索引

### VLA基础模型系列
- [pi_family.md](pi_family.md) — Physical Intelligence pi0 / pi0-FAST / pi0.5 / pi0.6 / pi0.7
- [groot_family.md](groot_family.md) — NVIDIA GR00T N1 / N1.5 / N1.6 / N1.7

### 其他主要VLA
- [rt2.md](rt2.md) — RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control
- [openvla.md](openvla.md) — OpenVLA: An Open-Source Vision-Language-Action Model
- [openvla_oft.md](openvla_oft.md) — OpenVLA-OFT: Optimal Fine-Tuning
- [octo.md](octo.md) — Octo: An Open-Source Generalist Robot Policy
- [rdt1b.md](rdt1b.md) — RDT-1B: Robotics Diffusion Transformer
- [hpt.md](hpt.md) — HPT: Heterogeneous Pre-trained Transformers
- [cogact.md](cogact.md) — CogACT: Synergizing Cognition and Action
- [egoscale.md](egoscale.md) — EgoScale: Scaling Egocentric Human Video Pre-training
- [simplevla_rl.md](simplevla_rl.md) — SimpleVLA-RL: RL Fine-Tuning of VLAs
- [uniact.md](uniact.md) — UniAct: Universal Action Tokenization

### 视觉运动策略
- [diffusion_policy.md](diffusion_policy.md) — Diffusion Policy: Visuomotor Policy Learning via Action Diffusion
- [act_aloha.md](act_aloha.md) — ACT / ALOHA: Learning Fine-Grained Bimanual Manipulation
- [dp3.md](dp3.md) — DP3: 3D Diffusion Policy
- [idp3.md](idp3.md) — iDP3: Improved 3D Diffusion Policy via Egocentric Point Clouds
- [dexwm.md](dexwm.md) — DexWM: Dexterous World Models

---

## 跨领域观察

**动作表示仍然是核心设计选择。** 所调查的模型采用了根本不同的动作表示方法：离散token（RT-2, OpenVLA）、连续流匹配（pi0, GR00T）、扩散（Diffusion Policy, RDT-1B, DP3）、CVAE（ACT）以及通用码本（UniAct）。每种选择对灵巧操作都有不同的权衡：离散token在高自由度下存在量化问题，连续方法能处理多模态但速度较慢，码本需要足够的训练多样性。目前没有任何单一方法在高自由度灵巧动作空间中展示出明显的优越性。

**灵巧手支持是例外而非常态。** 在本节调查的19个模型/系列中，只有4个具有某种形式的灵巧手支持：DP3（仅仿真）、iDP3（真实世界Inspire手）、DexWM（Allegro手）和EgoScale（仅表示层面——从视频中提取22自由度手部姿态，未进行物理机器人部署）。两大主要VLA系列（pi和GR00T）在所有版本中仍然完全以夹爪为中心。这一差距不仅仅是数据可用性的问题——主流VLA的基本动作表示、训练流程和评估协议都是围绕7D夹爪动作设计的。

**所有调查模型均缺乏力和阻抗输出。** 本节19个模型中没有任何一个输出力目标、阻抗参数或任何形式的柔顺性规格。这是一个普遍性差距：无论是VLA基础模型还是视觉运动策略，都仅生成位置（或速度）目标，依赖底层PD控制器处理接触。对于接触丰富的灵巧操作——需要调节每根手指的接触力——这代表了一个根本性的能力差距，在当前架构下无法通过扩大模型规模或训练数据来解决。

**VLM骨干网络的升级周期正在加速。** pi和GR00T系列在18个月内都多次升级了VLM骨干网络：pi从PaliGemma 3B迁移到Gemma 3 4B；GR00T从Eagle-2迁移到Eagle 2.5再到Cosmos-2B再到Cosmos-Reason2-2B。每次升级都带来改进的视觉理解和推理能力，但动作头架构保持相对稳定（pi使用流匹配，GR00T使用DiT）。这表明社区将VLM骨干网络质量视为主要的扩展轴，而动作生成被视为已解决的架构问题——这对于灵巧操作来说是一个潜在的问题假设，因为动作表示复杂度才是瓶颈。

**开源可用性与采用率相关，但与灵巧能力无关。** 最广泛采用的模型（Diffusion Policy, ACT, OpenVLA, Octo, pi0）完全开源，而最具灵巧能力的系统（EgoScale, DexWM）是封闭的。这造成了一个差距：研究社区最容易获取的工具恰恰是最不适合灵巧操作研究的，可能减缓VLA与灵巧性交叉领域的进展。

**推理速度制约实时灵巧控制。** 灵巧操作通常需要20-50 Hz的控制频率以维持稳定的手指接触。大多数VLA以1-12 Hz运行：RT-2约1-3 Hz，OpenVLA约4-6 Hz，GR00T N1.7在GPU上12 Hz或边缘设备上4.6 Hz。只有轻量级视觉运动策略（Diffusion Policy, ACT, DP3）接近灵巧控制所需的频率，但这些策略缺乏语言条件化和跨具身泛化能力。弥合这一速度-能力差距——同时实现VLA级别的泛化和视觉运动策略级别的控制频率——仍然是一个开放挑战。
