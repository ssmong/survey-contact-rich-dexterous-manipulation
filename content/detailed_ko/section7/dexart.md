### 7.3 DexArt

**전체 제목:** DexArt: Benchmarking Generalizable Dexterous Manipulation with Articulated Objects

**저자:** Chen Bao, Helin Xu, Yuzhe Qin, Xiaolong Wang

**학회/연도:** CVPR 2023

**arXiv:** https://arxiv.org/abs/2305.05706

**RL 알고리즘:** PPO with point-cloud observations. Trains with domain randomization over articulated object instances to achieve generalization.

**핸드 하드웨어:** Allegro Hand (16 DoF) mounted on a floating base (no arm)

**시뮬레이션 플랫폼:** SAPIEN (PhysX backend)

**Sim2Real 여부:** No. Simulation-only benchmark.

**작업:** 4 articulated object manipulation tasks: (1) faucet turning -- rotate faucet handles of varying geometry; (2) laptop opening -- open laptop lids with different hinge configurations; (3) bucket lifting -- grasp and lift buckets by handles; (4) toilet lid -- open/close toilet seats. Each task includes multiple object instances with varying geometry for generalization evaluation.

**핵심 방법론:** DexArt addresses dexterous manipulation of articulated objects, which requires understanding joint constraints and contact dynamics beyond rigid-body grasping. The benchmark uses point-cloud observations and trains across diverse object instances within each category, evaluating both in-distribution and out-of-distribution generalization. The approach reveals that naive RL struggles with articulated objects due to the combinatorial complexity of multi-finger contact with articulated joints.

**주요 기여:**
- Introduced the first benchmark specifically for dexterous manipulation of articulated objects with generalization evaluation
- Demonstrated that point-cloud-based RL policies can generalize across object instances within a category
- Identified key challenges: contact-rich articulated manipulation requires understanding of joint constraints that simple reward shaping does not capture

**한계점:** Sim-only, no real-world validation. Floating hand (no arm) simplifies the problem. Limited to 4 task categories. Performance degrades significantly on out-of-distribution object instances.

**시뮬레이션 전용 한계:** 시뮬레이션에서만 평가됨; sim-to-real 전이 미입증, 실제 환경 실행 가능성 미검증.

**결과:** Achieved reasonable success rates on in-distribution objects but showed substantial drops on novel instances, highlighting the generalization challenge (sim). Code and pretrained weights publicly available.

## 추론 / 배포

- **추론 지연 시간:** Not reported. The MLP policy with point cloud encoder runs in <5ms per forward pass.
- **배포 하드웨어:** Simulation only (SAPIEN). No real-robot deployment demonstrated.
- **실시간 가능 여부:** Yes, for the policy itself. However, only simulation evaluation was performed.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** No pre-collected dataset. Pure RL (PPO) with point-cloud observations in SAPIEN simulator.
- **수집 방법:** Pure RL in SAPIEN (PhysX backend). Domain randomization over articulated object instances within each category. 4 task categories: faucet turning, laptop opening, bucket lifting, toilet lid. Each category includes multiple object instances with varying geometry.
- **데이터 규모:** Multiple articulated object instances per category for training and out-of-distribution generalization evaluation.
- **원격 조작 장비:** Not applicable (pure RL, no demonstrations).
- **데이터 포맷:** Not applicable (online RL, no offline dataset).
- **공개 여부:** Yes -- code and pretrained weights publicly available.
