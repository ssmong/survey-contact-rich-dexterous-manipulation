### 2.2 DexGraspVLA

**Full title:** DexGraspVLA: A Vision-Language-Action Framework for Dexterous Grasping

**Authors:** Psi-Robot team et al.

**Venue/Year:** AAAI 2026

**arXiv:** [2502.08142](https://arxiv.org/abs/2502.08142)

**Hand hardware:** Custom dexterous hand (specific model and DoF count not publicly detailed at the abstracted level; the system is designed for multi-finger grasping)

**Tasks:**
- Dexterous grasping in cluttered environments
- Language-specified grasping (e.g., "grasp the red mug by its handle")
- Grasping under occlusion and varying object arrangements

**Key methodology:** DexGraspVLA employs a two-stage architecture that separates high-level planning from low-level dexterous control. A large vision-language model (Qwen2.5-VL-72B) serves as the semantic planner, interpreting language instructions and visual scenes to determine grasp intent and target object. A diffusion-based controller then generates fine-grained dexterous grasp actions conditioned on the planner's output. Language is used both for task specification and for grounding object references in cluttered scenes.

**Architecture/Parameters:**
- Planner: Qwen2.5-VL-72B (72 billion parameter vision-language model)
- Controller: diffusion-based action generation model
- The two-stage design keeps the large VLM frozen for planning while training a smaller diffusion controller for dexterous actions
- Controller checkpoint publicly available (Google Drive)

**Main contributions:**
- Demonstrated that very large VLMs (72B) can serve as effective planners for dexterous grasping when combined with a dedicated diffusion controller
- Two-stage architecture that decouples semantic understanding (VLM) from motor control (diffusion), allowing each component to be optimized independently
- Language-conditioned dexterous grasping in cluttered real-world scenarios, moving beyond single-object or isolated grasping settings

**Limitations/Gaps:**
- Relies on an extremely large VLM (72B parameters), raising questions about inference latency and deployment feasibility for real-time control
- Grasping-only: does not address post-grasp manipulation, in-hand reorientation, or tool use
- No force or tactile feedback integration; grasps are planned purely from vision and language
- Limited to a single hand hardware platform; no cross-embodiment evaluation

**Results:**

| Metric | Value | Notes |
|---|---|---|
| Grasping success rate | "90%+" (approximate, as reported) | Cluttered environments |

> **[EDITORIAL NOTE -- precision needed]:** The "90%+" figure is an approximate claim from the original entry. The exact success rate, the number of objects tested, the number of evaluation trials, and the specific clutter conditions must be extracted from the full paper (arXiv 2502.08142). Without these details, the claim cannot be properly contextualized. Key questions: (1) What is the exact percentage? (2) Over how many objects and trials? (3) What defines "cluttered" -- how many distractor objects? (4) Is this real-world or simulation?

- Outperforms prior language-conditioned grasping baselines (specific baseline names and margins should be extracted from the paper)
- Controller checkpoint released (Google Drive)
- Code released at [GitHub](https://github.com/Psi-Robot/DexGraspVLA)

## Inference / Deployment

- **Inference latency:** Not reported. The use of a 72B-parameter VLM (Qwen2.5-VL-72B) as the planner raises significant latency concerns, though the VLM may operate at a slower planning frequency while the diffusion controller runs at a higher action frequency.
- **Deployment hardware:** Not specified. Training hardware uses 8 NVIDIA H100 GPUs. The 72B VLM inference requires substantial GPU memory (likely multi-GPU or quantized deployment).
- **Real-time capable?** Likely constrained by the 72B VLM inference. The two-stage architecture (VLM planner + diffusion controller) may mitigate this if the VLM plans at a lower frequency, but specific latency figures are not publicly available.

## Dataset / Data Collection

- **Dataset used:** Custom human demonstration dataset. A small example dataset (51 samples) is provided for training understanding.
- **Collection method:** Human demonstrations. Specific teleoperation equipment details are not disclosed due to intellectual property constraints ("Due to intellectual property constraints, we are unable to open-source the hardware-related code").
- **Data scale:** Example dataset contains 51 demonstration samples. Full training dataset scale not disclosed.
- **Teleop equipment:** Not disclosed (IP-restricted).
- **Data format:** Zarr format. Each sample contains: action data (13 DoF -- robotic arm and hand), state data (13 DoF), third-view head camera images (RGB + binary mask, 4 channels), first-view wrist camera images (RGB, 3 channels), and episode segmentation metadata.
- **Publicly available?** Example dataset (51 demos) available via Google Drive. Controller checkpoint available on Google Drive. Full training dataset availability not confirmed. Code at [GitHub](https://github.com/Psi-Robot/DexGraspVLA).
