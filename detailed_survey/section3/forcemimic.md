## 3.15 ForceMimic

> **Note:** This is not a VLA (no language conditioning). Included in Section 3 for its force-output methodology, which is directly relevant to force-aware manipulation policy design.

- **Full title:** ForceMimic: Force-Centric Imitation Learning with Force-Motion Capture System for Contact-Rich Manipulation
- **Authors:** SJTU / Flexiv et al.
- **Venue/Year:** ICRA 2025
- **arXiv:** https://arxiv.org/abs/2410.07554

**Force/tactile input type:** Captured interaction wrench from a custom force-motion capture system that records both the human demonstrator's motions and the interaction forces during teleoperation.

**Force/impedance output:** Yes -- wrench-position hybrid output. The model predicts both desired end-effector positions and desired interaction wrenches, enabling a hybrid controller that actively regulates contact forces. **Force output type: full wrench (6D).**

**Robot platform:** Flexiv Rizon robotic arm + parallel-jaw gripper.

> **Limitation (gripper-only):** Evaluated only on parallel-jaw grippers; not validated on multi-finger dexterous hands.

**Tasks:** Vegetable peeling as the primary evaluation task -- a challenging contact-rich task requiring precise force control to peel without damaging the vegetable.

**Key methodology:** ForceMimic introduces a force-motion capture system that records both kinematic trajectories and interaction forces during human demonstrations. Unlike standard teleoperation that captures only positions, this system uses F/T sensors to record the forces the demonstrator applies during contact-rich tasks. The imitation learning policy then learns to predict both position and force targets, enabling a hybrid force-position controller that actively regulates contact. The hybrid imitation learning (HybridIL) formulation treats force and position as jointly predicted quantities, with separate loss terms for position tracking and force tracking.

**Architecture/Parameters:** Imitation learning policy trained on force-augmented demonstrations. The policy outputs both position targets and wrench targets. A hybrid force-position controller executes both targets simultaneously.

**Main contributions:**
- Introduces a force-motion capture system that captures both motions and forces during demonstrations, providing richer supervision for contact-rich imitation learning.
- Proposes HybridIL, a hybrid imitation learning formulation that jointly predicts position and force targets, enabling active force regulation.
- Demonstrates that hybrid force-position imitation significantly outperforms position-only imitation on vegetable peeling, where precise force control is critical.

**Limitations/Gaps:** Evaluated on a single task (vegetable peeling). The force-motion capture system adds hardware cost and complexity to the demonstration process. No VLA/language conditioning -- this is a visuomotor policy with force, not a full VLA. Code released (github.com/ForceMimic/hybridil) but no pretrained weights.

**Results:** ForceMimic achieves significantly higher success rates on vegetable peeling compared to position-only imitation learning baselines. The hybrid force-position output is critical for maintaining consistent peeling forces without cutting through or leaving too much skin.

## Inference / Deployment

- **Inference latency:** Not reported. The paper does not disclose per-step inference latency or control frequency during deployment. Data collection uses various sensor rates (F/T sensor at 1000 Hz, SLAM camera at 200 Hz, RGB-D at 30 Hz), but these are acquisition rates, not deployment specifications.
- **Deployment hardware:** Flexiv Rizon arm + parallel-jaw gripper with the ForceCapture system (custom F/T sensor integration). Inference hardware not specified.
- **Real-time capable?** Not verified. The hybrid force-position controller requires real-time execution, but specific inference latency figures are not provided.

## Dataset / Data Collection

- **Dataset used:** Custom demonstrations collected via the ForceCapture system (custom force-motion capture hardware). Focused on vegetable peeling tasks.
- **Collection method:** Human demonstrations collected using the ForceCapture system, which simultaneously records both kinematic trajectories and interaction wrenches during teleoperation. The system enables an operator to complete a vegetable peeling demonstration in ~5 minutes (vs. 13+ min with traditional force-feedback teleoperation).
- **Data scale:** Not explicitly reported. The paper focuses on the vegetable peeling task.
- **Teleop equipment:** ForceCapture system -- a custom force-motion capture system integrating F/T sensor (1000 Hz), SLAM camera (200 Hz), and RGB-D camera (30 Hz) for synchronized force-motion recording during demonstrations.
- **Data format:** Not reported. Processed dataset available for download.
- **Publicly available?** Yes. Processed dataset available via Google Drive. Code at [GitHub](https://github.com/ForceMimic/hybridil). ForceCapture system at [GitHub](https://github.com/ForceMimic/forcecapture). No pretrained weights released.
