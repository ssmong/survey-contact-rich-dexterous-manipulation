### 7.1 ResDex

**Full title:** ResDex: Residual Policy Learning for Dexterous Grasping with Large-Scale Object Training

**Authors:** Haoyu Xiong, Yufei Wang, Jiayi Chen, Yi Wu

**Venue/Year:** ICLR 2025

**RL algorithm:** PPO with Mixture-of-Experts (MoE) architecture and DAgger distillation; uses a residual policy on top of a base policy to handle diverse objects

**Hand hardware:** Shadow Hand (24 DoF)

**Sim platform:** IsaacGym Preview 4

**Sim2Real?** No

**Object count:** 3200 objects; 88.8% overall success rate (sim)

**Tasks:** Dexterous grasping of diverse objects at unprecedented scale (3200 objects)

**Key methodology:** Scales dexterous grasping to thousands of objects by decomposing the policy into a base grasping policy and a residual correction module using a Mixture-of-Experts architecture. The MoE enables specialization across object categories while sharing a common grasping backbone. DAgger distillation compresses the ensemble into a single deployable policy.

**Main contributions:**
- Scaled dexterous grasping training to 3200 diverse objects, the largest object set at time of publication
- Residual policy with MoE architecture for handling object diversity without catastrophic forgetting
- Achieved 88.8% success rate (sim) across the full 3200-object set with a single policy

**Quantitative results:**

| Metric | Value |
|---|---|
| Overall success rate | 88.8% (sim) |
| Object set size | 3200 |
| Hand | Shadow (24 DoF) |

**Limitations/Gaps:** Simulation-only (no sim2real transfer demonstrated); uses a single hand embodiment (Shadow); relies on ground-truth object state in simulation; no evaluation of grasp stability under perturbation

**Sim-only limitation:** Evaluated in simulation only; no sim-to-real transfer demonstrated, real-world viability unvalidated.

## Inference / Deployment

- **Inference latency:** Not reported. The distilled policy (MLP) runs in <1ms per forward pass.
- **Deployment hardware:** Simulation only (IsaacGym). No real-robot deployment demonstrated.
- **Real-time capable?** Yes, for the policy itself (MLP inference is trivially fast). However, only simulation evaluation was performed.

## Dataset / Data Collection

- **Dataset used:** No pre-collected dataset. Pure RL (PPO) with MoE architecture -- all data generated in simulation.
- **Collection method:** Pure RL in IsaacGym. Residual policy with Mixture-of-Experts trained on 3,200 objects. DAgger distillation compresses the MoE ensemble into a single policy. Uses ground-truth object state in simulation.
- **Data scale:** 3,200 objects for training. Standard parallel RL training scale.
- **Teleop equipment:** Not applicable (pure RL, no demonstrations).
- **Data format:** Not applicable (online RL, no offline dataset).
- **Publicly available?** Dataset/policy release status not reported.
