### 7.4 HandelBot

**Full title:** HandelBot: Learning to Play the Piano with Bimanual Dexterous Hands

**Authors:** Amber Xie, Kenneth Shaw, Deepak Pathak, et al. (Stanford)

**Venue/Year:** arXiv 2026

**arXiv:** https://arxiv.org/abs/2603.12243

**Musical instrument differentiation:** Advances over RoboPianist: real-world LEAP hands, PPO+curriculum, affordable hardware. Primary novelty is sim2real -- demonstrating that piano playing policies can transfer from simulation to physical LEAP Hands on a real piano. RoboPianist provided the benchmark; HandelBot provides the real-world execution.

**RL algorithm:** PPO with reward shaping based on musical score. Uses curriculum learning to progressively increase piece difficulty. Teacher-student distillation for real-world deployment.

**Hand hardware:** 2x LEAP Hands (16 DoF each, 32 DoF total bimanual)

**Sim platform:** IsaacGym / MuJoCo (for piano contact modeling)

**Sim2Real?** Yes. Demonstrated real piano playing on physical LEAP Hands (real).

**Tasks:** Bimanual piano playing -- pressing correct keys at correct times according to musical scores. Requires precise finger positioning, coordination between hands, and rapid contact-rich interaction with piano keys.

**Key methodology:** HandelBot trains bimanual dexterous policies to play piano pieces by formulating it as an RL problem with musical-score-conditioned rewards. The agent receives the upcoming notes as observations and must coordinate both hands to press the correct keys at the correct times. The contact-rich nature of piano playing (rapid key presses/releases, precise force control) makes this a challenging testbed. Curriculum learning starts with simple melodies and progresses to complex pieces.

**Main contributions:**
- Demonstrated real-world bimanual dexterous piano playing with LEAP Hands (real), a rare example of contact-rich musical manipulation with sim-to-real transfer
- Showed that RL with curriculum learning can handle the precise timing and coordination demands of musical performance
- Used the affordable LEAP Hand platform, making the work more reproducible than Shadow Hand-based approaches

**Limitations/Gaps:** Musical quality metrics are difficult to standardize. Force dynamics of real piano keys vs. simulation may limit expressiveness. Limited to pre-specified scores (no improvisation or adaptation).

**Results:** Successfully played piano pieces on real LEAP Hands (real). Code publicly available.

## Dataset / Data Collection

- **Dataset used:** Musical scores as task specifications. No pre-collected robot demonstration dataset.
- **Collection method:** Pure RL (PPO) with curriculum learning in IsaacGym/MuJoCo. Musical score-conditioned rewards. Teacher-student distillation for real-world deployment. Curriculum progresses from simple to complex pieces. Sim-to-real on 2x LEAP Hands (32 DoF total bimanual).
- **Data scale:** Musical scores of varying difficulty. Standard parallel RL training.
- **Teleop equipment:** Not applicable (pure RL, no demonstrations).
- **Data format:** Musical scores (note sequences with timing). Simulation environments.
- **Publicly available?** Code publicly available.

## Inference / Deployment

- **Inference latency:** Not explicitly reported. The distilled student MLP policy runs in <1ms per forward pass. Musical timing requires precise, low-latency control.
- **Deployment hardware:** 2x LEAP Hands (16 DoF each, 32 DoF total bimanual) on a physical piano. Policy trained in IsaacGym/MuJoCo; deployed via sim-to-real transfer.
- **Real-time capable?** Yes. Real-time piano playing demonstrated on physical LEAP Hands, requiring precise temporal coordination at musical tempos.
