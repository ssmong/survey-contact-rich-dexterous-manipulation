# 10.7 Open TeleDex

- **Full title:** Open TeleDex: Phone-Based Teleoperation for Dexterous Manipulation
- **Authors:** Omar Rayyan and collaborators
- **Venue/Year:** arXiv 2510.14771, October 2025
- **Input modality:** Smartphone-based hand tracking (phone camera + on-device ML)
- **Target hand:** Any arm + dexterous hand combination
- **Force feedback:** None
- **Cost:** Very low (uses existing smartphone)

## Key methodology/design

Open TeleDex leverages smartphone cameras and on-device machine learning models for hand pose estimation to enable dexterous teleoperation. The operator holds or positions their phone to capture their hand motions, which are processed on-device and streamed to the robot controller. By using hardware that most researchers already own, it eliminates all specialized input device costs. The system supports arbitrary arm + hand combinations through a modular retargeting layer.

## Main contributions

- Zero additional hardware cost (uses existing smartphone) for dexterous teleoperation
- On-device hand tracking eliminates the need for a dedicated workstation for pose estimation
- Modular support for diverse arm + hand combinations

## Limitations/Gaps

- Smartphone-based tracking has lower accuracy and higher latency than dedicated tracking systems
- Single-viewpoint camera limits tracking of occluded fingers
- No force feedback of any kind
- Phone must be positioned to maintain line-of-sight to the operator's hand, constraining workspace

## Data quality impact

Smartphone-based tracking introduces the highest positional noise and latency among the teleoperation systems in this section. Demonstrations are position-only with no force information, and the tracking quality is further degraded by the constrained phone viewpoint (single camera, potential occlusions). Policies trained on Open TeleDex data inherit both the force blindness common to all no-feedback systems and additional trajectory noise from the lower-fidelity tracking pipeline. This combination makes Open TeleDex data least suitable for precision contact-rich tasks, though it may be adequate for coarse grasping tasks where exact finger placement and force control are less critical.

## Open-source status

Open-source. GitHub: [omarrayyann/TeleDex](https://github.com/omarrayyann/TeleDex)
