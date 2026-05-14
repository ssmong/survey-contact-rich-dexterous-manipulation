### 7.4 DexDrummer

**전체 제목:** DexDrummer: Dexterous Drumming via Reinforcement Learning

**저자:** Hao-Chun Fang, Kenneth Shaw, Deepak Pathak, et al. (Stanford)

**학회/연도:** arXiv 2026

**arXiv:** https://arxiv.org/abs/2603.22263

**Musical instrument differentiation:** Distinguished by tool grasping (drumstick) and impact force control. Unlike piano playing (RoboPianist, HandelBot) where fingers directly contact keys, drumming requires holding tools and generating controlled impact forces on drum surfaces -- combining grasp stability with dynamic striking. Sim-only.

**RL 알고리즘:** PPO with musical-score-conditioned rewards. Similar framework to HandelBot but adapted for percussion. Requires learning to generate impact forces on drum surfaces.

**핸드 하드웨어:** Bimanual dexterous hands (holding drumsticks)

**시뮬레이션 플랫폼:** IsaacGym / MuJoCo

**Sim2Real 여부:** No (simulation results; real-world transfer not reported in initial preprint).

**작업:** Drumming -- striking drum surfaces at correct times with correct intensity according to musical scores. Involves holding drumsticks (tool use), rapid contact-rich impacts, bimanual coordination, and dynamic force control.

**핵심 방법론:** DexDrummer extends musical instrument playing to percussion, which introduces additional challenges beyond piano: the agent must hold tools (drumsticks), generate controlled impact forces (not just key presses), and coordinate rapid bimanual alternating strikes. The contact dynamics of stick-on-drum impacts are more violent and dynamic than piano key presses, requiring robust contact handling in simulation.

**주요 기여:**
- Extended dexterous musical manipulation to percussion/drumming, requiring tool-use and impact force control
- Demonstrated that RL can learn dynamic striking motions with held tools, combining grasping stability with impact generation
- Addressed bimanual coordination for alternating and simultaneous strikes

**한계점:** No real-world transfer demonstrated. Drumstick grasping stability during rapid striking is a significant sim-to-real challenge. Limited rhythmic complexity in evaluation.

**시뮬레이션 전용 한계:** 시뮬레이션에서만 평가됨; sim-to-real 전이 미입증, 실제 환경 실행 가능성 미검증.

**결과:** Achieved successful drumming in simulation with correct timing and force patterns (sim). Code publicly available.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** Musical scores for percussion as task specifications. No pre-collected robot demonstration dataset.
- **수집 방법:** Pure RL (PPO) with musical-score-conditioned rewards in IsaacGym/MuJoCo. Bimanual dexterous hands holding drumsticks. Agent learns tool grasping, impact force generation, and timing from reward feedback. Simulation only.
- **데이터 규모:** Musical scores of varying difficulty. Standard parallel RL training.
- **원격 조작 장비:** Not applicable (pure RL, no demonstrations).
- **데이터 포맷:** Musical scores (percussion note sequences with timing).
- **공개 여부:** Code publicly available.

## 추론 / 배포

- **추론 지연 시간:** Not reported. The MLP policy runs in <1ms per forward pass.
- **배포 하드웨어:** Simulation only (IsaacGym/MuJoCo). No real-robot deployment demonstrated.
- **실시간 가능 여부:** Yes, for the policy itself (MLP inference is trivially fast). However, only simulation evaluation was performed.
