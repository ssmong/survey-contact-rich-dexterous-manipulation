### 7.3 DexGarmentLab

**전체 제목:** DexGarmentLab: Dexterous Garment Manipulation Benchmark with Multi-Finger Hands

**저자:** Yuxuan Gao, Zihang Zhao, Zhenjun Yu, Haoyu Xiong, Ruihai Wu, Yan Shen, Jiangtao Gong, He Wang, et al.

**학회/연도:** NeurIPS 2025 (Spotlight)

**arXiv:** https://arxiv.org/abs/2503.18693

**RL 알고리즘:** PPO and SAC baselines provided. The benchmark supports multiple RL approaches and includes IL baselines (e.g., diffusion policy). Deformable simulation uses GPU-accelerated FEM/PBD cloth solvers.

**핸드 하드웨어:** Bimanual dexterous hands (simulated), supporting multiple hand models

**시뮬레이션 플랫폼:** IsaacSim (with GPU-accelerated cloth simulation)

**Sim2Real 여부:** No. Simulation benchmark only.

**작업:** 15 garment manipulation tasks across 2500+ garment instances. Tasks include: folding (t-shirts, pants, towels), hanging (on hangers, hooks), dressing (putting garments on mannequins), buttoning/unbuttoning, zipping, and re-arranging. These are long-horizon, multi-stage tasks requiring sequential contact-rich interactions with deformable objects.

**핵심 방법론:** DexGarmentLab tackles the intersection of dexterous manipulation and deformable object manipulation -- a particularly challenging combination because garments exhibit complex dynamics (folding, draping, wrinkling) that require precise multi-finger coordination. The benchmark leverages GPU-accelerated cloth simulation for parallel training and includes a large garment asset library (2500+ instances) for generalization evaluation. Task difficulty spans from simple pick-and-place to multi-stage sequences (e.g., fold, then stack).

**주요 기여:**
- First large-scale benchmark for dexterous garment manipulation with multi-finger hands (prior garment benchmarks used grippers)
- Scaled to 2500+ garment instances across 15 tasks, enabling systematic generalization evaluation
- Demonstrated that existing RL/IL methods achieve limited success on complex garment tasks, establishing challenging baselines for future work

**한계점:** Sim-only; cloth simulation fidelity (especially friction, self-collision) may not transfer to real. Current RL baselines achieve low success rates on complex tasks, suggesting the benchmark may require new algorithmic approaches. No tactile sensing modeled despite garment manipulation being inherently tactile.

**시뮬레이션 전용 한계:** 시뮬레이션에서만 평가됨; sim-to-real 전이 미입증, 실제 환경 실행 가능성 미검증.

**결과:** PPO and diffusion policy baselines achieved moderate success on simpler tasks (folding towels) but low success on complex multi-stage tasks (dressing) (sim). NeurIPS 2025 Spotlight. Code publicly available.

## 추론 / 배포

- **추론 지연 시간:** Not applicable (simulation benchmark). Policy inference speed depends on the RL/IL algorithm used; MLP policies run in <1ms.
- **배포 하드웨어:** Simulation only (IsaacSim with GPU-accelerated cloth simulation). No real-robot deployment.
- **실시간 가능 여부:** Not applicable (simulation benchmark; no real-robot deployment).

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** No pre-collected dataset. Benchmark environment with 2,500+ garment instances across 15 tasks in IsaacSim.
- **수집 방법:** Pure RL (PPO, SAC) and IL (diffusion policy) baselines trained in IsaacSim with GPU-accelerated cloth simulation. Deformable simulation via FEM/PBD cloth solvers. 15 garment tasks (folding, hanging, dressing, buttoning, zipping) with bimanual dexterous hands.
- **데이터 규모:** 2,500+ garment instances across 15 tasks. Benchmark provides standardized environments, not pre-collected datasets.
- **원격 조작 장비:** Not applicable (simulation benchmark).
- **데이터 포맷:** IsaacSim simulation environments. Standardized task definitions and evaluation protocols.
- **공개 여부:** Yes -- benchmark code publicly available.
