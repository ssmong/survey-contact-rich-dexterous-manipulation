### DexMachina

**Full Title:** DexMachina: Learning Dexterous Manipulation from Human Video via Retargeting and Reinforcement Learning

**Authors:** Mandi Zhao et al. (Stanford / NVIDIA)

**Venue/Year:** arXiv preprint, 2025

**Hand Hardware:** Six robot hands evaluated -- Inspire Hand, Allegro Hand (16 DoF), XHand, Schunk Hand, Ability Hand, and DexRobot Hand. This cross-embodiment evaluation is a distinguishing feature of the work.

**Tasks:** Bimanual articulated object manipulation tasks, including manipulating objects with complex kinematic structures (e.g., opening containers, operating mechanisms). The tasks require coordinated finger motions across multiple contact points.

**Key Methodology:** DexMachina learns dexterous manipulation skills from human video demonstrations. The pipeline consists of three stages: (1) extracting hand-object interaction trajectories from human videos, (2) retargeting these motions to diverse robot hand morphologies, and (3) refining the retargeted motions using reinforcement learning in simulation to produce physically feasible and robust policies. The Genesis simulator is used for physics-based training, enabling fast parallel environment rollouts.

**Architecture/Parameters:** The system uses hand motion retargeting networks to map human MANO hand representations to various robot hand joint configurations, followed by RL policy networks (PPO-based) for refinement. Model weights are not yet publicly released (evaluation marked as TODO).

**Sim Platform:** Genesis simulator. Sim-to-real transfer is not demonstrated -- the work is currently simulation-only, with the focus on the retargeting and learning pipeline across diverse hand embodiments.

**Main Contributions:**
- Proposes a video-to-policy pipeline that eliminates the need for robot-specific demonstration collection: human video alone is sufficient to produce policies for multiple robot hands, whereas prior retargeting work required kinematic correspondence tuning per embodiment.
- Demonstrates cross-embodiment dexterous manipulation across 6 morphologically distinct robot hands (Inspire, Allegro, XHand, Schunk, Ability, DexRobot) from the same human video source, showing that the retargeting generalizes across DoF counts and finger configurations.
- Introduces an RL refinement stage that closes the gap between kinematic retargeting and physically feasible execution, improving over direct retargeting baselines that produce kinematically valid but dynamically infeasible motions.

**Limitations/Gaps:**
- **Force/impedance awareness:** No. No force/torque sensing or impedance control is used. Contact forces during manipulation are determined by the simulation contact model and position-tracking behavior, not explicitly regulated. This may limit transfer to tasks requiring precise force modulation (e.g., fragile object manipulation).
- **VLA/language conditioning:** No. The pipeline is vision-based (human video input) but does not use language conditioning or VLA architectures.
- **Sim-to-real:** No. The work is simulation-only. Real-world deployment would require addressing the additional sim-to-real gap beyond the human-to-robot retargeting gap already addressed.
- **Code/weights availability:** Model weights and evaluation benchmarks are listed as TODO. Availability is pending.

**Results:** Evaluated on 7 demonstrations from the ARCTIC dataset involving 5 articulated objects, split into short-horizon (3 clips) and long-horizon (4 clips, including complex sequences like mid-air manipulation, lid opening/closing, flipping).

| Metric / Finding | Value | Context |
|-------------------|-------|---------|
| Hands evaluated | 6 | Inspire, Allegro, XHand, Schunk, Ability, DexRobot |
| ARCTIC demonstrations | 7 | 3 short-horizon + 4 long-horizon clips |
| Performance vs. baselines | Consistent improvement | DexMachina improves on all hands and tasks over direct retargeting |
| Long-horizon gains | Strongest | Particularly large improvements on long-horizon demos |
| Hand morphology effect | Larger hands perform better | Fully-actuated hands achieve higher final performance and better learning efficiency |
| Allegro Hand | Strong despite less anthropomorphic | Notable performance despite morphological differences from human hand |
| Inspire Hand | Requires strategy deviation | Less-actuated hands needed more deviation from human-guided strategies |

Note: Precise per-hand success rate numbers are reported in Figure 3 of the paper as bar charts rather than tabulated values.

## Inference / Deployment

- **Inference latency:** Not reported. The work is simulation-only with no real-world deployment.
- **Deployment hardware:** Simulation only (Genesis physics engine with PPO training using 12,000 parallel environments). No physical deployment hardware. The authors note "our learned RL policies have not yet been evaluated in real-world settings on the examined range of dexterous hands due to lack of hardware access."
- **Real-time capable?** Not applicable (simulation-only).

## Dataset / Data Collection

- **Dataset used:** Human video demonstrations of hand-object interactions (no named benchmark dataset). The pipeline ingests in-the-wild human videos as the data source.
- **Collection method:** Human video capture (passive recording of human hand manipulation). Hand-object interaction trajectories are extracted from video, retargeted to robot hand morphologies, and refined via RL in simulation. No robot teleoperation is required.
- **Data scale:** Not reported. The number of human video demonstrations used is not specified in public materials.
- **Teleop equipment:** Not applicable (human video input, not teleoperation).
- **Data format:** Not reported.
- **Publicly available?** Model weights and evaluation benchmarks listed as TODO; availability is pending.

> *Results verified from arXiv:2505.24853. Hand count updated from 4 to 6 (adding Ability Hand and DexRobot Hand). Evaluation uses ARCTIC dataset.*

---
