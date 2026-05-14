### 7.2 DexPBT

**Full title:** DexPBT: Scaling up Dexterous Manipulation for Hand-Arm Systems with Population Based Training

**Authors:** Aleksei Petrenko, Arthur Allshire, Gavriel State, Ankur Handa, Viktor Makoviychuk

**Venue/Year:** RSS 2023

**RL algorithm:** PPO with Population-Based Training (PBT); maintains a population of policies with different hyperparameters, periodically replacing underperformers with mutated copies of top performers

**Hand hardware:** Allegro Hand (16 DoF) + Kuka arm

**Sim platform:** IsaacGym

**Sim2Real?** No (simulation-only evaluation)

**Object count:** Multiple objects; evaluated on cube reorientation and other manipulation tasks

**Tasks:** Coordinated arm-hand manipulation including in-hand reorientation, regrasping, and object handover; multi-task training across diverse manipulation objectives

**Key methodology:** Applies Population-Based Training to dexterous arm-hand manipulation, automatically tuning reward weights, learning rates, and domain randomization parameters across a population of policies. PBT enables efficient hyperparameter search in the challenging high-dimensional action space of arm-hand systems (16 + 7 = 23 DoF). The population evolves toward policies that balance multiple task objectives without manual reward shaping.

**Main contributions:**
- First application of PBT to dexterous arm-hand manipulation, automating hyperparameter and reward tuning
- Multi-task training framework handling diverse manipulation objectives with a single population
- Demonstrated that PBT significantly outperforms fixed-hyperparameter PPO on arm-hand tasks

**Limitations/Gaps:** Simulation-only (no sim2real); PBT requires significant compute (population of parallel policies); limited object diversity; the evolved hyperparameters may not transfer across tasks or embodiments

**Sim-only limitation:** Evaluated in simulation only; no sim-to-real transfer demonstrated, real-world viability unvalidated.

## Inference / Deployment

- **Inference latency:** Not reported. The MLP policy runs in <1ms per forward pass.
- **Deployment hardware:** Simulation only (IsaacGym). No real-robot deployment demonstrated.
- **Real-time capable?** Yes, for the policy itself (MLP inference is trivially fast). However, only simulation evaluation was performed.

## Dataset / Data Collection

- **Dataset used:** No pre-collected dataset. Pure RL (PPO) with Population-Based Training (PBT) -- all data generated in simulation.
- **Collection method:** Pure RL in IsaacGym. PBT maintains a population of policies with different hyperparameters, automatically tuning reward weights, learning rates, and domain randomization. Multi-task training across diverse arm-hand manipulation objectives.
- **Data scale:** Standard parallel RL training in IsaacGym. Multiple objects for cube reorientation and other tasks.
- **Teleop equipment:** Not applicable (pure RL, no demonstrations).
- **Data format:** Not applicable (online RL, no offline dataset).
- **Publicly available?** Code release status not reported.
