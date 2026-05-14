### 7.1 DexPoint

**Full title:** DexPoint: Generalizable Point Cloud Reinforcement Learning for Sim-to-Real Dexterous Manipulation

**Authors:** Yuzhe Qin, Binghao Huang, Zhao-Heng Yin, Hao Su, Xiaolong Wang

**Venue/Year:** CoRL 2022

**arXiv:** https://arxiv.org/abs/2211.09423

**RL algorithm:** PPO with point cloud observations. Uses imagined hand point clouds as augmented inputs and contact-based reward shaping for efficient learning.

**Hand hardware:** Allegro Hand (16 DoF) for real-world experiments

**Sim platform:** IsaacGym (NVIDIA GPU-accelerated simulation)

**Sim2Real?** Yes. Zero-shot sim-to-real transfer on Allegro Hand. Key sim-to-real innovations: (1) point cloud representation is more transferable than RGB images across sim-to-real gap, (2) imagined hand point clouds provide a geometry-aware representation invariant to visual domain shift, (3) contact-based rewards encourage physically meaningful grasping behaviors.

**Object count:** Multiple objects within categories; demonstrated generalization to novel objects of the same category in real world.

**Tasks:** Dexterous grasping of diverse objects. Demonstrated category-level generalization: policies trained on a set of objects generalize to novel objects within the same category in the real world.

**Key methodology:** Proposes using point cloud observations for dexterous manipulation RL, addressing the sim-to-real gap that plagues image-based approaches. Two key innovations: (1) Augments the object point cloud with "imagined hand point clouds" -- synthetic point clouds of the robot hand generated from proprioceptive state -- providing geometric awareness of hand-object spatial relationships without relying on visual rendering. (2) Contact-based reward functions encourage the policy to learn physically meaningful interactions rather than exploiting simulator artifacts. The point cloud representation is naturally more sim-to-real transferable than RGB images since it captures geometry directly.

**Main contributions:**
- First RL-based policy achieving category-level generalization for dexterous grasping with sim-to-real transfer
- Introduced imagined hand point clouds as an augmented representation bridging sim-to-real for dexterous hands
- Contact-based reward design for physically meaningful grasping behaviors
- Demonstrated zero-shot sim-to-real transfer on Allegro Hand across diverse objects

**Quantitative results:**

| Metric | Value |
|---|---|
| Novel object generalization | Category-level (first for dexterous policy learning) |
| Real-world hand | Allegro Hand (16 DoF) |
| Sim2Real | Zero-shot transfer |
| Observation | Point cloud (object + imagined hand) |
| Sim platform | IsaacGym |

**Limitations/Gaps:**
- **Force control:** No force sensing or impedance control; position-based grasping only
- **VLA/Language:** No language conditioning or VLA integration
- **Sim2Real:** Point clouds require depth camera; depth sensing quality affects real-world performance
- **Code:** [GitHub](https://github.com/yzqin/dexpoint-release) available
- **Task scope:** Limited to grasping; does not address in-hand manipulation, tool use, or multi-stage tasks
- **Object diversity:** Category-level generalization shown but within limited categories; not tested on thousands of objects like UniDexGrasp

## Inference / Deployment

- **Inference latency:** Not explicitly reported. The MLP policy with point cloud (imagined hand) input runs in <5ms per forward pass.
- **Deployment hardware:** Allegro Hand (16 DoF) for real-world deployment. Policy trained in IsaacGym; deployed via zero-shot sim-to-real transfer with point cloud observations.
- **Real-time capable?** Yes. Lightweight policy with point cloud encoder supports real-time dexterous grasping on real Allegro Hand.
