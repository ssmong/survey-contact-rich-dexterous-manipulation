### TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation

**전체 제목:** TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation

**저자:** Junjie Wen, Yichen Zhu, Jinming Li, Minjie Zhu, Kun Wu, Zhiyuan Xu, Ning Liu, Ran Cheng, Chaomin Shen, Yaxin Peng, Feifei Feng, Jian Tang (East China Normal University, Midea Group AI Lab Shanghai, Syracuse University, Beijing Innovation Center of Humanoid Robotics, Shanghai University)

**학회/연도:** AAAI 2025

**아키텍처:** Compact VLA in three size variants: TinyVLA-S (422M, 101M trainable), TinyVLA-B (740M, 138M trainable), and TinyVLA-H (1.3B, 143M trainable). The backbone follows the LLaVA training pipeline with Pythia as the language model and a vision encoder. The action head is a diffusion policy decoder using Denoising Diffusion Probabilistic Models (DDPM), which generates continuous actions conditioned on VLM features. Fine-tuning uses LoRA adapters on attention Q/K/V weights, limiting trainable parameters to ~5% of the transformer. The key design choice is initializing the policy backbone from a pretrained multimodal model rather than training from scratch, eliminating the need for large-scale robotic pretraining.

**행동 공간:** 7D continuous (3D position + 3D rotation + gripper width), generated via diffusion decoding with action chunking. The diffusion head uses adaptive pooling, layer normalization, concatenation with proprioceptive state, and a 3-layer MLP for conditional embeddings.

**다지 핸드 지원:** ✗ --- Evaluated on single-arm gripper and bimanual gripper (UR5) systems only.

**힘/임피던스 출력:** ✗ --- Position targets only.

**핵심 방법론:** TinyVLA demonstrates that large-scale robotic pretraining (e.g., on OXE's 970K episodes) is unnecessary if the VLA backbone is initialized from a strong pretrained vision-language model. By coupling a compact VLM backbone (1.3B) with a diffusion policy decoder and applying LoRA fine-tuning, TinyVLA achieves performance matching or exceeding the 7B OpenVLA while being 5.5x smaller and 20x faster at inference. The diffusion decoder generates action chunks conditioned on the VLM's latent representations, enabling smooth, temporally coherent actions without autoregressive token-by-token decoding.

**훈련 데이터:** No large-scale robotic pretraining. Fine-tuned directly on task-specific demonstrations: 100 teleoperated trajectories per task for real-robot experiments. MetaWorld simulation tasks for additional evaluation.

**주요 기여:**
- Demonstrated that a 1.3B VLA initialized from a pretrained VLM and fine-tuned with LoRA + diffusion decoder matches the 7B OpenVLA's performance without any robotic pretraining stage, challenging the assumption that large-scale robot data pretraining is essential.
- Achieved 20x faster inference than OpenVLA (14ms vs. 292ms per action) with 5.5x fewer parameters, making real-time deployment feasible on consumer hardware.
- Showed strong generalization across language instructions, novel objects, unseen positions, appearance/background variations, and environmental shifts despite compact size and limited training data.

**정량적 결과:**

| Benchmark / Task | TinyVLA-H (1.3B) | OpenVLA (7B) | Diffusion Policy | Notes |
|---|---|---|---|---|
| Real-world single-arm avg (5 tasks) | 94.0% | 68.3% | — | +25.7% over OpenVLA |
| Bimanual UR5 avg | 44.5% | 0% | — | OpenVLA fails completely |
| MetaWorld 50 tasks avg (sim) | 31.6% | — | 10.5% | |
| Inference latency | 14 ms | 292 ms | — | 20x speedup |
| Parameters (total / trainable) | 1.3B / 143M | 7.2B / — | — | 5.5x smaller |

> **Note:** This comparison uses the authors' own 5 real-world single-arm tasks, not a community-standardized benchmark. OpenVLA was fine-tuned with the same protocol (100 demos). Results should be interpreted with caution as task selection may favor TinyVLA's design.

**한계점:**
- OpenVLA slightly outperforms TinyVLA on extreme out-of-distribution spatial generalization, likely because OXE pretraining provides broader data diversity.
- Evaluated only on gripper-based systems; no dexterous hand evaluation.
- No force/compliance awareness.
- MetaWorld simulation results (31.6%) remain modest in absolute terms.
- GitHub repository and model weights availability unclear from the paper; project page exists at https://tiny-vla.github.io/.

**공개 가중치/코드:** Project page: [tiny-vla.github.io](https://tiny-vla.github.io/). Explicit GitHub link or model weight download not confirmed in the paper.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** No large-scale pretraining dataset. Task-specific teleoperated demonstrations for fine-tuning (100 trajectories per task). MetaWorld simulation for sim evaluation.
- **수집 방법:** Teleoperation for real-robot tasks.
- **데이터 규모:** 100 demonstrations per task (real). No OXE-scale pretraining.
- **원격 조작 장비:** Not specified in the paper.
- **데이터 포맷:** Not specified.
- **공개 여부:** Project page exists but explicit data/weight release status unclear.

---
