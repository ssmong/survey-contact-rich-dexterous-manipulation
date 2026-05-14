### 7.1 ResDex

**전체 제목:** ResDex: Residual Policy Learning for Dexterous Grasping with Large-Scale Object Training

**저자:** Haoyu Xiong, Yufei Wang, Jiayi Chen, Yi Wu

**학회/연도:** ICLR 2025

**RL 알고리즘:** PPO with Mixture-of-Experts (MoE) architecture and DAgger distillation; uses a residual policy on top of a base policy to handle diverse objects

**핸드 하드웨어:** Shadow Hand (24 DoF)

**시뮬레이션 플랫폼:** IsaacGym Preview 4

**Sim2Real 여부:** No

**객체 수:** 3200 objects; 88.8% overall success rate (sim)

**작업:** Dexterous grasping of diverse objects at unprecedented scale (3200 objects)

**핵심 방법론:** Scales dexterous grasping to thousands of objects by decomposing the policy into a base grasping policy and a residual correction module using a Mixture-of-Experts architecture. The MoE enables specialization across object categories while sharing a common grasping backbone. DAgger distillation compresses the ensemble into a single deployable policy.

**주요 기여:**
- Scaled dexterous grasping training to 3200 diverse objects, the largest object set at time of publication
- Residual policy with MoE architecture for handling object diversity without catastrophic forgetting
- Achieved 88.8% success rate (sim) across the full 3200-object set with a single policy

**정량적 결과:**

| Metric | Value |
|---|---|
| Overall success rate | 88.8% (sim) |
| Object set size | 3200 |
| Hand | Shadow (24 DoF) |

**한계점:** Simulation-only (no sim2real transfer demonstrated); uses a single hand embodiment (Shadow); relies on ground-truth object state in simulation; no evaluation of grasp stability under perturbation

**시뮬레이션 전용 한계:** 시뮬레이션에서만 평가됨; sim-to-real 전이 미입증, 실제 환경 실행 가능성 미검증.

## 추론 / 배포

- **추론 지연 시간:** Not reported. The distilled policy (MLP) runs in <1ms per forward pass.
- **배포 하드웨어:** Simulation only (IsaacGym). No real-robot deployment demonstrated.
- **실시간 가능 여부:** Yes, for the policy itself (MLP inference is trivially fast). However, only simulation evaluation was performed.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** No pre-collected dataset. Pure RL (PPO) with MoE architecture -- all data generated in simulation.
- **수집 방법:** Pure RL in IsaacGym. Residual policy with Mixture-of-Experts trained on 3,200 objects. DAgger distillation compresses the MoE ensemble into a single policy. Uses ground-truth object state in simulation.
- **데이터 규모:** 3,200 objects for training. Standard parallel RL training scale.
- **원격 조작 장비:** Not applicable (pure RL, no demonstrations).
- **데이터 포맷:** Not applicable (online RL, no offline dataset).
- **공개 여부:** Dataset/policy release status not reported.
