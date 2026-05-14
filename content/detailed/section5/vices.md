### 5.3 VICES

**Full title:** Variable Impedance Control in End-Effector Space: An Action Space for Reinforcement Learning in Contact-Rich Tasks

**Authors:** Roberto Martin-Martin, Michelle A. Lee, Rachel Gardner, Silvio Savarese, Jeannette Bohg, Animesh Garg (Stanford / NVIDIA)

**Venue/Year:** IROS 2019

**How K/D are determined:** Reinforcement learning (policy gradient methods). The RL policy directly outputs impedance parameters as part of the action space. The key insight is that parameterizing the action space as variable impedance in Cartesian end-effector space (rather than joint torques or position targets) dramatically improves RL sample efficiency and task success for contact-rich manipulation.

**What is output:** Cartesian end-effector stiffness K (diagonal) and damping D (diagonal), along with a desired end-effector pose. The full action is (desired_pose, K, D), which is executed by a Cartesian impedance controller. The policy outputs per-axis stiffness and damping values.

**Robot platform:** Franka Emika Panda / Sawyer + parallel-jaw grippers in simulation. No dexterous hand.

**Tasks:** Contact-rich manipulation in Robosuite (MuJoCo): door opening, peg insertion, nut threading, and lift-and-place with contact constraints. These tasks require modulating compliance during different contact phases.

**Key methodology:** VICES proposes variable impedance control in end-effector space (VICES) as an action space for RL. Rather than learning joint torques or position targets, the RL agent outputs desired Cartesian pose + diagonal K and D matrices. A Cartesian impedance controller converts these to joint torques. This action space encodes the physical structure of impedance control, making it easier for RL to discover contact-rich strategies: the agent can learn to be stiff when pushing and compliant when aligning. The paper demonstrates that this action space outperforms joint torque, joint position, and end-effector position action spaces across all tested contact-rich tasks.

**Architecture/Parameters:** Standard RL policy network (MLP, ~256-256 hidden units). Policy gradient algorithm (PPO or SAC). Action space: 6D desired pose + 6D diagonal K + 6D diagonal D = 18D total. Cartesian impedance controller as the low-level executor. Trained in Robosuite/MuJoCo.

**Main contributions:**
- Establishes variable impedance in end-effector space as a superior RL action space for contact-rich manipulation, outperforming position, velocity, and torque action spaces
- Demonstrates that encoding impedance structure in the action space improves sample efficiency and final performance for RL in contact-rich tasks
- Provides systematic comparison of action space choices for contact-rich RL, which has influenced subsequent work

**Limitations/Gaps:**
- No dexterous hand -- gripper only (Franka/Sawyer)
- Simulation only (Robosuite/MuJoCo) -- no real-robot validation
- Diagonal K and D only -- does not learn full (off-diagonal) impedance matrices
- RL sample efficiency, while improved over torque-space, is still substantial
- 2019 paper; RL algorithms and simulation fidelity have advanced significantly since

**Results:** VICES action space achieved higher success rates and faster convergence than joint torque, joint position, and Cartesian position action spaces on all four contact-rich tasks in Robosuite. Door opening: ~90% vs. ~50% (position space). Peg insertion: ~85% vs. ~30% (torque space). The learned impedance profiles showed interpretable patterns (e.g., low lateral stiffness during insertion search).

## Inference / Deployment

- **Inference latency:** Not reported. The policy is a standard MLP (~256-256 hidden units), which runs in <1ms per forward pass on any modern hardware. The bottleneck is the simulation step, not policy inference.
- **Deployment hardware:** Simulation only (Robosuite/MuJoCo). No real-robot deployment. Policy inference uses standard MLP, deployable on any hardware.
- **Real-time capable?** Yes, for the policy itself. MLP inference is trivially fast (<1ms). However, the system was only evaluated in simulation; real-time deployment on physical hardware was not demonstrated.

## Dataset / Data Collection

- **Dataset used:** No pre-collected dataset. Pure RL -- data generated through online interaction with simulation environments.
- **Collection method:** Pure RL (PPO or SAC) in Robosuite/MuJoCo simulation. No human demonstrations. The agent learns entirely from reward-driven exploration in simulated contact-rich tasks (path following, door opening, surface wiping, peg insertion).
- **Data scale:** Standard RL training scale (millions of simulation steps across parallel environments). Specific episode counts not reported.
- **Teleop equipment:** Not applicable (pure RL, no demonstrations).
- **Data format:** Not applicable (online RL, no offline dataset).
- **Publicly available?** Simulation environments are standard Robosuite tasks. No separate dataset release (pure RL).
