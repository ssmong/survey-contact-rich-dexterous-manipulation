### UniAct: Universal Action Tokenization for Robotic Manipulation

**Full title:** UniAct: Universal Action Representation Meets Vision Foundation Model for Robotic Manipulation

**Authors:** Qi Qin, Yinuo Zhao, Boyuan Zheng, Hritik Bansal, Hernan Ceferino Vazquez, Yanan Zhao, Shubham Garg, Yihang Chen, Harsh Mehta, Nanyun Peng, Stefano Ermon, Hao Su (Multi-institution)

**Venue/Year:** CVPR 2025

**Architecture:** UniAct introduces a universal action codebook that maps diverse robot action spaces into a shared discrete vocabulary. The architecture uses a VQ-VAE (vector-quantized variational autoencoder) to learn an embodiment-agnostic action tokenization, which is then used as the output vocabulary for a VLA built on a pre-trained VLM backbone. This enables a single model to control different robots by mapping to and from the shared codebook.

**Action space:** Universal discrete codebook (typically 512-1024 codes). Each robot's native action space is mapped to/from this codebook via learned encoder-decoder pairs. The codebook captures motion primitives that are shared across embodiments.

**Dex hand support?** Not demonstrated on dexterous hands. The codebook architecture does not preclude it, but no dex hand data or evaluation is included. Whether the learned codebook can capture the high-dimensional, contact-rich action distributions required for multi-finger manipulation is an open question.

**Force/impedance output?** ✗ --- Position targets only; the codebook encodes position/velocity commands.

**Key methodology:** UniAct tackles the cross-embodiment action representation problem by learning a shared discrete codebook of motion primitives via VQ-VAE. Unlike approaches that zero-pad to a fixed dimension (RDT-1B) or use per-embodiment heads (HPT, GR00T), UniAct learns a genuinely shared action vocabulary where similar motions across embodiments map to the same codes. The VQ-VAE is trained on diverse cross-embodiment demonstration data. At inference, the VLA predicts a sequence of codebook indices, which are decoded into embodiment-specific actions.

**Training data:** Cross-embodiment demonstration data from OXE and other sources. The VQ-VAE codebook is trained on action trajectories from diverse robots.

**Main contributions:**
- Proposed a universal discrete action codebook that enables genuine cross-embodiment action sharing, going beyond per-embodiment adapters.
- Demonstrated that shared action primitives transfer across robot morphologies, improving sample efficiency on downstream tasks.
- The codebook approach provides interpretable action representations where similar motions cluster together.

**Quantitative results:**

| Benchmark / Task | UniAct | Baseline | Notes |
|---|---|---|---|
| *(Consult the CVPR 2025 paper for per-task results and comparisons to per-embodiment baselines.)* | | | |

**Limitations/Gaps:**
- Codebook size and structure may not capture the full continuous action space, particularly for high-DoF systems.
- Discretization introduces quantization errors similar to token-based VLAs.
- The VQ-VAE must be retrained when adding new embodiments with substantially different action spaces.
- No force/compliance information in the codebook.

**Open weights/code:** ✅ Code: [GitHub](https://github.com/2toinf/UniAct). ✗ Pre-trained weights not publicly available.

## Inference / Deployment

- **Inference latency:** Not explicitly benchmarked. The VQ-VAE codebook lookup is fast (<1ms), but the VLA backbone that predicts codebook indices determines the overall speed. With a VLM backbone, inference speed depends on the VLM size and whether decoding is autoregressive or parallel.
- **Deployment hardware:** Not reported. Depends on the VLM backbone size.
- **Real-time capable?** Depends on the VLA backbone. The codebook decoding step (index to continuous action) is trivially fast. The bottleneck is the VLA's inference speed for predicting codebook indices.

## Dataset / Data Collection

- **Dataset used:** Cross-embodiment demonstration data from OXE and other sources for VQ-VAE codebook training. VLA trained on OXE cross-embodiment data.
- **Collection method:** Aggregated teleoperation and scripted-policy data from OXE constituent datasets. The VQ-VAE codebook is trained on action trajectories from diverse robots to learn shared motion primitives.
- **Data scale:** OXE-scale cross-embodiment data. Specific episode counts not reported separately from OXE.
- **Teleop equipment:** Varies by OXE constituent dataset.
- **Data format:** Action trajectories quantized into universal discrete codebook (512-1024 codes). Input data in RLDS (OXE standard).
- **Publicly available?** OXE data is public. UniAct pre-trained weights not released.

---
