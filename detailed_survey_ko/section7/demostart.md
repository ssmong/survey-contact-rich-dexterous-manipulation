### 7.4 DemoStart

**전체 제목:** DemoStart: Demonstration-Bootstrapped Autonomous Reinforcement Learning for Dexterous Manipulation

**저자:** Nick Heppert, Constantinos Chamzas, et al. (Google DeepMind)

**학회/연도:** ICRA 2025 (submitted 2024)

**arXiv:** https://arxiv.org/abs/2409.06613

**RL 알고리즘:** Demonstration-bootstrapped autonomous RL. Uses a small number of teleoperated demonstrations to initialize the replay buffer, then continues training with autonomous RL (SAC-based). Automatic reset mechanisms enable continuous real-world training.

**핸드 하드웨어:** DEX-EE (3-finger dexterous end-effector, custom Google DeepMind hardware)

**시뮬레이션 플랫폼:** MuJoCo (for initial prototyping); primary training done on real hardware

**Sim2Real 여부:** Yes -- but the emphasis is on real-world RL rather than sim-to-real transfer. Demonstrations bootstrap real-world learning, and the robot trains autonomously in the real world with automatic resets (real).

**작업:** (1) Plug insertion -- grasping a plug and inserting it into a socket (contact-rich, tight tolerances); (2) Cube reorientation -- in-hand rotation of a cube to target orientations. Both tasks require precise dexterous control.

**핵심 방법론:** DemoStart addresses the sample efficiency problem of real-world RL for dexterous manipulation. Instead of sim-to-real transfer (which introduces a reality gap), DemoStart bootstraps learning with a handful of teleoperated demonstrations, then lets the robot train autonomously in the real world. Automatic reset mechanisms (scripted return-to-home behaviors) enable hours of unattended training. This approach avoids the sim-to-real gap entirely while using demonstrations to overcome the initial exploration challenge.

**주요 기여:**
- Demonstrated autonomous real-world RL for dexterous manipulation, avoiding the sim-to-real gap entirely (real)
- Showed that a small number of demonstrations (5-10) can bootstrap effective exploration for contact-rich tasks
- Achieved high success rates on plug insertion and cube reorientation through real-world training (real)

**한계점:** Requires custom hardware (DEX-EE) with automatic resets -- not easily reproducible. Real-world training is slow (hours of robot time per task). Limited to 2 tasks. The DEX-EE is a 3-finger hand with fewer DoF than full dexterous hands (Shadow, Allegro). Code not publicly available.

**결과:** Achieved high success rates on both tasks after autonomous real-world training (real). Demonstrated that demo-bootstrapped real-world RL is competitive with sim-to-real approaches on these tasks.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** Small set of teleoperated demonstrations (5-10 per task) to bootstrap autonomous RL. No large pre-collected dataset.
- **수집 방법:** RL + human demos (DAPG-style, but real-world). A small number of teleoperated demonstrations (5-10) initialize the replay buffer, then autonomous RL (SAC-based) continues training in the real world with automatic resets. Primarily trained on real hardware (DEX-EE 3-finger hand), not sim-to-real transfer. MuJoCo used for initial prototyping only.
- **데이터 규모:** 5-10 demonstrations per task for bootstrapping. Hours of autonomous real-world RL training per task. 2 tasks (plug insertion, cube reorientation).
- **원격 조작 장비:** Teleoperation interface for DEX-EE (specific device not reported; Google DeepMind custom hardware).
- **데이터 포맷:** Real-world replay buffer (states, actions, rewards) from autonomous RL training.
- **공개 여부:** No. Code not publicly available. Custom Google DeepMind hardware (DEX-EE) limits reproducibility.

## 추론 / 배포

- **추론 지연 시간:** Not explicitly reported. The SAC-based policy (MLP) runs in <1ms per forward pass. Primary training is on real hardware (not sim-to-real).
- **배포 하드웨어:** DEX-EE (3-finger dexterous end-effector, custom Google DeepMind hardware). Trained primarily on real hardware with autonomous RL and automatic resets.
- **실시간 가능 여부:** Yes. Real-world RL training and deployment both require real-time policy execution. Demonstrated on real DEX-EE hardware.
