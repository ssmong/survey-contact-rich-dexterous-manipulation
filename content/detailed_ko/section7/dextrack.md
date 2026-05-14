### 7.4 DexTrack

**전체 제목:** DexTrack: Towards Generalizable Neural Tracking Control for Dexterous Manipulation from Human References

**저자:** Yuzhe Qin, Meowuu7 (pseudonym), Hao Su, Xiaolong Wang, et al. (PKU / Shanghai AI Lab)

**학회/연도:** ICLR 2025

**arXiv:** https://arxiv.org/abs/2501.15760

**RL 알고리즘:** PPO with motion tracking reward. Policy learns to track retargeted human hand motion capture trajectories on robot hands. Uses privileged training with distillation.

**핸드 하드웨어:** Shadow Hand (24 DoF), Allegro Hand (16 DoF)

**시뮬레이션 플랫폼:** IsaacGym (inferred)

**Sim2Real 여부:** No. Simulation-only.

**작업:** Motion capture tracking: the robot hand must reproduce human hand motion trajectories retargeted from MoCap data. Tasks span grasping, in-hand manipulation, and dexterous coordination as captured in human demonstrations.

**핵심 방법론:** DexTrack trains a generalizable neural controller that can track arbitrary human hand motions retargeted to a robot hand. Rather than training one policy per task, DexTrack conditions on the target trajectory, enabling a single policy to handle diverse manipulation behaviors. The approach uses a tracking reward that penalizes deviations from reference joint angles and fingertip positions, combined with contact-aware rewards that encourage physically plausible interactions.

**주요 기여:**
- Trained a single generalizable policy that can track diverse human hand motions on robot hands, rather than per-task policies
- Demonstrated cross-embodiment tracking: the same framework works for Shadow (24 DoF) and Allegro (16 DoF) hands
- Provided a pathway from human demonstrations to robot execution via motion retargeting + neural tracking

**한계점:** Sim-only; real-world tracking not demonstrated. Retargeting from human to robot hand introduces kinematic mismatches. Tracking does not guarantee task success (faithfully reproducing motion does not account for object dynamics). Partial code release.

**시뮬레이션 전용 한계:** 시뮬레이션에서만 평가됨; sim-to-real 전이 미입증, 실제 환경 실행 가능성 미검증.

**결과:** Achieved high tracking accuracy across diverse motion trajectories on both Shadow and Allegro hands (sim). Code partially available.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** Human hand motion capture data retargeted to robot hands. RL training in IsaacGym.
- **수집 방법:** RL + human MoCap demos. PPO with motion tracking reward. Human hand MoCap trajectories retargeted to Shadow (24 DoF) and Allegro (16 DoF) hands. Policy conditioned on target trajectory for generalizable tracking. Privileged training with distillation.
- **데이터 규모:** Diverse MoCap trajectories spanning grasping, in-hand manipulation, and dexterous coordination. Specific trajectory counts not reported.
- **원격 조작 장비:** Not applicable (MoCap data, not live teleoperation).
- **데이터 포맷:** Retargeted MoCap trajectories (joint angle sequences for robot hands).
- **공개 여부:** Code partially available.

## 추론 / 배포

- **추론 지연 시간:** Not reported. The distilled student MLP policy runs in <1ms per forward pass.
- **배포 하드웨어:** Simulation only (IsaacGym). Evaluated on Shadow Hand (24 DoF) and Allegro Hand (16 DoF) in simulation. No real-robot deployment demonstrated.
- **실시간 가능 여부:** Yes, for the policy itself (MLP inference is trivially fast). However, only simulation evaluation was performed.
