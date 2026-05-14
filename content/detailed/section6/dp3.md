### DP3: 3D Diffusion Policy --- Generalizable Visuomotor Policy Learning via Simple 3D Representations

**Full title:** 3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations

**Authors:** Yanjie Ze, Gu Zhang, Kangning Zhang, Chenyuan Hu, Muhan Wang, Huazhe Xu (Tsinghua University)

**Venue/Year:** RSS 2024

**Architecture:** DP3 extends Diffusion Policy to operate on 3D point cloud observations instead of 2D images. The visual encoder processes depth-camera point clouds via a lightweight 3D encoder (PointNet++ or sparse 3D convolutions, ~5M parameters), producing per-point features that are aggregated into a global 3D scene representation. This 3D representation conditions a diffusion-based action decoder (similar to Diffusion Policy's 1D convolutional architecture). Total model size is ~30M parameters.

**Action space:** Continuous, variable dimensionality. Evaluated on up to 22-DoF action spaces in simulation (Adroit dexterous hand tasks: 24-DoF Shadow hand). Supports both EEF and joint-space actions. Action chunking inherited from Diffusion Policy.

**Dex hand support?** Partial (simulation only) --- Evaluated on Adroit hand manipulation benchmarks (door, pen, hammer) using a 24-DoF Shadow hand in MuJoCo. One of the first diffusion policies demonstrated on high-DoF dexterous hands, across 72 simulated tasks total. No real-robot dexterous hand deployment has been demonstrated.

**Force/impedance output?** ✗ --- Position targets only.

**Key methodology:** DP3 argues that 3D point cloud observations provide superior spatial reasoning and viewpoint generalization compared to 2D images for manipulation. By lifting observations to 3D, the policy becomes invariant to camera viewpoint changes and can reason about spatial relationships (e.g., relative positions of fingers and objects) that are ambiguous in 2D. The 3D encoder is deliberately kept lightweight to enable real-time inference. Combined with the diffusion action decoder, DP3 achieves strong performance across 72 simulation tasks spanning both gripper and dexterous hand manipulation.

**Training data:** Task-specific demonstration datasets. In simulation, demonstrations generated via scripted policies or RL-trained experts. Typically 100-200 demonstrations per task.

**Main contributions:**
- Demonstrated that simple 3D point cloud representations significantly improve policy generalization and sample efficiency compared to 2D image-based policies.
- Among the first diffusion policies evaluated on high-DoF dexterous hand tasks in simulation (Adroit benchmarks).
- Showed that a lightweight 3D encoder (~5M parameters) suffices for effective 3D policy learning, enabling real-time inference.

**Quantitative results:**

| Benchmark / Task | DP3 | Diffusion Policy (2D) | Notes |
|---|---|---|---|
| *(Consult the RSS 2024 paper for per-task success rates across 72 simulation tasks including Adroit dexterous hand benchmarks and gripper manipulation tasks.)* | | | |

**Limitations/Gaps:**
- Requires depth cameras for point cloud generation, which are not always available or reliable in real-world settings.
- Simulation-only evaluation for dexterous hand tasks; no real-robot dexterous hand results.
- Point cloud processing can be noisy with real sensors, requiring additional filtering and processing.
- No language conditioning.

**Open weights/code:** ✅ Code: [GitHub](https://github.com/YanjieZe/3D-Diffusion-Policy). ✗ No pre-trained weights (task-specific training).

## Inference / Deployment

- **Inference latency:** The lightweight 3D encoder (~5M parameters) and small diffusion action head (~25M total) enable fast inference. With DDIM acceleration, estimated ~10-20 Hz on a desktop GPU. Point cloud preprocessing (downsampling, normalization) adds minor overhead (~1-5ms).
- **Deployment hardware:** Desktop GPU for inference. The ~30M parameter total model is lightweight, comparable to Diffusion Policy. Requires depth cameras for point cloud input.
- **Real-time capable?** Yes, with DDIM acceleration. The lightweight 3D encoder was deliberately kept small to enable real-time inference. Comparable inference speed to Diffusion Policy (~10-20 Hz) with the added benefit of 3D spatial reasoning.

## Dataset / Data Collection

- **Dataset used:** Task-specific demonstration datasets across 72 simulated tasks. Includes Adroit dexterous hand benchmarks (door, pen, hammer with 24-DoF Shadow hand in MuJoCo) and gripper manipulation tasks.
- **Collection method:** Simulation demonstrations generated via scripted policies or RL-trained experts. Point cloud observations from simulated depth cameras. No real-robot dexterous hand data.
- **Data scale:** 100-200 demonstrations per task across 72 simulation tasks.
- **Teleop equipment:** Not applicable (simulation demonstrations from scripted/RL-expert policies).
- **Data format:** Point cloud observations (3D) + joint positions. Task-specific datasets.
- **Publicly available?** Code at https://github.com/YanjieZe/3D-Diffusion-Policy. Simulation environments are standard (Adroit/MuJoCo).

---
