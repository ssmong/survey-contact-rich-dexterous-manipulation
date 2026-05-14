### 7.2 SAPG

**Full title:** SAPG: Split and Merge Policy Gradient for Dexterous Manipulation

**Authors:** Jayesh Singla, Ananye Agarwal, Deepak Pathak

**Venue/Year:** ICML 2024 (Oral presentation)

**RL algorithm:** Split-and-merge policy gradient -- a novel RL algorithm that splits the policy into finger-level sub-policies during exploration (allowing independent per-finger exploration) and merges them during policy update (maintaining a single coordinated policy)

**Hand hardware:** Allegro Hand (16 DoF), Shadow Hand (24 DoF), and higher-DoF configurations (up to 46 DoF with additional arm joints)

**Sim platform:** IsaacGym Preview 4

**Sim2Real?** No (simulation-only)

**Object count:** Evaluated on standard benchmarks (cube rotation, pen spinning, baoding balls, etc.)

**Tasks:** In-hand reorientation, pen spinning, baoding ball manipulation, and other dexterous tasks from standard benchmarks (Adroit, DexHand)

**Key methodology:** Addresses the exploration challenge in high-DoF dexterous manipulation by splitting the policy gradient computation. During rollouts, each finger group explores independently with its own perturbation, enabling coordinated yet diverse exploration in the high-dimensional joint space. During gradient updates, the finger-level explorations are merged into a single policy update. This split-and-merge scheme dramatically improves sample efficiency over standard PPO in high-DoF settings.

**Main contributions:**
- Novel split-and-merge policy gradient algorithm specifically designed for high-DoF manipulation
- Significantly improved sample efficiency and final performance over PPO/SAC on standard dexterous benchmarks
- Scales to very high-DoF systems (46 DoF) where standard RL algorithms fail to learn

**Limitations/Gaps:** Simulation-only; the split structure assumes meaningful finger-level decomposition which may not apply to all manipulation tasks; evaluated primarily on standard benchmarks rather than real-world task diversity; no sim2real validation

**Sim-only limitation:** Evaluated in simulation only; no sim-to-real transfer demonstrated, real-world viability unvalidated.

## Inference / Deployment

- **Inference latency:** Not reported. The merged MLP policy runs in <1ms per forward pass, even for 46-DoF configurations.
- **Deployment hardware:** Simulation only (IsaacGym). No real-robot deployment demonstrated.
- **Real-time capable?** Yes, for the policy itself (MLP inference is trivially fast). However, only simulation evaluation was performed.

## Dataset / Data Collection

- **Dataset used:** No pre-collected dataset. Pure RL with novel split-and-merge policy gradient -- all data generated in simulation.
- **Collection method:** Pure RL in IsaacGym. Split-and-merge exploration: each finger group explores independently during rollouts, merged during gradient updates. Evaluated on standard Adroit/DexHand benchmarks (cube rotation, pen spinning, baoding balls). Up to 46 DoF.
- **Data scale:** Standard parallel RL training in IsaacGym. Standard benchmark objects.
- **Teleop equipment:** Not applicable (pure RL, no demonstrations).
- **Data format:** Not applicable (online RL, no offline dataset).
- **Publicly available?** Code release status not reported.
