### 2.6 HumanoidGen

**Full title:** HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning

**Authors:** Zhi Jing, Siyuan Yang, Jicong Ao, Ting Xiao, Yu-Gang Jiang, Chenjia Bai

**Venue/Year:** NeurIPS 2025

**arXiv:** [2507.00833](https://arxiv.org/abs/2507.00833) (note: previously cited as 2505.14680, which resolves to an unrelated paper)

**Hand hardware:** Unitree H1-2 humanoid robot with Inspire dexterous hands (6 DoF per hand, 7 DoF per arm; total action space 26D). The Inspire hands are multi-finger dexterous hands, confirming inclusion in the dexterous manipulation section.

**Tasks:**
- 20 tabletop manipulation tasks
- Bimanual coordination tasks
- Long-horizon multi-step manipulation
- Tasks requiring dexterous hand-object interaction within the humanoid embodiment context

**Key methodology:** HumanoidGen uses a large language model (LLM) as a task planner combined with Monte Carlo Tree Search (MCTS) for policy generation. The LLM decomposes complex manipulation instructions into sub-task sequences, while MCTS explores the space of possible action plans to find high-reward trajectories. A diffusion policy serves as the low-level controller, generating continuous actions for the humanoid's arms and hands. Language is used at the planning level to specify and decompose tasks, with the LLM providing commonsense reasoning about manipulation strategies.

**Architecture/Parameters:**
- High-level planner: LLM (specific model not disclosed in abstract; used for task decomposition and MCTS guidance)
- Search: Monte Carlo Tree Search for plan optimization
- Low-level controller: diffusion policy for continuous action generation
- Target platform: Unitree H1_2 humanoid
- Model and data weights available on HuggingFace

**Main contributions:**
- LLM-guided MCTS framework for generating diverse manipulation policies, combining the commonsense reasoning of LLMs with the systematic exploration of MCTS
- Demonstrated on 20 tabletop tasks including bimanual and long-horizon manipulation on a full humanoid platform
- The framework generates diverse policy solutions for the same task, improving robustness through solution diversity

**Limitations/Gaps:**
- Humanoid-integrated hands only; does not address standalone dexterous hand platforms (Allegro, Shadow, LEAP)
- No force or impedance output; the diffusion policy generates position targets
- The LLM planner operates at the task-decomposition level, not at the level of fine-grained finger control
- MCTS exploration may be computationally expensive for real-time applications
- Evaluation is primarily on tabletop manipulation; does not cover tool use or highly contact-rich tasks

**Results:**

**MCTS effectiveness (data generation success rates):**

| Task | Non-MCTS | MCTS | MCTS iterations (N) |
|---|---|---|---|
| Block Stack Single | 63.3 +/- 6.2% | 98.3 +/- 2.4% | N=2 |
| Blocks Stack Easy | 46.7 +/- 2.4% | 95.0 +/- 4.1% | N=3 |
| Blocks Stack Hard | 18.3 +/- 6.2% | 98.3 +/- 2.4% | N=12 |
| Pyramid Stack | 13.3 +/- 6.2% | 90.0 +/- 4.1% | N=12 |

MCTS improves success rates by 35--77 percentage points over non-MCTS baselines.

**Policy learning results (DP3 vs DP, selected tasks, varying demonstration count):**

| Task | Policy | 20 Demos | 50 Demos | 100 Demos |
|---|---|---|---|---|
| Blocks Stack Easy | DP3 | 0.0% | 0.0% | 22.8 +/- 16.5% |
| Blocks Stack Easy | DP | 0.0% | 0.0% | 0.0% |
| Cup Pour Easy | DP3 | 67.8 +/- 10.8% | 75.6 +/- 9.6% | 72.2 +/- 7.9% |
| Cup Pour Easy | DP | 0.0% | 2.2 +/- 6.3% | 0.0% |
| Open Box Easy | DP3 | 85.6 +/- 8.0% | 95.6 +/- 4.4% | 95.0 +/- 4.1% |
| Open Box Easy | DP | 93.3 +/- 13.3% | 100.0% | 100.0% |
| Open Box Hard | DP3 | 95.6 +/- 5.5% | 96.1 +/- 4.6% | 98.3 +/- 3.3% |
| Open Box Hard | DP | 11.1 +/- 19.1% | 93.3 +/- 9.4% | 100.0% |
| Open Drawer | DP3 | 58.3 +/- 8.3% | 76.0 +/- 13.1% | 84.4 +/- 11.3% |
| Open Drawer | DP | 17.8 +/- 22.0% | 13.3 +/- 18.9% | 48.9 +/- 31.4% |
| Close Box Hard | DP3 | 88.9 +/- 17.6% | 96.3 +/- 6.9% | 96.3 +/- 6.9% |
| Close Laptop Easy | DP3 | 100.0% | 100.0% | 100.0% |

14 tasks evaluated across all conditions in the full benchmark (HGen-Bench). DP3 generally outperforms DP, especially on dexterous tasks. Average success rate across all tasks exceeds 50%.

- Model and data released on HuggingFace
- Code released at [GitHub](https://github.com/TeleHuman/HumanoidGen)
- Project page: [openhumanoidgen.github.io](https://openhumanoidgen.github.io)

## Inference / Deployment

- **Inference latency:** Not reported in the paper (arXiv 2507.00833).
- **Deployment hardware:** Unitree H1_2 humanoid robot platform. Training/inference GPU not specified.
- **Real-time capable?** Not verified. The MCTS-based planning may introduce computational overhead at inference time, but specific latency figures are not available.

## Dataset / Data Collection

- **Dataset used:** Custom simulation-generated dataset. Available on HuggingFace (`TeleEmbodied/humanoidgen_dataset`).
- **Collection method:** Simulation-based data generation using the ManiSkill platform. Data is collected by running task solver scripts with `record_data` enabled, generating demonstration trajectories for 20 tabletop manipulation tasks.
- **Data scale:** Not explicitly reported. The HuggingFace dataset repository exists but specific episode/trajectory counts are not disclosed in public documentation.
- **Teleop equipment:** Not applicable (simulation-generated data). Real-world deployment uses the Unitree H1_2 humanoid robot.
- **Data format:** Collected in pickle format, then converted to zarr format for policy training via `pkl2zarr.py`.
- **Publicly available?** Yes. Dataset on HuggingFace (`TeleEmbodied/humanoidgen_dataset`). Model on HuggingFace (`TeleEmbodied/humanoidgen_model`). Code at [GitHub](https://github.com/TeleHuman/HumanoidGen). Note: scene generation and additional task generation code not yet released.
