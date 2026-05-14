### 7.1 DextrAH-G/RGB

**전체 제목:** DextrAH-G: Dexterous Arm-Hand Grasping with Geometric Fabrics

**저자:** Maximilian Haas-Heger, Viktor Makoviychuk, Ankur Handa, et al.

**학회/연도:** CoRL 2024

**RL 알고리즘:** PPO for grasp policy + geometric fabrics for arm motion planning; the RL policy controls the hand while geometric fabrics handle arm trajectory generation

**핸드 하드웨어:** Allegro Hand (16 DoF) + Kuka arm

**시뮬레이션 플랫폼:** Isaac Lab (NVIDIA)

**Sim2Real 여부:** Yes; demonstrated real-world arm-hand grasping with zero-shot transfer (real)

**객체 수:** Multiple objects evaluated; specific count not reported in the table

**작업:** Coordinated arm-hand dexterous grasping -- reaching, pre-shaping, and grasping objects on a table

**핵심 방법론:** Combines a learned dexterous grasp policy (PPO) with geometric fabrics for arm motion planning. Geometric fabrics provide a reactive, geometry-aware motion generation framework that handles arm trajectory and obstacle avoidance, while the RL policy focuses on finger control for grasping. This separation of concerns simplifies the learning problem and enables modular sim-to-real transfer. DextrAH-RGB extends this to RGB-based perception.

**주요 기여:**
- Integration of geometric fabrics with learned dexterous grasping for coordinated arm-hand control
- Modular architecture separating arm planning (geometric fabrics) from hand control (RL), simplifying each subproblem
- Demonstrated sim-to-real transfer on Allegro + Kuka system (real); forms the basis of NVIDIA GR00T-Dexterity

**한계점:** Geometric fabrics require hand-tuned parameters; limited to grasping (no in-hand manipulation or tool use); the separation between arm and hand control may limit performance on tasks requiring tight arm-hand coordination; evaluation on a relatively small object set compared to UniDexGrasp/ResDex

## 추론 / 배포

- **추론 지연 시간:** Not explicitly reported. The MLP hand policy runs in <1ms; geometric fabrics for arm control compute analytically in <1ms. Combined system supports high-frequency control.
- **배포 하드웨어:** Allegro Hand (16 DoF) + Kuka arm. Policy trained in Isaac Lab; deployed via zero-shot sim-to-real transfer. Forms the basis of NVIDIA GR00T-Dexterity.
- **실시간 가능 여부:** Yes. Both the MLP policy and geometric fabrics are computationally lightweight, supporting real-time arm-hand control on real hardware.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** No pre-collected dataset. Pure RL (PPO) for hand policy in Isaac Lab; geometric fabrics for arm motion (analytical, no learning).
- **수집 방법:** Pure RL in Isaac Lab for dexterous grasp policy. Geometric fabrics provide reactive arm trajectory generation (no training data needed). Sim-to-real transfer via domain randomization. DextrAH-RGB extends to RGB-based perception.
- **데이터 규모:** Standard parallel RL training in Isaac Lab. Object set size not prominently reported.
- **원격 조작 장비:** Not applicable (pure RL + analytical fabrics).
- **데이터 포맷:** Not applicable (online RL, no offline dataset).
- **공개 여부:** Forms basis of NVIDIA GR00T-Dexterity. Code release via Isaac Lab ecosystem.
