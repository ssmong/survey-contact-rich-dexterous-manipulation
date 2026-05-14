### 7.1 Dexonomy

**Full title:** Dexonomy: A Taxonomy and a Scalable Generation Pipeline for Dexterous Grasping

**Authors:** Jiayi Chen, Yuxing Chen, C. Karen Liu, He Wang

**Venue/Year:** RSS 2025

**PKU-EPIC lineage:** Extends BODex with 31 grasp types (vs untyped in BODex); the bilevel optimization core is shared with BODex, but Dexonomy adds a systematic grasp taxonomy derived from human grasping literature. The taxonomy-driven contact region templates are the primary contribution beyond BODex.

**RL algorithm:** Optimization-based (not RL); extends BODex with a taxonomy-driven grasp generation pipeline; uses cuRobo for IK solving

**Hand hardware:** Shadow Hand (24 DoF), Allegro Hand (16 DoF), LEAP Hand (16 DoF), Unitree G1 humanoid hand

**Sim platform:** MuJoCo + cuRobo

**Sim2Real?** Yes; 82.3% real-world success rate (real)

**Object count:** 10,700 objects across 31 grasp types; 9.5 million generated grasps

**Tasks:** Taxonomy-guided dexterous grasp generation with 31 distinct grasp types (precision, power, lateral, etc.)

**Key methodology:** Introduces a comprehensive grasp taxonomy with 31 types derived from human grasping literature, then builds a scalable pipeline that generates type-specific grasps for arbitrary objects. For each grasp type, contact region templates specify which hand surfaces contact which object surfaces. The optimization pipeline matches these templates to object geometry and solves for feasible hand configurations.

**Main contributions:**
- First systematic grasp taxonomy (31 types) applied to robotic dexterous grasp generation
- Scalable pipeline generating 9.5M grasps across 10.7K objects and 4 hand embodiments
- Cross-embodiment generalization across Shadow, Allegro, LEAP, and Unitree G1 hands

**Quantitative results:**

| Metric | Value |
|---|---|
| Real-world success rate | 82.3% (real) |
| Object set size | 10,700 |
| Grasp types | 31 |
| Generated grasps | 9.5M |
| Hands supported | Shadow, Allegro, LEAP, Unitree G1 |

**Limitations/Gaps:** Taxonomy is static and may not capture task-specific grasp requirements; optimization-based (no learned closed-loop policy); real-world validation limited to a subset of grasp types; assumes known object geometry

## Inference / Deployment

- **Inference latency:** Optimization-based grasp computation is offline. cuRobo-accelerated IK solving. Deployment executes pre-computed grasps open-loop.
- **Deployment hardware:** Real deployment on multiple hand platforms (Shadow, Allegro, LEAP, Unitree G1). 82.3% real-world success rate.
- **Real-time capable?** Yes, at deployment (pre-computed grasps executed open-loop). No online inference bottleneck.

## Dataset / Data Collection

- **Dataset used:** Procedurally generated taxonomy-driven grasp dataset. 10,700 objects, 31 grasp types, 9.5 million grasps total.
- **Collection method:** Optimization-based (extends BODex pipeline with taxonomy-driven contact region templates). cuRobo for IK solving. Cross-embodiment: Shadow, Allegro, LEAP, Unitree G1 hands. No RL, no demonstrations.
- **Data scale:** 9.5 million generated grasps across 10,700 objects and 4 hand embodiments. 31 grasp types (precision, power, lateral, etc.).
- **Teleop equipment:** Not applicable (optimization-based, no demonstrations).
- **Data format:** Grasp configurations indexed by object, hand, and grasp type.
- **Publicly available?** Dataset release status not reported. CAD and code availability not specified.
