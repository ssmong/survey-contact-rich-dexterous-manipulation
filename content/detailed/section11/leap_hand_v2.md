# 11.1 LEAP Hand V2

- **Full title:** LEAP Hand V2: Advanced Dexterous Robotic Hand
- **Authors:** Kenneth Shaw, Deepak Pathak (CMU)
- **Venue/Year:** 2024 (V1: RSS 2023)
- **DoF:** 16 actuated + articulated palm
- **Actuators:** Dynamixel servos
- **Cost:** ~$3,000
- **Weight:** Lightweight (mountable on standard robot arms)
- **Tactile sensing:** None built-in (aftermarket integration possible)
- **Sim model:** MuJoCo, Isaac Lab

## Quantitative specs

| Spec | Value |
|------|-------|
| Actuator control bandwidth | ~50 Hz effective control rate (Dynamixel servo limitation) |
| Maximum fingertip force | Not reported in available documentation |
| Durability | Thousands of grasp cycles demonstrated across multiple research groups (CrossDex, SeqDex, HandelBot, DexCap, ComFree-Sim) |

## Key methodology/design

LEAP Hand V2 builds on the original LEAP Hand (RSS 2023) with improved mechanical design, stronger actuators, and an articulated palm for enhanced grasp stability. The hand uses Dynamixel servo motors for all joints, providing position and current (torque proxy) feedback. The design emphasizes research accessibility: all structural parts are 3D-printable or use off-the-shelf components, and the bill of materials is fully documented. V2 adds an opposable palm joint that increases the grasp envelope and enables more human-like manipulation patterns.

## Main contributions

- Among the most widely adopted low-cost dexterous hands in the research community (used by CrossDex, SeqDex, HandelBot, DexCap, ComFree-Sim, and others)
- Articulated palm (V2) expanding grasp types beyond V1's fixed-palm design
- Proven sim-to-real pipeline with zero-shot transfer demonstrated across multiple independent research groups
- Robust mechanical design tolerating thousands of grasp cycles in research settings

## Limitations/Gaps

- No integrated tactile sensing; fingertip contact is position-controlled only
- Dynamixel servos have limited bandwidth (~50 Hz effective control rate) compared to custom actuators
- $3,000 cost, while low for a dexterous hand, is the highest in this section
- 16 DoF is fewer than the human hand (~20-25 functional DoF), limiting manipulation dexterity for some tasks

## Open-source status

Fully open-source (CAD, firmware, software). Project page: [v2-adv.leaphand.com](https://v2-adv.leaphand.com/)
