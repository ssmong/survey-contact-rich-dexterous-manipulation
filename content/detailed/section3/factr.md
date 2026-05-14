## 3.14 FACTR

- **Full title:** FACTR: Force-Attending Curriculum Training for Contact-Rich Robotic Manipulation
- **Authors:** RaindragonD et al. (CMU)
- **Venue/Year:** RSS 2025
- **arXiv:** https://arxiv.org/abs/2502.17432

**Force/tactile input type:** Joint torque signals derived from servo motor current readings. No external F/T or tactile sensor required -- the approach uses the Franka Panda's built-in joint torque sensing capabilities.

**Force/impedance output:** No. Position-only output. The joint torque is used as input context only.

> **Limitation (position-only output):** Position-only output; the policy cannot actively regulate contact forces despite receiving force/tactile input.

**Robot platform:** Franka Panda robotic arm + parallel-jaw gripper.

> **Limitation (gripper-only):** Evaluated only on parallel-jaw grippers; not validated on multi-finger dexterous hands.

**Tasks:** Box lifting, pivoting, and dough rolling -- contact-rich tasks requiring different force interaction modes (lifting requires grasp force, pivoting requires precise rotational torque, dough rolling requires consistent downward pressure).

**Key methodology:** FACTR introduces a curriculum training strategy for integrating force (joint torque) into visuomotor policies. The key insight is that naively adding force inputs can hurt performance due to the distribution shift between demonstration and deployment force profiles. FACTR addresses this through a force-attending curriculum: the model first learns vision-based manipulation, then gradually introduces force attention layers that learn to modulate the policy's actions based on joint torque readings. The curriculum prevents catastrophic forgetting of visual features while adding force reactivity. A force-attending transformer layer uses cross-attention between visual features and force tokens.

**Architecture/Parameters:** Transformer-based visuomotor policy with force-attending layers added via curriculum training. The force encoder processes joint torque signals into tokens that attend to visual features through cross-attention. Only the force encoder weights are publicly released.

**Main contributions:**
- Proposes curriculum training for force integration, addressing the practical challenge that naively adding force inputs can degrade performance.
- Uses joint torque (no additional sensors), making the approach applicable to any torque-controlled robot.
- Demonstrates that the force-attending curriculum improves performance on diverse contact-rich tasks (lifting, pivoting, rolling) beyond what vision alone provides.

**Limitations/Gaps:** No full model weights released (only the force encoder). Position-only output. Joint torque provides less precise contact information than dedicated F/T sensors or tactile sensors. Evaluated on 3 tasks on a single platform. The curriculum training adds complexity to the training pipeline.

**Results:**

| Metric | Value |
|--------|-------|
| Improvement over vision-only baselines | 10--30% across 3 tasks |
| Largest single-task gain | Dough rolling (consistent force application critical) |
| Curriculum vs. naive force concatenation | 15--20% improvement |

## Inference / Deployment

- **Inference latency:** Not reported. The paper does not disclose per-step inference latency or control frequency during deployment.
- **Deployment hardware:** Not specified. The policy uses a ViT encoder + MLP force encoder + transformer decoder. Franka Panda arm for real-world experiments.
- **Real-time capable?** Not verified. No quantitative latency benchmarks provided. The force-attending transformer layers add computational overhead, but the overall architecture is relatively lightweight.

## Dataset / Data Collection

- **Dataset used:** Custom demonstration dataset for 3 contact-rich tasks (box lifting, pivoting, dough rolling) on Franka Panda. No named benchmark.
- **Collection method:** Teleoperated demonstrations collected via a "low-cost, intuitive, bilateral teleoperation setup that relays external forces" -- the operator receives force feedback from the robot arm during demonstration, enabling force-sensitive data collection.
- **Data scale:** Not reported.
- **Teleop equipment:** Custom bilateral teleoperation system with force feedback relay. The operator's arm receives forces from the Franka Panda during demonstration collection.
- **Data format:** Not reported. Joint torque signals derived from servo motor current readings (Franka's built-in sensing).
- **Publicly available?** Partial. Force encoder weights released. Video results, codebase, and instructions available at jasonjzliu.com/factr/. Whether demonstration data is included is not confirmed.
