## 3.6 DreamTacVLA

- **Full title:** Learning to Feel the Future: Tactile World Model for Contact-Rich VLA Policy
- **Authors:** Northwestern University et al.
- **Venue/Year:** arXiv preprint, 2025
- **arXiv:** https://arxiv.org/abs/2512.23864

**Force/tactile input type:** Vision-based tactile sensors. Tactile images are processed through V-JEPA2 (a self-supervised visual encoder) to extract tactile latent representations rather than using raw tactile images directly.

**Force/impedance output:** No. Position-only action output. However, the model internally predicts future tactile latent states (a tactile world model) that are used to refine action predictions.

> **Limitation (position-only output):** Position-only output; the policy cannot actively regulate contact forces despite receiving force/tactile input.

**Robot platform:** Dobot Xtrainer robotic arm + gripper + vision-based tactile sensor.

> **Limitation (gripper-only):** Evaluated only on parallel-jaw grippers; not validated on multi-finger dexterous hands.

**Tasks:** 4 contact-rich manipulation tasks requiring tactile feedback for success. Tasks are designed to evaluate whether predicting future tactile states improves manipulation performance.

**Key methodology:** DreamTacVLA introduces a tactile world model that predicts future tactile latent representations conditioned on the current state and planned actions. The V-JEPA2 encoder processes raw tactile images into compact latent vectors. A world model module (transformer-based) learns to predict how the tactile latent will evolve given a candidate action sequence. This predicted future tactile state is then used to refine action predictions -- effectively allowing the policy to "feel the future" and avoid actions that would lead to undesirable contact states (e.g., excessive force, slip).

**Architecture/Parameters:** VLA backbone + V-JEPA2 tactile encoder + transformer-based tactile world model. The V-JEPA2 encoder is pretrained on large-scale visual data and fine-tuned on tactile images. The world model predicts future tactile latents, which are fed back into the action decoder for refinement.

**Main contributions:**
- Introduces a tactile world model that predicts future contact states, enabling proactive (rather than reactive) contact-rich manipulation.
- Uses V-JEPA2 as a tactile encoder, demonstrating that pretrained visual SSL models can effectively encode tactile image information.
- Shows that predicting future tactile states and conditioning actions on these predictions improves success rates on contact-rich tasks compared to both tactile-unaware and reactive-only tactile approaches.

**Limitations/Gaps:** No model weights released (code only at GitHub repository). The tactile world model adds computational overhead to inference. Limited to 4 tasks on a single robot platform. The V-JEPA2 encoder was designed for natural images and may not optimally encode tactile signals. The approach assumes vision-based tactile sensors (e.g., GelSight-style) and does not generalize to other tactile sensor modalities.

**Results:**

| Metric | Value |
|--------|-------|
| Best success rate | Up to 95% across 4 contact-rich tasks |
| Improvement over reactive-only tactile | 10--20% |

## Inference / Deployment

- **Inference latency:** Control loop runs at **50 Hz** (matching data collection frequency). The Think-Dream-Act pipeline adds inference overhead; the authors acknowledge this and suggest "policy distillation and adaptive dreaming for faster single-pass reasoning" as future work.
- **Deployment hardware:** Training on a single NVIDIA GPU (model not specified; ~8--12 hours for 20K steps). Dobot Xtrainer arm + gripper + vision-based tactile sensor. Inference GPU not separately specified.
- **Real-time capable?** Partially. The 50 Hz control rate is maintained, but the two-stage pipeline (world model prediction + action generation) introduces computational overhead. The authors explicitly flag inference speed as a limitation.

## Dataset / Data Collection

- **Dataset used:** Hybrid large-scale dataset combining high-fidelity digital twin simulation data and real-world experimental data. Constructed to mitigate tactile data scarcity and the wear-prone nature of tactile sensors.
- **Collection method:** Hybrid approach: (1) digital twin simulation generating synthetic tactile data, and (2) real-world experiments with vision-based tactile sensors (GelSight-style). Data collected at 50 Hz.
- **Data scale:** Not explicitly reported.
- **Teleop equipment:** Not reported. Data collected on Dobot Xtrainer arm with gripper and vision-based tactile sensor.
- **Data format:** Not reported.
- **Publicly available?** Code available (GitHub repository referenced). No model weights released. Dataset availability not confirmed.
