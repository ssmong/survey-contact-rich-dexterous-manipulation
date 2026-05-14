### Diffusion Policy: Visuomotor Policy Learning via Action Diffusion

**Full title:** Diffusion Policy: Visuomotor Policy Learning via Action Diffusion

**Authors:** Cheng Chi, Siyuan Feng, Yilun Du, Zhenjia Xu, Eric Cousineau, Benjamin Burchfiel, Shuran Song (Columbia University)

**Venue/Year:** RSS 2023

**Architecture:** Diffusion Policy adapts denoising diffusion probabilistic models (DDPMs) to robot action generation. Two architecture variants are proposed: (1) a CNN-based variant using 1D temporal convolutions (similar to a 1D U-Net) over the action sequence, and (2) a transformer-based variant where a transformer decoder attends to observation features and denoises action tokens. Both take visual observations (from ResNet or ViT encoders) as conditioning input. The model is lightweight: the CNN variant has ~25M parameters; the transformer variant ~40M.

**Action space:** Continuous, variable dimensionality. Typically 2D (planar pushing) to 7D (6-DoF EEF + gripper). The key innovation is "action chunking" --- predicting a chunk of T future actions (typically T=8-16) in a single denoising pass, then executing only the first few steps before replanning. This temporal action abstraction enables smooth, temporally coherent behavior.

**Dex hand support?** ✗ --- Designed and evaluated for gripper-based manipulation. However, the continuous action space and action chunking framework have been adopted by subsequent dexterous hand policies (DP3, iDP3).

**Force/impedance output?** ✗ --- Position targets only. Subsequent works (TacDiffusion, Reactive Diffusion Policy) have extended the diffusion framework to force-domain outputs.

**Key methodology:** Diffusion Policy treats visuomotor policy learning as a conditional denoising problem: given visual observations, the policy iteratively denoises a random noise vector into a coherent action trajectory. This formulation naturally handles multi-modality in the action distribution (e.g., reaching around an obstacle from the left or right), which is a key failure mode of MSE-based behavioral cloning. The action chunking mechanism generates temporally coherent action sequences, avoiding the jittery behavior of single-step policies. The denoising process uses DDPM with 10-100 diffusion steps during inference, with DDIM acceleration reducing this to 5-10 steps.

**Training data:** Trained from scratch on task-specific demonstration datasets. The original paper uses Push-T (200 episodes), robomimic tasks, and real-robot tabletop manipulation demonstrations. Typically requires 50-500 demonstrations per task.

**Main contributions:**
- Introduced diffusion models to robot action generation, establishing a new paradigm for visuomotor policy learning that naturally handles multi-modal action distributions.
- Proposed action chunking for diffusion policies, enabling temporally coherent behavior and stable closed-loop control.
- Demonstrated that diffusion policies significantly outperform behavioral cloning, energy-based models, and single-step policies on both simulated and real manipulation tasks.

**Quantitative results:**

| Benchmark / Task | Diffusion Policy (CNN) | Diffusion Policy (Transformer) | BC Baseline | Notes |
|---|---|---|---|---|
| *(Consult the RSS 2023 paper for per-task results on Push-T, robomimic, and real-robot benchmarks. The paper reports significant improvements over behavioral cloning and energy-based model baselines.)* | | | | |

**Limitations/Gaps:**
- Multi-step denoising introduces inference latency (10-100ms per action chunk depending on the number of diffusion steps), which may be problematic for high-frequency dexterous control.
- No language conditioning in the base model (task-specific training only).
- Requires task-specific training from scratch; no cross-task or cross-embodiment generalization in the original formulation.
- No force/compliance awareness.

**Open weights/code:** ✅ Code: [GitHub](https://github.com/real-stanford/diffusion_policy). ✗ No pre-trained weights (each task requires training from scratch).

## Inference / Deployment

- **Inference latency:** 10-100ms per action chunk depending on diffusion steps. With DDIM acceleration (5-10 steps instead of 100), the CNN variant (~25M parameters) achieves ~10-20 Hz on a desktop GPU (RTX 3090 class). The transformer variant (~40M parameters) is slightly slower. Action chunking (predicting 8-16 future steps) reduces the effective inference frequency requirement.
- **Deployment hardware:** Desktop GPU (NVIDIA RTX 3090/4090 or similar) for real-time inference. The lightweight model size (25-40M parameters) enables deployment on consumer hardware. No edge device (Jetson) benchmarks reported, but the small model size suggests feasibility.
- **Real-time capable?** Yes, with DDIM acceleration. At 10-20 Hz with 5-10 denoising steps, Diffusion Policy supports real-time control for typical manipulation tasks. With full 100-step DDPM, inference is too slow (~1-5 Hz). Action chunking further reduces the required inference frequency.

## Dataset / Data Collection

- **Dataset used:** Task-specific demonstration datasets. Push-T (200 episodes), robomimic benchmark tasks (lift, can, square, transport), and custom real-robot tabletop manipulation demonstrations.
- **Collection method:** Human demonstrations via teleoperation or scripted policies. Push-T: scripted. Robomimic: human teleop (SpaceMouse). Real-robot: SpaceMouse/keyboard teleoperation on UR5 or Franka.
- **Data scale:** 50-500 demonstrations per task. Push-T: 200 episodes. Robomimic: standard dataset sizes (200-300 episodes per task). Task-specific training from scratch (no cross-task pretraining).
- **Teleop equipment:** SpaceMouse and keyboard for real-robot demonstrations. Robomimic uses its standard proficient human (PH) and multi-human (MH) demonstration sets.
- **Data format:** HDF5 (robomimic format) and zarr (Diffusion Policy native format).
- **Publicly available?** Yes. Push-T and robomimic datasets are publicly available. Diffusion Policy code at https://github.com/real-stanford/diffusion_policy.

---
