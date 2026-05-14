### Grasp-to-Act

**Full Title:** Grasp-to-Act: Dynamic Tool Use via Dexterous Grasping

**Authors:** Researchers from UIUC RoboTouch lab et al.

**Venue/Year:** arXiv preprint, 2026

**Hand Hardware:** LEAP Hand (16 DoF) mounted on a UR5 robotic arm. (Note: earlier version of this entry incorrectly stated Allegro Hand; the paper specifies "16-DoF LEAP hand mounted on a 6-DoF UR5 robotic arm.")

**Tasks:** 5 dynamic tool-use tasks: (1) hammering a nail, (2) sawing, (3) cutting with scissors/knife, (4) stirring with a spoon, (5) scooping with a spatula. These tasks require dynamic interaction forces between the tool and the environment, going beyond quasi-static pick-and-place.

**Key Methodology:** Grasp-to-Act decomposes dexterous tool use into two phases: first establishing a functional grasp on the tool, then executing the task-specific manipulation action. The approach combines grasp planning with action execution, enabling the LEAP hand to dynamically wield tools for contact-rich tasks. The method integrates simulation-based training with real-world validation.

**Architecture/Parameters:** Not publicly detailed. The policy architecture handles the transition from grasp acquisition to dynamic tool manipulation as a continuous control problem.

**Sim Platform:** Training uses simulation environments, with sim-to-real transfer demonstrated on the physical LEAP hand. The specific simulator details are not fully disclosed.

**Main Contributions:**
- Introduces a grasp-to-action decomposition that separates functional grasp planning from task execution, whereas prior dexterous tool-use methods train monolithic policies that must learn both grasping and manipulation jointly.
- Demonstrates dynamic tool-use tasks (hammering, sawing) on a 16-DoF dexterous hand, requiring sustained contact forces during tool operation -- extending beyond the quasi-static grasping focus of most prior LEAP hand work.
- Validates across 5 tool-use tasks requiring qualitatively different manipulation strategies (impact, reciprocating, rotational, scooping motions).

**Limitations/Gaps:**
- **Force/impedance awareness:** No. No explicit force/impedance control is incorporated despite the dynamic nature of the tool-use tasks. Contact forces during hammering, sawing, and cutting are not explicitly regulated, relying instead on learned position trajectories and hardware compliance to produce adequate tool-environment interaction forces.
- **VLA/language conditioning:** No. Policies are task-specific with no language or vision-language backbone.
- **Sim-to-real:** Yes. Sim-to-real transfer is demonstrated on the physical LEAP hand, though simulator details are not fully disclosed.
- **Code/weights availability:** No code or model weights publicly released.

**Results:** Simulation results (Table I from paper) and real-world validation on the LEAP hand:

| Task | Success Rate (Sim) | Translational Slip (cm) | Rotational Slip (deg) |
|------|-------------------|------------------------|-----------------------|
| Hammer | 100.0% | 0.69 | 1.35 |
| Saw | 100.0% | 1.06 | 3.13 |
| Cut | 100.0% | 0.48 | 2.23 |
| Stir | 100.0% | 0.24 | 2.08 |
| Scoop | 100.0% | 0.17 | 1.25 |

G2A outperforms all baselines (analytical methods, RL base, RL with contact rewards, RL with pre-grasp pose, RL with eigengrasp, and G2A w/o adaptation) across all five tasks in both success rate and slip metrics. Real-world trials confirmed G2A's superiority with lowest slip and highest task completion rates.

## Inference / Deployment

- **Inference latency:** Not explicitly reported in the paper or project page.
- **Deployment hardware:** 16-DoF LEAP hand mounted on a UR5 robotic arm + Intel RealSense D435 RGB-D camera. RL policy training on NVIDIA RTX 4070 Ti Super GPU (~15 min convergence). Inference GPU not specified.
- **Real-time capable?** The system operates at **30 Hz control frequency** (both wrist trajectory and finger joint adjustments updated synchronously at 30 Hz). Per-step inference latency not quantified, but 30 Hz real-time control is demonstrated.

## Dataset / Data Collection

- **Dataset used:** Custom dataset; no standard benchmark name reported.
- **Collection method:** Simulation-based training with sim-to-real transfer. Specific details on demonstration collection method (e.g., scripted trajectories vs. teleoperation) are not publicly disclosed.
- **Data scale:** Not reported.
- **Teleop equipment:** Not reported.
- **Data format:** Not reported.
- **Publicly available?** No. No code, data, or model weights publicly released.

> *Results verified from arXiv:2602.20466. Hardware confirmed as LEAP Hand (not Allegro Hand as previously stated).*

---
