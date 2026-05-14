# 11.2 ORCA Hand

- **Full title:** ORCA Hand: An Affordable and Dexterous Robotic Hand for Contact-Rich Manipulation
- **Authors:** ETH Zurich (Robotics Systems Lab)
- **Venue/Year:** 2025
- **DoF:** 17 actuated
- **Cost:** <$2,000
- **Tactile sensing:** Integrated tactile sensors
- **Sim-to-real:** Demonstrated with 1-hour training time
- **Sim model:** Available (compatible with standard simulators)

## Quantitative specs

| Spec | Value |
|------|-------|
| Actuator control bandwidth | Not reported in available documentation |
| Maximum fingertip force | Not reported in available documentation |
| Durability | Not reported in available documentation |

## Key methodology/design

The ORCA Hand is a 17-DoF dexterous hand designed specifically for contact-rich manipulation research. Its distinguishing feature is integrated tactile sensing -- built into the fingertips from the ground up rather than as an aftermarket addition. The hand's mechanical design emphasizes robust contact interactions, with compliant fingertip structures that improve grasp stability on diverse objects. The accompanying sim-to-real pipeline demonstrates that RL policies can be trained and transferred in approximately 1 hour of total training time.

## Main contributions

- Integrated tactile sensing from design stage -- the only sub-$2K dexterous hand with built-in tactile in this survey
- 17 DoF providing slightly higher dexterity than 16-DoF alternatives (LEAP Hand)
- Rapid sim-to-real transfer pipeline (1-hour training) demonstrating practical deployability
- Fully open-source hardware design enabling community reproduction

## Limitations/Gaps

- Newer design with less community adoption and validation compared to LEAP Hand
- Tactile sensor specifications (resolution, modality) not fully characterized in available documentation
- <$2K cost is an estimate; actual build cost depends on local sourcing of components

## Open-source status

Fully open-source (hardware + software). Project page: [orcahand.com](https://www.orcahand.com/)
