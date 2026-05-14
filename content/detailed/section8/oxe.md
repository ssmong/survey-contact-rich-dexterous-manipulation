# 8.4.1 Open X-Embodiment (OXE)

- **Full title:** Open X-Embodiment: Robotic Learning Datasets and RT-X Models
- **Authors:** 294+ authors from 21 institutions (Google DeepMind, UC Berkeley, Stanford, CMU, MIT, and others); notable contributors include Sergey Levine, Pieter Abbeel, Chelsea Finn, Jitendra Malik
- **Venue/Year:** arXiv 2023 (submitted October 2023; last revised May 2025); associated with ICRA 2024
- **Scale:** ~1M robot episodes, 22 robot embodiments, 527 skills, 160K+ tasks
- **Hand/embodiment types:** 22 different robot platforms spanning single-arm, bimanual, and mobile manipulators (primarily parallel-jaw grippers; no dedicated multi-finger dexterous hand data)
- **Data format:** Standardized RLDS (Reinforcement Learning Datasets) format via TensorFlow Datasets
- **Collection method:** Multi-institutional collaborative aggregation of existing and newly collected datasets from 21 research labs worldwide

## Key methodology/design

OXE is the first large-scale cross-embodiment robot manipulation dataset, aggregating data from 21 institutions into a unified format. The core thesis is that pooling diverse robot data -- across different morphologies, sensors, and tasks -- enables positive transfer when training large generalist policies. The dataset is accompanied by the RT-X models (RT-1-X, RT-2-X), which demonstrate that a single policy trained on the full mixture outperforms policies trained on any single institution's data alone. The standardized RLDS format includes observations (images, proprioception), actions (end-effector or joint), language instructions, and episode metadata.

## Main contributions

- Largest cross-embodiment robot manipulation dataset at time of release (~1M episodes across 22 robots)
- Demonstrated positive transfer: RT-2-X trained on the full mixture shows 50%+ improvement over specialist models on average
- Established RLDS as the de facto standard format for cross-embodiment robot data
- Foundational pretraining dataset adopted by OpenVLA, Octo, RDT-1B, HPT, CrossFormer, and many subsequent generalist policies

## Downstream usage in surveyed works

OXE is the primary pretraining dataset for multiple systems covered in this survey:
- **OpenVLA** (§6): pretrained on OXE mixture
- **Octo** (§6): pretrained on OXE; OXE was designed alongside Octo
- **RDT-1B** (§6): uses OXE for large-scale pretraining
- **HPT** (§6): cross-embodiment pretraining on OXE
- **CrossFormer** (§6): designed specifically for OXE-scale cross-embodiment data

## Limitations/Gaps

- No multi-finger dexterous hand data: all embodiments use parallel-jaw grippers or simple end-effectors, making OXE unsuitable for pretraining dexterous manipulation policies without additional data
- No force/torque or tactile data: observations are limited to images and proprioception
- Significant class imbalance across embodiments: some robots contribute orders of magnitude more data than others
- Quality variance: data from different institutions uses different collection protocols, annotation quality, and task definitions
- Limited real-world diversity within individual embodiments compared to datasets like DROID that specifically target scene/environment diversity
- Action space heterogeneity requires careful normalization or embodiment-specific action heads
- No impedance/compliance control data or contact event annotations, limiting use for contact-rich policy learning.

## Availability

Open-source under CC BY 4.0. Available via TensorFlow Datasets and the [Open X-Embodiment project page](https://robotics-transformer-x.github.io/). Individual component datasets have varying licenses.
