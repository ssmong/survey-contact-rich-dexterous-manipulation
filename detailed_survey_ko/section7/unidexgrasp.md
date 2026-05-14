### 7.1 UniDexGrasp

**전체 제목:** UniDexGrasp: Universal Robotic Dexterous Grasping via Learning Diverse Proposal Generation and Goal-Conditioned Policy

**저자:** Yinzhen Xu, Weikang Wan, Jialiang Zhang, Haoran Liu, Zikang Yan, Hao Shen, Ruicheng Wang, He Wang

**학회/연도:** CVPR 2023

**RL 알고리즘:** PPO (goal-conditioned); two-stage pipeline with grasp proposal generation (CVAE) followed by goal-conditioned RL grasping policy

**핸드 하드웨어:** Shadow Hand (24 DoF)

**시뮬레이션 플랫폼:** IsaacGym

**Sim2Real 여부:** No

**객체 수:** 3000+ objects from diverse categories; ~60% success rate (sim)

**작업:** Universal dexterous grasping from arbitrary initial configurations

**핵심 방법론:** Decomposes the universal grasping problem into two stages: (1) a contact-map-based grasp proposal network generates diverse feasible grasp poses for novel objects, and (2) a goal-conditioned RL policy (PPO) executes the grasp given the proposed target hand configuration. The grasp proposal network uses a conditional variational autoencoder trained on successful grasps.

**주요 기여:**
- First system to attempt universal dexterous grasping across 3000+ objects with a single pipeline
- Contact-map-based grasp proposal generation that generalizes to unseen object geometries
- Goal-conditioned RL policy that can reach diverse grasp configurations

**정량적 결과:**

| Metric | Value |
|---|---|
| Overall success rate | ~60% (sim) |
| Object set size | 3000+ |
| Hand | Shadow (24 DoF) |

Note: the ~60% success rate is significantly lower than the follow-up UniDexGrasp++ (85.4% sim), indicating the performance ceiling of the original pipeline.

**한계점:** ~60% success rate is significantly lower than UniDexGrasp++ (85.4%); struggles with objects that require precise finger placement; simulation-only; Shadow Hand only; requires object point cloud at test time

**시뮬레이션 전용 한계:** 시뮬레이션에서만 평가됨; sim-to-real 전이 미입증, 실제 환경 실행 가능성 미검증.

## 추론 / 배포

- **추론 지연 시간:** Not reported. The CVAE grasp proposal + MLP goal-conditioned policy runs in <5ms total per step.
- **배포 하드웨어:** Simulation only (IsaacGym). No real-robot deployment demonstrated.
- **실시간 가능 여부:** Yes, for the policy itself. However, only simulation evaluation was performed.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** No pre-collected demonstration dataset. Two-stage pipeline: (1) CVAE-based grasp proposal network trained on successful grasps generated in simulation, (2) goal-conditioned RL policy (PPO) trained in IsaacGym.
- **수집 방법:** Grasp proposals generated procedurally via contact-map-based CVAE. RL policy trained via online interaction in IsaacGym with 3,000+ objects. Object meshes from diverse 3D model datasets.
- **데이터 규모:** 3,000+ objects. Grasp proposals generated at scale; RL training episodes not reported.
- **원격 조작 장비:** Not applicable (procedural generation + pure RL).
- **데이터 포맷:** Not applicable (online RL + procedural grasp generation).
- **공개 여부:** Object point clouds required at test time. Dataset/code release status not reported.
