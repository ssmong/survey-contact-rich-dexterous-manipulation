### RDT-1B: Robotics Diffusion Transformer

**Full title:** RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation

**Authors:** Songming Liu, Lingxuan Wu, Bangguo Li, Hengkai Tan, Huayu Chen, Zhengyi Wang, Ke Xu, Hang Su, Jun Zhu (Tsinghua University thu-ml)

**Venue/Year:** ICLR 2025

**Architecture:** 1.1B parameter diffusion transformer (DiT) for robot action generation. The architecture uses a pre-trained vision encoder (SigLIP) and language encoder (T5-XXL) to produce conditioning embeddings, which are injected into a large-scale DiT via adaptive layer normalization. The DiT is the action generation backbone, operating on a unified 128-dimensional action representation that accommodates different robot embodiments through zero-padding and masking. This is the largest open-source diffusion-based robot policy.

**Action space:** 128D unified representation. For bimanual systems, this encodes dual 7-DoF arms + grippers + base. For single-arm systems, unused dimensions are zero-padded. Actions are continuous, generated via iterative denoising.

**Dex hand support?** ✗ --- Evaluated on bimanual ALOHA gripper setups. The 128D action space could accommodate dexterous hand joints, but no dexterous hand demonstrations are included in training.

**Force/impedance output?** ✗ --- Position targets only.

**Key methodology:** RDT-1B scales the diffusion transformer architecture to 1.1B parameters for robot action generation, demonstrating scaling laws for diffusion-based robot policies. The unified 128D action space allows a single model to be pretrained across diverse embodiments by zero-padding actions to a common dimension. The DiT processes proprioceptive state, visual features, and language embeddings through cross-attention and AdaLN mechanisms. Multi-GPU training with data parallelism enables pretraining on large-scale cross-embodiment datasets.

**Training data:** Pretrained on 46 datasets from Open X-Embodiment and other sources, totaling approximately 1M robot episodes. Fine-tuning demonstrated on ALOHA bimanual manipulation tasks.

**Main contributions:**
- Largest open-source diffusion-based robot policy, demonstrating that diffusion transformers benefit from scaling in the robot action generation domain.
- Introduced a unified 128D action representation that accommodates diverse embodiments in a single model.
- Showed that large-scale diffusion pretraining on cross-embodiment data improves sample efficiency during fine-tuning.

**Quantitative results:**

| Benchmark / Task | RDT-1B | Best Baseline | Notes |
|---|---|---|---|
| *(Results not independently verified --- arXiv page could not be fetched. The paper reports results on ALOHA bimanual manipulation tasks. Consult ICLR 2025 paper for per-task success rates and comparisons to Diffusion Policy and ACT baselines.)* | | | |

**Limitations/Gaps:**
- Large model size (1.1B) makes inference slower than lightweight alternatives; requires GPU for real-time control.
- No dexterous hand support in the training data or evaluation.
- Zero-padding to 128D is wasteful for low-DoF robots and may introduce optimization challenges.
- No force/compliance capabilities.

**Open weights/code:** ✅ Fully open. [GitHub](https://github.com/thu-ml/RoboticsDiffusionTransformer), [HuggingFace](https://huggingface.co/thu-ml/RDT-1B).

## Inference / Deployment

- **Inference latency:** Not explicitly benchmarked. The 1.1B parameter DiT with iterative denoising is computationally intensive. Estimated ~3-10 Hz on a high-end GPU (A100 class), depending on the number of diffusion steps. The 128D action output (with zero-padding for lower-DoF robots) adds unnecessary computation for simple embodiments.
- **Deployment hardware:** Requires a high-end GPU for real-time inference. Multi-GPU training with data parallelism for pretraining. Specific deployment hardware not reported.
- **Real-time capable?** Limited. The 1.1B parameter count and multi-step diffusion process make RDT-1B slower than lightweight alternatives (Octo 93M, Diffusion Policy 25M). Suitable for moderate-speed manipulation (5-10 Hz) on desktop GPUs but not for high-frequency dexterous control.

## Dataset / Data Collection

- **Dataset used:** 46 datasets from Open X-Embodiment and other sources, totaling ~1M robot episodes. Fine-tuning on ALOHA bimanual manipulation tasks.
- **Collection method:** Aggregated cross-embodiment data from OXE and additional sources (teleoperation, scripted policies, autonomous collection). Unified 128D action representation via zero-padding and masking to accommodate different embodiments.
- **Data scale:** ~1M robot episodes from 46 datasets for pretraining. Fine-tuning scale varies by task.
- **Teleop equipment:** Varies by constituent dataset -- VR controllers, SpaceMouse, leader-follower, and others.
- **Data format:** Multiple formats unified during loading. OXE components in RLDS.
- **Publicly available?** Yes. OXE datasets are public. RDT-1B weights at https://huggingface.co/thu-ml/RDT-1B.

---
