### 7.1 DexGraspNet 2.0

**Full title:** DexGraspNet 2.0: Learning Generative Dexterous Grasping in Large-scale Synthetic Cluttered Scenes

**Authors:** Jiayi Chen, Yuxing Chen, Jialiang Zhang, Yinzhen Xu, Weikang Wan, He Wang

**Venue/Year:** CoRL 2024

**PKU-EPIC lineage:** Extends DexGraspNet 1.0 from isolated object grasping to scene-aware grasping in clutter; introduces diffusion-based generation (vs optimization in BODex) and massive dataset scale (426M grasps).

**RL algorithm:** Diffusion model for grasp generation; trained on massive synthetic dataset with scene-level context (clutter awareness)

**Hand hardware:** Shadow Hand (24 DoF)

**Sim platform:** IsaacGym

**Sim2Real?** Yes; 90.7% real-world success rate (real) on cluttered tabletop grasping

**Object count:** 1319 objects; 426 million grasps in the dataset

**Tasks:** Dexterous grasping in cluttered scenes with scene-aware grasp generation

**Key methodology:** Extends DexGraspNet to cluttered scenes by training a diffusion model that generates grasps conditioned on both the target object and the surrounding scene context (neighboring objects, table). The 426M-grasp dataset is generated in simulation with procedural clutter layouts. Scene-level conditioning enables collision-aware grasp generation that avoids neighboring objects.

**Main contributions:**
- First large-scale dexterous grasping dataset with clutter context (426M grasps)
- Scene-aware diffusion model that generates collision-free grasps in cluttered environments
- 90.7% sim-to-real success rate (real), demonstrating practical deployment of diffusion-based grasp generation

**Quantitative results:**

| Metric | Value |
|---|---|
| Real-world success rate | 90.7% (real) |
| Dataset size | 426M grasps |
| Object set size | 1319 |
| Hand | Shadow (24 DoF) |

**Limitations/Gaps:** Still open-loop grasp generation (no reactive execution); relies on accurate scene reconstruction; Shadow Hand only; clutter handling is geometric (no reasoning about object semantics or task goals)

## Inference / Deployment

- **Inference latency:** Diffusion-based grasp generation requires multiple denoising steps. Specific latency not reported, but typical diffusion inference is 50-500ms per grasp on a modern GPU.
- **Deployment hardware:** Real-world deployment on Shadow Hand demonstrated (90.7% success rate on cluttered tabletop grasping). GPU for diffusion inference not specified.
- **Real-time capable?** Limited. Grasp generation is offline (diffusion sampling), but execution of generated grasps is real-time. The diffusion model generates grasp poses, not closed-loop control commands.

## Dataset / Data Collection

- **Dataset used:** Custom large-scale synthetic cluttered-scene grasping dataset. 426 million grasps across 1,319 objects with scene-level clutter context.
- **Collection method:** Procedural generation in IsaacGym simulation. Cluttered scenes created with procedural layout generation. Diffusion model trained on generated grasps conditioned on both target object and surrounding scene context.
- **Data scale:** 426 million grasps, 1,319 objects. Largest scene-aware dexterous grasping dataset at time of publication.
- **Teleop equipment:** Not applicable (procedural simulation generation).
- **Data format:** Object/scene point clouds + grasp poses. Specific format not reported.
- **Publicly available?** Dataset release status not reported.
