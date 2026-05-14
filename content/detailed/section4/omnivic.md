### 4.2 OmniVIC

**Full title:** OmniVIC: Omnidirectional Variable Impedance Control via Vision-Language Model with Self-Improving RAG

**Authors:** Luigi Penco, Niko Suenderhauf, Fares Abu-Dakka, et al. (IIT Genoa / Georgia Tech)

**Venue/Year:** arXiv preprint, 2025

**How K/D are determined:** VLM (GPT-4o-mini) + self-improving RAG (Retrieval-Augmented Generation). The system maintains a database of prior task executions with associated impedance parameters and outcomes. When a new task is presented, the VLM retrieves relevant prior experiences via RAG, reasons about appropriate K/D values, and proposes impedance parameters. After execution, success/failure feedback is stored back into the database, enabling self-improvement over time.

**What is output:** Full 6D Cartesian stiffness matrix K and damping matrix D for omnidirectional impedance control. The parameters are direction-aware, allowing different compliance in different Cartesian axes.

**Robot platform:** Franka Emika Panda + 6-axis F/T sensor + parallel-jaw gripper. No dexterous hand.

**Tasks:** Contact-rich manipulation including: surface wiping with force regulation, peg-in-hole insertion, object polishing, compliant handover. Tasks require direction-dependent compliance (e.g., stiff along insertion axis, compliant laterally).

**Key methodology:** OmniVIC extends basic VLM-based impedance generation with a self-improving retrieval-augmented generation loop. The VLM receives the task description, current visual observation, and retrieved examples of similar past tasks with their impedance parameters and outcomes. It then generates direction-specific K/D values. The F/T sensor provides force feedback that is used to evaluate execution quality and update the RAG database. Over repeated trials, the system improves its impedance parameter selection for recurring task types without any gradient-based training.

**Architecture/Parameters:** GPT-4o-mini as the VLM backbone, FAISS or similar vector database for RAG retrieval, 6-axis F/T sensor for execution monitoring. The RAG database stores task descriptions, visual features, impedance parameters used, and success metrics. The impedance controller runs as a Cartesian impedance controller on the Franka.

**Main contributions:**
- Introduces self-improving RAG for impedance parameter selection, enabling the system to learn from execution outcomes without gradient updates
- Demonstrates omnidirectional (axis-specific) impedance generation from VLM reasoning, going beyond scalar stiffness
- Shows that RAG retrieval improves K/D selection accuracy over pure zero-shot VLM prompting across repeated trials

**Limitations/Gaps:**
- No dexterous hand -- gripper-only on Franka Panda
- Improvement loop requires multiple real-world trials; sample efficiency is limited by the VLM's reasoning rather than learned from data
- Relies on commercial VLM API (GPT-4o-mini)
- RAG database must be populated with initial trials; cold-start performance is equivalent to zero-shot VLM
- Does not address continuous impedance adaptation during contact (parameters are set per task phase)
- VLM inference latency (~100ms-1s) limits impedance updates to ~1-10 Hz, three orders of magnitude below the 100-1000 Hz required by real-time impedance controllers.

**Results:** Self-improving RAG outperformed pure zero-shot VLM impedance generation across all evaluated tasks. After several iterations, the system converged to impedance parameters comparable to expert-tuned values. F/T sensor feedback confirmed reduced peak forces and improved task success rates relative to fixed-impedance baselines.

## Inference / Deployment

- **Inference latency:** Not explicitly benchmarked. VLM inference via GPT-4o-mini API adds ~100ms-1s per impedance parameter query, plus RAG retrieval overhead (FAISS nearest-neighbor search, typically <10ms). Impedance parameters are generated per task phase, not per control step.
- **Deployment hardware:** Franka Emika Panda with 6-axis F/T sensor. VLM inference runs via cloud API (GPT-4o-mini); FAISS retrieval runs on a local machine (hardware not specified).
- **Real-time capable?** No, for impedance adaptation. The low-level impedance controller runs at real-time rates on the Franka, but VLM-based impedance updates are limited to ~1-10 Hz due to API call latency. Continuous impedance modulation during fast contact transitions is not supported.

## Dataset / Data Collection

- **Dataset used:** LIBERO benchmark (20 tasks: 10 from LIBERO-Object, 10 from LIBERO-Goal) for simulation evaluation. Custom RAG knowledge-base dataset built from execution experience.
- **Collection method:** Automated collection via robot policy execution with VLM-based assistance. Episodes labeled success/failure based on maximum contact force (Fmax) and time budget (Tmax) thresholds. RAG database stores task instruction (raw text + BGE-M3 embeddings), end-effector twist, gravity-compensated wrench, phase label, and controller parameters (K, D). Real-world validation on Franka Emika Panda with ATI Mini45 F/T sensor.
- **Data scale:** RAG database: 200 records (20 records per task-phase pair across 10 tasks; max capacity 20,000). Evaluation: 50 episodes per task per method across 10 query-set tasks. Three real-world contact-rich tasks.
- **Teleop equipment:** Not applicable (automated policy execution, not teleoperated).
- **Data format:** RAG records containing text embeddings, wrench data, phase labels {Free_motion, Approaching, Contact, Retreat}, and impedance parameters.
- **Publicly available?** Yes -- code, video, and RAG dataset at https://sites.google.com/view/omni-vic
