### 7.1 DexPoint

**전체 제목:** DexPoint: Generalizable Point Cloud Reinforcement Learning for Sim-to-Real Dexterous Manipulation

**저자:** Yuzhe Qin, Binghao Huang, Zhao-Heng Yin, Hao Su, Xiaolong Wang

**학회/연도:** CoRL 2022

**arXiv:** https://arxiv.org/abs/2211.09423

**RL 알고리즘:** PPO with point cloud observations. Uses imagined hand point clouds as augmented inputs and contact-based reward shaping for efficient learning.

**핸드 하드웨어:** Allegro Hand (16 DoF) for real-world experiments

**시뮬레이션 플랫폼:** IsaacGym (NVIDIA GPU-accelerated simulation)

**Sim2Real 여부:** Yes. Zero-shot sim-to-real transfer on Allegro Hand. Key sim-to-real innovations: (1) point cloud representation is more transferable than RGB images across sim-to-real gap, (2) imagined hand point clouds provide a geometry-aware representation invariant to visual domain shift, (3) contact-based rewards encourage physically meaningful grasping behaviors.

**객체 수:** Multiple objects within categories; demonstrated generalization to novel objects of the same category in real world.

**작업:** Dexterous grasping of diverse objects. Demonstrated category-level generalization: policies trained on a set of objects generalize to novel objects within the same category in the real world.

**핵심 방법론:** Proposes using point cloud observations for dexterous manipulation RL, addressing the sim-to-real gap that plagues image-based approaches. Two key innovations: (1) Augments the object point cloud with "imagined hand point clouds" -- synthetic point clouds of the robot hand generated from proprioceptive state -- providing geometric awareness of hand-object spatial relationships without relying on visual rendering. (2) Contact-based reward functions encourage the policy to learn physically meaningful interactions rather than exploiting simulator artifacts. The point cloud representation is naturally more sim-to-real transferable than RGB images since it captures geometry directly.

**주요 기여:**
- First RL-based policy achieving category-level generalization for dexterous grasping with sim-to-real transfer
- Introduced imagined hand point clouds as an augmented representation bridging sim-to-real for dexterous hands
- Contact-based reward design for physically meaningful grasping behaviors
- Demonstrated zero-shot sim-to-real transfer on Allegro Hand across diverse objects

**정량적 결과:**

| Metric | Value |
|---|---|
| Novel object generalization | Category-level (first for dexterous policy learning) |
| Real-world hand | Allegro Hand (16 DoF) |
| Sim2Real | Zero-shot transfer |
| Observation | Point cloud (object + imagined hand) |
| Sim platform | IsaacGym |

**한계점:**
- **Force control:** No force sensing or impedance control; position-based grasping only
- **VLA/Language:** No language conditioning or VLA integration
- **Sim2Real:** Point clouds require depth camera; depth sensing quality affects real-world performance
- **Code:** [GitHub](https://github.com/yzqin/dexpoint-release) available
- **Task scope:** Limited to grasping; does not address in-hand manipulation, tool use, or multi-stage tasks
- **Object diversity:** Category-level generalization shown but within limited categories; not tested on thousands of objects like UniDexGrasp

## 추론 / 배포

- **추론 지연 시간:** Not explicitly reported. The MLP policy with point cloud (imagined hand) input runs in <5ms per forward pass.
- **배포 하드웨어:** Allegro Hand (16 DoF) for real-world deployment. Policy trained in IsaacGym; deployed via zero-shot sim-to-real transfer with point cloud observations.
- **실시간 가능 여부:** Yes. Lightweight policy with point cloud encoder supports real-time dexterous grasping on real Allegro Hand.
