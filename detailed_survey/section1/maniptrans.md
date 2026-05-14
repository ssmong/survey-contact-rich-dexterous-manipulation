### ManipTrans

**Full Title:** ManipTrans: Transferring Dexterous Manipulation Across Embodiments

**Authors:** Researchers from BIGAI / Tsinghua University / Peking University et al.

**Venue/Year:** CVPR 2025

**Hand Hardware:** 4 robot hand embodiments evaluated: Shadow Hand (K=22 DoF), Articulated MANO (K=22 DoF), Inspire Hand (K=12 DoF), and Allegro Hand (K=16 DoF). Cross-embodiment transfer is demonstrated across these morphologically diverse hands.

**Tasks:** Bimanual dexterous manipulation tasks including pen cap removal, bottle unscrewing, and other articulated object manipulation requiring coordinated two-hand operation. The associated DexManipNet dataset contains 3,300 episodes across these tasks and embodiments.

**Key Methodology:** ManipTrans addresses the challenge of transferring dexterous manipulation skills across different robot hand embodiments. The approach learns an embodiment-agnostic manipulation representation that can be mapped to diverse hand morphologies. It uses a universal imitator architecture that takes demonstrations on one hand embodiment and produces policies executable on a different target hand, enabling cross-embodiment skill transfer without per-embodiment demonstration collection.

**Architecture/Parameters:** The imitator network learns a shared latent space for manipulation across embodiments. Pretrained imitator checkpoints and full model weights are released on HuggingFace. The system is trained in IsaacGym Preview 4 with parallel environments.

**Sim Platform:** NVIDIA IsaacGym Preview 4. Sim-to-real transfer is not demonstrated -- the work focuses on cross-embodiment transfer in simulation. The DexManipNet dataset provides MuJoCo-compatible demonstration data.

**Main Contributions:**
- Introduces a universal imitator that transfers manipulation demonstrations across 4 robot hand embodiments (Shadow, MANO, Inspire, Allegro) without requiring per-target demonstrations, whereas prior cross-embodiment approaches required at least some demonstration data on each target hand.
- Releases DexManipNet, a dataset of 3,300 bimanual manipulation episodes across multiple hands on HuggingFace -- the largest publicly available cross-embodiment dexterous manipulation dataset.
- Shows that a shared latent manipulation representation can match the performance of embodiment-specific policies trained with matched demonstrations, demonstrating that cross-embodiment transfer does not inherently sacrifice manipulation quality.

**Limitations/Gaps:**
- **Force/impedance awareness:** No. No force/torque sensing or impedance control is incorporated. The universal imitator operates entirely in joint position space, meaning that the force profiles arising during contact-rich manipulation (e.g., bottle unscrewing torques) are not explicitly controlled. For tasks where contact force magnitude matters (e.g., avoiding over-tightening or crushing), this could limit real-world applicability.
- **VLA/language conditioning:** No. Language conditioning and VLA integration are not explored. The universal imitator conditions on demonstration trajectories, not language instructions.
- **Sim-to-real:** No. The work is simulation-only. Cross-embodiment transfer is demonstrated within IsaacGym, but deployment on physical hardware is not addressed.
- **Code/weights availability:** Pretrained imitator checkpoints and model weights released on HuggingFace. DexManipNet dataset publicly available.

**Results:** Evaluated on bimanual manipulation tasks across 4 robot hand embodiments. Success defined as meeting thresholds: rotation <30 deg, translation <3cm, joint error <8cm, fingertip error <6cm.

| Method | Single-hand SR | Bimanual SR | Rotation Err (deg) | Translation Err (cm) | Joint Err (cm) | Fingertip Err (cm) |
|--------|---------------|-------------|--------------------|--------------------|----------------|-------------------|
| Retarget-Only | 4.6% | 0.0% | -- | -- | -- | -- |
| RL-Only | 34.3% | 12.1% | -- | -- | -- | -- |
| Retarget + Residual | 47.8% | 13.9% | -- | -- | -- | -- |
| **ManipTrans** | **58.1%** | **39.5%** | **8.60** | **0.49** | **2.15** | **1.36** |

Policy learning benchmark on bottle rearrangement (using DexManipNet):

| Method | Success Rate |
|--------|-------------|
| IBC | 4.69% |
| BET | 9.69% |
| DP-UNet | 18.44% |
| DP-Trans | 14.69% |

Hands evaluated: Shadow Hand (K=22), Articulated MANO (K=22), Inspire Hand (K=12), Allegro Hand (K=16). ManipTrans achieves consistent performance across all embodiments without per-embodiment hyperparameter adjustment.

## Inference / Deployment

- **Inference latency:** Not reported. The work is simulation-only (IsaacGym Preview 4).
- **Deployment hardware:** Simulation only. No real-world deployment demonstrated.
- **Real-time capable?** Not applicable (simulation-only). The universal imitator inference speed is not characterized.

## Dataset / Data Collection

- **Dataset used:** DexManipNet (custom dataset released with this work). Contains bimanual manipulation demonstrations across multiple robot hand embodiments.
- **Collection method:** Simulation-generated demonstrations in IsaacGym Preview 4. Demonstrations are produced via trajectory optimization / scripted controllers for bimanual manipulation tasks, then used for imitation learning across embodiments.
- **Data scale:** 3,300 bimanual manipulation episodes (1.34 million frames) across ~1,200 objects, 61 tasks from OakInk-V2, and ~600 bimanual sequences. 4 robot hand embodiments.
- **Teleop equipment:** Not applicable (simulation-generated data).
- **Data format:** MuJoCo-compatible demonstration data; released on HuggingFace.
- **Publicly available?** Yes. DexManipNet dataset publicly available on HuggingFace. Pretrained imitator checkpoints and model weights also released on HuggingFace.

---
