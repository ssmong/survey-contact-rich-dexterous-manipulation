### 7.1 UniDexGrasp++

**전체 제목:** UniDexGrasp++: Improving Dexterous Grasping Policy Learning via Geometry-aware Curriculum and Iterative Generalist-Specialist Learning

**저자:** Weikang Wan, Haoran Geng, Yun Liu, Zikang Yan, Yaodong Yang, He Wang

**학회/연도:** ICCV 2023

**PKU-EPIC lineage:** Improves UniDexGrasp from ~60% to 85.4% via iterative generalist-specialist learning. The geometry-aware curriculum and iterative specialist training specifically address the long-tail failure cases of UniDexGrasp.

**RL 알고리즘:** PPO with DAgger distillation; geometry-aware curriculum learning combined with iterative generalist-specialist training

**핸드 하드웨어:** Shadow Hand (24 DoF)

**시뮬레이션 플랫폼:** IsaacGym

**Sim2Real 여부:** No

**객체 수:** 3000+ objects; 85.4% state-based success rate (sim), 78.2% vision-based (sim)

**작업:** Universal dexterous grasping -- grasping arbitrary objects from a tabletop given goal grasp poses

**핵심 방법론:** Proposes a two-phase training pipeline. First, a geometry-aware curriculum orders training objects by grasping difficulty (estimated from contact geometry). Second, an iterative generalist-specialist loop trains specialist policies on hard object clusters, then distills them back into a generalist. This iteratively improves performance on the long tail of difficult objects.

**주요 기여:**
- Geometry-aware curriculum that significantly accelerates training convergence
- Iterative generalist-specialist learning scheme that improves long-tail performance from ~60% (UniDexGrasp) to 85.4%
- Vision-based policy achieving 78.2% across 3000+ objects using point cloud input

**정량적 결과:**

| Metric | Value |
|---|---|
| State-based success rate | 85.4% (sim) |
| Vision-based success rate | 78.2% (sim) |
| UniDexGrasp baseline | ~60% (sim) |
| Improvement over predecessor | +25.4 pp |
| Object set size | 3000+ |

**한계점:** Simulation-only; requires pre-computed goal grasp poses (from contact map estimation); Shadow Hand only; gap between state-based and vision-based performance (~7%) suggests visual perception remains a bottleneck

**시뮬레이션 전용 한계:** 시뮬레이션에서만 평가됨; sim-to-real 전이 미입증, 실제 환경 실행 가능성 미검증.

## 추론 / 배포

- **추론 지연 시간:** Not reported. The distilled generalist MLP policy runs in <1ms per forward pass.
- **배포 하드웨어:** Simulation only (IsaacGym). No real-robot deployment demonstrated.
- **실시간 가능 여부:** Yes, for the policy itself. However, only simulation evaluation was performed.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** No pre-collected demonstration dataset. Iterative generalist-specialist RL training with geometry-aware curriculum in IsaacGym.
- **수집 방법:** Pure RL (PPO) with DAgger distillation in IsaacGym. Geometry-aware curriculum orders 3,000+ objects by grasping difficulty. Iterative generalist-specialist loop trains specialists on hard object clusters, distills back into generalist. Both state-based and vision-based (point cloud) policies.
- **데이터 규모:** 3,000+ objects. State-based: 85.4% success. Vision-based: 78.2% success (sim).
- **원격 조작 장비:** Not applicable (pure RL, no demonstrations).
- **데이터 포맷:** Not applicable (online RL, no offline dataset).
- **공개 여부:** Dataset/code release status not reported.
