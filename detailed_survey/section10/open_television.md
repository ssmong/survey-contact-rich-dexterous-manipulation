# 10.9 Open-TeleVision

- **Full title:** Open-TeleVision: Teleoperation with Immersive Active Visual Feedback
- **Authors:** Xuxin Cheng, Jialong Li, Shiqi Yang, Ge Yang, Xiaolong Wang (UCSD)
- **Venue/Year:** CoRL 2024 (arXiv 2407.10107, July 2024)
- **Input modality:** Stereo VR headset (operator sees through robot's eyes)
- **Target hand:** Bimanual dexterous setup
- **Force feedback:** None (visual feedback substitutes)
- **Cost:** VR headset cost (consumer-grade)

## Key methodology/design

Open-TeleVision provides immersive visual feedback by streaming stereo video from the robot's head-mounted cameras to the operator's VR headset, creating a first-person perspective. The operator sees what the robot sees in stereoscopic 3D, which provides depth perception that partially compensates for the lack of haptic feedback. Hand tracking from the VR headset controls the robot's bimanual dexterous hands through real-time retargeting.

## Main contributions

- Immersive stereoscopic visual feedback from the robot's perspective, improving operator spatial awareness and manipulation accuracy
- Active visual feedback (operator head motion controls robot camera orientation) for natural viewpoint control
- Demonstrated improved task completion rates compared to fixed-viewpoint teleoperation

## Limitations/Gaps

- No force or haptic feedback; relies entirely on visual cues for contact-rich tasks
- Stereo camera setup on the robot adds hardware complexity and cost
- VR headset latency and display quality affect operator comfort during extended sessions
- Hand tracking accuracy depends on the specific VR headset's capabilities

## Data quality impact

The immersive stereo visual feedback improves operator spatial awareness, which translates to better finger placement accuracy compared to fixed-viewpoint systems. Operators can judge depth and object proximity more naturally, reducing positioning errors in demonstrations. However, the system provides no force feedback, so demonstrations remain force-blind. Policies trained on Open-TeleVision data benefit from more spatially accurate demonstrations (better finger-object alignment) but still cannot learn force regulation. The visual feedback substitutes for haptic cues in some scenarios (operators visually detect object deformation or slippage), but this is unreliable for tasks where contact forces are not visually observable (e.g., tightening a screw, pressing a button to a specific activation force).

## Open-source status

Open-source. GitHub: [OpenTeleVision/TeleVision](https://github.com/OpenTeleVision/TeleVision)
