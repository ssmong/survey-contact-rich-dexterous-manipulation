### DexterityGen

**Full Title:** DexterityGen: Foundation Controller for Unprecedented Dexterity

**Authors:** Researchers from UC Berkeley / Meta et al.

**Venue/Year:** RSS 2025

**Hand Hardware:** Allegro Hand (16 DoF) mounted on a robotic arm. The Allegro is used as the primary evaluation platform for tool-use dexterity.

**Tasks:** Dexterous tool-use tasks including pen manipulation (writing/drawing), screwdriver operation, and syringe handling. These tasks require precise fingertip control and coordinated multi-finger motions for tool-mediated actions.

**Key Methodology:** DexterityGen trains a foundation controller (3 tools demonstrated) for dexterous manipulation that generalizes across tool-use tasks. The approach uses reinforcement learning in IsaacGym to develop a general-purpose dexterous controller that can be adapted to specific tool-use scenarios. The foundation controller concept aims to provide a base policy with sufficient finger coordination skills that can be quickly specialized for new tools and tasks, reducing the per-task training burden.

**Architecture/Parameters:** RL-based policy trained in IsaacGym with massively parallel environments. The foundation controller architecture enables transfer to new tool-use tasks. No public code or weights are released.

**Sim Platform:** NVIDIA IsaacGym. Sim-to-real transfer is demonstrated -- the paper shows successful real-world deployment of policies trained in simulation.

**Main Contributions:**
- Introduces a "foundation controller" concept (3 tools demonstrated: pen, screwdriver, syringe) that provides a reusable base policy transferable across tool-use tasks, reducing per-task training time compared to training each tool-use policy from scratch.
- Demonstrates dexterous tool use on the Allegro hand requiring precise and varied fingertip control strategies -- pen writing requires fine tip control, screwdriver turning requires torque-generating finger coordination, and syringe handling requires linear push motions.
- Achieves sim-to-real transfer for tool-use tasks, showing that the foundation controller concept survives the sim-to-real gap on the physical Allegro hand system.

**Limitations/Gaps:**
- **Force/impedance awareness:** No. No force/impedance control is used. Tool-environment contact forces (e.g., pen pressure on paper, screwdriver insertion torque) are not explicitly regulated. The system relies on learned position trajectories and implicit compliance to produce adequate contact forces, which may limit applicability to tasks requiring precise force modulation.
- **VLA/language conditioning:** No. No language conditioning or VLA integration. The foundation controller is adapted to new tools via RL fine-tuning, not via language-specified task descriptions.
- **Sim-to-real:** Yes. Policies trained in IsaacGym are successfully deployed on the physical Allegro hand.
- **Code/weights availability:** No code or weights released.

**Results:** Evaluated on atomic dexterous skills and long-horizon tool-use tasks. Raw teleoperation baseline fails completely on most tasks; DexterityGen enables both stability and success.

Table I -- Real-world atomic skill performance (Success Rate and Time-to-Fall):

| Task | Metric | Context |
|------|--------|---------|
| Reorient Large (Up/Down) | SR reported | Raw teleop fails; DexGen succeeds |
| Reorient Small (Up/Down) | SR reported | Raw teleop fails; DexGen succeeds |
| Functional Grasp (normal/horizontal) | SR reported | DexGen enables stable functional grasps |
| Regrasp (Ball/Cylinder) | SR reported | DexGen enables stable regrasps |

Table II -- Long-horizon tool-use task breakdown (stage-wise success, N=20 trials each):

| Task | Reorient | Regrasp | Align | Use | Context |
|------|----------|---------|-------|-----|---------|
| Screwdriver | 16/20 (80%) | 11/20 (55%) | 5/20 (25%) | 3/20 (15%) | Sequential stages; each requires prior stage success |
| Syringe | 15/20 (75%) | 9/20 (45%) | -- | 4/20 (20%) | Three-stage pipeline |

Long-horizon success drops at each stage due to sequential chaining difficulty. The foundation controller provides reusable dexterous primitives that generalize across tool types.

## Inference / Deployment

- **Inference latency:** ~27 ms per inference cycle (37 Hz) on NVIDIA RTX 4090. Tested with both 8 and 12 DDIM sampling steps, with a trade-off between action accuracy and latency.
- **Deployment hardware:** NVIDIA RTX 4090 GPU on a Lambda workstation. Allegro Hand (16 DoF) mounted on a robotic arm for real-world deployment.
- **Real-time capable?** Yes. Diffusion sampling runs at 37 Hz; actual robot control operates at 10 Hz. Human teleoperation operates at 300 Hz via a separate retargeting method. The 10 Hz control rate is sufficient for arm-level tool use but below the frequencies needed for high-speed dexterous finger control.

## Dataset / Data Collection

- **Dataset used:** No external dataset; training data generated via RL simulation rollout in IsaacGym, supplemented by human teleoperation demonstrations for imitation learning.
- **Collection method:** RL simulation rollout in IsaacGym for foundation controller pre-training; human teleoperation via a retargeting method at 300 Hz for demonstration collection on the physical Allegro hand.
- **Data scale:** Not reported (RL training generates data on-the-fly; number of teleoperated demonstrations not specified).
- **Teleop equipment:** Human hand retargeting system operating at 300 Hz for real-world demonstration collection.
- **Data format:** Not reported.
- **Publicly available?** No. No code, data, or model weights released.

> *Results verified from arXiv:2502.04307. Stage-wise success rates extracted from Table II.*

---
