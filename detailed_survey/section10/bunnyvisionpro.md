# 10.2 BunnyVisionPro

- **Full title:** BunnyVisionPro: Real-Time Bimanual Dexterous Teleoperation for Imitation Learning
- **Authors:** Runyu Ding, Yuzhe Qin, Jiyue Zhu, Chengzhe Jia, Xiaolong Wang (HKU, UCSD)
- **Venue/Year:** arXiv 2407.03162, July 2024
- **Input modality:** Apple Vision Pro hand tracking (markerless, built-in cameras)
- **Target hand:** Bimanual dexterous setup (dual arms + dexterous hands)
- **Force feedback:** Low-cost haptic feedback module (optional)
- **Cost:** ~$3,500+ (Apple Vision Pro hardware cost)

## Key methodology/design

BunnyVisionPro repurposes the Apple Vision Pro's built-in hand tracking for real-time bimanual dexterous teleoperation. The system streams hand pose data from the Vision Pro headset to the robot controller over a local network, with real-time inverse kinematics mapping human hand poses to robot joint commands. An optional low-cost haptic feedback module provides basic contact feedback to the operator. The VR headset's high-quality hand tracking eliminates the need for gloves or external sensors.

## Main contributions

- Leverages consumer VR hardware (Apple Vision Pro) for research-grade bimanual dexterous teleoperation
- Real-time streaming pipeline with low-latency hand pose transfer over local network
- Optional haptic feedback integration for improved contact-rich task performance
- Demonstrated imitation learning from collected demonstrations

## Limitations/Gaps

- High hardware cost ($3,500 for Vision Pro alone) limits accessibility
- Hand tracking accuracy depends on lighting conditions and hand visibility to the headset cameras
- Haptic feedback is rudimentary compared to dedicated force feedback gloves
- Finger-level tracking resolution from Vision Pro may be insufficient for precise fine-motor tasks

## Data quality impact

The optional haptic module provides rudimentary binary contact feedback, but lacks force magnitude or direction information. Demonstrations collected without the haptic module are purely position-based, producing the same force-blind data quality issues as camera-only systems. Even with the haptic module enabled, the coarse contact signal does not allow operators to modulate grasp forces precisely, resulting in demonstrations that encode approximate finger trajectories without the force profiles needed for delicate manipulation tasks (e.g., handling fragile objects, controlled sliding).

## Open-source status

Open-source. GitHub: [Dingry/BunnyVisionPro](https://github.com/Dingry/BunnyVisionPro)
