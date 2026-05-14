### 7.4 Closing Reality Gap

**Full title:** Closing the Reality Gap for Force-Controlled Dexterous Grasping (exact title unverified; 2026 preprint)

**Authors:** Not fully verified

**Venue/Year:** arXiv 2026 (no confirmed arXiv link available)

**Note:** This entry is referenced in the survey table but the specific arXiv link could not be confirmed as of the survey date. Details below are based on available references.

> **All contributions below are marked [Unverified] because the paper was not directly accessed.**

**RL algorithm:** [Unverified] RL (PPO variant) with force-aware training. Specifically addresses the sim-to-real gap for force-controlled grasping by incorporating force feedback into the RL training loop and using force-domain randomization.

**Hand hardware:** [Unverified] 5-finger dexterous hand (specific model unverified)

**Sim platform:** [Unverified] Not confirmed

**Sim2Real?** [Unverified] Yes. Zero-shot sim-to-real transfer with force control, specifically targeting the force-domain reality gap.

**Tasks:** [Unverified] Force-controlled dexterous grasping -- grasping objects with explicit force regulation rather than pure position control. The focus is on achieving stable grasps that apply appropriate forces rather than just achieving kinematic contact.

**Key methodology:** [Unverified] This work specifically targets the reality gap in force-controlled dexterous manipulation. While most sim-to-real dexterous RL transfers position policies, force-controlled grasping requires matching both kinematic trajectories and force profiles. The approach introduces force-domain randomization and force-aware reward shaping to produce policies that transfer with correct force behaviors, not just correct positions.

**Main contributions:**
- [Unverified] Addressed the under-explored problem of sim-to-real transfer for force-controlled (not just position-controlled) dexterous grasping
- [Unverified] Demonstrated zero-shot transfer of force-aware grasping policies
- [Unverified] Highlighted that the "reality gap" for force-controlled manipulation is qualitatively different from the position-control reality gap

**Limitations/Gaps:** Paper not fully verified; details may differ from description above. Limited information available as of survey date. Specific hand platform and simulator not confirmed.

**Results:** No quantitative results can be reported; paper not accessed.

## Dataset / Data Collection

- **Dataset used:** [Unverified] No pre-collected dataset expected. Likely pure RL with force-aware training in simulation.
- **Collection method:** [Unverified] Pure RL with force-domain randomization and force-aware reward shaping. Targets sim-to-real transfer for force-controlled (not just position-controlled) dexterous grasping.
- **Data scale:** [Unverified] Not reported. Paper not fully accessed.
- **Teleop equipment:** Not applicable (pure RL, no demonstrations expected).
- **Data format:** Not applicable.
- **Publicly available?** Dataset details not reported. Paper not fully verified.

## Inference / Deployment

- **Inference latency:** [Unverified] Not reported. Expected MLP policy runs in <1ms per forward pass.
- **Deployment hardware:** [Unverified] 5-finger dexterous hand. Sim-to-real transfer with force control.
- **Real-time capable?** [Unverified] Expected yes, for MLP-based RL policy. Paper not fully verified.
