### ArtiGrasp

**Full Title:** ArtiGrasp: Physically Plausible Synthesis of Bi-Manual Dexterous Grasping and Articulation

**Authors:** Zijian Dong et al. (ETH Zurich)

**Venue/Year:** 3DV 2024

**Hand Hardware:** MANO hand model (human hand proxy). ArtiGrasp operates on the parametric MANO representation of human hands, using it as a physics-based proxy for studying bimanual dexterous grasping and articulation in simulation.

**Tasks:** 8 bimanual grasp + articulation environments from the ARCTIC-like dataset (3 objects excluded: scissors, capsule machine, phone). Tasks require two hands to simultaneously grasp an articulated object and operate its degrees of freedom (e.g., opening a laptop, operating a stapler). The tasks combine stable bimanual grasping with articulated object state change. 745 hand pose references generated across all objects.

**Key Methodology:** ArtiGrasp synthesizes physically plausible bimanual grasping and articulation motions using reinforcement learning in physics simulation. The approach trains policies that control two MANO hands to perform coordinated bimanual manipulation of articulated objects, ensuring physical plausibility through contact-aware simulation. The RaiSim physics engine provides accurate contact dynamics for hand-object interactions. The method learns to jointly optimize grasp stability and articulation progress.

**Architecture/Parameters:** RL policies trained with PPO. Pretrained model weights are publicly released. The policy takes as input the object state and hand proprioception, outputting joint angle targets for both MANO hands.

**Sim Platform:** RaiSim physics engine. Sim-to-real transfer is not demonstrated -- the work uses the MANO human hand model rather than a specific robot hand, focusing on motion synthesis rather than robot deployment.

**Main Contributions:**
- Jointly synthesizes bimanual grasping and articulation in a single policy, whereas prior work typically addressed grasping and articulated object manipulation as separate problems -- this is the first to optimize grasp stability and articulation progress simultaneously.
- Demonstrates physically plausible bimanual motions across 8 articulated objects using physics-based RL in RaiSim, producing motions that respect contact dynamics and joint limits rather than relying on kinematic interpolation.
- Releases pretrained models and code ([GitHub](https://github.com/zdchan/artigrasp)), enabling reproducibility.

**Limitations/Gaps:**
- **Force/impedance awareness:** No. No explicit force sensing or impedance control beyond implicit contact forces computed by the RaiSim physics engine. The policy outputs joint position targets; contact forces arise from the simulation's contact solver rather than being explicitly controlled. This means the system cannot regulate grasp force magnitude (e.g., to avoid crushing fragile objects) or articulation force (e.g., to detect joint limits).
- **VLA/language conditioning:** No. No language conditioning or vision-language integration.
- **Sim-to-real:** Not applicable in current form. The work uses the MANO human hand model rather than a specific robot hand, making direct robot deployment non-trivial -- it would require retargeting from MANO to a physical robot hand and addressing the additional sim-to-real gap.
- **Code/weights availability:** Code and pretrained model weights released ([GitHub](https://github.com/zdchan/artigrasp)).

**Results:** Evaluated on 8 articulated objects (745 hand pose references). Metrics include articulation success rate, displacement (object base movement), position error, and articulation angle error. Results are aggregated across objects.

Table 2 -- Grasping and Articulation (combined, aggregated across objects):

| Metric | ArtiGrasp (Ours) | D-Grasp (Baseline) |
|--------|-----------------|-------------------|
| Articulation success rate | 0.55 | 0.22 |
| Object base displacement | 0.01 m | 0.49 m |

Table 3 -- Dynamic Object Grasping and Articulation:

| Metric | ArtiGrasp (Ours) | D-Grasp (Baseline) |
|--------|-----------------|-------------------|
| Task success rate | 0.50 | 0.11 |
| Position error | 0.03 m | 0.05 m |
| Articulation angle error | 0.41 rad | 0.66 rad |

Table 4 -- Robustness to noisy hand pose estimates (image-based input):

| Metric | MoCap Input | Noisy (Image-based) |
|--------|------------|-------------------|
| Grasping success | 0.67 | 0.64 |

ArtiGrasp achieves 2.5x higher articulation success and 4.5x higher dynamic task success than D-Grasp, with near-zero object displacement (0.01m vs. 0.49m).

## Inference / Deployment

- **Inference latency:** Not reported. The work uses MANO human hand model in RaiSim simulation; no physical robot deployment.
- **Deployment hardware:** Simulation only (RaiSim physics engine). No real-world deployment hardware.
- **Real-time capable?** Not applicable (simulation-only, MANO hand model rather than a physical robot hand).

## Dataset / Data Collection

- **Dataset used:** No external dataset. Training data is generated via RL simulation rollout in RaiSim across 6 articulated object environments. Hand pose references are used to guide the policy.
- **Collection method:** RL simulation rollout with PPO in RaiSim physics engine. The policy learns bimanual grasping and articulation from scratch through physics-based RL. Image-based hand-object pose estimates from an off-the-shelf regressor are used for evaluation.
- **Data scale:** Not reported (on-policy RL training; data generated on-the-fly).
- **Teleop equipment:** Not applicable (RL-trained, no demonstrations).
- **Data format:** Not applicable (on-policy RL training). Pretrained model weights released.
- **Publicly available?** Yes. Code and pretrained model weights released ([GitHub](https://github.com/zdchan/artigrasp)).

---
