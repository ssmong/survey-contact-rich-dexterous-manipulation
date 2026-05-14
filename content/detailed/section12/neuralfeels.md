# 12.4 NeuralFeels

- **Full title:** NeuralFeels: Neural Field Methods for Tactile-Visual Object State Tracking
- **Authors:** Suddhu Sudharshan, Haozhi Qi, Pieter Abbeel, Jitendra Malik, Roberto Calandra, Michael Kaess, and collaborators (Meta FAIR, CMU, Berkeley)
- **Venue/Year:** Science Robotics, 2024
- **Hardware:** Allegro Hand (16 DoF) + DIGIT tactile sensors (4 fingertips)
- **Method:** Neural radiance fields (NeRF-style) fusing tactile and visual observations
- **Task:** In-hand object pose and shape tracking during manipulation

## Key methodology/design

NeuralFeels applies neural field methods (NeRF-inspired) to the problem of tracking object state during dexterous in-hand manipulation. The system fuses visual observations from external cameras with tactile images from DIGIT sensors mounted on an Allegro Hand's fingertips. A neural field represents the object's shape and appearance, and is continuously updated as the hand manipulates the object. Tactile observations provide local contact geometry that resolves visual ambiguities (e.g., when fingers occlude the object), while visual observations provide global shape context. This fusion enables accurate 6-DoF pose tracking even during complex in-hand manipulation where the object is heavily occluded.

## Main contributions

- First neural field method for real-time tactile-visual object tracking during dexterous in-hand manipulation
- Demonstrated on real Allegro Hand + DIGIT hardware performing in-hand manipulation of diverse objects
- Principled fusion of tactile (local contact geometry) and visual (global shape) observations through a shared neural field representation
- Published in Science Robotics, representing one of the highest-impact venues for this line of work

## Quantitative results (pose tracking)

| Object category | Pose error (translation, mm) | Pose error (rotation, deg) | Vision-only baseline | Tactile-only baseline |
|----------------|------------------------------|---------------------------|---------------------|-----------------------|
| Simple geometries | Low | Low | Higher (occlusion errors) | Higher (no global context) |
| Complex/textured objects | Low | Low | Moderate | Higher |
| Heavily occluded scenarios | Low (tactile resolves occlusion) | Low | Significantly worse | Comparable |

*Note: Exact numerical values are reported in the Science Robotics publication. The key finding is that tactile-visual fusion consistently outperforms either modality alone, with the largest gains in heavily occluded scenarios where vision alone fails. The neural field representation enables continuous tracking through contact state changes.*

## Limitations/Gaps

- Requires known object 3D models for initialization; not applicable to novel objects without prior shape information
- Neural field optimization is computationally expensive; real-time performance requires significant GPU resources
- Tracking only (state estimation); does not close the loop to generate manipulation actions
- Limited to DIGIT sensors on Allegro Hand; generalization to other sensor-hand combinations is not demonstrated
- Per-object neural field requires re-training for each new object

## Shared limitation

Like all tactile representation models in this section, NeuralFeels does not integrate into a closed-loop manipulation policy that generates actions. It provides state estimation (pose tracking) rather than action generation. See [Sparsh](sparsh.md#shared-limitation-no-closed-loop-policy-integration) for a detailed discussion of this shared limitation. NeuralFeels comes closest to closing this loop among the four models by operating on real dexterous hardware during active manipulation, but the tracking output would need to be consumed by a separate policy to complete the perception-action cycle.

## Open-source status

Open-source. GitHub: [facebookresearch/neuralfeels](https://github.com/facebookresearch/neuralfeels)
