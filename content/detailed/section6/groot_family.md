## 6.2 NVIDIA GR00T Family

### GR00T N1 / N1.5 / N1.6 / N1.7

**Full title:** GR00T N1: An Open Foundation Model for Generalist Humanoid Robot (initial release); subsequent versions released as model updates without separate publications.

**Authors:** NVIDIA Isaac Robotics team (Jim Fan, Yuke Zhu, Linxi "Jim" Fan, Dieter Fox, Anima Anandkumar, et al.)

**Venue/Year:** GR00T N1 announced GTC Mar 2025; N1.5 mid-2025; N1.6 late 2025; N1.7 May 2026. Associated technical reports published via NVIDIA Research blog and HuggingFace model cards.

**Architecture:**

| Version | Date | Params | VLM Backbone | DiT Layers | Key Change |
|---|---|---|---|---|---|
| **GR00T N1** | Mar 2025 | 2.2B | Eagle-2 (InternVL-based) | 16 | Initial release; dual-encoder (SigLIP vision + T5 language) with DiT action head |
| **GR00T N1.5** | Mid 2025 | 3B | Eagle 2.5 (frozen) | 16 | Increased parameter count; frozen VLM backbone; improved cross-embodiment generalization |
| **GR00T N1.6** | Late 2025 | 3B | Cosmos-2B | 32 | Doubled DiT depth; switched VLM to Cosmos-2B; native video understanding |
| **GR00T N1.7** | May 2026 | 3B | Cosmos-Reason2-2B (Qwen3-VL architecture) | 32 | Flexible-resolution vision (native aspect ratio); relative EEF action space; 20K hrs human video pretraining |

The architecture consists of three main components: (1) a vision encoder (SigLIP2 in N1.7) processes RGB camera frames, (2) a language encoder (T5) processes text instructions, and (3) a Diffusion Transformer (DiT) with adaptive layer normalization (AdaLN) denoises continuous action vectors conditioned on vision-language embeddings and proprioceptive state. A per-embodiment MLP maps between the shared latent action space and embodiment-specific joint configurations.

**Action space:** Variable dimensionality depending on robot embodiment. N1.7 adopted relative end-effector (EEF) actions --- representing actions as deltas from the current pose rather than absolute targets --- which improved cross-embodiment transfer. The per-embodiment MLP handles the mapping from shared action representations to robot-specific joint commands. Proprioception input uses configurable max-length padding indexed by embodiment ID to handle variable DoF counts.

**Dex hand support?** Limited. The humanoid embodiments (Unitree G1 via SONIC whole-body control) include integrated hand DoFs (Dex3-1: 7 DoF per hand), but the VLA does not natively support standalone multi-finger dexterous hands like Allegro or Shadow. The "22-DoF hand" capability referenced in EgoScale pretraining refers to the Sharpa hand action representation used during human video pretraining, not the deployment hand. GR00T-Dexterity (a separate RL workflow based on DextrAH-G, not part of the VLA) supports Allegro Hand 16-DoF with geometric fabrics in Isaac Lab.

**Force/impedance output?** ✗ --- All versions output position targets only.

**Key methodology:** GR00T combines a pre-trained vision-language foundation model with a diffusion transformer action head. The DiT denoises continuous action vectors over 4 diffusion steps, conditioned on visual observations, language instructions, and proprioceptive state via AdaLN. N1.7 introduced two key innovations: (1) relative EEF action representation that is consistent across both human and robot embodiments, enabling direct transfer of manipulation priors from human video to robot control; and (2) pretraining on 20K hours of EgoScale human video data alongside diverse robot demonstrations. The per-embodiment MLP architecture allows a single model to control different robots by learning embodiment-specific action encoders/decoders.

**Training data:** N1.7 is pretrained on 21.6M data points from 13 datasets, collected via hybrid methods (human teleoperation, robot autonomy, simulation). Key datasets include DROID (~76K trajectories, 350 hours, 564 scenes), Bridge (60K trajectories, 24 environments), LIBERO (130 language-conditioned tasks), and 20K hours of EgoScale human egocentric video. Post-training checkpoints are provided for specific dataset/embodiment combinations.

**Main contributions:**
- Demonstrated that a single VLA architecture can generalize across multiple robot embodiments (arms, bimanual systems, humanoids) via per-embodiment MLP adapters and a shared DiT action head.
- Established relative EEF actions as a unifying action representation that bridges human video and robot demonstrations, enabling large-scale pretraining on human manipulation data.
- Provided a complete open-source ecosystem (Isaac-GR00T) with fine-tuning, ONNX/TensorRT export, and deployment pipelines, including real-time inference on edge devices (NVIDIA Jetson Orin: 4.6 Hz with TensorRT).

**Quantitative results:**

| Benchmark / Task | GR00T N1.7 | Notes |
|---|---|---|
| *(Results not independently verified --- consult the NVIDIA technical report and HuggingFace model card for per-task success rates on DROID, Bridge, LIBERO, and humanoid benchmarks.)* | | |

**Licensing changes across versions:**

| Version | License |
|---|---|
| N1 | Non-commercial (NVIDIA research license) |
| N1.5 | Non-commercial (NVIDIA research license) |
| N1.6 | NVIDIA Open Model License (more permissive) |
| N1.7 | NVIDIA Open Model License (commercial use permitted) |

The progression from non-commercial to commercially permissive licensing is notable, enabling industrial adoption.

**Limitations/Gaps:**
- Standalone dexterous hands are not supported by the VLA itself; GR00T-Dexterity provides dexterous hand control but as a separate RL system without language conditioning.
- No force/impedance output: position-only control limits applicability to contact-rich tasks.
- The per-embodiment MLP requires embodiment-specific training data and an embodiment ID at inference, limiting zero-shot transfer to entirely new robot morphologies.
- Inference speed on edge devices (2.9-4.6 Hz on Orin) may be insufficient for high-frequency dexterous manipulation requiring 20+ Hz control.

**Open weights/code:** ✅ All versions available on [HuggingFace](https://huggingface.co/nvidia/GR00T-N1.7-3B) and [GitHub](https://github.com/NVIDIA/Isaac-GR00T). Code is Apache 2.0; model weights use NVIDIA Open Model License (commercially permissive from N1.6 onward).

## Inference / Deployment

- **Inference latency:** GR00T N1.7 runs at 2.9 Hz (PyTorch) to 4.6 Hz (TensorRT-optimized) on NVIDIA Jetson AGX Orin, using 4 DiT diffusion steps per action chunk. On a desktop GPU (e.g., A100), inference is faster but specific Hz figures for desktop deployment are not prominently reported.
- **Deployment hardware:** Primary edge target is NVIDIA Jetson AGX Orin (64GB). The Isaac-GR00T toolchain provides ONNX export and TensorRT optimization pipelines for edge deployment. Desktop GPUs (A100, RTX 4090) used for training and faster-than-real-time inference. Deployed on Unitree G1 humanoid via SONIC whole-body controller.
- **Real-time capable?** Marginal. At 2.9-4.6 Hz on Jetson Orin, GR00T N1.7 is suitable for slow to moderate manipulation tasks but insufficient for high-frequency dexterous control (20+ Hz). Action chunking partially compensates by predicting multiple future steps per inference. TensorRT optimization provides ~1.6x speedup over PyTorch on the same hardware.

## Dataset / Data Collection

- **Dataset used:** N1.7 pretrained on 21.6M data points from 13 datasets. Key datasets: DROID (~76K trajectories, 350 hours, 564 scenes), Bridge V2 (60K trajectories, 24 environments), LIBERO (130 language-conditioned tasks), and 20K hours of EgoScale human egocentric video (Ego4D, Ego-Exo4D, proprietary sources). Additional simulation and robot autonomy data.
- **Collection method:** Hybrid: human teleoperation (DROID, Bridge V2), robot autonomy (self-collected), simulation (Isaac Sim), and human egocentric video (EgoScale pipeline with 22-DoF Sharpa hand pose extraction). Post-training checkpoints provided for specific dataset/embodiment combinations.
- **Data scale:** 21.6M data points across 13 datasets. 20K hours of human video pretraining (EgoScale). DROID: 76K trajectories / 350 hours. Bridge: 60K trajectories. LIBERO: 130 tasks.
- **Teleop equipment:** Varies by dataset -- VR controllers (DROID), keyboard/SpaceMouse (Bridge V2), leader-follower (ALOHA-style). Human video data requires no teleoperation.
- **Data format:** LeRobot format for public datasets; RLDS for OXE-compatible components. NVIDIA Isaac-GR00T provides data loading utilities.
- **Publicly available?** Partially. DROID, Bridge V2, LIBERO are publicly available. EgoScale human video data and proprietary robot data are not released. Model weights are open (NVIDIA Open Model License from N1.6 onward).

---
