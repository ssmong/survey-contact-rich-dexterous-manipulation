### 7.2 DeXtreme

**전체 제목:** DeXtreme: Transfer of Agile In-Hand Manipulation from Simulation to Reality

**저자:** Ankur Handa, Arthur Allshire, Viktor Makoviychuk, Aleksei Petrenko, Ritvik Singh, Jingzhou Liu, Denys Makoviichuk, Karl Van Wyk, Alexander Zook, Yashraj Narang, Jean-Francois Lafleche, Dieter Fox, Gavriel State

**학회/연도:** ICRA 2023 (arXiv 2022)

**RL 알고리즘:** PPO (large-scale parallel training in IsaacGym); uses automatic domain randomization (ADR) that dynamically expands randomization ranges during training

**핸드 하드웨어:** Allegro Hand (16 DoF)

**시뮬레이션 플랫폼:** IsaacGym

**Sim2Real 여부:** Yes; automatic domain randomization (ADR) for sim-to-real transfer (real). ADR adaptively increases randomization ranges during training when policy performance is sufficient, pushing the policy toward broader robustness. Complemented by randomized visual observations

**객체 수:** Cube and other simple objects; focus on transfer quality rather than object diversity

**작업:** In-hand cube rotation to target orientations (building on the OpenAI Rubik's cube lineage)

**핵심 방법론:** Extends NVIDIA's IsaacGym-based training to Allegro Hand with Automatic Domain Randomization (ADR). ADR starts with narrow randomization ranges and progressively widens them as the policy learns, avoiding the issue of overly-challenging initial randomization that prevents learning. The system trains at massive scale (thousands of parallel environments) and achieves robust sim-to-real transfer without manual domain randomization tuning.

**주요 기여:**
- Automatic Domain Randomization (ADR) that eliminates manual tuning of randomization ranges
- First demonstration of sim-to-real in-hand manipulation on Allegro Hand (real) (prior work used Shadow Hand)
- Massive-scale parallel training infrastructure enabling rapid policy iteration

**한계점:** Limited to simple objects (primarily cubes); Allegro Hand only; no tactile sensing; ADR training is computationally expensive; limited to reorientation tasks without translation or functional manipulation goals

## 추론 / 배포

- **추론 지연 시간:** Not explicitly reported. The MLP policy runs in <1ms per forward pass, enabling high-frequency control.
- **배포 하드웨어:** Allegro Hand (16 DoF). Policy trained in IsaacGym at massive scale; deployed via zero-shot sim-to-real transfer with ADR.
- **실시간 가능 여부:** Yes. MLP-based RL policies are trivially fast for real-time dexterous control. Demonstrated on real Allegro Hand.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** No pre-collected dataset. Pure RL (PPO) with Automatic Domain Randomization (ADR) -- all data generated in simulation.
- **수집 방법:** Pure RL in IsaacGym at massive scale (thousands of parallel environments). ADR adaptively widens randomization ranges as policy performance improves. No demonstrations. Zero-shot sim-to-real transfer on Allegro Hand.
- **데이터 규모:** Massive-scale parallel training. Cube and simple objects for training/evaluation.
- **원격 조작 장비:** Not applicable (pure RL, no demonstrations).
- **데이터 포맷:** Not applicable (online RL, no offline dataset).
- **공개 여부:** Code release status not reported.
