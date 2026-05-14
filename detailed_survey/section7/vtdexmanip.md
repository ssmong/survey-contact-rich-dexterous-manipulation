### 7.3 VTDexManip

**Full title:** VTDexManip: A Vision-Tactile Dataset for Dexterous Manipulation

**Authors:** Qiang Luo, Xudong Han, Haoran Li, Ao Li, Boyang Gao, Shaowei Liu, et al.

**Venue/Year:** ICLR 2025

**arXiv:** https://arxiv.org/abs/2501.01370

**RL algorithm:** PPO with multi-modal observations (vision + binary tactile). The framework trains teacher policies with privileged state, then distills to student policies using vision and tactile inputs.

**Hand hardware:** Multi-finger dexterous hand (simulated), modeled with binary tactile sensor arrays on fingertips

**Sim platform:** IsaacGym

**Sim2Real?** No. Simulation-only benchmark and dataset.

**Tasks:** 6 complex dexterous tasks: (1) bottle cap opening/closing; (2) faucet turning; (3) object reorientation; (4) pen spinning; (5) valve turning; (6) lid manipulation. Tasks involve sustained multi-finger contact with objects requiring precise coordination.

**Key methodology:** VTDexManip provides both a benchmark and a large-scale dataset (565K frames, 182 objects) for vision-tactile dexterous manipulation. Binary tactile contact signals on each fingertip are used alongside visual observations to learn contact-aware policies. The dataset captures the correlation between visual object state, tactile contact patterns, and successful manipulation strategies, enabling both RL training and imitation learning approaches.

**Main contributions:**
- Created a large-scale vision-tactile dataset for dexterous manipulation (565K frames across 182 objects and 6 tasks)
- Demonstrated that incorporating tactile feedback improves policy performance on contact-rich tasks compared to vision-only baselines
- Released 18 pretrained models spanning different task-sensor combinations for community benchmarking

**Limitations/Gaps:** Binary tactile sensing is a significant simplification compared to real tactile sensors (e.g., GelSight) that provide rich spatial force distributions. Sim-only with no real-world validation. The gap between simulated and real tactile signals remains unaddressed.

**Sim-only limitation:** Evaluated in simulation only; no sim-to-real transfer demonstrated, real-world viability unvalidated.

**Results:** Vision+tactile policies outperformed vision-only baselines on 5 of 6 tasks (sim). Released 18 pretrained model checkpoints. Dataset and code publicly available.

## Dataset / Data Collection

- **Dataset used:** Custom large-scale vision-tactile dexterous manipulation dataset (VTDexManip). 565K frames, 182 objects, 6 tasks.
- **Collection method:** Generated in IsaacGym simulation. PPO-trained teacher policies with privileged state generate trajectories; vision + binary tactile observations recorded. 6 tasks: bottle cap, faucet, reorientation, pen spinning, valve, lid manipulation.
- **Data scale:** 565,000 frames across 182 objects and 6 tasks. 18 pretrained models released.
- **Teleop equipment:** Not applicable (simulation-generated data).
- **Data format:** Vision frames + binary tactile contact signals + proprioceptive state. Specific file format not reported.
- **Publicly available?** Yes -- dataset, 18 pretrained models, and code publicly available.

## Inference / Deployment

- **Inference latency:** Not applicable (simulation benchmark/dataset). Policy inference depends on the algorithm used; PPO-trained MLP policies run in <1ms.
- **Deployment hardware:** Simulation only (IsaacGym). No real-robot deployment.
- **Real-time capable?** Not applicable (simulation benchmark; no real-robot deployment).
