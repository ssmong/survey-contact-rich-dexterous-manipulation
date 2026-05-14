# 10.11 DexPilot

- **Full title:** DexPilot: Vision Based Teleoperation of Dexterous Robotic Hand-Arm System
- **Authors:** Ankur Handa, Karl Van Wyk, Wei Yang, Jacky Liang, Yu-Wei Chao, Qian Wan, Stan Birchfield, Nathan Ratliff, Dieter Fox (NVIDIA)
- **Venue/Year:** ICRA 2020 (arXiv 1910.03135, October 2019)
- **arXiv:** https://arxiv.org/abs/1910.03135
- **Input modality:** Vision-based (RGB camera observing bare human hand, no gloves or markers)
- **Target hand:** Allegro Hand (16 DoF) + Kuka IIWA arm (7 DoF), 23 DoA total
- **Force feedback:** None
- **Cost:** Low (single RGB camera)

## Key methodology/design

DexPilot enables teleoperation of a dexterous robotic hand-arm system by observing the operator's bare hand with a single RGB camera. The system detects hand keypoints (fingertips, knuckles, wrist) using a vision-based hand pose estimator, then solves an optimization problem to retarget the detected human hand pose to the robot hand's joint space. The retargeting formulation minimizes the discrepancy between human and robot fingertip positions while respecting joint limits and kinematic constraints of the Allegro Hand. Arm motion is controlled separately by mapping wrist pose to the Kuka IIWA end-effector via IK.

The key innovation is the marker-free, glove-free design: operators simply move their bare hand in front of a camera. This eliminates the need for specialized teleoperation hardware (VR controllers, haptic gloves, electromagnetic trackers) and reduces cost and setup time. The system supports the full 23 DoA of the hand-arm system, enabling complex manipulation beyond simple pick-and-place.

## Main contributions

- First vision-based (bare-hand, no markers/gloves) teleoperation system for a full dexterous hand-arm system with 23 DoA
- Optimization-based retargeting mapping human hand keypoints to Allegro Hand joint space with kinematic feasibility constraints
- Demonstrated complex manipulation tasks (beyond pick-and-place) using only a single RGB camera as input
- Demonstrated that vision-based hand tracking is sufficient for dexterous teleoperation, reducing hardware cost compared to glove/exoskeleton systems

## Limitations/Gaps

- No force/haptic feedback to the operator; manipulation relies entirely on visual feedback
- Vision-based hand tracking is sensitive to occlusion (fingers occluding each other) and lighting conditions
- Single-camera setup provides limited depth information, potentially causing retargeting ambiguities
- Latency from vision processing pipeline may limit high-frequency contact-rich tasks
- Evaluated on Allegro Hand + Kuka IIWA only; no cross-platform validation
- No policy learning component; pure teleoperation system (data collected could be used for downstream IL, but not demonstrated in the paper)

## Data quality impact

DexPilot collects position-only demonstrations with no force or tactile information. The vision-based hand tracking introduces noise and occasional tracking failures (especially during occlusion), which degrades demonstration quality compared to glove-based or exoskeleton-based systems. However, the low cost and ease of setup enable collecting larger datasets, potentially compensating for per-demonstration quality through volume. The system demonstrated that high-dimensional dexterous demonstrations can be collected without specialized hardware.

## Quantitative results

The paper evaluates speed and reliability metrics across two human demonstrators on multiple manipulation tasks. Tasks include grasping various objects, in-hand repositioning, and tool manipulation. Specific success rate numbers are reported across task categories but vary by demonstrator skill level.

| Metric | Value |
|---|---|
| Total DoA controlled | 23 (16 hand + 7 arm) |
| Input hardware | Single RGB camera |
| Hand tracking | Vision-based keypoint detection |
| Retargeting | Optimization-based |

## Open-source status

Not open-source. Project page with videos: https://sites.google.com/view/dex-pilot
