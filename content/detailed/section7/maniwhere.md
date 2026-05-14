### 7.4 Maniwhere

**Full title:** Maniwhere: Learning to Manipulate Anywhere with RL and Visual Generalization

**Authors:** Zhecheng Yuan, et al. (Shanghai AI Lab / Tsinghua)

**Venue/Year:** CoRL 2024

**arXiv:** https://arxiv.org/abs/2407.15815

**RL algorithm:** PPO with visual representation learning. Teacher-student framework where the teacher uses privileged state and the student uses visual observations. Visual domain randomization and data augmentation for generalization across environments.

**Hand hardware:** Allegro Hand (16 DoF) mounted on a robot arm

**Sim platform:** IsaacGym

**Sim2Real?** Yes. Sim-to-real transfer demonstrated with visual generalization to novel environments (real).

**Tasks:** 8 dexterous manipulation tasks including in-hand reorientation, object pick-and-place, and functional manipulation. The key evaluation dimension is visual generalization: policies must work across different backgrounds, lighting conditions, and distractor objects.

**Key methodology:** Maniwhere addresses a critical gap in dexterous RL: policies that work in sim or in a specific real-world setup but fail when the visual environment changes. The approach combines RL training with aggressive visual domain randomization and learns visual representations that are invariant to background, lighting, and distractor changes. A teacher-student framework separates the manipulation skill (learned with privileged state) from the visual perception (learned via distillation with visual observations).

**Main contributions:**
- Demonstrated visually generalizable dexterous manipulation -- policies that transfer across different visual environments, not just sim-to-real (real)
- Showed that visual domain randomization combined with representation learning enables robust dexterous policies for diverse settings
- Evaluated on 8 tasks spanning grasping, reorientation, and functional manipulation with the Allegro Hand (real)

**Limitations/Gaps:** Visual generalization is evaluated on background/lighting changes, not on object shape generalization. Allegro Hand is the only platform tested. 8 tasks is a moderate evaluation scale.

**Results:** Achieved successful sim-to-real transfer with visual generalization across novel environments on 8 tasks (real). Code publicly available.

## Dataset / Data Collection

- **Dataset used:** No pre-collected dataset. Pure RL (PPO) with visual domain randomization -- all data generated in simulation.
- **Collection method:** Pure RL in IsaacGym. Teacher-student framework: teacher trained with privileged state, student uses visual observations. Aggressive visual domain randomization (backgrounds, lighting, distractors) for visual generalization. Sim-to-real transfer on Allegro Hand + robot arm.
- **Data scale:** Standard parallel RL training in IsaacGym. 8 dexterous manipulation tasks for evaluation.
- **Teleop equipment:** Not applicable (pure RL, no demonstrations).
- **Data format:** Not applicable (online RL, no offline dataset).
- **Publicly available?** Code publicly available.

## Inference / Deployment

- **Inference latency:** Not explicitly reported. The visual student policy (CNN encoder + MLP) runs in <5ms per forward pass.
- **Deployment hardware:** Allegro Hand (16 DoF) mounted on a robot arm. Policy trained in IsaacGym; deployed via sim-to-real transfer with visual generalization to novel environments.
- **Real-time capable?** Yes. Demonstrated real-time dexterous manipulation on real Allegro Hand across varied environments.
