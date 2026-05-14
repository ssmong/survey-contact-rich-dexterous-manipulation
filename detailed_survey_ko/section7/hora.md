### 7.2 Hora

**전체 제목:** In-Hand Object Rotation via Rapid Motor Adaptation

**저자:** Haozhi Qi, Ashish Kumar, Roberto Calandra, Yi Ma, Jitendra Malik

**학회/연도:** CoRL 2022

**RL 알고리즘:** PPO with rapid motor adaptation (RMA); trains a base policy and an online adaptation module that infers environment parameters from recent interaction history

**핸드 하드웨어:** Allegro Hand (16 DoF)

**시뮬레이션 플랫폼:** IsaacGym Preview 4

**Sim2Real 여부:** Yes; zero-shot sim-to-real transfer using RMA for online adaptation (real). Domain randomization over physical parameters (mass, friction, scale) during training; the adaptation module infers these parameters at deployment from proprioceptive history

**객체 수:** Multiple objects including cubes, cylinders, and YCB objects; evaluated on ~10+ objects in the real world

**작업:** Continuous in-hand object rotation around a specified axis (z-axis rotation of objects held in the palm)

**핵심 방법론:** Builds on Rapid Motor Adaptation (RMA) for in-hand manipulation. A base policy is trained with PPO in simulation across randomized environments. An adaptation module (small MLP) is trained to predict latent environment parameters from a short history of proprioceptive observations. At deployment, the adaptation module provides implicit system identification, enabling the policy to adapt to real-world dynamics without explicit calibration.

**주요 기여:**
- First demonstration of rapid motor adaptation for dexterous in-hand rotation on real Allegro Hand (real)
- Online adaptation eliminates the need for manual system identification or hand-tuned domain randomization
- Robust zero-shot transfer across diverse object shapes and sizes on real hardware (real)

**한계점:** Limited to single-axis rotation (not arbitrary SE(3) reorientation); relies on proprioception only (no vision or tactile); objects must remain in a palm-up configuration; limited to rigid objects

## 추론 / 배포

- **추론 지연 시간:** Not explicitly reported. The MLP policy with RMA adaptation module runs in <1ms per forward pass, enabling high-frequency control.
- **배포 하드웨어:** Allegro Hand (16 DoF). Policy trained in IsaacGym; deployed via zero-shot sim-to-real transfer with online RMA adaptation. MLP policy is lightweight enough for any compute platform.
- **실시간 가능 여부:** Yes. MLP-based RL policy with lightweight RMA module runs at real-time rates on the Allegro Hand.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** No pre-collected dataset. Pure RL (PPO) with rapid motor adaptation (RMA) -- all data generated in simulation.
- **수집 방법:** Pure RL in IsaacGym with domain randomization over physical parameters (mass, friction, scale). Online adaptation module trained from proprioceptive history. Zero-shot sim-to-real transfer. Cubes, cylinders, and YCB objects.
- **데이터 규모:** Standard parallel RL training in IsaacGym. ~10+ objects evaluated in real world.
- **원격 조작 장비:** Not applicable (pure RL, no demonstrations).
- **데이터 포맷:** Not applicable (online RL, no offline dataset).
- **공개 여부:** Code release status not reported.
