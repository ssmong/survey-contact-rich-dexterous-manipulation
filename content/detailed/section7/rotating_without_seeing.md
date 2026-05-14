### 7.2 Rotating without Seeing

**Full title:** Rotating without Seeing: Towards In-hand Dexterity through Touch

**Authors:** Zhao-Heng Yin, Binghao Huang, Yuzhe Qin, Qifeng Chen, Xiaolong Wang

**Venue/Year:** RSS 2023

**arXiv:** https://arxiv.org/abs/2303.10880

**RL algorithm:** PPO with teacher-student distillation. Teacher policy trained with privileged state (object pose, contact forces); student policy distilled to use only proprioception and tactile input.

**Hand hardware:** Allegro Hand (16 DoF) with dense binary tactile sensors (touch/no-touch) covering fingertips, finger links, and palm

**Sim platform:** IsaacGym

**Sim2Real?** Yes. Zero-shot sim-to-real transfer. The use of binary tactile sensors (touch/no-touch) minimizes the sim-to-real gap since binary contact signals are easier to simulate accurately than high-resolution tactile images. Domain randomization over physical parameters.

**Tasks:** In-hand object rotation around specified axes using tactile feedback only (no vision). Tested on diverse objects including cubes, cylinders, and irregular shapes.

**Key methodology:** Demonstrates that tactile sensing alone (without any visual input) is sufficient for dexterous in-hand rotation. Uses dense binary force sensors that provide broad coverage across the hand surface. The binary nature of the sensors (contact vs. no contact) is deliberately chosen to minimize the sim-to-real gap, since binary contact signals can be simulated with high fidelity. A teacher-student framework first trains with privileged information, then distills to a policy using only proprioception and binary touch signals.

**Main contributions:**
- First RL-based demonstration of tactile-only (no vision) in-hand object rotation with sim-to-real transfer
- Showed that dense binary tactile sensors with broad coverage outperform sparse high-resolution sensors for sim-to-real dexterous manipulation
- Minimized sim-to-real gap by using binary (touch/no-touch) sensing modality that is trivially simulatable
- Generalized to novel objects not seen during training in real-world experiments

**Quantitative results:**

| Metric | Value |
|---|---|
| Rotation success (sim) | >90% across objects |
| Real-world transfer | Zero-shot, multiple objects |
| Sensor modality | Binary tactile only (no vision) |
| Hand | Allegro (16 DoF) |

**Limitations/Gaps:**
- **Force control:** Binary tactile only (touch/no-touch); no continuous force measurement or impedance control
- **VLA/Language:** No language conditioning or VLA integration
- **Sim2Real:** Binary tactile simplifies transfer but sacrifices force magnitude information
- **Code:** Project page at https://touchdexterity.github.io; code availability limited
- **Task scope:** Limited to rotation; does not address functional manipulation or tool use

## Inference / Deployment

- **Inference latency:** Not explicitly reported. The tactile-conditioned MLP policy runs in <1ms per forward pass. Binary tactile processing is computationally trivial.
- **Deployment hardware:** Allegro Hand (16 DoF) with dense binary tactile sensors. Policy trained in IsaacGym; deployed via zero-shot sim-to-real transfer.
- **Real-time capable?** Yes. Demonstrated real-time in-hand rotation on real Allegro Hand with binary tactile feedback.
