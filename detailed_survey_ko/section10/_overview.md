# Section 10: 원격조작 시스템

원격조작은 imitation learning을 위한 dexterous 조작 시연을 수집하는 주요 수단이다. 아래 시스템들은 $150 이하의 휴대용 디바이스부터 $3,500 이상의 VR 헤드셋 셋업까지 비용-충실도 스펙트럼에 걸쳐 있으며, 모션 캡처 품질, force feedback, 배포 비용 간의 서로 다른 trade-off를 가진다.

## 항목

| 항목 | 입력 모달리티 | Force Feedback | 비용 | 대상 Hand |
|------|-------------|----------------|------|-----------|
| [DexCap](dexcap.md) | EM 손가락 센서 + SLAM | 없음 | ~$2,000 | LEAP Hand |
| [BunnyVisionPro](bunnyvisionpro.md) | Apple Vision Pro 핸드 트래킹 | 저비용 haptic (선택 사항) | ~$3,500+ | 양팔 dexterous |
| [AnyTeleop](anyteleop.md) | 단일 RGB 카메라 | 없음 | 매우 저렴 (웹캠) | Allegro, Shadow 등 |
| [DOGlove](doglove.md) | 커스텀 haptic 글러브 | 5-DoF haptic | <$600 | 임의 dexterous hand |
| [DEXOP](dexop.md) | 수동식 exoskeleton | 고유수용감각 | 연구용 프로토타입 | 임의 dexterous hand |
| [DEX-Mouse](dex_mouse.md) | 핸드헬드 디바이스 | 역감각 | <$150 | 임의 dexterous hand |
| [Open TeleDex](open_teledex.md) | 스마트폰 카메라 | 없음 | 매우 저렴 (스마트폰) | 임의 팔 + hand |
| [OmniH2O](omnih2o.md) | VR / 음성 / RGB 카메라 | 없음 | 다양 | Humanoid 전신 |
| [Open-TeleVision](open_television.md) | 스테레오 VR 헤드셋 | 없음 (시각적 대체) | 소비자용 VR 헤드셋 | 양팔 dexterous |
| [DexPilot](dexpilot.md) | 단일 RGB 카메라 (맨손) | 없음 | 저렴 (단일 RGB 카메라) | Allegro Hand + Kuka IIWA |

## 관찰 사항

원격조작 환경은 비용 절감과 접근성 향상을 향한 뚜렷한 추세를 보인다. 2023년에 AnyTeleop이 카메라 전용 입력을 시연했고, 2026년에는 DEX-Mouse가 $150 이하로 dexterous 원격조작을 달성했다. 핵심 분기점은 force feedback이다: DOGlove (<$600)와 DEXOP만이 어떤 형태의 haptic 렌더링을 제공하며, 대다수 시스템은 비전 전용 또는 위치 전용이다. 이는 contact-rich dexterous 조작 -- 본 서베이의 초점 -- 이 본질적으로 힘 조절을 요구하지만, 이러한 policy를 학습시키는 데 사용되는 데이터 수집 시스템이 거의 보편적으로 force feedback이 부족하기 때문에 중요하다. 그 결과 imitation learning 데이터셋에 체계적 편향이 발생한다: 시연이 힘 인식 없이 수집되고, 이 데이터로 학습된 policy가 해당 한계를 물려받는다. DOGlove의 $600 이하 5-DoF haptic feedback은 힘 인식 데이터 수집을 향한 가장 유망한 진전이지만, multi-finger hand가 생성하는 공간적으로 분산된 접촉에 비해 손가락별 세분성이 조잡하다. 두 번째 추세는 범용 retargeting으로의 수렴이다 -- 시스템이 점점 단일 플랫폼이 아닌 임의의 로봇 hand를 지원하며, VLA 문헌에서의 cross-embodiment 방향 (UniDex-VLA, CrossDex)을 반영한다.
