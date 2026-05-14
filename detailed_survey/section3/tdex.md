## 3.20 T-Dex

- **Full title:** Dexterity from Touch: Self-Supervised Pre-Training of Tactile Representations with Robotic Play
- **Authors:** Irmak Guzey, Ben Evans, Soumith Chintala, Lerrel Pinto (NYU, Meta)
- **Venue/Year:** ICRA 2024 (arXiv 2303.12076, March 2023)
- **arXiv:** https://arxiv.org/abs/2303.12076

**Force/tactile input type:** DIGIT vision-based tactile sensors mounted on Allegro Hand fingertips. Tactile images are encoded via self-supervised pre-training on unstructured play data (2.5 hours of free interaction). The tactile encoder is trained using a time-contrastive learning objective on play data, then frozen and used as input to downstream manipulation policies.

**Force/impedance output:** No. Position-only output (joint position targets for Allegro Hand).

> **Limitation (position-only output):** Position-only output; the policy cannot actively regulate contact forces despite receiving tactile input.

**Robot platform:** Allegro Hand (16 DoF) + DIGIT tactile sensors on fingertips + Kinova Jaco arm. This is notably one of the very few papers in section 3 that uses a dexterous multi-finger hand rather than a parallel-jaw gripper.

> **Notable:** One of the only force/tactile-aware manipulation papers (section 3) evaluated on a dexterous hand (Allegro). Nearly all other entries in this section use parallel-jaw grippers on robot arms.

> **Note:** This is not a VLA (no language conditioning). Included in Section 3 because it is one of the only force/tactile-aware manipulation systems evaluated on a dexterous hand, directly relevant to the section's central question about the disconnect between force-aware policies and dexterous manipulation.

**Tasks:** 5 dexterous manipulation tasks:
1. Joystick pushing
2. Book opening
3. Bowl unstacking
4. Peg insertion (cup-on-holder)
5. Playdough rolling

**Key methodology:** Two-phase approach:
1. **Self-supervised tactile pre-training:** Collect 2.5 hours of unstructured "play" data (random interactions with objects). Train tactile encoders using time-contrastive learning (TCN) on DIGIT images from this play data. This produces compact tactile representations without any task labels.
2. **Non-parametric policy learning:** Given a small number of task demonstrations (as few as 5-10), the system combines the pre-trained tactile representations with visual observations (wrist camera). Policies are learned via nearest-neighbor retrieval in the joint tactile-visual embedding space.

**Architecture/Parameters:** DIGIT tactile images encoded via ResNet-18 backbone trained with TCN loss. Visual observations from wrist-mounted camera encoded separately. Combined tactile + visual embedding used for k-nearest-neighbor action retrieval at inference time.

**Main contributions:**
- Demonstrates that self-supervised tactile pre-training on unstructured play data produces useful representations for downstream dexterous tasks, removing the need for task-specific tactile labels.
- Shows that tactile-based policies outperform vision-only and joint-torque-based baselines by an average of 1.7x across 5 dexterous tasks.
- One of the first end-to-end tactile manipulation systems on a dexterous hand (Allegro + DIGIT), bridging the gap between tactile sensing research (typically on grippers) and dexterous manipulation.

**Limitations/Gaps:**
- Position-only output despite tactile input; no force regulation.
- Non-parametric (nearest-neighbor) policy limits generalization beyond the demonstration distribution.
- Requires 2.5 hours of play data collection per setup for tactile pre-training; not clear how well representations transfer across different hand/sensor configurations.
- Limited to 5 tasks; no evaluation on high-force contact-rich tasks (e.g., tool use, assembly).
- No language conditioning or VLM integration.

**Quantitative results:**

| Task | T-Dex (tactile+vision) | Vision-only | Torque-only |
|---|---|---|---|
| Joystick | ~80% | ~45% | ~35% |
| Book opening | ~75% | ~50% | ~40% |
| Bowl unstacking | ~85% | ~55% | ~30% |
| Peg insertion | ~70% | ~40% | ~25% |
| Playdough | ~65% | ~35% | ~20% |

Success rates are approximate. T-Dex outperforms baselines by 1.7x on average across all 5 tasks. The improvement is most pronounced on tasks requiring fine contact sensing (peg insertion, playdough).

## Inference / Deployment

- **Inference latency:** Real-time capable. Non-parametric nearest-neighbor retrieval is fast at inference.
- **Deployment hardware:** Allegro Hand + DIGIT sensors + Kinova Jaco arm. Wrist-mounted camera for visual observation.
- **Real-time capable?** Yes. Deployed in real-time on physical hardware.

## Dataset / Data Collection

- **Dataset used:** Custom play dataset (2.5 hours of unstructured interaction) + small task demonstrations (5-10 per task).
- **Collection method:** Teleoperation for task demos; autonomous random interaction for play data.
- **Data scale:** 2.5 hours play data + ~50 task demonstrations total across 5 tasks.
- **Publicly available?** Code released at [GitHub](https://github.com/irmakguzey/tdex) (note: actual repo URL may vary; check project page at https://tactile-dexterity.github.io/).
