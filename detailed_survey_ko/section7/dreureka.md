### 7.4 DrEureka

**전체 제목:** DrEureka: Language Model Guided Sim-To-Real Transfer

**저자:** Yecheng Jason Ma, William Liang, Hung-Ju Wang, Sam Wang, Yuke Zhu, Linxi Fan, Osbert Bastani, Dinesh Jayaraman

**학회/연도:** RSS 2024

**arXiv:** https://arxiv.org/abs/2406.01967

**RL 알고리즘:** PPO for policy training; LLM (GPT-4) generates both reward functions and domain randomization distributions. Extends Eureka by adding automated sim-to-real configuration.

**핸드 하드웨어:** Shadow Hand (simulation, dexterous manipulation tasks); Unitree Go1 (quadruped locomotion tasks, real-world)

**시뮬레이션 플랫폼:** IsaacGym

**Sim2Real 여부:** Yes. Key contribution is automating sim-to-real transfer configuration. The LLM generates domain randomization parameter distributions (ranges for mass, friction, motor gains, etc.) alongside reward functions, eliminating manual DR tuning. Demonstrated real-world transfer on quadruped locomotion (balancing on yoga ball) and dexterous manipulation.

**작업:** Quadruped locomotion (walking, balancing on yoga ball -- novel task) and dexterous manipulation tasks. The yoga ball balancing task is a novel real-world demonstration that had not been previously solved.

**핵심 방법론:** Extends Eureka from reward-only generation to full sim-to-real pipeline automation. Given environment source code and a task description, GPT-4 generates: (1) reward functions (as in Eureka) and (2) domain randomization distributions specifying the ranges of physics parameters to randomize during training. This eliminates the two most labor-intensive components of sim-to-real RL: reward engineering and domain randomization tuning. The LLM reasons about which physical parameters are relevant and proposes reasonable randomization ranges based on physical intuition encoded in its training data.

**주요 기여:**
- Proposed automating both reward design and domain randomization via LLMs, extending Eureka to the sim-to-real setting
- Achieved competitive or superior sim-to-real performance compared to human-designed configurations on standard benchmarks
- Solved novel real-world tasks (quadruped yoga ball balancing) without any manual sim-to-real tuning
- Extended the Eureka framework from simulation-only to real-world deployment

**정량적 결과:**

| Metric | Value |
|---|---|
| Sim2Real method | LLM-generated domain randomization |
| LLM used | GPT-4 |
| Real-world tasks | Quadruped yoga ball balancing, dexterous manipulation |
| vs. human-designed DR | Competitive or superior |
| Manual tuning required | None (fully automated) |

**한계점:**
- **Force control:** No force/impedance control; position-based actuation only
- **VLA/Language:** LLM used as a tool for configuration (not for policy); no language-conditioned policies
- **Sim2Real:** LLM-proposed DR ranges are not guaranteed to cover real-world conditions; relies on LLM's physical intuition
- **Code:** [GitHub](https://github.com/eureka-research/DrEureka) available
- **Dexterous results:** Real-world dexterous manipulation results less extensively validated than locomotion results
- **Compute:** Inherits Eureka's compute requirements plus sim-to-real training overhead

> **Note:** The primary real-world demonstration is a locomotion task (quadruped yoga ball balancing); dexterous manipulation results are less extensively validated.

## 추론 / 배포

- **추론 지연 시간:** Not reported. The trained MLP policy runs in <1ms per forward pass. LLM-based reward and DR generation is offline.
- **배포 하드웨어:** Real-world deployment demonstrated (quadruped locomotion on Unitree Go1; dexterous manipulation on Shadow Hand). LLM (GPT-4) used offline only.
- **실시간 가능 여부:** Yes. The deployed MLP policy supports real-time control. LLM is only used during the offline training configuration phase.
