### DexDeform

**Full Title:** DexDeform: Dexterous Deformable Object Manipulation with Human Demonstrations and Differentiable Physics

**Authors:** Sizhe Li et al. (MIT-IBM Watson AI Lab)

**Venue/Year:** ICLR 2023

**Hand Hardware:** Multi-finger hand in simulation. The hand model operates within the PlasticineLab differentiable physics environment, which provides soft-body contact dynamics for deformable object manipulation.

**Tasks:** 6 deformable object manipulation tasks, modeled on clay/play-doh manipulation scenarios. Tasks include shaping, molding, pressing, and forming deformable materials into target configurations. These tasks represent a unique challenge in dexterous manipulation due to the high-dimensional deformable state space.

**Key Methodology:** DexDeform combines human demonstrations with differentiable physics simulation for deformable object manipulation. The approach uses PlasticineLab, a differentiable soft-body simulator, to provide gradient information through the manipulation process. Human demonstrations guide the initial policy, which is then refined using differentiable physics gradients to optimize for target shape achievement. This hybrid approach leverages the efficiency of gradient-based optimization while using human demonstrations to provide reasonable initialization in the complex deformable manipulation landscape.

**Architecture/Parameters:** The policy network maps the current deformable object state to multi-finger hand actions. Differentiable physics gradients from PlasticineLab enable backpropagation through the simulation dynamics. Specific model sizes are not extensively documented.

**Sim Platform:** PlasticineLab (differentiable soft-body simulator). No sim-to-real transfer -- the work is entirely in simulation, with the unique challenge being the deformable object physics rather than rigid-body contact.

**Main Contributions:**
- Addresses dexterous deformable object manipulation, a domain requiring fundamentally different contact reasoning than rigid-body manipulation -- prior dexterous manipulation work focused almost exclusively on rigid objects, leaving deformable manipulation underexplored.
- Combines human demonstrations with differentiable physics gradients, enabling efficient policy optimization in the high-dimensional deformable state space -- this hybrid is novel because prior deformable manipulation used either pure RL (sample-inefficient) or pure trajectory optimization (prone to local minima without demonstration initialization).
- Introduces 6 benchmark tasks for deformable object manipulation with multi-finger hands, filling a gap in dexterous manipulation evaluation where no standardized deformable tasks previously existed.

**Limitations/Gaps:**
- **Force/impedance awareness:** No. No explicit force/impedance control is used. Although deformable object manipulation inherently involves force-mediated shape change, the system controls the hand via position targets and relies on differentiable physics gradients to implicitly learn appropriate force application. There is no explicit force feedback loop or impedance regulation.
- **VLA/language conditioning:** No. No language conditioning or vision-language integration. Tasks are specified via target shape configurations, not language descriptions.
- **Sim-to-real:** No. The work is entirely in simulation. Sim-to-real transfer for deformable manipulation is particularly challenging due to the difficulty of accurately modeling real-world deformable material properties (stiffness, plasticity, friction) in simulation.
- **Code/weights availability:** Code is released but without pretrained weights.

**Results:** Evaluated on a suite of 6 dexterous deformable object manipulation tasks. DexDeform outperforms RL baselines (PPO, SAC) and pure demonstration replay on final shape accuracy (Chamfer distance). The method uses human demonstrations for initialization and differentiable physics gradients for refinement, enabling better exploration and generalization across novel target shapes unseen in the initial demonstrations.

| Metric / Finding | Value | Context |
|-------------------|-------|---------|
| Tasks evaluated | 6 | Deformable object shaping/molding tasks in PlasticineLab |
| Primary metric | Chamfer distance (CD) | Measures shape accuracy vs. target configuration |
| vs. PPO | Lower CD | DexDeform achieves better final shape accuracy |
| vs. SAC | Lower CD | DexDeform achieves better final shape accuracy |
| vs. Demonstration replay | Lower CD | Refinement via differentiable physics improves upon raw demonstrations |
| Key advantage | Generalization | Better exploration across novel goals unseen in initial demos |

Note: Specific per-task Chamfer distance values are reported in the paper's results tables but could not be extracted from the arXiv page (no HTML version available for this 2023 paper). The paper PDF should be consulted for exact numerical values per task and method.

## Inference / Deployment

- **Inference latency:** Not reported. The work is entirely in simulation (PlasticineLab differentiable physics simulator).
- **Deployment hardware:** Simulation only. No real-world deployment.
- **Real-time capable?** Not applicable (simulation-only). The differentiable physics optimization is inherently offline and not designed for real-time control.

## Dataset / Data Collection

- **Dataset used:** Custom demonstrations for 6 deformable object manipulation tasks in PlasticineLab. No named benchmark dataset.
- **Collection method:** Human demonstrations collected in the PlasticineLab differentiable simulator. Demonstrations guide the initial policy, which is then refined using differentiable physics gradients.
- **Data scale:** Not reported. The number of human demonstrations per task is not specified in public materials.
- **Teleop equipment:** Not reported. The method of human demonstration collection in PlasticineLab (e.g., keyboard, scripted trajectories) is not detailed.
- **Data format:** Not reported. Code is released but without pretrained weights.
- **Publicly available?** Code released (without pretrained weights). Whether demonstration data is included in the code release is not confirmed.

> *ArXiv ID 2304.03223 confirmed as DexDeform (ICLR 2023). No HTML version available on arXiv; per-task Chamfer distance values are in the paper PDF tables.*

---
