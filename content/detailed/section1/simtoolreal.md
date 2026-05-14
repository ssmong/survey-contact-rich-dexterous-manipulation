### SimToolReal

**Full Title:** From Sim to Real: A Pipeline for Training and Deploying Dexterous Tool-Use Policies

**Authors:** Tyler Lum et al. (Stanford IPRL)

**Venue/Year:** arXiv preprint, 2026

**Hand Hardware:** Sharpa Hand (22 DoF) mounted on a KUKA robotic arm. The Sharpa hand is a high-DoF anthropomorphic dexterous hand designed for complex manipulation tasks requiring multi-finger coordination.

**Tasks:** 24 tool-use tasks evaluated, including hammer striking, screwdriver turning, spatula flipping, and other tool-mediated manipulation scenarios. The task suite is designed to cover a broad range of everyday tool-use behaviors that require coordinated finger-tool-object interactions.

**Key Methodology:** SimToolReal proposes an end-to-end pipeline for training dexterous tool-use policies in simulation and deploying them on real hardware. The approach trains reinforcement learning policies in IsaacGym with domain randomization to achieve robust sim-to-real transfer. The pipeline addresses the full workflow from simulation environment design through policy training to real-world deployment on the 22-DoF Sharpa hand.

**Architecture/Parameters:** RL policies trained with PPO in massively parallel IsaacGym environments. Policy networks are typically MLP-based with proprioceptive state inputs. Checkpoints are publicly released.

**Sim Platform:** NVIDIA IsaacGym. Sim-to-real transfer is demonstrated -- policies trained entirely in simulation are deployed on real hardware without fine-tuning.

**Main Contributions:**
- First to demonstrate a complete sim-to-real pipeline for dexterous tool use at 24-task scale, prior work covered at most a handful of tool-use tasks with high-DoF hands.
- Provides the largest dexterous tool-use evaluation suite, spanning diverse tool categories (striking, turning, scooping, etc.), whereas prior benchmarks focused on single tool types.
- Open-sources code ([GitHub](https://github.com/tylerlum/simtoolreal)) and model checkpoints, enabling reproducibility -- most comparable works do not release trained policies.

**Limitations/Gaps:**
- **Force/impedance awareness:** No. The system does not incorporate force/torque sensing or impedance control; it relies purely on position-based control targets. For tasks involving significant contact forces (hammering, prying), contact management is handled implicitly via simulation contact models and hardware compliance rather than explicit force regulation.
- **VLA/language conditioning:** No. Policies are task-specific RL agents with no language or vision-language model integration.
- **Sim-to-real:** Yes. Policies trained entirely in IsaacGym are deployed on real hardware without fine-tuning, using domain randomization to bridge the sim-to-real gap.
- **Code/weights availability:** Code released ([GitHub](https://github.com/tylerlum/simtoolreal)); model checkpoints publicly available.

**Results:** Evaluated across 120 real-world rollouts spanning 24 tasks, 12 object instances, and 6 tool categories (hammers, markers, erasers, brushes, spatulas, screwdrivers). The paper reports Task Progress (percentage of demonstrated goal poses tracked within epsilon=2cm tolerance) rather than binary success rates.

| Metric | Value | Context |
|--------|-------|---------|
| Improvement over baselines | +37% | SimToolReal vs. prior retargeting and fixed-grasp methods in task progress |
| Real-world rollouts | 120 | Spanning 24 tasks, 12 object instances, 6 tool categories |
| Best performance category | Eraser tasks | Translation-focused trajectories (highest task progress) |
| Specialist comparison | Matches | SimToolReal matches specialist policies on training conditions while maintaining robustness under trajectory variations |

Per-tool-category results (from paper figures): eraser and marker tasks achieve highest task progress; hammer, brush, spatula, and screwdriver tasks (requiring in-hand rotations) show moderate but successful performance. Kinematic retargeting baseline failed to grasp in most cases. Fixed-grasp baseline degraded on rotation-required tasks.

## Inference / Deployment

- **Inference latency:** Not explicitly reported. The paper mentions 30 Hz object pose tracking during real-world inference and domain randomization over observation delays and action-execution latency during training, but does not quantify per-step policy inference time.
- **Deployment hardware:** KUKA arm + Sharpa Hand (22 DoF) + ZED stereo camera for real-world deployment. GPU model used for policy inference not reported.
- **Real-time capable?** Likely yes for RL-based MLP policies (typically sub-millisecond inference), but specific control frequency not reported. The 30 Hz pose estimation suggests the control loop runs at or below 30 Hz.

## Dataset / Data Collection

- **Dataset used:** DexToolBench (custom benchmark created for this work), covering 6 tool categories: hammers, markers, erasers, brushes, spatulas, and screwdrivers, with multiple object instances and task variants per category.
- **Collection method:** RL simulation rollout in IsaacGym. Real-world RGB-D demonstrations captured via ZED camera (processed through SAM 2, SAM 3D for mesh extraction, FoundationPose for 6D pose estimation) are used to define task trajectories, which are converted to JSON pose files for simulation training.
- **Data scale:** Not explicitly reported (organized hierarchically per object category / object / task).
- **Teleop equipment:** Not applicable (RL-trained in simulation; real demonstrations captured via passive RGB-D recording, not teleoperation).
- **Data format:** RGB images, depth images, object masks, camera intrinsics (cam_K.txt), poses in robot frame (poses.json), organized in per-task directories.
- **Publicly available?** Yes. Benchmark data downloadable via `download_dextoolbench_data.py`; pretrained policy checkpoints via `download_pretrained_policy.py` ([GitHub](https://github.com/tylerlum/simtoolreal)).

---
