### 2.5 Grasp as You Say

**Full title:** Grasp as You Say: Language-Guided Dexterous Grasp Generation

**Authors:** Yi-Lin Wei, Jian-Jian Jiang, Chengyi Xing, Xian-Tuo Tan, Xiao-Ming Wu, Hao Li, Mark Cutkosky, Wei-Shi Zheng (Sun Yat-sen University, iSEE Laboratory)

**Venue/Year:** NeurIPS 2024

**arXiv:** [2405.19291](https://arxiv.org/abs/2405.19291)

**Hand hardware:** Shadow Dexterous Hand (simulation); Allegro Hand (28 DoF) + Flexiv Rizon 4 arm (real-world deployment)

**Tasks:**
- Language-guided dexterous grasp generation (e.g., "grasp the mug by its handle," "pick up the bottle from the top")
- Part-aware grasping: generating grasps that target specific object regions specified by language
- Evaluation across multiple object categories with diverse grasp intents

**Key methodology:** Grasp as You Say generates dexterous grasp poses conditioned on natural language descriptions specifying how an object should be grasped. The system takes as input a 3D object representation (point cloud or mesh) and a language instruction describing the desired grasp (e.g., part to grasp, grasp style). A language encoder processes the instruction to produce a conditioning vector, which guides a generative model to produce Shadow Hand joint configurations and wrist poses that realize the described grasp. The approach bridges the gap between semantic grasp intent (expressed in language) and the high-dimensional configuration space of a dexterous hand.

**Architecture/Parameters:**
- Language encoder: pre-trained language model for instruction encoding
- Grasp generation: conditional generative model over dexterous hand configuration space (simulation: Shadow Hand; real-world: Allegro Hand 28 DoF + wrist pose)
- Conditioning mechanism: language embedding modulates the grasp generation process
- Specific model size/parameter counts not publicly detailed at the abstract level

**Main contributions:**
- Proposes language-conditioned dexterous grasp generation, a previously unaddressed problem (per authors), enabling semantic specification of grasp intent (part, style) for a 24-DoF hand
- Demonstration that natural language can effectively condition high-dimensional dexterous grasp synthesis, producing physically plausible grasps that match linguistic descriptions
- Part-aware grasping capability: the system can distinguish between "grasp the mug by the handle" vs. "grasp the mug by the body," generating distinct hand configurations for each

**Limitations/Gaps:**
- Grasp generation only: produces static grasp poses, not full manipulation trajectories or post-grasp actions
- Simulation uses Shadow Hand; real-world deployment uses Allegro Hand (28 DoF) -- no cross-embodiment evaluation beyond this pair
- No force or tactile feedback; grasps are evaluated geometrically and in simulation, not with real-world contact dynamics
- Limited to grasping intent expressed through language; does not handle multi-step task instructions or manipulation beyond the initial grasp
- Sim-to-real transfer for the generated grasps is not demonstrated

**Results:**

**Dataset scale:** 50,000 grasp-instruction pairs across 1,800 household object categories.

**Grasp success rate (simulation, Isaac Gym):**

| Method | Success Rate | Q1 Grasp Quality |
|---|---|---|
| GraspCVAE | 29.12% | 0.054 |
| GraspTTA | 43.46% | 0.071 |
| DGTR | 51.91% | 0.078 |
| SceneDiffuser | 62.24% | 0.083 |
| **DexGYSGrasp (ours)** | **63.31%** | **0.083** |

**Intention consistency (FID-based, lower is better):**

| Method | FID | P-FID | Chamfer Distance |
|---|---|---|---|
| GraspCVAE | 31.26 | 29.02 | 3.138 |
| DGTR | 23.31 | 15.77 | 2.895 |
| SceneDiffuser | 20.44 | 7.932 | 1.679 |
| **DexGYSGrasp (ours)** | **6.538** | **5.595** | **1.198** |

**Grasp diversity (8 samples per condition):**

| Metric | DexGYSGrasp | DGTR | SceneDiffuser |
|---|---|---|---|
| Translation std (delta_t) | 6.118 | 2.037 | 0.346 |
| Rotation std (delta_r) | 55.68 | 14.01 | 3.455 |
| Joint angle std (delta_q) | 6.118 | 4.299 | 0.387 |

**Penetration depth:** 0.223 cm (DexGYSGrasp) vs. 0.163 cm (DGTR).

- Evaluated on 1,800 object categories with 50,000 grasp-instruction pairs
- Real-world deployment uses Allegro Hand (28 DoF) + Flexiv Rizon 4 arm + Intel RealSense D415
- Code released at [GitHub](https://github.com/iSEE-Laboratory/Grasp-as-You-Say)

## Inference / Deployment

- **Inference latency:** Not reported. The paper does not disclose grasp generation time or inference latency.
- **Deployment hardware:** Training performed on a single RTX 4090 GPU. Real-world experiments use an Allegro Hand + Flexiv Rizon 4 arm + Intel RealSense D415 camera. Inference GPU not specified separately.
- **Real-time capable?** Not applicable in the typical sense -- the system generates static grasp poses (not closed-loop control). Grasp generation speed is not characterized. The system produces a single grasp configuration rather than a continuous control policy.

## Dataset / Data Collection

- **Dataset used:** DexGYS (custom dataset released with this work). Also leverages OakInk 3D object meshes and Shadow Hand MJCF models from PKU.
- **Collection method:** Hand-object interaction retargeting strategy for cost-efficient grasp annotation, combined with an LLM-assisted language guidance annotation system to generate natural language grasp descriptions.
- **Data scale:** Not explicitly reported. Training and test splits available (train_with_guide_v2.1.json, test_with_guide_v2.1.json).
- **Teleop equipment:** Not applicable (grasp annotations generated via retargeting and LLM-based annotation, not teleoperation).
- **Data format:** JSON files (train/test splits with language guidance). Includes 3D object meshes (from OakInk), Shadow Hand MJCF models, and matched grasp results.
- **Publicly available?** Yes. Dataset available on HuggingFace ([datasets/wyl2077/DexGYS](https://huggingface.co/datasets/wyl2077/DexGYS/tree/main)). Code at [GitHub](https://github.com/iSEE-Laboratory/Grasp-as-You-Say).
