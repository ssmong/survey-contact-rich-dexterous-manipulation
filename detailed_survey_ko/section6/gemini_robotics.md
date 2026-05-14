# Gemini Robotics Family

> Google DeepMind's VLA model family built on Gemini 2.0, evolving from cloud-based to on-device deployment.

---

## 버전 이력

| Version | Date | VLM Backbone | Dex Hand | Force Output | Availability | Key Advance |
|---------|------|-------------|----------|-------------|-------------|-------------|
| **Gemini Robotics** | Mar 2025 | Gemini 2.0 | ✗ (gripper) | ✗ | Closed (trusted testers) | First Gemini-based VLA; 2x generalization benchmark |
| **Gemini Robotics-ER** | Mar 2025 | Gemini 2.0 | N/A (reasoning only) | N/A | Closed | Embodied Reasoning: spatial understanding, grasp prediction |
| **Gemini Robotics On-Device** | Jul 2025 | Gemini 2.0 (distilled) | ✗ | ✗ | SDK (trusted testers) | On-device inference, no network; fine-tune with 50-100 demos |
| **Gemini Robotics 1.5** | 2026 | Gemini (upgraded) | ✗ | ✗ | Trusted testers; ER 1.5 via API | VLA + reasoning; 15 academic benchmarks |
| **Gemini Robotics-ER 1.6** | Apr 2026 | Gemini (upgraded) | N/A | N/A | Via API | Enhanced spatial reasoning, multi-view understanding |

---

## Full Title

"Gemini Robotics: Bringing AI into the Physical World"

**저자:** Gemini Robotics Team, Google DeepMind (Saminda Abeyruwan, Joshua Ainslie, et al.; 117+ authors)

**학회/연도:** arXiv 2503.20020, March 2025 (subsequent versions announced via blog posts)

## Architecture

- **VLM backbone:** Gemini 2.0 foundation model with physical actions added as new output modality
- **Parameter count:** Not disclosed
- **행동 공간:** Direct motor commands from visual input + language instructions; dimensionality not publicly documented
- **Inference speed:** Not disclosed for any version. On-Device version runs locally without network dependency, suggesting optimized latency, but no Hz figures published.

## 로봇 플랫폼

| Platform | Type | Configuration |
|----------|------|---------------|
| ALOHA 2 | Bi-arm static | Primary training platform |
| Franka FR3 | Bi-arm collaborative | Cross-embodiment evaluation |
| Apptronik Apollo | Humanoid | Partnership demonstration |

## Tasks

Demonstrated capabilities include:
- Origami folding
- Packing items into Ziploc bags
- Unzipping bags
- Folding clothes
- Industrial belt assembly
- Open-vocabulary instruction following
- Long-horizon dexterous sequences

Specific task count and per-task success rates not publicly reported.

## Main Contributions

- Built on Gemini 2.0 as the first major foundation model to add physical actions as a native output modality alongside text, code, and images
- Reports 2x performance on a comprehensive generalization benchmark compared to other SOTA VLAs (specific benchmark and numbers not fully disclosed)
- Gemini Robotics-ER introduces embodied spatial reasoning (object detection, trajectory prediction, grasp prediction, multi-view correspondence) as a complementary capability to direct control
- On-Device variant enables deployment without cloud dependency, with fine-tuning from as few as 50-100 demonstrations

## Limitations/Gaps

- **No dexterous hand support.** All demonstrated platforms use parallel-jaw grippers (ALOHA, Franka) or humanoid-integrated hands (Apollo). No standalone multi-finger dexterous hand evaluation.
- **No force/torque output.** No mention of force sensing, impedance control, or compliance in any version.
- **Fully closed.** No open weights, no open code (except limited SDK for On-Device). Cannot be reproduced, fine-tuned by the community, or independently benchmarked. This is a more restrictive access model than RT-2 (which was also closed but at least published detailed results in a peer-reviewed venue).
- **Quantitative opacity.** "2x SOTA" claim lacks specifics: which benchmark, which baselines, what metric. Success rates for individual tasks not published.
- **Inference latency unknown.** Critical for real-time dexterous manipulation; not disclosed for any version.
- **Parameter count undisclosed.** Makes it impossible to assess compute requirements or compare efficiency with open VLAs.

## 다른 주요 VLA 패밀리와의 비교

| Dimension | Gemini Robotics | pi0~0.7 | GR00T N1~1.7 |
|-----------|----------------|---------|--------------|
| Open weights | ✗ | ✅ (pi0/0.5) | ✅ (all) |
| Dex hand | ✗ | ✗ | Humanoid-integrated |
| Force output | ✗ | ✗ | ✗ |
| On-device | ✅ (On-Device) | ✗ | ✅ (Jetson Orin) |
| Cross-embodiment | 3 platforms | 1 platform | Humanoid-focused |
| Param count | Undisclosed | ~3.3-5B | 2.2-3B |

## Results

| Metric | Value | Context |
|--------|-------|---------|
| Generalization benchmark | 2x vs SOTA VLAs | Benchmark identity not disclosed |
| ER end-to-end control | 2x-3x vs Gemini 2.0 base | On ER-specific spatial tasks |
| Fine-tuning efficiency | 50-100 demos | On-Device variant |
| Per-task success rates | Not disclosed | — |

> **Editorial note:** The quantitative claims are difficult to evaluate independently due to the fully closed nature of the model and the lack of benchmark specificity. The "2x SOTA" claim should be treated with caution until independently replicated or published in a peer-reviewed venue.

## 추론 / 배포

- **추론 지연 시간:** Not disclosed for any version. The On-Device variant runs locally without network dependency, suggesting optimized latency for edge deployment, but no Hz figures have been published. The cloud-based Gemini Robotics version presumably has higher latency due to network round-trips.
- **배포 하드웨어:** On-Device variant targets embedded/edge hardware (specific device not disclosed). Cloud versions run on Google TPU infrastructure. Parameter count undisclosed, making compute requirements impossible to assess.
- **실시간 가능 여부:** Unknown. The On-Device variant is designed for real-time control without network dependency, but no control frequency or latency figures have been published. This is a critical gap given that inference speed is essential for dexterous manipulation deployment.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** Not disclosed. Training data details are not publicly reported due to the fully closed nature of the model.
- **수집 방법:** Not disclosed. Primary training platform is ALOHA 2 (bimanual), with cross-embodiment evaluation on Franka FR3 and Apptronik Apollo humanoid. On-Device variant supports fine-tuning from 50-100 demonstrations.
- **데이터 규모:** Not disclosed. The scale of internal Google DeepMind robot data is unknown.
- **원격 조작 장비:** Not disclosed. ALOHA 2 uses leader-follower teleoperation.
- **데이터 포맷:** Not disclosed.
- **공개 여부:** No. Fully closed -- no weights, code, training data, or dataset details released. Limited SDK access for On-Device variant to trusted testers only.
