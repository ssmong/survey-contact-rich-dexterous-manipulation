# 11.3 ISyHand

- **Full title:** ISyHand: An Intrinsically Soft Dexterous Hand for Contact-Rich Manipulation
- **Authors:** MPI for Intelligent Systems (MPI-IS), Tubingen
- **Venue/Year:** 2025
- **DoF:** 18 (12 finger DoF + 6 palm/wrist DoF)
- **Cost:** ~$1,300
- **Tactile sensing:** None built-in
- **Actuation:** Tendon-driven with intrinsically soft (compliant) joints

## Quantitative specs

| Spec | Value |
|------|-------|
| Actuator control bandwidth | Not reported in available documentation |
| Maximum fingertip force | Not reported in available documentation (compliant joints may limit maximum force compared to rigid-joint designs) |
| Durability | Not reported in available documentation (tendon wear is a potential maintenance concern) |

## Key methodology/design

ISyHand takes a fundamentally different mechanical approach from rigid-joint hands like LEAP: it uses intrinsically soft (compliant) joints and tendon-driven actuation. The compliance is built into the joint mechanics rather than being achieved through control. This means the hand passively adapts to object geometries during grasping -- a physical form of impedance that does not require explicit force control. The 18-DoF design (12 finger + 6 palm/wrist) provides high dexterity, and the tendon-driven actuation allows the motors to be placed in the forearm, reducing fingertip weight and inertia.

## Main contributions

- Intrinsic mechanical compliance providing passive force regulation without explicit impedance control
- Highest DoF count (18) among sub-$2K hands in this survey
- Lowest cost ($1,300) with the highest DoF, offering strong dexterity-per-dollar
- Tendon-driven actuation enabling lightweight fingertips with low inertia

## Limitations/Gaps

- No tactile sensing; the compliant joints provide implicit contact adaptation but no explicit contact measurement
- Tendon-driven actuation introduces cable routing complexity and potential maintenance issues (tendon wear, slack)
- Sim-to-real transfer is more challenging for soft/compliant hands due to difficulty modeling tendon dynamics and joint compliance accurately
- Compliant joints may limit maximum fingertip force compared to rigid-joint designs

## Open-source status

Project page: [isyhand.is.mpg.de](https://isyhand.is.mpg.de/). Design files available.
