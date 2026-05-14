## 3.12 VLA-Touch

- **Full title:** VLA-Touch: Vision-Language-Action Model with Tactile Sensing for Contact-Rich Manipulation
- **Authors:** National University of Singapore (NUS) et al.
- **Venue/Year:** arXiv preprint, 2025
- **arXiv:** https://arxiv.org/abs/2507.17294

**Force/tactile input type:** GelSight vision-based tactile sensor providing high-resolution contact images.

**Force/impedance output:** No direct force output. Uses a residual correction mechanism -- the tactile signal drives a learned residual that corrects the base VLA's position-only action output. This provides implicit force-reactive behavior without explicit force targets.

> **Limitation (position-only output):** Position-only output; the policy cannot actively regulate contact forces despite receiving force/tactile input.

**Robot platform:** Robotic arm + parallel-jaw gripper equipped with GelSight sensors.

> **Limitation (gripper-only):** Evaluated only on parallel-jaw grippers; not validated on multi-finger dexterous hands.

**Tasks:** Contact-rich manipulation tasks requiring tactile feedback for success.

**Key methodology:** VLA-Touch uses a two-stage architecture: a pretrained VLA generates base position actions from vision and language, and a tactile residual module corrects these actions based on GelSight tactile images. The residual module is a lightweight network trained on contact-rich task data. The key insight is that the pretrained VLA provides good coarse motion plans from visual understanding, while the tactile residual provides fine-grained corrections during contact phases. This separation allows the system to leverage large-scale VLA pretraining without requiring tactile data during pretraining.

**Architecture/Parameters:** Two-stage: pretrained VLA (frozen or fine-tuned) + tactile residual correction network. The residual network is a lightweight CNN that processes GelSight images and outputs a position correction (delta) that is added to the VLA's base action.

**Main contributions:**
- Proposes a tactile residual correction approach that adds tactile reactivity to any pretrained VLA without modifying the VLA architecture or requiring tactile data during VLA pretraining.
- Releases code and model checkpoints (available on GitHub and HuggingFace), making it one of the most reproducible tactile VLA approaches.
- Demonstrates that a lightweight residual module can effectively bridge the gap between coarse VLA actions and fine-grained contact-rich requirements.

**Limitations/Gaps:** The residual correction is applied in position space, not force space -- the system cannot explicitly command desired forces. The two-stage design may introduce latency compared to end-to-end approaches. Limited to GelSight tactile sensors; generalization to other tactile modalities is not demonstrated.

**Results:** VLA-Touch improves success rates on contact-rich tasks compared to the base VLA without tactile input. Code and checkpoints are publicly available on GitHub and HuggingFace.

## Inference / Deployment

- **Inference latency:** Not reported. The two-stage design (pretrained VLA + tactile residual) may introduce additional latency compared to end-to-end approaches, but no specific latency figures are provided.
- **Deployment hardware:** Robotic arm + parallel-jaw gripper with GelSight sensors. Inference hardware not specified.
- **Real-time capable?** Not verified. The lightweight tactile residual network (CNN) should add minimal overhead to the base VLA inference, but no quantitative latency benchmarks are provided.

## Dataset / Data Collection

- **Dataset used:** Custom contact-rich manipulation task demonstrations with GelSight tactile data. The paper notes "the absence of large multi-modal datasets" as a challenge and designs an approach that does not require tactile data during VLA pretraining.
- **Collection method:** Demonstrations collected with GelSight vision-based tactile sensors for the tactile residual module training. The base VLA is pretrained on standard vision-language-action data.
- **Data scale:** Not reported.
- **Teleop equipment:** Not reported.
- **Data format:** Not reported.
- **Publicly available?** Yes. Code and model checkpoints released on GitHub and HuggingFace.
