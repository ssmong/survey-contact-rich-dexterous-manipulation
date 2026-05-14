# 9.6 DiffTactile

- **Full title:** DiffTactile: A Physics-based Differentiable Tactile Simulator for Contact-Rich Robotic Manipulation
- **Authors:** Zilin Si, Gu Zhang, Qingwei Ben, Branden Romero, Zhou Xian, Chao Liu, Chuang Gan
- **Venue/Year:** ICLR 2024
- **Sim platform:** Custom differentiable physics engine
- **Sensor models:** FEM-based tactile sensor models, parallel-jaw gripper implementations
- **Object models:** Soft (elastic, elastoplastic), rigid, multi-material, and cable objects
- **Tasks:** Box opening, manipulation with tactile reward signals

## Key methodology/design

DiffTactile models soft tactile sensors using finite element methods (FEM) and simulates contact interactions between sensors and objects with varied material properties. The entire simulation pipeline is differentiable, enabling gradient-based optimization of manipulation trajectories. This allows direct optimization of contact-rich behaviors through backpropagation through the physics, rather than requiring reward-based RL exploration.

## Main contributions

- First fully differentiable tactile simulation platform supporting FEM-based soft sensor models
- Support for diverse material properties (elastic, elastoplastic, rigid, multi-material, cable) enabling contact-rich task diversity
- Gradient-based skill learning for manipulation tasks using tactile feedback, bypassing the sample inefficiency of RL
- Integration of tactile sensing with differentiable contact physics for end-to-end optimization

## Limitations/Gaps

- Simulation speed is limited compared to GPU-parallel platforms (IsaacGym, ManiSkill3); FEM computation is expensive
- Sensor models are simplified compared to real GelSight/DIGIT sensors; optical simulation of tactile images is not included
- Limited to planar/parallel-jaw gripper configurations; multi-finger dexterous hand support is not demonstrated
- Real-world validation of optimized policies is limited

## Dexterous hand gap

**Does not support multi-finger hands -- only parallel-jaw grippers. This is a fundamental scope limitation for dexterous manipulation research.** All tasks and sensor models are designed around planar grippers with two opposing contact surfaces. Extending to multi-finger hands would require: (1) FEM models for multiple independently articulated fingertip sensors, (2) contact resolution between many simultaneous finger-object contact pairs, and (3) substantially higher computational cost. Until multi-finger support is added, DiffTactile's differentiable tactile physics cannot be applied to the dexterous hand platforms (LEAP, Allegro, Shadow) that dominate the field.

## Coverage gaps

| Criterion | Covered? |
|-----------|----------|
| Force/torque evaluation metrics | Partial (tactile reward signals include force information, but no standardized force evaluation protocol) |
| Deformable object tasks | Yes (elastic, elastoplastic, cable objects) |
| Tactile sensing | Yes (core contribution -- FEM-based differentiable tactile simulation) |
| Multi-stage / long-horizon tasks | No |
| Multi-hand coordination | No |

## Open-source status

Open-source under MIT license. GitHub: [Genesis-Embodied-AI/DiffTactile](https://github.com/Genesis-Embodied-AI/DiffTactile)
