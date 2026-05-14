## 3.18 TacDiffusion

- **Full title:** TacDiffusion: Environment-Aware Tactile-Conditioned Diffusion Policy for Contact-Rich Manipulation
- **Authors:** popnut123 et al. (TU Munich MIRMI)
- **Venue/Year:** ICRA 2025
- **arXiv:** https://arxiv.org/abs/2409.11047

**Force/tactile input type:** Tactile sensor providing contact information for grasp and manipulation feedback.

**Force/impedance output:** Yes -- 6D wrench output. The diffusion policy generates desired 6D wrenches (3 forces + 3 torques) as the action representation, operating in force space rather than position space. **Force output type: full wrench (6D).**

**Robot platform:** Gripper with integrated tactile sensor.

> **Limitation (gripper-only):** Evaluated only on parallel-jaw grippers; not validated on multi-finger dexterous hands.

**Tasks:** Contact-rich manipulation tasks evaluated in a force-domain diffusion framework.

**Key methodology:** TacDiffusion is a diffusion policy that operates in the force/wrench domain rather than the position domain. The model generates 6D wrench targets conditioned on tactile observations and environmental context. This force-domain formulation is naturally suited for contact-rich tasks where the desired behavior is better described in terms of forces (e.g., "apply 5N downward while sliding laterally") rather than positions. The diffusion model generates multi-modal wrench distributions, allowing the policy to represent diverse force interaction strategies. An environment-aware conditioning mechanism adjusts the force policy based on the estimated contact geometry and surface properties.

**Architecture/Parameters:** Diffusion policy with force/wrench action space (6D output). The model is conditioned on tactile observations and environmental context. The diffusion process generates wrench trajectories.

**Main contributions:**
- Proposes diffusion policy in force space, a fundamental shift from position-based diffusion policies that better represents contact-rich manipulation.
- Achieves 95.7% zero-shot transfer success rate, demonstrating that force-domain policies can generalize to novel scenarios.
- Introduces environment-aware conditioning that adapts force generation based on estimated contact geometry.

**Limitations/Gaps:** Code released (GitHub) but no pretrained weights. The force-domain formulation requires a robot with accurate force control capabilities. Evaluated primarily on gripper-based tasks -- no dexterous hand experiments. The 6D wrench output assumes a single contact point; multi-contact scenarios (as in dexterous manipulation) would require per-finger wrench generation.

**Results:**

| Metric | Value |
|--------|-------|
| Zero-shot transfer success rate | 95.7% |
| vs. position-domain diffusion policies | Force-domain formulation outperforms on tasks requiring precise force interaction |

## Inference / Deployment

- **Inference latency:** Depends on model size. DF1 (128 neurons): 503.8 Hz; DF2 (256 neurons): 297.5 Hz; **DF3 (512 neurons, selected): 141.8 Hz**; DF4 (1024 neurons): 51.2 Hz. The robot control loop operates at 1000 Hz, requiring a dynamic system-based filter to interpolate predictions and bridge the frequency gap.
- **Deployment hardware:** NVIDIA RTX 3090 GPU with PyTorch and ONNX optimization for inference. Real-time control PC with Intel i9-10900K CPU running Ubuntu 20.04 with real-time kernel.
- **Real-time capable?** Yes. The selected model (DF3) achieves 141.8 Hz inference, though below the 1000 Hz robot control loop -- bridged by a dynamic system-based filter for interpolation. This is among the fastest inference rates in the surveyed literature, enabled by the relatively small diffusion model operating in force space.

## Dataset / Data Collection

- **Dataset used:** Custom dataset for peg-in-hole assembly tasks with tactile feedback. Expert policies with primitive-switching logic generate the training data.
- **Collection method:** Expert policy rollouts for high-precision assembly tasks. Data generated from expert policies containing primitive-switching logic, not from human teleoperation.
- **Data scale:** Not explicitly reported.
- **Teleop equipment:** Not applicable (expert policy rollouts, not teleoperation).
- **Data format:** Stored in `$TacDiffusion_ROOT/dataset/` directory. Specific file format not documented.
- **Publicly available?** Yes. Dataset available on Google Drive ([TacDiffusion Dataset](https://drive.google.com/drive/folders/10Ix8utcx51R8NejvGRF-ujWEGy5MK05R)). Code at GitHub. Note: "No commercial use!" license restriction.
