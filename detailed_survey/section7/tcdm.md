### 7.3 TCDM

**Type: Benchmark + baseline method**

**Full title:** From One Hand to Multiple Hands: Imitation Learning for Dexterous Manipulation from Single-Camera Teleoperation (also known as TCDM -- Task-Conditioned Dexterous Manipulation)

**Authors:** Sudeep Dasari, Abhinav Gupta, et al. (Meta FAIR)

**Venue/Year:** ICRA 2023

**arXiv:** https://github.com/facebookresearch/TCDM

**RL algorithm:** Model-free RL (PPO) with motion-capture-derived reference trajectories as priors. Uses human hand motion capture data retargeted to robot hand morphologies to bootstrap policy learning.

**Hand hardware:** 3 hand platforms: Adroit/Shadow-like (30 DoF), D'Claw (9 DoF), and Allegro (16 DoF) in simulation

**Sim platform:** MuJoCo

**Sim2Real?** No. Simulation-only.

**Tasks:** 50 diverse manipulation tasks using 34 objects from the GRAB dataset. Tasks include grasping, repositioning, and functional manipulation (e.g., using tools, opening containers). Tasks are derived from human motion-capture demonstrations retargeted to different hand morphologies.

**Key methodology:** TCDM leverages human hand motion capture data as a prior for RL-based dexterous manipulation. Human demonstrations from the GRAB dataset are retargeted to different robot hand morphologies, then used as reference motions to guide RL training via a tracking reward. This approach bootstraps exploration for contact-rich tasks that are otherwise difficult to learn from scratch. The task-conditioned formulation allows a single policy to handle multiple manipulation behaviors.

**Main contributions:**
- Demonstrated that human MoCap data can effectively bootstrap RL for diverse dexterous manipulation tasks across different hand morphologies
- Scaled to 50 tasks with 34 objects -- substantially larger than prior dexterous RL benchmarks at the time
- Showed cross-embodiment transfer: the same human demonstrations can guide policies for hands with different kinematics and DoF counts

**Limitations/Gaps:** Simulation-only with no sim-to-real transfer. Retargeting quality varies across hand morphologies. Some tasks that require precise force control (e.g., fragile objects) are not well captured by kinematic retargeting alone.

**Sim-only limitation:** Evaluated in simulation only; no sim-to-real transfer demonstrated, real-world viability unvalidated.

**Results:** Achieved successful learning on the majority of the 50 tasks across all three hand platforms (sim). MoCap-guided initialization significantly outperformed random exploration baselines. Code and pretrained models available on GitHub.

## Inference / Deployment

- **Inference latency:** Not reported. The MLP policy runs in <1ms per forward pass.
- **Deployment hardware:** Simulation only (MuJoCo). No real-robot deployment demonstrated.
- **Real-time capable?** Yes, for the policy itself (MLP inference is trivially fast). However, only simulation evaluation was performed.

## Dataset / Data Collection

- **Dataset used:** GRAB dataset (human hand motion capture) for reference trajectories. RL training in MuJoCo.
- **Collection method:** RL + human MoCap demonstrations (DAPG-style). Human hand MoCap data from GRAB dataset retargeted to 3 robot hand morphologies (Adroit/Shadow-like 30 DoF, D'Claw 9 DoF, Allegro 16 DoF). Retargeted motions used as reference trajectories for RL (tracking reward). 50 tasks with 34 objects.
- **Data scale:** 50 tasks, 34 objects from GRAB. MoCap reference trajectories bootstrap RL exploration.
- **Teleop equipment:** Not applicable (human MoCap data from GRAB dataset, not live teleoperation).
- **Data format:** GRAB MoCap format (SMPL-H hand parameters) retargeted to robot joint angles.
- **Publicly available?** Yes -- code and pretrained models at https://github.com/facebookresearch/TCDM. GRAB dataset publicly available.
