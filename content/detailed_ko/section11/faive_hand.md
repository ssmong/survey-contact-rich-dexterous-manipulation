# 11.6 FAIVE Hand

- **전체 제목:** FAIVE Hand: A Low-Cost, 3D-Printed, Tendon-Driven Dexterous Robot Hand
- **저자:** ETH Zurich, Soft Robotics Lab (SRL)
- **학회/연도:** 2024 (오픈소스 하드웨어 공개; policy 학습 관련 논문 포함)
- **DoF:** 11+ 구동 (버전에 따라 다름; P0/P2/P4 리비전으로 DoF 증가)
- **비용:** ~$500-800 (부품 비용; 본 섹션의 모든 다른 hand보다 상당히 낮음)
- **Tactile 센싱:** 내장 없음 (손가락 끝 설계가 애프터마켓 센서 수용 가능)
- **구동 방식:** 시판 서보 모터를 사용한 건 구동; 3D 프린트 손가락 링크를 통한 건 라우팅
- **제작:** 완전 3D 프린트 구조 부품 (FDM/SLA); CNC 또는 커스텀 가공 불필요

## 정량 사양

| 사양 | 값 |
|------|-----|
| 손가락 | 4개 손가락 + 엄지 (인체형 배치) |
| 구동 DoF | 11+ (버전 의존; P4가 더 높은 DoF) |
| 수동 DoF | 건 결합을 통한 추가 under-actuated 관절 |
| 무게 | 미보고 (3D 프린트 구조로 경량 추정) |
| 액추에이터 제어 대역폭 | ~50 Hz (서보 모터에 의해 제한) |
| 최대 손가락 끝 힘 | 건 장력과 서보 토크에 의해 제한; direct-drive 설계보다 낮음 |

## 핵심 방법론/설계

FAIVE Hand는 초저가 접근성의 원칙을 중심으로 설계되었다. 모든 구조 부품이 소비자급 프린터에서 3D 프린트 가능하며, 구동은 건 라우팅을 갖춘 시판 서보 모터를 사용한다. under-actuated 건 구동 설계는 관절 DoF보다 적은 모터가 필요하며, 수동 관절 결합으로 적응적 grasping을 제공한다. 점진적으로 개선된 설계의 다수 하드웨어 리비전(P0, P2, P4)이 출시되었다. hand는 표준 로봇 팔에 장착되며 dexterous 조작 작업을 위한 RL 기반 sim-to-real transfer가 시연되었다.

## 주요 기여

- 초저가 dexterous hand (~$500-800), 본 서베이의 다른 모든 hand보다 약 2-6배 저렴
- 완전 3D 프린트 가능: CNC 가공, 레이저 컷팅, 커스텀 부품 불필요; dexterous 조작 하드웨어에 대한 접근 민주화
- 관절보다 적은 모터로 적응적 grasping을 제공하는 건 구동 under-actuation
- 커뮤니티 기여를 포함한 다수의 오픈소스 하드웨어 리비전
- 조작 policy에 대한 sim-to-real transfer 입증

## 한계점

- LEAP(16), ORCA(17), ISyHand(18)보다 낮은 DoF(11+)로 미세 조작 dexterity 제한
- 건 구동 방식이 케이블 라우팅 복잡성, 건 마모, 잠재적 이완 문제 도입
- 통합 tactile 센싱 없음; 애프터마켓 센서 없이 손가락 끝 힘 측정 불가
- 3D 프린트 부품이 사출 성형이나 CNC 가공 대안보다 기계적 내구성이 낮음; 장기 사용 후 재프린트 필요 가능
- 서보 모터 대역폭(~50 Hz) 및 토크가 Dynamixel 또는 커스텀 액추에이터에 비해 제한적
- LEAP Hand 대비 더 작은 연구 커뮤니티와 적은 출판된 sim-to-real 결과
- 건 역학과 3D 프린트 관절 compliance의 정확한 모델링 어려움으로 sim-to-real gap이 더 클 수 있음

## 오픈소스 현황

완전 오픈소스 (CAD, 펌웨어, 조립 설명서, BOM). GitHub: [srl-ethz/faive-hand](https://github.com/srl-ethz/faive-hand) (참고: 버전에 따라 저장소 명명 규칙이 다를 수 있음). 다수의 하드웨어 리비전 이용 가능.
