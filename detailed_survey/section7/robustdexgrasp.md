### 7.1 RobustDexGrasp

**Full title:** RobustDexGrasp: Robust Dexterous Grasping of General Objects from Single-view Point Clouds

**Authors:** Zhaole Sun, Kai Chen, Martin Pfanne, Yao Guo, Guang-Zhong Yang

**Venue/Year:** CoRL 2025

**RL algorithm:** PPO with teacher-student distillation; teacher uses privileged state info, student learns from single-view point clouds

**Hand hardware:** Allegro Hand (16 DoF) + UR5 arm

**Sim platform:** RaiSim

**Sim2Real?** Yes; 94.6% real-world success rate (real) on 512 real objects

**Object count:** 247,000 objects in simulation; 512 real objects for evaluation

**Tasks:** Robust dexterous grasping from single-view partial point clouds with arm-hand coordination

**Key methodology:** Trains a teacher policy with PPO using privileged full-state information, then distills it into a student policy that operates from single-view point clouds. The teacher-student framework bridges the gap between what is available in simulation (full state) and what is observable in the real world (partial view). Extensive domain randomization (object geometry, mass, friction, sensor noise) enables robust zero-shot sim-to-real transfer.

**Main contributions:**
- State-of-the-art sim-to-real dexterous grasping success rate (94.6% real) at time of publication
- Single-view point cloud input enabling practical deployment without full object reconstruction
- Demonstrated on Allegro + UR5 system with 512 diverse real objects, the largest real-world evaluation in the dexterous grasping literature

**Quantitative results:**

| Metric | Value |
|---|---|
| Real-world success rate | 94.6% (real) |
| Real eval object count | 512 |
| Sim training objects | 247,000 |
| Hand | Allegro (16 DoF) + UR5 |

**Limitations/Gaps:** Grasping only (no subsequent manipulation); uses RaiSim which has a smaller community than IsaacGym/MuJoCo; teacher-student gap may limit performance on highly novel geometries; no tactile feedback

## Inference / Deployment

- **Inference latency:** Not explicitly reported. The distilled student policy (MLP with point cloud encoder) runs in <5ms per forward pass.
- **Deployment hardware:** Allegro Hand (16 DoF) + UR5 arm. Policy trained in RaiSim; deployed via zero-shot sim-to-real transfer. 94.6% real-world success rate on 512 objects.
- **Real-time capable?** Yes. Lightweight distilled policy supports real-time grasping control on real hardware.

## Dataset / Data Collection

- **Dataset used:** No pre-collected dataset. Pure RL (PPO) with teacher-student distillation in RaiSim.
- **Collection method:** Pure RL in RaiSim simulation. Teacher trained with privileged full-state information; student distilled to single-view point cloud observations. Extensive domain randomization (object geometry, mass, friction, sensor noise). 247,000 simulated objects for training.
- **Data scale:** 247,000 objects in simulation for training. 512 real objects for evaluation. Real-world success rate: 94.6%.
- **Teleop equipment:** Not applicable (pure RL, no demonstrations).
- **Data format:** Not applicable (online RL, no offline dataset).
- **Publicly available?** Dataset/code release status not reported.
