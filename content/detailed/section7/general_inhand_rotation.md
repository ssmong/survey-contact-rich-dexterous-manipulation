### 7.2 General In-Hand Object Rotation with Vision and Touch

**Full title:** General In-Hand Object Rotation with Vision and Touch

**Authors:** Haozhi Qi, Brent Yi, Sudharshan Suresh, Mike Lambeta, Yi Ma, Roberto Calandra, Jitendra Malik

**Venue/Year:** CoRL 2023

**arXiv:** https://arxiv.org/abs/2309.09979

**RL algorithm:** PPO with teacher-student distillation and a visuotactile transformer for multimodal fusion. Teacher has access to ground-truth object state; student uses vision and touch.

**Hand hardware:** Allegro Hand (16 DoF) with DIGIT tactile sensors on fingertips

**Sim platform:** IsaacGym

**Sim2Real?** Yes. Zero-shot sim-to-real transfer. Trains with privileged state in simulation, then distills to realistic sensor modalities (RGB vision + DIGIT tactile images). The visuotactile transformer performs online inference of object shape and physical properties during deployment.

**Tasks:** Multi-axis fingertip-based in-hand object rotation. Rotates objects around multiple axes (not limited to single-axis as in prior work like Hora). Tested on diverse objects.

**Key methodology:** Extends the Hora/RotateIt line of work by fusing vision and touch through a visuotactile transformer architecture. The system trains in simulation with access to ground-truth object state, then uses a distillation process to transfer to policies that operate on realistic noisy sensory inputs (RGB images + DIGIT tactile readings). The transformer architecture fuses multimodal information to implicitly infer object shape and physical properties online, enabling generalization to unseen objects. This achieves general multi-axis in-hand rotation with combined vision and touch.

**Main contributions:**
- First learned policy combining vision and tactile sensing for multi-axis in-hand rotation with sim-to-real transfer
- Visuotactile transformer architecture that fuses RGB and tactile modalities for implicit object property inference
- Demonstrated improvement over vision-only and tactile-only baselines, showing complementary benefits of multimodal sensing
- Zero-shot sim-to-real transfer with realistic sensor simulation (DIGIT tactile + RGB)

**Quantitative results:**

| Metric | Value |
|---|---|
| Multi-axis rotation | Yes (improvement over single-axis Hora) |
| Sensor fusion | Vision (RGB) + Touch (DIGIT) |
| Baseline improvement | Outperforms vision-only and touch-only variants |
| Hand | Allegro (16 DoF) + DIGIT sensors |
| Real-world transfer | Zero-shot sim-to-real |

**Limitations/Gaps:**
- **Force control:** DIGIT provides tactile images, not explicit force vectors; no impedance control
- **VLA/Language:** No language conditioning or VLA integration
- **Sim2Real:** Tactile simulation fidelity (DIGIT image rendering in sim) remains a challenge; binary contact may transfer better
- **Code:** Part of the Hora codebase ecosystem; specific code release status varies
- **Task scope:** Focused on rotation; does not address grasping, tool use, or functional manipulation

## Inference / Deployment

- **Inference latency:** Not explicitly reported. The visuotactile transformer with DIGIT tactile encoder adds overhead compared to pure MLP policies, but should still run at ~20-50 Hz on a desktop GPU.
- **Deployment hardware:** Allegro Hand (16 DoF) with DIGIT tactile sensors on fingertips. Policy trained in IsaacGym; deployed via zero-shot sim-to-real transfer.
- **Real-time capable?** Yes. Demonstrated real-time in-hand rotation on real Allegro Hand with visuotactile input.
