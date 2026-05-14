### 5.11 Divide et Impera

**전체 제목:** Divide et Impera: Learning Impedance Families for Peg-in-Hole Assembly

**저자:** (MIT / KIT)

**학회/연도:** arXiv preprint, 2024

**K/D 결정 방법:** Neural network success predictor that evaluates candidate impedance parameter "families." The system trains a neural network to predict assembly success given a proposed impedance configuration, then uses this predictor to search over impedance parameter families to find configurations that maximize predicted success. Both K and D are optimized.

**출력:** Impedance parameter families -- sets of stiffness K and damping D configurations that are predicted to succeed for a given class of assembly tasks. Not a single K/D pair but a family (distribution) of viable impedance configurations, providing robustness to parameter variation.

**로봇 플랫폼:** Real robot arm (specific platform not prominently specified). No dexterous hand.

**작업:** Peg-in-hole assembly with varying peg/hole geometries, clearances, and materials. The focus is on finding impedance parameters that generalize across assembly variations within a task family.

**핵심 방법론:** Divide et Impera ("divide and conquer") approaches impedance learning by first defining families of impedance parameters (regions in K-D space) and then training a neural network to predict which families lead to successful assembly. Rather than learning a single optimal K/D setting, the system learns to partition the impedance space into success/failure regions, providing an entire family of viable configurations. This is more robust than point estimates because small variations in K/D within a successful family still lead to task success. The approach uses real-robot assembly trials to train the success predictor.

**아키텍처/파라미터:** Neural network success predictor (MLP or similar) mapping (task features, K, D) -> predicted success probability. Optimization over the predictor to find maximal-success impedance families. Real-robot data collection for training the predictor.

**주요 기여:**
- Impedance "family" concept: instead of learning a single K/D, learns regions in impedance space that are viable, providing robustness
- Neural network success predictor for impedance configuration evaluation, enabling efficient search over the impedance space
- Demonstrates that different assembly task variations (geometry, clearance) require different impedance families, motivating adaptive impedance selection

**한계점:**
- No dexterous hand -- arm-level assembly
- Narrow task domain (peg-in-hole assembly only)
- Requires real-robot data for training the success predictor -- no simulation-based pretraining
- No code or weights released
- Impedance families are computed offline, not adapted online during task execution
- Does not address multi-contact or multi-finger scenarios

**결과:** Divide et Impera identified impedance families that achieved higher assembly success rates than fixed-impedance or randomly sampled impedance configurations. The success predictor accurately identified viable vs. non-viable impedance regions, and the learned families transferred across minor geometry variations within a task class.

## 추론 / 배포

- **추론 지연 시간:** Not reported. Impedance families are computed offline via neural network success predictor optimization. At deployment time, a pre-computed impedance configuration from the successful family is applied -- no online inference required.
- **배포 하드웨어:** Real robot arm (specific platform not prominently specified). The offline optimization runs on standard compute; deployment uses fixed impedance from the pre-computed family.
- **실시간 가능 여부:** Yes, at deployment. The impedance parameters are selected offline and applied as fixed values during execution, so there is no online inference bottleneck. However, the impedance is not adapted online during task execution.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** Custom real-robot assembly trial dataset on KUKA LBR. Exhaustive grid search over impedance parameter space.
- **수집 방법:** Automated real-robot trials on KUKA LBR performing peg-in-hole assembly. Tested 3^8 = 6,561 impedance parameter combinations per peg type across 8 impedance parameters (translational stiffnesses kx, ky, kz; rotational stiffnesses kC, kB, kA; damping ratios). Four peg geometries: square, triangular, hexagonal, cylindrical (3D-printed PLA, PRUSA i3 MK3). Binary success/failure labels. Clearance tolerances: 0.14-0.20 mm.
- **데이터 규모:** 6,561 trials per peg x 4 peg types = ~26,244 total trials. ~22 seconds per trial, ~40 hours per peg, ~160 hours total. Success counts: 101 (triangle), 646 (square), 181 (hexagon), 147 (cylinder) out of 6,561 per peg.
- **원격 조작 장비:** Not applicable (automated grid search, no teleoperation).
- **데이터 포맷:** Binary success/failure labels indexed by 8-dimensional impedance parameter vectors. Parameter ranges discretized into 3 levels (small, medium, large).
- **공개 여부:** Yes -- CAD data of all workpieces via Dropbox; robot application code on GitHub. All hardware and software tools publicly available.
