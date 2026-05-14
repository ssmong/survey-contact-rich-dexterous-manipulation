### 7.4 Maniwhere

**전체 제목:** Maniwhere: Learning to Manipulate Anywhere with RL and Visual Generalization

**저자:** Zhecheng Yuan, et al. (Shanghai AI Lab / Tsinghua)

**학회/연도:** CoRL 2024

**arXiv:** https://arxiv.org/abs/2407.15815

**RL 알고리즘:** PPO with visual representation learning. Teacher-student framework where the teacher uses privileged state and the student uses visual observations. Visual domain randomization and data augmentation for generalization across environments.

**핸드 하드웨어:** Allegro Hand (16 DoF) mounted on a robot arm

**시뮬레이션 플랫폼:** IsaacGym

**Sim2Real 여부:** Yes. Sim-to-real transfer demonstrated with visual generalization to novel environments (real).

**작업:** 8 dexterous manipulation tasks including in-hand reorientation, object pick-and-place, and functional manipulation. The key evaluation dimension is visual generalization: policies must work across different backgrounds, lighting conditions, and distractor objects.

**핵심 방법론:** Maniwhere addresses a critical gap in dexterous RL: policies that work in sim or in a specific real-world setup but fail when the visual environment changes. The approach combines RL training with aggressive visual domain randomization and learns visual representations that are invariant to background, lighting, and distractor changes. A teacher-student framework separates the manipulation skill (learned with privileged state) from the visual perception (learned via distillation with visual observations).

**주요 기여:**
- Demonstrated visually generalizable dexterous manipulation -- policies that transfer across different visual environments, not just sim-to-real (real)
- Showed that visual domain randomization combined with representation learning enables robust dexterous policies for diverse settings
- Evaluated on 8 tasks spanning grasping, reorientation, and functional manipulation with the Allegro Hand (real)

**한계점:** Visual generalization is evaluated on background/lighting changes, not on object shape generalization. Allegro Hand is the only platform tested. 8 tasks is a moderate evaluation scale.

**결과:** Achieved successful sim-to-real transfer with visual generalization across novel environments on 8 tasks (real). Code publicly available.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** No pre-collected dataset. Pure RL (PPO) with visual domain randomization -- all data generated in simulation.
- **수집 방법:** Pure RL in IsaacGym. Teacher-student framework: teacher trained with privileged state, student uses visual observations. Aggressive visual domain randomization (backgrounds, lighting, distractors) for visual generalization. Sim-to-real transfer on Allegro Hand + robot arm.
- **데이터 규모:** Standard parallel RL training in IsaacGym. 8 dexterous manipulation tasks for evaluation.
- **원격 조작 장비:** Not applicable (pure RL, no demonstrations).
- **데이터 포맷:** Not applicable (online RL, no offline dataset).
- **공개 여부:** Code publicly available.

## 추론 / 배포

- **추론 지연 시간:** Not explicitly reported. The visual student policy (CNN encoder + MLP) runs in <5ms per forward pass.
- **배포 하드웨어:** Allegro Hand (16 DoF) mounted on a robot arm. Policy trained in IsaacGym; deployed via sim-to-real transfer with visual generalization to novel environments.
- **실시간 가능 여부:** Yes. Demonstrated real-time dexterous manipulation on real Allegro Hand across varied environments.
