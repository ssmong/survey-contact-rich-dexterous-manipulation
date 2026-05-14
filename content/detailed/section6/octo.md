### Octo: An Open-Source Generalist Robot Policy

**Full title:** Octo: An Open-Source Generalist Robot Policy

**Authors:** Octo Model Team: Dibya Ghosh, Homer Walke, Karl Pertsch, Kevin Black, Oier Mees, Sudeep Dasari, Joey Hejna, Tobias Kreiman, Charles Xu, Jianlan Luo, You Liang Tan, Lawrence Yunliang Chen, Pannag Sanketi, Quan Vuong, Ted Xiao, Dorsa Sadigh, Chelsea Finn, Sergey Levine

**Venue/Year:** RSS 2024

**Architecture:** Octo is a 93M parameter transformer-based policy (not a VLA in the strict sense, as it lacks a large pre-trained VLM backbone). It uses a modular architecture with separate tokenizers for images, language (via a frozen language model encoder), and proprioceptive state. These are combined via a transformer backbone that attends over all input tokens. The action head is a diffusion-based decoder that generates continuous actions conditioned on a readout token from the transformer.

**Action space:** Configurable per embodiment. Typically 7D (6-DoF EEF + gripper) but supports arbitrary action dimensions via the modular tokenizer design. Can represent both absolute and delta actions.

**Dex hand support?** ✗ --- Evaluated only on gripper-based systems, though the modular action head could accommodate higher-dimensional action spaces if training data included such demonstrations.

**Force/impedance output?** ✗ --- Position targets only.

**Key methodology:** Octo is designed as a lightweight, modular generalist policy that can be efficiently fine-tuned to new robot embodiments, sensor configurations, and action spaces. Unlike VLAs that inherit a massive VLM backbone, Octo trains its transformer from scratch on robot data, keeping the model small enough for fast inference and fine-tuning. The diffusion action head supports multi-modal action distributions, avoiding the mode-averaging problem of regression-based policies. The modular tokenizer design allows adding or removing observation modalities (e.g., wrist cameras, different proprioceptive formats) without architectural changes.

**Training data:** Pretrained on 800K robot episodes from the Open X-Embodiment (OXE) dataset. Fine-tuning demonstrated on WidowX, Franka, and various manipulation platforms with as few as 50 demonstrations.

**Main contributions:**
- Demonstrated that a small (93M) generalist policy can match or exceed much larger VLAs on fine-tuned downstream tasks *on the specific benchmarks tested*, challenging the assumption that VLA performance scales primarily with model size. (Whether this advantage holds across broader task distributions remains to be established.)
- Introduced a modular tokenizer architecture that enables straightforward adaptation to new observation and action spaces without retraining the full model.
- Provided the first open-source generalist robot policy with a standardized fine-tuning API.

**Quantitative results:**

| Benchmark / Task | Octo (93M) | RT-1-X | RT-2-X | Notes |
|---|---|---|---|---|
| *(Results not independently verified --- arXiv page could not be fetched. The paper reports competitive or superior performance to RT-1-X on fine-tuned WidowX and Franka tasks. Consult RSS 2024 paper for per-task success rates.)* | | | | |

**Limitations/Gaps:**
- Small model size limits zero-shot generalization compared to billion-parameter VLAs.
- No pre-trained VLM backbone means Octo lacks the semantic reasoning and instruction-following capabilities of VLAs like RT-2 or OpenVLA.
- Not demonstrated on dexterous hand systems.
- The frozen language encoder provides only coarse language conditioning compared to co-fine-tuned VLMs.

**Open weights/code:** ✅ Fully open. [GitHub](https://github.com/octo-models/octo), [HuggingFace](https://huggingface.co/rail-berkeley/octo-base).

## Inference / Deployment

- **Inference latency:** With only 93M parameters, Octo is significantly faster than billion-parameter VLAs. The diffusion action head uses a small number of denoising steps. Octo is designed to fine-tune "within a few hours on standard consumer GPUs," implying efficient inference as well. Estimated ~10-30 Hz on a consumer GPU, though specific benchmarks are not prominently reported.
- **Deployment hardware:** Designed for consumer GPU deployment. Can be fine-tuned on standard consumer GPUs (e.g., RTX 3090/4090). The 93M parameter footprint is small enough for edge deployment scenarios, though Jetson Orin benchmarks are not reported.
- **Real-time capable?** Yes, likely. The small model size (93M parameters, ~75x smaller than OpenVLA 7B) and efficient diffusion head should enable real-time control at manipulation-appropriate frequencies (10-30 Hz) on consumer hardware. The modular tokenizer design adds minimal overhead.

## Dataset / Data Collection

- **Dataset used:** Open X-Embodiment (OXE) dataset -- 800K robot episodes from diverse manipulation datasets. Fine-tuning demonstrated on WidowX, Franka, and various platforms.
- **Collection method:** Aggregated cross-embodiment data from OXE (teleoperation, scripted policies, human demonstrations). Fine-tuning requires as few as 50 demonstrations.
- **Data scale:** 800K robot episodes for pretraining (OXE subset). Fine-tuning: as few as 50 demonstrations per task.
- **Teleop equipment:** Varies by OXE constituent dataset.
- **Data format:** RLDS (TensorFlow Datasets) format, following OXE standard.
- **Publicly available?** Yes. OXE dataset is public. Octo weights at https://huggingface.co/rail-berkeley/octo-base.

---
