### 7.2 RotateIt

**Full title:** RotateIt: Tactile Rotary In-Hand Manipulation with Sim-to-Real Touch

**Authors:** Haozhi Qi, Brent Yi, Sudharshan Suresh, Michael Lambeta, Yi Ma, Roberto Calandra, Jitendra Malik

**Venue/Year:** CoRL 2023

**Hora/RotateIt/AnyRotate evolutionary chain:** Core RL (PPO+RMA) and hand (Allegro) unchanged from Hora; the primary contribution is the addition of DIGIT tactile sensing for rotation direction and slip detection. The RL algorithm, reward structure, and adaptation mechanism are inherited from Hora.

**RL algorithm:** PPO with tactile-informed policy; extends Hora with tactile sensing (DIGIT sensors) for rotation direction and slip detection

**Hand hardware:** Allegro Hand (16 DoF) + DIGIT tactile sensors on fingertips

**Sim platform:** IsaacGym

**Sim2Real?** Yes; sim-to-real with tactile domain randomization (real). Calibrates simulated tactile signals to real DIGIT sensor outputs, enabling zero-shot transfer of tactile-conditioned policies

**Object count:** Evaluated on diverse objects; specific count not reported but includes geometrically varied objects

**Tasks:** Tactile-guided in-hand rotation; continuous rotation of objects using fingertip tactile feedback for slip detection and rotation direction sensing

**Key methodology:** Augments the Hora framework with DIGIT optical tactile sensors on the Allegro Hand fingertips. A tactile encoder processes simulated tactile images alongside proprioceptive state. The key insight is that tactile sensing provides direct contact information that disambiguates object state more reliably than proprioception alone, particularly for detecting rotational slip. Tactile sim-to-real is addressed via randomized tactile signal augmentation.

**Main contributions:**
- First integration of optical tactile sensing (DIGIT) with RL-based in-hand rotation on a real dexterous hand (real)
- Tactile sim-to-real transfer pipeline with calibrated DIGIT simulation
- Demonstrated that tactile feedback improves rotation robustness over proprioception-only baselines (Hora)

**Limitations/Gaps:** Still limited to single-axis rotation; DIGIT sensors add cost and fragility; tactile sim-to-real gap remains (simulated tactile is simplified compared to real optical signals); limited to rigid objects

## Inference / Deployment

- **Inference latency:** Not explicitly reported. The tactile-conditioned MLP policy runs in <1ms per forward pass. Tactile image processing (DIGIT sensor) adds minor overhead.
- **Deployment hardware:** Allegro Hand (16 DoF) + DIGIT tactile sensors. Policy trained in IsaacGym; deployed via zero-shot sim-to-real transfer.
- **Real-time capable?** Yes. MLP-based policy with tactile conditioning is fast enough for real-time dexterous control on real hardware.

## Dataset / Data Collection

- **Dataset used:** No pre-collected dataset. Pure RL (PPO) with tactile-informed policy -- all data generated in simulation with sim-to-real transfer.
- **Collection method:** Pure RL in IsaacGym extending Hora framework. Tactile encoder processes simulated DIGIT tactile images alongside proprioceptive state. Tactile sim-to-real via randomized tactile signal augmentation and DIGIT calibration.
- **Data scale:** Standard parallel RL training in IsaacGym. Diverse objects evaluated.
- **Teleop equipment:** Not applicable (pure RL, no demonstrations).
- **Data format:** Not applicable (online RL, no offline dataset).
- **Publicly available?** Code release status not reported.
