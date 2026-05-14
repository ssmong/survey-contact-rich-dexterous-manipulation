### SimpleVLA-RL: Reinforcement Learning Fine-Tuning of Vision-Language-Action Models

**Full title:** SimpleVLA-RL: Reinforcement Learning for Vision-Language-Action Models

**Authors:** PRIME-RL team

**Venue/Year:** ICLR 2026

**Architecture:** SimpleVLA-RL applies reinforcement learning (RL) fine-tuning to a pre-trained VLA model. The base VLA is a vision-language-action model (architecture details follow the standard Prismatic/OpenVLA design). The RL fine-tuning adds a value head to the VLA and uses policy gradient methods (PPO-style) to optimize task performance beyond what imitation learning achieves. The VLA backbone is kept frozen or minimally adapted during RL fine-tuning.

**Action space:** Inherits the base VLA's action space (typically 7D EEF + gripper).

**Dex hand support?** ✗ --- Evaluated on standard manipulation benchmarks with gripper robots.

**Force/impedance output?** ✗ --- Position targets only.

**Key methodology:** SimpleVLA-RL addresses the fundamental limitation that imitation learning (IL) can only match the performance of the demonstration data. By applying RL fine-tuning to a pre-trained VLA, the model can discover strategies that exceed human-demonstrated performance. The approach uses the VLA's pre-trained representations as initialization for RL, providing a strong prior that accelerates RL training and avoids the sample inefficiency of training from scratch. A task-specific reward function guides the RL optimization.

**Training data:** Pre-trained VLA from standard cross-embodiment datasets (OXE). RL fine-tuning uses environment interaction, not demonstrations.

**Main contributions:**
- Applied RL fine-tuning to pre-trained VLAs, validating the known principle that RL can exceed the imitation learning ceiling, specifically in the VLA context. The contribution is the specific recipe --- demonstrating how to practically apply PPO-style RL to a pre-trained VLA without catastrophic forgetting --- rather than the theoretical insight itself, which is well-established in the broader RL literature.
- Provided a simple and reproducible recipe for applying RL to pre-trained VLAs.
- Showed that VLA representations provide a strong initialization that makes RL sample-efficient compared to training from scratch.

**Quantitative results:**

| Benchmark / Task | SimpleVLA-RL | IL-only VLA | Notes |
|---|---|---|---|
| *(Consult the ICLR 2026 paper for per-task results. The paper reports improvements over imitation-learning-only VLA baselines on manipulation benchmarks.)* | | | |

**Limitations/Gaps:**
- RL fine-tuning requires a reward function, which may be difficult to specify for contact-rich or dexterous tasks.
- Evaluated only on gripper-based manipulation; applicability to high-DoF dexterous systems is unknown.
- No force/compliance awareness in the reward or action space.

**Open weights/code:** ✅ Code: [GitHub](https://github.com/PRIME-RL/SimpleVLA-RL). ✗ Model weights not publicly available.

## Inference / Deployment

- **Inference latency:** Inherits the base VLA's inference speed. If built on OpenVLA-class architecture (~7B parameters), inference is approximately 4-6 Hz on a high-end GPU. The RL fine-tuning does not change the model architecture, so inference speed is unchanged from the pre-trained VLA.
- **Deployment hardware:** Same as the base VLA (requires a high-end GPU for 7B-class models). RL fine-tuning requires simulation environments for online interaction.
- **Real-time capable?** Depends on the base VLA. If the base VLA is real-time capable, the RL-fine-tuned version inherits the same inference speed.

## Dataset / Data Collection

- **Dataset used:** Pre-trained VLA from standard cross-embodiment datasets (OXE). RL fine-tuning uses online environment interaction, not pre-collected demonstrations.
- **Collection method:** Two-phase: (1) VLA pretraining via imitation learning on OXE cross-embodiment data, (2) RL fine-tuning via online interaction with task environments (PPO-style policy gradient). No additional demonstration data for RL phase.
- **Data scale:** OXE pretraining scale (inherited from base VLA). RL fine-tuning: online interaction, episode counts depend on task complexity.
- **Teleop equipment:** Not applicable for RL fine-tuning phase. Pretraining data uses standard OXE teleoperation methods.
- **Data format:** RLDS for pretraining (OXE). Online RL rollouts during fine-tuning.
- **Publicly available?** OXE pretraining data is public. RL fine-tuning generates data online (no offline dataset to release).

---
