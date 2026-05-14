### DexWM: Dexterous World Models for Multi-Finger Hand-Object Interaction

**Full title:** World Models for Dexterous Manipulation

**Authors:** Qichen Fu, Haoyu Xiong, Yian Wang, Xingyu Lin, Lerrel Pinto (Meta FAIR / NYU)

**Venue/Year:** arXiv 2025

**Architecture:** DexWM introduces a learned world model specifically designed for dexterous hand-object interaction. The architecture consists of: (1) an observation encoder that processes multi-view images and proprioceptive state (hand joint positions), (2) a latent dynamics model (transformer-based) that predicts future latent states given actions, and (3) a policy decoder that generates dexterous hand actions. The world model is trained to predict future visual observations and proprioceptive states, enabling planning and imagination-based policy improvement. Used alongside an Allegro hand (16 DoF) + Franka arm (7 DoF).

**Action space:** 23D (16-DoF Allegro hand joint positions + 7-DoF Franka arm joint positions). Continuous actions generated via the policy decoder.

**Dex hand support?** ✅ --- Explicitly designed for and evaluated on the Allegro hand (16 DoF) mounted on a Franka Panda arm.

**Force/impedance output?** ✗ --- Joint position targets only. The world model does not explicitly model contact forces.

**Key methodology:** DexWM addresses the challenge that model-free RL for dexterous manipulation requires millions of environment interactions. By learning a world model of hand-object interaction dynamics, the policy can be improved via imagined rollouts in the learned model, dramatically reducing the need for real or simulated environment interaction. The world model learns to capture the complex contact dynamics between multiple fingers and objects, including grasping, in-hand rotation, and object transfer. Key to the approach is a contact-aware latent representation that captures the discrete nature of contact events.

**Training data:** Simulation data from the Allegro + Franka system in MuJoCo/Isaac, combined with real-world manipulation data. The world model is trained on diverse hand-object interaction trajectories.

**Main contributions:**
- Proposes a world model explicitly designed for multi-finger dexterous hand-object interaction, capturing complex contact dynamics in a learned latent space.
- Demonstrated that planning in the learned world model achieves sample-efficient dexterous manipulation.
- Showed that the world model transfers across different objects without retraining.

**Quantitative results:**

| Benchmark / Task | DexWM | Model-Free RL | Notes |
|---|---|---|---|
| *(Consult the arXiv paper for per-task results on Allegro hand manipulation benchmarks including grasping, in-hand rotation, and object transfer.)* | | | |

**Limitations/Gaps:**
- World model prediction accuracy degrades over long horizons, particularly for novel contact configurations not seen during training.
- No language conditioning; task objectives are encoded implicitly.
- Neither code nor weights have been publicly released.
- Contact dynamics in the learned model are approximate; the world model does not explicitly represent contact forces or friction.

**Open weights/code:** ✗ --- Not publicly released as of May 2026.

## Inference / Deployment

- **Inference latency:** Not reported. The world model (transformer-based latent dynamics) requires multi-step rollouts for planning, which compounds inference cost. Policy inference from the decoder is fast, but planning in the learned world model adds latency proportional to the planning horizon and number of candidate trajectories evaluated.
- **Deployment hardware:** Allegro Hand (16 DoF) + Franka arm (7 DoF). GPU for world model inference and planning not specified.
- **Real-time capable?** Limited. Planning in the world model (imagined rollouts) is computationally expensive due to multi-step forward prediction. The policy decoder alone is fast, but the full planning loop may limit control frequency to ~5-10 Hz depending on planning horizon and compute hardware.

## Dataset / Data Collection

- **Dataset used:** Custom simulation and real-world hand-object interaction data for Allegro hand (16 DoF) + Franka arm (7 DoF).
- **Collection method:** Simulation data from MuJoCo/Isaac for world model training, combined with real-world manipulation data. Diverse hand-object interaction trajectories including grasping, in-hand rotation, and object transfer.
- **Data scale:** Not reported. Sufficient data for training a transformer-based latent dynamics model.
- **Teleop equipment:** Not specified. Real-world data collection method not detailed.
- **Data format:** Multi-view images + proprioceptive state (23D joint positions) + action sequences.
- **Publicly available?** No. Neither code, weights, nor data released.

---
