# 12.3 AnyTouch

- **Full title:** AnyTouch: Learning Unified Tactile Representations Across Multiple Sensors
- **Authors:** GeWu Lab (Renmin University of China)
- **Venue/Year:** ICLR 2025
- **Sensors supported:** 4+ tactile sensor types (TacQuad dataset)
- **Pretraining method:** Cross-sensor self-supervised learning
- **Dataset:** TacQuad -- 4-sensor paired tactile dataset

## Key methodology/design

AnyTouch extends the cross-sensor paradigm by pretraining on TacQuad, a dataset containing paired tactile readings from four different sensor types on the same objects/contacts. This paired data enables direct cross-sensor contrastive learning: the model learns representations that are invariant to sensor-specific visual artifacts while preserving contact-relevant information. The resulting encoder can process tactile data from any of the four sensor types and produce compatible representations, enabling transfer of tactile skills across sensor platforms.

## Main contributions

- TacQuad dataset: first large-scale paired multi-sensor tactile dataset (4 sensor types, same contacts)
- Cross-sensor SSL that explicitly learns sensor-invariant representations through paired data contrastive learning
- Demonstrated transfer of tactile representations across sensor types without fine-tuning
- Strongest cross-sensor generalization results among tactile foundation models

## Quantitative results (cross-sensor transfer)

| Evaluation | AnyTouch | Sparsh | Single-sensor baseline |
|------------|----------|--------|----------------------|
| Within-sensor performance | Competitive | Competitive | Best (trained on target sensor) |
| Cross-sensor transfer (seen sensors) | Best | Moderate degradation | Not applicable |
| Cross-sensor transfer (unseen sensors) | Degraded but functional | Significant degradation | Not applicable |
| Number of sensors supported | 4+ | 2 (DIGIT, GelSight) | 1 |

*Note: AnyTouch's paired-data contrastive learning produces stronger cross-sensor generalization than Sparsh's unpaired SSL, but both degrade relative to within-sensor training. Performance on sensor types not seen during pretraining remains a limitation.*

## Limitations/Gaps

- TacQuad dataset collection requires physically contacting the same surfaces with multiple sensors, which is labor-intensive and limits dataset scale
- 4 sensor types, while more than Sparsh (2), still covers only a fraction of the tactile sensor ecosystem
- Like Sparsh and UniTouch, does not demonstrate integration into closed-loop manipulation policies
- Representation quality degrades for sensor types not seen during pretraining

## Shared limitation

Like all tactile representation models in this section, AnyTouch does not demonstrate integration into closed-loop manipulation policies. See [Sparsh](sparsh.md#shared-limitation-no-closed-loop-policy-integration) for a detailed discussion of this shared limitation.

## Open-source status

Open-source (code + pretrained weights). GitHub: [GeWu-Lab/AnyTouch](https://github.com/GeWu-Lab/AnyTouch)
