### 7.2 Hora

**Full title:** In-Hand Object Rotation via Rapid Motor Adaptation

**Authors:** Haozhi Qi, Ashish Kumar, Roberto Calandra, Yi Ma, Jitendra Malik

**Venue/Year:** CoRL 2022

**RL algorithm:** PPO with rapid motor adaptation (RMA); trains a base policy and an online adaptation module that infers environment parameters from recent interaction history

**Hand hardware:** Allegro Hand (16 DoF)

**Sim platform:** IsaacGym Preview 4

**Sim2Real?** Yes; zero-shot sim-to-real transfer using RMA for online adaptation (real). Domain randomization over physical parameters (mass, friction, scale) during training; the adaptation module infers these parameters at deployment from proprioceptive history

**Object count:** Multiple objects including cubes, cylinders, and YCB objects; evaluated on ~10+ objects in the real world

**Tasks:** Continuous in-hand object rotation around a specified axis (z-axis rotation of objects held in the palm)

**Key methodology:** Builds on Rapid Motor Adaptation (RMA) for in-hand manipulation. A base policy is trained with PPO in simulation across randomized environments. An adaptation module (small MLP) is trained to predict latent environment parameters from a short history of proprioceptive observations. At deployment, the adaptation module provides implicit system identification, enabling the policy to adapt to real-world dynamics without explicit calibration.

**Main contributions:**
- First demonstration of rapid motor adaptation for dexterous in-hand rotation on real Allegro Hand (real)
- Online adaptation eliminates the need for manual system identification or hand-tuned domain randomization
- Robust zero-shot transfer across diverse object shapes and sizes on real hardware (real)

**Limitations/Gaps:** Limited to single-axis rotation (not arbitrary SE(3) reorientation); relies on proprioception only (no vision or tactile); objects must remain in a palm-up configuration; limited to rigid objects

## Inference / Deployment

- **Inference latency:** Not explicitly reported. The MLP policy with RMA adaptation module runs in <1ms per forward pass, enabling high-frequency control.
- **Deployment hardware:** Allegro Hand (16 DoF). Policy trained in IsaacGym; deployed via zero-shot sim-to-real transfer with online RMA adaptation. MLP policy is lightweight enough for any compute platform.
- **Real-time capable?** Yes. MLP-based RL policy with lightweight RMA module runs at real-time rates on the Allegro Hand.

## Dataset / Data Collection

- **Dataset used:** No pre-collected dataset. Pure RL (PPO) with rapid motor adaptation (RMA) -- all data generated in simulation.
- **Collection method:** Pure RL in IsaacGym with domain randomization over physical parameters (mass, friction, scale). Online adaptation module trained from proprioceptive history. Zero-shot sim-to-real transfer. Cubes, cylinders, and YCB objects.
- **Data scale:** Standard parallel RL training in IsaacGym. ~10+ objects evaluated in real world.
- **Teleop equipment:** Not applicable (pure RL, no demonstrations).
- **Data format:** Not applicable (online RL, no offline dataset).
- **Publicly available?** Code release status not reported.
