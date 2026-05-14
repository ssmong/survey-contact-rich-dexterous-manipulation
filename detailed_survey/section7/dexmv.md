### 7.4 DexMV

**Full title:** DexMV: Imitation Learning for Dexterous Manipulation from Human Videos

**Authors:** Yuzhe Qin, Yueh-Hua Wu, Shaowei Liu, Hanwen Jiang, Ruihan Yang, Yang Fu, Xiaolong Wang

**Venue/Year:** ECCV 2022

**arXiv:** https://arxiv.org/abs/2108.05877

**RL algorithm:** DAPG (Demo Augmented Policy Gradient) -- combines RL (PPO) with demonstrations extracted from human videos. The demonstrations provide initial guidance, and RL fine-tunes beyond demonstration quality.

**Hand hardware:** Adroit Hand (30 DoF, simulated Shadow Hand equivalent) in SAPIEN simulator

**Sim platform:** SAPIEN (for rendering and physics); MuJoCo (for Adroit hand dynamics)

**Sim2Real?** No. All experiments are in simulation. The paper focuses on the vision-to-policy pipeline (human video to robot demonstration to RL policy).

**Tasks:** Dexterous manipulation tasks including: object relocation, pour (pouring from a container), place (placing objects at target locations). Tasks require coordinated multi-finger manipulation.

**Key methodology:** Proposes a complete pipeline from human video to dexterous robot policy. (1) Captures human hand manipulation in video. (2) Uses computer vision (hand pose estimation, object tracking) to extract 3D hand and object trajectories from video. (3) Retargets human hand motions to the robot hand (Adroit) via optimization-based retargeting that maps human finger configurations to robot joint angles. (4) Uses the retargeted demonstrations with DAPG to train RL policies that surpass demonstration quality. The key insight is that human videos provide a natural and scalable source of dexterous manipulation demonstrations.

**Main contributions:**
- Proposed one of the first end-to-end pipelines from human video to dexterous RL policy, combining hand pose estimation, retargeting, and DAPG
- Demonstrated that RL policies trained with video-extracted demonstrations significantly outperform pure RL on dexterous tasks
- Introduced DexMV platform combining SAPIEN rendering with MuJoCo physics for dexterous manipulation research
- Showed that even noisy, imperfect demonstrations from video are sufficient to accelerate RL training

**Quantitative results:**

| Metric | Value |
|---|---|
| Tasks | Relocate, pour, place (dexterous manipulation) |
| DAPG + video demos vs. pure RL | Significantly higher success rates |
| Hand | Adroit (30 DoF, simulated) |
| Video source | Human hand manipulation recordings |
| Platform | SAPIEN + MuJoCo |

**Limitations/Gaps:**
- **Force control:** No force sensing or impedance control; position-based policies only
- **VLA/Language:** No language conditioning; task specification is implicit in the demonstration
- **Sim2Real:** No real-world experiments; simulation-only evaluation
- **Code:** [GitHub](https://github.com/yzqin/dexmv-sim) available
- **Retargeting:** Human-to-robot retargeting introduces errors due to kinematic differences; quality depends on hand pose estimation accuracy
- **Scalability:** Requires per-task human video capture; not yet demonstrated at scale

**Sim-only limitation:** Evaluated in simulation only; no sim-to-real transfer demonstrated, real-world viability unvalidated.

## Inference / Deployment

- **Inference latency:** Not reported. The MLP policy (DAPG-trained) runs in <1ms per forward pass.
- **Deployment hardware:** Simulation only (SAPIEN/MuJoCo). No real-robot deployment demonstrated.
- **Real-time capable?** Yes, for the policy itself (MLP inference is trivially fast). However, only simulation evaluation was performed.
