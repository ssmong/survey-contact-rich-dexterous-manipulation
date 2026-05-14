# 9.1 ManiSkill3

- **Full title:** ManiSkill3: GPU Parallelized Robotics Simulation and Benchmark with Enhanced Visual and Contact-Rich Environments
- **Authors:** Stone Tao, Fanbo Xiang, Arth Shukla, Yuzhe Qin, Xander Gao, Hao Su, and collaborators (UCSD, Stanford, others)
- **Venue/Year:** RSS 2025 (arXiv 2410.00425, October 2024)
- **Sim platform:** SAPIEN with GPU-parallelized physics (PhysX 5) and rendering
- **Dexterous support:** Allegro Hand, DClaw; extensible to arbitrary URDF hands
- **Tasks:** 20+ task families spanning rigid-body, deformable, and fluid manipulation; includes dexterous in-hand reorientation and multi-finger grasping environments
- **Performance:** Up to 430x faster than prior ManiSkill versions; supports thousands of parallel environments on a single GPU

## Key methodology/design

ManiSkill3 redesigns the simulation loop to exploit GPU parallelism for both physics stepping and visual rendering. It wraps SAPIEN's PhysX 5 backend to run thousands of environments simultaneously, enabling RL training that previously took days to complete in minutes. The framework provides a unified Gym-compatible API with built-in baselines for RL (PPO, SAC), imitation learning, and VLA evaluation.

## Main contributions

- GPU-parallelized simulation achieving 430x speedup over ManiSkill2 on rigid-body tasks, with significant speedups for soft-body and fluid tasks
- Unified benchmark with baselines spanning RL, IL (Diffusion Policy, ACT), and VLA (RT-2, Octo) for standardized comparison
- Enhanced contact-rich environments with improved collision detection and friction modeling for dexterous manipulation tasks

## Limitations/Gaps

- Tactile sensing simulation is limited; no native support for high-resolution tactile sensor models (e.g., GelSight, DIGIT)
- Soft-body simulation, while supported, is slower than rigid-body and less thoroughly benchmarked for dexterous tasks
- Sim-to-real transfer results for dexterous hand tasks are not extensively validated in the paper

## Coverage gaps

| Criterion | Covered? |
|-----------|----------|
| Force/torque evaluation metrics | No |
| Deformable object tasks | Yes (soft-body and fluid tasks included, though less benchmarked for dexterous hands) |
| Tactile sensing | No (no native tactile sensor models) |
| Multi-stage / long-horizon tasks | Partial (some multi-step tasks, but not a systematic long-horizon suite) |
| Multi-hand coordination | No |

## Open-source status

Fully open-source. Install via `pip install mani-skill`. GitHub: [haosulab/ManiSkill](https://github.com/haosulab/ManiSkill)
