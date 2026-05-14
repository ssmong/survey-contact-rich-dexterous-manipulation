### 7.4 DQ-RISE

**전체 제목:** DQ-RISE: Dexterous Quasi-Static Robotic In-Hand Skill Execution via Sim-to-Real Reinforcement Learning

**저자:** Chengzhong Ma, Wenzhao Lian, Changhao Wang, et al.

**학회/연도:** ICRA 2026

**arXiv:** https://arxiv.org/abs/2503.01766

**RL 알고리즘:** PPO-based sim-to-real RL with teacher-student distillation. Teacher uses privileged state; student uses proprioception and tactile/force input. Domain randomization for sim-to-real transfer.

**핸드 하드웨어:** OyMotion RoHand (dexterous hand) + Flexiv Rizon 4 arm

**시뮬레이션 플랫폼:** IsaacGym (inferred from Flexiv/dexterous RL pipeline norms)

**Sim2Real 여부:** Yes. Zero-shot sim-to-real transfer demonstrated on 6 real-world tasks with 85.83% average success rate (real).

**작업:** 6 real-world dexterous manipulation tasks involving quasi-static in-hand manipulation: object reorientation, precision placement, tool re-grasping, and functional manipulation. Tasks require careful force regulation and stable multi-finger coordination.

**핵심 방법론:** DQ-RISE focuses on quasi-static dexterous manipulation -- tasks where objects move slowly and forces must be carefully controlled to maintain stable grasps during manipulation. The approach uses teacher-student RL: a teacher policy trained with privileged simulation state (object pose, contact forces) is distilled into a student that relies on proprioception and available sensing. Domain randomization over dynamics parameters (friction, mass, motor gains) enables zero-shot sim-to-real transfer.

**주요 기여:**
- Demonstrated sim-to-real dexterous in-hand manipulation with the OyMotion RoHand, expanding the set of validated dexterous hand platforms
- Achieved 85.83% average success rate across 6 real tasks via zero-shot transfer (real)
- Focused on quasi-static manipulation, which is practically important for precise assembly and tool-use tasks

**정량적 결과:**

| Metric | Value |
|---|---|
| Average real-world success rate | 85.83% (real) |
| Number of real tasks | 6 |
| Hand | OyMotion RoHand + Flexiv Rizon 4 |

**한계점:** Quasi-static assumption limits applicability to dynamic tasks. 85.83% success rate leaves room for improvement. Limited object diversity in real-world evaluation.

**결과:** 85.83% average success rate on 6 real-world tasks (real). Code publicly available.

## 추론 / 배포

- **추론 지연 시간:** Not explicitly reported. The distilled student MLP policy runs in <1ms per forward pass, enabling high-frequency control.
- **배포 하드웨어:** OyMotion RoHand (dexterous hand) + Flexiv Rizon 4 arm. Policy trained in IsaacGym; deployed via zero-shot sim-to-real transfer.
- **실시간 가능 여부:** Yes. MLP-based policy supports real-time control. Demonstrated on real hardware with 85.83% success across 6 tasks.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** No pre-collected dataset. Pure RL (PPO) with teacher-student distillation -- all data generated in simulation.
- **수집 방법:** Pure RL in IsaacGym (inferred). Teacher trained with privileged state (object pose, contact forces); student uses proprioception and tactile/force input. Domain randomization for sim-to-real (friction, mass, motor gains). Zero-shot transfer to OyMotion RoHand + Flexiv Rizon 4 system.
- **데이터 규모:** Standard parallel RL training. 6 real-world quasi-static dexterous manipulation tasks for evaluation.
- **원격 조작 장비:** Not applicable (pure RL, no demonstrations).
- **데이터 포맷:** Not applicable (online RL, no offline dataset).
- **공개 여부:** Code publicly available.
