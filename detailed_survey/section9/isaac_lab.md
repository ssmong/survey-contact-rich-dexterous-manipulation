# 9.8 Isaac Lab

- **Full title:** Isaac Lab (formerly Orbit): A Unified and Modular Framework for Robot Learning
- **Developer:** NVIDIA (Isaac Sim team); evolved from Orbit (Mittal et al., IEEE RA-L 2023) and supersedes the deprecated IsaacGym (Preview 4)
- **Venue/Year:** IEEE RA-L 2023 (Orbit paper); Isaac Lab rebrand and major update 2024
- **Sim platform:** Built on NVIDIA Isaac Sim, powered by PhysX 5 (GPU-accelerated)
- **Dexterous support:** Allegro Hand, Shadow Hand, and any URDF/MJCF-based hand; supports articulated hand environments out of the box
- **Physics engine:** PhysX 5 with GPU-parallel rigid and deformable body simulation
- **Performance:** Thousands of parallel environments on a single GPU; comparable to IsaacGym speeds with improved API design

## Key methodology/design

Isaac Lab is NVIDIA's unified robot learning framework, built on top of Isaac Sim and designed as the successor to both IsaacGym (deprecated after Preview 4) and the earlier Orbit framework. It provides a modular, extensible API for creating GPU-parallelized robot learning environments. The framework supports RL, imitation learning, and sim-to-real transfer workflows. Unlike IsaacGym's standalone Python API, Isaac Lab integrates with the full Isaac Sim ecosystem, providing access to photorealistic rendering (RTX ray tracing), domain randomization, sensor simulation (cameras, LiDAR), and asset management. The environment API follows a gymnasium-compatible interface with support for vectorized (parallel) execution.

## Main contributions

- Replaces the deprecated IsaacGym (Preview 4) as NVIDIA's maintained simulation framework for robot learning
- GPU-parallel environment execution via PhysX 5 enabling thousands of simultaneous environments on one GPU
- Modular design: interchangeable robots, sensors, tasks, and reward functions through configuration
- Photorealistic rendering via RTX for visual sim-to-real transfer
- Built-in support for dexterous hand platforms (Allegro, Shadow) with pre-configured environments
- Compatible with major RL libraries (rl_games, RSL-rl, SKRL, Stable Baselines3)

## Usage in surveyed works

Isaac Lab (or its predecessor Isaac Sim / IsaacGym) is the simulation platform for multiple systems in this survey:
- **GR00T-Dexterity** (§7): Allegro Hand RL training in Isaac Lab
- **DextrAH-G/RGB** (§7): Allegro Hand + Kuka with geometric fabrics in Isaac Lab
- **CHIP** (§5): Humanoid impedance policy training in Isaac Sim
- **GR00T N1** (§6): policy evaluation and sim-to-real in Isaac Lab
- **TeleOpBench** (§9): teleoperation benchmark built on Isaac Sim

## Relationship to IsaacGym

IsaacGym (Preview 1-4) was NVIDIA's standalone GPU-parallel RL simulation library, widely used for dexterous manipulation research (in-hand rotation, DexPBT, HORA, etc.). IsaacGym is now deprecated and no longer maintained. Isaac Lab replaces it with a more modular architecture built on the full Isaac Sim platform. Key differences:
- IsaacGym: standalone Python library, limited rendering, no sensor simulation
- Isaac Lab: full Isaac Sim integration, RTX rendering, camera/LiDAR simulation, domain randomization
- Migration: most IsaacGym environments can be ported to Isaac Lab with API changes; NVIDIA provides migration guides

## Limitations/Gaps

- Requires NVIDIA GPU (no AMD/Intel support); tied to NVIDIA's proprietary Isaac Sim platform
- Heavier installation footprint than MuJoCo or Genesis (requires Isaac Sim, which is multi-GB)
- Closed-source physics engine (PhysX): not differentiable through contacts (unlike Genesis or DiffTactile)
- No built-in tactile sensor simulation (external plugins required)
- Learning curve: more complex API than IsaacGym's simple standalone interface
- Linux-only for full functionality (Windows support is partial)

## Coverage gaps

| Criterion | Covered? |
|-----------|----------|
| Force/torque evaluation metrics | No (force sensing available but no standardized force evaluation) |
| Deformable object tasks | Yes (PhysX 5 supports soft bodies) |
| Tactile sensing | No (no built-in tactile simulation; requires external plugins) |
| Multi-stage / long-horizon tasks | Partial (manager-based task API supports multi-stage, but few pre-built examples) |
| Multi-hand coordination | Partial (bimanual setups possible but not extensively benchmarked) |

## Open-source status

Open-source under BSD-3-Clause license. Install via `pip install isaaclab` (requires Isaac Sim). GitHub: [isaac-sim/IsaacLab](https://github.com/isaac-sim/IsaacLab). Documentation: [isaac-sim.github.io/IsaacLab](https://isaac-sim.github.io/IsaacLab/)
