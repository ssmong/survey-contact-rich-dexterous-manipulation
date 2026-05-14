# 9.5 Genesis

- **Full title:** Genesis: A Universal and Generative Physics Engine for Robotics and Beyond
- **Authors:** Genesis-Embodied-AI team (multi-institutional collaboration)
- **Venue/Year:** December 2024 (preprint, with performance benchmarking report January 2025)
- **Sim platform:** Custom multi-physics engine
- **Dexterous support:** Any URDF-based hand; supports rigid-body, deformable, and fluid interactions
- **Physics solvers:** Rigid body dynamics, MPM (Material Point Method), SPH (Smoothed Particle Hydrodynamics), FEM (Finite Element Method), PBD (Position-Based Dynamics), Stable Fluid
- **Performance:** Over 43 million FPS simulating a Franka arm on a single RTX 4090

## Key methodology/design

Genesis is designed as a universal physics platform that unifies six distinct physics solvers under a single API. It targets general-purpose robotics and embodied AI applications, functioning simultaneously as a physics engine, robotics simulation platform, photo-realistic rendering system, and generative data engine. The system is designed to be fully differentiable (currently supported for MPM and Tool Solver, with other solvers planned). It supports cross-platform execution on CPU, NVIDIA/AMD GPUs, and Apple Metal.

## Main contributions

- Unified multi-physics engine integrating rigid, soft, fluid, and cloth simulation under a single API
- High simulation speed (43M+ FPS for rigid-body) through GPU-parallel computation
- Differentiable simulation enabling gradient-based optimization for manipulation tasks
- Cross-platform support (Linux, macOS, Windows) with multiple GPU backend options
- Support for diverse robot types (arms, legged robots, drones, soft robots) and file formats (.xml, .urdf, .obj, .glb, .ply, .stl)

## Limitations/Gaps

- Differentiability is currently limited to MPM and Tool Solver; rigid-body and FEM solvers not yet differentiable
- Relatively new platform with less community adoption and fewer pre-built task environments compared to MuJoCo or Isaac Lab
- Contact dynamics accuracy for dexterous manipulation not yet extensively benchmarked against established simulators
- Photo-realistic rendering capabilities claimed but not yet widely validated for sim-to-real visual transfer

## Coverage gaps

| Criterion | Covered? |
|-----------|----------|
| Force/torque evaluation metrics | No (no standardized force-based evaluation metrics despite physics support) |
| Deformable object tasks | Yes (MPM, FEM, PBD solvers support deformable interactions) |
| Tactile sensing | No (no tactile sensor simulation modules) |
| Multi-stage / long-horizon tasks | No (no pre-built long-horizon task suites; platform supports custom tasks) |
| Multi-hand coordination | No |

## Open-source status

Open-source. Install via `pip install genesis-world`. GitHub: [Genesis-Embodied-AI/Genesis](https://github.com/Genesis-Embodied-AI/genesis)
