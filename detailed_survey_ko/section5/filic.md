### 5.5 FILIC

**전체 제목:** FILIC: Force-Impedance Learning in Contact-Rich Manipulation

**저자:** (Tsinghua / HKUST)

**학회/연도:** arXiv preprint, 2025

**K/D 결정 방법:** Fixed K and fixed B (damping). FILIC does not learn impedance parameters -- instead, it uses a fixed impedance controller as the low-level executor and learns a transformer-based IL policy that outputs position and force targets for this fixed-impedance controller. The inclusion in section 5 is because the system explicitly operates within an impedance control framework, even though K and B are hand-tuned rather than learned.

**출력:** Position targets and force setpoints for a fixed-impedance controller running at 25 Hz. The impedance parameters (K, B) are constants set by the user, not outputs of the learned policy.

**로봇 플랫폼:** AIRBOT Play robot arm. Evaluated in both MuJoCo simulation and real hardware. No dexterous hand.

**작업:** Contact-rich manipulation tasks: surface wiping, insertion, and force-regulated assembly tasks requiring consistent contact force maintenance.

**핵심 방법론:** FILIC uses a transformer-based imitation learning policy that predicts both position targets and desired contact forces at 25 Hz. These targets are executed by a fixed-impedance controller that regulates the interaction. The key contribution is the architecture for jointly predicting position and force targets from visual and proprioceptive input, rather than learning impedance parameters themselves. The fixed-impedance controller provides a stable execution framework, while the learned policy handles task-level planning and force setpoint generation.

**아키텍처/파라미터:** Transformer-based IL policy (encoder-decoder). Visual encoder for image observations. 25 Hz control frequency. Fixed Cartesian impedance controller with hand-tuned K and B. Trained on teleoperation demonstrations. MuJoCo for simulation evaluation, AIRBOT Play for real evaluation.

**주요 기여:**
- Demonstrates that learning force targets within a fixed-impedance framework can achieve contact-rich manipulation without learning impedance parameters
- Provides a practical architecture for joint position-force target prediction via imitation learning
- Evaluates in both simulation (MuJoCo) and real hardware (AIRBOT Play)

**한계점:**
- K and B are fixed (hand-tuned), not learned -- the system does not adapt impedance to the task
- No dexterous hand -- arm + gripper only
- 25 Hz control frequency is relatively slow for contact-rich tasks
- Does not generalize impedance across task types; different tasks require re-tuning K/B
- Fixed impedance limits performance in tasks requiring varying compliance (e.g., stiff insertion + compliant search)

**결과:** FILIC achieved higher success rates than position-only IL baselines on contact-rich tasks, demonstrating the value of force target prediction even with fixed impedance. Real-robot results on AIRBOT Play confirmed simulation findings. Code at github.com/OpenGHz/FILIC.

## 추론 / 배포

- **추론 지연 시간:** Policy runs at 25 Hz control frequency (40ms per step). This is explicitly stated in the paper as the operating frequency for position and force target prediction.
- **배포 하드웨어:** AIRBOT Play robot arm for real-robot evaluation; MuJoCo for simulation. Specific GPU for transformer policy inference not reported.
- **실시간 가능 여부:** Yes, at 25 Hz. The transformer-based IL policy generates position and force targets at 25 Hz, which is adequate for the tested contact-rich tasks, though relatively slow compared to typical impedance controller rates (100-1000 Hz).

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** Custom teleoperation demonstrations in simulation (MuJoCo) and on real hardware (AIRBOT Play 6-DoF arm).
- **수집 방법:** Teleoperation with force feedback. Simulation: haptic-feedback handheld controller with force visualization; 150 trajectories (50 single-shot insertions without contact, 100 with corrective motions) for peg-in-hole with 0.95 cm peg into 1 cm hole. Real-world: VR-based teleoperation with AR force vector visualization; 30 trajectories (10 single-shot, 20 with corrective actions) for charging plug insertion. Hole offset randomly perturbed by 1 mm during simulation collection.
- **데이터 규모:** 150 trajectories (simulation), 30 trajectories (real-world). Each trajectory includes RGB images (dual camera), joint positions/velocities/torques, EE Cartesian poses, external wrenches (6-DoF F/T), and operator commands.
- **원격 조작 장비:** Haptic-feedback handheld controller with vibrotactile feedback (simulation); VR headset with real-time AR force vector display (real-world).
- **데이터 포맷:** Not explicitly specified. Sampling rates: 25 Hz (policy), 250 Hz (control), 2 kHz (torque commands).
- **공개 여부:** Code at https://github.com/TATP-233/FILIC. Dataset release status not explicitly mentioned.
