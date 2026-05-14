# 10.8 OmniH2O

- **Full title:** OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning
- **Authors:** Tairan He, Zhengyi Luo, Xialin He, Wenli Xiao, Chong Zhang, Weinan Zhang, Kris Kitani, Changliu Liu, Guanya Shi (CMU LeCAR Lab)
- **Venue/Year:** CoRL 2024 (arXiv 2406.08858, June 2024)
- **Input modality:** Multi-modal -- VR controllers, voice commands, or RGB camera
- **Target hand:** Humanoid whole-body (including hands)
- **Force feedback:** None
- **Cost:** Varies by input modality (RGB camera is free; VR setup requires headset)

## Key methodology/design

OmniH2O provides a universal teleoperation framework for humanoid robots that accepts multiple input modalities -- VR controllers, voice commands, or plain RGB video -- and maps them to whole-body humanoid control including dexterous hand motions. The system uses a learned motion retargeting policy trained in simulation that generalizes across input modalities. This multi-modal approach allows operators to choose the most convenient input method for their setup and task.

## Main contributions

- Multi-modal input support (VR/voice/RGB) for humanoid teleoperation, enabling flexibility in deployment scenarios
- Learned retargeting policy that generalizes across input modalities without per-modality engineering
- Whole-body control including locomotion and dexterous manipulation in a unified framework

## Limitations/Gaps

- Dexterous hand control fidelity is lower than dedicated hand-only teleoperation systems
- No force/haptic feedback in any input modality
- Whole-body focus means hand manipulation quality may be compromised relative to hand-only systems
- RGB-only input mode has the lowest accuracy but broadest accessibility

## Data quality impact

The whole-body teleoperation focus means hand manipulation demonstrations are lower-fidelity than those from dedicated hand-only systems. The learned retargeting policy introduces a layer of abstraction between operator intent and robot motion that smooths out fine finger motions. Demonstrations collected via the RGB-only modality have the lowest hand control fidelity (comparable to AnyTeleop), while VR controller input provides better wrist-level control but limited independent finger articulation. No input modality provides force feedback, so all collected demonstrations lack force information. Policies trained on OmniH2O data are best suited for whole-body tasks where coarse hand control suffices (e.g., bimanual object transport) rather than precision dexterous manipulation.

## Open-source status

Open-source. GitHub: [LeCAR-Lab/human2humanoid](https://github.com/LeCAR-Lab/human2humanoid)
