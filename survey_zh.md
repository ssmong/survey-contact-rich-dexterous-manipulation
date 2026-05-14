# 接触丰富灵巧操作：综合综述

> 最后更新: 2026-05-14
> 范围：灵巧操作、力感知VLA、阻抗学习、RL策略及相关基准的论文、代码仓库和数据集（2018-2026年）。
> GitHub链接和权重可用性截至综述日期已验证；链接可能会失效。
>
> **标记说明：** ✅ = 可用/支持, ✗ = 不可用/不支持, — = 未报告或不适用。

**目的。** 本综述围绕三条研究主线的交叉展开：(1) 灵巧多指操作，(2) 视觉-语言-动作模型，(3) 力/阻抗感知控制。旨在梳理现有系统提供了哪些能力，以及哪些能力组合尚未充分探索，从而确定这些交叉领域的开放研究方向。范围特意聚焦于这三个领域；移动操作、工业自动化等相邻主题仅在与本综述核心主题交叉时涉及。

---

## 1. 灵巧工具使用与操作

使用多指手系统执行抓取、工具使用或超越平行夹爪的物体操作。

| 论文 | 研究组 | 会议 | 年份 | 手部(自由度) | 任务 | 仿真平台 | Sim2Real | 代码 | 权重 | VLA/语言 |
|---|---|---|---|---|---|---|---|---|---|---|
| [**SimToolReal**](https://arxiv.org/abs/2602.16863) | Stanford IPRL | arXiv | 2026 | Sharpa (22) + KUKA | 24个工具使用任务（锤子、螺丝刀、铲子） | IsaacGym | Yes | [GitHub](https://github.com/tylerlum/simtoolreal) ✅ | ✅ ckpt | ✗ |
| [**Grasp-to-Act**](https://arxiv.org/abs/2602.20466) | UIUC RoboTouch | arXiv | 2026 | LEAP (16) | 5个动态工具使用任务（锤子、锯、切割、搅拌、舀取） | Sim + real | Yes | ✗ | ✗ | ✗ |
| [**DexMachina**](https://arxiv.org/abs/2505.24853) | Stanford/NVIDIA | arXiv | 2025 | Inspire, Allegro, Xhand, Schunk | 双臂铰接物体操作 | Genesis | ✗ | [GitHub](https://github.com/MandiZhao/dexmachina) ✅ | ✗ (eval TODO) | ✗ |
| [**ManipTrans**](https://arxiv.org/abs/2503.21860) | BIGAI/Tsinghua/PKU | CVPR | 2025 | 4种手（Shadow, MANO, Inspire, Allegro） | 双臂任务（笔帽、瓶盖旋拧） | IsaacGym P4 | ✗ | [GitHub](https://github.com/ManipTrans/ManipTrans) ✅ | ✅ imitator ckpt + HF | ✗ |
| [**SPIDER**](https://arxiv.org/abs/2511.09484) | Meta FAIR / Berkeley | arXiv | 2025 | 9种人形机器人 | 重定向的人类演示 | MuJoCo | ✅ (Franka+Allegro) | [GitHub](https://github.com/facebookresearch/spider) ✅ | ✗ | ✗ |
| **Scaffolding+VLM** | Stanford / KIT | NeurIPS | 2025 | Allegro (16) + KUKA | 铰接物体（苹果、瓶子、抽屉） | Sim + real | Yes | [GitHub](https://github.com/vdebakker/vlm-scaffolding) ✅ | ✗ | ✅ Gemini VLM |
| [**DexUMI**](https://arxiv.org/abs/2505.21864) | Stanford | CoRL Best Paper Finalist | 2025 | XHand, Inspire | 真实世界灵巧操作 | 仅真实 | N/A | [GitHub](https://github.com/real-stanford/DexUMI) ✅ | ✗ | ✗ |
| [**DexterityGen**](https://arxiv.org/abs/2502.04307) | Berkeley/Meta | RSS | 2025 | Allegro (16) + 机械臂 | 工具使用（笔、螺丝刀、注射器） | IsaacGym | ✅ | ✗ | ✗ | ✗ |
| [**ArtiGrasp**](https://arxiv.org/abs/2309.03891) | ETH Zurich | 3DV | 2024 | MANO（人类代理） | 双臂抓取 + 铰接操作（8个物体） | RaiSim | ✗ | [GitHub](https://github.com/zdchan/artigrasp) ✅ | ✅ pretrained | ✗ |
| [**DexDeform**](https://arxiv.org/abs/2304.03223) | MIT-IBM | ICLR | 2023 | 多指（仿真） | 6个可变形物体任务（橡皮泥） | PlasticineLab | ✗ | [GitHub](https://github.com/sizhe-li/DexDeform) ✅ | ✗ | ✗ |

---

## 2. 灵巧VLA / 视觉-语言-动作

支持灵巧手或语言条件灵巧操作的VLA模型。

| 论文 | 研究组 | 会议 | 年份 | 手部(自由度) | 任务 | 代码 | 权重 | 核心方法 |
|---|---|---|---|---|---|---|---|---|
| [**UniDex-VLA**](https://arxiv.org/abs/2603.22264) | UniDex-AI | CVPR | 2026 | 通过FAAS支持8种手（Allegro, LEAP, Shadow, Inspire, Wuji, Oymotion, Ability, Xhand） | 工具使用，81%任务进度 | [GitHub](https://github.com/unidex-ai/UniDex) ✅ | ✅ 3-epoch + 32-epoch on HF | 3D VLA + flow matching, FAAS统一动作 |
| [**DexGraspVLA**](https://arxiv.org/abs/2502.08142) | Psi-Robot | AAAI | 2026 | 定制灵巧手 | 杂乱场景抓取，90%+成功率 | [GitHub](https://github.com/Psi-Robot/DexGraspVLA) ✅ | ✅ controller ckpt (GDrive) | Qwen2.5-VL-72B规划器 + diffusion控制器 |
| [**DexVLA**](https://arxiv.org/abs/2502.05855) | Multi-inst. | CoRL | 2025 | Yes（课程式） | 灵巧技能学习 | [GitHub](https://github.com/juruobenruo/DexVLA) ✅ | ✅ ScaleDP-H/L on HF | 在冻结VLM上的插件式1B diffusion专家 |
| **Dexora** | Multi-inst. | ICRA | 2025 | 双臂36自由度 | 抓取放置、灵巧操作、装配、工具使用 | [GitHub](https://github.com/ZZongzheng0918/Dexora) ✅ | ✅ real data on HF | 12.2K真实 + 100K仿真数据 |
| [**Grasp as You Say**](https://arxiv.org/abs/2405.19291) | Sun Yat-sen | NeurIPS | 2024 | Shadow (24) | 语言引导抓取（"抓住杯子把手"） | [GitHub](https://github.com/iSEE-Laboratory/Grasp-as-You-Say) ✅ | ✗ | 语言条件灵巧抓取生成 |
| [**HumanoidGen**](https://arxiv.org/abs/2507.00833) | TeleHuman | NeurIPS | 2025 | Unitree H1_2 + Inspire (每手6自由度) | 20个桌面任务（双臂、长时程） | [GitHub](https://github.com/TeleHuman/HumanoidGen) ✅ | ✅ HF (model + data) | LLM规划器 + MCTS + diffusion策略 |
| [**VLA+Diffusion Switch**](https://arxiv.org/abs/2410.14022) | — | arXiv | 2024 | ADAPT Hand (13) | 使用VLA切换的抓取放置 | ✗ | ✗ | VLA + diffusion策略切换，基于串联弹性多指手 |

---

## 3. 力感知VLA / 触觉VLA

融合力/力矩或触觉感知用于接触丰富任务的模型。若系统使用VLM/VLA骨干或语言条件则归入此处；否则，不含VLM骨干的力/阻抗系统归入§5。

| 论文 | 研究组 | 会议 | 年份 | 力输入 | 力/阻抗输出？ | 机器人 | 代码 | 权重 | 任务 |
|---|---|---|---|---|---|---|---|---|---|
| [**ForceVLA**](https://arxiv.org/abs/2505.22159) | SJTU/Fudan | NeurIPS | 2025 | 六轴力/力矩 | ✗（仅位置） | Flexiv Rizon + 夹爪 | [GitHub](https://github.com/ft-robotic/ForceVLA) ✅ | ✗ (data on HF) | 插件插入、擦拭、剥离（5个任务） |
| [**ForceVLA2**](https://arxiv.org/abs/2603.15169) | Shanghai AI Lab | CVPR | 2026 | 六轴力/力矩 300Hz | ✅ 混合力/位置 + 预测力 | Flexiv Rizon 4s + 夹爪 | ✗ "coming soon" | ✗ | 按压、清洁、组装齿轮（5个任务） |
| [**FD-VLA**](https://arxiv.org/abs/2602.02142) | NUS | ICRA | 2026 | 蒸馏式（推理时无传感器） | ✗ | UR5e + 夹爪 | ✗ | ✗ | 擦拭、插入、按钮按压（3个任务） |
| [**FAVLA**](https://arxiv.org/abs/2602.23648) | USTC | arXiv | 2026 | 六轴力/力矩高频 | ✗ | Monte双臂X-ARM | ✗ | ✗ | USB插入、齿轮、擦拭（4个任务） |
| [**HapticVLA**](https://arxiv.org/abs/2603.15257) | Skoltech | arXiv | 2026 | 触觉（蒸馏移除） | ✗ | LeRobot SO-101 + 触觉 | 论文声称将发布；截至2026年5月未找到公开仓库 | 未验证 | 罐子/华夫饼/鸡蛋抓取放置 |
| [**DreamTacVLA**](https://arxiv.org/abs/2512.23864) | Northwestern | arXiv | 2025 | 触觉 (V-JEPA2) | ✗ | Dobot Xtrainer + 夹爪 + 触觉 | [GitHub](https://github.com/michaelyeah7/learning-to-feel-the-future)（仅代码） | ✗ | 触觉世界模型预测未来潜在表征→动作优化；4个接触丰富任务最高95% |
| [**OmniVTLA**](https://arxiv.org/abs/2508.08706) | - | arXiv | 2025 | 视觉触觉 + 力觉触觉 | ✗ | 夹爪 + 灵巧手 | ✗（仅数据集） | ✗ | 抓取放置（灵巧手100%） |
| [**Tactile-VLA**](https://arxiv.org/abs/2507.09160) | Tsinghua | arXiv | 2025 | 触觉 | ✅ 混合位置-力 | 未指定 | ✗ | ✗ | 充电器插入90% |
| [**TaF-VLA**](https://arxiv.org/abs/2601.20321) | - | arXiv | 2026 | GelSight + 六轴力/力矩 | ✗ | Franka FR3 + 夹爪 | ✗ | ✗ | 8个接触丰富任务 |
| [**TA-VLA**](https://arxiv.org/abs/2509.07962) | Tsinghua AIR | CoRL | 2025 | 关节力矩 | 辅助力矩预测 | Cobot Magic ALOHA | ✗ | ✗ | 10个任务（按钮、充电器、USB…） |
| [**CRAFT**](https://arxiv.org/abs/2602.12532) | - | arXiv | 2026 | 力 | ✗ | 遥操作机械臂 | ✗ | ✗ | 可变形物体、对准任务 |
| [**VLA-Touch**](https://arxiv.org/abs/2507.17294) | NUS | arXiv | 2025 | GelSight触觉 | ✗（残差修正） | 机械臂 + 夹爪 | [GitHub](https://github.com/jxbi1010/VLA-Touch) ✅ | ✅ ckpts + HF | 接触丰富操作 |
| [**FoAR**](https://arxiv.org/abs/2411.15753) | SJTU | RA-L/IROS 2025 | 2024 | 六轴力/力矩 | ✗ | Flexiv Rizon + 夹爪 | [GitHub](https://github.com/Alan-Heoooh/FoAR) ✅ | ✗ | 擦拭、剥离 |
| [**FACTR**](https://arxiv.org/abs/2502.17432) | CMU | RSS | 2025 | 关节力矩（伺服电流） | ✗ | Franka + 夹爪 | [GitHub](https://github.com/RaindragonD/factr) ✅ | ✗（仅编码器） | 箱子提升、旋转、面团擀制 |
| [**ForceMimic**](https://arxiv.org/abs/2410.07554) | SJTU | ICRA | 2024 | 捕获的交互力矩 | ✅ 力矩-位置混合 | Flexiv + 夹爪 | [GitHub](https://github.com/ForceMimic/hybridil) ✅ | ✗ | 蔬菜削皮 |
| [**Reactive Diffusion Policy**](https://arxiv.org/abs/2503.02881) | - | RSS | 2025 | GelSight Mini | ✗（学习到的"类阻抗"） | Flexiv Rizon 4 + 夹爪 | [GitHub](https://github.com/xiaoxiaoxh/reactive_diffusion_policy) ✅ | ✅ ckpts + HF | 3个接触丰富任务 |
| [**ACP**](https://arxiv.org/abs/2410.09309) | Toyota/Columbia | ICRA | 2024 | 六轴力/力矩 (ATI) | ✅ 标量刚度 (K) | UR5e + 被动工具 | ✗ | ✗ | 物品翻转、花瓶擦拭 |
| [**TacDiffusion**](https://arxiv.org/abs/2409.11047) | TU Munich MIRMI | ICRA | 2024 | 触觉 | ✅ 6D力矩 | 夹爪 + 触觉 | [GitHub](https://github.com/popnut123/TacDiffusion) ✅ | ✗ | 力域diffusion，95.7%零样本 |
| [**FARM**](https://arxiv.org/abs/2510.13324) | TU Munich MIRMI | arXiv | 2025 | GelSight Mini | ✅ 夹持力 | 改装UMI夹爪 | ✗ | ✗ | 关节位置 + 力预测 |
| [**T-Dex**](https://arxiv.org/abs/2303.12076) | NYU (Pinto) | ICRA | 2024 | 触觉 (DIGIT) | ✗（仅位置） | **Allegro (16) + DIGIT** + Kinova机械臂 | [GitHub](https://github.com/irmakguzey/tdex) ✅ | ✗ | 5个灵巧任务（操纵杆、书本、碗、销钉、橡皮泥）；比纯视觉提升1.7倍。§3中极少数使用灵巧手的工作之一。 |

---

## 4. VLM引导的阻抗控制

由VLM/LLM生成或检索阻抗参数（K, D）用于底层控制器的系统。

| 论文 | 研究组 | 会议 | 年份 | K/D适应方式 | 刚度 (K) | 阻尼 (D) | 机器人 | 灵巧手？ | 代码 | 权重 |
|---|---|---|---|---|---|---|---|---|---|---|
| [**CompliantVLA-adaptor**](https://arxiv.org/abs/2601.15541) | IIT Genoa / TU Darmstadt | arXiv | 2026 | VLM (GPT-4o-mini) 零样本 | ✅ (Kx,Ky,Kz) | ✅ (Dx,Dy,Dz) | Franka Panda + 夹爪 | ✗ | 项目主页（待发布） | ✗（免训练） |
| [**OmniVIC**](https://arxiv.org/abs/2510.17150) | IIT Genoa / Georgia Tech | arXiv | 2025 | VLM + RAG自改进 | ✅ | ✅ | Franka Panda + 力/力矩传感器 | ✗ | ✗ | ✗（使用GPT-4o-mini API） |
| [**HumanoidVLM**](https://arxiv.org/abs/2601.14874) | - | HRI | 2026 | VLM (Molmo-7B) + FAISS RAG | ✅（检索） | ✅（检索） | Unitree G1人形 | ✗ | ✗ | ✗ |
| **SafeHumanoid** | 同一团队 | HRI | 2026 | VLM + RAG检索 | ✅ | ✅ | Unitree G1 | ✗ | ✗ | ✗ |
| [**ImpedanceGPT**](https://arxiv.org/abs/2503.02723) | - | IROS | 2025 | VLM (Molmo) + RAG | ✅ | ✅ | 无人机群（非操作） | N/A | [GitHub](https://github.com/Faryal-Batool/ImpedanceGPT) ✅ | ✗ |

---

## 5. 学习型阻抗 / 可变柔顺控制

不使用VLM骨干而学习或优化阻抗/刚度/阻尼参数的系统。VLM驱动的阻抗方法见§4。仅以力作为输入但输出位置的论文（如FoAR、FACTR）归入§3。

| 论文 | 研究组 | 会议 | 年份 | 刚度 (K) | 阻尼 (D) | 学习方法 | 机器人 | 灵巧手？ | 仿真 | 代码 | 权重 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [**Comp-ACT**](https://arxiv.org/abs/2406.14990) | OMRON SINIC X / UTokyo | IROS | 2024 | ✅ (12D Cholesky) | ✗ | IL（基于VR演示的ACT） | 2x UR5e + 夹爪 | ✗ | Robosuite (MuJoCo) | [GitHub](https://github.com/omron-sinicx/CompACT) ✅ | ✗ |
| [**Diff-Impedance**](https://arxiv.org/abs/2509.19696) | KIT / MIT | arXiv | 2025 | ✅ | ✅ | Diffusion + 基于能量的方法 | KUKA LBR iiwa | ✗ | Sim + real | [GitHub](https://github.com/StrokeAIRobotics/DiffusionBasedImpedanceLearning) ✅ | ✗ |
| [**VICES**](https://arxiv.org/abs/1906.08880) | Stanford / NVIDIA | IROS | 2019 | ✅ | ✅ | RL（策略梯度） | Franka/Sawyer + 夹爪 | ✗ | Robosuite (MuJoCo) | [robosuite/vices](https://github.com/ARISE-Initiative/robosuite/tree/vices_iros19) ✅ | ✗ |
| [**CHIP**](https://arxiv.org/abs/2512.14689) | NVIDIA NVLabs | ICRA | 2025 | ✅（末端执行器刚度） | ✗ | RL（事后扰动） | 人形35自由度 | ✗ | Isaac Sim | [Page](https://nvlabs.github.io/CHIP/) | ✗ |
| [**FILIC**](https://arxiv.org/abs/2509.17053) | Tsinghua/HKUST | arXiv | 2025 | 固定K | 固定B | IL（transformer，25Hz） | AIRBOT Play | ✗ | MuJoCo + real | [GitHub](https://github.com/OpenGHz/FILIC) ✅ | ✗ |
| [**CHEQ**](https://arxiv.org/abs/2501.07985) | RWTH Aachen | arXiv | 2025 | ✅ | ✅ | RL（混合自适应） | 机械臂（抛光） | ✗ | 真实硬件 | ✗ | ✗ |
| [**DA-VIL**](https://arxiv.org/abs/2410.19712) | IIIT/Brown | ICRA | 2024 | ✅ | 未报告 | RL + QP优化 | 双臂 | ✗ | Sim | 仅项目主页 | ✗ |
| [**DexForce**](https://arxiv.org/abs/2501.10356) | Stanford | RA-L | 2025 | 固定k_f | ✗ | 手动调参 | Allegro (16) | **✅** | ✗（仅真实） | ✗ | ✗ |
| [**Force Policy**](https://arxiv.org/abs/2602.22088) | SJTU/Flexiv | RSS | 2026 | 力目标 | ✗ | IL（遥操作演示） | Flexiv + 夹爪 | ✗ | ✗（仅真实） | ✗ | ✗ |
| [**IndustReal**](https://arxiv.org/abs/2305.17110) | NVIDIA | RSS | 2023 | 固定 | 固定 | RL (PPO) 学习位姿 | Franka + 夹爪 | ✗ | IsaacGym | [GitHub](https://github.com/NVlabs/industreallib) ✅ | ✅ RL policies |
| [**Divide et Impera**](https://arxiv.org/abs/2410.01054) | MIT/KIT | arXiv | 2024 | ✅（参数族） | ✅ | 神经网络成功率预测器 | 真实机械臂 | ✗ | Real | ✗ | ✗ |
| [**DCM**](https://arxiv.org/abs/2403.13221) | Omron SINIC X | IROS | 2024 | VIC输入 | ✗ | Diffusion接触模型 | 机械臂 + 夹爪 | ✗ | ✗ | ✗ | ✗ |

---

## 6. VLA基础模型：版本历史

### 6.1 Physical Intelligence pi系列

| 版本 | 日期 | 参数量 | VLM骨干 | 动作头 | 灵巧手 | 力/阻抗 | 开放权重 |
|---|---|---|---|---|---|---|---|
| **pi0** | 2024年10月 | 3.3B | PaliGemma 3B | Flow matching (300M) | ✗（夹爪） | ✗ | ✅ Apache 2.0 ([openpi](https://github.com/Physical-Intelligence/openpi), [HF](https://huggingface.co/lerobot/pi0_base)) |
| **pi0-FAST** | 2025年1月 | 3.3B | PaliGemma 3B | 自回归（FAST分词器） | ✗ | ✗ | ✅ Apache 2.0 (openpi) |
| **pi0.5** | 2025年4月 | 3.3B | PaliGemma 3B | 两阶段：FAST预训练 → flow matching | ✗ | ✗ | ✅ Apache 2.0 ([HF](https://huggingface.co/lerobot/pi05_base)) |
| **pi0.6 / pi\*0.6** | 2025年11月 | ~5B | Gemma3 4B | Flow + token双重 | ✗ | ✗ | 未正式发布；存在第三方复现 |
| **pi0.7** | 2026年4月 | ~5B | Gemma3 4B + 400M视觉 | Flow matching (860M DiT) | ✗ | ✗ | 截至2026年5月未发布 |

所有pi版本仅使用平行夹爪。动作空间为18-19D（双6自由度机械臂 + 夹爪 + 底座）。所有版本均无力或阻抗输出。

### 6.2 NVIDIA GR00T系列

| 版本 | 日期 | 参数量 | VLM骨干 | DiT层数 | 灵巧手 | 力/阻抗 | 开放权重 |
|---|---|---|---|---|---|---|---|
| **GR00T N1** | 2025年3月 | 2.2B | Eagle-2 | 16 | Fourier手（人形集成） | ✗ | ✅ 非商用 ([HF](https://huggingface.co/nvidia/GR00T-N1-2B)) |
| **GR00T N1.5** | 2025年中 | 3B | Eagle 2.5（冻结） | 16 | 未记录 | ✗ | ✅ 非商用 ([HF](https://huggingface.co/nvidia/GR00T-N1.5-3B)) |
| **GR00T N1.6** | 2025年末 | 3B | Cosmos-2B | 32 | 未记录 | ✗ | ✅ ([HF](https://huggingface.co/nvidia/GR00T-N1.6-3B)) |
| **GR00T N1.7** | 2026年5月 | 3B | Cosmos-Reason2-2B (Qwen3-VL) | 32 | 22自由度（EgoScale/Sharpa表征） | ✗ | ✅ 商用可 ([HF](https://huggingface.co/nvidia/GR00T-N1.7-3B)) |

**GR00T-Dexterity** 是一个独立的RL工作流（非VLA模型），基于DextrAH-G。它支持Allegro Hand (16自由度) + Kuka，在Isaac Lab中使用geometric fabrics。GR00T N1.x VLA模型不直接输出多指手动作。

所有GR00T VLA版本仅输出位置目标。N1.7中的"22自由度手"源自EgoScale预训练框架，该框架将人手运动表示为22自由度Sharpa手关节角度。Unitree G1的物理手（Dex3-1）每只手仅有7个自由度。22自由度能力指的是人体视频预训练中使用的动作表征，而非部署手。

### 6.3 其他主要VLA

| 论文 | 研究组 | 会议 | 年份 | 灵巧手？ | 力输出？ | 开源代码 | 开放权重 | 核心特点 |
|---|---|---|---|---|---|---|---|---|
| [**Gemini Robotics**](https://arxiv.org/abs/2503.20020) | Google DeepMind | arXiv | 2025 | ✗（夹爪） | ✗ | ✗ | ✗（封闭，受信测试者） | 基于Gemini 2.0的VLA；泛化基准2倍SOTA；ALOHA/Franka/Apollo |
| **Gemini Robotics 1.5** | Google DeepMind | Blog | 2026 | ✗ | ✗ | ✗ | ✗（受信测试者） | VLA + 推理；跨具身；Gemini API (ER 1.5) |
| **Gemini Robotics On-Device** | Google DeepMind | Blog | 2025 | ✗ | ✗ | SDK（有限） | ✗ | 端侧VLA；50-100个演示即可微调；无网络依赖 |
| [**RT-2**](https://arxiv.org/abs/2307.15818) | Google DeepMind | CoRL | 2023 | ✗ | ✗ | ✗ | ✗（封闭） | 55B VLM联合微调用于机器人动作 |
| [**OpenVLA**](https://arxiv.org/abs/2406.09246) | Berkeley/Stanford | CoRL | 2024 | ✗ | ✗ | [GitHub](https://github.com/openvla/openvla) ✅ | ✅ HF | 7B VLA基线，Apache 2.0 |
| [**OpenVLA-OFT**](https://arxiv.org/abs/2502.19645) | Stanford/Berkeley | RSS | 2025 | ✗ (ALOHA) | ✗ | [GitHub](https://github.com/moojink/openvla-oft) ✅ | ✅ | 推理速度提升26倍，并行解码 |
| [**Octo**](https://arxiv.org/abs/2405.12213) | Berkeley RAIL | RSS | 2024 | ✗ | ✗ | [GitHub](https://github.com/octo-models/octo) ✅ | ✅ HF | 93M，模块化微调 |
| [**RDT-1B**](https://arxiv.org/abs/2410.07864) | Tsinghua thu-ml | ICLR | 2025 | ✗（双臂） | ✗ | [GitHub](https://github.com/thu-ml/RoboticsDiffusionTransformer) ✅ | ✅ HF 1B | 最大开源diffusion模型 |
| [**HPT**](https://arxiv.org/abs/2409.20537) | MIT (Kaiming He) | NeurIPS | 2024 | ✗ | ✗ | [GitHub](https://github.com/liruiw/HPT) ✅ | ✗ | 异构具身预训练 |
| [**CogACT**](https://arxiv.org/abs/2411.19650) | Microsoft | arXiv | 2024 | ✗ | ✗ | [GitHub](https://github.com/microsoft/CogACT) ✅ | ✗ | 认知-动作分离 |
| [**EgoScale**](https://arxiv.org/abs/2602.16710) | NVIDIA/Berkeley | arXiv | 2026 | ✅ 22自由度 | ✗ | ✗ | ✗ | 2万小时人类视频，灵巧缩放定律 |
| [**SimpleVLA-RL**](https://arxiv.org/abs/2509.09674) | — | ICLR | 2025 | ✗ | ✗ | [GitHub](https://github.com/PRIME-RL/SimpleVLA-RL) ✅ | ✗ | VLA的RL微调 |
| [**SpatialVLA**](https://arxiv.org/abs/2501.15830) | Shanghai AI Lab / Multi-inst. | RSS | 2025 | ✗ | ✗ | ✅（项目主页） | ✅ | 3.5B VLA，基于PaliGemma2的Ego3D位置编码 + 自适应动作网格 |
| [**TinyVLA**](https://arxiv.org/abs/2409.12514) | ECNU / Midea | AAAI | 2025 | ✗ | ✗ | ✗（仅项目主页） | ✗ | 1.3B VLA + diffusion解码器；以20倍速度匹配7B OpenVLA |
| [**LLARVA**](https://arxiv.org/abs/2406.11815) | UC Berkeley | arXiv | 2024 | ✗ | ✗ | ✗（仅项目主页） | ✗ | 视觉-动作指令调优，2D视觉轨迹辅助任务 |
| [**UniAct**](https://arxiv.org/abs/2501.10105) | Multi-inst. | CVPR | 2025 | 面向多样化设计 | ✗ | [GitHub](https://github.com/2toinf/UniAct) ✅ | ✗ | 通用动作码本 |

### 6.4 视觉运动策略（无语言条件）

未使用VLM骨干但被广泛用作灵巧操作基线或模块的有影响力的视觉运动策略。

| 论文 | 研究组 | 会议 | 年份 | 灵巧手？ | 力输出？ | 开源代码 | 开放权重 | 核心特点 |
|---|---|---|---|---|---|---|---|---|
| [**Diffusion Policy**](https://arxiv.org/abs/2303.04137) | Columbia (Shuran Song) | RSS | 2023 | ✗ | ✗ | [GitHub](https://github.com/real-stanford/diffusion_policy) ✅ | ✗ | 奠基性diffusion策略方法 |
| [**ACT / ALOHA**](https://arxiv.org/abs/2304.13705) | Stanford (Tony Zhao) | RSS | 2023 | ✗（夹爪） | ✗ | [GitHub](https://github.com/tonyzhaozh/act) ✅ | ✗ | 动作分块transformer，双臂遥操作 |
| [**DP3**](https://arxiv.org/abs/2403.03954) | Tsinghua (Yanjie Ze) | RSS | 2024 | ✅（仿真） | ✗ | [GitHub](https://github.com/YanjieZe/3D-Diffusion-Policy) ✅ | ✗ | 3D点云diffusion，72个任务 |
| [**iDP3**](https://arxiv.org/abs/2410.10803) | Stanford/Tsinghua | IROS | 2025 | ✅ Inspire (25自由度) | ✗ | [GitHub](https://github.com/YanjieZe/Improved-3D-Diffusion-Policy) ✅ | ✗ | 在Fourier GR1人形上的自中心3D |
| [**DexWM**](https://arxiv.org/abs/2512.13644) | Meta FAIR / NYU | arXiv | 2025 | ✅ Allegro + Franka | ✗ | ✗ | ✗ | 灵巧手-物体交互的世界模型 |

---

## 7. 基于RL的灵巧操作

### 7.1 灵巧抓取

| 论文 | 研究组 | 会议 | 年份 | RL算法 | 手部(自由度) | 仿真 | Sim2Real | 物体 | 代码 | 权重 |
|---|---|---|---|---|---|---|---|---|---|---|
| [**CrossDex**](https://arxiv.org/abs/2410.02479) | PKU-RL | ICLR | 2025 | PPO + DAgger | 6种手（Shadow, Allegro, LEAP, ...） | IsaacGym P4 | ✅ | 100 (YCB+GRAB) | [GitHub](https://github.com/PKU-RL/CrossDex) ✅ | 部分 |
| [**ResDex**](https://arxiv.org/abs/2410.01481) | PKU-RL | ICLR | 2025 | PPO + MoE + DAgger | Shadow (24) | IsaacGym P4 | ✗ | 3200个，88.8% | [GitHub](https://github.com/PKU-RL/ResDex) ✅ | 部分 |
| [**UniDexGrasp++**](https://arxiv.org/abs/2304.00464) | PKU-EPIC | ICCV | 2023 | PPO + DAgger | Shadow (24) | IsaacGym | ✗ | 3000+，85.4% | [GitHub](https://github.com/PKU-EPIC/UniDexGrasp2) ✅ | ✅ state ckpt |
| [**UniDexGrasp**](https://arxiv.org/abs/2303.00938) | PKU-EPIC | CVPR | 2023 | PPO（目标条件） | Shadow (24) | IsaacGym | ✗ | 3000+，~60% | [GitHub](https://github.com/PKU-EPIC/UniDexGrasp) ✅ | ✗ |
| [**BODex**](https://arxiv.org/abs/2412.16490) | PKU-EPIC | ICRA | 2025 | 双层优化 | Shadow, Allegro, LEAP | cuRobo | ✅ 81% | 5355 | [GitHub](https://github.com/JYChen18/BODex) ✅ | Dataset on HF |
| [**DexGrasp Anything**](https://arxiv.org/abs/2409.11159) | ShanghaiTech | CVPR Highlight | 2025 | Diffusion | Shadow | IsaacGym | ✗ | 15K+，340万抓取 | [GitHub](https://github.com/4DVLab/DexGrasp-Anything) ✅ | ✅ HF+GDrive |
| [**DexGraspNet 2.0**](https://arxiv.org/abs/2410.15590) | PKU-EPIC | CoRL | 2024 | Diffusion | Shadow | IsaacGym | ✅ 90.7% | 1319个，4.26亿抓取 | [GitHub](https://github.com/PKU-EPIC/DexGraspNet2) ✅ | ✅ HF |
| [**RobustDexGrasp**](https://arxiv.org/abs/2501.01771) | ETH Zurich | CoRL | 2025 | PPO + 师生学习 | Allegro (16) + UR5 | RaiSim | ✅ 94.6% | 仿真247K，真实512 | [GitHub](https://github.com/zdchan/RobustDexGrasp) ✅ | ✅ |
| [**Dexonomy**](https://arxiv.org/abs/2504.01301) | PKU-EPIC | RSS | 2025 | 优化 | Shadow, Allegro, LEAP, Unitree G1 | MuJoCo + cuRobo | ✅ 82.3% | 10.7K，31种类型 | [GitHub](https://github.com/JYChen18/Dexonomy) ✅ | HF |
| [**UltraDexGrasp**](https://arxiv.org/abs/2603.05312) | InternRobotics | ICRA | 2026 | 多策略 | 多种 | BODex + cuRobo | ✅ 81.2% | 2000万帧 | [GitHub](https://github.com/InternRobotics/UltraDexGrasp) ✅ | ✗ |
| [**DexPoint**](https://arxiv.org/abs/2211.09423) | UCSD | CoRL | 2022 | PPO（点云） | Allegro (16) | IsaacGym | ✅ | 类别级新物体 | [GitHub](https://github.com/yzqin/dexpoint-release) ✅ | ✗ |
| [**AnyGrasp**](https://arxiv.org/abs/2212.08333) | SJTU (Cewu Lu) | IEEE T-RO | 2023 | 监督学习 (GSNet) | 平行夹爪 | GraspNet-1B | ✅ 93.3% | 300+未见物体，>900次/小时 | [SDK](https://github.com/graspnet/anygrasp_sdk)（需许可） | ✗ | 上游抓取检测（平行夹爪）。作为灵巧VLA流程中广泛使用的感知模块纳入。 |
| [**DextrAH-G/RGB**](https://arxiv.org/abs/2407.02274) | NVIDIA | CoRL | 2024 | PPO + geometric fabrics | Allegro (16) + Kuka | Isaac Lab | ✅ | 多物体 | [GitHub](https://github.com/NVlabs/DEXTRAH) ✅ | ✗ |

### 7.2 手内操作 / 重定向

| 论文 | 研究组 | 会议 | 年份 | 手部(自由度) | 仿真 | Sim2Real | 代码 | 权重 |
|---|---|---|---|---|---|---|---|---|
| [**Dactyl**](https://arxiv.org/abs/1808.00177) | OpenAI | arXiv 2018 / IJRR 2020 | 2018 | Shadow (24) | MuJoCo | ✅ (ADR) | ✗ | ✗ |
| [**Hora**](https://arxiv.org/abs/2210.04887) | Berkeley/Meta | CoRL | 2022 | Allegro (16) | IsaacGym P4 | ✅ | [GitHub](https://github.com/HaozhiQi/hora) ✅ | ✅ |
| [**Rotating w/o Seeing**](https://arxiv.org/abs/2303.10880) | UCSD | RSS | 2023 | Allegro (16) + 二值触觉 | IsaacGym | ✅ | [Page](https://touchdexterity.github.io) | ✗ |
| [**General In-Hand Rotation**](https://arxiv.org/abs/2309.09979) | Berkeley/Meta | CoRL | 2023 | Allegro (16) + DIGIT | IsaacGym | ✅ | (in hora repo) | ✗ |
| [**RotateIt**](https://arxiv.org/abs/2309.02388) | Berkeley/Meta/CMU | CoRL | 2023 | Allegro (16) + DIGIT | IsaacGym | ✅ | (in hora repo) | ✗ |
| [**AnyRotate**](https://arxiv.org/abs/2405.07391) | U. Bristol | CoRL | 2024 | Allegro (16) + 触觉 | IsaacGym | ✅ | ✗ | ✗ |
| [**Visual Dexterity**](https://arxiv.org/abs/2211.11744) | MIT CSAIL | Science Robotics | 2023 | D'Claw (9/12) | IsaacGym P3 | ✅ | [GitHub](https://github.com/Improbable-AI/dexenv) ✅ | ✅ |
| [**DeXtreme**](https://arxiv.org/abs/2210.13702) | NVIDIA | ICRA | 2023 | Allegro (16) | IsaacGym | ✅ | In IsaacGymEnvs ✅ | ✗ |
| [**DexPBT**](https://arxiv.org/abs/2305.12127) | NVIDIA | RSS | 2023 | Allegro (16) + Kuka | IsaacGym | ✗ | In IsaacGymEnvs ✅ | ✗ |
| [**SAPG**](https://arxiv.org/abs/2407.04890) | CMU | ICML Oral | 2024 | Allegro/Shadow (16-46) | IsaacGym P4 | ✗ | [GitHub](https://github.com/jayeshs999/sapg) ✅ | ✗ |
| [**DexHandDiff**](https://arxiv.org/abs/2411.18562) | HKU/Berkeley | CVPR | 2025 | Shadow | Adroit (MuJoCo) | ✗ | [GitHub](https://github.com/Liang-ZX/DexHandDiff) ✅ | ✅ HF |

### 7.3 长时程 / 多阶段 / 接触丰富

| 论文 | 研究组 | 会议 | 年份 | 手部(自由度) | 任务 | 仿真 | Sim2Real | 代码 | 权重 |
|---|---|---|---|---|---|---|---|---|---|
| [**SeqDex**](https://arxiv.org/abs/2309.00987) | Stanford | CoRL | 2023 | Allegro (16) | 链式策略（搜索→定向→抓取→插入） | IsaacGym | ✅ | [GitHub](https://github.com/sequential-dexterity/SeqDex) ✅ | ✅ |
| [**Bi-DexHands**](https://arxiv.org/abs/2206.08686) | PKU-MARL | NeurIPS | 2022 | 2x Shadow (48) | 16+双臂任务 | IsaacGym | ✗ | [GitHub](https://github.com/PKU-MARL/DexterousHands) ✅ | ✅ |
| [**DexArt**](https://arxiv.org/abs/2305.05706) | UCSD | CVPR | 2023 | Allegro (16) | 4个铰接物体任务 | SAPIEN | ✗ | [GitHub](https://github.com/Kami-code/dexart-release) ✅ | ✅ |
| [**TCDM**](https://arxiv.org/abs/2209.11221) | Meta | ICRA | 2023 | 3种手平台 | 50个任务，34个物体 | MuJoCo | ✗ | [GitHub](https://github.com/facebookresearch/TCDM) ✅ | ✅ |
| [**VTDexManip**](https://arxiv.org/abs/2501.01370) | - | ICLR | 2025 | 多指（仿真） | 6个任务（瓶盖、水龙头、重定向） | IsaacGym | ✗ | [GitHub](https://github.com/LQTS/VTDexManip) ✅ | ✅ 18个模型 |
| [**DexGarmentLab**](https://arxiv.org/abs/2503.18693) | Multi-inst. | NeurIPS Spotlight | 2025 | 双臂灵巧 | 15个衣物任务，2500+衣物 | IsaacSim | ✗ | [GitHub](https://github.com/wayrise/DexGarmentLab) ✅ | ✗ |
| [**Contact Trust Region**](https://arxiv.org/abs/2505.02291) | MIT CSAIL (Tedrake) | IJRR | 2025 | Allegro (16) | 接触丰富MPC | Drake | ✗ | ✗ | ✗ |
| [**Complementarity-Free**](https://arxiv.org/abs/2408.07855) | MIT CSAIL (Pang, Tedrake) | RSS | 2024 | Allegro (16) | 封闭形式可微接触，50-100 Hz MPC | Drake | ✗ | ✗ | ✗ |
| [**ComFree-Sim**](https://arxiv.org/abs/2603.12185) | — | arXiv | 2026 | LEAP Hand | 基于NVIDIA Warp的GPU并行接触MPC | Custom (Warp) | ✗ | ✗ | ✗ |

注：IndustReal（NVIDIA，RSS 2023）也使用RL解决接触丰富装配问题；详见§5。

### 7.4 近期其他RL工作

| 论文 | 研究组 | 会议 | 年份 | 手部(自由度) | 任务 | Sim2Real | 代码 |
|---|---|---|---|---|---|---|---|
| [**DQ-RISE**](https://arxiv.org/abs/2503.01766) | SJTU | ICRA | 2026 | OyMotion RoHand + Flexiv Rizon 4 | 6个真实任务，85.83% | ✅ | [GitHub](https://github.com/rise-policy/DQ-RISE) ✅ |
| [**DexTrack**](https://arxiv.org/abs/2501.15760) | PKU/Shanghai AI | ICLR | 2025 | Shadow (24), Allegro (16) | 动捕跟踪 | ✗ | [GitHub](https://github.com/Meowuu7/DexTrack) 部分 |
| [**BiDexHD**](https://arxiv.org/abs/2501.09821) | PKU | arXiv | 2025 | 2x Shadow (48) | 141个双臂任务 (TACO) | ✗ | ✗ |
| [**HandelBot**](https://arxiv.org/abs/2603.12243) | Stanford | arXiv | 2026 | LEAP (16) 双臂 | 真实钢琴弹奏 | ✅ | [GitHub](https://github.com/amberxie88/handelbot) ✅ |
| [**DexDrummer**](https://arxiv.org/abs/2603.22263) | Stanford | arXiv | 2026 | 双臂灵巧 | 打鼓（接触丰富） | ✗ | [GitHub](https://github.com/hc-fang/dexdrummer) ✅ |
| [**RoboPianist**](https://arxiv.org/abs/2304.04150) | Google/Berkeley | CoRL | 2023 | 仿人双臂 | 钢琴（150首曲目） | ✗ | [GitHub](https://github.com/google-research/robopianist) ✅ |
| [**DemoStart**](https://arxiv.org/abs/2409.06613) | Google DeepMind | ICRA | 2024 | DEX-EE（三指） | 插件插入、立方体重定向 | ✅ | ✗ |
| **Closing Reality Gap** | - | arXiv | 2026 | 五指手 | 力控抓取 | ✅ 零样本 | ✗ |
| [**Maniwhere**](https://arxiv.org/abs/2407.15815) | Shanghai AI Lab | CoRL | 2024 | Allegro (16) | 8个任务，视觉泛化 | ✅ | [GitHub](https://github.com/gemcollector/maniwhere) ✅ |
| [**Eureka**](https://arxiv.org/abs/2310.12931) | NVIDIA | ICLR | 2024 | Shadow (24，仿真) | LLM生成的奖励，转笔 | ✗ | [GitHub](https://github.com/eureka-research/Eureka) ✅ |
| [**DrEureka**](https://arxiv.org/abs/2406.01967) | NVIDIA | RSS | 2024 | Shadow（仿真）+ 四足 | LLM引导的域随机化，sim2real | ✅ | [GitHub](https://github.com/eureka-research/DrEureka) ✅ |
| [**DexMV**](https://arxiv.org/abs/2108.05877) | UCSD | ECCV | 2022 | Adroit (30，仿真) | 从人类视频的IL（倒、放置、重定位） | ✗ | [GitHub](https://github.com/yzqin/dexmv-sim) ✅ |
| [**CyberDemo**](https://arxiv.org/abs/2402.14795) | UCSD | CVPR | 2024 | Allegro (16) | 增强仿真演示，阀门旋转 | ✅ | [GitHub](https://github.com/wang59695487/CyberDemo) ✅ |

---

## 8. 数据集

### 8.1 机器人灵巧手数据集

| 数据集 | 年份 | 会议 | 规模 | 手类型 | 任务 | 力/力矩或触觉 | 下载 | 格式 |
|---|---|---|---|---|---|---|---|---|
| **UniDex** | 2026 | CVPR | 900万帧，50K+轨迹 | 8种机器人手 (FAAS) | 多样化操作 | ✗ | ✅ [HF](https://huggingface.co/datasets/UniDex-ai/UniDex) | HDF5 |
| **Dexora** | 2025 | ICRA | 12.2K集，40.5小时真实 | 双臂36自由度 | 抓取、操作、装配、工具 | ✗ | ✅ [HF](https://huggingface.co/datasets/ZZongzheng0918/Dexora) | Parquet+MP4 |
| **DexMimicGen** | 2024 | ICRA | 21K演示 | 双臂灵巧 | 9个任务 | ✗ | ✅ [HF](https://huggingface.co/datasets/MimicGen/dexmimicgen_datasets) 59.9GB | HDF5 |
| **DexGraspNet 2.0** | 2024 | CoRL | 4.26亿抓取 | Shadow | 抓取 | ✗ | ✅ [HF](https://huggingface.co/datasets/lhrlhr/DexGraspNet2.0) | WebDataset |
| **VTDexManip** | 2025 | ICLR | 56.5万帧，182个物体 | 多指（仿真） | 6个复杂任务 | ✅ 二值触觉 | ✅ [GitHub](https://github.com/LQTS/VTDexManip) | IsaacGym |
| **ManipTrans/DexManipNet** | 2025 | CVPR | 3.3K集 | 6种手 | 双臂操作 | ✗ | ✅ [HF](https://huggingface.co/datasets/ManipTrans/DexManipNet) | MuJoCo |
| **CEDex** | 2026 | ICRA | 2000万抓取，50万物体 | Shadow, Allegro, LEAP | 跨具身抓取 | ✗ | ✅ [GitHub](https://github.com/GeorgeWuzy/CEDex-Grasp) | Custom |
| **Dexonomy** | 2025 | RSS | 950万抓取，10.7K物体 | Shadow（已发布；论文涵盖Allegro, LEAP） | 31种抓取类型 | ✗ | ✅ [HF](https://huggingface.co/datasets/JiayiChenPKU/Dexonomy) | Custom |
| **Dex1B** | 2025 | RSS | 10亿演示，6K+物体 | Shadow, Inspire, Ability | 抓取 + 铰接 | ✗ | 不确定 | Custom |
| **Fourier ActionNet** | 2025 | — | 30K+轨迹，140小时 | Fourier灵巧手 | 真实人形双臂 | ✗ | ✅ [action-net.org](https://action-net.org/) | Custom |
| **RoboMIND** | 2025 | RSS | 107K轨迹，479个任务 | 多具身含灵巧 | 多样化操作 | ✗ | ✅ [HF](https://huggingface.co/datasets/x-humanoid-robomind/RoboMIND) | Custom |
| **Bi-DexHands** | 2022 | NeurIPS | 离线RL数据集 | 2x Shadow | 16+双臂任务 | ✗ | ✅ [GitHub](https://github.com/PKU-MARL/DexterousHands) | IsaacGym |
| **TCDM** | 2023 | ICRA | 50个任务，34个物体 | 3种手平台 | 多样化操作 | ✗ | ✅ [GitHub](https://github.com/facebookresearch/TCDM) | MuJoCo |
| **DAPG** | 2018 | RSS | 每任务25个人类演示 | Shadow（仿真） | 笔、门、锤子、球 | ✗ | ✅ [GitHub](https://github.com/aravindr93/hand_dapg) | Pickle/NumPy |

### 8.2 力 / 触觉 / 接触数据集

| 数据集 | 年份 | 会议 | 规模 | 传感器类型 | 手 | 下载 | 核心特点 |
|---|---|---|---|---|---|---|---|
| **ForceVLA-Data** | 2025 | NeurIPS | 244轨迹，14万步 | 六轴力/力矩 | 夹爪 (Flexiv) | ✅ [HF](https://huggingface.co/datasets/qiaojunyu/ForceVLA-real-data) | 接触丰富5个任务 |
| **REASSEMBLE** | 2024 | RSS | 4551个演示，781分钟 | 力/力矩 + 事件相机 + 音频 | 夹爪 | ✅ [TUData](https://researchdata.tuwien.ac.at/records/0ewrv-8cb44) | 多模态装配 |
| **RH20T** | 2023 | NeurIPS | 11万集，5000万帧 | 力/力矩 + 指尖触觉 | 夹爪 | ✅ [Site](https://rh20t.github.io/) | 140+任务 |
| **Touch100k** | 2025 | Info. Fusion | 10.1万样本 | GelSight | N/A | ✅ [GitHub](https://github.com/cocacola-lab/TLV-Link) | 大规模触觉-语言-视觉数据集 |
| **Sparsh/TacBench** | 2024 | CoRL | 46万+图像 | DIGIT/GelSight（跨传感器） | N/A | ✅ [GitHub](https://github.com/facebookresearch/sparsh) | 跨传感器SSL触觉编码器，5任务基准 |
| **TVL** | 2024 | ICML | 4.4万对 | DIGIT | N/A | ✅ [GitHub](https://github.com/Max-Fu/tvl) + [HF](https://huggingface.co/datasets/Max-Fu/TVL) | 触觉-视觉-语言对齐 |
| **FMB** | 2025 | IJRR | 22.5K演示 | 力/力矩 (Franka) | 夹爪 | ✅ [HF](https://huggingface.co/datasets/charlesxu0124/functional-manipulation-benchmark) | 功能性操作 |
| **FeelSight** | 2024 | Science Robotics | 70个实验 | DIGIT + Allegro | Allegro (16) | ✅ [HF](https://huggingface.co/datasets/suddhu/Feelsight) | 手内触觉-视觉跟踪 |
| **ContactPose** | 2020 | ECCV | 2306个抓取，290万图像 | 热接触 | 人手 | ✅ [GitHub](https://github.com/facebookresearch/ContactPose) | 功能性抓取 |

### 8.3 人手 / 自中心数据集

| 数据集 | 年份 | 会议 | 规模 | 模态 | 任务 | 语言 | 下载 |
|---|---|---|---|---|---|---|---|
| **EgoDex** | 2025 | ICLR | 829小时，30Hz 1080p | 自中心RGB + 68关节3D (AVP) | 194个桌面 | ✅ LLM描述 | ✅ [GitHub](https://github.com/apple/ml-egodex) ~1.7TB |
| **DexCanvas** | 2025 | arXiv | 7000小时（v0.1=1%） | 多视角RGB-D + MANO | 21种操作类型 | ✗ | ✅ [HF](https://huggingface.co/datasets/DEXROBOT/DexCanvas) v0.1 |
| **GigaHands** | 2025 | CVPR | 34小时，14K片段 | 多视角RGB + 3D手 | 双臂 | ✅ 8.4万标注 | ✅ [Site](https://ivl.cs.brown.edu/research/gigahands.html) |
| **DexWild** | 2025 | RSS | 9.5K集，33小时 | 多视角RGB + 手套 | 5个任务 | ✅ | ✅ [HF](https://huggingface.co/datasets/boardd/dexwild-dataset) 2.14TB |
| **HOI4D** | 2022 | CVPR | 240万RGB-D，4K序列 | 自中心RGB-D + 3D手 | 类别级 | ✅ 动作标签 | ✅ [Site](https://hoi4d.github.io/) |
| **GRAB** | 2020 | ECCV | 162万帧 | SMPL-X + MANO + 接触 | 全身抓取 | ✗ | ✅ [Site](https://grab.is.tue.mpg.de/)（需注册） |
| **ARCTIC** | 2023 | CVPR | 210万帧 | RGB + MANO + 接触 | 双臂铰接 | ✗ | ✅ [Site](https://arctic.is.tue.mpg.de/) ~116GB |
| **OakInk / OakInk2** | 2022/24 | CVPR | 23万+帧 | RGB + MANO + 物体 | 手-物体交互 | ✅ (v2) | ✅ [HF](https://huggingface.co/datasets/kelvin34501/OakInk-v2) |
| **DexYCB** | 2021 | CVPR | 58.2万RGB-D | RGB-D + MANO + 物体 | 抓取（20个YCB物体） | ✗ | ✅ [Site](https://dex-ycb.github.io/) 119GB |
| **Ego-Exo4D** | 2024 | CVPR | 1286小时，740名参与者 | 自中心+外视角RGB + IMU + 注视 | 熟练活动 | ✅ | ✅ [Site](https://ego-exo4d-data.org/)（需注册） |
| **Humanoid Everyday** | 2025 | arXiv | 10.3K轨迹，300万帧 | RGB + 深度 + LiDAR + 触觉 | 260个灵巧任务 | ✅ | ✅ [HF](https://huggingface.co/datasets/USC-GVL/humanoid-everyday) |

### 8.4 跨具身预训练数据集

| 数据集 | 年份 | 会议 | 规模 | 具身种类 | 任务 | 格式 | 下载 |
|---|---|---|---|---|---|---|---|
| [**Open X-Embodiment (OXE)**](https://arxiv.org/abs/2310.08864) | 2023 | arXiv/ICRA | ~100万集 | 22种机器人（仅夹爪） | 527个技能，160K+任务 | RLDS (TF Datasets) | ✅ [Site](https://robotics-transformer-x.github.io/) |
| [**DROID**](https://arxiv.org/abs/2403.12945) | 2024 | arXiv | 76K演示，350小时 | Franka Panda（1种具身，564个场景） | 84个任务，50名操作员 | 双目RGB + 本体感知 + 语言 | ✅ [Site](https://droid-dataset.github.io/) |

---

## 9. 仿真基准与平台

| 基准 | 会议 | 年份 | 灵巧手 | 仿真平台 | 核心特点 | 安装 |
|---|---|---|---|---|---|---|
| [**ManiSkill3**](https://arxiv.org/abs/2410.00425) | RSS | 2025 | Allegro, DClaw | SAPIEN (GPU) | 快430倍，RL/IL/VLA基线 | `pip install mani-skill` |
| **MuJoCo Playground** | RSS demo | 2025 | LEAP Hand | MuJoCo | 分钟级训练，零样本sim2real | `pip install playground` |
| **MuJoCo Manipulus** | 2025 | 2025 | 工具操作 | MuJoCo | 16个工具使用任务 | 开源 |
| **Adroit** | RSS | 2018 | Shadow (24) | MuJoCo | 标准RL基线 | `pip install gymnasium-robotics` |
| **Genesis** | Dec 2024 | 2024 | 任意URDF | Genesis | 430K倍实时，可微分 | `pip install genesis-world` |
| **DiffTactile** | ICLR | 2024 | 多指 | Custom | 可微分FEM触觉仿真 | [GitHub](https://github.com/Genesis-Embodied-AI/DiffTactile) |
| **TeleOpBench** | 2025 | 2025 | 3种人形 | Isaac Sim | 30个任务，4种遥操作模态 | [GitHub](https://github.com/cyjdlhy/TeleOpBench) |
| [**Isaac Lab**](https://isaac-sim.github.io/IsaacLab/) | RA-L / 2024 | 2024 | Allegro, Shadow, 任意URDF | Isaac Sim (PhysX 5) | IsaacGym继任者，GPU并行，RTX渲染 | `pip install isaaclab` |
| [**TACTO**](https://github.com/facebookresearch/tacto) | RA-L | 2022 | 夹爪（DIGIT/GelSight仿真） | PyBullet + PyRender | 基于视觉的触觉传感器仿真器 | `pip install tacto` |

---

## 10. 遥操作系统

| 系统 | 研究组 | 会议 | 年份 | 输入 | 目标手 | 力反馈 | 成本 | 代码 |
|---|---|---|---|---|---|---|---|---|
| [**DexCap**](https://arxiv.org/abs/2403.07788) | Stanford | RSS | 2024 | SLAM + 电磁 | LEAP Hand | ✗ | ~$2K | [GitHub](https://github.com/j96w/DexCap) ✅ |
| [**BunnyVisionPro**](https://arxiv.org/abs/2407.03162) | HKU / UCSD | arXiv | 2024 | Apple Vision Pro | 双臂灵巧 | 低成本触觉 | ~$3.5K+ | [GitHub](https://github.com/Dingry/BunnyVisionPro) ✅ |
| **AnyTeleop** | UCSD | RSS | 2023 | 视觉（摄像头） | 多种 | ✗ | 低 | 项目主页 |
| [**DOGlove**](https://arxiv.org/abs/2505.14635) | TEA Lab | RSS | 2025 | 触觉手套 | 任意灵巧手 | ✅ 5自由度 | <$600 | [GitHub](https://github.com/TEA-Lab/DOGlove) ✅ |
| [**DEXOP**](https://arxiv.org/abs/2509.04441) | Stanford | arXiv | 2025 | 被动外骨骼 | 任意灵巧手 | ✅ 本体感知 | - | [Page](https://dex-op.github.io/) |
| [**DEX-Mouse**](https://arxiv.org/abs/2604.15013) | - | arXiv | 2026 | 手持式接口 | 通用 | ✅ 动觉 | <$150 | 已开源 |
| [**Open TeleDex**](https://arxiv.org/abs/2510.14771) | - | arXiv | 2025 | 手机 | 任意臂 + 手 | ✗ | 极低 | [GitHub](https://github.com/omarrayyann/TeleDex) ✅ |
| [**OmniH2O**](https://arxiv.org/abs/2406.08858) | CMU LeCAR | CoRL | 2024 | VR/语音/RGB | 人形 | ✗ | - | [GitHub](https://github.com/LeCAR-Lab/human2humanoid) ✅ |
| [**Open-TeleVision**](https://arxiv.org/abs/2407.10107) | UCSD | CoRL | 2024 | 立体VR | 双臂灵巧 | ✗ | - | [GitHub](https://github.com/OpenTeleVision/TeleVision) ✅ |
| [**HATO**](https://arxiv.org/abs/2404.16823) | UC Berkeley | ICRA | 2024 | Meta Quest 2 VR | 2x Psyonic Ability Hand (6自由度) + 触觉传感器 | ✗（仅机器人端触觉） | 低（VR + 假肢手） | [GitHub](https://toruowo.github.io/hato/) ✅ |
| [**DexPilot**](https://arxiv.org/abs/1910.03135) | NVIDIA | ICRA | 2020 | 视觉（裸手，单RGB摄像头） | Allegro (16) + Kuka IIWA | ✗ | 极低（仅需摄像头） | [Page](https://sites.google.com/view/dex-pilot) |

---

## 11. 低成本灵巧手硬件

| 手 | 研究组 | 年份 | 自由度 | 成本 | Sim2Real | 触觉 | 设计文件 |
|---|---|---|---|---|---|---|---|
| **LEAP Hand V2** | CMU (Pathak) | 2024 | 16 + 掌部 | ~$3K | ✅ | ✗ | [Page](https://v2-adv.leaphand.com/) |
| **ORCA Hand** | ETH Zurich | 2025 | 17 | <$2K | ✅（1小时训练） | ✅ | [orcahand.com](https://www.orcahand.com/) 完全开源 |
| **ISyHand** | MPI-IS | 2025 | 18 (12+6掌部) | ~$1.3K | ✅ | ✗ | [Page](https://isyhand.is.mpg.de/) |
| **RUKA Hand** | NYU (Pinto) | 2025 | 15 | <$1.3K | ✅ | ✗ | [Page](https://ruka-hand.github.io/) |
| **FAIVE Hand** | ETH Zurich (SRL) | 2024 | 11+ | ~$500-800 | ✅ | ✗ | [GitHub](https://github.com/srl-ethz/faive-hand) 完全开源 |
| **Ability Hand** | PSYONIC Inc. | 2024 | 6 | 商用 | — | ✅ 指尖压力 | [psyonic.io](https://www.psyonic.io/ability-hand) 封闭 |
| **XHand / Inspire Hand** | 中国制造商 | 2023+ | 12-16 | ~$1-3K | 部分 | ✗ | 封闭源商用 |
| **Digit 360** | Meta FAIR | 2024 | N/A（传感器） | - | N/A | ✅ 18+种模态 | 计划开源 |

---

## 12. 触觉表征模型

| 模型 | 研究组 | 会议 | 年份 | 核心特点 | 代码 |
|---|---|---|---|---|---|
| **Sparsh** | Meta FAIR/CMU | CoRL | 2024 | SSL跨传感器触觉编码器，TacBench 5任务基准 | [GitHub](https://github.com/facebookresearch/sparsh) ✅，权重 ✅ |
| **UniTouch** | UCSD | CVPR | 2024 | 统一触觉-视觉-语言-声音对齐 | [GitHub](https://github.com/cfeng16/UniTouch) ✅，权重 ✅ |
| **AnyTouch** | Renmin Univ | ICLR | 2025 | 基于TacQuad 4传感器数据集的跨传感器SSL | [GitHub](https://github.com/GeWu-Lab/AnyTouch) ✅，权重 ✅ |
| **NeuralFeels** | Meta FAIR | Science Robotics | 2024 | 用于Allegro+DIGIT手内跟踪的神经场 | [GitHub](https://github.com/facebookresearch/neuralfeels) ✅ |

---

## 13. 开放研究方向

本节重点介绍从综述文献中浮现的尚未充分探索的能力交叉点。这些方向并非详尽无遗；同期或未发表的工作可能已部分解决其中一些方向。

### 13.1 能力矩阵

下表将代表性系统映射到与接触丰富灵巧操作相关的属性。"仿真"指用于训练或评估的公开可用仿真环境。

|  | 多指手 | 工具使用 | 力/阻抗输出 | VLA/语言 | 仿真 |
|---|---|---|---|---|---|
| **pi0~0.7** | ✗（仅夹爪） | ✗ | ✗ | ✅ | ✗ |
| **GR00T N1~1.7** | 仅人形集成 | ✗ | ✗ | ✅ | ✅ Isaac Lab |
| **GR00T-Dexterity** | ✅ Allegro | ✗（仅抓取） | ✗ | ✗（仅RL） | ✅ Isaac Lab |
| **UniDex-VLA** | ✅ 8种手 | ✅ | ✗ | ✅ | 部分（重定向环境） |
| **DexVLA** | ✅ | ✗ | ✗ | ✅ | ✗ |
| **SimToolReal** | ✅ Sharpa 22自由度 | ✅ 24个任务 | ✗ | ✗ | ✅ IsaacGym |
| **CompliantVLA-adaptor** | ✗（夹爪） | ✗ | ✅ K, D | ✅（冻结VLA） | ✅ LIBERO |
| **CHIP** | 人形35自由度 | ✗ | ✅ 末端刚度 (K) | ✗ (RL) | ✅ |
| **TacDiffusion** | ✗（夹爪） | ✗ | ✅ 6D力矩 | ✗ | ✗ |
| **DexForce** | ✅ Allegro | ✗ | 固定k_f（手动调参） | ✗ | ✗ |

### 13.2 观察与发现

使用多指手进行的接触丰富操作——例如工具使用、装配或处理易碎物体——需要调节交互力，而不仅仅是跟踪位置目标。力控制不足会导致物体滑落、工具损坏或环境破坏。虽然夹爪通常可以通过机械柔顺性来补偿，但高自由度灵巧手将接触分布在多个指尖，使得逐接触点力调节更加关键且更具挑战性。这促使我们审视现有系统是否将灵巧控制与力/阻抗感知相结合。

能力矩阵和更广泛的综述揭示了以下几个模式：

**灵巧VLA与力感知策略在很大程度上是独立发展的。** 灵巧VLA文献（§2）关注跨多种手的位置目标生成，而力/阻抗文献（§3-5）关注夹爪和机械臂的接触丰富控制。UniDex-VLA、DexVLA和DexGraspVLA均只输出位置目标。相反，输出阻抗参数的系统（CompliantVLA-adaptor、CHIP、Comp-ACT、VICES）仅在夹爪或机械臂上运行。DexForce是唯一一项结合力感知的灵巧手工作，在Allegro Hand上使用手动调参的固定缩放。

**跨具身动作表征仍然碎片化。** 多种方法竞相表征跨具身的灵巧手动作：FAAS（UniDex-VLA）、特征抓取（CrossDex）、通用码本（UniAct）、异构stems（HPT）以及每具身MLP（GR00T）。目前尚无共识哪种表征最能支持跨手泛化，且这些方法之间的直接比较十分稀少。

**灵巧数据采集是公认的瓶颈。** 低成本遥操作系统（§10）的大量涌现——DexCap、DOGlove、DEXOP、DEX-Mouse，均发表于2024-2026年——表明社区将数据采集视为主要障碍。尽管付出了这些努力，大多数灵巧数据集（§8.1）仍然只捕获关节位置和视觉数据，力/力矩模态几乎仅在基于夹爪的系统（§8.2）中可用。

**灵巧RL的Sim-to-Real迁移正在走向成熟。** 多篇近期论文展示了灵巧手的零样本或接近零样本sim-to-real迁移：CrossDex（LEAP）、RobustDexGrasp（Allegro，94.6%）、DeXtreme（Allegro）、DQ-RISE（LEAP+Franka，85.8%）以及HandelBot（双臂LEAP）。这表明仿真训练的灵巧策略正变得可实际部署，降低了该领域基于仿真研究的门槛。

**VLA模型系列仍以夹爪为中心。** 在所有综述的pi版本（pi0到pi0.7）和GR00T版本（N1到N1.7）中，没有任何版本原生支持独立的多指灵巧手（§6.1-6.2）。GR00T-Dexterity增加了Allegro支持，但作为独立的RL工作流，而非VLA本身的一部分。开源VLA生态系统（openpi、Isaac-GR00T、OpenVLA）尚未被社区扩展到灵巧手具身。

**基于模型的接触控制是一个互补维度。** 接触隐式MPC和可微分接触模型（Contact Trust Region、Complementarity-Free、ComFree-Sim）为接触丰富灵巧操作中的学习型阻抗提供了替代方案。近期工作在Allegro和LEAP手上实现了50-100 Hz的实时MPC。这些方法提供了学习策略通常缺乏的形式化保证（如互补性约束、无源性），但需要精确的动力学模型，且在软体/可变形接触中面临困难。基于模型和基于学习的力控制如何在灵巧手上结合——例如由基于模型的内环跟踪的学习型阻抗设定点——在很大程度上仍未被探索。

---

## 14. 参考链接

### 精选列表
- [Awesome-Force-Tactile-VLA](https://github.com/OpenHelix-Team/Awesome-Force-Tactile-VLA) — 力/触觉VLA论文维护列表

### 重要GitHub组织 / 项目主页
- [Google DeepMind](https://deepmind.google/models/gemini-robotics/) — Gemini Robotics, Gemini Robotics-ER, RT-2
- [PKU-EPIC](https://github.com/PKU-EPIC) — DexGraspNet, UniDexGrasp, BODex, Dexonomy
- [PKU-RL](https://github.com/PKU-RL) — CrossDex, ResDex
- [NVlabs](https://github.com/NVlabs) — DextrAH, DexMimicGen, IndustReal, CHIP
- [UniDex-AI](https://github.com/unidex-ai) — UniDex-VLA
- [Physical-Intelligence](https://github.com/Physical-Intelligence) — openpi (pi0, pi0-FAST, pi0.5); pi0.6, pi0.7未公开发布
- [NVIDIA Isaac-GR00T](https://github.com/NVIDIA/Isaac-GR00T) — GR00T N1~N1.7
- [ForceMimic](https://github.com/ForceMimic) — ForceMimic, ForceCapture
- [Meta FAIR](https://github.com/facebookresearch) — SPIDER, TCDM, Sparsh, NeuralFeels
