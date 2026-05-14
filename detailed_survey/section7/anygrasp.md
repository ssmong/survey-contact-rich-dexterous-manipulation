### 7.1 AnyGrasp

**Full title:** AnyGrasp: Robust and Efficient Grasp Perception in Spatial and Temporal Domains

**Authors:** Hao-Shu Fang, Chenxi Wang, Hongjie Fang, Minghao Gou, Jirong Liu, Hengxu Yan, Wenhai Liu, Yichen Xie, Cewu Lu (Shanghai Jiao Tong University)

**Venue/Year:** IEEE Transactions on Robotics (T-RO), 2023 (arXiv 2212.08333, December 2022)

**Inclusion rationale:** AnyGrasp is primarily a parallel-jaw grasp detection system, not a dexterous hand method. It is included here because it serves as a widely-used upstream grasp perception module in dexterous manipulation pipelines. Several dexterous VLA and grasping papers (e.g., DexGraspVLA, grasping systems using point cloud inputs) build upon or compare against AnyGrasp's grasp detection backbone. Understanding this foundational module provides context for the dexterous grasping methods in this section.

**RL algorithm:** Not RL-based. AnyGrasp uses supervised learning with dense analytical grasp labels. The GSNet (Grasp Scoring Network) architecture is trained on the GraspNet-1Billion dataset with dense supervision combining real perception data and analytically generated grasp labels.

**Hand hardware:** Parallel-jaw gripper (not a dexterous hand). Generates 7-DoF grasp poses for two-finger grippers.

**Sim platform:** Trained on GraspNet-1Billion dataset (which includes simulation-generated grasp labels); deployed directly on real hardware.

**Sim2Real?** Yes. Trained on GraspNet-1Billion (real RGB-D + analytical grasp labels) and deployed directly on physical robots with 93.3% success rate clearing 300+ unseen objects.

**Object count:** 300+ unseen objects in bin-clearing evaluation.

**Tasks:** Grasp detection and execution in cluttered scenes. Key capabilities:
1. Static grasp detection from single-frame point clouds
2. Dynamic grasp tracking (temporal correspondence across frames, demonstrated catching a swimming robot fish)
3. Bin clearing with dense clutter

**Key methodology:** AnyGrasp builds on GSNet, a point-cloud-based grasp detection network using PointNet2 backbone. The system processes depth images into point clouds and predicts dense 7-DoF grasp poses (position, orientation, width) with quality scores. Key innovations:
- **Dense supervision:** Combines real perception data with analytically generated grasp labels, providing richer training signal than sparse human annotations.
- **Center-of-mass awareness:** Incorporates object CoM estimation to predict more stable grasps.
- **Temporal grasp tracking:** Extends single-frame detection to temporal domain, establishing correspondence between grasps across frames for dynamic/moving objects.
- **Robustness to depth noise:** Demonstrated grasp detection under significant depth-sensing noise from consumer-grade RGB-D cameras.

**Main contributions:**
- Unified grasp perception framework covering both spatial (single-frame) and temporal (cross-frame tracking) domains.
- 93.3% success rate on 300+ unseen objects in bin clearing, with >900 mean picks per hour on a single-arm system.
- Dynamic grasping capability (catching a moving robot fish) via temporal grasp tracking.
- Widely adopted as upstream perception module; the AnyGrasp SDK and GSNet have been integrated into numerous downstream manipulation systems.

**Quantitative results:**

| Metric | Value |
|---|---|
| Bin clearing success rate | 93.3% (300+ unseen objects) |
| Mean picks per hour | >900 (single arm) |
| Dynamic grasping | Demonstrated (catching swimming robot fish) |
| Grasp pose representation | 7-DoF (position + orientation + width) |
| Input | Single-view point cloud (from RGB-D camera) |

**Limitations/Gaps:**
- Parallel-jaw gripper only; no multi-finger dexterous grasp generation.
- Proprietary SDK with license registration required; not fully open-source (compiled library + license).
- Generates grasp poses without execution policy; requires separate motion planning and control stack.
- Point cloud-based detection depends on depth camera quality; struggles with transparent/reflective objects.
- No language conditioning or semantic grasp selection.

**Code availability:** AnyGrasp SDK available at [GitHub](https://github.com/graspnet/anygrasp_sdk) with license registration (proprietary, compiled library). The underlying GSNet architecture has third-party open implementations.

**Relevance to dexterous manipulation:** While AnyGrasp itself detects parallel-jaw grasps, its point cloud processing pipeline and grasp quality estimation approach have influenced dexterous grasping methods. The GraspNet-1Billion dataset it was trained on has been extended with multi-finger grasp annotations in subsequent works. AnyGrasp's real-time detection speed (>900 picks/hour) sets a practical baseline that dexterous grasp planners must approach for deployment.

## Inference / Deployment

- **Inference latency:** Real-time grasp detection at >900 mean picks per hour on a single-arm system, implying grasp detection runs at well above real-time rates. Specific per-frame inference latency not explicitly reported but fast enough for continuous grasp tracking.
- **Deployment hardware:** Single-arm robot with parallel-jaw gripper + RGB-D camera (consumer-grade). Point cloud processing runs on a desktop GPU. The AnyGrasp SDK provides the inference pipeline.
- **Real-time capable?** Yes. >900 picks/hour demonstrated on real hardware. Dynamic grasping (catching a moving object) further confirms real-time capability.
