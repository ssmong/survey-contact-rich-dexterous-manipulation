## 3.7 OmniVTLA

- **Full title:** OmniVTLA: Omni Vision-Tactile-Language-Action Model for Dexterous Manipulation
- **Authors:** Not specified in survey table
- **Venue/Year:** arXiv preprint, 2025
- **arXiv:** https://arxiv.org/abs/2508.08706

**Force/tactile input type:** Both vision-based and force-based tactile sensors. The model is designed to handle heterogeneous tactile modalities (optical tactile images and force-based tactile signals) within a unified framework.

**Force/impedance output:** No. Position-only output.

> **Limitation (position-only output):** Position-only output; the policy cannot actively regulate contact forces despite receiving force/tactile input.

**Robot platform:** Evaluated on both parallel-jaw gripper and dexterous hand platforms.

> **Limitation (dexterous hand):** Dexterous hand evaluation limited to simple pick-and-place.

**Tasks:** Pick-and-place manipulation tasks. Achieves 100% success rate on dexterous hand pick-and-place tasks with tactile input.

**Key methodology:** OmniVTLA proposes a unified architecture that can process multiple tactile modalities (vision-based and force-based) alongside visual and language inputs. The model uses modality-specific encoders for each tactile type, which are then projected into a shared embedding space compatible with the VLM backbone. A modality-agnostic fusion layer combines tactile features with visual and language tokens. This design allows the same model architecture to work with different tactile sensor types without retraining.

**Architecture/Parameters:** Multi-modal VLA with modality-specific tactile encoders feeding into a shared VLM backbone. The architecture is designed to be sensor-agnostic at the fusion level.

**Main contributions:**
- Proposes a unified VLA framework that handles heterogeneous tactile modalities (vision-based and force-based) within a single model.
- Demonstrates that tactile input enables high success rates on dexterous hand manipulation (100% on pick-and-place).
- Provides a dataset for tactile-VLA training (dataset released, code not yet public).

**Limitations/Gaps:** No code released (dataset only). The evaluation is limited to relatively simple pick-and-place tasks. While the paper demonstrates dexterous hand support, the task complexity does not fully exploit the dexterous capabilities. The 100% success rate on pick-and-place suggests the tasks may not be sufficiently challenging to differentiate approaches.

**Results:**

| Metric | Value |
|--------|-------|
| Dex hand pick-and-place success | 100% |
| Multi-modal vs. single-modality | Multi-modal tactile fusion outperforms single-modality baselines |

## Inference / Deployment

- **Inference latency:** Not reported. The paper does not disclose per-step inference latency or control frequency.
- **Deployment hardware:** Training on NVIDIA A100 (80 GB VRAM) GPUs. Real-world experiments demonstrated on both gripper and dexterous hand platforms. Inference hardware not separately specified.
- **Real-time capable?** Not verified. No inference latency or control frequency reported in the paper.

## Dataset / Data Collection

- **Dataset used:** ObjTac (custom dataset released with this work). A comprehensive force-based tactile dataset capturing textual, visual, and tactile information.
- **Collection method:** Force-based tactile data collection using force/pressure sensors across 56 objects in 10 categories. Tri-modal samples combining visual, tactile, and textual information.
- **Data scale:** 135K tri-modal samples across 56 objects and 10 categories.
- **Teleop equipment:** Not reported. Automated data collection with force-based tactile sensors.
- **Data format:** Tri-modal: textual descriptions + visual images + force-based tactile readings.
- **Publicly available?** Yes. ObjTac dataset available at [readerek.github.io/Objtac.github.io](https://readerek.github.io/Objtac.github.io). Code not yet released (dataset only).
