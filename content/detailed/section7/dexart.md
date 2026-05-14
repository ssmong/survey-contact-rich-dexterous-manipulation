### 7.3 DexArt

**Full title:** DexArt: Benchmarking Generalizable Dexterous Manipulation with Articulated Objects

**Authors:** Chen Bao, Helin Xu, Yuzhe Qin, Xiaolong Wang

**Venue/Year:** CVPR 2023

**arXiv:** https://arxiv.org/abs/2305.05706

**RL algorithm:** PPO with point-cloud observations. Trains with domain randomization over articulated object instances to achieve generalization.

**Hand hardware:** Allegro Hand (16 DoF) mounted on a floating base (no arm)

**Sim platform:** SAPIEN (PhysX backend)

**Sim2Real?** No. Simulation-only benchmark.

**Tasks:** 4 articulated object manipulation tasks: (1) faucet turning -- rotate faucet handles of varying geometry; (2) laptop opening -- open laptop lids with different hinge configurations; (3) bucket lifting -- grasp and lift buckets by handles; (4) toilet lid -- open/close toilet seats. Each task includes multiple object instances with varying geometry for generalization evaluation.

**Key methodology:** DexArt addresses dexterous manipulation of articulated objects, which requires understanding joint constraints and contact dynamics beyond rigid-body grasping. The benchmark uses point-cloud observations and trains across diverse object instances within each category, evaluating both in-distribution and out-of-distribution generalization. The approach reveals that naive RL struggles with articulated objects due to the combinatorial complexity of multi-finger contact with articulated joints.

**Main contributions:**
- Introduced the first benchmark specifically for dexterous manipulation of articulated objects with generalization evaluation
- Demonstrated that point-cloud-based RL policies can generalize across object instances within a category
- Identified key challenges: contact-rich articulated manipulation requires understanding of joint constraints that simple reward shaping does not capture

**Limitations/Gaps:** Sim-only, no real-world validation. Floating hand (no arm) simplifies the problem. Limited to 4 task categories. Performance degrades significantly on out-of-distribution object instances.

**Sim-only limitation:** Evaluated in simulation only; no sim-to-real transfer demonstrated, real-world viability unvalidated.

**Results:** Achieved reasonable success rates on in-distribution objects but showed substantial drops on novel instances, highlighting the generalization challenge (sim). Code and pretrained weights publicly available.

## Inference / Deployment

- **Inference latency:** Not reported. The MLP policy with point cloud encoder runs in <5ms per forward pass.
- **Deployment hardware:** Simulation only (SAPIEN). No real-robot deployment demonstrated.
- **Real-time capable?** Yes, for the policy itself. However, only simulation evaluation was performed.

## Dataset / Data Collection

- **Dataset used:** No pre-collected dataset. Pure RL (PPO) with point-cloud observations in SAPIEN simulator.
- **Collection method:** Pure RL in SAPIEN (PhysX backend). Domain randomization over articulated object instances within each category. 4 task categories: faucet turning, laptop opening, bucket lifting, toilet lid. Each category includes multiple object instances with varying geometry.
- **Data scale:** Multiple articulated object instances per category for training and out-of-distribution generalization evaluation.
- **Teleop equipment:** Not applicable (pure RL, no demonstrations).
- **Data format:** Not applicable (online RL, no offline dataset).
- **Publicly available?** Yes -- code and pretrained weights publicly available.
