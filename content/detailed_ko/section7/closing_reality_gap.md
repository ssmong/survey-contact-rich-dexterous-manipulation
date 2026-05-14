### 7.4 Closing Reality Gap

**전체 제목:** Closing the Reality Gap for Force-Controlled Dexterous Grasping (exact title unverified; 2026 preprint)

**저자:** Not fully verified

**학회/연도:** arXiv 2026 (no confirmed arXiv link available)

**Note:** This entry is referenced in the survey table but the specific arXiv link could not be confirmed as of the survey date. Details below are based on available references.

> **All contributions below are marked [Unverified] because the paper was not directly accessed.**

**RL 알고리즘:** [Unverified] RL (PPO variant) with force-aware training. Specifically addresses the sim-to-real gap for force-controlled grasping by incorporating force feedback into the RL training loop and using force-domain randomization.

**핸드 하드웨어:** [Unverified] 5-finger dexterous hand (specific model unverified)

**시뮬레이션 플랫폼:** [Unverified] Not confirmed

**Sim2Real 여부:** [Unverified] Yes. Zero-shot sim-to-real transfer with force control, specifically targeting the force-domain reality gap.

**작업:** [Unverified] Force-controlled dexterous grasping -- grasping objects with explicit force regulation rather than pure position control. The focus is on achieving stable grasps that apply appropriate forces rather than just achieving kinematic contact.

**핵심 방법론:** [Unverified] This work specifically targets the reality gap in force-controlled dexterous manipulation. While most sim-to-real dexterous RL transfers position policies, force-controlled grasping requires matching both kinematic trajectories and force profiles. The approach introduces force-domain randomization and force-aware reward shaping to produce policies that transfer with correct force behaviors, not just correct positions.

**주요 기여:**
- [Unverified] Addressed the under-explored problem of sim-to-real transfer for force-controlled (not just position-controlled) dexterous grasping
- [Unverified] Demonstrated zero-shot transfer of force-aware grasping policies
- [Unverified] Highlighted that the "reality gap" for force-controlled manipulation is qualitatively different from the position-control reality gap

**한계점:** Paper not fully verified; details may differ from description above. Limited information available as of survey date. Specific hand platform and simulator not confirmed.

**결과:** No quantitative results can be reported; paper not accessed.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** [Unverified] No pre-collected dataset expected. Likely pure RL with force-aware training in simulation.
- **수집 방법:** [Unverified] Pure RL with force-domain randomization and force-aware reward shaping. Targets sim-to-real transfer for force-controlled (not just position-controlled) dexterous grasping.
- **데이터 규모:** [Unverified] Not reported. Paper not fully accessed.
- **원격 조작 장비:** Not applicable (pure RL, no demonstrations expected).
- **데이터 포맷:** Not applicable.
- **공개 여부:** Dataset details not reported. Paper not fully verified.

## 추론 / 배포

- **추론 지연 시간:** [Unverified] Not reported. Expected MLP policy runs in <1ms per forward pass.
- **배포 하드웨어:** [Unverified] 5-finger dexterous hand. Sim-to-real transfer with force control.
- **실시간 가능 여부:** [Unverified] Expected yes, for MLP-based RL policy. Paper not fully verified.
