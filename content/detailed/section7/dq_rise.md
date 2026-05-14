### 7.4 DQ-RISE

**Full title:** DQ-RISE: Dexterous Quasi-Static Robotic In-Hand Skill Execution via Sim-to-Real Reinforcement Learning

**Authors:** Chengzhong Ma, Wenzhao Lian, Changhao Wang, et al.

**Venue/Year:** ICRA 2026

**arXiv:** https://arxiv.org/abs/2503.01766

**RL algorithm:** PPO-based sim-to-real RL with teacher-student distillation. Teacher uses privileged state; student uses proprioception and tactile/force input. Domain randomization for sim-to-real transfer.

**Hand hardware:** OyMotion RoHand (dexterous hand) + Flexiv Rizon 4 arm

**Sim platform:** IsaacGym (inferred from Flexiv/dexterous RL pipeline norms)

**Sim2Real?** Yes. Zero-shot sim-to-real transfer demonstrated on 6 real-world tasks with 85.83% average success rate (real).

**Tasks:** 6 real-world dexterous manipulation tasks involving quasi-static in-hand manipulation: object reorientation, precision placement, tool re-grasping, and functional manipulation. Tasks require careful force regulation and stable multi-finger coordination.

**Key methodology:** DQ-RISE focuses on quasi-static dexterous manipulation -- tasks where objects move slowly and forces must be carefully controlled to maintain stable grasps during manipulation. The approach uses teacher-student RL: a teacher policy trained with privileged simulation state (object pose, contact forces) is distilled into a student that relies on proprioception and available sensing. Domain randomization over dynamics parameters (friction, mass, motor gains) enables zero-shot sim-to-real transfer.

**Main contributions:**
- Demonstrated sim-to-real dexterous in-hand manipulation with the OyMotion RoHand, expanding the set of validated dexterous hand platforms
- Achieved 85.83% average success rate across 6 real tasks via zero-shot transfer (real)
- Focused on quasi-static manipulation, which is practically important for precise assembly and tool-use tasks

**Quantitative results:**

| Metric | Value |
|---|---|
| Average real-world success rate | 85.83% (real) |
| Number of real tasks | 6 |
| Hand | OyMotion RoHand + Flexiv Rizon 4 |

**Limitations/Gaps:** Quasi-static assumption limits applicability to dynamic tasks. 85.83% success rate leaves room for improvement. Limited object diversity in real-world evaluation.

**Results:** 85.83% average success rate on 6 real-world tasks (real). Code publicly available.

## Inference / Deployment

- **Inference latency:** Not explicitly reported. The distilled student MLP policy runs in <1ms per forward pass, enabling high-frequency control.
- **Deployment hardware:** OyMotion RoHand (dexterous hand) + Flexiv Rizon 4 arm. Policy trained in IsaacGym; deployed via zero-shot sim-to-real transfer.
- **Real-time capable?** Yes. MLP-based policy supports real-time control. Demonstrated on real hardware with 85.83% success across 6 tasks.

## Dataset / Data Collection

- **Dataset used:** No pre-collected dataset. Pure RL (PPO) with teacher-student distillation -- all data generated in simulation.
- **Collection method:** Pure RL in IsaacGym (inferred). Teacher trained with privileged state (object pose, contact forces); student uses proprioception and tactile/force input. Domain randomization for sim-to-real (friction, mass, motor gains). Zero-shot transfer to OyMotion RoHand + Flexiv Rizon 4 system.
- **Data scale:** Standard parallel RL training. 6 real-world quasi-static dexterous manipulation tasks for evaluation.
- **Teleop equipment:** Not applicable (pure RL, no demonstrations).
- **Data format:** Not applicable (online RL, no offline dataset).
- **Publicly available?** Code publicly available.
