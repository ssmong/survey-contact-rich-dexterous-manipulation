# Section 9: Simulation Benchmarks & Platforms

Simulation environments are foundational infrastructure for dexterous manipulation research. They enable massively parallel RL training, safe policy evaluation, and sim-to-real transfer pipelines. This section surveys platforms that specifically support multi-finger hand manipulation or provide differentiable contact physics relevant to dexterous tasks.

## Entries

| Entry | Platform | Dexterous Support | Key Strength |
|-------|----------|-------------------|--------------|
| [ManiSkill3](maniskill3.md) | SAPIEN / PhysX 5 | Allegro, DClaw, any URDF | GPU-parallel speed (430x), unified RL/IL/VLA baselines |
| [MuJoCo Playground](mujoco_playground.md) | MuJoCo MJX (JAX) | LEAP Hand, Shadow Hand | Minutes-scale training, zero-shot sim-to-real |
| [MuJoCo Manipulus](mujoco_manipulus.md) | MuJoCo | Multi-finger tool manipulation | First dedicated dexterous tool-use benchmark (16 tasks) |
| [Adroit](adroit.md) | MuJoCo | Shadow Hand (24 DoF) | Canonical RL benchmark (pen, door, hammer, ball) |
| [Genesis](genesis.md) | Custom multi-physics | Any URDF | Unified multi-physics (6 solvers), 43M+ FPS |
| [DiffTactile](difftactile.md) | Custom differentiable | Parallel-jaw only | Differentiable FEM-based tactile simulation |
| [TeleOpBench](teleopbench.md) | Isaac Sim | 3 humanoid embodiments | First dual-arm dexterous teleoperation benchmark (30 tasks) |
| [Isaac Lab](isaac_lab.md) | Isaac Sim (PhysX 5) | Allegro, Shadow, any URDF | IsaacGym successor; GPU-parallel, RTX rendering, modular API |
| [TACTO](tacto.md) | PyBullet + PyRender | Gripper (DIGIT/GelSight sensor sim) | Vision-based tactile sensor image simulation |

## Observations

The simulation landscape for dexterous manipulation is fragmenting across three axes: (1) **speed** -- GPU-parallel engines (ManiSkill3, MuJoCo Playground, Genesis) now train policies in minutes; (2) **physics fidelity** -- differentiable engines (Genesis, DiffTactile) enable gradient-based optimization through contact; (3) **task coverage** -- specialized benchmarks (Manipulus for tool use, TeleOpBench for teleoperation, Adroit for RL baselines) target specific capability gaps. No single platform yet combines GPU-parallel speed, differentiable contact physics, high-fidelity tactile simulation, and comprehensive dexterous task suites. DiffTactile provides the most detailed tactile physics but lacks GPU parallelism; ManiSkill3 provides the best parallel RL infrastructure but has minimal tactile support. Genesis aims for unification but is still maturing. Adroit remains the default RL evaluation target despite being nearly a decade old, illustrating both the value of standardized benchmarks and the community's slow migration to newer platforms.
