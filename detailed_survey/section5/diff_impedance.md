### 5.2 Diff-Impedance

**Full title:** Diffusion-Based Impedance Learning for Contact-Rich Manipulation

**Authors:** Fan Yang, Hanna Ziesche, Zhichao Wen, Marco Ewerton, Leonel Rozo (KIT / MIT)

**Venue/Year:** arXiv preprint, 2025

**How K/D are determined:** Diffusion model + energy-based optimization. A diffusion policy is trained to jointly predict position trajectories and impedance profiles (both K and D). The diffusion model generates samples from the learned joint distribution of positions and impedance parameters, and an energy-based refinement step optimizes the impedance profiles for stability and task performance. Both stiffness and damping are independently learned.

**What is output:** Full Cartesian stiffness K and damping D matrices, jointly predicted with position trajectories. The diffusion model outputs the complete impedance profile over a trajectory horizon, not just instantaneous values.

**Robot platform:** KUKA LBR iiwa 14 R820 (7-DoF torque-controlled arm). Evaluated in both simulation and on real hardware. No dexterous hand.

**Tasks:** Contact-rich manipulation tasks including: surface polishing with force regulation, peg insertion with lateral compliance, wiping tasks requiring constant contact force, and object pivoting.

**Key methodology:** Diff-Impedance formulates impedance trajectory prediction as a conditional denoising diffusion process. The model takes visual observations and task conditioning as input and iteratively denoises a joint trajectory of positions and impedance parameters. The energy-based component introduces a physics-informed loss that penalizes impedance profiles that would violate passivity or produce unstable contact behavior. This hybrid approach combines the expressiveness of diffusion models (capturing multimodal demonstration distributions) with physics-based constraints on the impedance output.

**Architecture/Parameters:** Conditional denoising diffusion probabilistic model (DDPM). UNet-based denoiser with visual conditioning (ResNet encoder). Joint output space: position trajectory (6D x horizon) + K trajectory (6D or 36D x horizon) + D trajectory (6D or 36D x horizon). Energy function for stability-aware refinement. Trained on kinesthetic teaching demonstrations on the KUKA iiwa.

**Main contributions:**
- Proposes a diffusion-based approach to jointly learn position trajectories and full impedance profiles (both K and D)
- Energy-based refinement provides physics-informed constraints on the generated impedance, improving stability
- Demonstrates sim-to-real transfer of learned impedance policies on the KUKA iiwa

**Limitations/Gaps:**
- No dexterous hand -- KUKA arm with end-effector tool only
- Diffusion inference is computationally expensive (~10-50 denoising steps), limiting control frequency
- Energy-based refinement adds additional computation; real-time applicability depends on hardware
- Trained on kinesthetic teaching demonstrations, which are labor-intensive to collect
- Does not address multi-contact scenarios (e.g., multiple fingertips)

**Results:** Outperformed fixed-impedance and position-only diffusion policy baselines on all contact-rich tasks. The learned impedance profiles adapted across task phases (e.g., lower stiffness during approach, higher during contact). Successful sim-to-real transfer on the real KUKA iiwa. Code at github.com/StrokeAIRobotics/DiffusionBasedImpedanceLearning.

## Inference / Deployment

- **Inference latency:** Not explicitly benchmarked. Diffusion-based inference requires ~10-50 denoising steps per trajectory prediction, which is computationally expensive. Typical diffusion policy inference latency is 50-500ms per action on a modern GPU, depending on denoising steps and network size.
- **Deployment hardware:** KUKA LBR iiwa 14 R820 for real-robot experiments. GPU for diffusion model inference not specified.
- **Real-time capable?** Limited. Diffusion inference is the bottleneck -- the multi-step denoising process limits control frequency to approximately 2-20 Hz depending on hardware and number of denoising steps. The trajectory-level prediction (outputting an impedance profile over a horizon) partially mitigates this by reducing the required inference frequency.

## Dataset / Data Collection

- **Dataset used:** Custom kinesthetic teaching demonstrations collected on KUKA LBR iiwa 14 R820.
- **Collection method:** Kinesthetic teaching (human physically guides the robot arm). The robot's joint torque sensors capture the demonstrated trajectories and impedance profiles. Sim-to-real transfer evaluated from MuJoCo simulation to real KUKA iiwa.
- **Data scale:** Not explicitly reported. Multiple demonstrations per task (surface polishing, peg insertion, wiping, object pivoting).
- **Teleop equipment:** Kinesthetic teaching (no teleoperation device; direct physical guidance of the KUKA iiwa torque-controlled arm).
- **Data format:** Position trajectories (6D x horizon) + stiffness K trajectories + damping D trajectories. Specific file format not reported.
- **Publicly available?** Code at https://github.com/StrokeAIRobotics/DiffusionBasedImpedanceLearning. Dataset release status not specified.
