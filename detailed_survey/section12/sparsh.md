# 12.1 Sparsh

- **Full title:** Sparsh: Self-Supervised Touch Representations for Vision-Based and Multi-Modal Tactile Sensing
- **Authors:** Carolina Higuera, Akash Sharma, Chaithanya Krishna Bodduluri, Taosha Fan, Patrick Chaney, Mrinal Kalakrishnan, Michael Kaess, Byron Boots, Mike Lambeta, Tingfan Wu, Mustafa Mukadam (Meta FAIR, CMU)
- **Venue/Year:** CoRL 2024
- **Sensors supported:** DIGIT, GelSight (cross-sensor)
- **Training data:** 460K+ tactile images across multiple sensor types
- **Pretraining method:** Self-supervised learning (SSL) -- MAE (Masked Autoencoder), DINO, IJEPA variants
- **Benchmark:** TacBench -- 5-task tactile benchmark (force estimation, slip detection, texture classification, pose estimation, grasp stability)

## Key methodology/design

Sparsh trains tactile encoders using self-supervised learning on a large corpus of tactile images from multiple sensor types (DIGIT, GelSight). By using SSL pretraining (MAE, DINO, IJEPA), Sparsh learns tactile representations without requiring task-specific labels, analogous to how vision foundation models learn from unlabeled image data. The key innovation is cross-sensor generalization: representations learned on DIGIT images transfer to GelSight and vice versa, despite the significant visual differences between sensor outputs. Sparsh also introduces TacBench, a standardized 5-task benchmark for evaluating tactile representations.

## Main contributions

- First large-scale SSL tactile encoder demonstrating cross-sensor transfer (DIGIT to GelSight and reverse)
- TacBench: standardized 5-task benchmark (force estimation, slip detection, texture classification, pose estimation, grasp stability) for tactile representation evaluation
- Systematic comparison of SSL methods (MAE, DINO, IJEPA) for tactile data, finding that MAE and DINO outperform IJEPA
- 460K+ image pretraining corpus establishing a scale precedent for tactile SSL

## Quantitative results (TacBench)

| Task | Metric | MAE | DINO | IJEPA | Supervised baseline |
|------|--------|-----|------|-------|---------------------|
| Force estimation | RMSE (N) | Best among SSL | Comparable to MAE | Worse | Comparable to SSL |
| Slip detection | Accuracy (%) | Best among SSL | Comparable to MAE | Worse | Comparable to SSL |
| Texture classification | Accuracy (%) | Competitive | Competitive | Lower | Slightly better |
| Pose estimation | Error (mm/deg) | Best among SSL | Comparable | Worse | Comparable |
| Grasp stability | Accuracy (%) | Competitive | Competitive | Lower | Comparable |

*Note: MAE and DINO consistently outperform IJEPA across TacBench tasks. SSL methods achieve performance comparable to supervised baselines, demonstrating that task-specific labels are not necessary for learning useful tactile representations.*

## Limitations/Gaps

- Limited to vision-based tactile sensors (camera-based like DIGIT/GelSight); does not handle resistive, capacitive, or barometric tactile arrays
- Cross-sensor transfer, while demonstrated, still shows performance degradation compared to within-sensor training
- TacBench tasks are relatively simple (classification, regression); does not evaluate representations on full manipulation policies
- Pretraining data is predominantly from flat-surface probing; diversity of contact geometries is limited

## Shared limitation: No closed-loop policy integration

**This limitation -- no integration into closed-loop manipulation policies -- is shared by all tactile representation models in this section (Sparsh, [UniTouch](unitouch.md), [AnyTouch](anytouch.md), [NeuralFeels](neuralfeels.md)).** All four models evaluate their learned representations on standalone perception tasks (classification, regression, tracking) rather than demonstrating end-to-end use as a tactile encoder within a manipulation policy (VLA or RL). This disconnect means the representations are validated for perceptual quality but not for actionable utility -- a representation that accurately estimates contact force may not produce features useful for a policy deciding how to adjust grasp force. Closing this loop by using a pretrained tactile encoder as the tactile backbone of a dexterous manipulation policy is the critical next step for this line of work.

## Open-source status

Fully open-source (code + pretrained weights). GitHub: [facebookresearch/sparsh](https://github.com/facebookresearch/sparsh)
