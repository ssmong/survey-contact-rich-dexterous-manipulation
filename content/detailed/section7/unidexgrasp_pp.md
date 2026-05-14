### 7.1 UniDexGrasp++

**Full title:** UniDexGrasp++: Improving Dexterous Grasping Policy Learning via Geometry-aware Curriculum and Iterative Generalist-Specialist Learning

**Authors:** Weikang Wan, Haoran Geng, Yun Liu, Zikang Yan, Yaodong Yang, He Wang

**Venue/Year:** ICCV 2023

**PKU-EPIC lineage:** Improves UniDexGrasp from ~60% to 85.4% via iterative generalist-specialist learning. The geometry-aware curriculum and iterative specialist training specifically address the long-tail failure cases of UniDexGrasp.

**RL algorithm:** PPO with DAgger distillation; geometry-aware curriculum learning combined with iterative generalist-specialist training

**Hand hardware:** Shadow Hand (24 DoF)

**Sim platform:** IsaacGym

**Sim2Real?** No

**Object count:** 3000+ objects; 85.4% state-based success rate (sim), 78.2% vision-based (sim)

**Tasks:** Universal dexterous grasping -- grasping arbitrary objects from a tabletop given goal grasp poses

**Key methodology:** Proposes a two-phase training pipeline. First, a geometry-aware curriculum orders training objects by grasping difficulty (estimated from contact geometry). Second, an iterative generalist-specialist loop trains specialist policies on hard object clusters, then distills them back into a generalist. This iteratively improves performance on the long tail of difficult objects.

**Main contributions:**
- Geometry-aware curriculum that significantly accelerates training convergence
- Iterative generalist-specialist learning scheme that improves long-tail performance from ~60% (UniDexGrasp) to 85.4%
- Vision-based policy achieving 78.2% across 3000+ objects using point cloud input

**Quantitative results:**

| Metric | Value |
|---|---|
| State-based success rate | 85.4% (sim) |
| Vision-based success rate | 78.2% (sim) |
| UniDexGrasp baseline | ~60% (sim) |
| Improvement over predecessor | +25.4 pp |
| Object set size | 3000+ |

**Limitations/Gaps:** Simulation-only; requires pre-computed goal grasp poses (from contact map estimation); Shadow Hand only; gap between state-based and vision-based performance (~7%) suggests visual perception remains a bottleneck

**Sim-only limitation:** Evaluated in simulation only; no sim-to-real transfer demonstrated, real-world viability unvalidated.

## Inference / Deployment

- **Inference latency:** Not reported. The distilled generalist MLP policy runs in <1ms per forward pass.
- **Deployment hardware:** Simulation only (IsaacGym). No real-robot deployment demonstrated.
- **Real-time capable?** Yes, for the policy itself. However, only simulation evaluation was performed.

## Dataset / Data Collection

- **Dataset used:** No pre-collected demonstration dataset. Iterative generalist-specialist RL training with geometry-aware curriculum in IsaacGym.
- **Collection method:** Pure RL (PPO) with DAgger distillation in IsaacGym. Geometry-aware curriculum orders 3,000+ objects by grasping difficulty. Iterative generalist-specialist loop trains specialists on hard object clusters, distills back into generalist. Both state-based and vision-based (point cloud) policies.
- **Data scale:** 3,000+ objects. State-based: 85.4% success. Vision-based: 78.2% success (sim).
- **Teleop equipment:** Not applicable (pure RL, no demonstrations).
- **Data format:** Not applicable (online RL, no offline dataset).
- **Publicly available?** Dataset/code release status not reported.
