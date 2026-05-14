### 7.2 RotateIt

**전체 제목:** RotateIt: Tactile Rotary In-Hand Manipulation with Sim-to-Real Touch

**저자:** Haozhi Qi, Brent Yi, Sudharshan Suresh, Michael Lambeta, Yi Ma, Roberto Calandra, Jitendra Malik

**학회/연도:** CoRL 2023

**Hora/RotateIt/AnyRotate evolutionary chain:** Core RL (PPO+RMA) and hand (Allegro) unchanged from Hora; the primary contribution is the addition of DIGIT tactile sensing for rotation direction and slip detection. The RL algorithm, reward structure, and adaptation mechanism are inherited from Hora.

**RL 알고리즘:** PPO with tactile-informed policy; extends Hora with tactile sensing (DIGIT sensors) for rotation direction and slip detection

**핸드 하드웨어:** Allegro Hand (16 DoF) + DIGIT tactile sensors on fingertips

**시뮬레이션 플랫폼:** IsaacGym

**Sim2Real 여부:** Yes; sim-to-real with tactile domain randomization (real). Calibrates simulated tactile signals to real DIGIT sensor outputs, enabling zero-shot transfer of tactile-conditioned policies

**객체 수:** Evaluated on diverse objects; specific count not reported but includes geometrically varied objects

**작업:** Tactile-guided in-hand rotation; continuous rotation of objects using fingertip tactile feedback for slip detection and rotation direction sensing

**핵심 방법론:** Augments the Hora framework with DIGIT optical tactile sensors on the Allegro Hand fingertips. A tactile encoder processes simulated tactile images alongside proprioceptive state. The key insight is that tactile sensing provides direct contact information that disambiguates object state more reliably than proprioception alone, particularly for detecting rotational slip. Tactile sim-to-real is addressed via randomized tactile signal augmentation.

**주요 기여:**
- First integration of optical tactile sensing (DIGIT) with RL-based in-hand rotation on a real dexterous hand (real)
- Tactile sim-to-real transfer pipeline with calibrated DIGIT simulation
- Demonstrated that tactile feedback improves rotation robustness over proprioception-only baselines (Hora)

**한계점:** Still limited to single-axis rotation; DIGIT sensors add cost and fragility; tactile sim-to-real gap remains (simulated tactile is simplified compared to real optical signals); limited to rigid objects

## 추론 / 배포

- **추론 지연 시간:** Not explicitly reported. The tactile-conditioned MLP policy runs in <1ms per forward pass. Tactile image processing (DIGIT sensor) adds minor overhead.
- **배포 하드웨어:** Allegro Hand (16 DoF) + DIGIT tactile sensors. Policy trained in IsaacGym; deployed via zero-shot sim-to-real transfer.
- **실시간 가능 여부:** Yes. MLP-based policy with tactile conditioning is fast enough for real-time dexterous control on real hardware.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** No pre-collected dataset. Pure RL (PPO) with tactile-informed policy -- all data generated in simulation with sim-to-real transfer.
- **수집 방법:** Pure RL in IsaacGym extending Hora framework. Tactile encoder processes simulated DIGIT tactile images alongside proprioceptive state. Tactile sim-to-real via randomized tactile signal augmentation and DIGIT calibration.
- **데이터 규모:** Standard parallel RL training in IsaacGym. Diverse objects evaluated.
- **원격 조작 장비:** Not applicable (pure RL, no demonstrations).
- **데이터 포맷:** Not applicable (online RL, no offline dataset).
- **공개 여부:** Code release status not reported.
