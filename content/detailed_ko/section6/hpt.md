### HPT: Heterogeneous Pre-trained Transformers

**전체 제목:** Scaling Proprioceptive-Visual Learning with Heterogeneous Pre-trained Transformers

**저자:** Lirui Wang, Xinlei Chen, Jialiang Zhao, Kaiming He (MIT CSAIL)

**학회/연도:** NeurIPS 2024

**아키텍처:** HPT addresses cross-embodiment heterogeneity by using embodiment-specific "stem" networks (small MLPs or convolutions) that project heterogeneous proprioceptive and action spaces into a shared latent representation. A shared transformer trunk processes the aligned representations, and embodiment-specific "head" networks decode outputs back to the original action space. Vision features come from pre-trained encoders (CLIP, DINOv2). The shared trunk has ~300M parameters; total size varies with the number of stems/heads.

**행동 공간:** Variable per embodiment, handled by the per-embodiment head networks. Supports arbitrary proprioceptive and action dimensions.

**다지 핸드 지원:** ✗ --- Not explicitly demonstrated on dexterous hands, though the heterogeneous stem/head architecture is designed to accommodate arbitrary embodiment configurations.

**힘/임피던스 출력:** ✗ --- Position targets only.

**핵심 방법론:** HPT tackles the fundamental challenge that different robots have different observation and action space dimensions, making naive cross-embodiment training impossible. The stem-trunk-head architecture decouples embodiment-specific processing from shared representation learning. During pretraining, multiple embodiment-specific stems and heads are trained jointly with the shared trunk, learning a universal manipulation representation. At fine-tuning time, new stems/heads can be added for unseen embodiments while keeping the trunk frozen.

**훈련 데이터:** Pretrained on diverse cross-embodiment datasets including subsets of OXE, spanning 50+ distinct robot configurations.

**주요 기여:**
- Proposed the stem-trunk-head architecture for heterogeneous cross-embodiment pretraining, providing a principled solution to the action/observation space mismatch problem.
- Demonstrated that a shared transformer trunk learns transferable manipulation representations across diverse embodiments.
- Showed that the approach scales with data diversity: more diverse pretraining data improves downstream fine-tuning performance.

**정량적 결과:**

| Benchmark / Task | HPT | Baseline | Notes |
|---|---|---|---|
| *(Consult the NeurIPS 2024 paper for per-task results. The paper reports improvements from scaling data diversity across embodiments.)* | | | |

**한계점:**
- Each new embodiment requires training a new stem and head, with some embodiment-specific data.
- The approach has not been evaluated on high-DoF dexterous hand systems.
- No language conditioning in the base model (proprioceptive-visual only).
- No public model weights released.

**공개 가중치/코드:** ✅ Code: [GitHub](https://github.com/liruiw/HPT). ✗ Pre-trained weights not publicly available.

## 추론 / 배포

- **추론 지연 시간:** Not explicitly benchmarked. The shared transformer trunk (~300M parameters) plus lightweight per-embodiment stems/heads should run at ~10-30 Hz on a desktop GPU, comparable to medium-sized transformer policies.
- **배포 하드웨어:** Not reported. The ~300M parameter trunk is moderate-sized, requiring a desktop GPU for real-time inference but smaller than billion-parameter VLAs.
- **실시간 가능 여부:** Yes, likely. The moderate model size and MLP-based stems/heads should support real-time control at typical manipulation frequencies. However, specific benchmarks are not reported.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** Subsets of Open X-Embodiment (OXE) spanning 50+ distinct robot configurations for pretraining. Fine-tuning on task-specific demonstration data.
- **수집 방법:** Aggregated cross-embodiment data from OXE (teleoperation, scripted policies). The stem-trunk-head architecture handles heterogeneous observation/action spaces across embodiments.
- **데이터 규모:** 50+ robot configurations for pretraining. Fine-tuning demonstration counts not specified.
- **원격 조작 장비:** Varies by OXE constituent dataset.
- **데이터 포맷:** Multiple formats handled by per-embodiment stem networks.
- **공개 여부:** OXE data is public. Pre-trained HPT weights are not released.

---
