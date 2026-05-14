### 7.2 Dactyl (OpenAI)

**Full title:** Learning Dexterous In-Hand Manipulation

**Authors:** Marcin Andrychowicz, Bowen Baker, Maciek Chociej, Rafal Jozefowicz, Bob McGrew, Jakub Pachocki, Arthur Petron, Matthias Plappert, Glenn Powell, Alex Ray, Jonas Schneider, Szymon Sidor, Josh Tobin, Peter Welinder, Lilian Weng, Wojciech Zaremba (OpenAI)

**Venue/Year:** arXiv 2018 (1808.00177); extended version in IJRR 2020

**arXiv:** https://arxiv.org/abs/1808.00177

**RL algorithm:** PPO (distributed, same system as OpenAI Five); LSTM policy with asymmetric actor-critic (privileged info in critic)

**Hand hardware:** Shadow Dexterous Hand (24 DoF) mounted on a fixed base

**Sim platform:** MuJoCo (custom OpenAI simulation environment)

**Sim2Real?** Yes. Massive automatic domain randomization (ADR) over 50+ physical parameters (friction, mass, gravity, actuator gains, observation noise, etc.). Policies trained entirely in simulation transfer zero-shot to real Shadow Hand. Vision-based variant uses randomized visual appearances for sim2real of perception.

**Tasks:** In-hand object reorientation: rotating a cube to achieve a target face orientation. The block must be reoriented to match a sequence of randomly sampled goal orientations.

**Key methodology:** Trains a recurrent RL policy (LSTM + PPO) in simulation with extensive automatic domain randomization across physics parameters, visual appearances, and observation noise. The key insight is that sufficient randomization of simulation parameters produces policies robust enough for zero-shot sim-to-real transfer. The LSTM implicitly performs system identification from interaction history, adapting to real-world dynamics without explicit calibration.

**Main contributions:**
- First demonstration of sim-to-real RL for dexterous in-hand manipulation on a physical anthropomorphic hand (Shadow Hand)
- Introduced automatic domain randomization (ADR) as a scalable sim2real methodology for high-DoF manipulation
- Demonstrated emergent dexterous behaviors (finger gaiting, finger pivoting, multi-finger coordination) learned purely from RL without demonstrations
- Established sim-to-real domain randomization as a viable methodology for high-DoF dexterous manipulation, influencing subsequent work (Hora, DeXtreme, DexPBT, etc.)

**Quantitative results:**

| Metric | Value |
|---|---|
| Consecutive successful rotations | 50 in a row (real) |
| Face reorientation success | ~100% for trained goal set (sim); Quantitative real-world success rate not explicitly reported beyond the 50-consecutive-rotation demonstration. |
| Domain randomization parameters | 50+ randomized dimensions |
| Hand DoF | 24 (Shadow Dexterous Hand) |
| Training | ~100 years of simulated experience (distributed) |

**Limitations/Gaps:**
- **Force control:** No force/torque sensing or impedance control; position-only actuation
- **VLA/Language:** No vision-language integration; purely state-based or vision-based RL
- **Sim2Real:** Requires massive compute for domain randomization; ADR does not guarantee coverage of all real-world conditions
- **Code:** Not publicly released; the Shadow Hand hardware is expensive (~$100K+), limiting reproducibility
- **Task scope:** Limited to block rotation; does not generalize to diverse objects or functional manipulation
- **Sensing:** No tactile feedback; relies on fingertip position sensing and (optionally) RGB vision
- Trained on a single cube only; no object shape generalization
- Requires massive distributed compute (~100 years of simulated experience, ~6000 CPU cores); not reproducible by most labs
- Shadow Hand costs ~$100K+, limiting reproduction

## Inference / Deployment

- **Inference latency:** Not explicitly reported. The LSTM policy runs in <5ms per forward pass including recurrent state update. The system ran at real-time control rates on the Shadow Hand.
- **Deployment hardware:** Shadow Dexterous Hand (24 DoF) on a fixed base. Policy trained in MuJoCo with massive distributed compute; deployed via zero-shot sim-to-real transfer with ADR.
- **Real-time capable?** Yes. Demonstrated real-time in-hand object rotation on the physical Shadow Hand. The LSTM policy supports real-time control at the Shadow Hand's native servo rate.
