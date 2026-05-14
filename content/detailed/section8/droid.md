# 8.4.2 DROID

- **Full title:** DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset
- **Authors:** Alexander Khazatsky, Karl Pertsch, Suraj Nair, Ashwin Balakrishna, Sudeep Dasari, and 95+ contributors; senior advisors Sergey Levine (UC Berkeley) and Chelsea Finn (Stanford)
- **Venue/Year:** arXiv 2024 (submitted March 2024; revised April 2025)
- **Scale:** 76,000 demonstration trajectories, 350 hours of interaction data, 564 distinct scenes, 84 tasks, 50 data collectors across 12 months
- **Geographic diversity:** Collectors across North America, Asia, and Europe
- **Robot:** Franka Emika Panda with parallel-jaw gripper (standardized hardware setup)
- **Data format:** Includes stereo RGB, wrist camera, proprioception, end-effector poses, language annotations
- **Collection method:** Distributed in-the-wild teleoperation across diverse real-world environments with standardized hardware

## Key methodology/design

DROID addresses a critical bottleneck in robot learning: existing datasets are collected in a small number of controlled lab environments, limiting policy generalization to new scenes. DROID tackles this by distributing data collection across 50 operators in diverse real-world settings (homes, offices, kitchens, labs) using a standardized Franka Panda hardware setup. The emphasis is on scene and environment diversity rather than task diversity. Each trajectory includes multi-view stereo RGB, wrist camera, full proprioception, and natural language task descriptions. The authors provide the full dataset, policy learning code, and a detailed hardware reproduction guide.

## Main contributions

- Largest single-embodiment "in-the-wild" manipulation dataset with 564 distinct real-world scenes
- Demonstrated that scene diversity is as important as scale: policies trained on DROID generalize significantly better to unseen environments
- Standardized, reproducible hardware setup enabling distributed data collection at scale
- Comprehensive data modalities (stereo RGB, wrist cam, proprioception, language) in a consistent format

## Downstream usage in surveyed works

DROID is used as pretraining or co-training data by several systems in this survey:
- **pi0** (§6): incorporates DROID in pretraining mixture
- **GR00T N1** (§6): uses DROID as part of cross-embodiment pretraining
- **OpenVLA** (§6): DROID included in fine-tuning experiments

## Limitations/Gaps

- Single embodiment (Franka Panda with parallel-jaw gripper): no dexterous hand data, limiting direct applicability to multi-finger manipulation
- No force/torque or tactile sensing data despite the Franka Panda having built-in joint torque sensors and a wrist F/T sensor that require no additional hardware to record — a notable missed opportunity for contact-rich research
- 84 tasks is relatively limited compared to OXE's 527 skills; emphasis is on scene diversity over task diversity
- Franka-specific: policies pretrained on DROID require embodiment adaptation for non-Franka robots
- Collection across 50 operators introduces variability in demonstration quality and style
- Hardware cost (~$30K+ for Franka setup) limits reproduction to well-funded labs

## Availability

Open-source under CC BY 4.0. Full dataset, policy code, and hardware guide available at [droid-dataset.github.io](https://droid-dataset.github.io/).
