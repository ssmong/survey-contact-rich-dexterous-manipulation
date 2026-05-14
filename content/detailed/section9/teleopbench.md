# 9.7 TeleOpBench

- **Full title:** TeleOpBench: A Simulator-Centric Benchmark for Dual-Arm Dexterous Teleoperation
- **Authors:** Hangyu Li, Qin Zhao, Haoran Xu, and collaborators
- **Venue/Year:** 2025 (arXiv 2505.12748)
- **Sim platform:** Isaac Sim
- **Dexterous support:** 3 humanoid embodiments with dual-arm dexterous hands
- **Teleoperation interfaces:** Camera-based (SMPLerX + MediaPipe) and VisionPro-based (Apple Vision Pro)
- **Tasks:** 30 dual-arm dexterous manipulation tasks
- **Evaluation:** 4 teleoperation modalities benchmarked

## Key methodology/design

TeleOpBench provides a standardized benchmark for evaluating teleoperation systems for dual-arm dexterous manipulation. It implements two motion capture pipelines: a camera-based pipeline using SMPLerX and MediaPipe for webcam-based human motion capture, and a VR-based pipeline using Apple Vision Pro. The benchmark includes real-time inverse kinematics processing, MeshCat-based 3D visualization, and motion data transmission. By standardizing the evaluation environment and metrics, it enables direct comparison of different teleoperation approaches.

## Main contributions

- First systematic benchmark for dual-arm dexterous teleoperation with 30 standardized tasks
- Support for multiple teleoperation modalities (camera-based and VR-based) with direct comparison
- Real-time inverse kinematics pipeline for mapping human hand motion to diverse robot embodiments
- Standardized metrics for teleoperation quality assessment

## Limitations/Gaps

- Benchmark is simulation-only; real robot execution is not included in the evaluation pipeline
- Limited to two teleoperation input modalities; glove-based and exoskeleton-based interfaces are not covered
- Force feedback evaluation is not included despite its relevance to contact-rich manipulation
- 3 humanoid embodiments may not cover the diversity of real-world dexterous platforms

## Coverage gaps

| Criterion | Covered? |
|-----------|----------|
| Force/torque evaluation metrics | No (teleoperation quality metrics do not include force regulation assessment) |
| Deformable object tasks | No |
| Tactile sensing | No |
| Multi-stage / long-horizon tasks | Partial (some tasks involve sequential steps, but no explicit long-horizon evaluation protocol) |
| Multi-hand coordination | Yes (dual-arm dexterous manipulation is the core focus) |

## Open-source status

Open-source (Python 98%, C++ 2%). GitHub: [cyjdlhy/TeleOpBench](https://github.com/cyjdlhy/TeleOpBench)
