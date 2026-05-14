### 7.3 Contact Trust Region

### Model-Based MPC (not RL)

**Note: Model-based trajectory optimization/MPC, not RL.**

**전체 제목:** A Contact-Implicit Model Predictive Control Framework for Dexterous In-Hand Manipulation (Contact Trust Region)

**저자:** Aykut Onol, Russ Tedrake, et al. (MIT CSAIL / Toyota Research Institute)

**학회/연도:** IJRR 2025

**arXiv:** https://arxiv.org/abs/2505.02291

**Method:** Contact-implicit model predictive control (CI-MPC). Uses trajectory optimization with complementarity constraints to reason about contact mode switches. Trust regions stabilize the optimization over the non-smooth contact landscape.

**핸드 하드웨어:** Allegro Hand (16 DoF)

**시뮬레이션 플랫폼:** Drake (MIT)

**Sim2Real 여부:** No. Simulation-only results reported.

**작업:** Contact-rich dexterous manipulation tasks requiring deliberate making and breaking of contact. In-hand reorientation and finger-gaiting where the controller must plan through contact mode transitions (e.g., lifting a finger and re-placing it at a new contact location).

**핵심 방법론:** Rather than learning a policy via RL, this work formulates dexterous manipulation as a contact-implicit trajectory optimization problem. The key challenge is that contact dynamics are non-smooth (complementarity constraints), making standard gradient-based optimization unreliable. The trust region approach constrains each optimization step to remain in a region where the local contact model is valid, enabling stable MPC through contact transitions. This produces physically consistent plans that respect friction cones, contact normals, and complementarity.

**주요 기여:**
- Proposed a trust-region stabilization for contact-implicit MPC that handles the non-smoothness of contact dynamics
- Demonstrated real-time-capable MPC for multi-finger contact-rich manipulation in Drake
- Provided a principled alternative to RL for contact-rich tasks where physical consistency and constraint satisfaction are critical

**한계점:** Requires an accurate dynamics model (no sim-to-real). Computational cost limits to moderate-complexity contact scenarios. Not demonstrated on real hardware. Limited object complexity compared to RL-based approaches that can handle diverse objects.

**시뮬레이션 전용 한계:** 시뮬레이션에서만 평가됨; sim-to-real 전이 미입증, 실제 환경 실행 가능성 미검증.

**결과:** Achieved stable contact-implicit MPC for Allegro Hand manipulation tasks with contact mode transitions (sim). Published in IJRR 2025.

## 추론 / 배포

- **추론 지연 시간:** Contact-implicit MPC solving speed depends on the number of contact modes and planning horizon. Specific Hz not reported; typical contact-implicit MPC runs at 10-50 Hz for moderate-complexity problems.
- **배포 하드웨어:** Simulation only (Drake). No real-robot deployment demonstrated.
- **실시간 가능 여부:** Potentially, for simple contact scenarios. Contact-implicit optimization is computationally expensive due to combinatorial contact modes; real-time feasibility depends on problem complexity.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** No dataset. Model-based trajectory optimization/MPC (not learning-based).
- **수집 방법:** Not applicable. Contact-implicit MPC uses an analytical dynamics model (Drake) with complementarity constraints. No training data, no demonstrations, no RL. Trust regions stabilize optimization over non-smooth contact landscape.
- **데이터 규모:** Not applicable (model-based, no training data).
- **원격 조작 장비:** Not applicable.
- **데이터 포맷:** Not applicable.
- **공개 여부:** Drake simulator is open-source. Paper-specific code release status not reported.
