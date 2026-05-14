### 7.4 RoboPianist

**전체 제목:** RoboPianist: Dexterous Piano Playing with Deep Reinforcement Learning

**저자:** Kevin Zakka, Philipp Wu, Laura Smith, Nimrod Gileadi, Taylor Howell, Xue Bin Peng, Sumeet Singh, Yuval Tassa, Pete Florence, Andy Zeng, Pieter Abbeel

**학회/연도:** CoRL 2023

**arXiv:** https://arxiv.org/abs/2304.04150

**Musical instrument differentiation:** Contribution is the benchmark (150 pieces, quantifiable metrics), not piano playing per se. The value lies in providing a standardized, diverse evaluation suite for high-DoF contact-rich RL with natural success metrics (note accuracy, timing). Sim-only.

**RL 알고리즘:** Model-free RL (MPO -- Maximum a Posteriori Policy Optimization, from DeepMind) with a musical-score-conditioned reward. Multi-objective reward balancing note accuracy, timing, and energy efficiency.

**핸드 하드웨어:** Anthropomorphic bimanual hands (simulated, based on human hand anatomy, ~46 DoF total)

**시뮬레이션 플랫폼:** MuJoCo (DeepMind)

**Sim2Real 여부:** No. Simulation-only benchmark.

**작업:** Piano playing of 150 classical pieces from the PIG dataset. The agent must play multi-voice piano pieces requiring independent finger control, bimanual coordination, and precise timing. Pieces range from simple scales to complex Chopin etudes.

**핵심 방법론:** RoboPianist formulates piano playing as a high-dimensional RL problem with ~46 DoF anthropomorphic hands. The observation includes the upcoming musical score (notes, timing), current hand proprioception, and key states. The reward penalizes missed notes, wrong notes, and timing errors while encouraging energy-efficient motions. The benchmark provides a standardized evaluation suite across 150 pieces of varying difficulty, enabling systematic comparison of RL algorithms for contact-rich coordination tasks.

**주요 기여:**
- Created a standardized benchmark for dexterous piano playing with 150 pieces, enabling reproducible evaluation of high-DoF RL
- Demonstrated that model-free RL can learn complex bimanual finger coordination for musical performance
- Open-sourced a high-quality MuJoCo piano environment with realistic key mechanics and a diverse repertoire

**한계점:** Simulation-only; no real-world piano playing demonstrated. Anthropomorphic hand model does not correspond to any commercially available robot hand. MPO algorithm from DeepMind is not as widely used as PPO.

**시뮬레이션 전용 한계:** 시뮬레이션에서만 평가됨; sim-to-real 전이 미입증, 실제 환경 실행 가능성 미검증.

**결과:** Successfully learned to play pieces of moderate difficulty (sim). Performance degraded on complex pieces requiring wide hand spans or rapid passages. Code and environments publicly available.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** PIG dataset (Piano Informatics for Genomics) -- 150 classical piano pieces providing musical scores as task specifications.
- **수집 방법:** Pure RL (MPO) in MuJoCo simulation. No demonstrations. Musical scores from PIG dataset define the target note sequences and timing. Agent learns from reward feedback (note accuracy, timing, energy efficiency). ~46 DoF anthropomorphic bimanual hands.
- **데이터 규모:** 150 classical pieces of varying difficulty (simple scales to complex Chopin etudes).
- **원격 조작 장비:** Not applicable (pure RL, no demonstrations).
- **데이터 포맷:** Musical scores (MIDI-like note sequences with timing). MuJoCo simulation environments.
- **공개 여부:** Yes -- MuJoCo piano environment, PIG dataset, and code publicly available.

## 추론 / 배포

- **추론 지연 시간:** Not applicable (simulation benchmark). Policy inference (MLP/LSTM) runs in <1ms per forward pass.
- **배포 하드웨어:** Simulation only (MuJoCo). No real-robot deployment.
- **실시간 가능 여부:** Not applicable (simulation benchmark; no real-robot deployment).
