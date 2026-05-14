# 10.11 DexPilot

- **전체 제목:** DexPilot: Vision Based Teleoperation of Dexterous Robotic Hand-Arm System
- **저자:** Ankur Handa, Karl Van Wyk, Wei Yang, Jacky Liang, Yu-Wei Chao, Qian Wan, Stan Birchfield, Nathan Ratliff, Dieter Fox (NVIDIA)
- **학회/연도:** ICRA 2020 (arXiv 1910.03135, 2019년 10월)
- **arXiv:** https://arxiv.org/abs/1910.03135
- **입력 모달리티:** 비전 기반 (맨손 인간 손을 관찰하는 RGB 카메라, 글러브나 마커 없음)
- **대상 hand:** Allegro Hand (16 DoF) + Kuka IIWA arm (7 DoF), 총 23 DoA
- **Force feedback:** 없음
- **비용:** 저렴 (단일 RGB 카메라)

## 핵심 방법론/설계

DexPilot은 단일 RGB 카메라로 운영자의 맨손을 관찰하여 dexterous 로봇 hand-arm 시스템의 원격조작을 가능하게 한다. 시스템은 비전 기반 핸드 포즈 추정기를 사용하여 핸드 키포인트(손가락 끝, 관절, 손목)를 감지한 후, 감지된 인간 핸드 포즈를 로봇 hand의 관절 공간으로 retarget하는 최적화 문제를 풀어낸다. retargeting 공식은 Allegro Hand의 관절 한계와 kinematic 제약 조건을 존중하면서 인간과 로봇 손가락 끝 위치 간의 차이를 최소화한다. 팔 동작은 wrist 포즈를 IK를 통해 Kuka IIWA end-effector에 매핑하여 별도로 제어된다.

핵심 혁신은 마커 없는, 글러브 없는 설계이다: 운영자가 카메라 앞에서 맨손을 움직이기만 하면 된다. 이로써 전문 원격조작 하드웨어(VR 컨트롤러, haptic 글러브, 전자기 트래커)의 필요성이 제거되고 비용과 셋업 시간이 절감된다. 시스템은 hand-arm 시스템의 전체 23 DoA를 지원하여 단순한 pick-and-place를 넘어선 복잡한 조작을 가능하게 한다.

## 주요 기여

- 23 DoA의 완전한 dexterous hand-arm 시스템을 위한 최초의 비전 기반(맨손, 마커/글러브 없음) 원격조작 시스템
- kinematic 실현 가능성 제약 조건을 갖춘 인간 핸드 키포인트를 Allegro Hand 관절 공간에 매핑하는 최적화 기반 retargeting
- 단일 RGB 카메라만으로 복잡한 조작 작업(pick-and-place 이상) 입증
- 비전 기반 핸드 트래킹이 dexterous 원격조작에 충분함을 입증하여 글러브/exoskeleton 시스템 대비 하드웨어 비용 절감

## 한계점

- 운영자에게 force/haptic feedback 없음; 조작이 전적으로 시각 피드백에 의존
- 비전 기반 핸드 트래킹이 가림(손가락이 서로 가리는 경우) 및 조명 조건에 민감
- 단일 카메라 셋업이 제한된 깊이 정보를 제공하여 retargeting 모호성 유발 가능
- 비전 처리 파이프라인의 지연이 고주파 contact-rich 작업을 제한할 수 있음
- Allegro Hand + Kuka IIWA에서만 평가; 크로스 플랫폼 검증 없음
- policy 학습 구성요소 없음; 순수 원격조작 시스템 (수집된 데이터가 downstream IL에 사용 가능하나 논문에서 시연되지 않음)

## 데이터 품질 영향

DexPilot은 force 또는 tactile 정보 없이 위치 전용 시연을 수집한다. 비전 기반 핸드 트래킹이 노이즈와 간헐적 트래킹 실패(특히 가림 중)를 도입하여, 글러브 기반 또는 exoskeleton 기반 시스템 대비 시연 품질을 저하시킨다. 그러나 저비용과 쉬운 셋업으로 더 대규모 데이터셋 수집이 가능하여, 양으로 시연당 품질을 잠재적으로 보상한다. 시스템은 전문 하드웨어 없이도 고차원 dexterous 시연 수집이 가능함을 입증했다.

## 정량적 결과

논문은 다수의 조작 작업에 걸쳐 두 명의 인간 시연자에 대한 속도 및 신뢰성 메트릭을 평가한다. 작업에는 다양한 객체 잡기, in-hand repositioning, 도구 조작이 포함된다. 구체적인 성공률은 작업 범주에 걸쳐 보고되나 시연자 숙련도에 따라 다양하다.

| 메트릭 | 값 |
|--------|-----|
| 총 제어 DoA | 23 (hand 16 + arm 7) |
| 입력 하드웨어 | 단일 RGB 카메라 |
| 핸드 트래킹 | 비전 기반 키포인트 감지 |
| Retargeting | 최적화 기반 |

## 오픈소스 현황

비오픈소스. 비디오가 포함된 프로젝트 페이지: https://sites.google.com/view/dex-pilot
