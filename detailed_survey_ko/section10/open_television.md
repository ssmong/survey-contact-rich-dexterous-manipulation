# 10.9 Open-TeleVision

- **전체 제목:** Open-TeleVision: Teleoperation with Immersive Active Visual Feedback
- **저자:** Xuxin Cheng, Jialong Li, Shiqi Yang, Ge Yang, Xiaolong Wang (UCSD)
- **학회/연도:** CoRL 2024 (arXiv 2407.10107, 2024년 7월)
- **입력 모달리티:** 스테레오 VR 헤드셋 (운영자가 로봇의 눈을 통해 봄)
- **대상 hand:** 양팔 dexterous 셋업
- **Force feedback:** 없음 (시각적 피드백으로 대체)
- **비용:** VR 헤드셋 비용 (소비자급)

## 핵심 방법론/설계

Open-TeleVision은 로봇의 머리 장착 카메라에서 운영자의 VR 헤드셋으로 스테레오 비디오를 스트리밍하여 몰입형 시각 피드백을 제공하며, 1인칭 시점을 생성한다. 운영자가 입체 3D로 로봇이 보는 것을 보게 되어, haptic feedback의 부재를 부분적으로 보상하는 깊이 인식을 제공한다. VR 헤드셋의 핸드 트래킹이 실시간 retargeting을 통해 로봇의 양팔 dexterous hand를 제어한다.

## 주요 기여

- 로봇 시점에서의 몰입형 입체 시각 피드백으로 운영자의 공간 인식 및 조작 정확도 향상
- 자연스러운 시점 제어를 위한 능동 시각 피드백 (운영자의 머리 동작이 로봇 카메라 방향 제어)
- 고정 시점 원격조작 대비 향상된 작업 완수율 입증

## 한계점

- force 또는 haptic feedback 없음; contact-rich 작업에서 시각적 단서에만 의존
- 로봇의 스테레오 카메라 셋업이 하드웨어 복잡성과 비용 추가
- VR 헤드셋 지연 및 디스플레이 품질이 장시간 세션에서 운영자 편의에 영향
- 핸드 트래킹 정확도가 특정 VR 헤드셋의 능력에 의존

## 데이터 품질 영향

몰입형 스테레오 시각 피드백이 운영자의 공간 인식을 향상시키며, 이는 고정 시점 시스템 대비 더 나은 손가락 배치 정확도로 이어진다. 운영자가 깊이와 객체 근접성을 더 자연스럽게 판단할 수 있어 시연에서 위치 오차가 감소한다. 그러나 시스템은 force feedback을 제공하지 않아 시연은 force-blind로 남는다. Open-TeleVision 데이터로 학습된 policy는 더 공간적으로 정확한 시연(더 나은 finger-object alignment)에서 이점을 얻지만, 여전히 힘 조절을 학습할 수 없다. 시각 피드백이 일부 시나리오에서 haptic 단서를 대체하지만(운영자가 객체 변형이나 미끄러짐을 시각적으로 감지), 접촉력이 시각적으로 관찰 불가능한 작업(예: 나사 조이기, 특정 활성화 힘까지 버튼 누르기)에서는 신뢰할 수 없다.

## 오픈소스 현황

오픈소스. GitHub: [OpenTeleVision/TeleVision](https://github.com/OpenTeleVision/TeleVision)
