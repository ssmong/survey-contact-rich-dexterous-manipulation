## 3.2 ForceVLA2

- **Full title:** ForceVLA2: Towards Force-Aware Vision-Language-Action Model with Hybrid Force-Position Prediction
- **Authors:** Shanghai AI Lab et al.
- **Venue/Year:** CVPR 2026
- **arXiv:** https://arxiv.org/abs/2603.15169

**Force/tactile input type:** 6-axis F/T sensor at 300 Hz sampling rate. High-frequency force signals are processed through a temporal encoder before being fused with visual and language tokens.

**Force/impedance output:** Yes -- hybrid force/position output. The model predicts both position targets and desired contact forces. A predicted force signal is output alongside position commands, enabling a hybrid force-position controller at execution time. **Force output type: full wrench (6D).**

**Robot platform:** Flexiv Rizon 4s robotic arm + parallel-jaw gripper.

> **Limitation (gripper-only):** Evaluated only on parallel-jaw grippers; not validated on multi-finger dexterous hands.

**Tasks:** 5 contact-rich tasks including pressing, surface cleaning, gear assembly, insertion, and force-sensitive alignment tasks.

**Key methodology:** ForceVLA2 extends the ForceVLA paradigm by adding force prediction to the output space. The model uses a dual-head architecture where one head generates position targets and another predicts the expected interaction forces. At inference time, a hybrid force-position controller uses the predicted force as a feedforward term alongside position tracking. The 300 Hz F/T input is processed through a temporal convolution network to extract force features at a frequency compatible with the VLA's inference rate (~10 Hz), creating a multi-scale temporal representation of contact dynamics.

**Architecture/Parameters:** VLA backbone with dual action heads (position head and force prediction head). The force prediction head outputs 6D wrench targets that are used by a low-level hybrid force-position controller.

**Main contributions:**
- One of the earliest VLAs to produce explicit force targets as part of the action output, enabling active force regulation rather than passive compliance.
- Introduces a high-frequency force temporal encoder (300 Hz input) that bridges the gap between fast contact dynamics and the slower VLA inference loop.
- Demonstrates that hybrid force-position output improves performance on tasks requiring precise force control (e.g., gear assembly, cleaning with controlled pressure).

**Limitations/Gaps:** Code and weights marked as "coming soon" with no public release as of May 2026. Single robot platform (Flexiv). The hybrid controller still relies on a tuned low-level controller to execute the force targets. Limited task diversity (5 tasks). The approach has not been validated on dexterous hands.

**Results:** Improved success rates over ForceVLA on contact-rich tasks, particularly on gear assembly and cleaning tasks where force regulation is critical. Specific numerical improvements reported over position-only baselines on all 5 tasks.

## Inference / Deployment

- **Inference latency:** **15 Hz** inference speed (~67 ms per action step) with a chunk size of 30, on NVIDIA RTX 4090 GPU.
- **Deployment hardware:** NVIDIA RTX 4090 GPU for inference. Flexiv Rizon 4s arm + parallel-jaw gripper for real-world deployment. F/T sensor sampled at 300 Hz.
- **Real-time capable?** Yes. 15 Hz on RTX 4090 is sufficient for reactive manipulation tasks requiring hybrid force-position control. The 67 ms per step allows the system to process observations and generate hybrid force-position commands with adequate responsiveness for contact-rich interactions.

## Dataset / Data Collection

- **Dataset used:** ForceVLA2-Dataset (custom dataset released with this work).
- **Collection method:** Teleoperated demonstrations on Flexiv Rizon 4s arm with synchronized high-frequency (300 Hz) 6-axis F/T recording alongside multi-view images, task prompts, and proprioceptive state.
- **Data scale:** 1,000 trajectories across 5 contact-rich tasks (wiping, pressing, assembling, and others).
- **Teleop equipment:** Not explicitly detailed. Teleoperation on Flexiv Rizon 4s with 300 Hz F/T sensor.
- **Data format:** Multi-modal: multi-view images, task prompts, proprioceptive state, and force signals. Specific file format not reported.
- **Publicly available?** Code and weights marked as "coming soon" with no public release as of May 2026. Project page referenced but data release status not confirmed.
