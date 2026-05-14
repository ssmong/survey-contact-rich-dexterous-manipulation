# 6. VLA Foundation Models: Version History

This section provides detailed entries for the major vision-language-action (VLA) model families and visuomotor policies surveyed in the main table. Each entry covers architecture, action representation, training data, contributions, and gaps relevant to contact-rich dexterous manipulation.

**Notation:** ✅ = available/supported, ✗ = not available/not supported, — = not reported or not applicable.

## File Index

### VLA Foundation Model Families
- [pi_family.md](pi_family.md) — Physical Intelligence pi0 / pi0-FAST / pi0.5 / pi0.6 / pi0.7
- [groot_family.md](groot_family.md) — NVIDIA GR00T N1 / N1.5 / N1.6 / N1.7

### Other Major VLAs
- [rt2.md](rt2.md) — RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control
- [openvla.md](openvla.md) — OpenVLA: An Open-Source Vision-Language-Action Model
- [openvla_oft.md](openvla_oft.md) — OpenVLA-OFT: Optimal Fine-Tuning
- [octo.md](octo.md) — Octo: An Open-Source Generalist Robot Policy
- [rdt1b.md](rdt1b.md) — RDT-1B: Robotics Diffusion Transformer
- [hpt.md](hpt.md) — HPT: Heterogeneous Pre-trained Transformers
- [cogact.md](cogact.md) — CogACT: Synergizing Cognition and Action
- [egoscale.md](egoscale.md) — EgoScale: Scaling Egocentric Human Video Pre-training
- [simplevla_rl.md](simplevla_rl.md) — SimpleVLA-RL: RL Fine-Tuning of VLAs
- [uniact.md](uniact.md) — UniAct: Universal Action Tokenization

### Visuomotor Policies
- [diffusion_policy.md](diffusion_policy.md) — Diffusion Policy: Visuomotor Policy Learning via Action Diffusion
- [act_aloha.md](act_aloha.md) — ACT / ALOHA: Learning Fine-Grained Bimanual Manipulation
- [dp3.md](dp3.md) — DP3: 3D Diffusion Policy
- [idp3.md](idp3.md) — iDP3: Improved 3D Diffusion Policy via Egocentric Point Clouds
- [dexwm.md](dexwm.md) — DexWM: Dexterous World Models

---

## Cross-cutting Observations

**Action representation remains the central design choice.** The surveyed models adopt fundamentally different approaches to action representation: discrete tokens (RT-2, OpenVLA), continuous flow matching (pi0, GR00T), diffusion (Diffusion Policy, RDT-1B, DP3), CVAE (ACT), and universal codebooks (UniAct). Each choice carries tradeoffs for dexterous manipulation: discrete tokens suffer quantization at high DoF, continuous methods handle multi-modality but are slower, and codebooks require sufficient training diversity. No single approach has demonstrated clear superiority for high-DoF dexterous action spaces.

**Dexterous hand support is the exception, not the rule.** Of the 19 models/families surveyed in this section, only 4 have any form of dexterous hand support: DP3 (simulation only), iDP3 (real-world Inspire hand), DexWM (Allegro hand), and EgoScale (representation-level only --- 22-DoF hand pose extraction from video, not physical robot deployment). The two major VLA families (pi and GR00T) remain entirely gripper-centric across all versions. This gap is not merely a matter of data availability --- the fundamental action representations, training pipelines, and evaluation protocols of mainstream VLAs are designed around 7D gripper actions.

**Force and impedance output is absent across all surveyed models.** None of the 19 models in this section output force targets, impedance parameters, or any form of compliance specification. This is a universal gap: both VLA foundation models and visuomotor policies generate only position (or velocity) targets, relying on low-level PD controllers for contact handling. For contact-rich dexterous manipulation --- where regulating per-finger contact forces is essential --- this represents a fundamental capability gap that cannot be addressed by scaling model size or training data within current architectures.

**The VLM backbone upgrade cycle is accelerating.** Both pi and GR00T families have upgraded their VLM backbones multiple times within 18 months: pi moved from PaliGemma 3B to Gemma 3 4B; GR00T moved from Eagle-2 to Eagle 2.5 to Cosmos-2B to Cosmos-Reason2-2B. Each upgrade brings improved visual understanding and reasoning, but the action head architectures remain relatively stable (flow matching for pi, DiT for GR00T). This suggests the community views VLM backbone quality as the primary scaling axis, while action generation is treated as a solved architectural problem --- a potentially problematic assumption for dexterous manipulation where action representation complexity is the bottleneck.

**Open-source availability correlates with adoption but not with dexterous capability.** The most widely adopted models (Diffusion Policy, ACT, OpenVLA, Octo, pi0) are fully open-source, while the most capable dexterous systems (EgoScale, DexWM) are closed. This creates a gap where the tools most accessible to the research community are those least suited to dexterous manipulation research, potentially slowing progress at the VLA-dexterity intersection.

**Inference speed constrains real-time dexterous control.** Dexterous manipulation typically requires 20-50 Hz control rates for stable finger contact. Most VLAs operate at 1-12 Hz: RT-2 at ~1-3 Hz, OpenVLA at ~4-6 Hz, GR00T N1.7 at 12 Hz (GPU) or 4.6 Hz (edge). Only the lightweight visuomotor policies (Diffusion Policy, ACT, DP3) approach the frequencies needed for dexterous control, but these lack language conditioning and cross-embodiment generalization. Bridging this speed-capability gap --- achieving both VLA-level generalization and visuomotor-policy-level control frequency --- remains an open challenge.
