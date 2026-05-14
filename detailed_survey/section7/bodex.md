### 7.1 BODex

**Full title:** BODex: Bilevel Optimization for Efficient and Scalable Dexterous Grasping

**Authors:** Jiayi Chen, Yuxing Chen, Jialiang Zhang, He Wang

**Venue/Year:** ICRA 2025

**PKU-EPIC lineage:** Replaces RL-based grasp generation (UniDexGrasp/UniDexGrasp++) with bilevel optimization, enabling cross-hand support without per-hand RL training. Core algorithmic shift from learned policies to optimization-based grasp synthesis.

**RL algorithm:** Bilevel optimization (not standard RL) -- outer loop optimizes grasp contact points, inner loop solves inverse kinematics via cuRobo; generates grasp datasets rather than learned policies

**Hand hardware:** Shadow Hand (24 DoF), Allegro Hand (16 DoF), LEAP Hand (16 DoF)

**Sim platform:** cuRobo (CUDA-accelerated robot optimization)

**Sim2Real?** Yes; 81% real-world success rate (real) with generated grasps

**Object count:** 5355 objects; massive-scale grasp dataset generation

**Tasks:** Dexterous grasp generation (grasp pose synthesis rather than closed-loop control)

**Key methodology:** Formulates dexterous grasp synthesis as a bilevel optimization problem. The outer level optimizes contact point locations on the object surface to maximize grasp quality metrics (force closure, surface coverage). The inner level uses cuRobo's GPU-accelerated inverse kinematics to find feasible hand configurations reaching those contacts. This avoids RL training entirely, enabling rapid grasp generation at scale.

**Main contributions:**
- Orders of magnitude faster grasp generation than RL-based approaches (minutes vs. hours)
- Cross-embodiment support (Shadow, Allegro, LEAP) from a single optimization framework
- 81% sim-to-real transfer rate (real), validating generated grasps on physical hardware

**Quantitative results:**

| Metric | Value |
|---|---|
| Real-world success rate | 81% (real) |
| Object set size | 5355 |
| Hands supported | Shadow, Allegro, LEAP |
| Generation speed | Orders of magnitude faster than RL |

**Limitations/Gaps:** Open-loop grasp synthesis (no closed-loop execution policy); relies on accurate object geometry; no handling of object uncertainty or partial views; grasp quality metrics may not capture real-world robustness factors (surface friction, compliance)

## Inference / Deployment

- **Inference latency:** Optimization-based grasp computation is offline (not real-time inference). cuRobo-accelerated IK solving is orders of magnitude faster than RL-based alternatives for grasp generation. Deployment executes pre-computed grasps open-loop.
- **Deployment hardware:** Real deployment on Shadow, Allegro, and LEAP hands (81% real-world success rate). Grasp computation uses NVIDIA GPU via cuRobo.
- **Real-time capable?** Yes, at deployment (pre-computed grasps executed open-loop). Grasp generation itself is offline but fast (cuRobo-accelerated).

## Dataset / Data Collection

- **Dataset used:** Procedurally generated grasp dataset via bilevel optimization (not RL). 5,355 objects from 3D model repositories.
- **Collection method:** Optimization-based grasp synthesis using cuRobo (CUDA-accelerated). Outer loop optimizes contact points on object surfaces; inner loop solves inverse kinematics. Cross-embodiment (Shadow, Allegro, LEAP). No RL training, no demonstrations.
- **Data scale:** 5,355 objects. Massive-scale grasp dataset generated in minutes (vs. hours for RL approaches).
- **Teleop equipment:** Not applicable (optimization-based, no demonstrations).
- **Data format:** Generated grasp poses (hand configurations for target objects). Specific format not reported.
- **Publicly available?** Dataset/code release status not reported.
