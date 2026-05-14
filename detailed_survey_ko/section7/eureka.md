### 7.4 Eureka

**전체 제목:** Eureka: Human-Level Reward Design via Coding Large Language Models

**저자:** Yecheng Jason Ma, William Liang, Guanzhi Wang, De-An Huang, Osbert Bastani, Dinesh Jayaraman, Yuke Zhu, Linxi Fan, Anima Anandkumar

**학회/연도:** ICLR 2024

**arXiv:** https://arxiv.org/abs/2310.12931

**RL 알고리즘:** PPO (IsaacGym RL tasks); the LLM generates reward function code, which is used to train PPO policies. Evolutionary optimization over reward candidates with LLM-based mutation.

**핸드 하드웨어:** Shadow Hand (24 DoF) in simulation (pen spinning task); additional 9 robot morphologies across 29 environments

**시뮬레이션 플랫폼:** IsaacGym (NVIDIA GPU-accelerated RL environments)

**Sim2Real 여부:** No. All results are in simulation. The paper focuses on reward design, not sim-to-real transfer.

**작업:** 29 tasks across 10 robot morphologies. Flagship task: Shadow Hand pen spinning (first successful RL solution to this task). Other tasks include cartpole, quadruped locomotion, humanoid, and various manipulation benchmarks.

**핵심 방법론:** Uses GPT-4 to generate reward function code from environment source code and task descriptions. An evolutionary search proposes multiple reward candidates per iteration, trains RL policies for each, evaluates fitness, and feeds results back to the LLM for refinement. The LLM uses environment code (not natural language task descriptions) as context, enabling it to write executable reward functions. Optionally incorporates human feedback through natural language to refine rewards via in-context learning.

**주요 기여:**
- Proposed automated reward design via LLM code generation that outperforms manually designed reward functions on IsaacGym benchmarks across diverse RL tasks (83% of tasks, 52% average normalized improvement)
- First successful RL policy for Shadow Hand pen spinning in simulation (no real-world transfer), achieved by combining Eureka-generated rewards with curriculum learning
- Demonstrated that LLMs can generate reward functions from environment source code without domain-specific prompting
- Gradient-free in-context learning approach for incorporating human feedback into reward design

**정량적 결과:**

| Metric | Value |
|---|---|
| Tasks outperforming human rewards | 83% (29 tasks, 10 robot morphologies) |
| Average normalized improvement | 52% over expert human rewards |
| Pen spinning | First successful RL solution (Shadow Hand) |
| LLM used | GPT-4 |
| Reward candidates per iteration | Multiple (evolutionary search) |

**한계점:**
- **Force control:** No force/torque sensing or impedance control; all tasks use position-based control
- **VLA/Language:** Uses LLM for reward generation (not for policy); no language-conditioned policies
- **Sim2Real:** No real-world experiments; all results in simulation
- **Code:** [GitHub](https://github.com/eureka-research/Eureka) available
- **Compute:** Requires substantial GPU compute for parallel reward candidate evaluation and significant LLM API costs
- **Generalization:** Reward functions are task-specific; no cross-task transfer of reward designs
- All results are in simulation only; 'superhuman' comparisons are against manually designed reward functions in IsaacGym, not against human physical performance.

## 추론 / 배포

- **추론 지연 시간:** Not reported. The trained MLP policy runs in <1ms per forward pass. LLM reward generation is offline (not part of deployment).
- **배포 하드웨어:** Simulation only (IsaacGym). No real-robot deployment. LLM (GPT-4) used offline for reward function generation.
- **실시간 가능 여부:** Yes, for the trained policy (MLP inference is trivially fast). Eureka's contribution is reward generation, not inference optimization.
