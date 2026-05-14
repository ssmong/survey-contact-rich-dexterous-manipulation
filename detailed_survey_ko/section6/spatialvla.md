### SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model

**전체 제목:** SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model

**저자:** Delin Qu, Haoming Song, Qizhi Chen, Yuanqi Yao, Xinyi Ye, Yan Ding, Zhigang Wang, JiaYuan Gu, Bin Zhao, Dong Wang, Xuelong Li (Shanghai AI Laboratory, Fudan University, Shanghai Jiao Tong University, Zhejiang University, ShanghaiTech University, Northwestern Polytechnical University)

**학회/연도:** RSS 2025

**아키텍처:** 3.5B parameter VLA built on the PaliGemma2 VLM backbone. The vision encoder is SigLIP, and the language model is Gemma 2. SpatialVLA introduces two spatial modules on top of this backbone: (1) Ego3D Position Encoding, which integrates monocular depth (from ZoeDepth) with 2D semantic features via camera back-projection and sinusoidal encoding + learnable MLPs, injecting 3D spatial awareness into visual tokens; and (2) Adaptive Action Grids, which discretize continuous 7D actions into 3 spatial tokens (translation + rotation + gripper) using a Gaussian-fitted non-uniform grid with 8,194 vocabulary entries, replacing the standard 7-token-per-step linear binning.

**행동 공간:** 7D (3D translation + 3D rotation + gripper), discretized into 3 spatial tokens per step via Adaptive Action Grids. The grid partitions are fitted to per-dimension Gaussian action distributions, concentrating resolution where actions are dense. During fine-tuning, grids can be re-adapted via trilinear interpolation of token embeddings.

**다지 핸드 지원:** ✗ --- Gripper-only (single-arm) evaluation.

**힘/임피던스 출력:** ✗ --- Position targets only.

**핵심 방법론:** SpatialVLA addresses the observation that standard VLAs lack explicit 3D spatial understanding, which limits precise manipulation. Ego3D Position Encoding injects egocentric 3D coordinates into visual tokens without requiring external 3D sensors --- only RGB + monocular depth estimation. Adaptive Action Grids reduce the number of action tokens from 7 to 3 per step while preserving precision by concentrating discretization bins where actions are statistically dense, improving both inference speed and action quality. The model is pretrained on 1.1M real-world robot episodes and supports zero-shot transfer and LoRA fine-tuning.

**훈련 데이터:** Pretrained on 1.1M real-world robot episodes from a mixture of Open X-Embodiment (OXE) subsets and RH20T. Fine-tuned on downstream tasks including Google Fractal, BridgeData V2, and LIBERO (50 demonstrations per task). Training: 10 days on 64 A100 GPUs, batch size 2,048.

**주요 기여:**
- Introduced Ego3D Position Encoding to inject monocular-depth-derived 3D spatial information into VLA visual tokens, improving spatial reasoning without requiring depth sensors at test time.
- Proposed Adaptive Action Grids that reduce action tokens from 7 to 3 per step while maintaining precision via distribution-aware non-uniform discretization, enabling ~20 Hz inference.
- Achieved the highest reported zero-shot and fine-tuned scores on SimplerEnv benchmarks among models at or below 3.5B parameters (as of RSS 2025), competitive with models 15x larger (RT-2-X 55B).

**정량적 결과:**

| Benchmark / Task | SpatialVLA (zero-shot) | SpatialVLA (fine-tuned) | OpenVLA | Octo | Notes |
|---|---|---|---|---|---|
| SimplerEnv Google Robot (visual matching) | 71.9% | 75.1% | ~49% | — | +15.6% over RoboVLM zero-shot |
| SimplerEnv Google Robot (variant agg.) | 68.8% | 70.7% | — | — | |
| SimplerEnv WidowX (zero-shot) | 34.4% | 42.7% | — | — | 100% on eggplant task after FT |
| LIBERO average (fine-tuned) | — | 78.1% | 76.5% | 75.1% | Ranked 1st; LIBERO-Spatial: 88.2% |
| Inference speed | ~20 Hz (RTX 4090, 8.5 GB) | | ~5 Hz | | |

**한계점:**
- Gaussian fitting for action grids is suboptimal for distributions with extreme single-axis motions, which can cause grid clustering and capability loss.
- Autoregressive decoding is inherently slower than diffusion-based action heads for high-frequency control.
- No history/temporal context mechanism; relies on single-frame observations, limiting long-horizon task performance (struggles on LIBERO-Long).
- Variable quality in the OXE dataset hinders training efficiency; data curation/distillation is needed.
- Gripper-only; no dexterous hand or force-aware evaluation.

**공개 가중치/코드:** ✅ Code and weights: [project page](https://spatialvla.github.io/). Authors state all code and details are open-sourced.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** Open X-Embodiment (OXE) subsets + RH20T for pretraining. BridgeData V2, Google Fractal, LIBERO for fine-tuning.
- **수집 방법:** Aggregated cross-embodiment data from OXE. Fine-tuning demonstrations from standard benchmarks.
- **데이터 규모:** 1.1M real-world robot episodes for pretraining. Fine-tuning: 50 demonstrations per task (LIBERO), 6 episodes (Fractal).
- **원격 조작 장비:** Varies by OXE constituent dataset.
- **데이터 포맷:** RLDS (OXE standard).
- **공개 여부:** OXE and RH20T are public. Model weights available via project page.

---
