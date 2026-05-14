### 5.7 DA-VIL

**전체 제목:** DA-VIL: Adaptive Dual-Arm Manipulation with Reinforcement Learning and Variable Impedance Control

**저자:** (IIIT Hyderabad / Brown University)

**학회/연도:** ICRA 2025 (submitted 2024)

**K/D 결정 방법:** Reinforcement learning + Quadratic Programming (QP) optimization. The RL policy learns high-level task parameters including desired stiffness, and a QP solver optimizes the impedance parameters in real-time to satisfy contact constraints (e.g., force limits, kinematic feasibility) while tracking the RL-specified stiffness targets. This two-level architecture separates task-level impedance reasoning (RL) from constraint satisfaction (QP).

**출력:** Cartesian stiffness K (optimized by QP). Damping D is not explicitly learned; uncontrolled damping can produce oscillatory contact behavior.

**로봇 플랫폼:** Dual-arm robot (simulation). No dexterous hand.

**작업:** Dual-arm cooperative manipulation: collaborative object transport, bimanual insertion, and tasks requiring coordinated compliance between two arms in contact with a shared object.

**핵심 방법론:** DA-VIL addresses the challenge of dual-arm impedance control where the two arms must coordinate their compliance to avoid internal forces on the shared object. The RL policy outputs desired behavior parameters (including stiffness targets), and a QP solver computes the actual impedance parameters that best approximate these targets while satisfying hard constraints (joint limits, force limits, kinematic compatibility between the two arms). This approach avoids the instability that can arise when two independently impedance-controlled arms grasp the same object with incompatible compliance settings.

**아키텍처/파라미터:** Two-level architecture: (1) RL policy (PPO or similar) outputting desired task parameters including stiffness targets, and (2) QP solver computing feasible impedance parameters subject to constraints. Dual-arm simulation environment.

**주요 기여:**
- Two-level RL + QP architecture for dual-arm variable impedance control with constraint satisfaction
- Addresses the coordination problem in dual-arm impedance control (avoiding internal forces from incompatible compliance)
- Demonstrates that QP-based impedance optimization improves dual-arm manipulation robustness

**한계점:**
- No dexterous hand -- dual arm with grippers
- Simulation only -- no real-robot experiments
- Damping not explicitly learned or reported; uncontrolled damping can produce oscillatory contact behavior
- Project page only -- no public code repository with runnable code
- Dual-arm coordination is specific; unclear how the approach extends to multi-finger scenarios

**결과:** DA-VIL outperformed fixed-impedance and unconstrained RL baselines on dual-arm cooperative tasks in simulation. QP-constrained impedance reduced internal forces on shared objects and improved task success rates.

## 추론 / 배포

- **추론 지연 시간:** Not reported. The two-level architecture (RL policy MLP + QP solver) should run in <5ms per step. QP solvers for impedance optimization typically solve in <1ms for the constraint dimensions involved.
- **배포 하드웨어:** Simulation only (dual-arm simulation environment). No real-robot deployment demonstrated. Specific compute hardware not reported.
- **실시간 가능 여부:** Yes, in principle. Both the MLP policy and the QP solver are lightweight and should support real-time control. However, only simulation evaluation was performed.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** No pre-collected dataset. Pure RL -- data generated through simulation interaction.
- **수집 방법:** Pure RL (PPO or similar) in dual-arm simulation environment. No human demonstrations. The QP solver operates online during both training and evaluation to compute feasible impedance parameters from RL-proposed targets.
- **데이터 규모:** Standard RL training scale in simulation. Specific episode counts not reported.
- **원격 조작 장비:** Not applicable (pure RL, no demonstrations).
- **데이터 포맷:** Not applicable (online RL, no offline dataset).
- **공개 여부:** No public code repository. Project page only.
