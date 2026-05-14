### 5.6 CHEQ

**전체 제목:** CHEQ: Contact-aware Hybrid Equilibrium Q-learning for Variable Impedance Control

**저자:** (RWTH Aachen)

**학회/연도:** arXiv preprint, 2025

**K/D 결정 방법:** Reinforcement learning (hybrid adaptive Q-learning). The RL agent learns both stiffness K and damping D as part of a hybrid action space that combines continuous impedance parameter selection with discrete mode switching (e.g., free-space motion vs. contact regulation). The Q-learning framework optimizes impedance parameters for equilibrium contact force regulation.

**출력:** Cartesian stiffness K and damping D, along with desired equilibrium position. The agent learns to modulate both K and D continuously during task execution, adapting compliance to the current contact phase.

**로봇 플랫폼:** Industrial robot arm for polishing/grinding tasks. Real hardware evaluation (not simulation-only). No dexterous hand.

**작업:** Surface polishing and grinding tasks requiring consistent contact force regulation against workpieces with varying geometry and stiffness.

**핵심 방법론:** CHEQ formulates variable impedance control as a hybrid RL problem with both discrete (contact mode) and continuous (impedance parameters) action components. The Q-learning framework learns to select impedance parameters that drive the system toward a desired force equilibrium during contact. The "contact-aware" aspect means the agent explicitly reasons about contact/non-contact transitions and adjusts impedance accordingly -- high compliance during approach to avoid impact, and appropriate stiffness during contact to maintain desired force. The hybrid formulation handles the discontinuity at contact transitions better than purely continuous RL formulations.

**아키텍처/파라미터:** Hybrid Q-network with discrete mode head and continuous impedance parameter head. Continuous outputs: K (stiffness), D (damping), desired position. Discrete output: contact mode (free-space, approaching, in-contact, retracting). Trained on real hardware with force feedback.

**주요 기여:**
- Hybrid RL formulation that explicitly handles contact/non-contact mode transitions for impedance learning
- Contact-aware Q-learning that optimizes impedance for force equilibrium during contact
- Real-hardware evaluation on industrial polishing tasks, demonstrating practical applicability

**한계점:**
- No dexterous hand -- industrial arm for polishing/grinding
- Narrow task domain (surface processing); unclear generalization to diverse manipulation tasks
- No code or weights released
- RL training on real hardware is sample-inefficient and requires careful safety constraints
- Limited to single-contact-point scenarios (polishing); does not address multi-contact tasks

**결과:** CHEQ achieved more consistent contact force regulation than fixed-impedance and basic RL baselines during polishing tasks. Force tracking error reduced by 20-40% compared to position-controlled polishing. The hybrid discrete-continuous action space improved learning stability at contact transitions.

## 추론 / 배포

- **추론 지연 시간:** Not reported. The Q-network (MLP with discrete mode head and continuous impedance head) runs in <1ms per forward pass. Real-time impedance updates are feasible given the lightweight architecture.
- **배포 하드웨어:** Industrial robot arm for real-hardware polishing/grinding evaluation. Specific GPU or compute hardware not reported.
- **실시간 가능 여부:** Yes, likely. The hybrid Q-network is lightweight (MLP-based), and the system was evaluated on real hardware for industrial polishing tasks, suggesting real-time operation. Specific control frequency not reported.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** No pre-collected dataset. RL trained directly on real hardware with force feedback.
- **수집 방법:** Online RL (hybrid adaptive Q-learning) on real industrial robot hardware performing polishing/grinding tasks. Data generated through real-world interaction with force feedback. No simulation pre-training mentioned. Safety constraints applied during real-hardware RL training.
- **데이터 규모:** Not reported. Real-hardware RL is sample-limited; specific episode counts not disclosed.
- **원격 조작 장비:** Not applicable (pure RL, no demonstrations).
- **데이터 포맷:** Not applicable (online RL, no offline dataset).
- **공개 여부:** No. No code or weights released.
