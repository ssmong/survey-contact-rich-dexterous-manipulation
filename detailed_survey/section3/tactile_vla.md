## 3.8 Tactile-VLA

- **Full title:** Tactile-VLA: Tactile Vision-Language-Action Model with Hybrid Position-Force Control
- **Authors:** Tsinghua University et al.
- **Venue/Year:** arXiv preprint, 2025
- **arXiv:** https://arxiv.org/abs/2507.09160

**Force/tactile input type:** Tactile sensors (specific type not detailed in the survey table).

**Force/impedance output:** Yes -- hybrid position-force output. The model generates both position targets and force targets, which are executed through a hybrid position-force controller. **Force output type: partial (hybrid pos-force, not full 6D wrench).**

**Robot platform:** Not specified in detail.

> **Limitation (gripper-only):** Evaluated only on parallel-jaw grippers; not validated on multi-finger dexterous hands.

**Tasks:** Charger insertion as the primary evaluation task. Achieves 90% success rate.

**Key methodology:** Tactile-VLA integrates tactile input into a VLA framework and extends the action space to include both position and force targets. The hybrid output enables the robot to switch between position control (for free-space motion) and force control (for contact phases) based on the inferred task phase. The tactile input provides rich contact information that helps the model determine when to transition between control modes and what force targets to command during contact.

**Architecture/Parameters:** VLA with tactile encoder and hybrid position-force action head. The action space includes both Cartesian position targets and desired contact forces.

**Main contributions:**
- One of the few VLA models to output hybrid position-force actions, enabling active force regulation during contact.
- Demonstrates that combining tactile input with hybrid force-position output achieves high success rates on precision insertion tasks (90% on charger insertion).
- Proposes an integrated approach where the VLA itself determines when to use position vs. force control based on tactile feedback.

**Limitations/Gaps:** No code or weights released. Robot platform details are underspecified. Evaluated primarily on a single task (charger insertion). The hybrid controller design and force target calibration likely require per-task tuning.

**Results:**

| Metric | Value |
|--------|-------|
| Charger insertion success rate | 90% |
| vs. position-only baselines | Hybrid position-force output outperforms position-only |

## Inference / Deployment

- **Inference latency:** Not reported. The paper does not disclose per-step inference latency, control frequency, or deployment hardware.
- **Deployment hardware:** Not specified. Robot platform details are underspecified in available materials.
- **Real-time capable?** Not verified. Inference latency and deployment hardware not reported.

## Dataset / Data Collection

- **Dataset used:** Custom demonstration dataset for charger insertion task. No named benchmark. The paper uses "few demonstrations" to connect VLM knowledge to robot tactile sensors.
- **Collection method:** Teleoperated demonstrations with tactile sensor input. Specific collection details not reported.
- **Data scale:** Few demonstrations (exact count not reported).
- **Teleop equipment:** Not reported.
- **Data format:** Not reported.
- **Publicly available?** No. No code or weights released.

> *Dataset details from training knowledge, not verified from source -- the arXiv abstract did not disclose data specifics.*
