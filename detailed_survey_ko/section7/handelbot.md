### 7.4 HandelBot

**전체 제목:** HandelBot: Learning to Play the Piano with Bimanual Dexterous Hands

**저자:** Amber Xie, Kenneth Shaw, Deepak Pathak, et al. (Stanford)

**학회/연도:** arXiv 2026

**arXiv:** https://arxiv.org/abs/2603.12243

**Musical instrument differentiation:** Advances over RoboPianist: real-world LEAP hands, PPO+curriculum, affordable hardware. Primary novelty is sim2real -- demonstrating that piano playing policies can transfer from simulation to physical LEAP Hands on a real piano. RoboPianist provided the benchmark; HandelBot provides the real-world execution.

**RL 알고리즘:** PPO with reward shaping based on musical score. Uses curriculum learning to progressively increase piece difficulty. Teacher-student distillation for real-world deployment.

**핸드 하드웨어:** 2x LEAP Hands (16 DoF each, 32 DoF total bimanual)

**시뮬레이션 플랫폼:** IsaacGym / MuJoCo (for piano contact modeling)

**Sim2Real 여부:** Yes. Demonstrated real piano playing on physical LEAP Hands (real).

**작업:** Bimanual piano playing -- pressing correct keys at correct times according to musical scores. Requires precise finger positioning, coordination between hands, and rapid contact-rich interaction with piano keys.

**핵심 방법론:** HandelBot trains bimanual dexterous policies to play piano pieces by formulating it as an RL problem with musical-score-conditioned rewards. The agent receives the upcoming notes as observations and must coordinate both hands to press the correct keys at the correct times. The contact-rich nature of piano playing (rapid key presses/releases, precise force control) makes this a challenging testbed. Curriculum learning starts with simple melodies and progresses to complex pieces.

**주요 기여:**
- Demonstrated real-world bimanual dexterous piano playing with LEAP Hands (real), a rare example of contact-rich musical manipulation with sim-to-real transfer
- Showed that RL with curriculum learning can handle the precise timing and coordination demands of musical performance
- Used the affordable LEAP Hand platform, making the work more reproducible than Shadow Hand-based approaches

**한계점:** Musical quality metrics are difficult to standardize. Force dynamics of real piano keys vs. simulation may limit expressiveness. Limited to pre-specified scores (no improvisation or adaptation).

**결과:** Successfully played piano pieces on real LEAP Hands (real). Code publicly available.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** Musical scores as task specifications. No pre-collected robot demonstration dataset.
- **수집 방법:** Pure RL (PPO) with curriculum learning in IsaacGym/MuJoCo. Musical score-conditioned rewards. Teacher-student distillation for real-world deployment. Curriculum progresses from simple to complex pieces. Sim-to-real on 2x LEAP Hands (32 DoF total bimanual).
- **데이터 규모:** Musical scores of varying difficulty. Standard parallel RL training.
- **원격 조작 장비:** Not applicable (pure RL, no demonstrations).
- **데이터 포맷:** Musical scores (note sequences with timing). Simulation environments.
- **공개 여부:** Code publicly available.

## 추론 / 배포

- **추론 지연 시간:** Not explicitly reported. The distilled student MLP policy runs in <1ms per forward pass. Musical timing requires precise, low-latency control.
- **배포 하드웨어:** 2x LEAP Hands (16 DoF each, 32 DoF total bimanual) on a physical piano. Policy trained in IsaacGym/MuJoCo; deployed via sim-to-real transfer.
- **실시간 가능 여부:** Yes. Real-time piano playing demonstrated on physical LEAP Hands, requiring precise temporal coordination at musical tempos.
