### 7.3 TCDM

**Type: Benchmark + baseline method**

**전체 제목:** From One Hand to Multiple Hands: Imitation Learning for Dexterous Manipulation from Single-Camera Teleoperation (also known as TCDM -- Task-Conditioned Dexterous Manipulation)

**저자:** Sudeep Dasari, Abhinav Gupta, et al. (Meta FAIR)

**학회/연도:** ICRA 2023

**arXiv:** https://github.com/facebookresearch/TCDM

**RL 알고리즘:** Model-free RL (PPO) with motion-capture-derived reference trajectories as priors. Uses human hand motion capture data retargeted to robot hand morphologies to bootstrap policy learning.

**핸드 하드웨어:** 3 hand platforms: Adroit/Shadow-like (30 DoF), D'Claw (9 DoF), and Allegro (16 DoF) in simulation

**시뮬레이션 플랫폼:** MuJoCo

**Sim2Real 여부:** No. Simulation-only.

**작업:** 50 diverse manipulation tasks using 34 objects from the GRAB dataset. Tasks include grasping, repositioning, and functional manipulation (e.g., using tools, opening containers). Tasks are derived from human motion-capture demonstrations retargeted to different hand morphologies.

**핵심 방법론:** TCDM leverages human hand motion capture data as a prior for RL-based dexterous manipulation. Human demonstrations from the GRAB dataset are retargeted to different robot hand morphologies, then used as reference motions to guide RL training via a tracking reward. This approach bootstraps exploration for contact-rich tasks that are otherwise difficult to learn from scratch. The task-conditioned formulation allows a single policy to handle multiple manipulation behaviors.

**주요 기여:**
- Demonstrated that human MoCap data can effectively bootstrap RL for diverse dexterous manipulation tasks across different hand morphologies
- Scaled to 50 tasks with 34 objects -- substantially larger than prior dexterous RL benchmarks at the time
- Showed cross-embodiment transfer: the same human demonstrations can guide policies for hands with different kinematics and DoF counts

**한계점:** Simulation-only with no sim-to-real transfer. Retargeting quality varies across hand morphologies. Some tasks that require precise force control (e.g., fragile objects) are not well captured by kinematic retargeting alone.

**시뮬레이션 전용 한계:** 시뮬레이션에서만 평가됨; sim-to-real 전이 미입증, 실제 환경 실행 가능성 미검증.

**결과:** Achieved successful learning on the majority of the 50 tasks across all three hand platforms (sim). MoCap-guided initialization significantly outperformed random exploration baselines. Code and pretrained models available on GitHub.

## 추론 / 배포

- **추론 지연 시간:** Not reported. The MLP policy runs in <1ms per forward pass.
- **배포 하드웨어:** Simulation only (MuJoCo). No real-robot deployment demonstrated.
- **실시간 가능 여부:** Yes, for the policy itself (MLP inference is trivially fast). However, only simulation evaluation was performed.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** GRAB dataset (human hand motion capture) for reference trajectories. RL training in MuJoCo.
- **수집 방법:** RL + human MoCap demonstrations (DAPG-style). Human hand MoCap data from GRAB dataset retargeted to 3 robot hand morphologies (Adroit/Shadow-like 30 DoF, D'Claw 9 DoF, Allegro 16 DoF). Retargeted motions used as reference trajectories for RL (tracking reward). 50 tasks with 34 objects.
- **데이터 규모:** 50 tasks, 34 objects from GRAB. MoCap reference trajectories bootstrap RL exploration.
- **원격 조작 장비:** Not applicable (human MoCap data from GRAB dataset, not live teleoperation).
- **데이터 포맷:** GRAB MoCap format (SMPL-H hand parameters) retargeted to robot joint angles.
- **공개 여부:** Yes -- code and pretrained models at https://github.com/facebookresearch/TCDM. GRAB dataset publicly available.
