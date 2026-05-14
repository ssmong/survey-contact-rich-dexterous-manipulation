# 7. RL-based Dexterous Manipulation

> **Success rate comparability warning.** Success rates reported in Section 7.1 are NOT directly comparable across papers. They differ in: (1) simulation vs real-world evaluation, (2) hand embodiment and DoF count, (3) object set size and composition, (4) success criteria definition, and (5) state estimation method (privileged state vs vision vs point cloud). Comparisons should only be made within papers that share the same evaluation protocol.

## 7.1 Dexterous Grasping

**Papers in this section:**
1. [CrossDex](crossdex.md) -- Cross-embodiment dexterous grasping (6 hands, eigengrasp action space)
2. [ResDex](resdex.md) -- Residual policy + MoE for 3200-object grasping
3. [UniDexGrasp](unidexgrasp.md) -- First universal dexterous grasping pipeline (3000+ objects)
4. [UniDexGrasp++](unidexgrasp_pp.md) -- Iterative generalist-specialist improvement over UniDexGrasp
5. [BODex](bodex.md) -- Bilevel optimization for cross-hand grasp generation (not RL)
6. [Dexonomy](dexonomy.md) -- Taxonomy-guided grasp generation with 31 grasp types
7. [UltraDexGrasp](ultradexgrasp.md) -- Ultra-scale cross-embodiment grasp dataset (20M frames)
8. [DexGrasp Anything](dexgrasp_anything.md) -- Diffusion-based universal grasp synthesis (15K+ objects)
9. [DexGraspNet 2.0](dexgraspnet_2.md) -- Scene-aware diffusion grasping in clutter
10. [RobustDexGrasp](robustdexgrasp.md) -- Single-view point cloud grasping (94.6% real)
11. [DextrAH-G/RGB](dextrah_g.md) -- Geometric fabrics + RL for arm-hand grasping

## 7.2 In-Hand Manipulation / Reorientation

**Papers in this section:**
12. [Hora](hora.md) -- Rapid motor adaptation for in-hand rotation
13. [RotateIt](rotateit.md) -- Tactile (DIGIT) addition to Hora framework
14. [AnyRotate](anyrotate.md) -- Gravity-invariant rotation extending Hora/RotateIt
15. [Visual Dexterity](visual_dexterity.md) -- SO(3) reorientation with depth sensing
16. [DeXtreme](dextreme.md) -- Automatic domain randomization for Allegro Hand
17. [DexPBT](dexpbt.md) -- Population-based training for arm-hand systems
18. [SAPG](sapg.md) -- Split-and-merge policy gradient for high-DoF manipulation
19. [DexHandDiff](dexhanddiff.md) -- Interaction-aware diffusion planning

## 7.3 Long-Horizon / Multi-Stage / Contact-Rich

**Papers in this section:**
20. [SeqDex](seqdex.md) -- Sequential sub-policy chaining for long-horizon tasks
21. [Bi-DexHands](bi_dexhands.md) -- Bimanual dexterous manipulation benchmark (16+ tasks)
22. [DexArt](dexart.md) -- Articulated object manipulation benchmark
23. [TCDM](tcdm.md) -- MoCap-guided multi-task dexterous manipulation benchmark (50 tasks)
24. [VTDexManip](vtdexmanip.md) -- Vision-tactile dexterous manipulation dataset
25. [DexGarmentLab](dexgarmentlab.md) -- Dexterous garment manipulation benchmark

### Model-Based MPC (not RL)

26. [Contact Trust Region](contact_trust_region.md) -- Contact-implicit MPC with trust regions
27. [Complementarity-Free](complementarity_free.md) -- Differentiable compliant contact simulation
28. [ComFree-Sim](comfree_sim.md) -- GPU-parallel complementarity-free contact simulation

## 7.4 Additional Recent RL

**Papers in this section:**
29. [DQ-RISE](dq_rise.md) -- Quasi-static in-hand manipulation with sim-to-real
30. [DexTrack](dextrack.md) -- Neural tracking of human hand motion
31. [BiDexHD](bidexhd.md) -- Bimanual dexterous manipulation from human demos (141 tasks)
32. [RoboPianist](robopianist.md) -- Piano playing benchmark (150 pieces, sim-only)
33. [HandelBot](handelbot.md) -- Real-world bimanual piano playing with LEAP Hands
34. [DexDrummer](dexdrummer.md) -- Drumming with tool grasping (sim-only)
35. [DemoStart](demostart.md) -- Demonstration-bootstrapped real-world RL
36. [Closing Reality Gap](closing_reality_gap.md) -- Force-controlled dexterous grasping
37. [Maniwhere](maniwhere.md) -- Visually generalizable dexterous manipulation

---

### 분야 횡단 관찰

**Dexterous grasping is converging on diffusion and optimization approaches.** The most recent grasping works (DexGrasp Anything, DexGraspNet 2.0, BODex, Dexonomy) have moved away from end-to-end RL toward diffusion-based generative models and bilevel optimization for grasp pose synthesis. This reflects the recognition that grasp generation is fundamentally a structured prediction problem where the multi-modal distribution of valid grasps is better captured by generative models than by discriminative RL policies. PPO-based approaches (UniDexGrasp, ResDex, RobustDexGrasp) remain competitive for closed-loop execution but are increasingly used as the execution backend rather than the grasp synthesis method.

**The PKU-EPIC pipeline dominates dexterous grasping.** Seven of the eleven grasping papers (UniDexGrasp, UniDexGrasp++, BODex, DexGraspNet 2.0, Dexonomy, UltraDexGrasp, and partially DexGrasp Anything) share authors or build directly on the PKU-EPIC grasp generation pipeline. This creates a coherent progression (UniDexGrasp -> UniDexGrasp++ -> BODex -> Dexonomy -> UltraDexGrasp) but also means the literature may overfit to the assumptions of this pipeline (Shadow Hand as default, cuRobo for IK, IsaacGym for verification).

**In-hand manipulation lags behind grasping in object diversity and real-world scale.** While grasping papers routinely evaluate on thousands of objects (3200 for ResDex, 10.7K for Dexonomy, 15K+ for DexGrasp Anything), in-hand manipulation papers typically evaluate on tens of objects. The gap reflects the harder exploration problem: in-hand manipulation requires sustained multi-contact coordination, making it infeasible to train on thousands of objects without curriculum or decomposition strategies.

**Tactile sensing is emerging as essential for in-hand manipulation but absent from grasping.** RotateIt, AnyRotate, and the broader trend show that tactile feedback significantly improves in-hand manipulation robustness, particularly for detecting slip and maintaining contact under gravity. In contrast, none of the eleven grasping papers use tactile sensing, relying instead on proprioception and vision. This suggests a gap: robust grasping under uncertainty (deformable objects, uncertain friction) would likely benefit from tactile feedback.

**Sim-to-real success rates vary significantly across the two subtasks.** For grasping, real-world success rates are high and climbing (RobustDexGrasp 94.6%, DexGraspNet 2.0 90.7%). For in-hand manipulation, real-world success is harder to quantify (continuous rotation tasks are measured by sustained rotation time rather than discrete success). The grasping sim-to-real problem is arguably simpler because grasps are quasi-static events, while in-hand manipulation requires continuous dynamic control.

**Shadow Hand dominates simulation; Allegro dominates real-world.** In the grasping literature, 8 of 11 papers use Shadow Hand (24 DoF) in simulation. For real-world deployment, Allegro Hand (16 DoF) is the most common choice (RobustDexGrasp, DextrAH-G, and all in-hand manipulation real-world results except Visual Dexterity's D'Claw). This reflects Shadow Hand's role as a high-DoF simulation standard versus Allegro's practical advantages (commercially available, robust hardware, good SDK). Cross-embodiment approaches (CrossDex, BODex, Dexonomy) are beginning to bridge this gap.

**Single-axis rotation versus full SE(3) reorientation remains a frontier.** Most in-hand manipulation papers (Hora, RotateIt, AnyRotate, DeXtreme) focus on rotation around a single axis. Visual Dexterity stands out for achieving SO(3) reorientation, but on a simpler 3-finger hand (D'Claw). Achieving full SO(3) or SE(3) reorientation on a 5-finger hand with sim-to-real transfer remains an open challenge.

**No in-hand manipulation work combines vision, tactile, and force control.** Each in-hand manipulation paper uses at most two sensing modalities: proprioception + vision (Visual Dexterity, DeXtreme), or proprioception + tactile (RotateIt, AnyRotate). No work in the surveyed literature combines all three for dexterous in-hand manipulation, despite evidence that each modality provides complementary information (vision for global pose, tactile for contact state, force for interaction dynamics).

**From single-task to multi-task scale.** There is a clear progression in task-set size: from SeqDex's single chained task (2023) to Bi-DexHands' 16+ tasks (2022) to TCDM's 50 tasks (2023) to BiDexHD's 141 tasks (2025). This scaling has been enabled by GPU-parallelized simulation (primarily IsaacGym) and by leveraging human motion capture data for exploration guidance.

**Contact-implicit optimization vs. RL.** Section 7.3 includes two distinct paradigms: learning-based RL approaches (SeqDex, Bi-DexHands, DexArt, TCDM, VTDexManip, DexGarmentLab) and optimization-based contact-implicit MPC (Contact Trust Region, Complementarity-Free, ComFree-Sim). The optimization approaches offer physical consistency and constraint satisfaction but require accurate models and scale poorly to diverse objects. RL approaches scale better but offer fewer guarantees on physical consistency.

**The sim-to-real gap remains the primary bottleneck.** Of the 18 papers across Sections 7.3--7.4, only 5 demonstrate sim-to-real transfer (SeqDex, DQ-RISE, HandelBot, DemoStart, Maniwhere). The majority remain simulation-only. DemoStart takes the alternative approach of real-world RL, avoiding the sim-to-real gap entirely but requiring custom hardware with automatic resets.

**Musical instrument playing as a contact-rich benchmark.** RoboPianist, HandelBot, and DexDrummer use musical performance as a testbed for contact-rich bimanual coordination. These tasks provide natural, quantifiable success metrics (note accuracy, timing) and require rapid, precise contact events -- making them compelling benchmarks despite their niche application domain.

**Force-awareness remains rare.** Among all papers, only DQ-RISE and "Closing Reality Gap" explicitly address force-controlled manipulation. The vast majority train position-controlled policies, even for contact-rich tasks. VTDexManip includes binary tactile sensing but not continuous force feedback.

**Human demonstrations as exploration priors.** TCDM, DexTrack, BiDexHD, and DemoStart all use human demonstrations (either MoCap or teleoperation) to bootstrap RL exploration. This is emerging as a dominant strategy for scaling dexterous RL to complex tasks, addressing the fundamental exploration challenge of high-DoF manipulation.
