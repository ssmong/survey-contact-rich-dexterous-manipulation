### 2.4 Dexora

**Full title:** Dexora: Open-Source VLA for High-DoF Bimanual Dexterity

**Authors:** Dexora Team (Tsinghua University; contact: pjr24@mails.tsinghua.edu.cn)

**Venue/Year:** ICRA 2026

**GitHub:** [ZZongzheng0918/Dexora](https://github.com/ZZongzheng0918/Dexora)

**Hand hardware:** Bimanual system with dual dexterous hands, 36 DoF total. Teleoperation uses exoskeleton for arm control and Apple Vision Pro for dexterous hand control.

**Tasks (by category with dataset proportions):**
- Pick-and-place (55% of dataset)
- Dexterous manipulation (20%)
- Assembly (15%)
- Articulated object manipulation (10%)

**Key methodology:** Dexora is an open-source VLA framework that combines large-scale teleoperated real-world data with simulated training data for high-DoF bimanual dexterous manipulation. The hybrid data collection approach uses exoskeleton teleoperation for arm control and Vision Pro hand tracking for dexterous finger control. Multi-view synchronized recording across four camera perspectives captures demonstrations alongside robot proprioceptive feedback. The system follows the LIBERO-2.1 standard for data format compliance.

**Architecture/Parameters:**
- VLA architecture details not fully disclosed in the repository as of the survey date
- Training data: 12.2K real-world teleoperated episodes + 100K simulated episodes
- Real-world data: approximately 40.5 hours
- Object inventory: curated 347-object set with procurement links for reproducibility
- Multi-view input: four synchronized camera perspectives

**Main contributions:**
- Large-scale open-source bimanual dexterous dataset: 12.2K real-world episodes (40.5 hours) plus 100K simulated episodes, with a curated 347-object inventory including procurement links
- Hybrid teleoperation pipeline combining exoskeleton (arms) and Vision Pro (hands) for high-quality bimanual dexterous demonstrations
- LIBERO-2.1 standard compliance and full data release on HuggingFace, lowering the barrier for reproducible dexterous VLA research

**Limitations/Gaps:**
- arXiv link is placeholder format ("2026.xxxxx") as of the survey date, suggesting the full paper may not yet be publicly available
- VLA architecture details are sparse in the current repository
- No force or tactile sensing in the data collection pipeline; demonstrations capture joint positions and visual data only
- 36-DoF bimanual system is specific; cross-embodiment transfer to other hand platforms is not addressed

**Results:**

> **[EDITORIAL NOTE -- no task success rates reported]:** This entry contains only dataset statistics (episode counts, hours, object counts) but no task success rates or manipulation performance metrics. This is a critical gap: without success rates per task category (pick-and-place, dexterous manipulation, assembly, articulated object manipulation), it is impossible to assess the VLA's actual manipulation capability. The full paper or repository should be consulted for quantitative task performance. Until then, this entry documents a dataset and framework contribution, not a demonstrated manipulation capability.

| Metric | Value | Notes |
|---|---|---|
| Real-world episodes | 12.2K | Teleoperated |
| Simulated episodes | 100K | Generated |
| Real-world data duration | ~40.5 hours | |
| Object inventory | 347 objects | With procurement links |
| Task success rates | **Not reported** | Critical gap |

- Data and model weights released on HuggingFace
- Code released at [GitHub](https://github.com/ZZongzheng0918/Dexora)

## Inference / Deployment

- **Inference latency:** Not reported. The repository and available documentation do not disclose inference latency or control frequency.
- **Deployment hardware:** Bimanual system with dual dexterous hands (36 DoF total). Data collection uses exoskeleton (arms) + Apple Vision Pro (hands). Inference hardware not specified.
- **Real-time capable?** Not verified. No inference latency or deployment hardware information available in public materials.

## Dataset / Data Collection

- **Dataset used:** Dexora dataset (custom, released with this work). Two components: real-world teleoperated episodes and simulated episodes.
- **Collection method:** Hybrid teleoperation system coupling an exoskeleton (for arm control, 7 DoF per arm) with Apple Vision Pro (for dexterous hand control). Multi-view synchronized recording across four camera perspectives with robot proprioceptive feedback.
- **Data scale:** 12.2K real-world teleoperated episodes (2.92M frames, ~40.5 hours) + 100K simulated episodes (coming soon). 347 objects across 17 semantic categories with procurement links (Taobao/Amazon) for reproducibility.
- **Teleop equipment:** Exoskeleton for arm control + Apple Vision Pro for dexterous hand tracking (36 DoF bimanual system total).
- **Data format:** LIBERO-2.1 standard. Episodes contain multi-view RGB observations, robot state (joint positions/velocities), action commands, and 5 natural language task descriptions per trajectory. Available in both episode-centric and task-level organizational views.
- **Publicly available?** Yes. Real-world dataset (12.2K episodes) released on HuggingFace. Model weights also on HuggingFace. Code at [GitHub](https://github.com/ZZongzheng0918/Dexora). Simulation dataset release forthcoming.
