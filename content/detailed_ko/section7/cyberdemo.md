### 7.4 CyberDemo

**전체 제목:** CyberDemo: Augmenting Simulated Human Demonstration for Real-World Dexterous Manipulation

**저자:** Jun Wang, Yuzhe Qin, Kaiming Kuang, Yigit Korkmaz, Akhilan Gurumoorthy, Hao Su, Xiaolong Wang

**학회/연도:** CVPR 2024

**arXiv:** https://arxiv.org/abs/2402.14795

**RL 알고리즘:** Imitation learning (behavior cloning) from augmented simulated demonstrations. Uses human hand demonstrations retargeted to robot hand in simulation, then extensively augmented with domain randomization.

**핸드 하드웨어:** Allegro Hand (16 DoF) for real-world deployment

**시뮬레이션 플랫폼:** IsaacGym / SAPIEN (for simulation environment and demonstration augmentation)

**Sim2Real 여부:** Yes. Core contribution is sim-to-real transfer via augmented simulated demonstrations. Demonstrations are collected from human hand motions, retargeted to the Allegro Hand in simulation, then augmented with variations in object pose, lighting, physical properties, and camera viewpoints. Policies trained on augmented sim data transfer to real Allegro Hand.

**작업:** Dexterous manipulation including valve rotation (tri-valve, tetra-valve, penta-valve) and other object manipulation tasks. Tested on objects with varying geometry and physical properties, including novel objects not seen during training.

**핵심 방법론:** Addresses the data bottleneck in real-world dexterous manipulation by leveraging simulation for data augmentation. (1) Collects human demonstrations of manipulation tasks. (2) Retargets human hand motions to Allegro Hand in simulation. (3) Massively augments demonstrations in simulation by varying object geometry, texture, pose, physics parameters, and camera viewpoints. (4) Trains visuomotor policies (behavior cloning) on the augmented dataset. The key finding is that augmented simulated demonstrations outperform real-world demonstrations for policy training, because simulation enables orders-of-magnitude more diversity than real data collection.

**주요 기여:**
- Demonstrated that augmented simulated demonstrations surpass real-world demonstrations for dexterous manipulation policy training
- Extensive data augmentation pipeline in simulation (geometry, texture, pose, physics, viewpoint variations)
- Successful sim-to-real transfer on Allegro Hand for valve rotation and manipulation tasks
- Generalization to novel objects not seen during training, including different valve configurations

**정량적 결과:**

| Metric | Value |
|---|---|
| Sim demos vs. real demos | Sim augmented demos outperform real demos |
| Real-world hand | Allegro Hand (16 DoF) |
| Novel object generalization | Yes (unseen valve types) |
| Tasks | Valve rotation (tri/tetra/penta), manipulation |
| Sim2Real | Zero-shot via augmented demonstrations |

> Specific per-task success rates not reported in this entry; consult the paper for detailed numbers.

**한계점:**
- **Force control:** No force sensing or impedance control; position-based imitation learning
- **VLA/Language:** No language conditioning or VLA backbone
- **Sim2Real:** Augmentation helps but sim-to-real gap in contact dynamics remains; performance on highly contact-sensitive tasks not extensively evaluated
- **Code:** [GitHub](https://github.com/wang59695487/CyberDemo) available
- **Scalability:** Requires human demonstration collection as seed; augmentation is automated but seed collection is manual

## 추론 / 배포

- **추론 지연 시간:** Not explicitly reported. The behavior cloning policy (MLP/CNN) runs in <5ms per forward pass.
- **배포 하드웨어:** Allegro Hand (16 DoF) for real-world deployment. Policy trained on augmented simulated demonstrations in IsaacGym/SAPIEN; deployed via zero-shot sim-to-real transfer.
- **실시간 가능 여부:** Yes. Lightweight imitation learning policy supports real-time control on real Allegro Hand.
