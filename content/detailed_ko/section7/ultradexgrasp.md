### 7.1 UltraDexGrasp

**전체 제목:** UltraDexGrasp: Ultra-Scalable Dexterous Grasping with Cross-Embodiment Diverse Grasp Dataset

**저자:** Jiayi Chen, He Wang, et al.

**학회/연도:** ICRA 2026

**PKU-EPIC lineage:** Scales Dexonomy from 9.5M to 20M grasps; the primary contribution is dataset scale, not algorithmic novelty. The optimization pipeline (BODex/cuRobo bilevel optimization) and taxonomy structure (from Dexonomy) are inherited. The paper demonstrates that scaling the generated grasp data improves cross-embodiment transfer but does not introduce new optimization or learning methods.

**RL 알고리즘:** Multi-strategy approach combining optimization (BODex/cuRobo) with policy learning; leverages diverse grasp datasets for cross-embodiment training

**핸드 하드웨어:** Multiple dexterous hands (cross-embodiment)

**시뮬레이션 플랫폼:** BODex + cuRobo

**Sim2Real 여부:** Yes; 81.2% real-world success rate (real)

**객체 수:** 20 million training frames across diverse objects

**작업:** Ultra-scale cross-embodiment dexterous grasping

**핵심 방법론:** Builds on the BODex/Dexonomy pipeline to generate an ultra-large-scale cross-embodiment grasp dataset (20M frames), then trains cross-embodiment grasping policies using this data. The multi-strategy approach combines optimization-based grasp generation with learned execution policies, leveraging the scale and diversity of the generated dataset to achieve robust generalization.

**주요 기여:**
- Largest-scale dexterous grasping dataset at time of publication (20M frames)
- Cross-embodiment grasping trained from diverse generated data rather than hand-specific policies
- Demonstrates that scaling grasp data generation translates to improved real-world transfer

**정량적 결과:**

| Metric | Value |
|---|---|
| Real-world success rate | 81.2% (real) |
| Dataset size | 20M frames |
| Dexonomy baseline dataset | 9.5M grasps |

**한계점:** Building on prior optimization pipelines (BODex, Dexonomy) -- incremental improvement over those baselines; 81.2% real success rate is lower than RobustDexGrasp (94.6%), suggesting cross-embodiment generality trades off with single-embodiment performance; limited task diversity beyond grasping

## 추론 / 배포

- **추론 지연 시간:** Not explicitly reported. The learned policy runs in <5ms per forward pass. Optimization-based grasp generation is offline.
- **배포 하드웨어:** Multiple dexterous hands (cross-embodiment). 81.2% real-world success rate demonstrated.
- **실시간 가능 여부:** Yes, at deployment. The learned policy supports real-time grasping control on real hardware.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** Ultra-large-scale cross-embodiment grasp dataset, extending BODex/Dexonomy pipelines. 20 million training frames.
- **수집 방법:** Optimization-based grasp generation (BODex/cuRobo bilevel optimization) combined with policy learning from generated data. Cross-embodiment training across multiple hand morphologies.
- **데이터 규모:** 20 million training frames. Extends Dexonomy's 9.5M grasps to larger scale.
- **원격 조작 장비:** Not applicable (optimization-based generation + RL from generated data).
- **데이터 포맷:** Grasp datasets with training frames for cross-embodiment policy learning.
- **공개 여부:** Dataset release status not reported.
