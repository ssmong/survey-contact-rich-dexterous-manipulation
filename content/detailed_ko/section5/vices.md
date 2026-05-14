### 5.3 VICES

**전체 제목:** Variable Impedance Control in End-Effector Space: An Action Space for Reinforcement Learning in Contact-Rich Tasks

**저자:** Roberto Martin-Martin, Michelle A. Lee, Rachel Gardner, Silvio Savarese, Jeannette Bohg, Animesh Garg (Stanford / NVIDIA)

**학회/연도:** IROS 2019

**K/D 결정 방법:** Reinforcement learning (policy gradient methods). The RL policy directly outputs impedance parameters as part of the action space. The key insight is that parameterizing the action space as variable impedance in Cartesian end-effector space (rather than joint torques or position targets) dramatically improves RL sample efficiency and task success for contact-rich manipulation.

**출력:** Cartesian end-effector stiffness K (diagonal) and damping D (diagonal), along with a desired end-effector pose. The full action is (desired_pose, K, D), which is executed by a Cartesian impedance controller. The policy outputs per-axis stiffness and damping values.

**로봇 플랫폼:** Franka Emika Panda / Sawyer + parallel-jaw grippers in simulation. No dexterous hand.

**작업:** Contact-rich manipulation in Robosuite (MuJoCo): door opening, peg insertion, nut threading, and lift-and-place with contact constraints. These tasks require modulating compliance during different contact phases.

**핵심 방법론:** VICES proposes variable impedance control in end-effector space (VICES) as an action space for RL. Rather than learning joint torques or position targets, the RL agent outputs desired Cartesian pose + diagonal K and D matrices. A Cartesian impedance controller converts these to joint torques. This action space encodes the physical structure of impedance control, making it easier for RL to discover contact-rich strategies: the agent can learn to be stiff when pushing and compliant when aligning. The paper demonstrates that this action space outperforms joint torque, joint position, and end-effector position action spaces across all tested contact-rich tasks.

**아키텍처/파라미터:** Standard RL policy network (MLP, ~256-256 hidden units). Policy gradient algorithm (PPO or SAC). Action space: 6D desired pose + 6D diagonal K + 6D diagonal D = 18D total. Cartesian impedance controller as the low-level executor. Trained in Robosuite/MuJoCo.

**주요 기여:**
- Establishes variable impedance in end-effector space as a superior RL action space for contact-rich manipulation, outperforming position, velocity, and torque action spaces
- Demonstrates that encoding impedance structure in the action space improves sample efficiency and final performance for RL in contact-rich tasks
- Provides systematic comparison of action space choices for contact-rich RL, which has influenced subsequent work

**한계점:**
- No dexterous hand -- gripper only (Franka/Sawyer)
- Simulation only (Robosuite/MuJoCo) -- no real-robot validation
- Diagonal K and D only -- does not learn full (off-diagonal) impedance matrices
- RL sample efficiency, while improved over torque-space, is still substantial
- 2019 paper; RL algorithms and simulation fidelity have advanced significantly since

**결과:** VICES action space achieved higher success rates and faster convergence than joint torque, joint position, and Cartesian position action spaces on all four contact-rich tasks in Robosuite. Door opening: ~90% vs. ~50% (position space). Peg insertion: ~85% vs. ~30% (torque space). The learned impedance profiles showed interpretable patterns (e.g., low lateral stiffness during insertion search).

## 추론 / 배포

- **추론 지연 시간:** Not reported. The policy is a standard MLP (~256-256 hidden units), which runs in <1ms per forward pass on any modern hardware. The bottleneck is the simulation step, not policy inference.
- **배포 하드웨어:** Simulation only (Robosuite/MuJoCo). No real-robot deployment. Policy inference uses standard MLP, deployable on any hardware.
- **실시간 가능 여부:** Yes, for the policy itself. MLP inference is trivially fast (<1ms). However, the system was only evaluated in simulation; real-time deployment on physical hardware was not demonstrated.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** No pre-collected dataset. Pure RL -- data generated through online interaction with simulation environments.
- **수집 방법:** Pure RL (PPO or SAC) in Robosuite/MuJoCo simulation. No human demonstrations. The agent learns entirely from reward-driven exploration in simulated contact-rich tasks (path following, door opening, surface wiping, peg insertion).
- **데이터 규모:** Standard RL training scale (millions of simulation steps across parallel environments). Specific episode counts not reported.
- **원격 조작 장비:** Not applicable (pure RL, no demonstrations).
- **데이터 포맷:** Not applicable (online RL, no offline dataset).
- **공개 여부:** Simulation environments are standard Robosuite tasks. No separate dataset release (pure RL).
