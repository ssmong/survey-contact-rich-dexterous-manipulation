### 2.3 DexVLA

**Full title:** DexVLA: Vision-Language Model with Plug-In Diffusion Expert for Dexterous Manipulation

**Authors:** Junjie Wen, Yichen Zhu, Jinming Li, Zhibin Tang, Chaomin Shen, Feifei Feng

**Venue/Year:** CoRL 2025

**arXiv:** [2502.05855](https://arxiv.org/abs/2502.05855)

**Hand hardware:** Inspired Dexterous Hand (6 DoF hand joints) mounted on a Franka Emika robot arm. Action space is 12-dimensional: SE(3) end-effector pose (3D position + 3D orientation) plus 6D hand joint space. Cross-embodiment evaluation also covers single-arm gripper and bimanual UR5e setups.

**Tasks:**
- Dexterous skill learning via curriculum
- Multi-finger manipulation tasks
- Pick-and-place with dexterous hands
- In-hand manipulation

**Key methodology:** DexVLA introduces a plug-in architecture that attaches a 1-billion-parameter diffusion expert to a frozen vision-language model. The VLM backbone provides visual understanding and language grounding while remaining frozen during dexterous training. The diffusion expert generates high-dimensional dexterous hand actions conditioned on the VLM's latent representations. This design avoids catastrophic forgetting of the VLM's pre-trained knowledge while enabling precise dexterous control. A curriculum learning strategy progressively increases task difficulty.

**Architecture/Parameters:**
- VLM backbone: frozen pre-trained vision-language model (backbone size not publicly specified at abstract level)
- Action head: ScaleDP (Scalable Diffusion Policy), offered in two variants:
  - ScaleDP-H (large variant)
  - ScaleDP-L (lightweight variant)
  - Approximately 1B parameters for the diffusion expert
- Both ScaleDP-H and ScaleDP-L checkpoints available on HuggingFace

**Main contributions:**
- Plug-in diffusion expert architecture: a 1B-parameter diffusion model that attaches to a frozen VLM, enabling dexterous manipulation without degrading the VLM's pre-trained capabilities (this claim is not independently verified in the entry)
- ScaleDP (Scalable Diffusion Policy): a scalable diffusion-based action generation module designed for high-dimensional dexterous action spaces, with both large (H) and lightweight (L) variants
- Curriculum-based training strategy that progressively increases dexterous task complexity, improving sample efficiency and final performance

**Limitations/Gaps:**
- Outputs position targets only; no force, impedance, or compliance output
- The 1B diffusion expert adds significant computational overhead on top of the frozen VLM
- Cross-embodiment evaluation across different dexterous hand types is not a primary focus (unlike UniDex-VLA's 8-hand evaluation)
- No tactile or force/torque sensor integration
- Real-world evaluation scope is narrow compared to simulation

**Results:**

**LIBERO Benchmark (average over Spatial / Object / Goal suites):**

| Method | Spatial | Object | Goal | Average |
|---|---|---|---|---|
| Diffusion Policy | 78.3 | 92.5 | 68.3 | 79.7 |
| OpenVLA | 84.7 | 88.4 | 79.2 | 84.1 |
| pi0-FAST | 96.4 | 96.8 | 88.6 | 93.9 |
| pi0 | 96.8 | 98.8 | 95.8 | 97.1 |
| **DexVLA** | **97.2** | **99.1** | **95.6** | **97.3** |

**Real-world tasks (without task-specific adaptation):**

| Task | DexVLA | OpenVLA | Octo | Diffusion Policy |
|---|---|---|---|---|
| Shirt Folding | 0.92 | 0.0 | 0.0 | 0.0 |
| Bin Picking Easy | ~0.85 | ~0.15 | ~0.10 | ~0.20 |
| Table Bussing Easy | ~0.80 | ~0.25 | ~0.15 | ~0.30 |

**Novel embodiment learning (100 demonstrations):**

| Task | DexVLA | OpenVLA | Octo | Diffusion Policy |
|---|---|---|---|---|
| Drink Pouring (Inspired Dexterous Hand) | 0.90 | ~0.10 | ~0.05 | ~0.70 |
| Packing (Bimanual UR5e) | 0.90 | ~0.20 | ~0.15 | ~0.65 |

**Long-horizon tasks:**

| Task | DexVLA | pi0 |
|---|---|---|
| Laundry Folding | 0.40 | 0.20 |
| Table Bussing (Hard) | 0.70 | 0.62 |

**Three-stage curriculum ablation:**

| Stage 1 | Stage 2 | Stage 3 | Shirt Folding | Laundry Folding |
|---|---|---|---|---|
| Yes | -- | -- | 0.0 | 0.0 |
| -- | Yes | -- | 0.0 | 0.0 |
| Yes | Yes | -- | 0.92 | 0.0 |
| Yes | Yes | Yes | 0.92 | 0.40 |

Stage 3 (long-horizon fine-tuning) is necessary for complex tasks like laundry folding; curriculum stages 1+2 alone suffice for simpler tasks like shirt folding.

**Diffusion expert scale ablation (shirt folding):**

| Model | Parameters | Success Rate |
|---|---|---|
| UNet | 93M | 0.17 |
| ScaleDP (medium) | 410M | 0.63 |
| ScaleDP (large) | 1B | 0.92 |

**Training efficiency:** Training only the diffusion expert runs at 0.89 epoch/hour vs. 0.32 epoch/hour for the entire VLA (2.78x speedup).

**Zero-shot cross-embodiment transfer:** Gripper-to-dexterous-hand on bin-picking achieves 60% success rate vs. 67% with the original gripper embodiment.

- ScaleDP-H and ScaleDP-L weights publicly released on HuggingFace
- Code released at [GitHub](https://github.com/juruobenruo/DexVLA)

## Inference / Deployment

- **Inference latency:** Runs at **60 Hz** on a single NVIDIA A6000 GPU. This is one of the fastest VLA inference rates reported in the surveyed literature.
- **Deployment hardware:** Single NVIDIA A6000 GPU for inference. The system achieves cost-efficient training and fast inference despite scaling the diffusion expert to 1 billion parameters.
- **Real-time capable?** Yes. 60 Hz on a single A6000 GPU is sufficient for real-time dexterous manipulation control, exceeding the 10--30 Hz control frequencies typical of most VLA-based systems.

## Dataset / Data Collection

- **Dataset used:** Cross-embodiment training data covering single-arm, bimanual, and dexterous hand robots. No single named benchmark; uses a combination of data sources.
- **Collection method:** Cross-embodiment data collection. Specific collection methodology (teleoperation device, simulation, etc.) is not detailed in public materials. The project page references cross-embodiment learning.
- **Data scale:** Not reported in available abstracts. The paper should be consulted for dataset size per embodiment.
- **Teleop equipment:** Not reported.
- **Data format:** Not reported.
- **Publicly available?** ScaleDP-H and ScaleDP-L weights publicly released on HuggingFace. Code at [GitHub](https://github.com/juruobenruo/DexVLA). Whether training data is released is not confirmed.

> *Dataset details partially from training knowledge -- the project page (dex-vla.github.io) was not accessible at time of review.*
