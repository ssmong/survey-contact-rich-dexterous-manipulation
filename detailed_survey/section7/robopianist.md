### 7.4 RoboPianist

**Full title:** RoboPianist: Dexterous Piano Playing with Deep Reinforcement Learning

**Authors:** Kevin Zakka, Philipp Wu, Laura Smith, Nimrod Gileadi, Taylor Howell, Xue Bin Peng, Sumeet Singh, Yuval Tassa, Pete Florence, Andy Zeng, Pieter Abbeel

**Venue/Year:** CoRL 2023

**arXiv:** https://arxiv.org/abs/2304.04150

**Musical instrument differentiation:** Contribution is the benchmark (150 pieces, quantifiable metrics), not piano playing per se. The value lies in providing a standardized, diverse evaluation suite for high-DoF contact-rich RL with natural success metrics (note accuracy, timing). Sim-only.

**RL algorithm:** Model-free RL (MPO -- Maximum a Posteriori Policy Optimization, from DeepMind) with a musical-score-conditioned reward. Multi-objective reward balancing note accuracy, timing, and energy efficiency.

**Hand hardware:** Anthropomorphic bimanual hands (simulated, based on human hand anatomy, ~46 DoF total)

**Sim platform:** MuJoCo (DeepMind)

**Sim2Real?** No. Simulation-only benchmark.

**Tasks:** Piano playing of 150 classical pieces from the PIG dataset. The agent must play multi-voice piano pieces requiring independent finger control, bimanual coordination, and precise timing. Pieces range from simple scales to complex Chopin etudes.

**Key methodology:** RoboPianist formulates piano playing as a high-dimensional RL problem with ~46 DoF anthropomorphic hands. The observation includes the upcoming musical score (notes, timing), current hand proprioception, and key states. The reward penalizes missed notes, wrong notes, and timing errors while encouraging energy-efficient motions. The benchmark provides a standardized evaluation suite across 150 pieces of varying difficulty, enabling systematic comparison of RL algorithms for contact-rich coordination tasks.

**Main contributions:**
- Created a standardized benchmark for dexterous piano playing with 150 pieces, enabling reproducible evaluation of high-DoF RL
- Demonstrated that model-free RL can learn complex bimanual finger coordination for musical performance
- Open-sourced a high-quality MuJoCo piano environment with realistic key mechanics and a diverse repertoire

**Limitations/Gaps:** Simulation-only; no real-world piano playing demonstrated. Anthropomorphic hand model does not correspond to any commercially available robot hand. MPO algorithm from DeepMind is not as widely used as PPO.

**Sim-only limitation:** Evaluated in simulation only; no sim-to-real transfer demonstrated, real-world viability unvalidated.

**Results:** Successfully learned to play pieces of moderate difficulty (sim). Performance degraded on complex pieces requiring wide hand spans or rapid passages. Code and environments publicly available.

## Dataset / Data Collection

- **Dataset used:** PIG dataset (Piano Informatics for Genomics) -- 150 classical piano pieces providing musical scores as task specifications.
- **Collection method:** Pure RL (MPO) in MuJoCo simulation. No demonstrations. Musical scores from PIG dataset define the target note sequences and timing. Agent learns from reward feedback (note accuracy, timing, energy efficiency). ~46 DoF anthropomorphic bimanual hands.
- **Data scale:** 150 classical pieces of varying difficulty (simple scales to complex Chopin etudes).
- **Teleop equipment:** Not applicable (pure RL, no demonstrations).
- **Data format:** Musical scores (MIDI-like note sequences with timing). MuJoCo simulation environments.
- **Publicly available?** Yes -- MuJoCo piano environment, PIG dataset, and code publicly available.

## Inference / Deployment

- **Inference latency:** Not applicable (simulation benchmark). Policy inference (MLP/LSTM) runs in <1ms per forward pass.
- **Deployment hardware:** Simulation only (MuJoCo). No real-robot deployment.
- **Real-time capable?** Not applicable (simulation benchmark; no real-robot deployment).
