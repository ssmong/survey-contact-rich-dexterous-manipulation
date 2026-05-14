# 12.2 UniTouch

- **Full title:** UniTouch: Universal Touch Representation for Robot Manipulation
- **Authors:** Che Fang and collaborators (UCSD)
- **Venue/Year:** CVPR 2024
- **Sensors supported:** Multiple vision-based tactile sensors
- **Alignment:** Touch-vision-language-sound multimodal alignment
- **Pretraining method:** Contrastive learning aligning tactile representations with vision, language, and audio modalities

## Key methodology/design

UniTouch learns a unified tactile representation by aligning touch signals with three other modalities: vision, language, and sound. Using contrastive learning (CLIP-style), UniTouch maps tactile images into a shared embedding space with visual images, text descriptions, and audio recordings of contact events. This multimodal alignment enables zero-shot transfer: a tactile representation can be queried with language ("rough surface") or matched to visual appearance without tactile-specific labels. The approach draws on the insight that touch, vision, language, and sound provide complementary descriptions of physical contact.

## Main contributions

- First touch-vision-language-sound alignment model, enabling cross-modal queries (e.g., "find the texture that feels like sandpaper" from vision or language)
- Zero-shot tactile classification through language-tactile alignment without task-specific training
- Unified representation space enabling tactile data to benefit from the rich semantics of language and vision encoders
- Demonstrated on multiple downstream tasks including material classification and contact property estimation

## Quantitative results

| Task | Metric | UniTouch | Vision-only baseline | Touch-only baseline |
|------|--------|----------|---------------------|---------------------|
| Material classification (zero-shot) | Accuracy (%) | Enabled via language alignment | Not applicable | Not applicable (requires labels) |
| Cross-modal retrieval (touch-to-vision) | Recall@K | Demonstrated | N/A | N/A |
| Contact property estimation | Regression error | Competitive with supervised | Vision-only worse for contact properties | Better for contact-specific tasks |

*Note: UniTouch's primary advantage is enabling zero-shot and cross-modal capabilities that single-modality models cannot perform. Direct accuracy comparisons with supervised baselines are task-dependent.*

## Limitations/Gaps

- Multimodal alignment quality depends heavily on the availability and quality of paired touch-vision-language-sound data, which is scarce
- Sound modality is useful for impact/contact events but less informative for quasi-static manipulation (grasping, sliding)
- Representation is optimized for classification/retrieval tasks; utility for closed-loop manipulation policy learning is not demonstrated
- Limited to vision-based tactile sensors; non-visual tactile modalities are not supported

## Shared limitation

Like all tactile representation models in this section, UniTouch does not demonstrate integration into closed-loop manipulation policies. See [Sparsh](sparsh.md#shared-limitation-no-closed-loop-policy-integration) for a detailed discussion of this shared limitation.

## Open-source status

Open-source (code + pretrained weights). GitHub: [cfeng16/UniTouch](https://github.com/cfeng16/UniTouch)
