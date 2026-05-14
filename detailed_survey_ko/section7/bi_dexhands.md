### 7.3 Bi-DexHands

**Type: Benchmark + baseline method**

**전체 제목:** Towards Human-Level Bimanual Dexterous Manipulation with Reinforcement Learning

**저자:** Yuanpei Chen, Tianhao Wu, Shengjie Wang, Xidong Feng, Jiechuan Jiang, Zongqing Lu, Stephen McAleer, Hao Dong, Song-Chun Zhu, Yaodong Yang

**학회/연도:** NeurIPS 2022 (Datasets and Benchmarks Track)

**arXiv:** https://arxiv.org/abs/2206.08686

**RL 알고리즘:** Comprehensive benchmark supporting multiple RL algorithms: PPO, SAC, TRPO, MAPPO, HAPPO, MADDPG. Also supports offline RL (BCQ, CQL, TD3+BC) and multi-agent RL formulations.

**핸드 하드웨어:** 2x Shadow Hands (48 DoF total, 24 per hand)

**시뮬레이션 플랫폼:** IsaacGym (NVIDIA GPU-accelerated)

**Sim2Real 여부:** No. Simulation-only benchmark.

**작업:** 16+ bimanual dexterous tasks organized by difficulty: (1) simple tasks -- hand-over, catch underarm, two-catch underarm; (2) moderate tasks -- over-arm catch, pen twirling, door open/close, push block, scissors, swing cup; (3) complex tasks -- re-orientation, grasp-and-place, stack blocks, pour water, lift pot. Tasks involve coordinated bimanual contact-rich manipulation.

**핵심 방법론:** Bi-DexHands formulates bimanual manipulation as both single-agent and multi-agent RL problems, enabling systematic comparison of centralized vs. decentralized training. The benchmark provides standardized reward functions, observation spaces, and evaluation protocols for each task. GPU-parallelized environments in IsaacGym enable training thousands of environments simultaneously.

**주요 기여:**
- Created the first large-scale bimanual dexterous manipulation benchmark with 16+ tasks of varying difficulty
- Systematically compared single-agent RL, multi-agent RL, and offline RL algorithms on the same task suite
- Found that multi-agent RL (especially HAPPO) can match or outperform single-agent methods on bimanual tasks while offering better scalability

**정량적 결과:**

| Algorithm | Relative performance |
|---|---|
| HAPPO | Best overall across tasks |
| PPO | Competitive on simpler tasks |
| Offline RL (BCQ, CQL, TD3+BC) | Significant gap vs online methods |

All results are simulation-only (sim).

**한계점:** Simulation-only with no sim-to-real transfer. Shadow Hands are expensive and rarely used in real-world labs. Tasks use privileged state observations (object pose, velocity), not vision. No force/tactile sensing modeled.

**시뮬레이션 전용 한계:** 시뮬레이션에서만 평가됨; sim-to-real 전이 미입증, 실제 환경 실행 가능성 미검증.

**결과:** HAPPO achieved the best overall performance across tasks (sim). PPO remained competitive on simpler tasks. Offline RL methods showed significant performance gaps compared to online methods. Code and pretrained checkpoints released.

## 추론 / 배포

- **추론 지연 시간:** Not applicable (simulation benchmark). MLP policy inference runs in <1ms per forward pass.
- **배포 하드웨어:** Simulation only (IsaacGym). No real-robot deployment.
- **실시간 가능 여부:** Not applicable (simulation benchmark; no real-robot deployment).

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** No pre-collected dataset for online RL methods. Benchmark also supports offline RL using replay buffers from trained online policies.
- **수집 방법:** Pure RL (PPO, SAC, TRPO, MAPPO, HAPPO, MADDPG) in IsaacGym with GPU-parallelized environments. 16+ bimanual dexterous tasks with dual Shadow Hands (48 DoF total). Offline RL baselines (BCQ, CQL, TD3+BC) use replay buffers generated from online RL training.
- **데이터 규모:** 16+ tasks. Thousands of parallel environments in IsaacGym. Offline datasets generated from online RL rollouts.
- **원격 조작 장비:** Not applicable (pure RL benchmark).
- **데이터 포맷:** IsaacGym simulation data. Standardized reward functions and observation spaces per task.
- **공개 여부:** Yes -- code and pretrained checkpoints released. Benchmark environment publicly available.
