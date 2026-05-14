### 7.2 Visual Dexterity

**전체 제목:** Visual Dexterity: In-Hand Reorientation of Novel Objects Using Depth Sensing

**저자:** Tao Chen, Megha Tippur, Siyang Wu, Vikash Kumar, Edward Adelson, Pulkit Agrawal

**학회/연도:** Science Robotics 2023 (originally arXiv 2022)

**RL 알고리즘:** PPO with asymmetric actor-critic; teacher uses privileged state, student trained with domain randomization and depth image observations

**핸드 하드웨어:** D'Claw hand (9-12 DoF, depending on configuration); a low-cost 3-finger hand

**시뮬레이션 플랫폼:** IsaacGym Preview 3

**Sim2Real 여부:** Yes; zero-shot sim-to-real with domain randomization (visual and physical) (real). Depth-only perception enables robust transfer by sidestepping RGB sim-to-real gap

**객체 수:** Evaluated on 100+ novel objects unseen during training in real-world experiments

**작업:** Arbitrary in-hand reorientation to goal orientations (SO(3) reorientation, not just single-axis rotation)

**핵심 방법론:** Trains a visuomotor policy using depth images from a wrist-mounted RealSense camera for 6D object pose tracking during in-hand reorientation. The key architectural choice is depth-only input, which has a much smaller sim-to-real gap than RGB. An asymmetric actor-critic trains with privileged object pose in simulation; the deployed policy uses only depth observations. Extensive procedural object generation creates diverse training objects.

**주요 기여:**
- Full SO(3) in-hand reorientation (not just single-axis rotation) on real hardware with novel objects (real)
- Depth-only perception for minimal sim-to-real visual gap
- Generalization to 100+ novel real-world objects including household items not in the training distribution (real)

**한계점:** D'Claw is a 3-finger hand with limited dexterity compared to 5-finger hands; depth cameras have limitations with transparent/reflective objects; reorientation only (no translation control); requires wrist-mounted camera with clear view of the object

## 추론 / 배포

- **추론 지연 시간:** Not explicitly reported. The MLP policy with depth image input runs in <5ms per forward pass (depth image encoding + MLP).
- **배포 하드웨어:** D'Claw hand (9-12 DoF) + wrist-mounted Intel RealSense depth camera. Policy trained in IsaacGym; deployed via zero-shot sim-to-real transfer with domain randomization.
- **실시간 가능 여부:** Yes. Lightweight policy supports real-time control. Demonstrated on real D'Claw hand with 100+ novel objects.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** No pre-collected dataset. Pure RL (PPO) with asymmetric actor-critic -- all data generated in simulation.
- **수집 방법:** Pure RL in IsaacGym with domain randomization (visual and physical). Teacher uses privileged object state; student trained with depth image observations from wrist-mounted RealSense camera. Extensive procedural object generation creates diverse training objects. Zero-shot sim-to-real transfer.
- **데이터 규모:** Procedurally generated training objects. 100+ novel real-world objects for evaluation (unseen during training).
- **원격 조작 장비:** Not applicable (pure RL, no demonstrations).
- **데이터 포맷:** Not applicable (online RL, no offline dataset).
- **공개 여부:** Code release status not reported.
