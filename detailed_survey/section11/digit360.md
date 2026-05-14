# 11.5 Digit 360

- **Full title:** Digit 360: A Multimodal Tactile Fingertip Sensor
- **Authors:** Meta FAIR
- **Venue/Year:** 2024
- **Type:** Tactile sensor (fingertip module), not a complete hand
- **Sensing modalities:** 18+ modalities including normal/shear force, vibration, temperature, proximity, and high-resolution tactile images
- **Cost:** Not publicly disclosed
- **Target integration:** Any dexterous hand platform (designed as a modular fingertip)

## Quantitative specs

| Spec | Value |
|------|-------|
| Sensing modalities | 18+ simultaneous (normal force, shear force, vibration, temperature, proximity, tactile images, and others) |
| Form factor | Fingertip-scale, designed for drop-in replacement on existing hands |
| Computational overhead | Significant -- 18+ modalities require parallel data processing |
| Availability | Not yet publicly available (planned open-source release as of survey date) |

## Key methodology/design

Digit 360 is not a hand but a multimodal tactile fingertip sensor designed to be integrated into dexterous hands. It extends Meta's DIGIT line of vision-based tactile sensors by dramatically expanding the sensing modalities from a single camera-based tactile image to 18+ simultaneous modalities including spatially distributed normal and shear forces, high-frequency vibration, temperature, and proximity sensing. The sensor uses a compact form factor designed to replace standard fingertips on existing dexterous hands.

## Main contributions

- Among the most comprehensive tactile fingertip sensors reported, with 18+ simultaneous sensing modalities
- Multimodal sensing (force, vibration, temperature, proximity) in a single fingertip-scale package
- Designed for integration with existing dexterous hand platforms as a modular upgrade
- Addresses the sensing gap in current low-cost hands (LEAP, RUKA, ISyHand all lack tactile)

## Limitations/Gaps

- Not a complete hand; requires integration into an existing hand platform
- Cost not disclosed; likely significantly more expensive than the hands themselves
- Not yet widely available to the research community (planned open-source release)
- Data processing for 18+ modalities simultaneously introduces computational overhead
- Integration with existing sim-to-real pipelines for tactile-equipped hands is not yet demonstrated

## Open-source status

Planned open-source release (as of survey date, not yet publicly available).
