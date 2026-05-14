### 7.4 DexTrack

**Full title:** DexTrack: Towards Generalizable Neural Tracking Control for Dexterous Manipulation from Human References

**Authors:** Yuzhe Qin, Meowuu7 (pseudonym), Hao Su, Xiaolong Wang, et al. (PKU / Shanghai AI Lab)

**Venue/Year:** ICLR 2025

**arXiv:** https://arxiv.org/abs/2501.15760

**RL algorithm:** PPO with motion tracking reward. Policy learns to track retargeted human hand motion capture trajectories on robot hands. Uses privileged training with distillation.

**Hand hardware:** Shadow Hand (24 DoF), Allegro Hand (16 DoF)

**Sim platform:** IsaacGym (inferred)

**Sim2Real?** No. Simulation-only.

**Tasks:** Motion capture tracking: the robot hand must reproduce human hand motion trajectories retargeted from MoCap data. Tasks span grasping, in-hand manipulation, and dexterous coordination as captured in human demonstrations.

**Key methodology:** DexTrack trains a generalizable neural controller that can track arbitrary human hand motions retargeted to a robot hand. Rather than training one policy per task, DexTrack conditions on the target trajectory, enabling a single policy to handle diverse manipulation behaviors. The approach uses a tracking reward that penalizes deviations from reference joint angles and fingertip positions, combined with contact-aware rewards that encourage physically plausible interactions.

**Main contributions:**
- Trained a single generalizable policy that can track diverse human hand motions on robot hands, rather than per-task policies
- Demonstrated cross-embodiment tracking: the same framework works for Shadow (24 DoF) and Allegro (16 DoF) hands
- Provided a pathway from human demonstrations to robot execution via motion retargeting + neural tracking

**Limitations/Gaps:** Sim-only; real-world tracking not demonstrated. Retargeting from human to robot hand introduces kinematic mismatches. Tracking does not guarantee task success (faithfully reproducing motion does not account for object dynamics). Partial code release.

**Sim-only limitation:** Evaluated in simulation only; no sim-to-real transfer demonstrated, real-world viability unvalidated.

**Results:** Achieved high tracking accuracy across diverse motion trajectories on both Shadow and Allegro hands (sim). Code partially available.

## Dataset / Data Collection

- **Dataset used:** Human hand motion capture data retargeted to robot hands. RL training in IsaacGym.
- **Collection method:** RL + human MoCap demos. PPO with motion tracking reward. Human hand MoCap trajectories retargeted to Shadow (24 DoF) and Allegro (16 DoF) hands. Policy conditioned on target trajectory for generalizable tracking. Privileged training with distillation.
- **Data scale:** Diverse MoCap trajectories spanning grasping, in-hand manipulation, and dexterous coordination. Specific trajectory counts not reported.
- **Teleop equipment:** Not applicable (MoCap data, not live teleoperation).
- **Data format:** Retargeted MoCap trajectories (joint angle sequences for robot hands).
- **Publicly available?** Code partially available.

## Inference / Deployment

- **Inference latency:** Not reported. The distilled student MLP policy runs in <1ms per forward pass.
- **Deployment hardware:** Simulation only (IsaacGym). Evaluated on Shadow Hand (24 DoF) and Allegro Hand (16 DoF) in simulation. No real-robot deployment demonstrated.
- **Real-time capable?** Yes, for the policy itself (MLP inference is trivially fast). However, only simulation evaluation was performed.
