# 10.10 HATO

- **Full title:** Learning Visuotactile Skills with Two Multifingered Hands
- **Authors:** Toru Lin, Yu Zhang, Qiyang Li, Haozhi Qi, Brent Yi, Sergey Levine, Jitendra Malik (UC Berkeley)
- **Venue/Year:** ICRA 2024 (arXiv 2404.16823, April 2024)
- **arXiv:** https://arxiv.org/abs/2404.16823
- **Input modality:** Meta Quest 2 VR controllers (arm pose tracking) + grip button/thumbstick (finger control)
- **Target hand:** 2x Psyonic Ability Hand (6 DoF each, repurposed prosthetic hands with built-in touch sensors)
- **Force feedback:** None to operator (but touch sensors on the robot hands provide tactile input to the learned policy)
- **Cost:** Low-cost (off-the-shelf VR hardware + prosthetic hands)

## Key methodology/design

HATO is a bimanual dexterous teleoperation system built from off-the-shelf VR electronics (Meta Quest 2) and repurposed prosthetic hands (Psyonic Ability Hand) equipped with fingertip touch sensors. The system uses two UR5e arms with one Ability Hand each. Arm control maps VR controller pose to end-effector position via IK. Finger control uses the grip button for non-thumb flexion (4 DoF) and thumbstick for thumb flexion/abduction (2 DoF per hand). The system collects visuotactile demonstrations at 10 Hz, capturing RGB-D images (3 cameras: 2 wrist-mounted + 1 head-view), proprioception, and touch sensor readings.

Policies are learned using Denoising Diffusion Probabilistic Models (DDPM) following the diffusion policy framework. A single observation predicts 16-step action sequences. Each modality is encoded separately: ResNet-18 for RGB-D (with GroupNorm), two-layer MLPs for proprioception and touch signals. All encoded features are concatenated as input to the diffusion model, which outputs 24-dimensional actions (6 DoF per arm + 6 DoF per hand). Inference uses temporal ensemble for motion smoothing.

## Main contributions

- Low-cost bimanual dexterous teleoperation system using off-the-shelf VR hardware and prosthetic hands (~$600/hand vs. $10K+ for research hands)
- Among the first demonstrations of visuotactile policy learning on bimanual multifingered hands, with systematic ablation of sensing modalities
- Shows that touch sensing is critical for contact-rich bimanual tasks (removing touch drops Steak Serving from 5/10 to 0/10)
- Dataset saturation analysis: 75-200 demonstrations sufficient for effective learning across tasks

## Limitations/Gaps

- Prosthetic Ability Hand has only 6 DoF per hand (underactuated), significantly less dexterous than Shadow (24) or Allegro (16)
- VR controller-based finger mapping is coarse: grip button controls 4 fingers simultaneously, limiting independent finger control
- No force/haptic feedback to the operator during teleoperation, which limits contact-rich task quality
- Touch sensors provide binary/low-resolution contact signals (6 per fingertip), not high-resolution tactile like DIGIT or GelSight
- Evaluated on 4 tasks only; no in-hand manipulation or fine assembly tasks

## Data quality impact

The built-in touch sensors on the Ability Hand provide fingertip contact information that is recorded during teleoperation and used as input to learned policies. However, the operator receives no haptic feedback, so force modulation during data collection relies entirely on visual cues. The touch signals are low-resolution compared to vision-based tactile sensors (DIGIT, GelSight), providing coarse contact/no-contact information rather than spatially resolved pressure maps. Despite these limitations, ablations show that including touch data meaningfully improves policy success on contact-sensitive tasks.

## Quantitative results

| Task | Success (full) | Pickup | Demos used |
|---|---|---|---|
| Slippery Handover | 10/10 | 10/10 | 75 |
| Tower Block Stacking | 10/10 | 10/10 | 75 |
| Wine Pouring | 9/10 | 10/10 | 100 |
| Steak Serving | 5/10 | 10/10 | 200 |

**Ablation results (Steak Serving):**
- Full model (vision + touch + proprio): 5/10
- Without touch: 0/10
- Without vision: 0/10
- Without wrist cameras: 2/10
- Depth does not markedly improve learning

## Open-source status

Open-source (hardware + software + dataset). Project page: https://toruowo.github.io/hato/
