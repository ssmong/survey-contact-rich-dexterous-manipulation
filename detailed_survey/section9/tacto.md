# 9.9 TACTO

- **Full title:** TACTO: A Fast, Flexible and Open-source Simulator for High-Resolution Vision-based Tactile Sensors
- **Authors:** Shaoxiong Wang, Mike Lambeta, Po-Wei Chou, Roberto Calandra
- **Institution:** Meta FAIR (Facebook AI Research)
- **Venue/Year:** IEEE Robotics and Automation Letters (RA-L) 2022
- **Sim platform:** PyBullet (physics) + PyRender (tactile rendering)
- **Sensor models:** DIGIT, OmniTact, GelSight-style vision-based tactile sensors
- **Tasks:** Grasping, rolling, object manipulation with tactile feedback

## Key methodology/design

TACTO simulates vision-based tactile sensors by rendering synthetic tactile images from contact geometry. Rather than attempting physically accurate contact deformation simulation, TACTO focuses on fast, visually plausible tactile image generation. When an object contacts a simulated sensor, TACTO renders the contact patch using PyRender with appropriate lighting and gel surface properties, producing RGB tactile images similar to those from real DIGIT or GelSight sensors. The physics simulation (rigid body dynamics, collision detection) is handled by PyBullet, while TACTO handles only the tactile rendering pipeline. This separation allows TACTO to be integrated with any PyBullet-based manipulation environment.

## Main contributions

- First open-source simulator specifically targeting high-resolution synthetic tactile images for DIGIT and OmniTact vision-based tactile sensors
- Fast rendering enabling RL training with tactile observations (significantly faster than FEM-based alternatives like DiffTactile)
- Modular design: sensor geometry and optical properties are configurable via YAML files
- Simple integration with existing PyBullet environments via a thin API layer
- Headless rendering support (EGL/OSMESA) for server-side training

## Usage in surveyed works

TACTO or its tactile simulation approach has been referenced by multiple works in this survey:
- **Sparsh** (§12): tactile encoder trained/evaluated with simulated and real DIGIT data
- **RotateIt** (§7): uses tactile simulation for in-hand rotation
- Other tactile manipulation papers using DIGIT/GelSight benefit from TACTO-style simulated data for pretraining or augmentation

## Limitations/Gaps

- Explicitly not physically accurate: "not meant to provide physically accurate dynamics of contacts (e.g., deformation, friction)" -- contact forces and deformation are approximated
- PyBullet backend limits simulation speed compared to GPU-parallel engines (IsaacGym, ManiSkill3)
- No differentiable rendering: cannot backpropagate gradients through the tactile image generation
- Limited to vision-based tactile sensors (DIGIT, OmniTact, GelSight); does not simulate resistive, capacitive, or barometric tactile sensors
- No multi-finger dexterous hand environments included out of the box (examples focus on parallel-jaw grippers)
- Some visualization issues between PyBullet and PyRender on macOS

## Coverage gaps

| Criterion | Covered? |
|-----------|----------|
| Force/torque evaluation metrics | No (tactile images are visual, not force-calibrated) |
| Deformable object tasks | No (rigid body physics only via PyBullet) |
| Tactile sensing | Yes (core contribution -- synthetic tactile image generation) |
| Multi-stage / long-horizon tasks | No |
| Multi-hand coordination | No |

## Open-source status

Open-source under MIT License. Install via `pip install tacto`. GitHub: [facebookresearch/tacto](https://github.com/facebookresearch/tacto)
