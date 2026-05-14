# Section 11: Low-Cost Dexterous Hand Hardware

The availability of affordable, research-grade dexterous hands is a prerequisite for scaling dexterous manipulation research. This section covers hands designed for under ~$3,000 that target the research community with open-source designs, sim-to-real compatibility, and practical robustness.

## Entries

| Entry | DoF | Cost | Tactile | Actuation | Key Distinction |
|-------|-----|------|---------|-----------|-----------------|
| [LEAP Hand V2](leap_hand_v2.md) | 16 + articulated palm | ~$3,000 | None built-in | Dynamixel servos | Most widely adopted; proven sim-to-real |
| [ORCA Hand](orca_hand.md) | 17 | <$2,000 | Integrated | Not specified | Only sub-$2K hand with built-in tactile |
| [ISyHand](isyhand.md) | 18 (12+6) | ~$1,300 | None | Tendon-driven, compliant joints | Intrinsic mechanical compliance |
| [RUKA Hand](ruka_hand.md) | 15 | <$1,300 | None | Not specified | Lowest complexity, easiest assembly |
| [FAIVE Hand](faive_hand.md) | 11+ | ~$500-800 | None | Tendon-driven (servo motors) | Ultra-low-cost, fully 3D-printed |
| [Ability Hand](ability_hand.md) | 6 | Commercial | Fingertip pressure | DC motors | FDA-cleared, mass-produced, used in UniDex-VLA |
| [XHand / Inspire Hand](xhand_inspire.md) | 12-16 | ~$1-3K | None standard | DC motors + gears | Most-used commercial dex hands in recent research |
| [Digit 360](digit360.md) | N/A (sensor) | Not disclosed | 18+ modalities | N/A | Modular tactile fingertip for any hand |

## Observations

The low-cost dexterous hand landscape reveals a clear cost-capability frontier: LEAP Hand V2 ($3K, 16 DoF, widely adopted) anchors the high end, while ISyHand ($1.3K, 18 DoF, compliant) and RUKA ($1.3K, 15 DoF, simple) push costs below $1,500. The most notable gap is tactile sensing: among complete hands, only ORCA Hand includes integrated tactile sensors. LEAP, ISyHand, and RUKA all require aftermarket tactile integration (e.g., mounting DIGIT or GelSight sensors), which adds cost, complexity, and often changes the fingertip geometry. Digit 360 from Meta could bridge this gap as a modular tactile fingertip, but it is not yet publicly available. The disconnect between hands and sensing is consequential for contact-rich manipulation: the hands most widely used for dexterous RL (LEAP Hand, used by CrossDex, SeqDex, HandelBot, etc.) operate without any tactile feedback, meaning policies trained on these platforms cannot learn force-aware behaviors from physical interaction. ISyHand's intrinsic compliance offers a partial mechanical solution, but without sensing, the compliance is unobservable by the policy. A hand that combines LEAP-level community adoption, ORCA-level tactile integration, and ISyHand-level compliance at sub-$2K cost does not yet exist.
