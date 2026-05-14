# 9.3 MuJoCo Manipulus

- **Full title:** MuJoCo Manipulus: A Dexterous Tool Manipulation Benchmark
- **Authors:** Google DeepMind and collaborators
- **Venue/Year:** 2025 (preprint)
- **Sim platform:** MuJoCo
- **Dexterous support:** Multi-finger hands performing tool manipulation
- **Tasks:** 16 tool-use tasks including hammering, screwdriving, stirring, and other functional tool manipulation scenarios

## Key methodology/design

Manipulus provides a benchmark specifically targeting dexterous tool manipulation, an area underrepresented in existing simulation benchmarks. The environments require coordinated multi-finger control to grasp, reorient, and functionally use tools -- going beyond simple pick-and-place to contact-rich functional interactions. Tasks are designed to test both the grasping and functional use phases of tool manipulation.

## Main contributions

- First dedicated benchmark for dexterous tool manipulation with 16 distinct tasks in MuJoCo
- Systematic evaluation of tool-use capabilities requiring both grasp stability and functional dexterity
- Compatible with standard MuJoCo ecosystem (Gymnasium, dm_control)

## Limitations/Gaps

- Tool geometries and physical properties are simplified compared to real-world tools
- No deformable tool or workpiece interactions (e.g., cutting, spreading)
- Limited sim-to-real validation for tool-use policies

## Coverage gaps

| Criterion | Covered? |
|-----------|----------|
| Force/torque evaluation metrics | No |
| Deformable object tasks | No (rigid tools and workpieces only) |
| Tactile sensing | No |
| Multi-stage / long-horizon tasks | Partial (tool-use involves grasp + functional use, but tasks are not explicitly multi-stage sequences) |
| Multi-hand coordination | No |

## Open-source status

Open-source. Available through MuJoCo ecosystem.
