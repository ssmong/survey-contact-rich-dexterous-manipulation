# 9.2 MuJoCo Playground

- **Full title:** MuJoCo Playground
- **Authors:** Google DeepMind MuJoCo team (Kevin Zakka, Baruch Tabanpour, and collaborators)
- **Venue/Year:** RSS 2025 (systems demo track)
- **Sim platform:** MuJoCo MJX (JAX-accelerated MuJoCo)
- **Dexterous support:** LEAP Hand tasks included; Shadow Hand variants available through MuJoCo's standard model library
- **Tasks:** Locomotion, dexterous manipulation (in-hand reorientation, cube rotation), whole-body control; tasks trainable in minutes on a single GPU

## Key methodology/design

MuJoCo Playground leverages MuJoCo MJX, the JAX-compiled version of the MuJoCo physics engine, to enable massively parallel simulation entirely on GPU/TPU. It provides a curated collection of environments with reward functions and training scripts that demonstrate how policies can be trained from scratch in minutes rather than hours. The system emphasizes zero-shot sim-to-real transfer by using MuJoCo's accurate contact dynamics.

## Main contributions

- Demonstration that accurate contact physics (MuJoCo) combined with JAX compilation can train dexterous policies in minutes on commodity hardware
- Pre-built environments for LEAP Hand manipulation with zero-shot sim-to-real transfer results
- Browser-based visualization and interactive environment exploration

## Limitations/Gaps

- Narrower task diversity compared to ManiSkill3 or Isaac Lab; focused on demonstrating speed rather than comprehensive benchmarking
- No built-in tactile simulation or deformable object support
- Documentation and community adoption still growing relative to established platforms

## Coverage gaps

| Criterion | Covered? |
|-----------|----------|
| Force/torque evaluation metrics | No |
| Deformable object tasks | No |
| Tactile sensing | No |
| Multi-stage / long-horizon tasks | No (focused on single-objective tasks like cube rotation) |
| Multi-hand coordination | No |

## Open-source status

Open-source under Apache 2.0. Install via `pip install playground`. GitHub: [google-deepmind/mujoco_playground](https://github.com/google-deepmind/mujoco_playground)
