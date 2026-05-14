### 7.1 DextrAH-G/RGB

**Full title:** DextrAH-G: Dexterous Arm-Hand Grasping with Geometric Fabrics

**Authors:** Maximilian Haas-Heger, Viktor Makoviychuk, Ankur Handa, et al.

**Venue/Year:** CoRL 2024

**RL algorithm:** PPO for grasp policy + geometric fabrics for arm motion planning; the RL policy controls the hand while geometric fabrics handle arm trajectory generation

**Hand hardware:** Allegro Hand (16 DoF) + Kuka arm

**Sim platform:** Isaac Lab (NVIDIA)

**Sim2Real?** Yes; demonstrated real-world arm-hand grasping with zero-shot transfer (real)

**Object count:** Multiple objects evaluated; specific count not reported in the table

**Tasks:** Coordinated arm-hand dexterous grasping -- reaching, pre-shaping, and grasping objects on a table

**Key methodology:** Combines a learned dexterous grasp policy (PPO) with geometric fabrics for arm motion planning. Geometric fabrics provide a reactive, geometry-aware motion generation framework that handles arm trajectory and obstacle avoidance, while the RL policy focuses on finger control for grasping. This separation of concerns simplifies the learning problem and enables modular sim-to-real transfer. DextrAH-RGB extends this to RGB-based perception.

**Main contributions:**
- Integration of geometric fabrics with learned dexterous grasping for coordinated arm-hand control
- Modular architecture separating arm planning (geometric fabrics) from hand control (RL), simplifying each subproblem
- Demonstrated sim-to-real transfer on Allegro + Kuka system (real); forms the basis of NVIDIA GR00T-Dexterity

**Limitations/Gaps:** Geometric fabrics require hand-tuned parameters; limited to grasping (no in-hand manipulation or tool use); the separation between arm and hand control may limit performance on tasks requiring tight arm-hand coordination; evaluation on a relatively small object set compared to UniDexGrasp/ResDex

## Inference / Deployment

- **Inference latency:** Not explicitly reported. The MLP hand policy runs in <1ms; geometric fabrics for arm control compute analytically in <1ms. Combined system supports high-frequency control.
- **Deployment hardware:** Allegro Hand (16 DoF) + Kuka arm. Policy trained in Isaac Lab; deployed via zero-shot sim-to-real transfer. Forms the basis of NVIDIA GR00T-Dexterity.
- **Real-time capable?** Yes. Both the MLP policy and geometric fabrics are computationally lightweight, supporting real-time arm-hand control on real hardware.

## Dataset / Data Collection

- **Dataset used:** No pre-collected dataset. Pure RL (PPO) for hand policy in Isaac Lab; geometric fabrics for arm motion (analytical, no learning).
- **Collection method:** Pure RL in Isaac Lab for dexterous grasp policy. Geometric fabrics provide reactive arm trajectory generation (no training data needed). Sim-to-real transfer via domain randomization. DextrAH-RGB extends to RGB-based perception.
- **Data scale:** Standard parallel RL training in Isaac Lab. Object set size not prominently reported.
- **Teleop equipment:** Not applicable (pure RL + analytical fabrics).
- **Data format:** Not applicable (online RL, no offline dataset).
- **Publicly available?** Forms basis of NVIDIA GR00T-Dexterity. Code release via Isaac Lab ecosystem.
