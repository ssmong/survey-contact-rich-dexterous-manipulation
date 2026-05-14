### 7.3 Bi-DexHands

**Type: Benchmark + baseline method**

**Full title:** Towards Human-Level Bimanual Dexterous Manipulation with Reinforcement Learning

**Authors:** Yuanpei Chen, Tianhao Wu, Shengjie Wang, Xidong Feng, Jiechuan Jiang, Zongqing Lu, Stephen McAleer, Hao Dong, Song-Chun Zhu, Yaodong Yang

**Venue/Year:** NeurIPS 2022 (Datasets and Benchmarks Track)

**arXiv:** https://arxiv.org/abs/2206.08686

**RL algorithm:** Comprehensive benchmark supporting multiple RL algorithms: PPO, SAC, TRPO, MAPPO, HAPPO, MADDPG. Also supports offline RL (BCQ, CQL, TD3+BC) and multi-agent RL formulations.

**Hand hardware:** 2x Shadow Hands (48 DoF total, 24 per hand)

**Sim platform:** IsaacGym (NVIDIA GPU-accelerated)

**Sim2Real?** No. Simulation-only benchmark.

**Tasks:** 16+ bimanual dexterous tasks organized by difficulty: (1) simple tasks -- hand-over, catch underarm, two-catch underarm; (2) moderate tasks -- over-arm catch, pen twirling, door open/close, push block, scissors, swing cup; (3) complex tasks -- re-orientation, grasp-and-place, stack blocks, pour water, lift pot. Tasks involve coordinated bimanual contact-rich manipulation.

**Key methodology:** Bi-DexHands formulates bimanual manipulation as both single-agent and multi-agent RL problems, enabling systematic comparison of centralized vs. decentralized training. The benchmark provides standardized reward functions, observation spaces, and evaluation protocols for each task. GPU-parallelized environments in IsaacGym enable training thousands of environments simultaneously.

**Main contributions:**
- Created the first large-scale bimanual dexterous manipulation benchmark with 16+ tasks of varying difficulty
- Systematically compared single-agent RL, multi-agent RL, and offline RL algorithms on the same task suite
- Found that multi-agent RL (especially HAPPO) can match or outperform single-agent methods on bimanual tasks while offering better scalability

**Quantitative results:**

| Algorithm | Relative performance |
|---|---|
| HAPPO | Best overall across tasks |
| PPO | Competitive on simpler tasks |
| Offline RL (BCQ, CQL, TD3+BC) | Significant gap vs online methods |

All results are simulation-only (sim).

**Limitations/Gaps:** Simulation-only with no sim-to-real transfer. Shadow Hands are expensive and rarely used in real-world labs. Tasks use privileged state observations (object pose, velocity), not vision. No force/tactile sensing modeled.

**Sim-only limitation:** Evaluated in simulation only; no sim-to-real transfer demonstrated, real-world viability unvalidated.

**Results:** HAPPO achieved the best overall performance across tasks (sim). PPO remained competitive on simpler tasks. Offline RL methods showed significant performance gaps compared to online methods. Code and pretrained checkpoints released.

## Inference / Deployment

- **Inference latency:** Not applicable (simulation benchmark). MLP policy inference runs in <1ms per forward pass.
- **Deployment hardware:** Simulation only (IsaacGym). No real-robot deployment.
- **Real-time capable?** Not applicable (simulation benchmark; no real-robot deployment).

## Dataset / Data Collection

- **Dataset used:** No pre-collected dataset for online RL methods. Benchmark also supports offline RL using replay buffers from trained online policies.
- **Collection method:** Pure RL (PPO, SAC, TRPO, MAPPO, HAPPO, MADDPG) in IsaacGym with GPU-parallelized environments. 16+ bimanual dexterous tasks with dual Shadow Hands (48 DoF total). Offline RL baselines (BCQ, CQL, TD3+BC) use replay buffers generated from online RL training.
- **Data scale:** 16+ tasks. Thousands of parallel environments in IsaacGym. Offline datasets generated from online RL rollouts.
- **Teleop equipment:** Not applicable (pure RL benchmark).
- **Data format:** IsaacGym simulation data. Standardized reward functions and observation spaces per task.
- **Publicly available?** Yes -- code and pretrained checkpoints released. Benchmark environment publicly available.
