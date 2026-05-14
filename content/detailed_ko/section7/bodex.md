### 7.1 BODex

**전체 제목:** BODex: Bilevel Optimization for Efficient and Scalable Dexterous Grasping

**저자:** Jiayi Chen, Yuxing Chen, Jialiang Zhang, He Wang

**학회/연도:** ICRA 2025

**PKU-EPIC lineage:** Replaces RL-based grasp generation (UniDexGrasp/UniDexGrasp++) with bilevel optimization, enabling cross-hand support without per-hand RL training. Core algorithmic shift from learned policies to optimization-based grasp synthesis.

**RL 알고리즘:** Bilevel optimization (not standard RL) -- outer loop optimizes grasp contact points, inner loop solves inverse kinematics via cuRobo; generates grasp datasets rather than learned policies

**핸드 하드웨어:** Shadow Hand (24 DoF), Allegro Hand (16 DoF), LEAP Hand (16 DoF)

**시뮬레이션 플랫폼:** cuRobo (CUDA-accelerated robot optimization)

**Sim2Real 여부:** Yes; 81% real-world success rate (real) with generated grasps

**객체 수:** 5355 objects; massive-scale grasp dataset generation

**작업:** Dexterous grasp generation (grasp pose synthesis rather than closed-loop control)

**핵심 방법론:** Formulates dexterous grasp synthesis as a bilevel optimization problem. The outer level optimizes contact point locations on the object surface to maximize grasp quality metrics (force closure, surface coverage). The inner level uses cuRobo's GPU-accelerated inverse kinematics to find feasible hand configurations reaching those contacts. This avoids RL training entirely, enabling rapid grasp generation at scale.

**주요 기여:**
- Orders of magnitude faster grasp generation than RL-based approaches (minutes vs. hours)
- Cross-embodiment support (Shadow, Allegro, LEAP) from a single optimization framework
- 81% sim-to-real transfer rate (real), validating generated grasps on physical hardware

**정량적 결과:**

| Metric | Value |
|---|---|
| Real-world success rate | 81% (real) |
| Object set size | 5355 |
| Hands supported | Shadow, Allegro, LEAP |
| Generation speed | Orders of magnitude faster than RL |

**한계점:** Open-loop grasp synthesis (no closed-loop execution policy); relies on accurate object geometry; no handling of object uncertainty or partial views; grasp quality metrics may not capture real-world robustness factors (surface friction, compliance)

## 추론 / 배포

- **추론 지연 시간:** Optimization-based grasp computation is offline (not real-time inference). cuRobo-accelerated IK solving is orders of magnitude faster than RL-based alternatives for grasp generation. Deployment executes pre-computed grasps open-loop.
- **배포 하드웨어:** Real deployment on Shadow, Allegro, and LEAP hands (81% real-world success rate). Grasp computation uses NVIDIA GPU via cuRobo.
- **실시간 가능 여부:** Yes, at deployment (pre-computed grasps executed open-loop). Grasp generation itself is offline but fast (cuRobo-accelerated).

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** Procedurally generated grasp dataset via bilevel optimization (not RL). 5,355 objects from 3D model repositories.
- **수집 방법:** Optimization-based grasp synthesis using cuRobo (CUDA-accelerated). Outer loop optimizes contact points on object surfaces; inner loop solves inverse kinematics. Cross-embodiment (Shadow, Allegro, LEAP). No RL training, no demonstrations.
- **데이터 규모:** 5,355 objects. Massive-scale grasp dataset generated in minutes (vs. hours for RL approaches).
- **원격 조작 장비:** Not applicable (optimization-based, no demonstrations).
- **데이터 포맷:** Generated grasp poses (hand configurations for target objects). Specific format not reported.
- **공개 여부:** Dataset/code release status not reported.
