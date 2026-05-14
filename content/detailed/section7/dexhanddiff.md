### 7.2 DexHandDiff

**Full title:** DexHandDiff: Interaction-Aware Diffusion Planning for Adaptive Dexterous Manipulation

**Authors:** Zixuan Liang, Xinyu Zhan, Yisi Hu, Zhehao Cai, Jian Tang, Jianqiang Wang

**Venue/Year:** CVPR 2025

**RL algorithm:** Diffusion-based planning (denoising diffusion for trajectory generation); not standard RL but generates full manipulation trajectories via conditional diffusion

**Hand hardware:** Shadow Hand (24 DoF)

**Sim platform:** Adroit (MuJoCo-based benchmark)

**Sim2Real?** No (simulation benchmark evaluation)

**Object count:** Standard Adroit benchmark objects (pen, door, hammer, ball, etc.)

**Tasks:** In-hand pen rotation, door opening, hammer use, ball relocation -- the standard Adroit benchmark suite plus additional manipulation tasks

**Key methodology:** Uses a conditional diffusion model to generate full manipulation trajectories (sequence of hand joint configurations) conditioned on the current state and goal. The key innovation is interaction-aware denoising: the diffusion process incorporates predicted contact information to guide trajectory generation toward physically plausible contact-rich motions. This avoids the myopic behavior of single-step RL policies by planning entire trajectories.

**Main contributions:**
- Interaction-aware diffusion planning that incorporates contact prediction into trajectory generation
- Full-trajectory planning for dexterous manipulation (vs. single-step policy output)
- State-of-the-art results on Adroit benchmark tasks, outperforming prior RL and imitation learning methods

**Limitations/Gaps:** Simulation-only (Adroit benchmark); computational cost of diffusion planning may limit real-time deployment; evaluated on Shadow Hand in MuJoCo only; no real-world validation; limited to the standard Adroit task set

**Sim-only limitation:** Evaluated in simulation only; no sim-to-real transfer demonstrated, real-world viability unvalidated.

## Inference / Deployment

- **Inference latency:** Diffusion-based trajectory planning requires multiple denoising steps (50-500ms per trajectory on a modern GPU). Not designed for real-time step-by-step control.
- **Deployment hardware:** Simulation only (Adroit/MuJoCo). No real-robot deployment demonstrated.
- **Real-time capable?** Limited. Diffusion planning generates full trajectories offline; real-time replanning would require fast denoising (DDIM acceleration) or caching.

## Dataset / Data Collection

- **Dataset used:** Adroit benchmark demonstration data (MuJoCo) for training the diffusion-based trajectory planner.
- **Collection method:** Diffusion-based planning -- not standard RL. Conditional diffusion model generates full manipulation trajectories from state+goal. Trained on demonstration trajectories from the Adroit benchmark suite. Interaction-aware denoising incorporates predicted contact information.
- **Data scale:** Standard Adroit benchmark demonstration sets (pen, door, hammer, ball tasks). Specific episode counts per task follow Adroit conventions.
- **Teleop equipment:** Not applicable (Adroit demonstrations are pre-collected scripted/expert data).
- **Data format:** Adroit benchmark format (MuJoCo state trajectories).
- **Publicly available?** Adroit benchmark is publicly available. DexHandDiff code release status not reported.
