# 10.1 DexCap

- **Full title:** DexCap: Scalable and Portable Mocap Data Collection System for Dexterous Manipulation
- **Authors:** Chen Wang, Haochen Shi, Weizhuo Wang, Ruohan Zhang, Li Fei-Fei, C. Karen Liu (Stanford)
- **Venue/Year:** RSS 2024 (arXiv 2403.07788, March 2024)
- **Input modality:** SLAM-based hand tracking + electromagnetic finger sensors (StretchSense gloves)
- **Target hand:** LEAP Hand (16 DoF)
- **Force feedback:** None
- **Cost:** ~$2,000 (gloves + sensors)

## Key methodology/design

DexCap captures human hand motion using electromagnetic tracking sensors attached to each finger, combined with SLAM-based wrist tracking for global positioning. The system retargets captured human hand motions to the LEAP Hand using an optimization-based retargeting pipeline that maps human finger kinematics to the robot hand's joint space. The portable design -- requiring no external motion capture infrastructure -- enables data collection in diverse real-world environments rather than being confined to a lab.

## Main contributions

- Portable, infrastructure-free dexterous motion capture system requiring only worn sensors (no external cameras or markers)
- Optimization-based retargeting pipeline mapping human hand motions to LEAP Hand with kinematic feasibility constraints
- Demonstrated scalable data collection for imitation learning of dexterous manipulation policies

## Limitations/Gaps

- No force/haptic feedback to the operator, which limits contact-rich task performance (operator cannot feel grasp forces)
- Electromagnetic sensors can suffer from interference in metallic environments
- Retargeting introduces motion artifacts when human and robot hand kinematics diverge significantly
- Demonstrated primarily on LEAP Hand; adaptation to other hand platforms requires re-calibration

## Data quality impact

Demonstrations capture finger joint trajectories but lack any force or contact information. Policies trained on DexCap data learn position-based grasp strategies without force regulation, resulting in brittle grasps that either apply excessive force (crushing) or insufficient force (dropping) when transferred to real hardware. The absence of force feedback also means the operator cannot modulate grasp force during collection, so demonstrations do not encode the force profiles needed for contact-rich tasks like insertion or in-hand reorientation under load.

## Open-source status

Open-source. GitHub: [j96w/DexCap](https://github.com/j96w/DexCap)
