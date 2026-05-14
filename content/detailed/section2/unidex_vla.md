### 2.1 UniDex-VLA

**Full title:** UniDex-VLA: A Universal Dexterous Manipulation Framework with Vision-Language-Action Model

**Authors:** Chen, Y. et al. (UniDex-AI)

**Venue/Year:** CVPR 2026

**arXiv:** [2603.22264](https://arxiv.org/abs/2603.22264)

**Hand hardware:** 8 dexterous robot hands via the Fingertip-Aligned Action Space (FAAS): Allegro (16 DoF), LEAP (16 DoF), Shadow (24 DoF), Inspire (12 DoF), Wuji, Oymotion, Ability, and Xhand. FAAS projects arbitrary hand kinematics into a unified fingertip-centric representation, enabling a single policy to control all eight hands without per-embodiment fine-tuning.

**Tasks:**
- Tool use (hammer, screwdriver, spatula)
- Object grasping and reorientation
- Pick-and-place manipulation
- Articulated object manipulation

**Key methodology:** UniDex-VLA combines a 3D VLA backbone with a flow-matching action head. The core innovation is FAAS (Fingertip-Aligned Action Space), a cross-embodiment action representation that maps heterogeneous hand joint spaces to a shared fingertip-centric coordinate frame. Language instructions condition the policy via the VLA's language encoder, enabling task specification through natural language. The 3D representation provides spatial grounding for precise finger-object interactions.

**Architecture/Parameters:**
- VLA backbone: 3D vision-language model (specific backbone size not publicly disclosed as of the survey date)
- Action head: flow-matching generative model
- Action space: FAAS unified representation across 8 hand embodiments
- Training data: 9M frames, 50K+ trajectories across 8 hand types (UniDex dataset)

**Main contributions:**
- FAAS (Fingertip-Aligned Action Space): a novel cross-embodiment action representation that unifies 8 different dexterous hands into a single policy, removing the need for per-hand fine-tuning
- Among the first VLAs to demonstrate cross-hand generalization (8 platforms, per authors' claim), achieving 81% task progress across 8 physically different hand platforms
- Release of the UniDex dataset (9M frames, 50K+ trajectories) and pretrained model weights (3-epoch and 32-epoch checkpoints on HuggingFace)

**Limitations/Gaps:**
- Outputs position targets only; no force or impedance output despite targeting contact-rich tool-use tasks
- FAAS reduces diverse hand kinematics to fingertip poses, potentially losing intra-finger dexterity for tasks requiring specific joint configurations (e.g., power grasps, finger gaiting)
- Primary evaluation is in simulation; real-world deployment across all 8 hands not demonstrated
- No tactile or force/torque sensing integration

**Results:**

| Metric | Value | Notes |
|---|---|---|
| Average task progress | 81% | Across 8 dexterous hand embodiments |
| Hands evaluated | 8 | DoF range: 12 (Inspire) to 24 (Shadow) |
| Training data | 9M frames, 50K+ trajectories | UniDex dataset |
| Cross-hand transfer | Zero-shot | Single trained policy controls all 8 hands |

> **[EDITORIAL NOTE -- metric ambiguity]:** The reported "81% task progress" metric is ambiguous. It is unclear whether this is a binary task success rate (fraction of tasks completed) or a continuous progress metric (average percentage of task completion across episodes, where partial completions contribute fractionally). The paper should be consulted directly to resolve this distinction, as the two interpretations imply very different levels of performance. If continuous progress, the effective binary success rate may be substantially lower.

- Pretrained weights publicly available (3-epoch and 32-epoch on HuggingFace)
- Code released at [GitHub](https://github.com/unidex-ai/UniDex)

> **[EDITORIAL NOTE -- results verification needed]:** Per-task and per-hand breakdowns of the 81% figure were not extractable from the abstract. The full paper should be consulted for disaggregated results by task type and hand embodiment.

## Inference / Deployment

- **Inference latency:** Not reported. The paper does not disclose per-step inference latency or control frequency.
- **Deployment hardware:** Training uses 8 NVIDIA H800 GPUs (total batch size 128 for pretraining; 2 H800 GPUs per task for post-training). Real-world setup uses a 7-DoF Franka arm with three dexterous end-effectors and Intel RealSense L515 for egocentric RGB-D. Inference GPU not specified.
- **Real-time capable?** Not verified. Training hardware (H800) is disclosed but inference hardware and latency are not reported, making real-time capability assessment impossible from public information.

## Dataset / Data Collection

- **Dataset used:** UniDex-Dataset (custom, robot-centric dataset constructed for this work). Also uses UniDex-Cap, a portable capture setup enabling human-robot data co-training.
- **Collection method:** Human-in-the-loop retargeting from egocentric human video datasets. Researchers employed a retargeting procedure to align fingertip trajectories while preserving plausible hand-object contacts. Operates on 3D point clouds with human hands masked to narrow kinematic and visual gaps between human and robot data.
- **Data scale:** 9M frames, 50K+ trajectories across 8 dexterous hand types (DoF range: 12 to 24).
- **Teleop equipment:** UniDex-Cap portable capture setup (details in paper). Source data from egocentric human video, retargeted to robot embodiments.
- **Data format:** Synchronized RGB-D streams and human hand poses converted into robot-executable trajectories through FAAS (Fingertip-Aligned Action Space).
- **Publicly available?** Pretrained weights (3-epoch and 32-epoch checkpoints) on HuggingFace. Code at [GitHub](https://github.com/unidex-ai/UniDex). Whether the UniDex-Dataset itself is publicly released is not confirmed in available materials.
