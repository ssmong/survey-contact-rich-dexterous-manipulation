## 3.9 TaF-VLA

- **Full title:** TaF-VLA: Tactile and Force Vision-Language-Action Model for Contact-Rich Manipulation
- **Authors:** Not specified in survey table
- **Venue/Year:** arXiv preprint, 2026
- **arXiv:** https://arxiv.org/abs/2601.20321

**Force/tactile input type:** Dual-modality force sensing: GelSight vision-based tactile sensor + 6-axis F/T sensor. Both modalities are processed and fused within the VLA framework, providing complementary contact information (local surface contact from GelSight and global wrench from F/T sensor).

**Force/impedance output:** No. Position-only output.

> **Limitation (position-only output):** Position-only output; the policy cannot actively regulate contact forces despite receiving force/tactile input.

**Robot platform:** Franka FR3 robotic arm + parallel-jaw gripper with GelSight and F/T sensors.

> **Limitation (gripper-only):** Evaluated only on parallel-jaw grippers; not validated on multi-finger dexterous hands.

**Tasks:** 8 contact-rich manipulation tasks spanning a range of contact modalities.

**Key methodology:** TaF-VLA fuses two complementary force/tactile modalities within a unified VLA framework. The GelSight sensor provides high-resolution local contact geometry (surface deformation, slip detection), while the 6-axis F/T sensor provides global interaction wrench information. Separate encoders process each modality: a CNN-based encoder for GelSight images and an MLP encoder for F/T signals. The encoded features are fused through cross-attention with visual and language tokens in the VLM backbone. The dual-modality design aims to capture both fine-grained contact properties (from GelSight) and global force trends (from F/T).

**Architecture/Parameters:** VLA backbone with dual tactile/force encoders -- a CNN encoder for GelSight tactile images and an MLP encoder for 6-axis F/T readings. Both are projected into the VLM embedding space and fused via cross-attention.

**Main contributions:**
- Proposes joint fusion of vision-based tactile and F/T sensing within a VLA, demonstrating that the two modalities provide complementary information for contact-rich tasks.
- Evaluates on 8 diverse contact-rich tasks, the largest task set among force-aware VLA papers.
- Ablation studies demonstrate that the dual-modality (tactile + F/T) fusion outperforms either single modality alone.

**Limitations/Gaps:** No code or weights released. Position-only output despite rich force/tactile input. The requirement for both GelSight and F/T sensors increases hardware cost and complexity. Evaluated only on Franka FR3 with no cross-platform experiments. The dual-sensor requirement limits practical applicability.

**Results:** The dual-modality (GelSight + F/T) model outperforms single-modality variants across the 8 tasks. The complementary nature of local tactile and global force information is most beneficial on tasks with varied contact geometries.

## Inference / Deployment

- **Inference latency:** Not explicitly reported in Hz or ms. The authors acknowledge that "predicting a long horizon of future actions ensures trajectory smoothness, [but] it inherently limits the frequency of closed-loop corrections" and that "force interactions are inherently fast, highlighting the need for architectures capable of faster inference."
- **Deployment hardware:** NVIDIA RTX 4090 workstation for inference. Franka FR3 arm + parallel-jaw gripper with GelSight and F/T sensors.
- **Real-time capable?** Partially. Deployed on RTX 4090 but the authors explicitly identify real-time control frequency as an unmet need, noting the policy "exhibits latency and is prone to failure during high-frequency dynamic events." The receding-horizon action output limits closed-loop correction frequency.

## Dataset / Data Collection

- **Dataset used:** TaF-Dataset (custom dataset released with this work). Features synchronized dual-modality force/tactile data.
- **Collection method:** Automated tactile-force data acquisition device (custom hardware). The system automatically collects synchronized GelSight vision-based tactile observations, 6-axis force/torque readings, and matrix force maps.
- **Data scale:** Over 10 million synchronized tactile observations, 6-axis F/T readings, and matrix force maps.
- **Teleop equipment:** Not applicable (automated data acquisition device, not teleoperation).
- **Data format:** Synchronized multi-modal: GelSight tactile images + 6-axis F/T signals + force map data.
- **Publicly available?** Not confirmed. The arXiv abstract does not specify whether the TaF-Dataset is publicly released.
