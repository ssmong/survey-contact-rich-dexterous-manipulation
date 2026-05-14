### 7.3 VTDexManip

**전체 제목:** VTDexManip: A Vision-Tactile Dataset for Dexterous Manipulation

**저자:** Qiang Luo, Xudong Han, Haoran Li, Ao Li, Boyang Gao, Shaowei Liu, et al.

**학회/연도:** ICLR 2025

**arXiv:** https://arxiv.org/abs/2501.01370

**RL 알고리즘:** PPO with multi-modal observations (vision + binary tactile). The framework trains teacher policies with privileged state, then distills to student policies using vision and tactile inputs.

**핸드 하드웨어:** Multi-finger dexterous hand (simulated), modeled with binary tactile sensor arrays on fingertips

**시뮬레이션 플랫폼:** IsaacGym

**Sim2Real 여부:** No. Simulation-only benchmark and dataset.

**작업:** 6 complex dexterous tasks: (1) bottle cap opening/closing; (2) faucet turning; (3) object reorientation; (4) pen spinning; (5) valve turning; (6) lid manipulation. Tasks involve sustained multi-finger contact with objects requiring precise coordination.

**핵심 방법론:** VTDexManip provides both a benchmark and a large-scale dataset (565K frames, 182 objects) for vision-tactile dexterous manipulation. Binary tactile contact signals on each fingertip are used alongside visual observations to learn contact-aware policies. The dataset captures the correlation between visual object state, tactile contact patterns, and successful manipulation strategies, enabling both RL training and imitation learning approaches.

**주요 기여:**
- Created a large-scale vision-tactile dataset for dexterous manipulation (565K frames across 182 objects and 6 tasks)
- Demonstrated that incorporating tactile feedback improves policy performance on contact-rich tasks compared to vision-only baselines
- Released 18 pretrained models spanning different task-sensor combinations for community benchmarking

**한계점:** Binary tactile sensing is a significant simplification compared to real tactile sensors (e.g., GelSight) that provide rich spatial force distributions. Sim-only with no real-world validation. The gap between simulated and real tactile signals remains unaddressed.

**시뮬레이션 전용 한계:** 시뮬레이션에서만 평가됨; sim-to-real 전이 미입증, 실제 환경 실행 가능성 미검증.

**결과:** Vision+tactile policies outperformed vision-only baselines on 5 of 6 tasks (sim). Released 18 pretrained model checkpoints. Dataset and code publicly available.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** Custom large-scale vision-tactile dexterous manipulation dataset (VTDexManip). 565K frames, 182 objects, 6 tasks.
- **수집 방법:** Generated in IsaacGym simulation. PPO-trained teacher policies with privileged state generate trajectories; vision + binary tactile observations recorded. 6 tasks: bottle cap, faucet, reorientation, pen spinning, valve, lid manipulation.
- **데이터 규모:** 565,000 frames across 182 objects and 6 tasks. 18 pretrained models released.
- **원격 조작 장비:** Not applicable (simulation-generated data).
- **데이터 포맷:** Vision frames + binary tactile contact signals + proprioceptive state. Specific file format not reported.
- **공개 여부:** Yes -- dataset, 18 pretrained models, and code publicly available.

## 추론 / 배포

- **추론 지연 시간:** Not applicable (simulation benchmark/dataset). Policy inference depends on the algorithm used; PPO-trained MLP policies run in <1ms.
- **배포 하드웨어:** Simulation only (IsaacGym). No real-robot deployment.
- **실시간 가능 여부:** Not applicable (simulation benchmark; no real-robot deployment).
