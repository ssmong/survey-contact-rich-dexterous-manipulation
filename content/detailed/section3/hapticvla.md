## 3.5 HapticVLA

- **Full title:** HapticVLA: Haptic-Enhanced Vision-Language-Action Model via Tactile Distillation
- **Authors:** Skoltech et al.
- **Venue/Year:** arXiv preprint, 2026
- **arXiv:** https://arxiv.org/abs/2603.15257

**Force/tactile input type:** Tactile sensors used during training but distilled away at inference. The model learns from tactile signals during training and operates without tactile sensors at deployment, similar to the FD-VLA distillation approach but applied to tactile (rather than F/T) modality.

**Force/impedance output:** No. Position-only output.

> **Limitation (position-only output):** Position-only output; the policy cannot actively regulate contact forces despite receiving force/tactile input.

**Robot platform:** LeRobot SO-101 arm with tactile sensors attached during training data collection.

> **Limitation (gripper-only):** Evaluated only on parallel-jaw grippers; not validated on multi-finger dexterous hands.

**Tasks:** Pick-and-place tasks with contact-sensitive objects: jar handling, waffle picking, egg manipulation. These tasks benefit from tactile feedback due to the fragility or slipperiness of the objects.

**Key methodology:** HapticVLA uses tactile distillation -- a teacher model trained with tactile input supervises a student model that operates from vision and language only. The tactile signals provide privileged information about grasp quality, contact stability, and surface properties during training. The student model learns to infer these contact properties from visual cues through feature-level distillation. This enables deploying the policy on low-cost robots without tactile sensors.

**Architecture/Parameters:** Teacher-student architecture with tactile distillation. The teacher receives vision + language + tactile; the student uses vision + language only. Built on a VLA backbone compatible with the LeRobot ecosystem.

**Main contributions:**
- Applies the distillation paradigm (similar to FD-VLA) to tactile modality rather than F/T sensing, demonstrating the generality of the privileged-modality distillation approach.
- Targets low-cost robot platforms (LeRobot SO-101), showing that tactile knowledge can improve manipulation even on consumer-grade hardware.
- Demonstrates improved grasp success on fragile and deformable objects compared to vision-only baselines.

**Limitations/Gaps:** Paper claims code release but no public repository verified as of May 2026. The distillation removes tactile sensing entirely at deployment, losing reactive capabilities that require real-time tactile feedback. Limited to pick-and-place tasks -- no evaluation on more complex contact-rich tasks like insertion or assembly.

**Results:** Improved success rates on fragile object handling (jar, egg) tasks compared to vision-only baselines. The distillation approach transfers tactile knowledge to the vision-only student with moderate fidelity.

## Inference / Deployment

- **Inference latency:** Not explicitly reported in ms or Hz. Tactile sensor arrays operate at 120 Hz, providing the perception input rate.
- **Deployment hardware:** **NVIDIA Jetson Orin NX 16 GB** edge computer for all inference computations during real-world experiments. LeRobot SO-101 arm with tactile sensors.
- **Real-time capable?** Yes. Deployed on edge hardware (Jetson Orin NX), indicating the system is designed for real-time robotic control. The foundation model (SmolVLA) is described as "optimized for high-frequency edge deployment via asynchronous inference."

## Dataset / Data Collection

- **Dataset used:** Custom demonstration dataset for pick-and-place tasks with contact-sensitive objects (jar handling, waffle picking, egg manipulation). No named benchmark.
- **Collection method:** Demonstrations with tactile sensors (used during training, distilled away at inference). Teacher model trained with tactile input; student model learns from vision and language only via tactile distillation. The system uses "precomputed, safety-aware tactile rewards."
- **Data scale:** Not reported.
- **Teleop equipment:** Not reported. Data collected on LeRobot SO-101 arm with tactile sensors attached.
- **Data format:** Not reported.
- **Publicly available?** Paper claims code release but no public repository verified as of May 2026.

> *Dataset details from training knowledge, not verified from source -- the arXiv abstract did not disclose data specifics.*
