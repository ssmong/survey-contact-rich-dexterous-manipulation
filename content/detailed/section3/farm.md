## 3.19 FARM

- **Full title:** FARM: Force-Aware Robotic Manipulation with Tactile Feedback
- **Authors:** TU Munich MIRMI et al.
- **Venue/Year:** arXiv preprint, 2025
- **arXiv:** https://arxiv.org/abs/2510.13324

**Force/tactile input type:** GelSight Mini vision-based tactile sensor integrated into a modified UMI gripper.

**Force/impedance output:** Yes -- grip force prediction. The model jointly predicts end-effector position and grip force, enabling closed-loop grip force control based on tactile feedback. **Force output type: partial (grip force only, not full 6D wrench).**

**Robot platform:** Modified UMI (Universal Manipulation Interface) gripper with integrated GelSight Mini tactile sensors.

> **Limitation (gripper-only):** Evaluated only on parallel-jaw grippers; not validated on multi-finger dexterous hands.

**Tasks:** Manipulation tasks requiring coordinated position and grip force control. The model jointly predicts joint position and grip force trajectories.

**Key methodology:** FARM integrates GelSight Mini tactile sensors into the UMI gripper and learns a policy that jointly predicts position and grip force. The GelSight images are processed through a CNN encoder that extracts contact features (pressure distribution, slip detection, surface texture). These features condition a policy that outputs both joint position trajectories and grip force targets. The grip force prediction is particularly important for tasks involving fragile or deformable objects where excessive grip force can cause damage. The approach extends the UMI framework (which typically provides position-only trajectories from human demonstrations) with force awareness.

**Architecture/Parameters:** Policy model with GelSight CNN encoder, outputting joint position + grip force trajectories. Extends the UMI data collection and policy framework with tactile sensing and force prediction.

**Main contributions:**
- Extends the popular UMI manipulation framework with tactile sensing (GelSight Mini) and grip force prediction.
- Demonstrates that joint position + force prediction improves manipulation of force-sensitive objects compared to position-only UMI policies.
- Provides a practical integration of vision-based tactile sensing into an existing, widely-used manipulation framework (UMI).

**Limitations/Gaps:** No code or weights released. The grip force prediction is limited to the gripper's closing force -- it does not provide full 6D wrench control. The modified UMI gripper design may not be compatible with standard UMI hardware. Limited evaluation scope.

**Results:**

> **Quantitative results: not available.** Specific success rates or numerical comparisons could not be verified from publicly available information. The paper reports improved manipulation performance on force-sensitive tasks compared to standard UMI (position-only), and that grip force prediction enables handling fragile objects that standard UMI policies damage.

## Inference / Deployment

- **Inference latency:** Diffusion policy runs at **7 Hz** (~143 ms between high-level action predictions). The lower-level force controller operates at 25 Hz (synchronized with GelSight Mini image acquisition), and the gripper actuator operates at ~50 Hz.
- **Deployment hardware:** Franka Research 3 robot + Actuated UMI gripper with integrated GelSight Mini tactile sensors. GPU for inference not specified.
- **Real-time capable?** Yes, through hierarchical control. The 7 Hz policy provides targets that faster lower-level controllers execute at 25--50 Hz, bridging the gap between "high-level action selection and real-time motor actuation."

## Dataset / Data Collection

- **Dataset used:** Custom demonstration dataset collected via a modified UMI gripper with integrated GelSight Mini tactile sensor. No named benchmark.
- **Collection method:** Human demonstrations collected using a modified handheld Universal Manipulation Interface (UMI) gripper that integrates a GelSight Mini visual tactile sensor. The demonstrations capture both position trajectories and tactile contact information.
- **Data scale:** Not reported.
- **Teleop equipment:** Modified UMI handheld gripper with integrated GelSight Mini visual tactile sensor. The GelSight Mini provides contact images during demonstrations.
- **Data format:** Not reported. Follows the UMI framework extended with tactile data.
- **Publicly available?** Codebase and design files open-sourced at [tactile-farm.github.io](https://tactile-farm.github.io). Whether the demonstration dataset itself is publicly released is not confirmed. No pretrained weights released.
