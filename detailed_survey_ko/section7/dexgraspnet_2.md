### 7.1 DexGraspNet 2.0

**전체 제목:** DexGraspNet 2.0: Learning Generative Dexterous Grasping in Large-scale Synthetic Cluttered Scenes

**저자:** Jiayi Chen, Yuxing Chen, Jialiang Zhang, Yinzhen Xu, Weikang Wan, He Wang

**학회/연도:** CoRL 2024

**PKU-EPIC lineage:** Extends DexGraspNet 1.0 from isolated object grasping to scene-aware grasping in clutter; introduces diffusion-based generation (vs optimization in BODex) and massive dataset scale (426M grasps).

**RL 알고리즘:** Diffusion model for grasp generation; trained on massive synthetic dataset with scene-level context (clutter awareness)

**핸드 하드웨어:** Shadow Hand (24 DoF)

**시뮬레이션 플랫폼:** IsaacGym

**Sim2Real 여부:** Yes; 90.7% real-world success rate (real) on cluttered tabletop grasping

**객체 수:** 1319 objects; 426 million grasps in the dataset

**작업:** Dexterous grasping in cluttered scenes with scene-aware grasp generation

**핵심 방법론:** Extends DexGraspNet to cluttered scenes by training a diffusion model that generates grasps conditioned on both the target object and the surrounding scene context (neighboring objects, table). The 426M-grasp dataset is generated in simulation with procedural clutter layouts. Scene-level conditioning enables collision-aware grasp generation that avoids neighboring objects.

**주요 기여:**
- First large-scale dexterous grasping dataset with clutter context (426M grasps)
- Scene-aware diffusion model that generates collision-free grasps in cluttered environments
- 90.7% sim-to-real success rate (real), demonstrating practical deployment of diffusion-based grasp generation

**정량적 결과:**

| Metric | Value |
|---|---|
| Real-world success rate | 90.7% (real) |
| Dataset size | 426M grasps |
| Object set size | 1319 |
| Hand | Shadow (24 DoF) |

**한계점:** Still open-loop grasp generation (no reactive execution); relies on accurate scene reconstruction; Shadow Hand only; clutter handling is geometric (no reasoning about object semantics or task goals)

## 추론 / 배포

- **추론 지연 시간:** Diffusion-based grasp generation requires multiple denoising steps. Specific latency not reported, but typical diffusion inference is 50-500ms per grasp on a modern GPU.
- **배포 하드웨어:** Real-world deployment on Shadow Hand demonstrated (90.7% success rate on cluttered tabletop grasping). GPU for diffusion inference not specified.
- **실시간 가능 여부:** Limited. Grasp generation is offline (diffusion sampling), but execution of generated grasps is real-time. The diffusion model generates grasp poses, not closed-loop control commands.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** Custom large-scale synthetic cluttered-scene grasping dataset. 426 million grasps across 1,319 objects with scene-level clutter context.
- **수집 방법:** Procedural generation in IsaacGym simulation. Cluttered scenes created with procedural layout generation. Diffusion model trained on generated grasps conditioned on both target object and surrounding scene context.
- **데이터 규모:** 426 million grasps, 1,319 objects. Largest scene-aware dexterous grasping dataset at time of publication.
- **원격 조작 장비:** Not applicable (procedural simulation generation).
- **데이터 포맷:** Object/scene point clouds + grasp poses. Specific format not reported.
- **공개 여부:** Dataset release status not reported.
