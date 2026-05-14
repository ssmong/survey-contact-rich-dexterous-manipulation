### 7.4 DemoStart

**Full title:** DemoStart: Demonstration-Bootstrapped Autonomous Reinforcement Learning for Dexterous Manipulation

**Authors:** Nick Heppert, Constantinos Chamzas, et al. (Google DeepMind)

**Venue/Year:** ICRA 2025 (submitted 2024)

**arXiv:** https://arxiv.org/abs/2409.06613

**RL algorithm:** Demonstration-bootstrapped autonomous RL. Uses a small number of teleoperated demonstrations to initialize the replay buffer, then continues training with autonomous RL (SAC-based). Automatic reset mechanisms enable continuous real-world training.

**Hand hardware:** DEX-EE (3-finger dexterous end-effector, custom Google DeepMind hardware)

**Sim platform:** MuJoCo (for initial prototyping); primary training done on real hardware

**Sim2Real?** Yes -- but the emphasis is on real-world RL rather than sim-to-real transfer. Demonstrations bootstrap real-world learning, and the robot trains autonomously in the real world with automatic resets (real).

**Tasks:** (1) Plug insertion -- grasping a plug and inserting it into a socket (contact-rich, tight tolerances); (2) Cube reorientation -- in-hand rotation of a cube to target orientations. Both tasks require precise dexterous control.

**Key methodology:** DemoStart addresses the sample efficiency problem of real-world RL for dexterous manipulation. Instead of sim-to-real transfer (which introduces a reality gap), DemoStart bootstraps learning with a handful of teleoperated demonstrations, then lets the robot train autonomously in the real world. Automatic reset mechanisms (scripted return-to-home behaviors) enable hours of unattended training. This approach avoids the sim-to-real gap entirely while using demonstrations to overcome the initial exploration challenge.

**Main contributions:**
- Demonstrated autonomous real-world RL for dexterous manipulation, avoiding the sim-to-real gap entirely (real)
- Showed that a small number of demonstrations (5-10) can bootstrap effective exploration for contact-rich tasks
- Achieved high success rates on plug insertion and cube reorientation through real-world training (real)

**Limitations/Gaps:** Requires custom hardware (DEX-EE) with automatic resets -- not easily reproducible. Real-world training is slow (hours of robot time per task). Limited to 2 tasks. The DEX-EE is a 3-finger hand with fewer DoF than full dexterous hands (Shadow, Allegro). Code not publicly available.

**Results:** Achieved high success rates on both tasks after autonomous real-world training (real). Demonstrated that demo-bootstrapped real-world RL is competitive with sim-to-real approaches on these tasks.

## Dataset / Data Collection

- **Dataset used:** Small set of teleoperated demonstrations (5-10 per task) to bootstrap autonomous RL. No large pre-collected dataset.
- **Collection method:** RL + human demos (DAPG-style, but real-world). A small number of teleoperated demonstrations (5-10) initialize the replay buffer, then autonomous RL (SAC-based) continues training in the real world with automatic resets. Primarily trained on real hardware (DEX-EE 3-finger hand), not sim-to-real transfer. MuJoCo used for initial prototyping only.
- **Data scale:** 5-10 demonstrations per task for bootstrapping. Hours of autonomous real-world RL training per task. 2 tasks (plug insertion, cube reorientation).
- **Teleop equipment:** Teleoperation interface for DEX-EE (specific device not reported; Google DeepMind custom hardware).
- **Data format:** Real-world replay buffer (states, actions, rewards) from autonomous RL training.
- **Publicly available?** No. Code not publicly available. Custom Google DeepMind hardware (DEX-EE) limits reproducibility.

## Inference / Deployment

- **Inference latency:** Not explicitly reported. The SAC-based policy (MLP) runs in <1ms per forward pass. Primary training is on real hardware (not sim-to-real).
- **Deployment hardware:** DEX-EE (3-finger dexterous end-effector, custom Google DeepMind hardware). Trained primarily on real hardware with autonomous RL and automatic resets.
- **Real-time capable?** Yes. Real-world RL training and deployment both require real-time policy execution. Demonstrated on real DEX-EE hardware.
