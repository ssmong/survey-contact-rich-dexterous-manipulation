### RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control

**Full title:** RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control

**Authors:** Anthony Brohan, Noah Brown, Justice Carbajal, Yevgen Chebotar, Xi Chen, Krzysztof Choromanski, Tianli Ding, Danny Driess, Avinava Dubey, Chelsea Finn, Pete Florence, Chuyuan Fu, Montse Gonzalez Arenas, Keerthana Gopalakrishnan, Kehang Han, Karol Hausman, Alexander Herzog, Jasmine Hsu, Brian Ichter, Alex Irpan, Nikhil Joshi, Ryan Julian, Dmitry Kalashnikov, Yuheng Kuang, Isabel Leal, Lisa Lee, Tsang-Wei Edward Lee, Sergey Levine, Yao Lu, Henryk Michalewski, Igor Mordatch, Karl Pertsch, Kanishka Rao, Krista Reymann, Michael Ryoo, Grecia Salazar, Pannag Sanketi, Pierre Sermanet, Jaspiar Singh, Anikait Singh, Radu Soricut, Huong Tran, Vincent Vanhoucke, Quan Vuong, Ayzaan Wahid, Stefan Welker, Paul Wohlhart, Jialin Wu, Fei Xia, Ted Xiao, Peng Xu, Sichun Xu, Tianhe Yu, Brianna Zitkovich (Google DeepMind)

**Venue/Year:** CoRL 2023

**Architecture:** RT-2 co-fine-tunes a large vision-language model (PaLI-X 55B or PaLM-E 12B) to output robot actions as text tokens alongside natural language. The VLM backbone is either PaLI-X (55B parameters, ViT-22B vision encoder) or PaLM-E (12B parameters). There is no separate action head; actions are tokenized as integers in the range [0, 255] and decoded autoregressively as part of the language output sequence.

**Action space:** 7D for the RT-2 robot (6-DoF end-effector pose delta + gripper open/close), discretized into 256 bins per dimension. Actions are represented as text strings (e.g., "1 128 91 241 5 101 127") in the VLM's output vocabulary.

**Dex hand support?** ✗ --- Designed for a single-arm mobile manipulator with a parallel-jaw gripper.

**Force/impedance output?** ✗ --- Position targets only.

**Key methodology:** RT-2 demonstrates that pre-trained vision-language models can be directly fine-tuned to output robot actions by representing actions as token sequences in the VLM's existing vocabulary. The key insight is that web-scale visual and semantic knowledge transfers to robotic manipulation: the model exhibits emergent capabilities such as reasoning about novel objects, following complex instructions, and performing rudimentary chain-of-thought planning --- abilities not present in the robot training data. This established the VLA paradigm of leveraging internet-scale VLM pretraining for robot control.

**Training data:** Robot data from the RT-2 fleet: ~130K episodes on approximately 700 tasks from Google's mobile manipulators. Co-fine-tuned with web-scale vision-language data from PaLI-X or PaLM-E pretraining corpora.

**Main contributions:**
- Established the VLA paradigm: showed that co-fine-tuning a VLM on robot data yields emergent semantic reasoning and generalization capabilities for manipulation.
- Demonstrated positive transfer from web-scale data to robot control, with the 55B PaLI-X variant significantly outperforming the 12B PaLM-E variant on novel object and instruction generalization.
- Introduced chain-of-thought reasoning for robotic manipulation, where the VLM generates intermediate reasoning steps before action tokens.

**Quantitative results:**

| Evaluation Category | RT-2 (PaLI-X 55B) | RT-2 (PaLM-E 12B) | RT-1 Baseline | Notes |
|---|---|---|---|---|
| *(Results not independently verified --- arXiv page could not be fetched. The paper reports improvements over RT-1 on seen tasks and substantial gains on novel object/instruction generalization. Consult CoRL 2023 paper for per-category success rates.)* | | | | |

**Limitations/Gaps:**
- Extremely large model (55B) with slow inference (~1-3 Hz), impractical for real-time dexterous control.
- Closed-source: no weights, code, or training data released. This severely limits reproducibility and community extension.
- Limited to Google's specific robot embodiment; no cross-embodiment capability.
- Autoregressive action tokenization introduces quantization error and sequential decoding latency.

**Open weights/code:** ✗ --- Fully closed. No public weights, code, or data.

## Inference / Deployment

- **Inference latency:** RT-2 (PaLI-X 55B) runs at approximately 1-3 Hz due to the massive 55B parameter model and sequential autoregressive action token decoding (7 tokens decoded one at a time). The smaller PaLM-E 12B variant is faster but still limited to ~3-5 Hz. Each action requires decoding 7 sequential tokens through the full VLM.
- **Deployment hardware:** Google's internal TPU infrastructure for the 55B model. The PaLM-E 12B variant may run on high-end GPUs but still requires substantial compute. Not deployable on edge devices.
- **Real-time capable?** No, for dexterous manipulation. At 1-3 Hz (55B) or 3-5 Hz (12B), RT-2 is too slow for tasks requiring >10 Hz control. The autoregressive token-by-token decoding of 7D actions is inherently sequential and cannot be parallelized. Suitable only for slow, coarse manipulation tasks on Google's mobile manipulators.

## Dataset / Data Collection

- **Dataset used:** Google's internal robot fleet data (~130K episodes across ~700 tasks) co-fine-tuned with web-scale vision-language pretraining corpora from PaLI-X or PaLM-E.
- **Collection method:** Teleoperation on Google's mobile manipulator fleet. Robot data combined with internet-scale image-text pairs for co-fine-tuning the VLM backbone.
- **Data scale:** ~130K robot episodes across ~700 tasks. Web-scale VLM pretraining data (billions of image-text pairs from PaLI-X/PaLM-E).
- **Teleop equipment:** Not specified. Google's internal teleoperation setup for mobile manipulators.
- **Data format:** Not disclosed (internal Google format).
- **Publicly available?** No. Fully closed -- no robot data, weights, or code released.

---
