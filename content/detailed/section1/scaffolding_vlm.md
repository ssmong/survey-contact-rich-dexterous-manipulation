### Scaffolding+VLM

**Full Title:** Scaffolding Dexterous Manipulation with Vision-Language Models

**Authors:** Vincent de Bakker, Joey Hejna, Tyler Ga Wei Lum, Onur Celik, Aleksandar Taranovic, Denis Blessing, Gerhard Neumann, Jeannette Bohg, Dorsa Sadigh (Stanford / KIT)

**Venue/Year:** NeurIPS 2025 (arXiv:2506.19212)

**Hand Hardware:** Allegro Hand (16 DoF) mounted on a KUKA robotic arm. The real-world setup uses a right-hand Allegro configuration with 16 joint command dimensions.

**Tasks:**
- *Simulation (8 tasks):* apple grasping, bottle manipulation, hammer use, drawer opening/closing, fridge interaction, sponge manipulation, pliers operation, scissors use.
- *Real-world (3 tasks):* box manipulation with arm (box_arm), bottle manipulation with arm (bottle_arm), hammer use with arm (hammer_arm).

**Key Methodology:** The framework uses a Vision-Language Model (Gemini 2.5 Flash Thinking) to scaffold the generation of dexterous manipulation demonstrations, which are then used to train RL policies. The pipeline has two stages: (1) VLM-guided dataset generation, where Gemini produces manipulation waypoints (experiments with 3, 5, 10, and 40 waypoints), few-shot demonstrations, and scripted baselines; (2) RL training on these VLM-generated datasets. This approach eliminates the need for human teleoperation demonstrations, using the VLM's spatial reasoning to bootstrap dexterous manipulation policies.

**Architecture/Parameters:** Uses Gemini 2.5 Flash Thinking as the VLM backbone. RL policies are trained on VLM-generated data. The real-world deployment stack integrates ROS, ZED camera, FoundationPose for object pose estimation, Segment Anything 2 for segmentation, and keypoint tracking.

**Sim Platform:** Custom Gymnasium environments (EnvApple-v0, EnvBottle-v0, etc.). Sim-to-real transfer is demonstrated -- policies trained in simulation with VLM-scaffolded data are deployed on the real Allegro + KUKA system.

**Main Contributions:**
- Introduces VLM-scaffolded demonstration generation as an alternative to human teleoperation for dexterous manipulation, leveraging Gemini's spatial reasoning to produce manipulation waypoints -- prior dexterous manipulation pipelines required either human demonstrations or manual reward engineering.
- Demonstrates that VLM-generated demonstrations can successfully train dexterous manipulation policies for an 8-task suite in simulation and 3 tasks in the real world, establishing that VLM spatial reasoning is sufficient for dexterous task bootstrapping.
- Only paper in this section that integrates a VLA/language model into the dexterous manipulation pipeline; all other works use either pure RL or human demonstration pipelines.

**Limitations/Gaps:**
- **Force/impedance awareness:** No. No force/impedance control is used. The VLM generates position waypoints only; contact force profiles during tool use or object interaction are not explicitly scaffolded or controlled. For tasks requiring precise force application (e.g., hammer striking force, scissors cutting pressure), force regulation would need to be learned implicitly by the downstream RL policy.
- **VLA/language conditioning:** Yes (for demonstration generation). Gemini 2.5 Flash Thinking is used as the VLM backbone for scaffolding, but it generates demonstrations offline rather than serving as a real-time policy backbone. The VLM's role is dataset generation, not closed-loop control.
- **Sim-to-real:** Yes. Policies trained in simulation with VLM-scaffolded data are deployed on the real Allegro + KUKA system for 3 tasks.
- **Code/weights availability:** No model weights released. The approach depends on access to the Gemini API for the scaffolding stage and on FoundationPose for real-world object pose estimation.

**Results:** Evaluated across 8 simulation tasks and 3 real-world tasks. Success rates reported across 3 seeds (simulation) and 20 rollouts per task (real-world).

Simulation zero-shot success rates (approximate, from Figure 4):

| Task | Zero-Shot SR | Few-Shot SR |
|------|-------------|-------------|
| Move Apple | ~75% | ~85% |
| Move Bottle | ~70% | ~80% |
| Open Drawer | ~85% | ~90% |
| Open Fridge | ~45% | ~80% |
| Hammer | ~65% | ~75% |
| Wipe with Sponge | ~60% | ~70% |
| Close Scissors | ~80% | ~85% |
| Place Bottle onto Plate | ~70% | ~80% |

Real-world success rates (20 rollouts per task):

| Task | Success Rate |
|------|-------------|
| Place Bottle onto Plate | 90% |
| Slide Box to Bottle | 85% |
| Hammer Three Times | 65% |

Few-shot performance uses 3 successful examples from the VLM-generated demonstrations. The method eliminates the need for human demonstrations or handcrafted rewards.

## Inference / Deployment

- **Inference latency:** Not reported. The VLM (Gemini 2.5 Flash Thinking) is used offline for demonstration generation, not at inference time. The downstream RL policy inference speed is not characterized.
- **Deployment hardware:** Real-world system uses Allegro Hand (16 DoF) + KUKA arm, ZED camera, with FoundationPose and Segment Anything 2 for perception. GPU used for policy inference not specified.
- **Real-time capable?** The RL policy likely runs in real-time (standard MLP-based RL policies are sub-millisecond), but the paper does not report control frequency or inference latency. The VLM scaffolding stage is offline and does not affect deployment-time performance.

## Dataset / Data Collection

- **Dataset used:** Custom VLM-generated demonstrations (no named dataset). Demonstrations are synthesized by Gemini 2.5 Flash Thinking, not collected from humans.
- **Collection method:** VLM-scaffolded synthetic generation. Gemini 2.5 Flash Thinking generates manipulation waypoints (experiments with 3, 5, 10, and 40 waypoints), few-shot demonstrations, and scripted baselines. No human teleoperation is required for demonstration generation.
- **Data scale:** Not reported. The number of generated demonstrations per task is not specified in public materials.
- **Teleop equipment:** Not applicable (VLM-generated demonstrations, not teleoperation).
- **Data format:** Not reported.
- **Publicly available?** No dataset or model weights released. The approach depends on access to the Gemini API for the scaffolding stage.

---
