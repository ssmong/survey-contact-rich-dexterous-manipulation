### 7.2 SAPG

**전체 제목:** SAPG: Split and Merge Policy Gradient for Dexterous Manipulation

**저자:** Jayesh Singla, Ananye Agarwal, Deepak Pathak

**학회/연도:** ICML 2024 (Oral presentation)

**RL 알고리즘:** Split-and-merge policy gradient -- a novel RL algorithm that splits the policy into finger-level sub-policies during exploration (allowing independent per-finger exploration) and merges them during policy update (maintaining a single coordinated policy)

**핸드 하드웨어:** Allegro Hand (16 DoF), Shadow Hand (24 DoF), and higher-DoF configurations (up to 46 DoF with additional arm joints)

**시뮬레이션 플랫폼:** IsaacGym Preview 4

**Sim2Real 여부:** No (simulation-only)

**객체 수:** Evaluated on standard benchmarks (cube rotation, pen spinning, baoding balls, etc.)

**작업:** In-hand reorientation, pen spinning, baoding ball manipulation, and other dexterous tasks from standard benchmarks (Adroit, DexHand)

**핵심 방법론:** Addresses the exploration challenge in high-DoF dexterous manipulation by splitting the policy gradient computation. During rollouts, each finger group explores independently with its own perturbation, enabling coordinated yet diverse exploration in the high-dimensional joint space. During gradient updates, the finger-level explorations are merged into a single policy update. This split-and-merge scheme dramatically improves sample efficiency over standard PPO in high-DoF settings.

**주요 기여:**
- Novel split-and-merge policy gradient algorithm specifically designed for high-DoF manipulation
- Significantly improved sample efficiency and final performance over PPO/SAC on standard dexterous benchmarks
- Scales to very high-DoF systems (46 DoF) where standard RL algorithms fail to learn

**한계점:** Simulation-only; the split structure assumes meaningful finger-level decomposition which may not apply to all manipulation tasks; evaluated primarily on standard benchmarks rather than real-world task diversity; no sim2real validation

**시뮬레이션 전용 한계:** 시뮬레이션에서만 평가됨; sim-to-real 전이 미입증, 실제 환경 실행 가능성 미검증.

## 추론 / 배포

- **추론 지연 시간:** Not reported. The merged MLP policy runs in <1ms per forward pass, even for 46-DoF configurations.
- **배포 하드웨어:** Simulation only (IsaacGym). No real-robot deployment demonstrated.
- **실시간 가능 여부:** Yes, for the policy itself (MLP inference is trivially fast). However, only simulation evaluation was performed.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** No pre-collected dataset. Pure RL with novel split-and-merge policy gradient -- all data generated in simulation.
- **수집 방법:** Pure RL in IsaacGym. Split-and-merge exploration: each finger group explores independently during rollouts, merged during gradient updates. Evaluated on standard Adroit/DexHand benchmarks (cube rotation, pen spinning, baoding balls). Up to 46 DoF.
- **데이터 규모:** Standard parallel RL training in IsaacGym. Standard benchmark objects.
- **원격 조작 장비:** Not applicable (pure RL, no demonstrations).
- **데이터 포맷:** Not applicable (online RL, no offline dataset).
- **공개 여부:** Code release status not reported.
