# 9.4 Adroit

- **Full title:** Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations
- **Authors:** Aravind Rajeswaran, Vikash Kumar, Abhishek Gupta, Giulia Vezzani, John Schulman, Emanuel Todorov, Sergey Levine
- **Venue/Year:** RSS 2018
- **Sim platform:** MuJoCo
- **Dexterous support:** Shadow Hand (24 DoF) simulated model (referred to as the ADROIT hand)
- **Tasks:** 4 canonical tasks -- pen rotation, door opening, hammer use, ball relocation
- **Demos:** 25 human demonstrations per task collected via CyberGlove

## Key methodology/design

Adroit introduced the DAPG (Demo Augmented Policy Gradient) algorithm, which combines a small number of human demonstrations with RL fine-tuning to solve complex dexterous manipulation tasks. The Shadow Hand model in MuJoCo became the de facto standard for dexterous RL benchmarking. Human demonstrations are collected through a CyberGlove teleoperation interface and used to initialize the policy, overcoming the exploration challenges of high-dimensional dexterous action spaces.

## Main contributions

- Established the canonical benchmark for dexterous RL with 4 tasks (pen, door, hammer, ball) that remain widely used
- DAPG algorithm demonstrating that a small number of human demos dramatically accelerates RL for high-DoF hands
- Open-source 24-DoF Shadow Hand model for MuJoCo that became the community standard

## Limitations/Gaps

- Only 4 tasks with relatively simple contact patterns; does not cover multi-stage or tool-use manipulation
- Shadow Hand model lacks tactile sensing simulation
- MuJoCo CPU-only at the time; now superseded by GPU-accelerated alternatives for large-scale training but remains a standard evaluation target
- Sim-to-real gap was not addressed in the original work

## Coverage gaps

| Criterion | Covered? |
|-----------|----------|
| Force/torque evaluation metrics | No |
| Deformable object tasks | No |
| Tactile sensing | No |
| Multi-stage / long-horizon tasks | No (each task is a single-stage objective) |
| Multi-hand coordination | No |

## Open-source status

Fully open-source. Available via `pip install gymnasium-robotics` (Gymnasium-Robotics provides maintained Adroit environments). Original code: [GitHub](https://github.com/aravindr93/hand_dapg)
