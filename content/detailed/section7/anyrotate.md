### 7.2 AnyRotate

**Full title:** AnyRotate: Gravity-Invariant In-Hand Object Rotation with Sim-to-Real Touch

**Authors:** Max Yang, Chenghua Lu, Alex Church, Yijiong Lin, Chris Li, Efi Psomopoulou, Nathan F. Lepora

**Venue/Year:** CoRL 2024

**Hora/RotateIt/AnyRotate evolutionary chain:** Extends the Hora/RotateIt framework with gravity randomization; the RL algorithm (PPO+RMA) is inherited from Hora. The primary novelty is training across randomized gravity directions to enable rotation with any hand orientation, plus the finding that tactile sensing is essential for gravity-invariant rotation (proprioception-only fails in non-palm-up orientations).

**RL algorithm:** PPO with tactile-conditioned policy; extends tactile in-hand rotation to arbitrary gravity directions (gravity-invariant)

**Hand hardware:** Allegro Hand (16 DoF) + tactile sensors (TacTip-based)

**Sim platform:** IsaacGym

**Sim2Real?** Yes; sim-to-real with tactile domain randomization across varied hand orientations (real)

**Object count:** Multiple objects evaluated in various orientations

**Tasks:** Gravity-invariant in-hand object rotation -- continuous rotation with the hand held at arbitrary orientations (palm-up, palm-down, sideways)

**Key methodology:** Addresses a key limitation of prior work (Hora, RotateIt) which assumes a palm-up hand configuration. Trains the rotation policy across randomized gravity directions relative to the hand, using tactile feedback to maintain stable contact regardless of gravity orientation. The tactile signal provides critical contact state information when gravity is not aligned with the palm, where proprioception alone is insufficient.

**Main contributions:**
- First gravity-invariant in-hand rotation policy, enabling rotation with any hand orientation (real)
- Demonstrated that tactile sensing is essential for gravity-invariant rotation (proprioception-only fails in non-palm-up orientations)
- Sim-to-real transfer across hand orientations not seen during real-world training (real)

**Limitations/Gaps:** Still single-axis rotation; limited object diversity in real-world evaluation; custom tactile sensor setup may not generalize to other sensor types; no code publicly released at time of survey

## Inference / Deployment

- **Inference latency:** Not explicitly reported. The tactile-conditioned MLP policy runs in <1ms per forward pass.
- **Deployment hardware:** Allegro Hand (16 DoF) + TacTip-based tactile sensors. Policy trained in IsaacGym; deployed via zero-shot sim-to-real transfer across varied hand orientations.
- **Real-time capable?** Yes. MLP-based policy with tactile conditioning supports real-time control. Demonstrated on real Allegro Hand in multiple orientations.

## Dataset / Data Collection

- **Dataset used:** No pre-collected dataset. Pure RL (PPO) with tactile-conditioned policy and gravity randomization -- all data generated in simulation.
- **Collection method:** Pure RL in IsaacGym extending Hora/RotateIt framework. Gravity direction randomized during training. Tactile feedback (TacTip-based) for contact state in varied hand orientations. Sim-to-real via tactile domain randomization.
- **Data scale:** Standard parallel RL training in IsaacGym. Multiple objects in various orientations.
- **Teleop equipment:** Not applicable (pure RL, no demonstrations).
- **Data format:** Not applicable (online RL, no offline dataset).
- **Publicly available?** No code publicly released at time of survey.
