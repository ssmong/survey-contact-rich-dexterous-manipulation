## 3.17 ACP

> **Note:** This is not a VLA (no language conditioning). Included in Section 3 for its force-output methodology, which is directly relevant to force-aware manipulation policy design.

- **Full title:** ACP: Adaptive Compliance Policy for Contact-Rich Manipulation with Impedance Control
- **Authors:** Toyota Research Institute / Columbia University et al.
- **Venue/Year:** ICRA 2025
- **arXiv:** https://arxiv.org/abs/2410.09309

**Force/tactile input type:** 6-axis F/T sensor (ATI industrial-grade sensor) providing high-precision force/torque measurements.

**Force/impedance output:** Yes -- outputs a scalar stiffness parameter that modulates the robot's impedance controller. The policy learns to adapt the compliance level based on the task phase and contact state. **Force output type: partial (scalar stiffness only).**

**Robot platform:** UR5e robotic arm + passive tool attachments (e.g., spatula, sponge).

> **Limitation (gripper-only):** Evaluated only on parallel-jaw grippers; not validated on multi-finger dexterous hands.

**Tasks:** Item flipping (using a spatula) and vase wiping -- tasks requiring variable compliance: high stiffness for free-space motion and tool positioning, low stiffness for compliant contact during interaction.

**Key methodology:** ACP learns an adaptive compliance policy that outputs both position targets and a scalar stiffness parameter for the robot's impedance controller. The stiffness parameter dynamically adjusts the robot's compliance -- stiffer during precise positioning phases and more compliant during contact phases. The policy is trained through imitation learning on demonstrations where the demonstrator's varying grip force is recorded via the ATI F/T sensor as a proxy for desired compliance. The scalar stiffness modulates all Cartesian directions uniformly.

**Architecture/Parameters:** Imitation learning policy with position + scalar stiffness output. The stiffness output is a single scalar that uniformly scales the Cartesian impedance controller's stiffness matrix. Input includes visual observation and 6-axis F/T readings.

**Main contributions:**
- Proposes learning adaptive compliance alongside position targets, enabling the robot to dynamically adjust its stiffness based on task phase.
- Demonstrates that even a single scalar stiffness parameter significantly improves contact-rich task performance compared to fixed-compliance baselines.
- Shows practical applications (item flipping, vase wiping) where variable compliance is essential for task success.

**Limitations/Gaps:** No code or weights released. The scalar stiffness output is a simplification -- real tasks may require per-axis or per-direction stiffness adaptation. Only 2 tasks evaluated. Not a VLA model (no language conditioning). The use of passive tools (spatula, sponge) limits the generalization to tasks requiring active tool manipulation.

**Results:** ACP with adaptive compliance achieves higher success rates on item flipping and vase wiping compared to fixed-stiffness baselines. The learned stiffness profile shows intuitive patterns: high stiffness during positioning, low stiffness during contact.

## Inference / Deployment

- **Inference latency:** Not reported. The paper specifies sensor/actuator rates (GoPro at 60 Hz, robot Cartesian commands at 500 Hz, ATI F/T sensor at up to 7000 Hz) but does not disclose the policy's inference latency or decision frequency.
- **Deployment hardware:** UR5e robotic arm + passive tool attachments (spatula, sponge) + ATI F/T sensor + GoPro camera. Inference GPU not specified.
- **Real-time capable?** Not verified. The underlying robot and sensor infrastructure supports high-frequency control (500 Hz pose commands, 7000 Hz F/T), but the policy's computational latency is not quantified.

## Dataset / Data Collection

- **Dataset used:** Custom human demonstration dataset for 2 contact-rich tasks (item flipping, vase wiping). No named benchmark.
- **Collection method:** Human demonstrations on UR5e arm. The demonstrator's varying grip force is recorded via ATI F/T sensor as a proxy for desired compliance. Demonstrations capture both kinematic trajectories and interaction forces.
- **Data scale:** Not reported.
- **Teleop equipment:** Not explicitly detailed. Demonstrations collected on UR5e with ATI industrial-grade F/T sensor (up to 7000 Hz) and GoPro camera (60 Hz).
- **Data format:** Not reported.
- **Publicly available?** No. No code, data, or weights released.
