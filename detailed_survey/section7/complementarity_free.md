### 7.3 Complementarity-Free

### Model-Based MPC (not RL)

**Note: Model-based trajectory optimization/MPC, not RL.**

**Full title:** Differentiable Compliant Contact Simulation for Dexterous Manipulation (Complementarity-Free Multi-Contact Model)

**Authors:** Tao Pang, Russ Tedrake group (MIT CSAIL)

**Venue/Year:** RSS 2025 (submitted 2024)

**arXiv:** https://arxiv.org/abs/2408.07855

**Method:** Differentiable simulation for trajectory optimization and MPC. Replaces non-smooth complementarity constraints with a smooth, closed-form compliant contact model that permits gradient computation through contact events.

**Hand hardware:** Allegro Hand (16 DoF)

**Sim platform:** Drake (MIT)

**Sim2Real?** No. Simulation-only.

**Tasks:** Contact-rich dexterous manipulation with the Allegro Hand. Tasks requiring MPC at 50-100 Hz with multi-finger contact, including in-hand pivoting, finger gaiting, and contact-mode-switching manipulation.

**Key methodology:** Standard rigid-body contact simulation uses complementarity constraints (LCPs) that are non-smooth and non-differentiable at contact mode transitions. This work replaces them with a compliant (penalty-based) contact model that has a closed-form, differentiable expression. This enables gradient-based trajectory optimization and MPC to "see through" contact events, computing informative gradients even when contacts are being made and broken. The resulting MPC runs at 50-100 Hz for multi-finger manipulation.

**Main contributions:**
- Derived a closed-form differentiable contact model that eliminates the need for complementarity constraints while preserving physical realism
- Achieved 50-100 Hz MPC rates for multi-finger contact-rich manipulation -- a significant speedup over prior contact-implicit optimizers
- Enabled gradient-based planning through contact mode transitions, where prior methods relied on combinatorial or sampling-based approaches

**Limitations/Gaps:** The compliant contact model introduces approximation errors (penetration). Not validated on real hardware. Requires accurate model parameters (stiffness, damping). Limited to quasi-static or slow-dynamic regimes where the compliant model is valid.

**Sim-only limitation:** Evaluated in simulation only; no sim-to-real transfer demonstrated, real-world viability unvalidated.

**Results:** Demonstrated real-time MPC at 50-100 Hz for Allegro Hand contact-rich manipulation in Drake (sim). Presented at RSS 2025.

## Inference / Deployment

- **Inference latency:** MPC runs at 50-100 Hz (10-20ms per control step) for Allegro Hand contact-rich manipulation in Drake simulation.
- **Deployment hardware:** Simulation only (Drake). No real-robot deployment demonstrated.
- **Real-time capable?** Yes, in simulation. The differentiable contact model enables real-time MPC at 50-100 Hz, which is sufficient for dexterous manipulation. Real-hardware deployment not validated.

## Dataset / Data Collection

- **Dataset used:** No dataset. Model-based differentiable simulation and MPC (not learning-based).
- **Collection method:** Not applicable. Differentiable compliant contact simulation replaces complementarity constraints with smooth, closed-form contact model. Enables gradient-based trajectory optimization and MPC at 50-100 Hz. No training data needed.
- **Data scale:** Not applicable (model-based, no training data).
- **Teleop equipment:** Not applicable.
- **Data format:** Not applicable.
- **Publicly available?** Drake simulator is open-source. Paper-specific code release status not reported.
