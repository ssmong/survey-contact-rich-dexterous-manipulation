# 第一章：灵巧工具使用与操作

本章综述了近期关于多指手系统执行抓取、工具使用或超越平行夹爪的物体操作的研究工作。每篇论文均从方法论、硬件、评估和贡献等方面进行了详细评述。

**本章包含的论文：**
- [SimToolReal](simtoolreal.md) -- 面向24项灵巧工具使用任务的仿真到真实迁移流程（Sharpa Hand，22自由度）
- [Grasp-to-Act](grasp_to_act.md) -- 面向动态工具使用的抓取到动作分解（Allegro Hand，16自由度）
- [DexMachina](dexmachina.md) -- 从人类视频到多形态灵巧策略（4种机器人手）
- [ManipTrans](maniptrans.md) -- 跨形态操作迁移（6种机器人手，CVPR 2025）
- [SPIDER](spider.md) -- 跨9个人形平台的形态重定向（Meta FAIR）
- [Scaffolding+VLM](scaffolding_vlm.md) -- VLM辅助的演示生成（Allegro Hand，NeurIPS 2025）
- [DexUMI](dexumi.md) -- 纯真实世界灵巧数据采集接口（CoRL 2025最佳论文提名）
- [DexterityGen](dexteritygen.md) -- 工具使用基础控制器，演示3种工具（Allegro Hand，RSS 2025）
- [ArtiGrasp](artigrasp.md) -- 双手抓取与铰接体操作合成（MANO手，3DV 2024）
- [DexDeform](dexdeform.md) -- 基于可微物理的可变形物体操作（ICLR 2023）

---

## 跨论文观察

本章10篇论文呈现出以下几个共性模式：

**位置控制占主导；力感知缺失。** 10篇论文中没有任何一篇引入了显式的力/力矩传感或阻抗控制。所有系统均输出关节位置或角度目标值。值得注意的是，许多任务（锤击、锯切、可变形操作）本质上涉及显著的接触力。该领域依赖仿真接触模型或硬件柔顺性来隐式处理力。

**跨形态评估成为日益增长的主题。** 多篇论文在多种手部平台上进行了评估：ManipTrans（6种手）、SPIDER（9种形态）、DexMachina（4种手）和DexUMI（2种手）。这反映了社区对通用灵巧操作方法的推动，使其不再局限于单一硬件平台。Allegro Hand（16自由度）作为评估平台出现在10篇论文中的5篇中，使其成为事实上的标准。

**仿真到真实仍是主要范式，但存在显著例外。** SimToolReal、Grasp-to-Act、Scaffolding+VLM和DexterityGen展示了仿真到真实的迁移。DexUMI采取了相反的纯真实世界方法（CoRL最佳论文提名），表明两种范式均有其价值。五篇论文（DexMachina、ManipTrans、SPIDER、ArtiGrasp、DexDeform）仍停留在仿真阶段。

**人类演示作为起点。** 大多数方法使用人类演示作为初始化——来自视频（DexMachina）、运动捕捉（SPIDER、ManipTrans）、遥操作（DexUMI、Grasp-to-Act）或VLM生成的代理（Scaffolding+VLM）。只有SimToolReal和DexterityGen完全依赖强化学习奖励工程，不使用人类演示数据，但代价是需要大量的逐任务工程工作。

**VLM/语言集成度极低。** 仅Scaffolding+VLM引入了视觉语言模型（Gemini 2.5 Flash），且其将VLM用于演示生成辅助而非作为策略主干。本章中没有论文使用VLA架构进行灵巧控制。这与基于夹爪的VLA文献（综述第二章）形成了鲜明对比，突显了基础模型能力与灵巧手控制之间的差距。

**可变形和铰接物体拓展了任务边界。** DexDeform（可变形物体）和ArtiGrasp（铰接物体）超越了刚体抓取和工具使用，涉及具有内部自由度的物体类别。这些工作仍停留在仿真阶段，反映了为仿真到真实迁移建模复杂物体物理特性的额外挑战。

**IsaacGym是主导仿真平台**，用于展示仿真到真实迁移的论文（SimToolReal、DexterityGen、ManipTrans），而其他平台服务于特定用途：Genesis用于跨形态重定向（DexMachina）、RaiSim用于接触密集的双手任务（ArtiGrasp）、PlasticineLab用于可微可变形物理（DexDeform）、MuJoCo用于广泛的形态支持（SPIDER）。
