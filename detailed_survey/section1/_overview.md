# Section 1: Dexterous Tool Use & Manipulation

This section surveys recent work on multi-fingered hand systems performing grasping, tool use, or object manipulation beyond parallel-jaw grippers. Each paper is reviewed in detail covering methodology, hardware, evaluation, and contributions.

**Papers in this section:**
- [SimToolReal](simtoolreal.md) -- Sim-to-real pipeline for 24 dexterous tool-use tasks (Sharpa Hand, 22 DoF)
- [Grasp-to-Act](grasp_to_act.md) -- Grasp-to-action decomposition for dynamic tool use (Allegro Hand, 16 DoF)
- [DexMachina](dexmachina.md) -- Human video to multi-embodiment dexterous policies (4 robot hands)
- [ManipTrans](maniptrans.md) -- Cross-embodiment manipulation transfer (6 robot hands, CVPR 2025)
- [SPIDER](spider.md) -- Embodiment retargeting across 9 humanoid platforms (Meta FAIR)
- [Scaffolding+VLM](scaffolding_vlm.md) -- VLM-scaffolded demonstration generation (Allegro Hand, NeurIPS 2025)
- [DexUMI](dexumi.md) -- Real-world-only dexterous data collection interface (CoRL 2025 Best Paper Finalist)
- [DexterityGen](dexteritygen.md) -- Foundation controller for tool use, 3 tools demonstrated (Allegro Hand, RSS 2025)
- [ArtiGrasp](artigrasp.md) -- Bimanual grasping and articulation synthesis (MANO hands, 3DV 2024)
- [DexDeform](dexdeform.md) -- Deformable object manipulation with differentiable physics (ICLR 2023)

---

## Cross-cutting Observations

Several patterns emerge across the 10 papers in this section:

**Position control dominates; force awareness is absent.** None of the 10 papers incorporates explicit force/torque sensing or impedance control for the dexterous hand. All systems output joint position or angle targets. This is notable because many of the tasks (hammering, sawing, deformable manipulation) inherently involve significant contact forces. The field relies on simulation contact models or hardware compliance to handle forces implicitly.

**Cross-embodiment evaluation is a growing theme.** Multiple papers evaluate on diverse hand platforms: ManipTrans (6 hands), SPIDER (9 embodiments), DexMachina (4 hands), and DexUMI (2 hands). This reflects a community push toward general dexterous manipulation methods that are not locked to a single hardware platform. The Allegro hand (16 DoF) appears as an evaluation platform in 5 of 10 papers, making it the de facto standard.

**Sim-to-real remains the primary paradigm, with notable exceptions.** SimToolReal, Grasp-to-Act, Scaffolding+VLM, and DexterityGen demonstrate sim-to-real transfer. DexUMI takes the contrasting real-world-only approach (CoRL Best Paper Finalist), suggesting that both paradigms have merit. Five papers (DexMachina, ManipTrans, SPIDER, ArtiGrasp, DexDeform) remain simulation-only.

**Human demonstrations as the starting point.** Most approaches use human demonstrations as initialization -- either from video (DexMachina), motion capture (SPIDER, ManipTrans), teleoperation (DexUMI, Grasp-to-Act), or VLM-generated proxies (Scaffolding+VLM). Only SimToolReal and DexterityGen rely purely on RL reward engineering without human demonstration data, at the cost of significant per-task engineering effort.

**VLM/language integration is minimal.** Only Scaffolding+VLM incorporates a vision-language model (Gemini 2.5 Flash), and it uses the VLM for demonstration generation scaffolding rather than as a policy backbone. No paper in this section uses a VLA architecture for dexterous control. This contrasts sharply with the gripper-based VLA literature (Section 2 of the survey), highlighting a gap between foundation model capabilities and dexterous hand control.

**Deformable and articulated objects expand the task frontier.** DexDeform (deformable objects) and ArtiGrasp (articulated objects) push beyond rigid-body grasping and tool use, addressing object categories with internal degrees of freedom. These works remain simulation-only, reflecting the additional challenges of modeling complex object physics for sim-to-real transfer.

**IsaacGym is the dominant simulation platform** for papers that demonstrate sim-to-real transfer (SimToolReal, DexterityGen, ManipTrans), while alternative platforms serve niche purposes: Genesis for cross-embodiment retargeting (DexMachina), RaiSim for contact-rich bimanual tasks (ArtiGrasp), PlasticineLab for differentiable deformable physics (DexDeform), and MuJoCo for broad embodiment support (SPIDER).
