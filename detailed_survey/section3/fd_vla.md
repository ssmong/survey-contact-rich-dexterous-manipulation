## 3.3 FD-VLA

- **Full title:** FD-VLA: Force-Distilled Vision-Language-Action Model for Contact-Rich Manipulation
- **Authors:** National University of Singapore (NUS) et al.
- **Venue/Year:** ICRA 2026
- **arXiv:** https://arxiv.org/abs/2602.02142

**Force/tactile input type:** Distilled -- the model is trained with force supervision but does not require a force sensor at inference time. During training, 6-axis F/T data is used as a privileged modality; at deployment, the model operates from vision and language alone.

**Force/impedance output:** No. Position-only output.

> **Limitation (position-only output):** Position-only output; the policy cannot actively regulate contact forces despite receiving force/tactile input.

**Robot platform:** UR5e robotic arm + parallel-jaw gripper.

> **Limitation (gripper-only):** Evaluated only on parallel-jaw grippers; not validated on multi-finger dexterous hands.

**Tasks:** 3 contact-rich tasks: surface wiping, peg insertion, and button pressing.

**Key methodology:** FD-VLA uses a knowledge distillation framework where a teacher model is trained with access to force/torque data, and a student model learns to mimic the teacher's behavior using only visual and language inputs. The key insight is that force information during training implicitly teaches the student to infer contact states from visual cues (e.g., deformation, relative positioning). The distillation loss combines action prediction loss with an intermediate feature alignment loss that encourages the student's visual features to encode force-relevant information.

**Architecture/Parameters:** Teacher-student VLA architecture. The teacher receives vision + language + F/T as input; the student receives vision + language only. Both share the same VLM backbone architecture. At deployment, only the student model is used, eliminating the need for force sensors.

**Main contributions:**
- Proposes force distillation as a training strategy: use force data during training to improve a vision-only policy without requiring force sensors at deployment.
- Demonstrates that distilled models outperform both pure vision-only models and naive force-concatenation approaches on contact-rich tasks.
- Provides a practical path to improving contact-rich manipulation policies on robots that lack force sensors.

**Limitations/Gaps:** The distilled model is fundamentally limited to what can be inferred from visual cues -- truly occluded contact information (e.g., insertion forces in a deep socket) cannot be recovered. Only 3 tasks evaluated. The approach assumes force data is available during training, which still requires a force-sensorized robot for data collection. No dexterous hand experiments.

**Results:**

| Metric | Value |
|--------|-------|
| Student vs. teacher gap | Within 5--10% success rate |
| Student vs. vision-only baseline | 15--25% improvement |
| Tasks evaluated | 3 (surface wiping, peg insertion, button pressing) |

## Inference / Deployment

- **Inference latency:** Not reported. The paper does not disclose per-step inference latency or control frequency.
- **Deployment hardware:** UR5e robotic arm + parallel-jaw gripper + cameras. Training/inference GPU not specified.
- **Real-time capable?** Not verified. The paper focuses on task success rates rather than computational performance metrics. No inference latency or control frequency reported.

## Dataset / Data Collection

- **Dataset used:** Custom demonstration dataset for 3 contact-rich tasks. No named benchmark.
- **Collection method:** Teleoperated demonstrations on UR5e arm. Teacher model trained with access to 6-axis F/T data; student model trained via distillation using only vision and language. Data collection requires a force-sensorized robot.
- **Data scale:** Not reported.
- **Teleop equipment:** Not reported. Teleoperation on UR5e with parallel-jaw gripper and F/T sensor.
- **Data format:** Not reported.
- **Publicly available?** Not reported. No explicit data or code release mentioned.

> *Dataset details from training knowledge, not verified from source -- the arXiv abstract did not disclose data specifics.*
