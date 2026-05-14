# Section 3: Force-aware VLA / Tactile VLA -- Overview

> Models incorporating force/torque or tactile sensing for contact-rich tasks. This section covers systems that use a VLM/VLA backbone or language conditioning together with force/tactile modalities. Force/impedance-focused systems without a VLM backbone appear in Section 5.

## Papers in this section

| # | Paper | Force/Tactile Input | Force Output | Robot | VLA? |
|---|-------|---------------------|--------------|-------|------|
| 3.1 | [ForceVLA](forcevla.md) | 6-axis F/T | No (position-only) | Flexiv Rizon 4 | Yes |
| 3.2 | [ForceVLA2](forcevla2.md) | 6-axis F/T (300 Hz) | Yes (full wrench) | Flexiv Rizon 4s | Yes |
| 3.3 | [FD-VLA](fd_vla.md) | Distilled F/T | No (position-only) | UR5e | Yes |
| 3.4 | [FAVLA](favla.md) | Dual 6-axis F/T | No (position-only) | Monte dual-arm (X-ARM) | Yes |
| 3.5 | [HapticVLA](hapticvla.md) | Distilled tactile | No (position-only) | LeRobot SO-101 | Yes |
| 3.6 | [DreamTacVLA](dreamtacvla.md) | Vision-based tactile (V-JEPA2) | No (position-only) | Dobot Xtrainer | Yes |
| 3.7 | [OmniVTLA](omnivtla.md) | Vision-based + force-based tactile | No (position-only) | Gripper + dex hand | Yes |
| 3.8 | [Tactile-VLA](tactile_vla.md) | Tactile sensor | Yes (partial: hybrid pos-force) | Not specified | Yes |
| 3.9 | [TaF-VLA](taf_vla.md) | GelSight + 6-axis F/T | No (position-only) | Franka FR3 | Yes |
| 3.10 | [TA-VLA](ta_vla.md) | Joint torque (motor current) | Auxiliary torque prediction | Cobot Magic ALOHA | Yes |
| 3.11 | [CRAFT](craft.md) | Force sensing | No (position-only) | Franka Panda | Yes |
| 3.12 | [VLA-Touch](vla_touch.md) | GelSight tactile | No (residual correction) | Arm + gripper + GelSight | Yes |
| 3.13 | [FoAR](foar.md) | 6-axis F/T | No (position-only) | Flexiv Rizon | No |
| 3.14 | [FACTR](factr.md) | Joint torque (motor current) | No (position-only) | Franka Panda | Yes |
| 3.15 | [ForceMimic](forcemimic.md) | Captured interaction wrench | Yes (full wrench) | Flexiv Rizon | No |
| 3.16 | [Reactive Diffusion Policy](reactive_diffusion_policy.md) | GelSight Mini tactile | No (position-only, impedance-like) | Flexiv Rizon 4 | Yes |
| 3.17 | [ACP](acp.md) | 6-axis F/T (ATI) | Yes (partial: scalar stiffness) | UR5e | No |
| 3.18 | [TacDiffusion](tacdiffusion.md) | Tactile sensor | Yes (full wrench: 6D) | Gripper + tactile | Yes |
| 3.19 | [FARM](farm.md) | GelSight Mini tactile | Yes (partial: grip force) | Modified UMI gripper | Yes |
| 3.20 | [T-DEX](tdex.md) | DIGIT vision-based tactile | No (position-only) | Allegro Hand (16 DoF) + Kinova Jaco | No |

## Cross-cutting Observations

### 1. Input modality vs. output modality asymmetry

A striking pattern across all 20 papers is the asymmetry between force/tactile input and force output. While all 20 papers use force or tactile information as input, only 6 produce any form of force/impedance output. The remaining 14 papers use force/tactile exclusively as input to improve position-only action generation. This suggests the community has largely addressed the "sensing" side of force-aware manipulation but the "actuation" side -- actively commanding forces -- remains underdeveloped.

**Force output subdivision:**
- **Full wrench output (6D forces + torques):** ForceVLA2, ForceMimic, TacDiffusion
- **Partial force output:** Tactile-VLA (hybrid pos-force), FARM (grip force only), ACP (scalar stiffness only)

### 2. Sensor type fragmentation

The papers span a wide range of force/tactile sensor types: 6-axis F/T sensors (ForceVLA, ForceVLA2, FAVLA, TaF-VLA, FoAR, ACP), GelSight vision-based tactile (TaF-VLA, VLA-Touch, Reactive Diffusion Policy, FARM), DIGIT-style tactile, joint torque from motor current (TA-VLA, FACTR), and distilled/virtual force (FD-VLA, HapticVLA). There is no standardization on which force/tactile modality works best, and very few papers compare across sensor types. TaF-VLA is the only paper that fuses two force modalities (GelSight + F/T), though it does not compare against papers using other sensor combinations.

### 3. The distillation trend

Three papers (FD-VLA, HapticVLA, and partially TA-VLA with its auxiliary torque prediction) explore using force/tactile data during training but operating without sensors at inference. This "force distillation" paradigm offers a practical path to deploying force-aware policies on low-cost robots, but fundamentally limits the system to visual inference about contact -- it cannot react to truly unexpected contact events that are only observable through force/tactile sensing.

### 4. Task evaluation remains narrow

Despite spanning 20 papers, the task repertoire is dominated by insertion tasks (plug, USB, charger, connector), wiping/cleaning, and peeling. Only a few papers evaluate on more diverse tasks: TA-VLA (10 tasks), TaF-VLA (8 tasks), and ForceVLA/ForceVLA2 (5 tasks each). The contact-rich task benchmarks used across papers are not standardized, making direct comparison difficult.

### 5. Dexterous hand gap

T-DEX is the sole paper evaluating force/tactile manipulation on a dexterous hand (Allegro) with non-trivial contact-rich tasks. However, T-DEX uses a non-parametric nearest-neighbor policy without language conditioning -- it is not a VLA. No VLA with language conditioning has been evaluated on a multi-finger dexterous hand for contact-rich tasks beyond simple pick-and-place (OmniVTLA).

### 6. Temporal scale challenges

Force and tactile signals operate at much higher frequencies (100-1000 Hz) than typical VLA inference rates (5-20 Hz). Papers address this mismatch differently: ForceVLA2 uses temporal convolution on 300 Hz F/T data, Reactive Diffusion Policy uses a slow-fast dual architecture, FACTR uses force-attending transformer layers with curriculum training, and most others simply downsample force signals to match the VLA rate. The optimal approach for bridging these temporal scales remains an open question.

### 7. Reproducibility varies widely

Of the 20 papers, ~10 release code publicly: ForceVLA, FoAR, FACTR, ForceMimic, Reactive Diffusion Policy, VLA-Touch, TacDiffusion, DreamTacVLA, T-DEX, and FARM. Among these, only Reactive Diffusion Policy and VLA-Touch release both code and model checkpoints. The remaining ~10 papers have no public code, limiting reproducibility and building upon prior work.

Note on ForceVLA: the public release is primarily the ForceVLA-Data dataset on HuggingFace (244 trajectories). Whether model code (as opposed to data-only) is publicly available should be independently verified.

### 8. Robot platform concentration

The Flexiv Rizon platform appears in 5 of the 20 papers (ForceVLA, ForceVLA2, FoAR, ForceMimic, Reactive Diffusion Policy), reflecting its built-in 6-axis F/T sensing and compliance control capabilities. Franka Panda/FR3 appears in 3 papers (TaF-VLA, FACTR, CRAFT). The concentration on a small number of platforms limits evidence for cross-platform generalization of force-aware VLA approaches.

### 9. Position of force-aware VLAs in the broader VLA landscape

Comparing Section 3 to the VLA foundation models in Section 6, none of the major VLA families (pi0, GR00T N1, OpenVLA, Octo, RDT-1B) include force/tactile input or force output. Force-aware VLAs remain a specialized niche built on top of or inspired by these foundation models, rather than being integrated into the foundation models themselves. This suggests that force/tactile modalities are not yet considered essential to VLA pretraining, despite their importance for contact-rich tasks.

### 10. From reactive to predictive force reasoning

Most papers use force/tactile input reactively -- adjusting actions based on current contact state. DreamTacVLA is a notable exception, introducing a tactile world model that predicts future contact states and uses these predictions to proactively adjust actions. This predictive approach is promising for anticipatory force control (e.g., adjusting grip force before an expected impact), but remains largely unexplored beyond this single paper.
