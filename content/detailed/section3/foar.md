## 3.13 FoAR

> **Note:** This is not a VLA (no language conditioning). Included in Section 3 for its force-output methodology, which is directly relevant to force-aware manipulation policy design.

- **Full title:** FoAR: Force-Aware Reactive Policy for Contact-Rich Robotic Manipulation
- **Authors:** Alan Heoooh et al. (SJTU)
- **Venue/Year:** RA-L / IROS 2025
- **arXiv:** https://arxiv.org/abs/2411.15753

**Force/tactile input type:** 6-axis F/T sensor mounted at the wrist (Flexiv Rizon's built-in sensor).

**Force/impedance output:** No. Position-only output. The force is used as input for reactive behavior but the robot executes position commands.

> **Limitation (position-only output):** Position-only output; the policy cannot actively regulate contact forces despite receiving force/tactile input.

**Robot platform:** Flexiv Rizon robotic arm + parallel-jaw gripper.

> **Limitation (gripper-only):** Evaluated only on parallel-jaw grippers; not validated on multi-finger dexterous hands.

**Tasks:** Surface wiping and tape/vegetable peeling -- tasks requiring maintaining contact with a surface while moving along it.

**Key methodology:** FoAR is a force-aware reactive policy that uses real-time F/T feedback to generate reactive position adjustments. The policy is trained via imitation learning on demonstrations that include synchronized F/T readings. A key design choice is the use of a force-conditioned action representation where the F/T signal modulates the action output through a gating mechanism -- when contact forces are within acceptable ranges, the policy follows the nominal trajectory; when forces deviate, the policy generates corrective motions. This enables the robot to maintain desired contact during wiping and peeling tasks even when the surface geometry is uncertain.

**Architecture/Parameters:** Transformer-based reactive policy with force conditioning. The model processes a history of F/T readings alongside visual observations and generates position-only action chunks. The force gating mechanism is implemented as a learned attention-weighted fusion.

**Main contributions:**
- Introduces a force-conditioned reactive policy that generates real-time corrective motions based on F/T feedback, enabling robust contact maintenance.
- Demonstrates effective wiping and peeling behaviors that generalize across surface geometries, where maintaining consistent contact force is critical.
- Releases code publicly (GitHub), enabling reproducibility.

**Limitations/Gaps:** Not a full VLA model -- FoAR uses force and vision but does not include language conditioning. Position-only output limits the ability to explicitly regulate contact forces. Evaluated on only 2 task types (wiping and peeling). Limited to a single robot platform.

**Results:** FoAR achieves robust contact-rich manipulation on wiping and peeling tasks, maintaining consistent contact forces through reactive position adjustments. The force-conditioned policy significantly outperforms vision-only baselines on these tasks. Code available at GitHub (github.com/Alan-Heoooh/FoAR).

## Inference / Deployment

- **Inference latency:** Policy operates at approximately **10 Hz** for action prediction (action horizon of 20 steps). F/T data is sampled at 100 Hz (high-frequency sensing). Diffusion model uses 20 DDIM iterations for inference.
- **Deployment hardware:** Training on 2x NVIDIA A100 GPUs. Inference/deployment on Intel Core i9-10900K CPU + NVIDIA RTX 3090 GPU. Flexiv Rizon arm for real-world execution.
- **Real-time capable?** Yes, at 10 Hz with temporal ensemble buffering. The 10 Hz action prediction rate with DDIM-based diffusion is sufficient for the wiping and peeling tasks evaluated, though the DDIM iterations add latency compared to direct policy inference.

## Dataset / Data Collection

- **Dataset used:** Custom demonstration dataset for surface wiping and tape/vegetable peeling tasks on Flexiv Rizon arm. No named benchmark.
- **Collection method:** Teleoperated demonstrations with synchronized 6-axis F/T recording (100 Hz) and visual observations. F/T data from the Flexiv Rizon's built-in wrist sensor.
- **Data scale:** Not reported.
- **Teleop equipment:** Not explicitly detailed. Teleoperation on Flexiv Rizon arm with built-in wrist F/T sensor.
- **Data format:** Not reported.
- **Publicly available?** Code released at [GitHub](https://github.com/Alan-Heoooh/FoAR). Whether demonstration data is included in the release is not confirmed. Project page at tonyfang.net/FoAR/.
