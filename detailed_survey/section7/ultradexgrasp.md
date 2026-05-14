### 7.1 UltraDexGrasp

**Full title:** UltraDexGrasp: Ultra-Scalable Dexterous Grasping with Cross-Embodiment Diverse Grasp Dataset

**Authors:** Jiayi Chen, He Wang, et al.

**Venue/Year:** ICRA 2026

**PKU-EPIC lineage:** Scales Dexonomy from 9.5M to 20M grasps; the primary contribution is dataset scale, not algorithmic novelty. The optimization pipeline (BODex/cuRobo bilevel optimization) and taxonomy structure (from Dexonomy) are inherited. The paper demonstrates that scaling the generated grasp data improves cross-embodiment transfer but does not introduce new optimization or learning methods.

**RL algorithm:** Multi-strategy approach combining optimization (BODex/cuRobo) with policy learning; leverages diverse grasp datasets for cross-embodiment training

**Hand hardware:** Multiple dexterous hands (cross-embodiment)

**Sim platform:** BODex + cuRobo

**Sim2Real?** Yes; 81.2% real-world success rate (real)

**Object count:** 20 million training frames across diverse objects

**Tasks:** Ultra-scale cross-embodiment dexterous grasping

**Key methodology:** Builds on the BODex/Dexonomy pipeline to generate an ultra-large-scale cross-embodiment grasp dataset (20M frames), then trains cross-embodiment grasping policies using this data. The multi-strategy approach combines optimization-based grasp generation with learned execution policies, leveraging the scale and diversity of the generated dataset to achieve robust generalization.

**Main contributions:**
- Largest-scale dexterous grasping dataset at time of publication (20M frames)
- Cross-embodiment grasping trained from diverse generated data rather than hand-specific policies
- Demonstrates that scaling grasp data generation translates to improved real-world transfer

**Quantitative results:**

| Metric | Value |
|---|---|
| Real-world success rate | 81.2% (real) |
| Dataset size | 20M frames |
| Dexonomy baseline dataset | 9.5M grasps |

**Limitations/Gaps:** Building on prior optimization pipelines (BODex, Dexonomy) -- incremental improvement over those baselines; 81.2% real success rate is lower than RobustDexGrasp (94.6%), suggesting cross-embodiment generality trades off with single-embodiment performance; limited task diversity beyond grasping

## Inference / Deployment

- **Inference latency:** Not explicitly reported. The learned policy runs in <5ms per forward pass. Optimization-based grasp generation is offline.
- **Deployment hardware:** Multiple dexterous hands (cross-embodiment). 81.2% real-world success rate demonstrated.
- **Real-time capable?** Yes, at deployment. The learned policy supports real-time grasping control on real hardware.

## Dataset / Data Collection

- **Dataset used:** Ultra-large-scale cross-embodiment grasp dataset, extending BODex/Dexonomy pipelines. 20 million training frames.
- **Collection method:** Optimization-based grasp generation (BODex/cuRobo bilevel optimization) combined with policy learning from generated data. Cross-embodiment training across multiple hand morphologies.
- **Data scale:** 20 million training frames. Extends Dexonomy's 9.5M grasps to larger scale.
- **Teleop equipment:** Not applicable (optimization-based generation + RL from generated data).
- **Data format:** Grasp datasets with training frames for cross-embodiment policy learning.
- **Publicly available?** Dataset release status not reported.
