### 7.3 DexGarmentLab

**Full title:** DexGarmentLab: Dexterous Garment Manipulation Benchmark with Multi-Finger Hands

**Authors:** Yuxuan Gao, Zihang Zhao, Zhenjun Yu, Haoyu Xiong, Ruihai Wu, Yan Shen, Jiangtao Gong, He Wang, et al.

**Venue/Year:** NeurIPS 2025 (Spotlight)

**arXiv:** https://arxiv.org/abs/2503.18693

**RL algorithm:** PPO and SAC baselines provided. The benchmark supports multiple RL approaches and includes IL baselines (e.g., diffusion policy). Deformable simulation uses GPU-accelerated FEM/PBD cloth solvers.

**Hand hardware:** Bimanual dexterous hands (simulated), supporting multiple hand models

**Sim platform:** IsaacSim (with GPU-accelerated cloth simulation)

**Sim2Real?** No. Simulation benchmark only.

**Tasks:** 15 garment manipulation tasks across 2500+ garment instances. Tasks include: folding (t-shirts, pants, towels), hanging (on hangers, hooks), dressing (putting garments on mannequins), buttoning/unbuttoning, zipping, and re-arranging. These are long-horizon, multi-stage tasks requiring sequential contact-rich interactions with deformable objects.

**Key methodology:** DexGarmentLab tackles the intersection of dexterous manipulation and deformable object manipulation -- a particularly challenging combination because garments exhibit complex dynamics (folding, draping, wrinkling) that require precise multi-finger coordination. The benchmark leverages GPU-accelerated cloth simulation for parallel training and includes a large garment asset library (2500+ instances) for generalization evaluation. Task difficulty spans from simple pick-and-place to multi-stage sequences (e.g., fold, then stack).

**Main contributions:**
- First large-scale benchmark for dexterous garment manipulation with multi-finger hands (prior garment benchmarks used grippers)
- Scaled to 2500+ garment instances across 15 tasks, enabling systematic generalization evaluation
- Demonstrated that existing RL/IL methods achieve limited success on complex garment tasks, establishing challenging baselines for future work

**Limitations/Gaps:** Sim-only; cloth simulation fidelity (especially friction, self-collision) may not transfer to real. Current RL baselines achieve low success rates on complex tasks, suggesting the benchmark may require new algorithmic approaches. No tactile sensing modeled despite garment manipulation being inherently tactile.

**Sim-only limitation:** Evaluated in simulation only; no sim-to-real transfer demonstrated, real-world viability unvalidated.

**Results:** PPO and diffusion policy baselines achieved moderate success on simpler tasks (folding towels) but low success on complex multi-stage tasks (dressing) (sim). NeurIPS 2025 Spotlight. Code publicly available.

## Inference / Deployment

- **Inference latency:** Not applicable (simulation benchmark). Policy inference speed depends on the RL/IL algorithm used; MLP policies run in <1ms.
- **Deployment hardware:** Simulation only (IsaacSim with GPU-accelerated cloth simulation). No real-robot deployment.
- **Real-time capable?** Not applicable (simulation benchmark; no real-robot deployment).

## Dataset / Data Collection

- **Dataset used:** No pre-collected dataset. Benchmark environment with 2,500+ garment instances across 15 tasks in IsaacSim.
- **Collection method:** Pure RL (PPO, SAC) and IL (diffusion policy) baselines trained in IsaacSim with GPU-accelerated cloth simulation. Deformable simulation via FEM/PBD cloth solvers. 15 garment tasks (folding, hanging, dressing, buttoning, zipping) with bimanual dexterous hands.
- **Data scale:** 2,500+ garment instances across 15 tasks. Benchmark provides standardized environments, not pre-collected datasets.
- **Teleop equipment:** Not applicable (simulation benchmark).
- **Data format:** IsaacSim simulation environments. Standardized task definitions and evaluation protocols.
- **Publicly available?** Yes -- benchmark code publicly available.
