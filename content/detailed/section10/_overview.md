# Section 10: Teleoperation Systems

Teleoperation is the primary means of collecting dexterous manipulation demonstrations for imitation learning. The systems below span the cost-fidelity spectrum, from sub-$150 handheld devices to $3,500+ VR headset setups, each making different tradeoffs between motion capture quality, force feedback, and deployment cost.

## Entries

| Entry | Input Modality | Force Feedback | Cost | Target Hand |
|-------|---------------|----------------|------|-------------|
| [DexCap](dexcap.md) | EM finger sensors + SLAM | None | ~$2,000 | LEAP Hand |
| [BunnyVisionPro](bunnyvisionpro.md) | Apple Vision Pro hand tracking | Low-cost haptic (optional) | ~$3,500+ | Bimanual dexterous |
| [AnyTeleop](anyteleop.md) | Single RGB camera | None | Very low (webcam) | Allegro, Shadow, others |
| [DOGlove](doglove.md) | Custom haptic glove | 5-DoF haptic | <$600 | Any dexterous hand |
| [DEXOP](dexop.md) | Passive exoskeleton | Proprioceptive | Research prototype | Any dexterous hand |
| [DEX-Mouse](dex_mouse.md) | Handheld device | Kinesthetic | <$150 | Any dexterous hand |
| [Open TeleDex](open_teledex.md) | Smartphone camera | None | Very low (smartphone) | Any arm + hand |
| [OmniH2O](omnih2o.md) | VR / voice / RGB camera | None | Varies | Humanoid whole-body |
| [Open-TeleVision](open_television.md) | Stereo VR headset | None (visual substitute) | Consumer VR headset | Bimanual dexterous |
| [DexPilot](dexpilot.md) | Single RGB camera (bare hand) | None | Low (single RGB camera) | Allegro Hand + Kuka IIWA |

## Observations

The teleoperation landscape shows a clear trend toward cost reduction and accessibility. In 2023, AnyTeleop demonstrated camera-only input; by 2026, DEX-Mouse achieved dexterous teleoperation for under $150. The critical divide is force feedback: only DOGlove (<$600) and DEXOP provide any form of haptic rendering, while the majority of systems are vision-only or position-only. This is significant because contact-rich dexterous manipulation -- the focus of this survey -- fundamentally requires force regulation, yet the data collection systems used to train these policies almost universally lack force feedback. The result is a systematic bias in imitation learning datasets: demonstrations are collected without force awareness, and policies trained on this data inherit that limitation. DOGlove's 5-DoF haptic feedback at <$600 is the most promising step toward force-aware data collection, but its per-finger granularity is coarse compared to the spatially distributed contacts that multi-finger hands create. A second trend is the convergence on universal retargeting -- systems increasingly support arbitrary robot hands rather than being designed for a single platform, mirroring the cross-embodiment direction in the VLA literature (UniDex-VLA, CrossDex).
