### CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation

**전체 제목:** CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation

**저자:** Qixiu Li, Yaobo Liang, Zeyu Wang, Lin Luo, Xi Chen, Mozheng Liao, Fangyun Wei, Yu Deng, Sicheng Xu, Yizhong Zhang, Xiaofan Wang, Bei Liu, Jianlong Fu, Jianmin Bao, Dong Chen, Yuanchun Shi, Jiaolong Yang, Baining Guo (Microsoft Research)

**학회/연도:** arXiv 2024

**아키텍처:** CogACT separates the VLA into explicit cognition and action stages. The cognition module is a VLM (InternVL2 based on InternViT-300M + InternLM2-1.8B) that processes visual observations and language instructions to produce a latent "cognitive plan." The action module is a diffusion-based decoder that translates the cognitive plan into continuous robot actions. This separation allows each module to be optimized independently and enables iterative refinement of the action generation.

**행동 공간:** 7D (6-DoF EEF delta + gripper), generated as continuous values via diffusion decoding with action chunking.

**다지 핸드 지원:** ✗ --- Gripper-only evaluation.

**힘/임피던스 출력:** ✗ --- Position targets only.

**핵심 방법론:** CogACT argues that existing VLAs conflate two fundamentally different tasks --- semantic understanding and precise motor control --- in a single autoregressive decoding process, which degrades both. By explicitly separating cognition (VLM reasoning) from action (diffusion generation), each module can use the architecture best suited to its task. The cognitive plan serves as a compressed, semantically rich conditioning signal for the diffusion action head, avoiding the information bottleneck of tokenized actions.

**훈련 데이터:** Pretrained on OXE cross-embodiment data. Fine-tuned on SimplerEnv and real-robot manipulation tasks.

**주요 기여:**
- Proposed explicit cognition-action separation *within a single end-to-end VLA architecture*, with a VLM generating a latent plan and a diffusion head generating precise actions. (Note: prior work such as SayCan separated reasoning from action execution differently --- at the system level, with a language model selecting from a fixed set of pre-trained skills. CogACT's contribution is integrating both stages into a single differentiable architecture where the cognitive plan is a learned latent representation, not a discrete skill selection.)
- Demonstrated that this separation improves both language understanding and action precision compared to monolithic VLAs.
- Achieved highest reported results on SimplerEnv benchmarks at the time of publication.

**정량적 결과:**

| Benchmark / Task | CogACT | OpenVLA | RT-2-X | Notes |
|---|---|---|---|---|
| *(Consult the arXiv paper for per-task results on SimplerEnv and real-robot evaluations. The paper reports highest reported SimplerEnv performance at time of publication.)* | | | | |

**한계점:**
- Two-stage architecture increases overall model complexity and may introduce latency between cognition and action.
- Only evaluated on gripper-based systems with 7D actions.
- No force/compliance awareness.
- Pre-trained weights not publicly released.

**공개 가중치/코드:** ✅ Code: [GitHub](https://github.com/microsoft/CogACT). ✗ Model weights not publicly available.

## 추론 / 배포

- **추론 지연 시간:** Not explicitly benchmarked. The two-stage architecture (VLM cognition + diffusion action) introduces latency from both stages: the InternVL2 VLM (~2B parameters) processes visual/language input, then the diffusion decoder generates actions over multiple denoising steps. Estimated ~5-15 Hz depending on diffusion steps and hardware.
- **배포 하드웨어:** Not reported. The ~2B parameter VLM backbone requires a GPU for real-time inference (e.g., A100 or RTX 4090 class).
- **실시간 가능 여부:** Limited. The two-stage pipeline adds latency compared to monolithic VLAs. The diffusion action head requires multiple denoising steps. Suitable for moderate-speed manipulation but may be too slow for high-frequency dexterous control.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** Open X-Embodiment (OXE) for cross-embodiment pretraining. Fine-tuned on SimplerEnv and real-robot manipulation tasks.
- **수집 방법:** Aggregated cross-embodiment data from OXE. Fine-tuning demonstrations from standard manipulation benchmarks.
- **데이터 규모:** OXE pretraining scale (comparable to OpenVLA). Fine-tuning task-specific demonstration counts not reported.
- **원격 조작 장비:** Varies by OXE constituent dataset.
- **데이터 포맷:** RLDS (OXE standard).
- **공개 여부:** OXE data is public. CogACT model weights are not released.

---
