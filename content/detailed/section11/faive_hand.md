# 11.6 FAIVE Hand

- **Full title:** FAIVE Hand: A Low-Cost, 3D-Printed, Tendon-Driven Dexterous Robot Hand
- **Authors:** ETH Zurich, Soft Robotics Lab (SRL)
- **Venue/Year:** 2024 (open-source hardware release; associated publications on policy learning)
- **DoF:** 11+ actuated (varies by version; P0/P2/P4 revisions with increasing DoF)
- **Cost:** ~$500-800 (bill of materials; significantly below all other hands in this section)
- **Tactile sensing:** None built-in (fingertip design accommodates aftermarket sensors)
- **Actuation:** Tendon-driven with off-the-shelf servo motors; tendons routed through 3D-printed finger linkages
- **Fabrication:** Fully 3D-printed structural components (FDM/SLA); no CNC or custom machining required

## Quantitative specs

| Spec | Value |
|------|-------|
| Fingers | 4 fingers + thumb (anthropomorphic layout) |
| Actuated DoF | 11+ (version-dependent; P4 has higher DoF) |
| Passive DoF | Additional under-actuated joints via tendon coupling |
| Weight | Not reported (3D-printed structure suggests low weight) |
| Actuator control bandwidth | ~50 Hz (limited by servo motors) |
| Maximum fingertip force | Limited by tendon tension and servo torque; lower than direct-drive designs |

## Key methodology/design

The FAIVE Hand is designed around the principle of ultra-low-cost accessibility. All structural components are 3D-printable on consumer-grade printers, and actuation uses commodity servo motors with tendon routing. The under-actuated tendon-driven design means fewer motors are needed than the number of joint DoFs, with passive joint coupling providing adaptive grasping. Multiple hardware revisions (P0, P2, P4) have been released with progressively refined designs. The hand mounts on standard robot arms and has been demonstrated with RL-based sim-to-real transfer for dexterous manipulation tasks.

## Main contributions

- Ultra-low-cost dexterous hand (~$500-800), approximately 2-6x cheaper than any other hand in this survey
- Fully 3D-printable: no CNC machining, laser cutting, or custom parts required; democratizes access to dexterous manipulation hardware
- Tendon-driven under-actuation providing adaptive grasping with fewer motors than joints
- Multiple open-source hardware revisions with community contributions
- Demonstrated sim-to-real transfer for manipulation policies

## Limitations/Gaps

- Lower DoF (11+) than LEAP (16), ORCA (17), or ISyHand (18), limiting fine manipulation dexterity
- Tendon-driven actuation introduces cable routing complexity, tendon wear, and potential slack issues
- No integrated tactile sensing; fingertip forces are not measurable without aftermarket sensors
- 3D-printed parts have lower mechanical durability than injection-molded or CNC-machined alternatives; may require reprinting after extended use
- Limited servo motor bandwidth (~50 Hz) and torque compared to Dynamixel or custom actuators
- Smaller research community and fewer published sim-to-real results compared to LEAP Hand
- Sim-to-real gap may be larger due to difficulty accurately modeling tendon dynamics and 3D-printed joint compliance

## Open-source status

Fully open-source (CAD, firmware, assembly instructions, BOM). GitHub: [srl-ethz/faive-hand](https://github.com/srl-ethz/faive-hand) (note: repository may use different naming conventions across versions). Multiple hardware revisions available.
