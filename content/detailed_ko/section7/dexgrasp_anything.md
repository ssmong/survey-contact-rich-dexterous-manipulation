### 7.1 DexGrasp Anything

**전체 제목:** DexGrasp Anything: Learning Universal Dexterous Grasping with Diffusion Models

**저자:** Jiayi Chen, Yubin Ke, Renxin Zhong, Shilong Mu, Hao-Shu Fang, Cewu Lu

**학회/연도:** CVPR 2025 (Highlight)

**RL 알고리즘:** Diffusion model (denoising diffusion probabilistic model for grasp pose generation); not standard RL but a generative approach

**핸드 하드웨어:** Shadow Hand (24 DoF)

**시뮬레이션 플랫폼:** IsaacGym

**Sim2Real 여부:** No

**객체 수:** 15,000+ objects; 3.4 million generated grasps across the dataset

**작업:** Universal dexterous grasp synthesis for arbitrary objects, including challenging thin, small, and articulated objects

**핵심 방법론:** Trains a diffusion model to generate dexterous grasp poses conditioned on object point clouds. The model learns the distribution of successful grasps from a large-scale simulated dataset, then generates diverse grasp proposals at inference via iterative denoising. A physics-based discriminator filters generated grasps for feasibility and stability.

**주요 기여:**
- Diffusion-based grasp generation enabling diverse, multi-modal grasp sampling for each object
- Largest dexterous grasping dataset at time of publication (3.4M grasps, 15K+ objects)
- Handles challenging object categories (thin, small, articulated) where optimization-based methods struggle

**정량적 결과:**

| Metric | Value |
|---|---|
| Object set size | 15,000+ |
| Generated grasps | 3.4M |
| Hand | Shadow (24 DoF) |
| Evaluation | Simulation only (sim) |

**한계점:** Simulation-only; Shadow Hand only; open-loop grasp generation without execution policy; diffusion sampling speed may limit real-time deployment; no demonstration of closed-loop grasping with the generated poses

**시뮬레이션 전용 한계:** 시뮬레이션에서만 평가됨; sim-to-real 전이 미입증, 실제 환경 실행 가능성 미검증.

## 추론 / 배포

- **추론 지연 시간:** Diffusion-based grasp pose generation requires multiple denoising steps (50-500ms per grasp on a modern GPU). This is offline grasp generation, not real-time control.
- **배포 하드웨어:** Simulation only (IsaacGym). No real-robot deployment demonstrated.
- **실시간 가능 여부:** No, for grasp generation (diffusion sampling is offline). The generated grasp poses could be executed by a real-time controller, but the full pipeline was not demonstrated in real-time.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** Custom large-scale simulated dexterous grasping dataset. 3.4 million generated grasps across 15,000+ objects.
- **수집 방법:** Diffusion model trained on simulated grasp data. Grasps generated in IsaacGym via simulation rollouts with physics-based discriminator filtering for feasibility and stability. Shadow Hand (24 DoF).
- **데이터 규모:** 3.4 million grasps, 15,000+ objects. Largest dexterous grasping dataset at time of publication.
- **원격 조작 장비:** Not applicable (simulated grasp generation, no demonstrations).
- **데이터 포맷:** Object point clouds + grasp poses. Specific file format not reported.
- **공개 여부:** Dataset release status not reported.
