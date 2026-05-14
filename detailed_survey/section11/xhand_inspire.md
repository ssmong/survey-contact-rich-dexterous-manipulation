# 11.8 XHand / Inspire Hand

- **Full title:** XHand (also marketed as X-Hand) and Inspire Hand (also known as Inspire-Robots Dexterous Hand)
- **Manufacturer:** Chinese robotics manufacturers (Inspire-Robots for Inspire Hand; various manufacturers for XHand variants)
- **Year:** Available from ~2023 onward; increasingly adopted in research from 2024-2025
- **DoF:** Inspire Hand: ~12 actuated (5 fingers, independent flexion/extension + some abduction/adduction); XHand: ~12-16 DoF (varies by version)
- **Cost:** Significantly lower than Western-manufactured alternatives (estimated $1,000-3,000 range; specific pricing varies by supplier and configuration)
- **Tactile sensing:** None standard (some versions support optional tactile modules)
- **Actuation:** DC motors with gear reduction; position-controlled

## Quantitative specs

| Spec | Value |
|------|-------|
| Fingers | 5 (anthropomorphic layout) |
| Actuated DoF (Inspire) | ~12 (independent finger flexion + thumb opposition) |
| Actuated DoF (XHand) | ~12-16 (version-dependent) |
| Weight | ~500-800g (varies by version) |
| Grip force | Moderate (sufficient for typical manipulation tasks) |
| Control interface | Serial/CAN bus; ROS driver available for some versions |
| Sim model | MuJoCo, IsaacGym (community-contributed URDFs) |

## Key methodology/design

The XHand and Inspire Hand are Chinese-manufactured dexterous hands that have gained significant traction in the robotics research community due to their combination of reasonable cost, adequate DoF, and commercial availability. Unlike the open-source research hands (LEAP, ORCA, ISyHand, RUKA, FAIVE), these are commercially produced products with professional-grade construction. They fill a practical niche: more affordable than Shadow Hand (~$100K+) or Allegro Hand (~$15K+), commercially available without assembly, and with enough DoF (12-16) for meaningful dexterous manipulation research. The Inspire Hand and XHand are sometimes used interchangeably in the literature, though they come from different manufacturers and have distinct specifications.

## Usage in surveyed works

These hands appear frequently across the survey, despite having no dedicated hardware entry until now:
- **DexMachina** (§1): Inspire Hand and XHand both used as target embodiments for bimanual manipulation
- **ManipTrans** (§1): Inspire Hand and XHand among 6 supported hands for cross-embodiment motion transfer
- **DexUMI** (§1): XHand and Inspire Hand used for real-world dexterous manipulation (CoRL 2025 Best Paper Finalist)
- **UniDex-VLA** (§2): both Inspire and XHand included in the 8-hand FAAS framework
- **iDP3** (§6): Inspire Hand (25 DoF configuration) on Fourier GR1 humanoid
- **Dex1B** (§8): Inspire Hand included in the 1B-demo dataset

## Main contributions (as research platforms)

- Among the most frequently adopted commercially available dexterous hands in recent research, particularly in the Chinese robotics community
- Cost-effective alternative to Shadow/Allegro for labs needing multi-finger manipulation hardware
- Proven cross-embodiment compatibility: successfully integrated into retargeting frameworks (ManipTrans, UniDex-VLA FAAS) alongside Shadow, Allegro, and LEAP
- Commercial availability eliminates assembly time and calibration effort
- Growing ecosystem of community-contributed URDF/MJCF models for simulation

## Limitations/Gaps

- Specifications inconsistently reported across papers: DoF counts vary (12 to 25 reported for "Inspire Hand" depending on how passive joints are counted), making direct comparison difficult
- No standardized sim model: URDF/MJCF files are community-contributed and may not match actual hardware precisely
- Closed-source hardware: no CAD files or firmware modification possible
- No integrated tactile sensing in standard configurations
- Documentation and support primarily in Chinese; English documentation may be limited
- Multiple manufacturers and versions create confusion: "XHand" and "Inspire Hand" are sometimes conflated despite being different products
- Build quality and consistency may vary between production batches and suppliers
- Limited independent benchmarking of actuator specs (bandwidth, force, repeatability)

## Open-source status

Closed-source commercial products. Inspire Hand available from [inspire-robots.com](https://www.inspire-robots.com/). XHand available from various Chinese robotics suppliers. Community-contributed URDF models available in some research repositories (ManipTrans, DexMachina).
