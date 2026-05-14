### 7.1 RobustDexGrasp

**전체 제목:** RobustDexGrasp: Robust Dexterous Grasping of General Objects from Single-view Point Clouds

**저자:** Zhaole Sun, Kai Chen, Martin Pfanne, Yao Guo, Guang-Zhong Yang

**학회/연도:** CoRL 2025

**RL 알고리즘:** PPO with teacher-student distillation; teacher uses privileged state info, student learns from single-view point clouds

**핸드 하드웨어:** Allegro Hand (16 DoF) + UR5 arm

**시뮬레이션 플랫폼:** RaiSim

**Sim2Real 여부:** Yes; 94.6% real-world success rate (real) on 512 real objects

**객체 수:** 247,000 objects in simulation; 512 real objects for evaluation

**작업:** Robust dexterous grasping from single-view partial point clouds with arm-hand coordination

**핵심 방법론:** Trains a teacher policy with PPO using privileged full-state information, then distills it into a student policy that operates from single-view point clouds. The teacher-student framework bridges the gap between what is available in simulation (full state) and what is observable in the real world (partial view). Extensive domain randomization (object geometry, mass, friction, sensor noise) enables robust zero-shot sim-to-real transfer.

**주요 기여:**
- State-of-the-art sim-to-real dexterous grasping success rate (94.6% real) at time of publication
- Single-view point cloud input enabling practical deployment without full object reconstruction
- Demonstrated on Allegro + UR5 system with 512 diverse real objects, the largest real-world evaluation in the dexterous grasping literature

**정량적 결과:**

| Metric | Value |
|---|---|
| Real-world success rate | 94.6% (real) |
| Real eval object count | 512 |
| Sim training objects | 247,000 |
| Hand | Allegro (16 DoF) + UR5 |

**한계점:** Grasping only (no subsequent manipulation); uses RaiSim which has a smaller community than IsaacGym/MuJoCo; teacher-student gap may limit performance on highly novel geometries; no tactile feedback

## 추론 / 배포

- **추론 지연 시간:** Not explicitly reported. The distilled student policy (MLP with point cloud encoder) runs in <5ms per forward pass.
- **배포 하드웨어:** Allegro Hand (16 DoF) + UR5 arm. Policy trained in RaiSim; deployed via zero-shot sim-to-real transfer. 94.6% real-world success rate on 512 objects.
- **실시간 가능 여부:** Yes. Lightweight distilled policy supports real-time grasping control on real hardware.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** No pre-collected dataset. Pure RL (PPO) with teacher-student distillation in RaiSim.
- **수집 방법:** Pure RL in RaiSim simulation. Teacher trained with privileged full-state information; student distilled to single-view point cloud observations. Extensive domain randomization (object geometry, mass, friction, sensor noise). 247,000 simulated objects for training.
- **데이터 규모:** 247,000 objects in simulation for training. 512 real objects for evaluation. Real-world success rate: 94.6%.
- **원격 조작 장비:** Not applicable (pure RL, no demonstrations).
- **데이터 포맷:** Not applicable (online RL, no offline dataset).
- **공개 여부:** Dataset/code release status not reported.
