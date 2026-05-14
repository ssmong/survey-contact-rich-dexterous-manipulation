### ACT / ALOHA: Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware

**Full title:** Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware

**Authors:** Tony Z. Zhao, Vikash Kumar, Sergey Levine, Chelsea Finn (Stanford University)

**Venue/Year:** RSS 2023

**Architecture:** Action Chunking with Transformers (ACT) is a CVAE (conditional variational autoencoder) policy with a transformer encoder-decoder architecture. The encoder processes visual observations from multiple cameras (wrist and overhead) via ResNet-18 backbones, combined with joint position proprioception. A style variable z (sampled from a learned prior during inference) is concatenated to enable multi-modal action generation. The transformer decoder autoregressively generates a chunk of future joint-space actions. Total model size is approximately 40-80M parameters.

**Action space:** 14D for bimanual ALOHA: two 6-DoF ViperX 300s arms (joint positions) + 2 gripper widths. ACT predicts action chunks of 50-100 future timesteps at 50 Hz, executing k steps before replanning (temporal ensembling with exponential weighting for smooth transitions).

**Dex hand support?** ✗ --- Designed for the ALOHA bimanual gripper system. The joint-space action representation could extend to dexterous hands if appropriately trained, but this has not been demonstrated. Subsequent works have adapted ACT-like architectures for dexterous systems (e.g., Comp-ACT).

**Force/impedance output?** ✗ --- Joint position targets only, tracked by the robot's internal PD controller. Comp-ACT (IROS 2024) later extended ACT to output variable impedance parameters.

**Key methodology:** ACT combines two key ideas: (1) action chunking with temporal ensembling, where the policy predicts a long horizon of future actions but only executes a few steps before replanning, and (2) a CVAE training framework where a "style variable" z captures the multi-modality in human demonstrations (e.g., different strategies for the same task). During training, the encoder infers z from the full action sequence; during inference, z is sampled from the learned prior. ACT is co-developed with the ALOHA hardware platform, a low-cost (~$20K) bimanual teleoperation and robot system using off-the-shelf ViperX arms.

**Training data:** Task-specific demonstration data collected via the ALOHA teleoperation system. Typically 50-500 teleoperated demonstrations per task at 50 Hz. Tasks include bimanual threading, stacking, transferring, and precision placement.

**Main contributions:**
- Introduced action chunking with temporal ensembling as a principled approach to multi-step action prediction, enabling fine-grained manipulation from a modest number of demonstrations.
- Co-developed the ALOHA low-cost bimanual teleoperation platform, dramatically lowering the barrier to bimanual manipulation research.
- Demonstrated that a relatively simple imitation learning approach can solve fine-grained bimanual tasks (e.g., threading a zip tie) that were previously considered too difficult for IL.

**Quantitative results:**

| Benchmark / Task | ACT | BC Baseline | Notes |
|---|---|---|---|
| *(Consult the RSS 2023 paper for per-task success rates on ALOHA bimanual manipulation tasks including threading, stacking, and transfer.)* | | | |

**Limitations/Gaps:**
- Joint-space action representation limits cross-embodiment transfer.
- The CVAE style variable can collapse during training, reducing multi-modality coverage.
- No language conditioning (task-specific models only).
- No force/compliance output; relies on the robot's built-in PD controller for contact handling.

**Open weights/code:** ✅ Code: [GitHub](https://github.com/tonyzhaozh/act). ✗ No pre-trained weights (task-specific training required).

## Inference / Deployment

- **Inference latency:** ACT runs at 50 Hz control frequency, matching the ALOHA hardware's native rate. The lightweight transformer decoder (~40-80M parameters) with CVAE inference requires only a single forward pass per action chunk (no iterative denoising). Inference latency is approximately 5-10ms per forward pass on a desktop GPU.
- **Deployment hardware:** Desktop GPU for policy inference (specific model not reported, but the ~40-80M parameter model is lightweight). The ALOHA hardware platform (dual ViperX 300s arms) is low-cost (~$20K).
- **Real-time capable?** Yes. ACT operates at 50 Hz with action chunking (predicting 50-100 future steps), executing k steps before replanning with temporal ensembling. The single-pass CVAE inference (no iterative denoising) makes ACT significantly faster than diffusion-based alternatives.

## Dataset / Data Collection

- **Dataset used:** Custom teleoperation demonstrations collected via the ALOHA bimanual hardware platform for each task.
- **Collection method:** Leader-follower teleoperation using the ALOHA system (low-cost ~$20K bimanual setup with dual ViperX 300s arms). Human demonstrator controls the leader arms while follower arms replicate motions at 50 Hz. Data includes joint positions from all joints + gripper widths + multi-view camera images (wrist-mounted and overhead).
- **Data scale:** 50-500 demonstrations per task at 50 Hz. Tasks include bimanual threading, stacking, transferring, and precision placement.
- **Teleop equipment:** ALOHA leader-follower system: dual ViperX 300s 6-DoF arms with parallel-jaw grippers. Low-cost, open-source teleoperation hardware.
- **Data format:** HDF5 files containing joint positions, gripper states, and camera images.
- **Publicly available?** Code at https://github.com/tonyzhaozh/act. ALOHA hardware designs are open-source. Task-specific demonstration datasets are not centrally released (users collect their own).

---
