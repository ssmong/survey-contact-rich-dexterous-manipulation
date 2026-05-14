# 10.4 DOGlove

- **Full title:** DOGlove: Dexterous Manipulation with a Low-Cost Open-Source Haptic Force Feedback Glove
- **Authors:** Han Zhang, Hanwen Zhao, Yixuan Wang, and collaborators (TEA Lab)
- **Venue/Year:** RSS 2025 (arXiv 2505.14635, May 2025)
- **Input modality:** Custom haptic glove with joint angle sensors + force feedback actuators
- **Target hand:** Any dexterous hand (demonstrated with multiple platforms)
- **Force feedback:** 5-DoF haptic feedback (one per finger)
- **Cost:** <$600

## Key methodology/design

DOGlove is a custom-designed haptic glove that provides both motion capture and force feedback for dexterous teleoperation. The glove measures finger joint angles through embedded sensors and renders contact forces back to the operator's fingers through small actuators (one per finger, 5-DoF total). The design prioritizes low cost and open-source reproducibility, using off-the-shelf components and 3D-printed structural parts. The bidirectional force feedback enables operators to feel grasp contacts, significantly improving teleoperation quality for contact-rich tasks.

## Main contributions

- Sub-$600 dexterous teleoperation glove with bidirectional haptic feedback -- the lowest-cost force-feedback solution surveyed
- 5-DoF haptic rendering (one per fingertip) enabling operators to feel contact forces during manipulation
- Fully open-source hardware design (3D-printable) and software stack
- Demonstrated improved manipulation quality compared to no-feedback teleoperation

## Limitations/Gaps

- 5-DoF haptic feedback provides only per-finger force, not spatially distributed fingertip contact patterns
- Force rendering fidelity is limited by actuator bandwidth and power
- Requires per-user calibration for accurate kinematic mapping
- Glove form factor may restrict natural hand motion range

## Data quality impact

DOGlove is the only sub-$1K system that embeds force information into collected demonstrations. The 5-DoF haptic feedback allows operators to modulate grasp force during data collection, producing demonstrations that encode force-aware behaviors absent from camera-only or position-only systems. However, the per-finger force granularity is coarse: each finger receives a single scalar force signal rather than spatially distributed contact pressure, so operators cannot distinguish contact location or pressure distribution within a fingertip. Policies trained on DOGlove data show improved force regulation compared to force-blind demonstrations, but still lack the fine contact awareness needed for tasks requiring precise fingertip pressure control (e.g., controlled sliding, texture-dependent grasping).

## Open-source status

Fully open-source (hardware + software). GitHub: [TEA-Lab/DOGlove](https://github.com/TEA-Lab/DOGlove)
