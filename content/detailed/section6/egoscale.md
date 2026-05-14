### EgoScale: Scaling Egocentric Human Video Pre-training for Dexterous Robot Manipulation

**Full title:** Scaling Manipulation Learning with Visual Kinematic Chain Prediction

**Authors:** Xinyu Zhang, Yifu Lu, Haozhan Yang, Yifan Guo, Liang Zhao, Yuke Zhu, Linxi "Jim" Fan (NVIDIA Research / UC Berkeley)

**Venue/Year:** arXiv 2026

**Architecture:** EgoScale introduces a pretraining framework that converts egocentric human video into training data for robot manipulation. It uses a visual kinematic chain representation that tracks human hand and object poses from video, converting them into 22-DoF Sharpa hand action representations. The VLA architecture builds on the GR00T framework with a vision-language backbone and diffusion transformer action head. The key architectural contribution is the hand-object pose estimation pipeline, not a new VLA architecture.

**Action space:** 22-DoF (Sharpa hand representation) extracted from human hand pose tracking in egocentric video. This captures finger articulation, wrist pose, and object interactions.

**Dex hand support?** Partial (representation only). The 22-DoF Sharpa hand representation models multi-finger configurations during human video pretraining, but deployment on a physical 22-DoF dexterous robot hand has not been demonstrated. The dexterous capability is at the representation level (video pose extraction), not physical robot deployment. The pipeline extracts 22-DoF hand poses from human video and uses them as pseudo-labels for pretraining, but the downstream transfer to an actual multi-finger robot hand performing contact-rich manipulation is not validated in the paper.

**Force/impedance output?** ✗ --- Position targets derived from visual pose estimation; no force information.

**Key methodology:** EgoScale addresses the data scarcity problem for dexterous manipulation by leveraging the massive scale of human egocentric video. It trains a visual kinematic chain predictor to extract 22-DoF hand action labels from unlabeled human video, then uses these pseudo-labels to pretrain a robot manipulation policy. The approach demonstrates a dexterous manipulation scaling law: performance improves log-linearly with the amount of human video pretraining data, up to 20K hours. This human video pretraining was subsequently integrated into GR00T N1.7.

**Training data:** 20,000 hours of human egocentric video (Ego4D, Ego-Exo4D, and proprietary sources). Robot fine-tuning data from multiple platforms.

**Main contributions:**
- Demonstrated a scaling law for dexterous manipulation: log-linear improvement with human video pretraining scale up to 20K hours.
- Introduced a pipeline for extracting 22-DoF dexterous hand action labels from unlabeled egocentric video.
- Showed that human video pretraining transfers to robot manipulation, bridging the embodiment gap between human hands and robot end-effectors.

**Quantitative results:**

| Benchmark / Task | EgoScale (20K hrs) | Without Pretraining | Notes |
|---|---|---|---|
| *(Consult the arXiv paper for scaling law curves and per-task results. The paper reports log-linear improvement in downstream manipulation performance with pretraining data scale.)* | | | |

**Limitations/Gaps:**
- **Critical: physical dex hand deployment not validated.** Whether the video-derived 22-DoF representation transfers to actual multi-finger robot hand control has not been validated. The 22-DoF Sharpa hand representation is used during pretraining (extracting poses from human video), but the paper does not demonstrate deployment on a physical 22-DoF dexterous robot hand performing autonomous manipulation. The dexterous capability remains at the representation level.
- The 22-DoF representation is tied to the Sharpa hand morphology; adaptation to other hand designs requires re-retargeting.
- No force information is captured from video --- contact forces during manipulation are unobserved.
- Neither code nor weights have been publicly released.
- The extracted hand poses from video are noisy and may not capture fine-grained finger contacts accurately.

**Open weights/code:** ✗ --- Not publicly released as of May 2026.

## Inference / Deployment

- **Inference latency:** Not reported. EgoScale is primarily a pretraining framework (hand pose extraction from video), not a standalone inference system. The downstream VLA (built on GR00T framework) inherits the inference characteristics of GR00T N1.7 (~2.9-4.6 Hz on Jetson Orin).
- **Deployment hardware:** The pose extraction pipeline processes video offline. The downstream VLA deployment follows GR00T N1.7 specifications.
- **Real-time capable?** Not applicable for the pretraining pipeline (offline video processing). Downstream VLA deployment inherits GR00T N1.7 real-time characteristics.

## Dataset / Data Collection

- **Dataset used:** 20,000 hours of human egocentric video from Ego4D, Ego-Exo4D, and proprietary NVIDIA sources. Robot fine-tuning data from multiple platforms.
- **Collection method:** Human egocentric video (passive observation, no teleoperation) processed through a visual kinematic chain predictor that extracts 22-DoF Sharpa hand action pseudo-labels from unlabeled video. Robot fine-tuning uses teleoperated demonstrations on target platforms.
- **Data scale:** 20,000 hours of human video for pretraining. Robot fine-tuning scale varies. Demonstrated scaling law: log-linear performance improvement up to 20K hours.
- **Teleop equipment:** Not applicable for video pretraining (passive human video). Robot fine-tuning uses platform-specific teleoperation.
- **Data format:** Extracted 22-DoF hand pose trajectories from video as pseudo-labels. Raw video from Ego4D (publicly available) and proprietary sources.
- **Publicly available?** Partially. Ego4D and Ego-Exo4D are publicly available datasets. Proprietary NVIDIA video data and extracted pseudo-labels are not released. EgoScale code/weights not released.

---
