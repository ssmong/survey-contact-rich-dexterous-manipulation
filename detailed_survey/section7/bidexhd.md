### 7.4 BiDexHD

**Full title:** BiDexHD: Bimanual Dexterous Manipulation from Human Demonstrations

**Authors:** Yuanpei Chen, Yaodong Yang, et al. (PKU)

**Venue/Year:** arXiv 2025

**arXiv:** https://arxiv.org/abs/2501.09821

**RL algorithm:** RL (PPO) with human demonstration-guided exploration. Uses retargeted human bimanual demonstrations to initialize and guide RL training on 141 tasks from the TACO benchmark.

**Hand hardware:** 2x Shadow Hands (48 DoF total)

**Sim platform:** IsaacGym

**Sim2Real?** No. Simulation-only.

**Tasks:** 141 bimanual dexterous manipulation tasks from the TACO dataset. Tasks include: bimanual object handover, coordinated assembly, tool use with two hands, container manipulation, and other tasks requiring tight bimanual coordination. This is the largest bimanual dexterous task set reported.

**Key methodology:** BiDexHD addresses the challenge of learning bimanual dexterous policies at scale. Human bimanual demonstrations are retargeted to the dual Shadow Hand setup and used to initialize RL exploration. The demonstration-guided approach significantly reduces the exploration burden for complex bimanual tasks where random exploration rarely discovers useful behaviors. The TACO benchmark provides a standardized evaluation across 141 tasks with varying complexity.

**Main contributions:**
- Scaled bimanual dexterous RL to 141 tasks -- the largest reported bimanual dexterous task set
- Demonstrated that human demonstration-guided RL substantially outperforms pure RL on complex bimanual tasks
- Built on and extended the TACO benchmark for systematic bimanual evaluation

**Limitations/Gaps:** Simulation-only with dual Shadow Hands (48 DoF), which are impractical for most real-world labs. No vision-based policies (uses privileged state). Quality of retargeted demonstrations depends on the human-to-robot morphology mapping. Code not publicly available.

**Sim-only limitation:** Evaluated in simulation only; no sim-to-real transfer demonstrated, real-world viability unvalidated.

**Results:** Achieved successful learning on a large fraction of the 141 TACO tasks (sim), significantly outperforming baselines without demonstration guidance.

## Dataset / Data Collection

- **Dataset used:** TACO benchmark (141 bimanual dexterous tasks). Human bimanual demonstrations retargeted to dual Shadow Hands.
- **Collection method:** RL + human demo-guided exploration (DAPG-style). Human bimanual demonstrations retargeted to dual Shadow Hand setup (48 DoF total) to initialize and guide PPO exploration on 141 tasks. Privileged state observations (no vision).
- **Data scale:** 141 bimanual tasks from TACO dataset. Human demonstrations used for exploration guidance.
- **Teleop equipment:** Not applicable (retargeted human MoCap/video demonstrations, not live robot teleoperation).
- **Data format:** Retargeted demonstration trajectories for dual Shadow Hands.
- **Publicly available?** Code not publicly available. TACO benchmark available separately.

## Inference / Deployment

- **Inference latency:** Not reported. The MLP policy runs in <1ms per forward pass.
- **Deployment hardware:** Simulation only (IsaacGym). No real-robot deployment demonstrated.
- **Real-time capable?** Yes, for the policy itself (MLP inference is trivially fast). However, only simulation evaluation was performed.
