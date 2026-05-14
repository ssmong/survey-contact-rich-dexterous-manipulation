### 7.2 DeXtreme

**Full title:** DeXtreme: Transfer of Agile In-Hand Manipulation from Simulation to Reality

**Authors:** Ankur Handa, Arthur Allshire, Viktor Makoviychuk, Aleksei Petrenko, Ritvik Singh, Jingzhou Liu, Denys Makoviichuk, Karl Van Wyk, Alexander Zook, Yashraj Narang, Jean-Francois Lafleche, Dieter Fox, Gavriel State

**Venue/Year:** ICRA 2023 (arXiv 2022)

**RL algorithm:** PPO (large-scale parallel training in IsaacGym); uses automatic domain randomization (ADR) that dynamically expands randomization ranges during training

**Hand hardware:** Allegro Hand (16 DoF)

**Sim platform:** IsaacGym

**Sim2Real?** Yes; automatic domain randomization (ADR) for sim-to-real transfer (real). ADR adaptively increases randomization ranges during training when policy performance is sufficient, pushing the policy toward broader robustness. Complemented by randomized visual observations

**Object count:** Cube and other simple objects; focus on transfer quality rather than object diversity

**Tasks:** In-hand cube rotation to target orientations (building on the OpenAI Rubik's cube lineage)

**Key methodology:** Extends NVIDIA's IsaacGym-based training to Allegro Hand with Automatic Domain Randomization (ADR). ADR starts with narrow randomization ranges and progressively widens them as the policy learns, avoiding the issue of overly-challenging initial randomization that prevents learning. The system trains at massive scale (thousands of parallel environments) and achieves robust sim-to-real transfer without manual domain randomization tuning.

**Main contributions:**
- Automatic Domain Randomization (ADR) that eliminates manual tuning of randomization ranges
- First demonstration of sim-to-real in-hand manipulation on Allegro Hand (real) (prior work used Shadow Hand)
- Massive-scale parallel training infrastructure enabling rapid policy iteration

**Limitations/Gaps:** Limited to simple objects (primarily cubes); Allegro Hand only; no tactile sensing; ADR training is computationally expensive; limited to reorientation tasks without translation or functional manipulation goals

## Inference / Deployment

- **Inference latency:** Not explicitly reported. The MLP policy runs in <1ms per forward pass, enabling high-frequency control.
- **Deployment hardware:** Allegro Hand (16 DoF). Policy trained in IsaacGym at massive scale; deployed via zero-shot sim-to-real transfer with ADR.
- **Real-time capable?** Yes. MLP-based RL policies are trivially fast for real-time dexterous control. Demonstrated on real Allegro Hand.

## Dataset / Data Collection

- **Dataset used:** No pre-collected dataset. Pure RL (PPO) with Automatic Domain Randomization (ADR) -- all data generated in simulation.
- **Collection method:** Pure RL in IsaacGym at massive scale (thousands of parallel environments). ADR adaptively widens randomization ranges as policy performance improves. No demonstrations. Zero-shot sim-to-real transfer on Allegro Hand.
- **Data scale:** Massive-scale parallel training. Cube and simple objects for training/evaluation.
- **Teleop equipment:** Not applicable (pure RL, no demonstrations).
- **Data format:** Not applicable (online RL, no offline dataset).
- **Publicly available?** Code release status not reported.
