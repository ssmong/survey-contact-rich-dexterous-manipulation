### OpenVLA-OFT: Open Vision-Language-Action Model with Optimal Fine-Tuning

**전체 제목:** Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success

**저자:** Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, Suraj Nair, Ashwin Balakrishna, Sergey Levine, Percy Liang, Chelsea Finn

**학회/연도:** RSS 2025

**아키텍처:** Built on OpenVLA 7B with three key modifications: (1) parallel action decoding replacing sequential autoregressive generation, (2) continuous action outputs replacing discrete token bins, and (3) a lightweight FiLM-conditioned action head appended after the VLM backbone. The VLM backbone remains Prismatic (SigLIP + DinoV2 + Llama 2 7B).

**행동 공간:** 7D or 14D (for bimanual ALOHA: dual 6-DoF arms + 2 grippers), now decoded as continuous values in parallel rather than as sequential discrete tokens. Supports action chunking (multiple future timesteps per forward pass).

**다지 핸드 지원:** ✗ --- Designed for single-arm gripper and bimanual ALOHA gripper setups.

**힘/임피던스 출력:** ✗ --- Position targets only.

**핵심 방법론:** OpenVLA-OFT addresses the inference speed bottleneck of autoregressive VLAs by replacing sequential token decoding with parallel continuous action prediction. A FiLM-conditioned action head processes the VLM's output embeddings to produce all action dimensions simultaneously. Combined with action chunking and fine-tuning recipe optimizations (learning rate scheduling, data augmentation), this achieves 26x faster inference than OpenVLA while improving task success rates. The work demonstrates that the autoregressive action tokenization used by RT-2 and OpenVLA is suboptimal.

**훈련 데이터:** Same OXE pretraining as OpenVLA. Fine-tuning evaluated on Bridge V2 and ALOHA bimanual tasks.

**주요 기여:**
- Achieved 26x faster inference over OpenVLA by eliminating sequential action decoding.
- Demonstrated that continuous parallel action outputs outperform discrete tokenized actions in both speed and accuracy.
- Provided a systematic study of fine-tuning recipes for VLAs, identifying optimal learning rates, augmentation strategies, and action representation choices.

**정량적 결과:**

| Metric | OpenVLA-OFT | OpenVLA | Speedup | Notes |
|---|---|---|---|---|
| *(Results not independently verified --- consult the RSS 2025 paper for per-task success rates on Bridge V2 and ALOHA bimanual benchmarks. The paper reports 26x inference speedup with improved success rates.)* | | | | |

**한계점:**
- Still limited to gripper-based systems; the 7/14D action space does not extend to dexterous hands.
- Relies on the same Prismatic VLM backbone, inheriting its single-view limitation.
- No force/compliance awareness.

**공개 가중치/코드:** ✅ Fully open. [GitHub](https://github.com/moojink/openvla-oft), [HuggingFace](https://huggingface.co/openvla/openvla-7b-oft).

## 추론 / 배포

- **추론 지연 시간:** OpenVLA-OFT achieves 26x faster inference than OpenVLA by replacing sequential autoregressive decoding with parallel continuous action prediction. This corresponds to approximately 100-150 Hz for action head decoding (though total system throughput depends on image encoding). With action chunking, the effective control rate is substantially higher than the per-inference frequency.
- **배포 하드웨어:** Same 7B parameter VLM backbone as OpenVLA, requiring a GPU (A100 or consumer RTX 4090 class) for inference. The parallel action head is lightweight (FiLM-conditioned MLP), so the speedup comes from eliminating sequential token decoding, not from model size reduction.
- **실시간 가능 여부:** Yes. The 26x speedup over OpenVLA brings inference to a level suitable for real-time manipulation control. Combined with action chunking, the system can maintain smooth control at manipulation-appropriate frequencies. This is a critical improvement for practical VLA deployment.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** Same OXE pretraining as OpenVLA (970K episodes, 22 embodiments). Fine-tuning evaluated on Bridge V2 and ALOHA bimanual tasks.
- **수집 방법:** Same as OpenVLA -- aggregated cross-embodiment teleoperation data from OXE. Fine-tuning demonstrations collected via respective teleoperation systems (SpaceMouse for Bridge V2, leader-follower for ALOHA).
- **데이터 규모:** 970K episodes (pretraining, inherited from OpenVLA). Fine-tuning scale varies by task.
- **원격 조작 장비:** Inherited from OXE constituent datasets.
- **데이터 포맷:** RLDS (TensorFlow Datasets) for OXE pretraining data.
- **공개 여부:** Yes. Same as OpenVLA -- OXE is public. OFT weights at https://huggingface.co/openvla/openvla-7b-oft.

---
