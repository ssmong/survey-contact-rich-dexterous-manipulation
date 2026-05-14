### DexUMI

**Full Title:** DexUMI: Dexterous Universal Manipulation Interface

**Authors:** Researchers from Stanford et al.

**Venue/Year:** CoRL 2025 (Best Paper Finalist)

**Hand Hardware:** XHand and Inspire Hand. DexUMI is designed as a hardware-agnostic interface, supporting multiple dexterous hand platforms for real-world manipulation data collection and policy deployment.

**Tasks:** Real-world dexterous manipulation tasks. The system focuses on enabling data collection and policy learning for diverse manipulation scenarios using dexterous hands in unstructured real-world environments. Specific tasks span everyday manipulation behaviors.

**Key Methodology:** DexUMI extends the Universal Manipulation Interface (UMI) paradigm to dexterous multi-finger hands. The approach provides a portable, low-cost data collection framework that maps human hand motions to dexterous robot hands for in-the-wild demonstration collection. Unlike most dexterous manipulation works that rely on simulation, DexUMI operates entirely in the real world, using human demonstrations collected via the interface to train imitation learning policies. The emphasis is on practical deployability and broad task coverage with minimal setup overhead.

**Architecture/Parameters:** Imitation learning policies trained from real-world demonstrations collected via the DexUMI hardware interface. The specific policy architecture follows the UMI framework adapted for higher-dimensional dexterous hand action spaces.

**Sim Platform:** Real-world only -- no simulation is used. The entire pipeline (data collection, training, deployment) operates on physical hardware.

**Main Contributions:**
- Extends the UMI framework to dexterous hands, providing a portable and accessible data collection interface for multi-finger manipulation -- prior dexterous hand teleoperation systems required expensive motion capture setups or custom glove hardware, whereas DexUMI uses a low-cost portable device.
- Demonstrates real-world-only dexterous manipulation learning without any simulation, in contrast to the sim-to-real paradigm dominant in the field -- this shows that real-world imitation learning is viable for high-DoF hands, not just parallel-jaw grippers.
- CoRL 2025 Best Paper Finalist.

**Limitations/Gaps:**
- **Force/impedance awareness:** No. No force/torque sensing or impedance control is incorporated. The imitation learning policies learn position trajectories from demonstrations, without explicit force regulation. For tasks requiring precise contact force control (e.g., inserting fragile objects, controlled tool application), the position-only control scheme may be insufficient.
- **VLA/language conditioning:** No. The pipeline uses demonstration-based imitation learning with no language conditioning or VLA backbone. Task specification is via physical demonstrations, not language instructions.
- **Sim-to-real:** Not applicable. The system operates entirely in the real world with no simulation component. This eliminates the sim-to-real gap but limits scalability of data collection compared to simulation-based approaches.
- **Code/weights availability:** Not publicly documented at time of review.

**Results:** Average success rate of 86% across tasks, evaluated on both underactuated (Inspire Hand, 6 active DoFs) and fully-actuated (XHand, 12 active DoFs) platforms. Best configuration uses relative finger actions, tactile sensing, and inpainting-based visual adaptation.

| Task | Hand | Success Rate |
|------|------|-------------|
| Cube Picking | Inspire Hand | 1.00 |
| Egg Carton Opening | Inspire Hand | 0.85 |
| Tea Picking (tool) | Inspire Hand | 1.00 |
| Tea Picking (leaf) | Inspire Hand | 0.85 |
| Kitchen - Knob | XHand | 1.00 |
| Kitchen - Pan | XHand | 0.85 |
| Kitchen - Salt | XHand | 0.95 |
| Kitchen - Overall | XHand | 0.75 |

Data collection is 3.2x more efficient than traditional teleoperation methods (within 15-minute collection sessions).

## Inference / Deployment

- **Inference latency:** Policy executes at **10 Hz**. The UR5 arm executes commands at 125 Hz, the Inspire Hand at 10 Hz, and the XHand at 60 Hz. The policy predicts 16 future action steps, executes only the first 8, at 10 Hz.
- **Deployment hardware:** UR5 robotic arm + XHand or Inspire Hand. Uses pretrained DINO-V2 for visual feature extraction. Inference GPU not specified.
- **Real-time capable?** Yes, at 10 Hz policy frequency. The system compensates for sensor latency through temporal alignment (tcapture = treceive - lsensor). The 10 Hz rate is suitable for arm-level manipulation but slower than the XHand's native 60 Hz capability.

## Dataset / Data Collection

- **Dataset used:** Custom real-world demonstrations collected via the DexUMI hardware interface. No named benchmark dataset.
- **Collection method:** In-the-wild human demonstrations collected via the DexUMI portable handheld device, which maps human hand motions to dexterous robot hands (XHand, Inspire Hand). The system is designed for low-cost, portable data collection without motion capture or VR setups.
- **Data scale:** Not reported in public materials. The paper should be consulted for the number of demonstrations collected per task.
- **Teleop equipment:** DexUMI handheld device -- a portable, low-cost interface extending the Universal Manipulation Interface (UMI) paradigm to multi-finger dexterous hands. No expensive gloves, exoskeletons, or MoCap required.
- **Data format:** Not reported. Follows the UMI framework adapted for higher-dimensional dexterous hand action spaces.
- **Publicly available?** Not publicly documented at time of review.

> *Results verified from arXiv:2505.21864. Per-task success rates extracted from Table 1. Average 86% success rate confirmed.*

---
