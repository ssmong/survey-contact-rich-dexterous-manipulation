### 7.3 ComFree-Sim

### Model-Based MPC (not RL)

**Note: Model-based trajectory optimization/MPC, not RL.**

**전체 제목:** Complementarity-Free Dexterous Manipulation on GPU (ComFree-Sim)

**저자:** Not fully verified (2026 preprint)

**학회/연도:** arXiv 2026

**arXiv:** https://arxiv.org/abs/2603.12185

**Method:** GPU-parallel complementarity-free contact simulation for trajectory optimization and MPC. Extends the complementarity-free approach to run on NVIDIA Warp for massively parallel contact computation.

**핸드 하드웨어:** LEAP Hand (16 DoF)

**시뮬레이션 플랫폼:** Custom simulator built on NVIDIA Warp

**Sim2Real 여부:** No. Simulation-only.

**작업:** Multi-finger contact-rich manipulation with the LEAP Hand. Contact-mode-switching tasks similar to the complementarity-free line of work but parallelized across thousands of environments.

**핵심 방법론:** ComFree-Sim takes the complementarity-free differentiable contact model and implements it on GPU using NVIDIA Warp, enabling thousands of parallel contact simulations. This bridges the gap between the physical accuracy of contact-implicit optimization and the parallelism of RL simulation platforms like IsaacGym. The GPU backend enables both massively parallel MPC rollouts and potential integration with RL training loops.

**주요 기여:**
- Ported complementarity-free contact simulation to GPU (NVIDIA Warp), achieving large-scale parallelism
- Enabled thousands of parallel contact-rich manipulation simulations, previously limited to single-environment CPU computation
- Demonstrated the LEAP Hand as a target platform, broadening applicability beyond Drake/Allegro setups

**한계점:** Very recent preprint (2026) with limited external validation. No sim-to-real results. Code not publicly available as of survey date. The NVIDIA Warp ecosystem is less mature than IsaacGym/MuJoCo for full RL workflows.

**시뮬레이션 전용 한계:** 시뮬레이션에서만 평가됨; sim-to-real 전이 미입증, 실제 환경 실행 가능성 미검증.

**결과:** Achieved GPU-parallel contact simulation for LEAP Hand manipulation (sim). Specific quantitative results pending further publication.

## 추론 / 배포

- **추론 지연 시간:** GPU-parallel complementarity-free simulation enables massively parallel contact computation. Specific Hz for single-instance MPC not reported, but GPU parallelism is designed for real-time or faster-than-real-time operation.
- **배포 하드웨어:** Simulation only (NVIDIA Warp). No real-robot deployment demonstrated.
- **실시간 가능 여부:** Designed for real-time GPU-parallel MPC, but real-hardware deployment not demonstrated.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** No dataset. GPU-parallel complementarity-free contact simulation for trajectory optimization/MPC.
- **수집 방법:** Not applicable. Extends the complementarity-free differentiable contact model to NVIDIA Warp for massively parallel contact computation. No training data -- model-based approach. Enables both parallel MPC rollouts and potential integration with RL training.
- **데이터 규모:** Not applicable (model-based simulation framework).
- **원격 조작 장비:** Not applicable.
- **데이터 포맷:** Not applicable.
- **공개 여부:** Code not publicly available as of survey date (2026 preprint).
