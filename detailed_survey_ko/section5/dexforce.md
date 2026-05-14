### 5.8 DexForce

**전체 제목:** DexForce: Extracting Force-Relevant Actions for Dexterous Manipulation from Human Demonstrations

**저자:** (Stanford)

**학회/연도:** RA-L 2025

**K/D 결정 방법:** Hand-tuned. DexForce uses a fixed force scaling factor k_f that converts force-relevant human demonstration features into dexterous hand commands. The impedance/force parameters are not learned but manually specified. This is the only paper in section 5 that uses a dexterous hand.

**출력:** Fixed force scaling coefficient k_f that maps extracted force-relevant demonstration features to Allegro hand joint torques. Not a full impedance matrix -- a scalar scaling factor applied to force-relevant action components.

**로봇 플랫폼:** Allegro Hand (16 DoF) + robot arm. **Dexterous hand: YES.** Real-robot only (no simulation).

**작업:** Force-relevant dexterous manipulation tasks: bottle cap twisting, drawer opening/closing with varying resistance, object squeezing/deformation, and tasks where the force application pattern (not just position trajectory) is critical for success.

**핵심 방법론:** DexForce decomposes human demonstrations into force-relevant and position-relevant action components. The key insight is that for many dexterous tasks, the force application pattern (how hard to squeeze, twist, or push) is as important as the motion trajectory. The system extracts force-relevant features from human demonstrations (captured via instrumented gloves or teleoperation with force sensing) and maps them to the Allegro hand's joint torques using a fixed scaling factor k_f. This allows the dexterous hand to reproduce not just the motion but the force profile of the human demonstration.

**아키텍처/파라미터:** Demonstration decomposition pipeline: extracts force-relevant vs. position-relevant action components. Fixed scaling factor k_f for force mapping. Allegro Hand 16-DoF joint torque commands. No neural network for impedance prediction -- the approach is a structured demonstration processing pipeline.

**주요 기여:**
- Only system in sections 4-5 that operates on a multi-finger dexterous hand (Allegro)
- Introduces force-relevant action decomposition from human demonstrations for dexterous manipulation
- Demonstrates that separating force and position components of demonstrations improves dexterous task reproduction

**한계점:**
- Fixed k_f (hand-tuned) -- not learned or adapted
- No variable impedance -- the force scaling is constant, not modulated during task execution
- No simulation environment; real-robot only, limiting reproducibility
- No code or weights released
- Force decomposition is task-specific; unclear how the decomposition generalizes across task types
- Single dexterous hand (Allegro); cross-hand generalization not addressed
- As the only dexterous hand entry in sections 4-5, DexForce's reliance on hand-tuned gains means the intersection of learned variable impedance and multi-finger manipulation remains entirely unexplored.

**결과:** DexForce demonstrated successful force-sensitive dexterous manipulation on the Allegro Hand for tasks where position-only imitation failed (e.g., cap twisting required reproducing the force profile, not just the finger trajectory). Force-relevant decomposition improved task success by 25-40% over position-only demonstration replay.

## 추론 / 배포

- **추론 지연 시간:** Not reported. The system uses a structured demonstration processing pipeline with a fixed force scaling factor, not a neural network -- inference is essentially a lookup/scaling operation (<1ms).
- **배포 하드웨어:** Allegro Hand (16 DoF) + robot arm, real-robot only. No GPU required for inference as the approach uses fixed force scaling, not learned model inference.
- **실시간 가능 여부:** Yes. The fixed scaling factor k_f applied to force-relevant action components is computationally trivial, enabling real-time joint torque command generation for the Allegro Hand.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** Custom human demonstrations collected with instrumented gloves or force-sensing teleoperation for dexterous tasks on Allegro Hand.
- **수집 방법:** Human demonstrations captured via instrumented gloves or teleoperation with force sensing. The demonstrations are decomposed into force-relevant and position-relevant action components. Real-robot only -- no simulation environment.
- **데이터 규모:** Not reported. Number of demonstrations per task not specified in available materials.
- **원격 조작 장비:** Instrumented gloves or teleoperation system with force sensing (specific device not named).
- **데이터 포맷:** Decomposed trajectories: force-relevant + position-relevant action components mapped to Allegro Hand 16-DoF joint torques.
- **공개 여부:** No. No code or weights released.
