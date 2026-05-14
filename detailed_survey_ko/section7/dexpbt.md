### 7.2 DexPBT

**전체 제목:** DexPBT: Scaling up Dexterous Manipulation for Hand-Arm Systems with Population Based Training

**저자:** Aleksei Petrenko, Arthur Allshire, Gavriel State, Ankur Handa, Viktor Makoviychuk

**학회/연도:** RSS 2023

**RL 알고리즘:** PPO with Population-Based Training (PBT); maintains a population of policies with different hyperparameters, periodically replacing underperformers with mutated copies of top performers

**핸드 하드웨어:** Allegro Hand (16 DoF) + Kuka arm

**시뮬레이션 플랫폼:** IsaacGym

**Sim2Real 여부:** No (simulation-only evaluation)

**객체 수:** Multiple objects; evaluated on cube reorientation and other manipulation tasks

**작업:** Coordinated arm-hand manipulation including in-hand reorientation, regrasping, and object handover; multi-task training across diverse manipulation objectives

**핵심 방법론:** Applies Population-Based Training to dexterous arm-hand manipulation, automatically tuning reward weights, learning rates, and domain randomization parameters across a population of policies. PBT enables efficient hyperparameter search in the challenging high-dimensional action space of arm-hand systems (16 + 7 = 23 DoF). The population evolves toward policies that balance multiple task objectives without manual reward shaping.

**주요 기여:**
- First application of PBT to dexterous arm-hand manipulation, automating hyperparameter and reward tuning
- Multi-task training framework handling diverse manipulation objectives with a single population
- Demonstrated that PBT significantly outperforms fixed-hyperparameter PPO on arm-hand tasks

**한계점:** Simulation-only (no sim2real); PBT requires significant compute (population of parallel policies); limited object diversity; the evolved hyperparameters may not transfer across tasks or embodiments

**시뮬레이션 전용 한계:** 시뮬레이션에서만 평가됨; sim-to-real 전이 미입증, 실제 환경 실행 가능성 미검증.

## 추론 / 배포

- **추론 지연 시간:** Not reported. The MLP policy runs in <1ms per forward pass.
- **배포 하드웨어:** Simulation only (IsaacGym). No real-robot deployment demonstrated.
- **실시간 가능 여부:** Yes, for the policy itself (MLP inference is trivially fast). However, only simulation evaluation was performed.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** No pre-collected dataset. Pure RL (PPO) with Population-Based Training (PBT) -- all data generated in simulation.
- **수집 방법:** Pure RL in IsaacGym. PBT maintains a population of policies with different hyperparameters, automatically tuning reward weights, learning rates, and domain randomization. Multi-task training across diverse arm-hand manipulation objectives.
- **데이터 규모:** Standard parallel RL training in IsaacGym. Multiple objects for cube reorientation and other tasks.
- **원격 조작 장비:** Not applicable (pure RL, no demonstrations).
- **데이터 포맷:** Not applicable (online RL, no offline dataset).
- **공개 여부:** Code release status not reported.
