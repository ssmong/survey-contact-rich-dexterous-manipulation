### 7.4 DexDrummer

**Full title:** DexDrummer: Dexterous Drumming via Reinforcement Learning

**Authors:** Hao-Chun Fang, Kenneth Shaw, Deepak Pathak, et al. (Stanford)

**Venue/Year:** arXiv 2026

**arXiv:** https://arxiv.org/abs/2603.22263

**Musical instrument differentiation:** Distinguished by tool grasping (drumstick) and impact force control. Unlike piano playing (RoboPianist, HandelBot) where fingers directly contact keys, drumming requires holding tools and generating controlled impact forces on drum surfaces -- combining grasp stability with dynamic striking. Sim-only.

**RL algorithm:** PPO with musical-score-conditioned rewards. Similar framework to HandelBot but adapted for percussion. Requires learning to generate impact forces on drum surfaces.

**Hand hardware:** Bimanual dexterous hands (holding drumsticks)

**Sim platform:** IsaacGym / MuJoCo

**Sim2Real?** No (simulation results; real-world transfer not reported in initial preprint).

**Tasks:** Drumming -- striking drum surfaces at correct times with correct intensity according to musical scores. Involves holding drumsticks (tool use), rapid contact-rich impacts, bimanual coordination, and dynamic force control.

**Key methodology:** DexDrummer extends musical instrument playing to percussion, which introduces additional challenges beyond piano: the agent must hold tools (drumsticks), generate controlled impact forces (not just key presses), and coordinate rapid bimanual alternating strikes. The contact dynamics of stick-on-drum impacts are more violent and dynamic than piano key presses, requiring robust contact handling in simulation.

**Main contributions:**
- Extended dexterous musical manipulation to percussion/drumming, requiring tool-use and impact force control
- Demonstrated that RL can learn dynamic striking motions with held tools, combining grasping stability with impact generation
- Addressed bimanual coordination for alternating and simultaneous strikes

**Limitations/Gaps:** No real-world transfer demonstrated. Drumstick grasping stability during rapid striking is a significant sim-to-real challenge. Limited rhythmic complexity in evaluation.

**Sim-only limitation:** Evaluated in simulation only; no sim-to-real transfer demonstrated, real-world viability unvalidated.

**Results:** Achieved successful drumming in simulation with correct timing and force patterns (sim). Code publicly available.

## Dataset / Data Collection

- **Dataset used:** Musical scores for percussion as task specifications. No pre-collected robot demonstration dataset.
- **Collection method:** Pure RL (PPO) with musical-score-conditioned rewards in IsaacGym/MuJoCo. Bimanual dexterous hands holding drumsticks. Agent learns tool grasping, impact force generation, and timing from reward feedback. Simulation only.
- **Data scale:** Musical scores of varying difficulty. Standard parallel RL training.
- **Teleop equipment:** Not applicable (pure RL, no demonstrations).
- **Data format:** Musical scores (percussion note sequences with timing).
- **Publicly available?** Code publicly available.

## Inference / Deployment

- **Inference latency:** Not reported. The MLP policy runs in <1ms per forward pass.
- **Deployment hardware:** Simulation only (IsaacGym/MuJoCo). No real-robot deployment demonstrated.
- **Real-time capable?** Yes, for the policy itself (MLP inference is trivially fast). However, only simulation evaluation was performed.
