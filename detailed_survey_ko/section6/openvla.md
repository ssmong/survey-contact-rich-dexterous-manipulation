### OpenVLA: An Open-Source Vision-Language-Action Model

**전체 제목:** OpenVLA: An Open-Source Vision-Language-Action Model

**저자:** Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, Ted Xiao, Ashwin Balakrishna, Suraj Nair, Rafael Rafailov, Ethan Foster, Grace Lam, Pannag Sanketi, Quan Vuong, Thomas Kollar, Benjamin Burchfiel, Russ Tedrake, Dorsa Sadigh, Sergey Levine, Percy Liang, Chelsea Finn

**학회/연도:** CoRL 2024

**아키텍처:** 7B parameter VLA built on the Prismatic VLM backbone (SigLIP + DinoV2 dual vision encoders fused into a Llama 2 7B language model). Actions are output as discrete tokens via autoregressive decoding, following the RT-2 paradigm. No separate action head; the LLM's output vocabulary is extended with 256 action bins per dimension.

**행동 공간:** 7D (6-DoF end-effector delta + gripper), discretized into 256 bins per dimension, decoded as text tokens.

**다지 핸드 지원:** ✗ --- Single-arm gripper systems only.

**힘/임피던스 출력:** ✗ --- Position targets only.

**핵심 방법론:** OpenVLA provides the first fully open-source replication of the RT-2 VLA paradigm. It is trained on the Open X-Embodiment (OXE) dataset, a large-scale cross-embodiment robot dataset, and fine-tuned on downstream tasks using parameter-efficient methods (LoRA). The dual vision encoder (SigLIP for semantics + DinoV2 for spatial features) provides complementary visual representations. OpenVLA serves as a community baseline, enabling direct comparison and extension of VLA methods.

**훈련 데이터:** Pretrained on 970K robot episodes from the Open X-Embodiment (OXE) dataset spanning 22 robot embodiments. The OXE mixture includes Bridge V2, RT-1, DROID, and numerous other datasets. Fine-tuning uses task-specific demonstration data (typically 50-500 episodes).

**주요 기여:**
- The first widely-adopted open-source VLA (Apache 2.0) with competitive performance to RT-2, enabling community research.
- Demonstrated that LoRA fine-tuning of a pretrained VLA can adapt to new tasks with as few as 50 demonstrations.
- Established a reproducible VLA baseline with standardized evaluation protocols.

**정량적 결과:**

| Benchmark / Task | OpenVLA (7B) | RT-2-X | Notes |
|---|---|---|---|
| *(Results not independently verified --- arXiv page could not be fetched. The paper reports competitive performance with RT-2-X on Bridge V2 and SimplerEnv benchmarks. Consult CoRL 2024 paper for per-task success rates.)* | | | |

**한계점:**
- Autoregressive single-token action decoding is slow (~4-6 Hz) and limits action expressiveness.
- 7D action space is restrictive for bimanual or dexterous systems.
- Quantization of continuous actions into 256 bins introduces precision loss, particularly for fine manipulation.
- No multi-view image support in the base model.

**공개 가중치/코드:** ✅ Fully open under Apache 2.0. [GitHub](https://github.com/openvla/openvla), [HuggingFace](https://huggingface.co/openvla/openvla-7b).

## 추론 / 배포

- **추론 지연 시간:** OpenVLA runs at approximately 4-6 Hz on a single A100 GPU. The sequential autoregressive decoding of 7 action tokens through the full 7B parameter LLM is the bottleneck -- each action dimension is decoded one at a time, requiring 7 full forward passes through the model per action step.
- **배포 하드웨어:** Requires a high-end GPU (NVIDIA A100 or equivalent) for inference. Can be quantized (4-bit, 8-bit) for deployment on consumer GPUs (RTX 3090/4090). Fine-tuning via LoRA is possible on consumer GPUs. Not deployable on edge devices due to the 7B parameter footprint.
- **실시간 가능 여부:** Marginal. At 4-6 Hz, OpenVLA is usable for slow tabletop manipulation but too slow for contact-rich or dexterous tasks requiring 10+ Hz control. OpenVLA-OFT addresses this bottleneck with 26x faster inference via parallel action decoding.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** Open X-Embodiment (OXE) dataset -- 970K robot episodes spanning 22 robot embodiments. The OXE mixture includes Bridge V2, RT-1, DROID, and numerous other community-contributed datasets.
- **수집 방법:** Aggregated from multiple sources with diverse collection methods: teleoperation (VR controllers, SpaceMouse, leader-follower), scripted policies, and human demonstrations across 22 different robot platforms. Fine-tuning uses task-specific demonstrations (typically 50-500 episodes).
- **데이터 규모:** 970K robot episodes across 22 embodiments for pretraining. Fine-tuning: 50-500 demonstrations per task.
- **원격 조작 장비:** Varies by constituent dataset -- Meta Quest VR controllers (DROID), SpaceMouse (Bridge V2), leader-follower (ALOHA), and others.
- **데이터 포맷:** RLDS (TensorFlow Datasets) format, following the Open X-Embodiment standard.
- **공개 여부:** Yes. OXE dataset is fully public. Model weights at https://huggingface.co/openvla/openvla-7b (Apache 2.0).

---
