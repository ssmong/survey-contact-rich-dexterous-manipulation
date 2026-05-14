## 3.16 Reactive Diffusion Policy

- **Full title:** Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation
- **Authors:** xiaoxiaoxh et al.
- **Venue/Year:** RSS 2025
- **arXiv:** https://arxiv.org/abs/2503.02881

**Force/tactile input type:** GelSight Mini vision-based tactile sensor providing high-resolution contact images at each fingertip of the gripper.

**Force/impedance output:** No explicit force/impedance output, but the policy learns "impedance-like" reactive behavior. The diffusion policy generates position actions that implicitly encode compliant behavior conditioned on tactile feedback, producing motions that adapt to contact states as an impedance controller would.

> **Limitation (position-only output):** Position-only output; the policy cannot actively regulate contact forces despite receiving force/tactile input.

**Robot platform:** Flexiv Rizon 4 robotic arm + parallel-jaw gripper equipped with GelSight Mini sensors.

> **Limitation (gripper-only):** Evaluated only on parallel-jaw grippers; not validated on multi-finger dexterous hands.

**Tasks:** 3 contact-rich manipulation tasks that require reactive tactile behavior.

**Key methodology:** Reactive Diffusion Policy introduces a slow-fast architecture for visual-tactile policy learning. The "slow" pathway processes visual observations through a diffusion policy to generate coarse action plans. The "fast" pathway processes tactile (GelSight Mini) images at high frequency to generate reactive corrections to the slow plan. The fast pathway acts like a learned impedance controller -- it adjusts the robot's motion in response to contact events detected through tactile images, without explicitly computing or commanding forces. The diffusion policy framework enables multi-modal action distributions, allowing the policy to represent diverse reactive strategies.

**Architecture/Parameters:** Dual-speed diffusion policy: slow visual pathway (standard diffusion policy inference rate) + fast tactile pathway (higher-frequency reactive corrections). The tactile pathway is a lightweight network that processes GelSight Mini images and outputs position corrections.

**Main contributions:**
- Proposes a slow-fast architecture that separates visual planning (slow) from tactile reaction (fast), matching the natural timescales of visual and tactile perception.
- Demonstrates that the fast tactile pathway learns impedance-like reactive behavior without explicit force control, providing compliance through learned position corrections.
- Releases code and checkpoints publicly (GitHub and HuggingFace), supporting reproducibility.

**Limitations/Gaps:** Position-only output despite the impedance-like behavior. The learned reactive corrections may not generalize to force ranges outside the training distribution. Limited to 3 tasks. Requires GelSight Mini sensors, which add cost and fragility.

**Results:** The slow-fast architecture outperforms both tactile-unaware diffusion policies and single-speed tactile diffusion policies across 3 contact-rich tasks. Code and model checkpoints available at GitHub (github.com/xiaoxiaoxh/reactive_diffusion_policy) and HuggingFace.

## Inference / Deployment

- **Inference latency:** Fast policy (Asymmetric Tokenizer): **<1 ms** per step (theoretical >300 Hz). Slow policy (Latent Diffusion Policy): **~100 ms** per step (~1--2 Hz for high-level planning). Combined system operates at **24 FPS** during experiments (matching tactile sensor constraints).
- **Deployment hardware:** NVIDIA RTX 4090 GPU + Intel Core i9-14900K CPU. Flexiv Rizon 4 arm + parallel-jaw gripper with GelSight Mini sensors.
- **Real-time capable?** Yes. The hierarchical slow-fast design enables genuine closed-loop reactivity: the fast network provides sub-millisecond tactile/force feedback control while the slow network handles complex trajectory modeling at lower frequency. This is one of the fastest reactive systems in the surveyed literature.

## Dataset / Data Collection

- **Dataset used:** Custom demonstration dataset for 3 contact-rich tasks. No named benchmark.
- **Collection method:** Teleoperated demonstrations collected via TactAR, a VR-based teleoperation system using the Meta Quest 3 headset that provides real-time tactile feedback through augmented reality. Multi-sensor data recorded at 24 fps across visual and tactile modalities.
- **Data scale:** Example dataset contains 25,710 timesteps (publicly released on HuggingFace). Full training dataset scale not explicitly reported.
- **Teleop equipment:** TactAR system with Meta Quest 3 VR headset, two robot arms (Flexiv Rizon 4 or Franka Research 3), RealSense D435/D415 cameras, and optional GelSight Mini tactile sensors.
- **Data format:** Zarr format. Contains: action, RGB images, tactile embeddings, gripper state, TCP poses/velocities, forces, and timestamps organized hierarchically by sensor/robot.
- **Publicly available?** Yes. Dataset on HuggingFace ([WendiChen/reactive_diffusion_policy_dataset](https://huggingface.co/datasets/WendiChen/reactive_diffusion_policy_dataset)). Model checkpoints on HuggingFace ([WendiChen/reactive_diffusion_policy_model](https://huggingface.co/WendiChen/reactive_diffusion_policy_model)). Code at [GitHub](https://github.com/xiaoxiaoxh/reactive_diffusion_policy).
