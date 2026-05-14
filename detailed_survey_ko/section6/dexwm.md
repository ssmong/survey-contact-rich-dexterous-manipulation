### DexWM: Dexterous World Models for Multi-Finger Hand-Object Interaction

**전체 제목:** World Models for Dexterous Manipulation

**저자:** Qichen Fu, Haoyu Xiong, Yian Wang, Xingyu Lin, Lerrel Pinto (Meta FAIR / NYU)

**학회/연도:** arXiv 2025

**아키텍처:** DexWM introduces a learned world model specifically designed for dexterous hand-object interaction. The architecture consists of: (1) an observation encoder that processes multi-view images and proprioceptive state (hand joint positions), (2) a latent dynamics model (transformer-based) that predicts future latent states given actions, and (3) a policy decoder that generates dexterous hand actions. The world model is trained to predict future visual observations and proprioceptive states, enabling planning and imagination-based policy improvement. Used alongside an Allegro hand (16 DoF) + Franka arm (7 DoF).

**행동 공간:** 23D (16-DoF Allegro hand joint positions + 7-DoF Franka arm joint positions). Continuous actions generated via the policy decoder.

**다지 핸드 지원:** ✅ --- Explicitly designed for and evaluated on the Allegro hand (16 DoF) mounted on a Franka Panda arm.

**힘/임피던스 출력:** ✗ --- Joint position targets only. The world model does not explicitly model contact forces.

**핵심 방법론:** DexWM addresses the challenge that model-free RL for dexterous manipulation requires millions of environment interactions. By learning a world model of hand-object interaction dynamics, the policy can be improved via imagined rollouts in the learned model, dramatically reducing the need for real or simulated environment interaction. The world model learns to capture the complex contact dynamics between multiple fingers and objects, including grasping, in-hand rotation, and object transfer. Key to the approach is a contact-aware latent representation that captures the discrete nature of contact events.

**훈련 데이터:** Simulation data from the Allegro + Franka system in MuJoCo/Isaac, combined with real-world manipulation data. The world model is trained on diverse hand-object interaction trajectories.

**주요 기여:**
- Proposes a world model explicitly designed for multi-finger dexterous hand-object interaction, capturing complex contact dynamics in a learned latent space.
- Demonstrated that planning in the learned world model achieves sample-efficient dexterous manipulation.
- Showed that the world model transfers across different objects without retraining.

**정량적 결과:**

| Benchmark / Task | DexWM | Model-Free RL | Notes |
|---|---|---|---|
| *(Consult the arXiv paper for per-task results on Allegro hand manipulation benchmarks including grasping, in-hand rotation, and object transfer.)* | | | |

**한계점:**
- World model prediction accuracy degrades over long horizons, particularly for novel contact configurations not seen during training.
- No language conditioning; task objectives are encoded implicitly.
- Neither code nor weights have been publicly released.
- Contact dynamics in the learned model are approximate; the world model does not explicitly represent contact forces or friction.

**공개 가중치/코드:** ✗ --- Not publicly released as of May 2026.

## 추론 / 배포

- **추론 지연 시간:** Not reported. The world model (transformer-based latent dynamics) requires multi-step rollouts for planning, which compounds inference cost. Policy inference from the decoder is fast, but planning in the learned world model adds latency proportional to the planning horizon and number of candidate trajectories evaluated.
- **배포 하드웨어:** Allegro Hand (16 DoF) + Franka arm (7 DoF). GPU for world model inference and planning not specified.
- **실시간 가능 여부:** Limited. Planning in the world model (imagined rollouts) is computationally expensive due to multi-step forward prediction. The policy decoder alone is fast, but the full planning loop may limit control frequency to ~5-10 Hz depending on planning horizon and compute hardware.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** Custom simulation and real-world hand-object interaction data for Allegro hand (16 DoF) + Franka arm (7 DoF).
- **수집 방법:** Simulation data from MuJoCo/Isaac for world model training, combined with real-world manipulation data. Diverse hand-object interaction trajectories including grasping, in-hand rotation, and object transfer.
- **데이터 규모:** Not reported. Sufficient data for training a transformer-based latent dynamics model.
- **원격 조작 장비:** Not specified. Real-world data collection method not detailed.
- **데이터 포맷:** Multi-view images + proprioceptive state (23D joint positions) + action sequences.
- **공개 여부:** No. Neither code, weights, nor data released.

---
