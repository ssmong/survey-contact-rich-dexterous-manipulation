### 2.7 VLA + Diffusion Policy Switching

**Full title:** Bi-Manual Dexterous Manipulation via Reinforcement Learning with Vision-Language Action Switching

**Authors:** Cheng Pan, Kai Junge, Benhui Dai, Qinghua Guan, Josie Hughes (CREATE Lab, STI, EPFL, Lausanne; Embodied AI, Lausanne)

**Venue/Year:** arXiv preprint, 2024

**arXiv:** [2410.14022](https://arxiv.org/abs/2410.14022)

**Hand hardware:** ADAPT Hand (13 DoF) -- a series-elastic, tendon-driven multi-finger hand designed for compliant manipulation

**Tasks:**
- Pick-and-place with dexterous multi-finger hand
- VLA-guided manipulation with policy switching between high-level VLA commands and low-level diffusion policy execution

**Key methodology:** This work proposes a switching mechanism between a vision-language-action model and a diffusion policy for dexterous manipulation on a series-elastic multi-finger hand. The VLA handles high-level task understanding and coarse motion planning from language instructions, while the diffusion policy takes over for fine-grained dexterous control during contact-rich phases. The switching logic determines when to transition between VLA-level commands and diffusion-level execution based on task state. The ADAPT Hand's series-elastic actuation provides inherent mechanical compliance, complementing the position-based policy output.

**Architecture/Parameters:**
- High-level: VLA model for language-conditioned task understanding
- Low-level: diffusion policy for fine-grained dexterous action generation
- Switching mechanism: state-dependent transition between VLA and diffusion policy
- Hand: ADAPT Hand with 13 DoF and series-elastic elements
- Specific model sizes not publicly detailed

**Main contributions:**
- Proposed a VLA-to-diffusion policy switching framework for dexterous manipulation, leveraging the strengths of each: VLAs for semantic understanding and diffusion policies for precise motor control
- Demonstrated the approach on a series-elastic multi-finger hand (ADAPT, 13 DoF), one of the few VLA works to target a compliant dexterous hand rather than rigid position-controlled hands
- Highlighted the value of mechanical compliance (series-elastic actuation) as a complement to learned position policies in contact-rich settings

**Limitations/Gaps:**
- No open-source code or model weights released
- Limited task diversity: primarily pick-and-place; does not cover tool use, assembly, or in-hand manipulation
- The switching mechanism is relatively simple; more sophisticated arbitration (e.g., learned switching, continuous blending) is not explored
- No explicit force or impedance output from the policy; compliance comes from the hand's mechanical design rather than learned control
- Single hand platform (ADAPT 13 DoF); no cross-embodiment evaluation
- Evaluation scope appears limited compared to other works in this section

**Results:**

**Pick-and-place success (5 trials per object-placement combination):**

| Method | Avg. Success Score |
|---|---|
| VLA-only (pepper) | 0.43 |
| VLA-only (tape) | 0.23 |
| **VLA + Diffusion switching** | **0.82** |

VLA+Diffusion switching improves over VLA-only by ~90% for pepper and ~257% for tape.

**Compliance vs. rigid configuration:**

| Condition | Compliant | Rigid |
|---|---|---|
| Knob-turning with size variation | +58% avg. improvement over rigid | baseline |
| Control noise robustness (Gaussian N(0,5)mm) | <8% performance decrease | 74% performance decrease |
| Spring contact stability | +38% improvement | baseline |

**Multi-step dexterous tasks (10 trials each):**

| Task | Success Rate |
|---|---|
| Water bottle opening & pouring | >0.6 |
| Sticky note peeling & pasting | >0.6 |
| Multi-object grasping | >0.6 |

**Initial configuration sensitivity:** >50% success when hand starts within ~15 cm of target; drops below 50% beyond 15 cm offset (8 trials per distance).

**Data collection:** 20 demonstration trajectories per object-placement (pick-and-place); 30 demonstrations per dexterous task; ~5 Hz sampling frequency.

- Demonstrated VLA + diffusion policy switching on the 13-DoF ADAPT Hand
- Series-elastic actuation provides useful passive compliance during contact, with quantified robustness gains
- No public code or weights available

## Inference / Deployment

- **Inference latency:** Not reported. Demonstration data was collected at ~5 Hz sampling frequency, but this reflects data capture rate, not deployment control frequency.
- **Deployment hardware:** UR5 robotic arm + ADAPT Hand (13 DoF) with series-elastic actuation. Vision/sensor processing on Raspberry Pi 4B units. Inference GPU not specified.
- **Real-time capable?** Not verified. The paper does not report autonomous execution control frequency or inference latency. The switching mechanism between VLA and diffusion policy may introduce variable latency depending on which mode is active.

## Dataset / Data Collection

- **Dataset used:** Custom demonstration dataset. "Minimal demonstration data" mentioned in the abstract.
- **Collection method:** Teleoperated demonstrations on the UR5 + ADAPT Hand (13 DoF) system. Data collected at ~5 Hz sampling frequency.
- **Data scale:** 20 demonstration trajectories per object-placement combination (pick-and-place tasks); 30 demonstration trajectories per dexterous task (tasks A--C).
- **Teleop equipment:** Not detailed. The ADAPT Hand uses series-elastic, tendon-driven actuation; teleoperation interface specifics are not disclosed.
- **Data format:** Not reported.
- **Publicly available?** No. No code, data, or model weights publicly released.
