### 7.3 ComFree-Sim

### Model-Based MPC (not RL)

**Note: Model-based trajectory optimization/MPC, not RL.**

**Full title:** Complementarity-Free Dexterous Manipulation on GPU (ComFree-Sim)

**Authors:** Not fully verified (2026 preprint)

**Venue/Year:** arXiv 2026

**arXiv:** https://arxiv.org/abs/2603.12185

**Method:** GPU-parallel complementarity-free contact simulation for trajectory optimization and MPC. Extends the complementarity-free approach to run on NVIDIA Warp for massively parallel contact computation.

**Hand hardware:** LEAP Hand (16 DoF)

**Sim platform:** Custom simulator built on NVIDIA Warp

**Sim2Real?** No. Simulation-only.

**Tasks:** Multi-finger contact-rich manipulation with the LEAP Hand. Contact-mode-switching tasks similar to the complementarity-free line of work but parallelized across thousands of environments.

**Key methodology:** ComFree-Sim takes the complementarity-free differentiable contact model and implements it on GPU using NVIDIA Warp, enabling thousands of parallel contact simulations. This bridges the gap between the physical accuracy of contact-implicit optimization and the parallelism of RL simulation platforms like IsaacGym. The GPU backend enables both massively parallel MPC rollouts and potential integration with RL training loops.

**Main contributions:**
- Ported complementarity-free contact simulation to GPU (NVIDIA Warp), achieving large-scale parallelism
- Enabled thousands of parallel contact-rich manipulation simulations, previously limited to single-environment CPU computation
- Demonstrated the LEAP Hand as a target platform, broadening applicability beyond Drake/Allegro setups

**Limitations/Gaps:** Very recent preprint (2026) with limited external validation. No sim-to-real results. Code not publicly available as of survey date. The NVIDIA Warp ecosystem is less mature than IsaacGym/MuJoCo for full RL workflows.

**Sim-only limitation:** Evaluated in simulation only; no sim-to-real transfer demonstrated, real-world viability unvalidated.

**Results:** Achieved GPU-parallel contact simulation for LEAP Hand manipulation (sim). Specific quantitative results pending further publication.

## Inference / Deployment

- **Inference latency:** GPU-parallel complementarity-free simulation enables massively parallel contact computation. Specific Hz for single-instance MPC not reported, but GPU parallelism is designed for real-time or faster-than-real-time operation.
- **Deployment hardware:** Simulation only (NVIDIA Warp). No real-robot deployment demonstrated.
- **Real-time capable?** Designed for real-time GPU-parallel MPC, but real-hardware deployment not demonstrated.

## Dataset / Data Collection

- **Dataset used:** No dataset. GPU-parallel complementarity-free contact simulation for trajectory optimization/MPC.
- **Collection method:** Not applicable. Extends the complementarity-free differentiable contact model to NVIDIA Warp for massively parallel contact computation. No training data -- model-based approach. Enables both parallel MPC rollouts and potential integration with RL training.
- **Data scale:** Not applicable (model-based simulation framework).
- **Teleop equipment:** Not applicable.
- **Data format:** Not applicable.
- **Publicly available?** Code not publicly available as of survey date (2026 preprint).
