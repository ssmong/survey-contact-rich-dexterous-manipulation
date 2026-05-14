# 11.7 Ability Hand

- **Full title:** Ability Hand
- **Manufacturer:** PSYONIC Inc. (Champaign, IL, USA)
- **Year:** Commercially available (FDA 510(k) cleared; first commercial prosthetic with touch feedback)
- **DoF:** 6 actuated (5 independent finger flexion/extension + wrist rotation in prosthetic version; robotics version may differ)
- **Cost:** Commercial pricing (not publicly disclosed; prosthetic versions covered by insurance/VA in the US)
- **Tactile sensing:** Integrated touch sensors in each fingertip (pressure-sensitive; provides sensory feedback in prosthetic application)
- **Actuation:** High-speed DC motors; advertised as fastest prosthetic hand on the market
- **Certification:** FDA 510(k) cleared for prosthetic use

## Quantitative specs

| Spec | Value |
|------|-------|
| Finger closing speed | <500 ms full close (among fastest commercially available) |
| Grip force | Sufficient for daily living tasks (specific N not publicly listed) |
| Weight | ~450g (hand only, prosthetic version) |
| Fingers | 5 independently actuated fingers |
| Touch sensors | Pressure sensors in all 5 fingertips |
| Waterproofing | IP rating for daily use (prosthetic version) |
| Control interface | sEMG (prosthetic); serial/API (research) |

## Key methodology/design

The Ability Hand is a commercially manufactured dexterous hand originally designed as a prosthetic device. It features 6 DoF (5 independent finger actuations + wrist rotation), integrated fingertip touch sensors, and high-speed actuation. Unlike the research-oriented open-source hands in this section (LEAP, ORCA, ISyHand, RUKA, FAIVE), the Ability Hand is a mass-produced commercial product with FDA clearance and professional build quality. For robotics research, it provides a robust, sensor-equipped platform that does not require assembly or calibration.

## Usage in surveyed works

The Ability Hand appears in this survey through:
- **UniDex-VLA** (§2): one of 8 hands supported via the FAAS (Fingertip Action-Agnostic Space) framework, alongside Allegro, LEAP, Shadow, Inspire, Wuji, Oymotion, and XHand
- **Dex1B** (§8): included as one of the embodiments in the 1B-demo grasp dataset

## Main contributions (as a research platform)

- Only commercially manufactured, FDA-cleared hand used in recent dexterous manipulation research
- Integrated fingertip touch sensors providing tactile feedback without aftermarket modification
- Professional build quality and reliability exceeding 3D-printed or lab-assembled alternatives
- Proven compatibility with VLA frameworks (UniDex-VLA FAAS)
- High actuation speed enabling dynamic manipulation tasks

## Limitations/Gaps

- Commercial pricing makes it significantly more expensive than open-source alternatives (LEAP ~$3K, FAIVE ~$500-800)
- Closed-source hardware: no CAD files, firmware, or design modifications possible
- 6 DoF is substantially lower than LEAP (16), ORCA (17), or ISyHand (18), limiting fine dexterity
- Originally designed for prosthetics, not robotics: control interface and form factor may not be optimized for research use
- Limited sim model availability: no official URDF/MJCF models for standard simulators, making sim-to-real pipelines harder to establish
- Touch sensor data format and API may not be standardized for robotics research workflows

## Open-source status

Closed-source commercial product. Available for purchase from [psyonic.io](https://www.psyonic.io/ability-hand). No open-source design files.
