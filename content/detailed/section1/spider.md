### SPIDER

**Full Title:** SPIDER: Sim-to-Real Policy Adaptation for Dexterous Manipulation via Embodiment Retargeting

**Authors:** Researchers from Meta FAIR / UC Berkeley et al.

**Venue/Year:** arXiv preprint, 2025

**Hand Hardware:** 9 different humanoid embodiments evaluated. SPIDER targets the broad challenge of retargeting human demonstrations to diverse humanoid robot morphologies, covering a wide range of hand-arm kinematic configurations.

**Tasks:** Retargeted human demonstration tasks. The system takes human motion capture data and produces physically executable policies for different humanoid embodiments. Tasks span manipulation behaviors captured from human demonstrations.

**Key Methodology:** SPIDER addresses sim-to-real policy adaptation through embodiment retargeting. The approach takes human demonstrations captured via motion capture and retargets them to target humanoid embodiments using a physics-based optimization in MuJoCo simulation. The retargeting preserves the functional intent of the original human motion while respecting the kinematic and dynamic constraints of each target embodiment. The method focuses on producing physically plausible motions that can serve as initializations for further RL-based policy refinement.

**Architecture/Parameters:** The retargeting pipeline uses optimization-based motion adaptation combined with physics simulation to ensure dynamic feasibility. Specific network architecture details depend on the downstream policy learning approach.

**Sim Platform:** MuJoCo. Sim-to-real transfer IS demonstrated -- the paper deploys retargeted trajectories on a physical Franka Emika Panda + Allegro Hand system for four dexterous tasks (rotating light bulb, manipulating spoon, playing guitar, unplugging charger). Trajectories are retargeted from single RGB video input and executed directly on the physical robot.

**Main Contributions:**
- Proposes a retargeting framework covering 9 humanoid embodiments -- the broadest embodiment coverage in the surveyed literature -- whereas prior retargeting work (DexMachina: 4, ManipTrans: 6) covered fewer and less morphologically diverse targets.
- Demonstrates that physics-based retargeting in MuJoCo preserves manipulation intent across morphologically diverse robots, producing motions that satisfy dynamic feasibility constraints rather than only kinematic correspondence.
- Open-sources the framework ([GitHub](https://github.com/facebookresearch/spider)), enabling community extensions to new embodiments.

**Limitations/Gaps:**
- **Force/impedance awareness:** No. No force sensing or impedance control is incorporated. The retargeting optimizes for kinematic and dynamic feasibility but does not explicitly reason about contact force profiles. Tasks requiring precise force modulation (e.g., insertion, polishing) would need additional force-aware policy layers beyond what SPIDER provides.
- **VLA/language conditioning:** No. The pipeline operates on motion capture demonstrations with no language input or vision-language integration.
- **Sim-to-real:** Yes. Real robot deployment is demonstrated on a Franka Emika Panda + Allegro Hand for four dexterous tasks. Retargeted trajectories from single RGB video are executed directly on physical hardware.
- **Code/weights availability:** Code released ([GitHub](https://github.com/facebookresearch/spider)). Pretrained weights depend on the specific downstream policy.

**Results:** Evaluated across 9 embodiments (5 dexterous hands: Allegro, XHand, Inspire, Ability, Schunk; 4 humanoid robots: Unitree G1, Unitree H1-2, Fourier N1, Booster T1) using multiple datasets.

Table 1 -- Ablation study success rates (full method improves ~18% over annealed sampling alone, range 0.54--1.00).

Table 2 -- Full dataset success rates:

| Dataset | Inspire | Allegro | XHand | Ability | Schunk |
|---------|---------|---------|-------|---------|--------|
| Oakink | 0.479 (best) | 0.413--0.459 range | -- | -- | -- |
| GigaHands | 0.879 (best) | 0.706--0.812 range | -- | -- | -- |

Table 3 -- Comparison with RL baselines:

| Method | Dataset | Success Rate | Speed |
|--------|---------|-------------|-------|
| SPIDER | Oakink (1022 traj.) | 47.9% | 2.5 FPS |
| ManipTrans | Oakink | 39.5% | 0.1 FPS |
| SPIDER | ARCTIC | 42.0% | 1.5 FPS |
| DexMachina | ARCTIC | 67.1% | 0.05 FPS |

SPIDER is 10x faster than RL baselines. Generated 2.4M frames of dynamically feasible robot data. Real robot deployment confirmed on Franka Emika Panda + Allegro Hand for 4 dexterous tasks (rotating light bulb, manipulating spoon, playing guitar, unplugging charger).

## Inference / Deployment

- **Inference latency:** Trajectory generation runs at 2.5 FPS for dexterous manipulation (Oakink dataset) and 19.6--23.1 FPS for humanoid tasks. Not real-time for dexterous manipulation at the 50 Hz control frequency used in physics simulation.
- **Deployment hardware:** RTX 4090 GPUs for ablations/speed tests; H100 GPUs for large-scale dataset generation. Real robot deployment on Franka Emika Panda + Allegro Hand uses direct trajectory execution (no GPU required at execution time).
- **Real-time capable?** No for dexterous manipulation generation (2.5 FPS vs. 50 Hz target). Approaching real-time for humanoid tasks (19.6--23.1 FPS). The system is 10x faster than RL baselines but designed primarily for offline trajectory generation rather than closed-loop real-time control.

## Dataset / Data Collection

- **Dataset used:** Multiple existing human hand-object interaction datasets, including Gigahands, Hot3D, OakInk, and others. SPIDER integrates and processes these public datasets rather than collecting new data. ManipTrans data is also referenced.
- **Collection method:** Human video / motion capture data from the above datasets, processed through the SPIDER retargeting pipeline to produce robot-executable trajectories for 9 humanoid embodiments.
- **Data scale:** Not reported as a single number; depends on the source datasets used. Example data provided via HuggingFace (`retarget/retarget_example`).
- **Teleop equipment:** Not applicable (source data is human video / MoCap, not robot teleoperation).
- **Data format:** Processed through multi-stage pipeline (raw data -> preprocessing -> kinematic trajectories -> retargeted outputs). Example data on HuggingFace.
- **Publicly available?** Yes. Code released ([GitHub](https://github.com/facebookresearch/spider)). Example retargeted datasets available on HuggingFace.

---
