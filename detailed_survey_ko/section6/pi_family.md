## 6.1 Physical Intelligence pi Family

### pi0 / pi0-FAST / pi0.5 / pi0.6 / pi0.7

**전체 제목:** pi0: A Vision-Language-Action Flow Model for General Robot Control (initial paper); subsequent versions released as technical reports or blog posts without individual arXiv publications.

**저자:** Physical Intelligence (Kevin Black, Noah Brown, Danny Driess, Adnan Esmail, Michael Equi, Chelsea Finn, Niccolo Fusai, Lachy Groom, Karol Hausman, Brian Ichter, Szymon Jakubczak, Tim Jones, Liyiming Ke, Sergey Levine, Adrian Li-Bell, Mohith Mothukuri, Suraj Nair, Karl Pertsch, Lucy Xiaoyang Shi, James Tanner, Quan Vuong, Anna Walling, Haohuan Wang, Ury Zhilinsky)

**학회/연도:** pi0 introduced Oct 2024 (arXiv 2410.24164); pi0-FAST Jan 2025 (arXiv 2501.13987); pi0.5 Apr 2025 (technical report); pi0.6 ~Nov 2025; pi0.7 ~Apr 2026.

**아키텍처:**

| Version | Date | Params | VLM Backbone | Action Head | Key Change |
|---|---|---|---|---|---|
| **pi0** | Oct 2024 | 3.3B | PaliGemma 3B (SigLIP ViT + Gemma 2B LM) | Flow matching (~300M params) | Foundational VLA with flow-matching action generation |
| **pi0-FAST** | Jan 2025 | 3.3B | PaliGemma 3B | Autoregressive with FAST tokenizer | Replaced continuous flow head with discrete action tokens for faster inference |
| **pi0.5** | Apr 2025 | 3.3B | PaliGemma 3B | Two-stage: FAST pretrain then flow matching fine-tune | Knowledge insulation for better open-world generalization; web-scale VLM knowledge preserved |
| **pi0.6** | ~Nov 2025 | ~5B | Gemma 3 4B | Dual flow + token heads | Upgraded VLM backbone from PaliGemma to Gemma 3; larger capacity |
| **pi0.7** | ~Apr 2026 | ~5B | Gemma 3 4B + 400M vision encoder | Flow matching (860M DiT) | Larger dedicated DiT action head; improved vision encoder |

The architecture follows a consistent pattern across versions: a pre-trained vision-language model processes multi-view images and optional language instructions, producing contextualized embeddings that condition an action generation head. The action head denoises or decodes a chunk of future actions (typically 16-50 timesteps) in a single forward pass.

**행동 공간:** 18-19 dimensions across all versions: dual 6-DoF arms (position + orientation) + gripper widths + optional mobile base velocity. All versions use parallel-jaw grippers exclusively.

**다지 핸드 지원:** ✗ --- No version supports multi-finger dexterous hands. Action representations are designed for bimanual arm + gripper setups.

**힘/임피던스 출력:** ✗ --- All versions output position targets only. No force, torque, or impedance parameters.

**핵심 방법론:** pi0 introduced flow matching as an action generation mechanism for VLAs, treating robot action prediction as a conditional denoising process. The VLM backbone is co-fine-tuned with the action head on robot demonstration data, enabling the model to follow natural language instructions while generating precise motor commands. pi0-FAST replaced the continuous flow head with an autoregressive discrete tokenizer (FAST) that bins continuous actions into a learned vocabulary, trading some precision for 5-10x faster inference. pi0.5 introduced a two-stage training recipe --- FAST pretraining for broad coverage followed by flow-matching fine-tuning for precision --- with "knowledge insulation" to prevent catastrophic forgetting of the base VLM's world knowledge during robot fine-tuning.

**훈련 데이터:** 10,000+ hours of robot manipulation data across multiple embodiments. Pre-training uses a mixture of internet-scale vision-language data (inherited from PaliGemma/Gemma) and cross-embodiment robot demonstrations. Fine-tuning datasets include DROID, ALOHA, Bridge V2, and proprietary Physical Intelligence data. Supported robots include UR5, ALOHA bimanual, and various single-arm platforms.

**주요 기여:**
- Established flow matching as a viable action head for VLAs, enabling continuous multi-modal action distributions without the quantization artifacts of autoregressive tokenization.
- Demonstrated that co-fine-tuning a frozen VLM with a lightweight action head achieves strong language-conditioned manipulation from relatively modest robot data.
- The open-source openpi framework provides a complete fine-tuning and inference pipeline, making pi0/pi0-FAST/pi0.5 accessible for academic research.

**정량적 결과:**

*pi0 (arXiv 2410.24164):*

| Benchmark / Task | pi0 | Best Baseline | Notes |
|---|---|---|---|
| *(Results not independently verified --- arXiv page could not be fetched. Consult the paper directly for per-task success rates on DROID, ALOHA, and Bridge V2 benchmarks.)* | | | |

*pi0-FAST (arXiv 2501.13987):*

| Benchmark / Task | pi0-FAST | pi0 (flow) | Notes |
|---|---|---|---|
| *(Results not independently verified --- arXiv page could not be fetched. The paper reports comparable success rates to pi0 flow matching at 5-10x faster inference speed. Consult the paper for per-task numbers.)* | | | |

**한계점:**
- Strictly gripper-only: the 18-19D action space cannot represent multi-finger hand configurations. Extending to dexterous hands would require fundamental changes to the action representation.
- No force or compliance awareness: all outputs are position targets, making the model unsuitable for contact-rich tasks requiring force regulation.
- pi0.6 and pi0.7 are not publicly released; only pi0, pi0-FAST, and pi0.5 have open weights.
- Training data is predominantly from parallel-jaw gripper demonstrations, creating an embodiment bias that would hinder adaptation to dexterous platforms.

**공개 가중치/코드:** ✅ pi0, pi0-FAST, pi0.5 available under Apache 2.0 via [openpi](https://github.com/Physical-Intelligence/openpi) and [HuggingFace](https://huggingface.co/lerobot/pi0_base). pi0.6 and pi0.7 not publicly released as of May 2026.

## 추론 / 배포

- **추론 지연 시간:** pi0 (flow matching) runs at approximately 3-5 Hz due to the iterative denoising process (multiple flow-matching steps per action chunk). pi0-FAST achieves 5-10x faster inference (~15-50 Hz) by replacing the flow head with autoregressive FAST token decoding, generating action chunks in a single forward pass. pi0.5 fine-tuning with flow matching returns to pi0-level speed (~3-5 Hz). Specific ms-per-step figures not publicly benchmarked on standardized hardware.
- **배포 하드웨어:** Evaluated on desktop GPUs (specific model not disclosed in public materials). The 3.3B parameter model requires a capable GPU (e.g., NVIDIA A100/RTX 4090 class) for real-time flow-matching inference. pi0-FAST's discrete tokenization is more CPU/edge-friendly. No Jetson Orin deployment reported.
- **실시간 가능 여부:** pi0-FAST: Yes, at ~15-50 Hz with action chunking, suitable for typical manipulation control frequencies. pi0 (flow matching): Marginal, at ~3-5 Hz -- sufficient for slow manipulation but too slow for dexterous tasks requiring 20+ Hz. Action chunking (predicting 16-50 future steps per inference) compensates for low inference frequency by executing multiple steps between inferences.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** 10,000+ hours of robot manipulation data across multiple embodiments. Pre-training mixture includes internet-scale vision-language data (inherited from PaliGemma/Gemma) and cross-embodiment robot demonstrations. Fine-tuning datasets include DROID (~76K trajectories, 350 hours), ALOHA bimanual demonstrations, Bridge V2, and proprietary Physical Intelligence data.
- **수집 방법:** Teleoperation (various setups per dataset: VR controllers for DROID, leader-follower for ALOHA, keyboard/SpaceMouse for Bridge V2) + web-scale vision-language pretraining data. Supported robots include UR5, ALOHA bimanual, and various single-arm platforms.
- **데이터 규모:** 10,000+ hours total robot data. DROID: ~76K trajectories / 350 hours / 564 scenes. Bridge V2: ~60K trajectories / 24 environments. Additional proprietary data from Physical Intelligence.
- **원격 조작 장비:** Varies by dataset component -- Meta Quest VR controllers (DROID), leader-follower arms (ALOHA), keyboard/SpaceMouse (Bridge V2).
- **데이터 포맷:** RLDS (TensorFlow Datasets) for OXE-compatible datasets; proprietary formats for Physical Intelligence data. LeRobot format for open-source release.
- **공개 여부:** Partially. DROID, Bridge V2, and ALOHA datasets are publicly available. Proprietary Physical Intelligence data is not released. Model weights for pi0/pi0-FAST/pi0.5 are open (Apache 2.0).

---
