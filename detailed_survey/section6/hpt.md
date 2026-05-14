### HPT: Heterogeneous Pre-trained Transformers

**Full title:** Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers

**Authors:** Lirui Wang, Xinlei Chen, Jialiang Zhao, Kaiming He (MIT CSAIL)

**Venue/Year:** NeurIPS 2024

**Architecture:** HPT addresses cross-embodiment heterogeneity by using embodiment-specific "stem" networks (small MLPs or convolutions) that project heterogeneous proprioceptive and action spaces into a shared latent representation. A shared transformer trunk processes the aligned representations, and embodiment-specific "head" networks decode outputs back to the original action space. Vision features come from pre-trained encoders (CLIP, DINOv2). The shared trunk has ~300M parameters; total size varies with the number of stems/heads.

**Action space:** Variable per embodiment, handled by the per-embodiment head networks. Supports arbitrary proprioceptive and action dimensions.

**Dex hand support?** ✗ --- Not explicitly demonstrated on dexterous hands, though the heterogeneous stem/head architecture is designed to accommodate arbitrary embodiment configurations.

**Force/impedance output?** ✗ --- Position targets only.

**Key methodology:** HPT tackles the fundamental challenge that different robots have different observation and action space dimensions, making naive cross-embodiment training impossible. The stem-trunk-head architecture decouples embodiment-specific processing from shared representation learning. During pretraining, multiple embodiment-specific stems and heads are trained jointly with the shared trunk, learning a universal manipulation representation. At fine-tuning time, new stems/heads can be added for unseen embodiments while keeping the trunk frozen.

**Training data:** Pretrained on diverse cross-embodiment datasets including subsets of OXE, spanning 50+ distinct robot configurations.

**Main contributions:**
- Proposed the stem-trunk-head architecture for heterogeneous cross-embodiment pretraining, providing a principled solution to the action/observation space mismatch problem.
- Demonstrated that a shared transformer trunk learns transferable manipulation representations across diverse embodiments.
- Showed that the approach scales with data diversity: more diverse pretraining data improves downstream fine-tuning performance.

**Quantitative results:**

| Benchmark / Task | HPT | Baseline | Notes |
|---|---|---|---|
| *(Consult the NeurIPS 2024 paper for per-task results. The paper reports improvements from scaling data diversity across embodiments.)* | | | |

**Limitations/Gaps:**
- Each new embodiment requires training a new stem and head, with some embodiment-specific data.
- The approach has not been evaluated on high-DoF dexterous hand systems.
- No language conditioning in the base model (proprioceptive-visual only).
- No public model weights released.

**Open weights/code:** ✅ Code: [GitHub](https://github.com/liruiw/HPT). ✗ Pre-trained weights not publicly available.

## Inference / Deployment

- **Inference latency:** Not explicitly benchmarked. The shared transformer trunk (~300M parameters) plus lightweight per-embodiment stems/heads should run at ~10-30 Hz on a desktop GPU, comparable to medium-sized transformer policies.
- **Deployment hardware:** Not reported. The ~300M parameter trunk is moderate-sized, requiring a desktop GPU for real-time inference but smaller than billion-parameter VLAs.
- **Real-time capable?** Yes, likely. The moderate model size and MLP-based stems/heads should support real-time control at typical manipulation frequencies. However, specific benchmarks are not reported.

## Dataset / Data Collection

- **Dataset used:** Subsets of Open X-Embodiment (OXE) spanning 50+ distinct robot configurations for pretraining. Fine-tuning on task-specific demonstration data.
- **Collection method:** Aggregated cross-embodiment data from OXE (teleoperation, scripted policies). The stem-trunk-head architecture handles heterogeneous observation/action spaces across embodiments.
- **Data scale:** 50+ robot configurations for pretraining. Fine-tuning demonstration counts not specified.
- **Teleop equipment:** Varies by OXE constituent dataset.
- **Data format:** Multiple formats handled by per-embodiment stem networks.
- **Publicly available?** OXE data is public. Pre-trained HPT weights are not released.

---
