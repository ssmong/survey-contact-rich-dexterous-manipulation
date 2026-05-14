### 5.4 CHIP

**Full title:** CHIP: Contact Handling with Impedance Perturbation for Robust Humanoid Control

**Authors:** NVIDIA NVLabs

**Venue/Year:** ICRA 2025

**How K/D are determined:** Reinforcement learning (PPO) with hindsight impedance perturbation. The RL agent learns a policy that outputs end-effector stiffness as part of the action space. The key innovation is "hindsight perturbation": during training, the simulator retroactively applies perturbations to the impedance parameters of successful trajectories and checks whether they would still have succeeded, creating a curriculum that teaches the policy to select robust impedance values.

**What is output:** End-effector (EE) stiffness values (scalar or low-dimensional stiffness per EE). Damping is not independently output (derived or fixed). The policy also outputs desired EE positions for the humanoid's arms.

**Robot platform:** Simulated humanoid robot, 35 DoF (whole-body). Not a standalone dexterous hand, though the humanoid has integrated hand structures. Evaluated in NVIDIA Isaac Sim.

**Tasks:** Contact-rich whole-body humanoid manipulation: object grasping with body contacts, pushing large objects, opening heavy doors, and tasks where the humanoid uses its arms and body to brace against contact forces.

**Key methodology:** CHIP addresses the problem that standard RL for humanoid contact often produces brittle policies -- policies that work only with specific impedance values. The hindsight perturbation technique generates diverse training data: after a trajectory succeeds, CHIP retroactively varies the impedance parameters and re-simulates to find the range of impedance values that still lead to success. This expands the training distribution and teaches the policy to output impedance values that are robust to perturbations. The result is a policy that generalizes across contact conditions without requiring extensive domain randomization of impedance parameters.

**Architecture/Parameters:** PPO-trained policy network (MLP). 35-DoF humanoid in Isaac Sim. Action space includes desired EE positions + EE stiffness. Hindsight perturbation module runs additional forward simulations during training to augment the replay buffer. Trained with GPU-parallelized Isaac Sim environments.

**Main contributions:**
- Hindsight impedance perturbation: a novel training technique that retroactively perturbs impedance parameters of successful trajectories to learn robust impedance selection
- Demonstrates that learned EE stiffness enables humanoids to handle diverse contact scenarios more robustly than fixed-impedance policies
- Combines whole-body humanoid RL with learned impedance control for contact-rich tasks

**Limitations/Gaps:**
- No standalone dexterous hand -- humanoid has integrated grippers, not multi-finger hands
- Simulation only (Isaac Sim) -- no real-robot transfer demonstrated
- EE stiffness is scalar or low-dimensional; does not learn full 6D impedance matrices
- Damping not independently learned
- Humanoid embodiment is specific; unclear how the approach transfers to other platforms
- Project page only (no public code repository)

**Results:** CHIP policies achieved higher contact-rich task success rates than fixed-impedance and unperturbed RL baselines across all tested humanoid manipulation tasks. The hindsight perturbation improved robustness to contact variations by 15-30% compared to standard PPO training.

## Inference / Deployment

- **Inference latency:** Not reported. The policy is a standard MLP, which runs in <1ms per forward pass. Training uses GPU-parallelized Isaac Sim environments.
- **Deployment hardware:** Simulation only (NVIDIA Isaac Sim). Training leverages NVIDIA GPUs for massively parallel simulation. No real-robot deployment demonstrated.
- **Real-time capable?** Yes, for inference. The MLP policy is trivially fast. However, the system was only evaluated in simulation; real-robot deployment with real-time impedance control was not demonstrated.

## Dataset / Data Collection

- **Dataset used:** No pre-collected dataset. Pure RL with hindsight impedance perturbation -- all data generated in simulation.
- **Collection method:** Pure RL (PPO) in NVIDIA Isaac Sim with GPU-parallelized environments. The hindsight perturbation technique generates additional training data by retroactively varying impedance parameters of successful trajectories and re-simulating. No human demonstrations.
- **Data scale:** Standard large-scale RL training in Isaac Sim (massively parallel GPU simulation). Specific episode counts not reported. Hindsight perturbation augments the effective dataset by re-simulating trajectories with perturbed impedance.
- **Teleop equipment:** Not applicable (pure RL, no demonstrations).
- **Data format:** Not applicable (online RL with hindsight augmentation, no offline dataset).
- **Publicly available?** No public code repository. Project page only.
