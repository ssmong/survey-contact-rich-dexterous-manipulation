### 5.6 CHEQ

**Full title:** CHEQ: Contact-aware Hybrid Equilibrium Q-learning for Variable Impedance Control

**Authors:** (RWTH Aachen)

**Venue/Year:** arXiv preprint, 2025

**How K/D are determined:** Reinforcement learning (hybrid adaptive Q-learning). The RL agent learns both stiffness K and damping D as part of a hybrid action space that combines continuous impedance parameter selection with discrete mode switching (e.g., free-space motion vs. contact regulation). The Q-learning framework optimizes impedance parameters for equilibrium contact force regulation.

**What is output:** Cartesian stiffness K and damping D, along with desired equilibrium position. The agent learns to modulate both K and D continuously during task execution, adapting compliance to the current contact phase.

**Robot platform:** Industrial robot arm for polishing/grinding tasks. Real hardware evaluation (not simulation-only). No dexterous hand.

**Tasks:** Surface polishing and grinding tasks requiring consistent contact force regulation against workpieces with varying geometry and stiffness.

**Key methodology:** CHEQ formulates variable impedance control as a hybrid RL problem with both discrete (contact mode) and continuous (impedance parameters) action components. The Q-learning framework learns to select impedance parameters that drive the system toward a desired force equilibrium during contact. The "contact-aware" aspect means the agent explicitly reasons about contact/non-contact transitions and adjusts impedance accordingly -- high compliance during approach to avoid impact, and appropriate stiffness during contact to maintain desired force. The hybrid formulation handles the discontinuity at contact transitions better than purely continuous RL formulations.

**Architecture/Parameters:** Hybrid Q-network with discrete mode head and continuous impedance parameter head. Continuous outputs: K (stiffness), D (damping), desired position. Discrete output: contact mode (free-space, approaching, in-contact, retracting). Trained on real hardware with force feedback.

**Main contributions:**
- Hybrid RL formulation that explicitly handles contact/non-contact mode transitions for impedance learning
- Contact-aware Q-learning that optimizes impedance for force equilibrium during contact
- Real-hardware evaluation on industrial polishing tasks, demonstrating practical applicability

**Limitations/Gaps:**
- No dexterous hand -- industrial arm for polishing/grinding
- Narrow task domain (surface processing); unclear generalization to diverse manipulation tasks
- No code or weights released
- RL training on real hardware is sample-inefficient and requires careful safety constraints
- Limited to single-contact-point scenarios (polishing); does not address multi-contact tasks

**Results:** CHEQ achieved more consistent contact force regulation than fixed-impedance and basic RL baselines during polishing tasks. Force tracking error reduced by 20-40% compared to position-controlled polishing. The hybrid discrete-continuous action space improved learning stability at contact transitions.

## Inference / Deployment

- **Inference latency:** Not reported. The Q-network (MLP with discrete mode head and continuous impedance head) runs in <1ms per forward pass. Real-time impedance updates are feasible given the lightweight architecture.
- **Deployment hardware:** Industrial robot arm for real-hardware polishing/grinding evaluation. Specific GPU or compute hardware not reported.
- **Real-time capable?** Yes, likely. The hybrid Q-network is lightweight (MLP-based), and the system was evaluated on real hardware for industrial polishing tasks, suggesting real-time operation. Specific control frequency not reported.

## Dataset / Data Collection

- **Dataset used:** No pre-collected dataset. RL trained directly on real hardware with force feedback.
- **Collection method:** Online RL (hybrid adaptive Q-learning) on real industrial robot hardware performing polishing/grinding tasks. Data generated through real-world interaction with force feedback. No simulation pre-training mentioned. Safety constraints applied during real-hardware RL training.
- **Data scale:** Not reported. Real-hardware RL is sample-limited; specific episode counts not disclosed.
- **Teleop equipment:** Not applicable (pure RL, no demonstrations).
- **Data format:** Not applicable (online RL, no offline dataset).
- **Publicly available?** No. No code or weights released.
