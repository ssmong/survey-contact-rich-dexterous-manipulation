### 7.1 DexGrasp Anything

**Full title:** DexGrasp Anything: Learning Universal Dexterous Grasping with Diffusion Models

**Authors:** Jiayi Chen, Yubin Ke, Renxin Zhong, Shilong Mu, Hao-Shu Fang, Cewu Lu

**Venue/Year:** CVPR 2025 (Highlight)

**RL algorithm:** Diffusion model (denoising diffusion probabilistic model for grasp pose generation); not standard RL but a generative approach

**Hand hardware:** Shadow Hand (24 DoF)

**Sim platform:** IsaacGym

**Sim2Real?** No

**Object count:** 15,000+ objects; 3.4 million generated grasps across the dataset

**Tasks:** Universal dexterous grasp synthesis for arbitrary objects, including challenging thin, small, and articulated objects

**Key methodology:** Trains a diffusion model to generate dexterous grasp poses conditioned on object point clouds. The model learns the distribution of successful grasps from a large-scale simulated dataset, then generates diverse grasp proposals at inference via iterative denoising. A physics-based discriminator filters generated grasps for feasibility and stability.

**Main contributions:**
- Diffusion-based grasp generation enabling diverse, multi-modal grasp sampling for each object
- Largest dexterous grasping dataset at time of publication (3.4M grasps, 15K+ objects)
- Handles challenging object categories (thin, small, articulated) where optimization-based methods struggle

**Quantitative results:**

| Metric | Value |
|---|---|
| Object set size | 15,000+ |
| Generated grasps | 3.4M |
| Hand | Shadow (24 DoF) |
| Evaluation | Simulation only (sim) |

**Limitations/Gaps:** Simulation-only; Shadow Hand only; open-loop grasp generation without execution policy; diffusion sampling speed may limit real-time deployment; no demonstration of closed-loop grasping with the generated poses

**Sim-only limitation:** Evaluated in simulation only; no sim-to-real transfer demonstrated, real-world viability unvalidated.

## Inference / Deployment

- **Inference latency:** Diffusion-based grasp pose generation requires multiple denoising steps (50-500ms per grasp on a modern GPU). This is offline grasp generation, not real-time control.
- **Deployment hardware:** Simulation only (IsaacGym). No real-robot deployment demonstrated.
- **Real-time capable?** No, for grasp generation (diffusion sampling is offline). The generated grasp poses could be executed by a real-time controller, but the full pipeline was not demonstrated in real-time.

## Dataset / Data Collection

- **Dataset used:** Custom large-scale simulated dexterous grasping dataset. 3.4 million generated grasps across 15,000+ objects.
- **Collection method:** Diffusion model trained on simulated grasp data. Grasps generated in IsaacGym via simulation rollouts with physics-based discriminator filtering for feasibility and stability. Shadow Hand (24 DoF).
- **Data scale:** 3.4 million grasps, 15,000+ objects. Largest dexterous grasping dataset at time of publication.
- **Teleop equipment:** Not applicable (simulated grasp generation, no demonstrations).
- **Data format:** Object point clouds + grasp poses. Specific file format not reported.
- **Publicly available?** Dataset release status not reported.
