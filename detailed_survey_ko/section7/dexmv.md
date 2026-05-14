### 7.4 DexMV

**전체 제목:** DexMV: Imitation Learning for Dexterous Manipulation from Human Videos

**저자:** Yuzhe Qin, Yueh-Hua Wu, Shaowei Liu, Hanwen Jiang, Ruihan Yang, Yang Fu, Xiaolong Wang

**학회/연도:** ECCV 2022

**arXiv:** https://arxiv.org/abs/2108.05877

**RL 알고리즘:** DAPG (Demo Augmented Policy Gradient) -- combines RL (PPO) with demonstrations extracted from human videos. The demonstrations provide initial guidance, and RL fine-tunes beyond demonstration quality.

**핸드 하드웨어:** Adroit Hand (30 DoF, simulated Shadow Hand equivalent) in SAPIEN simulator

**시뮬레이션 플랫폼:** SAPIEN (for rendering and physics); MuJoCo (for Adroit hand dynamics)

**Sim2Real 여부:** No. All experiments are in simulation. The paper focuses on the vision-to-policy pipeline (human video to robot demonstration to RL policy).

**작업:** Dexterous manipulation tasks including: object relocation, pour (pouring from a container), place (placing objects at target locations). Tasks require coordinated multi-finger manipulation.

**핵심 방법론:** Proposes a complete pipeline from human video to dexterous robot policy. (1) Captures human hand manipulation in video. (2) Uses computer vision (hand pose estimation, object tracking) to extract 3D hand and object trajectories from video. (3) Retargets human hand motions to the robot hand (Adroit) via optimization-based retargeting that maps human finger configurations to robot joint angles. (4) Uses the retargeted demonstrations with DAPG to train RL policies that surpass demonstration quality. The key insight is that human videos provide a natural and scalable source of dexterous manipulation demonstrations.

**주요 기여:**
- Proposed one of the first end-to-end pipelines from human video to dexterous RL policy, combining hand pose estimation, retargeting, and DAPG
- Demonstrated that RL policies trained with video-extracted demonstrations significantly outperform pure RL on dexterous tasks
- Introduced DexMV platform combining SAPIEN rendering with MuJoCo physics for dexterous manipulation research
- Showed that even noisy, imperfect demonstrations from video are sufficient to accelerate RL training

**정량적 결과:**

| Metric | Value |
|---|---|
| Tasks | Relocate, pour, place (dexterous manipulation) |
| DAPG + video demos vs. pure RL | Significantly higher success rates |
| Hand | Adroit (30 DoF, simulated) |
| Video source | Human hand manipulation recordings |
| Platform | SAPIEN + MuJoCo |

**한계점:**
- **Force control:** No force sensing or impedance control; position-based policies only
- **VLA/Language:** No language conditioning; task specification is implicit in the demonstration
- **Sim2Real:** No real-world experiments; simulation-only evaluation
- **Code:** [GitHub](https://github.com/yzqin/dexmv-sim) available
- **Retargeting:** Human-to-robot retargeting introduces errors due to kinematic differences; quality depends on hand pose estimation accuracy
- **Scalability:** Requires per-task human video capture; not yet demonstrated at scale

**시뮬레이션 전용 한계:** 시뮬레이션에서만 평가됨; sim-to-real 전이 미입증, 실제 환경 실행 가능성 미검증.

## 추론 / 배포

- **추론 지연 시간:** Not reported. The MLP policy (DAPG-trained) runs in <1ms per forward pass.
- **배포 하드웨어:** Simulation only (SAPIEN/MuJoCo). No real-robot deployment demonstrated.
- **실시간 가능 여부:** Yes, for the policy itself (MLP inference is trivially fast). However, only simulation evaluation was performed.
