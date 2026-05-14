# Section 12: Tactile Representation Models

Tactile sensing provides direct measurement of contact geometry, forces, and material properties that vision alone cannot capture. However, raw tactile signals (high-resolution images from GelSight/DIGIT, or force arrays from resistive sensors) are high-dimensional and sensor-specific. Tactile representation models learn compact, transferable encodings of tactile data, analogous to how ImageNet-pretrained vision encoders provide general visual features. This section covers foundation models for tactile representation.

## Entries

| Entry | Sensors | Method | Key Strength |
|-------|---------|--------|--------------|
| [Sparsh](sparsh.md) | DIGIT, GelSight | SSL (MAE, DINO, IJEPA) | Cross-sensor transfer; TacBench benchmark |
| [UniTouch](unitouch.md) | Multiple vision-based | Contrastive (CLIP-style) | Touch-vision-language-sound alignment |
| [AnyTouch](anytouch.md) | 4+ types (TacQuad) | Cross-sensor SSL | Strongest cross-sensor generalization |
| [NeuralFeels](neuralfeels.md) | DIGIT on Allegro Hand | Neural fields (NeRF-style) | Real-hardware tactile-visual fusion for state estimation |

## Shared limitation

All four tactile representation models in this section demonstrate their learned representations on classification, regression, or tracking benchmarks -- none shows end-to-end integration as a tactile encoder within a closed-loop manipulation policy (VLA or RL). This disconnect between representation learning and manipulation policy learning is the most significant gap in this area. See the [Sparsh entry](sparsh.md) for a detailed discussion of this shared limitation.

## Observations

Tactile representation models are following the trajectory of vision foundation models with a 3-5 year lag: SSL pretraining on large unlabeled corpora (Sparsh), multimodal alignment (UniTouch), cross-sensor generalization (AnyTouch), and task-specific neural fields (NeuralFeels). The field has converged on vision-based tactile sensors (DIGIT, GelSight) as the primary input modality, which is both a strength (leveraging existing vision encoder architectures) and a limitation (excluding non-visual tactile modalities like resistive arrays, barometric sensors, or the 18+ modalities of Digit 360). The most significant gap is the disconnect between representation learning and manipulation policy learning. NeuralFeels comes closest by demonstrating on real Allegro + DIGIT hardware, but it provides state estimation rather than action generation. Closing this loop -- using a pretrained tactile encoder (Sparsh, UniTouch, AnyTouch) as the tactile backbone of a dexterous manipulation policy -- is a clear next step that no published system has yet demonstrated.
