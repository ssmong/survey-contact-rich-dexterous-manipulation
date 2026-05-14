### 5.12 DCM

**전체 제목:** DCM: Diffusion Contact Model for Compliant Manipulation

**저자:** (OMRON SINIC X)

**학회/연도:** IROS 2024

**K/D 결정 방법:** The system takes variable impedance control (VIC) parameters as input (not output). DCM is a diffusion-based contact dynamics model that predicts the outcome of applying a given impedance configuration to a contact-rich manipulation scenario. It does not generate impedance parameters; rather, it models the consequences of impedance choices, enabling downstream planning or optimization to select appropriate K/D.

**출력:** Predicted contact state transitions (position, force, contact geometry) given a VIC impedance configuration as input. The diffusion model generates distributions over future states conditioned on the current state and chosen impedance parameters. Not an impedance generator but an impedance-conditioned world model.

**로봇 플랫폼:** Robot arm + gripper. No dexterous hand. Evaluated on real hardware.

**작업:** Contact-rich manipulation tasks where the outcome depends on the chosen impedance configuration: insertion tasks with varying clearances, assembly tasks where compliance affects alignment success.

**핵심 방법론:** DCM formulates contact dynamics prediction as a conditional diffusion process. Given the current state (position, contact forces, object pose) and a proposed VIC impedance configuration (K, D), the diffusion model generates samples from the distribution of possible next states. This allows planning algorithms to evaluate different impedance choices by predicting their outcomes -- effectively serving as a "what-if" simulator for impedance-conditioned contact dynamics. The diffusion framework captures the multimodality of contact outcomes (e.g., a peg might slide into the hole or jam depending on impedance settings).

**아키텍처/파라미터:** Conditional DDPM for contact state prediction. Input conditioning: current state + VIC parameters (K, D). Output: distribution over next state (position, force). Trained on real contact interaction data. No separate impedance generator -- the diffusion model is the contact dynamics predictor.

**주요 기여:**
- Diffusion-based contact dynamics model conditioned on impedance parameters, enabling "what-if" analysis of impedance choices
- Captures multimodal contact outcomes (success/failure modes) as a distribution, not a point prediction
- Can be integrated with downstream planners for impedance-aware manipulation planning

**한계점:**
- Does not output impedance parameters -- it is a contact model, not an impedance controller
- No dexterous hand -- arm + gripper
- Requires real contact interaction data for training the diffusion model
- Computational cost of diffusion sampling may limit online planning speed
- No code or weights released
- Not a standalone controller; requires a separate planner or optimizer to use its predictions

**결과:** DCM produced more accurate and diverse contact state predictions than deterministic dynamics models and simple Gaussian models. The predicted contact outcome distributions correctly captured success/failure modes for different impedance configurations in insertion tasks. When integrated with a simple planner, DCM-guided impedance selection outperformed fixed-impedance baselines.

## 추론 / 배포

- **추론 지연 시간:** Not explicitly reported. As a diffusion-based model, DCM requires multiple denoising steps per prediction, with typical inference latency of 50-500ms per sample on a modern GPU. Planning with DCM requires multiple samples to evaluate different impedance configurations, further increasing total computation time.
- **배포 하드웨어:** Real hardware evaluation (robot arm + gripper). GPU for diffusion model inference not specified.
- **실시간 가능 여부:** Limited. Diffusion sampling for contact state prediction is computationally expensive, and using DCM for online planning (evaluating multiple impedance configurations) compounds the cost. Best suited for offline impedance selection or slow-rate online replanning rather than high-frequency real-time control.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** Custom real contact interaction dataset collected on robot arm + gripper for insertion/assembly tasks.
- **수집 방법:** Real-robot contact interaction data. The diffusion contact model is trained on trajectories of (state, impedance parameters, next state) tuples collected during contact-rich manipulation with varying impedance configurations.
- **데이터 규모:** Not reported. Number of interaction trajectories and total data volume not specified in available materials.
- **원격 조작 장비:** Not applicable (data collected through automated interaction, not teleoperation).
- **데이터 포맷:** State transition tuples: (current position, contact forces, object pose, VIC parameters K/D) -> (next state). Specific file format not reported.
- **공개 여부:** No. No code or weights released.
