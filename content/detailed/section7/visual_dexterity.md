### 7.2 Visual Dexterity

**Full title:** Visual Dexterity: In-Hand Reorientation of Novel Objects Using Depth Sensing

**Authors:** Tao Chen, Megha Tippur, Siyang Wu, Vikash Kumar, Edward Adelson, Pulkit Agrawal

**Venue/Year:** Science Robotics 2023 (originally arXiv 2022)

**RL algorithm:** PPO with asymmetric actor-critic; teacher uses privileged state, student trained with domain randomization and depth image observations

**Hand hardware:** D'Claw hand (9-12 DoF, depending on configuration); a low-cost 3-finger hand

**Sim platform:** IsaacGym Preview 3

**Sim2Real?** Yes; zero-shot sim-to-real with domain randomization (visual and physical) (real). Depth-only perception enables robust transfer by sidestepping RGB sim-to-real gap

**Object count:** Evaluated on 100+ novel objects unseen during training in real-world experiments

**Tasks:** Arbitrary in-hand reorientation to goal orientations (SO(3) reorientation, not just single-axis rotation)

**Key methodology:** Trains a visuomotor policy using depth images from a wrist-mounted RealSense camera for 6D object pose tracking during in-hand reorientation. The key architectural choice is depth-only input, which has a much smaller sim-to-real gap than RGB. An asymmetric actor-critic trains with privileged object pose in simulation; the deployed policy uses only depth observations. Extensive procedural object generation creates diverse training objects.

**Main contributions:**
- Full SO(3) in-hand reorientation (not just single-axis rotation) on real hardware with novel objects (real)
- Depth-only perception for minimal sim-to-real visual gap
- Generalization to 100+ novel real-world objects including household items not in the training distribution (real)

**Limitations/Gaps:** D'Claw is a 3-finger hand with limited dexterity compared to 5-finger hands; depth cameras have limitations with transparent/reflective objects; reorientation only (no translation control); requires wrist-mounted camera with clear view of the object

## Inference / Deployment

- **Inference latency:** Not explicitly reported. The MLP policy with depth image input runs in <5ms per forward pass (depth image encoding + MLP).
- **Deployment hardware:** D'Claw hand (9-12 DoF) + wrist-mounted Intel RealSense depth camera. Policy trained in IsaacGym; deployed via zero-shot sim-to-real transfer with domain randomization.
- **Real-time capable?** Yes. Lightweight policy supports real-time control. Demonstrated on real D'Claw hand with 100+ novel objects.

## Dataset / Data Collection

- **Dataset used:** No pre-collected dataset. Pure RL (PPO) with asymmetric actor-critic -- all data generated in simulation.
- **Collection method:** Pure RL in IsaacGym with domain randomization (visual and physical). Teacher uses privileged object state; student trained with depth image observations from wrist-mounted RealSense camera. Extensive procedural object generation creates diverse training objects. Zero-shot sim-to-real transfer.
- **Data scale:** Procedurally generated training objects. 100+ novel real-world objects for evaluation (unseen during training).
- **Teleop equipment:** Not applicable (pure RL, no demonstrations).
- **Data format:** Not applicable (online RL, no offline dataset).
- **Publicly available?** Code release status not reported.
