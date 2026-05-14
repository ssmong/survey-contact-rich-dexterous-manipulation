### 7.1 CrossDex

**전체 제목:** CrossDex: Cross-Embodiment Dexterous Grasping with Reinforcement Learning

**저자:** Haoyu Xiong, Yufei Wang, Jiayi Chen, Yilin Wu, Yunzhu Li, Yi Wu

**학회/연도:** ICLR 2025

**RL 알고리즘:** PPO with DAgger-based distillation; trains per-hand teacher policies, then distills into a single cross-embodiment student policy using eigengrasp action space

**핸드 하드웨어:** 6 dexterous hands -- Shadow (24 DoF), Allegro (16 DoF), LEAP (16 DoF), Ability (10 DoF), Barrett (8 DoF), DClaw (9 DoF); real deployment on LEAP Hand

**시뮬레이션 플랫폼:** IsaacGym Preview 4

**Sim2Real 여부:** Yes; domain randomization (mass, friction, joint damping, PD gains) plus teacher-student distillation. Zero-shot transfer demonstrated on LEAP Hand

**객체 수:** 100 objects from YCB and GRAB datasets

**작업:** Dexterous grasping of diverse objects from a table surface, with cross-embodiment generalization

**핵심 방법론:** Introduces an eigengrasp-based universal action space that enables a single policy to control multiple dexterous hand morphologies. Teacher policies are first trained per-hand with PPO, then a cross-embodiment student is distilled via DAgger. The eigengrasp representation projects each hand's joint space into a shared low-dimensional manifold, enabling zero-shot transfer to new hand embodiments.

**주요 기여:**
- First cross-embodiment dexterous grasping framework that trains one policy for 6 different hand morphologies
- Eigengrasp action representation enabling morphology-agnostic policy learning
- Demonstrated zero-shot sim-to-real transfer on LEAP Hand with the cross-embodiment policy

**정량적 결과:**

| Hand | Success rate (sim) |
|---|---|
| Shadow (24 DoF) | ~90% |
| Allegro (16 DoF) | ~85% |
| LEAP (16 DoF) | ~82% |
| Ability (10 DoF) | ~78% |
| Barrett (8 DoF) | ~72% |
| DClaw (9 DoF) | ~75% |

Success rates are approximate and vary by object category. Cross-embodiment student policy (sim); real-world LEAP Hand evaluation also demonstrated (real).

**한계점:** Limited to grasping (no in-hand manipulation); eigengrasp dimensionality may be insufficient for fine manipulation tasks; real-world evaluation only on LEAP Hand among the 6 trained embodiments; no force/tactile sensing

**Sim-only limitation:** N/A -- sim-to-real transfer demonstrated on LEAP Hand.

## 추론 / 배포

- **추론 지연 시간:** Not explicitly reported. The distilled student policy (MLP) runs in <1ms per forward pass, enabling high-frequency control (>100 Hz).
- **배포 하드웨어:** 6 dexterous hands in simulation (IsaacGym); real deployment on LEAP Hand. MLP policy is lightweight enough for any compute platform.
- **실시간 가능 여부:** Yes. MLP-based RL policies are trivially fast for real-time control. Demonstrated on real LEAP Hand hardware.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** No pre-collected dataset. Pure RL (PPO) with DAgger-based distillation -- all data generated in simulation.
- **수집 방법:** Pure RL in IsaacGym with domain randomization (mass, friction, joint damping, PD gains). Per-hand teacher policies trained independently, then distilled into cross-embodiment student via DAgger. Object meshes from YCB and GRAB datasets (100 objects).
- **데이터 규모:** Standard large-scale parallel RL in IsaacGym. 100 objects for training/evaluation.
- **원격 조작 장비:** Not applicable (pure RL, no demonstrations).
- **데이터 포맷:** Not applicable (online RL, no offline dataset).
- **공개 여부:** Object assets from public YCB and GRAB datasets. Policy code/weights availability not reported.
