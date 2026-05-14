### 7.2 AnyRotate

**전체 제목:** AnyRotate: Gravity-Invariant In-Hand Object Rotation with Sim-to-Real Touch

**저자:** Max Yang, Chenghua Lu, Alex Church, Yijiong Lin, Chris Li, Efi Psomopoulou, Nathan F. Lepora

**학회/연도:** CoRL 2024

**Hora/RotateIt/AnyRotate evolutionary chain:** Extends the Hora/RotateIt framework with gravity randomization; the RL algorithm (PPO+RMA) is inherited from Hora. The primary novelty is training across randomized gravity directions to enable rotation with any hand orientation, plus the finding that tactile sensing is essential for gravity-invariant rotation (proprioception-only fails in non-palm-up orientations).

**RL 알고리즘:** PPO with tactile-conditioned policy; extends tactile in-hand rotation to arbitrary gravity directions (gravity-invariant)

**핸드 하드웨어:** Allegro Hand (16 DoF) + tactile sensors (TacTip-based)

**시뮬레이션 플랫폼:** IsaacGym

**Sim2Real 여부:** Yes; sim-to-real with tactile domain randomization across varied hand orientations (real)

**객체 수:** Multiple objects evaluated in various orientations

**작업:** Gravity-invariant in-hand object rotation -- continuous rotation with the hand held at arbitrary orientations (palm-up, palm-down, sideways)

**핵심 방법론:** Addresses a key limitation of prior work (Hora, RotateIt) which assumes a palm-up hand configuration. Trains the rotation policy across randomized gravity directions relative to the hand, using tactile feedback to maintain stable contact regardless of gravity orientation. The tactile signal provides critical contact state information when gravity is not aligned with the palm, where proprioception alone is insufficient.

**주요 기여:**
- First gravity-invariant in-hand rotation policy, enabling rotation with any hand orientation (real)
- Demonstrated that tactile sensing is essential for gravity-invariant rotation (proprioception-only fails in non-palm-up orientations)
- Sim-to-real transfer across hand orientations not seen during real-world training (real)

**한계점:** Still single-axis rotation; limited object diversity in real-world evaluation; custom tactile sensor setup may not generalize to other sensor types; no code publicly released at time of survey

## 추론 / 배포

- **추론 지연 시간:** Not explicitly reported. The tactile-conditioned MLP policy runs in <1ms per forward pass.
- **배포 하드웨어:** Allegro Hand (16 DoF) + TacTip-based tactile sensors. Policy trained in IsaacGym; deployed via zero-shot sim-to-real transfer across varied hand orientations.
- **실시간 가능 여부:** Yes. MLP-based policy with tactile conditioning supports real-time control. Demonstrated on real Allegro Hand in multiple orientations.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** No pre-collected dataset. Pure RL (PPO) with tactile-conditioned policy and gravity randomization -- all data generated in simulation.
- **수집 방법:** Pure RL in IsaacGym extending Hora/RotateIt framework. Gravity direction randomized during training. Tactile feedback (TacTip-based) for contact state in varied hand orientations. Sim-to-real via tactile domain randomization.
- **데이터 규모:** Standard parallel RL training in IsaacGym. Multiple objects in various orientations.
- **원격 조작 장비:** Not applicable (pure RL, no demonstrations).
- **데이터 포맷:** Not applicable (online RL, no offline dataset).
- **공개 여부:** No code publicly released at time of survey.
