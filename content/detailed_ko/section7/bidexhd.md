### 7.4 BiDexHD

**전체 제목:** BiDexHD: Bimanual Dexterous Manipulation from Human Demonstrations

**저자:** Yuanpei Chen, Yaodong Yang, et al. (PKU)

**학회/연도:** arXiv 2025

**arXiv:** https://arxiv.org/abs/2501.09821

**RL 알고리즘:** RL (PPO) with human demonstration-guided exploration. Uses retargeted human bimanual demonstrations to initialize and guide RL training on 141 tasks from the TACO benchmark.

**핸드 하드웨어:** 2x Shadow Hands (48 DoF total)

**시뮬레이션 플랫폼:** IsaacGym

**Sim2Real 여부:** No. Simulation-only.

**작업:** 141 bimanual dexterous manipulation tasks from the TACO dataset. Tasks include: bimanual object handover, coordinated assembly, tool use with two hands, container manipulation, and other tasks requiring tight bimanual coordination. This is the largest bimanual dexterous task set reported.

**핵심 방법론:** BiDexHD addresses the challenge of learning bimanual dexterous policies at scale. Human bimanual demonstrations are retargeted to the dual Shadow Hand setup and used to initialize RL exploration. The demonstration-guided approach significantly reduces the exploration burden for complex bimanual tasks where random exploration rarely discovers useful behaviors. The TACO benchmark provides a standardized evaluation across 141 tasks with varying complexity.

**주요 기여:**
- Scaled bimanual dexterous RL to 141 tasks -- the largest reported bimanual dexterous task set
- Demonstrated that human demonstration-guided RL substantially outperforms pure RL on complex bimanual tasks
- Built on and extended the TACO benchmark for systematic bimanual evaluation

**한계점:** Simulation-only with dual Shadow Hands (48 DoF), which are impractical for most real-world labs. No vision-based policies (uses privileged state). Quality of retargeted demonstrations depends on the human-to-robot morphology mapping. Code not publicly available.

**시뮬레이션 전용 한계:** 시뮬레이션에서만 평가됨; sim-to-real 전이 미입증, 실제 환경 실행 가능성 미검증.

**결과:** Achieved successful learning on a large fraction of the 141 TACO tasks (sim), significantly outperforming baselines without demonstration guidance.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** TACO benchmark (141 bimanual dexterous tasks). Human bimanual demonstrations retargeted to dual Shadow Hands.
- **수집 방법:** RL + human demo-guided exploration (DAPG-style). Human bimanual demonstrations retargeted to dual Shadow Hand setup (48 DoF total) to initialize and guide PPO exploration on 141 tasks. Privileged state observations (no vision).
- **데이터 규모:** 141 bimanual tasks from TACO dataset. Human demonstrations used for exploration guidance.
- **원격 조작 장비:** Not applicable (retargeted human MoCap/video demonstrations, not live robot teleoperation).
- **데이터 포맷:** Retargeted demonstration trajectories for dual Shadow Hands.
- **공개 여부:** Code not publicly available. TACO benchmark available separately.

## 추론 / 배포

- **추론 지연 시간:** Not reported. The MLP policy runs in <1ms per forward pass.
- **배포 하드웨어:** Simulation only (IsaacGym). No real-robot deployment demonstrated.
- **실시간 가능 여부:** Yes, for the policy itself (MLP inference is trivially fast). However, only simulation evaluation was performed.
