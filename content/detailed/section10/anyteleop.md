# 10.3 AnyTeleop

- **Full title:** AnyTeleop: A General Vision-Based Dexterous Robot Hand-Arm Teleoperation System
- **Authors:** Yuzhe Qin, Wei Yang, Binghao Huang, Karl Van Wyk, Hao Su, Xiaolong Wang, Dieter Fox (UCSD, NVIDIA)
- **Venue/Year:** RSS 2023
- **Input modality:** Single RGB camera (vision-based hand pose estimation)
- **Target hand:** Multiple dexterous hands (Allegro, Shadow, and others via modular retargeting)
- **Force feedback:** None
- **Cost:** Very low (requires only a webcam)

## Key methodology/design

AnyTeleop uses vision-based hand pose estimation from a single RGB camera to drive dexterous robot hands. The system decouples hand pose estimation from robot-specific retargeting, using a modular retargeting module that maps detected human hand poses to any supported robot hand. This design enables teleoperation across diverse hand platforms without hardware-specific sensors or gloves. The vision-only approach minimizes setup cost and complexity.

## Main contributions

- Camera-only teleoperation requiring no wearable sensors, gloves, or VR hardware
- Modular retargeting architecture supporting multiple robot hand platforms from a single input pipeline
- Lowest-cost entry point for dexterous teleoperation (webcam only)

## Limitations/Gaps

- Vision-based hand tracking is less accurate than sensor-based approaches, especially for occluded or fast-moving fingers
- No force feedback, making contact-rich tasks difficult for operators
- Single-camera setup limits depth perception and can introduce tracking jitter
- Latency from vision processing pipeline may affect real-time control quality

## Data quality impact

Demonstrations lack force information and have lower positional accuracy than sensor-based systems, producing policies with poor force regulation. The single-camera tracking introduces jitter and occasional tracking loss during fast finger motions or occlusions, which manifests as noise in the demonstration trajectories. Policies trained on this data inherit both the force blindness and the positional noise, leading to imprecise finger placement and no learned contact force modulation. For tasks requiring controlled contact (e.g., insertion, pivoting, surface following), AnyTeleop demonstrations are insufficient to learn the necessary force-position coordination.

## Open-source status

Project page available. Code partially released.
