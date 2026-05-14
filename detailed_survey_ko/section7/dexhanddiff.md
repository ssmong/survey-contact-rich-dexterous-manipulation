### 7.2 DexHandDiff

**전체 제목:** DexHandDiff: Interaction-Aware Diffusion Planning for Adaptive Dexterous Manipulation

**저자:** Zixuan Liang, Xinyu Zhan, Yisi Hu, Zhehao Cai, Jian Tang, Jianqiang Wang

**학회/연도:** CVPR 2025

**RL 알고리즘:** Diffusion-based planning (denoising diffusion for trajectory generation); not standard RL but generates full manipulation trajectories via conditional diffusion

**핸드 하드웨어:** Shadow Hand (24 DoF)

**시뮬레이션 플랫폼:** Adroit (MuJoCo-based benchmark)

**Sim2Real 여부:** No (simulation benchmark evaluation)

**객체 수:** Standard Adroit benchmark objects (pen, door, hammer, ball, etc.)

**작업:** In-hand pen rotation, door opening, hammer use, ball relocation -- the standard Adroit benchmark suite plus additional manipulation tasks

**핵심 방법론:** Uses a conditional diffusion model to generate full manipulation trajectories (sequence of hand joint configurations) conditioned on the current state and goal. The key innovation is interaction-aware denoising: the diffusion process incorporates predicted contact information to guide trajectory generation toward physically plausible contact-rich motions. This avoids the myopic behavior of single-step RL policies by planning entire trajectories.

**주요 기여:**
- Interaction-aware diffusion planning that incorporates contact prediction into trajectory generation
- Full-trajectory planning for dexterous manipulation (vs. single-step policy output)
- State-of-the-art results on Adroit benchmark tasks, outperforming prior RL and imitation learning methods

**한계점:** Simulation-only (Adroit benchmark); computational cost of diffusion planning may limit real-time deployment; evaluated on Shadow Hand in MuJoCo only; no real-world validation; limited to the standard Adroit task set

**시뮬레이션 전용 한계:** 시뮬레이션에서만 평가됨; sim-to-real 전이 미입증, 실제 환경 실행 가능성 미검증.

## 추론 / 배포

- **추론 지연 시간:** Diffusion-based trajectory planning requires multiple denoising steps (50-500ms per trajectory on a modern GPU). Not designed for real-time step-by-step control.
- **배포 하드웨어:** Simulation only (Adroit/MuJoCo). No real-robot deployment demonstrated.
- **실시간 가능 여부:** Limited. Diffusion planning generates full trajectories offline; real-time replanning would require fast denoising (DDIM acceleration) or caching.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** Adroit benchmark demonstration data (MuJoCo) for training the diffusion-based trajectory planner.
- **수집 방법:** Diffusion-based planning -- not standard RL. Conditional diffusion model generates full manipulation trajectories from state+goal. Trained on demonstration trajectories from the Adroit benchmark suite. Interaction-aware denoising incorporates predicted contact information.
- **데이터 규모:** Standard Adroit benchmark demonstration sets (pen, door, hammer, ball tasks). Specific episode counts per task follow Adroit conventions.
- **원격 조작 장비:** Not applicable (Adroit demonstrations are pre-collected scripted/expert data).
- **데이터 포맷:** Adroit benchmark format (MuJoCo state trajectories).
- **공개 여부:** Adroit benchmark is publicly available. DexHandDiff code release status not reported.
