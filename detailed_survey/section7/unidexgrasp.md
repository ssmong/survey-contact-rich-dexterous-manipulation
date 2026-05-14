### 7.1 UniDexGrasp

**Full title:** UniDexGrasp: Universal Robotic Dexterous Grasping via Learning Diverse Proposal Generation and Goal-Conditioned Policy

**Authors:** Yinzhen Xu, Weikang Wan, Jialiang Zhang, Haoran Liu, Zikang Yan, Hao Shen, Ruicheng Wang, He Wang

**Venue/Year:** CVPR 2023

**RL algorithm:** PPO (goal-conditioned); two-stage pipeline with grasp proposal generation (CVAE) followed by goal-conditioned RL grasping policy

**Hand hardware:** Shadow Hand (24 DoF)

**Sim platform:** IsaacGym

**Sim2Real?** No

**Object count:** 3000+ objects from diverse categories; ~60% success rate (sim)

**Tasks:** Universal dexterous grasping from arbitrary initial configurations

**Key methodology:** Decomposes the universal grasping problem into two stages: (1) a contact-map-based grasp proposal network generates diverse feasible grasp poses for novel objects, and (2) a goal-conditioned RL policy (PPO) executes the grasp given the proposed target hand configuration. The grasp proposal network uses a conditional variational autoencoder trained on successful grasps.

**Main contributions:**
- First system to attempt universal dexterous grasping across 3000+ objects with a single pipeline
- Contact-map-based grasp proposal generation that generalizes to unseen object geometries
- Goal-conditioned RL policy that can reach diverse grasp configurations

**Quantitative results:**

| Metric | Value |
|---|---|
| Overall success rate | ~60% (sim) |
| Object set size | 3000+ |
| Hand | Shadow (24 DoF) |

Note: the ~60% success rate is significantly lower than the follow-up UniDexGrasp++ (85.4% sim), indicating the performance ceiling of the original pipeline.

**Limitations/Gaps:** ~60% success rate is significantly lower than UniDexGrasp++ (85.4%); struggles with objects that require precise finger placement; simulation-only; Shadow Hand only; requires object point cloud at test time

**Sim-only limitation:** Evaluated in simulation only; no sim-to-real transfer demonstrated, real-world viability unvalidated.

## Inference / Deployment

- **Inference latency:** Not reported. The CVAE grasp proposal + MLP goal-conditioned policy runs in <5ms total per step.
- **Deployment hardware:** Simulation only (IsaacGym). No real-robot deployment demonstrated.
- **Real-time capable?** Yes, for the policy itself. However, only simulation evaluation was performed.

## Dataset / Data Collection

- **Dataset used:** No pre-collected demonstration dataset. Two-stage pipeline: (1) CVAE-based grasp proposal network trained on successful grasps generated in simulation, (2) goal-conditioned RL policy (PPO) trained in IsaacGym.
- **Collection method:** Grasp proposals generated procedurally via contact-map-based CVAE. RL policy trained via online interaction in IsaacGym with 3,000+ objects. Object meshes from diverse 3D model datasets.
- **Data scale:** 3,000+ objects. Grasp proposals generated at scale; RL training episodes not reported.
- **Teleop equipment:** Not applicable (procedural generation + pure RL).
- **Data format:** Not applicable (online RL + procedural grasp generation).
- **Publicly available?** Object point clouds required at test time. Dataset/code release status not reported.
