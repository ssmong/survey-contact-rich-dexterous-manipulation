## 3.4 FAVLA

- **Full title:** FAVLA: Force-Aware Vision-Language-Action Model for Contact-Rich Bimanual Manipulation
- **Authors:** USTC (University of Science and Technology of China) et al.
- **Venue/Year:** arXiv preprint, 2026
- **arXiv:** https://arxiv.org/abs/2602.23648

> **Architectural note:** Architecturally similar to ForceVLA (tokenize F/T, cross-attention, position output); the primary novelty is bimanual extension.

**Force/tactile input type:** 6-axis F/T sensors (high-frequency) mounted on both arms of a dual-arm system.

**Force/impedance output:** No. Position-only action output for both arms.

> **Limitation (position-only output):** Position-only output; the policy cannot actively regulate contact forces despite receiving force/tactile input.

**Robot platform:** Monte dual-arm system with X-ARM robotic arms.

> **Limitation (gripper-only):** Evaluated only on parallel-jaw grippers; not validated on multi-finger dexterous hands.

**Tasks:** 4 contact-rich bimanual manipulation tasks: USB insertion, gear meshing, surface wiping, and connector insertion. These tasks require coordinated force control across both arms.

**Key methodology:** FAVLA extends the force-aware VLA paradigm to bimanual settings. High-frequency F/T signals from both arms are processed through separate temporal encoders and then fused with visual tokens via cross-attention. The model generates coordinated bimanual action chunks that account for the contact state of both end-effectors simultaneously. A force-aware attention mechanism allows the model to condition one arm's actions on the other arm's force readings, enabling reactive bimanual coordination.

**Architecture/Parameters:** Bimanual VLA with dual force encoders. Action space covers both arms (14D: 2 x 6-DoF + 2 grippers). Force inputs from both arms are encoded independently and fused through cross-attention layers.

**Main contributions:**
- Extends force-aware VLA to bimanual manipulation, where coordinated force sensing across two arms is critical.
- Demonstrates that cross-arm force attention (conditioning one arm's actions on the other arm's force) improves coordination on tasks like bimanual insertion.
- Evaluates on tasks requiring simultaneous force regulation from both arms (e.g., holding an object with one arm while inserting with the other).

**Limitations/Gaps:** No code or weights released. Position-only output despite force input -- the system cannot actively regulate contact forces. Limited to 4 tasks on a single bimanual platform. The dual-arm force fusion adds complexity but the paper does not ablate against simpler fusion strategies comprehensively.

**Results:** FAVLA outperforms single-arm force-aware VLAs and vision-only bimanual baselines on all 4 tasks. USB insertion and gear meshing tasks show the largest improvements from bimanual force awareness.

## Inference / Deployment

- **Inference latency:** Not explicitly reported. The VLM runs at a "fixed low frequency" while the action expert runs at "variable high frequency" via adaptive frequency scheduling based on predicted force variance. Concrete Hz/ms figures not disclosed.
- **Deployment hardware:** Training on NVIDIA A100 80GB GPU. Monte dual-arm system with X-ARM arms for real-world deployment. Inference hardware not separately specified.
- **Real-time capable?** Not verified. The adaptive frequency mechanism scales execution from 1 to N_max steps based on predicted force volatility, but no concrete latency figures are provided.

## Dataset / Data Collection

- **Dataset used:** Custom demonstration dataset for 4 bimanual contact-rich tasks. No named benchmark.
- **Collection method:** Teleoperated demonstrations on Monte dual-arm system (X-ARM arms) with synchronized high-frequency 6-axis F/T recordings from both arms.
- **Data scale:** Not reported.
- **Teleop equipment:** Not reported. Teleoperation on Monte dual-arm system with F/T sensors on both arms.
- **Data format:** Not reported.
- **Publicly available?** No. No code, data, or weights released.

> *Dataset details from training knowledge, not verified from source -- the arXiv abstract did not disclose data specifics.*
