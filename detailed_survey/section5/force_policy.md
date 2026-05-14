### 5.9 Force Policy

**Full title:** Force Policy: Learning Contact-Rich Manipulation from Force Demonstrations

**Authors:** (SJTU / Flexiv Robotics)

**Venue/Year:** RSS 2026

> **Note:** This paper uses hybrid position-force control, not impedance control. Included for topical proximity to force-aware manipulation.

**How K/D are determined:** Imitation learning from teleoperation demonstrations that capture force profiles. The learned policy outputs force targets (desired interaction wrenches), not impedance parameters directly. The system operates in a hybrid position-force control framework where the learned force targets complement position trajectories.

**What is output:** Force/wrench targets along task-relevant axes, predicted by the IL policy. These are desired interaction forces, not stiffness or damping matrices. A low-level hybrid position-force controller executes the combined position + force targets.

**Robot platform:** Flexiv Rizon arm + parallel-jaw gripper. Real-robot only (no simulation). No dexterous hand.

**Tasks:** Contact-rich manipulation tasks requiring precise force regulation: plug insertion, surface wiping with controlled contact force, gear assembly, object polishing. These tasks require maintaining specific force profiles during contact.

**Key methodology:** Force Policy learns to predict desired interaction forces from teleoperation demonstrations where the demonstrator's applied forces are captured via the Flexiv Rizon's built-in F/T sensing. The IL policy takes visual and proprioceptive input and outputs both position targets and force targets at each timestep. A hybrid position-force controller executes the combined targets: position control in unconstrained directions and force control in constrained (contact) directions. The key contribution is demonstrating that learning force targets from demonstrations is more effective than learning position-only targets for contact-rich tasks.

**Architecture/Parameters:** Transformer-based IL policy for joint position-force target prediction. Flexiv Rizon's integrated 6-axis F/T sensing for demonstration capture. Hybrid position-force controller for execution. Real-robot only -- no simulation training or evaluation.

**Main contributions:**
- Demonstrates force-target learning from teleoperation demonstrations for contact-rich manipulation
- Shows that explicit force prediction outperforms position-only imitation for tasks requiring force regulation
- Real-robot evaluation on industrially relevant tasks (insertion, assembly, polishing)

**Limitations/Gaps:**
- No dexterous hand -- Flexiv arm + gripper
- Real-robot only; no simulation for reproducibility or ablation
- Outputs force targets, not impedance parameters -- does not enable variable compliance
- No code or weights released
- Force demonstrations require force-sensing teleoperation setup (Flexiv-specific)
- Does not learn impedance; the hybrid controller's impedance parameters are fixed

**Results:** Force Policy achieved higher success rates than position-only IL and fixed-force baselines on all tested contact-rich tasks. Force tracking accuracy during insertion tasks improved significantly compared to position-only approaches. Real-robot demonstrations on the Flexiv Rizon confirmed practical applicability.

## Inference / Deployment

- **Inference latency:** Not explicitly reported. The transformer-based IL policy predicts position and force targets per timestep. Specific control frequency not stated, but the Flexiv Rizon supports high-frequency force control; the learned policy likely operates at 10-50 Hz.
- **Deployment hardware:** Flexiv Rizon arm with integrated 6-axis F/T sensing. Real-robot only evaluation. GPU for policy inference not specified.
- **Real-time capable?** Yes, likely. The system was demonstrated on real hardware (Flexiv Rizon) for contact-rich tasks requiring force regulation, implying real-time operation. The hybrid position-force controller runs at the robot's native control rate; the learned policy provides targets at a lower frequency.

## Dataset / Data Collection

- **Dataset used:** Custom teleoperation demonstrations collected on Flexiv Rizon arm with integrated F/T sensing.
- **Collection method:** Teleoperation with force capture. Demonstrator's applied forces recorded via Flexiv Rizon's built-in 6-axis F/T sensor during contact-rich tasks (plug insertion, surface wiping, gear assembly, polishing). Real-robot only -- no simulation.
- **Data scale:** Not explicitly reported. Number of demonstrations per task not disclosed in available materials.
- **Teleop equipment:** Flexiv Rizon's native teleoperation interface with integrated 6-axis F/T sensing for force capture during demonstrations.
- **Data format:** Joint position-force target trajectories with F/T sensor readings. Specific file format not reported.
- **Publicly available?** No. No code or weights released.
