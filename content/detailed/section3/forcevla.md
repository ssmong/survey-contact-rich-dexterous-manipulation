## 3.1 ForceVLA

- **Full title:** ForceVLA: Towards Force-Aware Vision-Language-Action Model for Contact-Rich Manipulation
- **Authors:** Qiaojun Yu et al. (SJTU, Fudan University)
- **Venue/Year:** NeurIPS 2025
- **arXiv:** https://arxiv.org/abs/2505.22159

**Force/tactile input type:** 6-axis force/torque (F/T) sensor mounted at the wrist of a Flexiv Rizon arm. The raw F/T signals (Fx, Fy, Fz, Tx, Ty, Tz) are tokenized and fed into the VLA backbone alongside visual tokens.

**Force/impedance output:** No. Position-only output. The force information is used as input context to improve policy decisions, but the robot executes position commands through the Flexiv Rizon's built-in controller.

> **Limitation (position-only output):** Position-only output; the policy cannot actively regulate contact forces despite receiving force/tactile input.

**Robot platform:** Flexiv Rizon 4 robotic arm + parallel-jaw gripper.

> **Limitation (gripper-only):** Evaluated only on parallel-jaw grippers; not validated on multi-finger dexterous hands.

**Tasks:** 5 contact-rich manipulation tasks -- plug insertion, surface wiping, tape peeling, cup stacking with force-sensitive alignment, and eraser wiping. All tasks require interpreting contact forces to determine task progress or adjust motion.

**Key methodology:** ForceVLA extends a pretrained VLA (based on the OpenVLA architecture) by introducing a force tokenizer that converts continuous 6-axis F/T readings into discrete tokens compatible with the VLM's vocabulary. Force tokens are interleaved with vision and language tokens in the transformer's input sequence. The model is fine-tuned end-to-end on a small dataset of teleoperated demonstrations that include synchronized F/T recordings. A force-conditioned attention mechanism allows the model to attend to force history when generating the next action chunk.

**Architecture/Parameters:** Built on OpenVLA (7B parameters). The force tokenizer adds a lightweight MLP encoder that projects 6D F/T readings into the VLM's embedding space. Action output is position-based (7D: 6-DoF end-effector pose + gripper).

**Main contributions:**
- Proposes integrating 6-axis F/T sensing as an explicit input modality in a VLA, tokenizing continuous force readings into discrete tokens compatible with the VLM vocabulary.
- Demonstrates that force-aware VLAs significantly outperform vision-only VLAs on contact-rich tasks where visual cues alone are insufficient (e.g., determining insertion success from force feedback rather than visual occlusion).
- Releases a force-annotated manipulation dataset (ForceVLA-Data: 244 trajectories, ~140K steps) covering 5 contact-rich tasks with synchronized F/T data (available on HuggingFace).

**Limitations/Gaps:** Position-only output means the robot cannot actively regulate contact forces -- it relies on the Flexiv arm's built-in compliance. Limited to 5 tasks with a relatively small dataset. Single robot platform (Flexiv Rizon) with no cross-embodiment evaluation. The force tokenization approach discretizes continuous force signals, potentially losing high-frequency contact information.

**Code/data availability:** ForceVLA-Data dataset released on HuggingFace (244 trajectories). Whether model code (as distinct from data) is publicly released should be independently verified -- the primary public artifact is the dataset.

**Results:**

| Metric | Value |
|--------|-------|
| Success rate improvement over vision-only VLA | 15--30% across 5 tasks |
| Largest single-task gain | Plug insertion (force feedback essential for detecting successful mating) |
| Dataset size | 244 trajectories, ~140K steps |

## Inference / Deployment

- **Inference latency:** Not reported. The paper does not disclose per-step inference latency or control frequency. Built on the pi-zero framework with flow-based action generation.
- **Deployment hardware:** Training on 8x NVIDIA RTX 4090 GPUs. Flexiv Rizon 4 arm + parallel-jaw gripper for real-world deployment. Inference hardware not separately specified.
- **Real-time capable?** Not verified. Inference latency and control frequency are not disclosed in the paper or project page.

## Dataset / Data Collection

- **Dataset used:** ForceVLA-Data (custom dataset released with this work). Covers 5 contact-rich manipulation tasks with synchronized vision, proprioception, and force/torque signals.
- **Collection method:** Teleoperated demonstrations on Flexiv Rizon 4 arm with synchronized 6-axis F/T recording alongside visual and proprioceptive data.
- **Data scale:** 244 trajectories, ~140K steps across 5 tasks (plug insertion, surface wiping, tape peeling, cup stacking, eraser wiping).
- **Teleop equipment:** Not explicitly detailed. Teleoperation on Flexiv Rizon 4 with F/T sensor.
- **Data format:** Synchronized multi-modal data (vision + proprioception + 6-axis F/T). Specific file format not reported.
- **Publicly available?** Yes. ForceVLA-Data dataset released on HuggingFace (244 trajectories). Code and data available at project page (sites.google.com/view/forcevla2025).
