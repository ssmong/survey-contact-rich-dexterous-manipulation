### 7.3 Contact Trust Region

### Model-Based MPC (not RL)

**Note: Model-based trajectory optimization/MPC, not RL.**

**Full title:** A Contact-Implicit Model Predictive Control Framework for Dexterous In-Hand Manipulation (Contact Trust Region)

**Authors:** Aykut Onol, Russ Tedrake, et al. (MIT CSAIL / Toyota Research Institute)

**Venue/Year:** IJRR 2025

**arXiv:** https://arxiv.org/abs/2505.02291

**Method:** Contact-implicit model predictive control (CI-MPC). Uses trajectory optimization with complementarity constraints to reason about contact mode switches. Trust regions stabilize the optimization over the non-smooth contact landscape.

**Hand hardware:** Allegro Hand (16 DoF)

**Sim platform:** Drake (MIT)

**Sim2Real?** No. Simulation-only results reported.

**Tasks:** Contact-rich dexterous manipulation tasks requiring deliberate making and breaking of contact. In-hand reorientation and finger-gaiting where the controller must plan through contact mode transitions (e.g., lifting a finger and re-placing it at a new contact location).

**Key methodology:** Rather than learning a policy via RL, this work formulates dexterous manipulation as a contact-implicit trajectory optimization problem. The key challenge is that contact dynamics are non-smooth (complementarity constraints), making standard gradient-based optimization unreliable. The trust region approach constrains each optimization step to remain in a region where the local contact model is valid, enabling stable MPC through contact transitions. This produces physically consistent plans that respect friction cones, contact normals, and complementarity.

**Main contributions:**
- Proposed a trust-region stabilization for contact-implicit MPC that handles the non-smoothness of contact dynamics
- Demonstrated real-time-capable MPC for multi-finger contact-rich manipulation in Drake
- Provided a principled alternative to RL for contact-rich tasks where physical consistency and constraint satisfaction are critical

**Limitations/Gaps:** Requires an accurate dynamics model (no sim-to-real). Computational cost limits to moderate-complexity contact scenarios. Not demonstrated on real hardware. Limited object complexity compared to RL-based approaches that can handle diverse objects.

**Sim-only limitation:** Evaluated in simulation only; no sim-to-real transfer demonstrated, real-world viability unvalidated.

**Results:** Achieved stable contact-implicit MPC for Allegro Hand manipulation tasks with contact mode transitions (sim). Published in IJRR 2025.

## Inference / Deployment

- **Inference latency:** Contact-implicit MPC solving speed depends on the number of contact modes and planning horizon. Specific Hz not reported; typical contact-implicit MPC runs at 10-50 Hz for moderate-complexity problems.
- **Deployment hardware:** Simulation only (Drake). No real-robot deployment demonstrated.
- **Real-time capable?** Potentially, for simple contact scenarios. Contact-implicit optimization is computationally expensive due to combinatorial contact modes; real-time feasibility depends on problem complexity.

## Dataset / Data Collection

- **Dataset used:** No dataset. Model-based trajectory optimization/MPC (not learning-based).
- **Collection method:** Not applicable. Contact-implicit MPC uses an analytical dynamics model (Drake) with complementarity constraints. No training data, no demonstrations, no RL. Trust regions stabilize optimization over non-smooth contact landscape.
- **Data scale:** Not applicable (model-based, no training data).
- **Teleop equipment:** Not applicable.
- **Data format:** Not applicable.
- **Publicly available?** Drake simulator is open-source. Paper-specific code release status not reported.
