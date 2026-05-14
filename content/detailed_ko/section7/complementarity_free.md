### 7.3 Complementarity-Free

### Model-Based MPC (not RL)

**Note: Model-based trajectory optimization/MPC, not RL.**

**전체 제목:** Differentiable Compliant Contact Simulation for Dexterous Manipulation (Complementarity-Free Multi-Contact Model)

**저자:** Tao Pang, Russ Tedrake group (MIT CSAIL)

**학회/연도:** RSS 2025 (submitted 2024)

**arXiv:** https://arxiv.org/abs/2408.07855

**Method:** Differentiable simulation for trajectory optimization and MPC. Replaces non-smooth complementarity constraints with a smooth, closed-form compliant contact model that permits gradient computation through contact events.

**핸드 하드웨어:** Allegro Hand (16 DoF)

**시뮬레이션 플랫폼:** Drake (MIT)

**Sim2Real 여부:** No. Simulation-only.

**작업:** Contact-rich dexterous manipulation with the Allegro Hand. Tasks requiring MPC at 50-100 Hz with multi-finger contact, including in-hand pivoting, finger gaiting, and contact-mode-switching manipulation.

**핵심 방법론:** Standard rigid-body contact simulation uses complementarity constraints (LCPs) that are non-smooth and non-differentiable at contact mode transitions. This work replaces them with a compliant (penalty-based) contact model that has a closed-form, differentiable expression. This enables gradient-based trajectory optimization and MPC to "see through" contact events, computing informative gradients even when contacts are being made and broken. The resulting MPC runs at 50-100 Hz for multi-finger manipulation.

**주요 기여:**
- Derived a closed-form differentiable contact model that eliminates the need for complementarity constraints while preserving physical realism
- Achieved 50-100 Hz MPC rates for multi-finger contact-rich manipulation -- a significant speedup over prior contact-implicit optimizers
- Enabled gradient-based planning through contact mode transitions, where prior methods relied on combinatorial or sampling-based approaches

**한계점:** The compliant contact model introduces approximation errors (penetration). Not validated on real hardware. Requires accurate model parameters (stiffness, damping). Limited to quasi-static or slow-dynamic regimes where the compliant model is valid.

**시뮬레이션 전용 한계:** 시뮬레이션에서만 평가됨; sim-to-real 전이 미입증, 실제 환경 실행 가능성 미검증.

**결과:** Demonstrated real-time MPC at 50-100 Hz for Allegro Hand contact-rich manipulation in Drake (sim). Presented at RSS 2025.

## 추론 / 배포

- **추론 지연 시간:** MPC runs at 50-100 Hz (10-20ms per control step) for Allegro Hand contact-rich manipulation in Drake simulation.
- **배포 하드웨어:** Simulation only (Drake). No real-robot deployment demonstrated.
- **실시간 가능 여부:** Yes, in simulation. The differentiable contact model enables real-time MPC at 50-100 Hz, which is sufficient for dexterous manipulation. Real-hardware deployment not validated.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** No dataset. Model-based differentiable simulation and MPC (not learning-based).
- **수집 방법:** Not applicable. Differentiable compliant contact simulation replaces complementarity constraints with smooth, closed-form contact model. Enables gradient-based trajectory optimization and MPC at 50-100 Hz. No training data needed.
- **데이터 규모:** Not applicable (model-based, no training data).
- **원격 조작 장비:** Not applicable.
- **데이터 포맷:** Not applicable.
- **공개 여부:** Drake simulator is open-source. Paper-specific code release status not reported.
