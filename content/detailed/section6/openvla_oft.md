### OpenVLA-OFT: Open Vision-Language-Action Model with Optimal Fine-Tuning

**Full title:** Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success

**Authors:** Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, Suraj Nair, Ashwin Balakrishna, Sergey Levine, Percy Liang, Chelsea Finn

**Venue/Year:** RSS 2025

**Architecture:** Built on OpenVLA 7B with three key modifications: (1) parallel action decoding replacing sequential autoregressive generation, (2) continuous action outputs replacing discrete token bins, and (3) a lightweight FiLM-conditioned action head appended after the VLM backbone. The VLM backbone remains Prismatic (SigLIP + DinoV2 + Llama 2 7B).

**Action space:** 7D or 14D (for bimanual ALOHA: dual 6-DoF arms + 2 grippers), now decoded as continuous values in parallel rather than as sequential discrete tokens. Supports action chunking (multiple future timesteps per forward pass).

**Dex hand support?** ✗ --- Designed for single-arm gripper and bimanual ALOHA gripper setups.

**Force/impedance output?** ✗ --- Position targets only.

**Key methodology:** OpenVLA-OFT addresses the inference speed bottleneck of autoregressive VLAs by replacing sequential token decoding with parallel continuous action prediction. A FiLM-conditioned action head processes the VLM's output embeddings to produce all action dimensions simultaneously. Combined with action chunking and fine-tuning recipe optimizations (learning rate scheduling, data augmentation), this achieves 26x faster inference than OpenVLA while improving task success rates. The work demonstrates that the autoregressive action tokenization used by RT-2 and OpenVLA is suboptimal.

**Training data:** Same OXE pretraining as OpenVLA. Fine-tuning evaluated on Bridge V2 and ALOHA bimanual tasks.

**Main contributions:**
- Achieved 26x faster inference over OpenVLA by eliminating sequential action decoding.
- Demonstrated that continuous parallel action outputs outperform discrete tokenized actions in both speed and accuracy.
- Provided a systematic study of fine-tuning recipes for VLAs, identifying optimal learning rates, augmentation strategies, and action representation choices.

**Quantitative results:**

| Metric | OpenVLA-OFT | OpenVLA | Speedup | Notes |
|---|---|---|---|---|
| *(Results not independently verified --- consult the RSS 2025 paper for per-task success rates on Bridge V2 and ALOHA bimanual benchmarks. The paper reports 26x inference speedup with improved success rates.)* | | | | |

**Limitations/Gaps:**
- Still limited to gripper-based systems; the 7/14D action space does not extend to dexterous hands.
- Relies on the same Prismatic VLM backbone, inheriting its single-view limitation.
- No force/compliance awareness.

**Open weights/code:** ✅ Fully open. [GitHub](https://github.com/moojink/openvla-oft), [HuggingFace](https://huggingface.co/openvla/openvla-7b-oft).

## Inference / Deployment

- **Inference latency:** OpenVLA-OFT achieves 26x faster inference than OpenVLA by replacing sequential autoregressive decoding with parallel continuous action prediction. This corresponds to approximately 100-150 Hz for action head decoding (though total system throughput depends on image encoding). With action chunking, the effective control rate is substantially higher than the per-inference frequency.
- **Deployment hardware:** Same 7B parameter VLM backbone as OpenVLA, requiring a GPU (A100 or consumer RTX 4090 class) for inference. The parallel action head is lightweight (FiLM-conditioned MLP), so the speedup comes from eliminating sequential token decoding, not from model size reduction.
- **Real-time capable?** Yes. The 26x speedup over OpenVLA brings inference to a level suitable for real-time manipulation control. Combined with action chunking, the system can maintain smooth control at manipulation-appropriate frequencies. This is a critical improvement for practical VLA deployment.

## Dataset / Data Collection

- **Dataset used:** Same OXE pretraining as OpenVLA (970K episodes, 22 embodiments). Fine-tuning evaluated on Bridge V2 and ALOHA bimanual tasks.
- **Collection method:** Same as OpenVLA -- aggregated cross-embodiment teleoperation data from OXE. Fine-tuning demonstrations collected via respective teleoperation systems (SpaceMouse for Bridge V2, leader-follower for ALOHA).
- **Data scale:** 970K episodes (pretraining, inherited from OpenVLA). Fine-tuning scale varies by task.
- **Teleop equipment:** Inherited from OXE constituent datasets.
- **Data format:** RLDS (TensorFlow Datasets) for OXE pretraining data.
- **Publicly available?** Yes. Same as OpenVLA -- OXE is public. OFT weights at https://huggingface.co/openvla/openvla-7b-oft.

---
