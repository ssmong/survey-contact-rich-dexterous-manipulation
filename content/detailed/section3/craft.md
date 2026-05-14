## 3.11 CRAFT

- **Full title:** CRAFT: Contact-Rich Affordance-aware Force-guided Transformer for Manipulation
- **Authors:** Not specified in survey table
- **Venue/Year:** arXiv preprint, 2026
- **arXiv:** https://arxiv.org/abs/2602.12532

**Force/tactile input type:** Force sensing (specific sensor type not detailed in the survey table).

**Force/impedance output:** No. Position-only output.

> **Limitation (position-only output):** Position-only output; the policy cannot actively regulate contact forces despite receiving force/tactile input.

**Robot platform:** Teleoperated robotic arm.

> **Limitation (gripper-only):** Evaluated only on parallel-jaw grippers; not validated on multi-finger dexterous hands.

**Tasks:** Deformable object manipulation and alignment tasks that require contact-rich interactions.

**Key methodology:** CRAFT integrates force information with contact affordance reasoning within a transformer-based policy. The model learns to predict contact affordances (where and how to make contact) conditioned on force feedback, enabling force-guided manipulation of deformable objects and precise alignment. The affordance prediction module identifies task-relevant contact regions, and the force-guided transformer generates actions that achieve desired contact states. This approach is particularly suited for tasks where the contact geometry changes during manipulation (e.g., deformable objects).

**Architecture/Parameters:** Transformer-based policy with affordance prediction module and force encoder. The architecture combines contact affordance reasoning with force-conditioned action generation.

**Main contributions:**
- Combines contact affordance prediction with force-guided action generation, providing a structured approach to contact-rich manipulation.
- Addresses deformable object manipulation, where contact geometry changes dynamically and force feedback is essential.
- Proposes a force-guided attention mechanism that conditions manipulation actions on the current and desired contact states.

**Limitations/Gaps:** No code or weights released. Limited details available on the specific force sensor and robot platform. The affordance prediction module may not generalize to novel objects without retraining. Evaluation is limited to deformable and alignment tasks.

**Results:**

> **Quantitative results: not available.** The arXiv abstract does not provide specific success rates or numerical comparisons. The paper reports improved performance on deformable object manipulation compared to force-unaware baselines, particularly on tasks where contact geometry changes during execution, but no concrete numbers could be verified from publicly available information.

## Inference / Deployment

- **Inference latency:** Not reported. The paper does not disclose per-step inference latency or control frequency.
- **Deployment hardware:** Franka Emika Panda robot arm for real-world experiments. The VIB module is described as "lightweight and model-agnostic," integrated with pi-zero and RDT architectures. Inference GPU not specified.
- **Real-time capable?** Not verified. The lightweight VIB module suggests low computational overhead, but no quantitative latency benchmarks are provided.

## Dataset / Data Collection

- **Dataset used:** Custom demonstration dataset for deformable object manipulation and alignment tasks. No named benchmark.
- **Collection method:** Teleoperated demonstrations collected via a "homologous leader-follower teleoperation system that collects synchronized vision, language, and force data across diverse contact-rich tasks."
- **Data scale:** Not reported.
- **Teleop equipment:** Homologous leader-follower teleoperation system (specific hardware not detailed).
- **Data format:** Synchronized multi-modal: vision + language + force data.
- **Publicly available?** No. No code or weights released.
