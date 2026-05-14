# 9.7 TeleOpBench

- **전체 제목:** TeleOpBench: A Simulator-Centric Benchmark for Dual-Arm Dexterous Teleoperation
- **저자:** Hangyu Li, Qin Zhao, Haoran Xu 외
- **학회/연도:** 2025 (arXiv 2505.12748)
- **시뮬레이션 플랫폼:** Isaac Sim
- **Dexterous 지원:** dexterous hand를 갖춘 3개 humanoid embodiment
- **원격조작 인터페이스:** 카메라 기반 (SMPLerX + MediaPipe) 및 VisionPro 기반 (Apple Vision Pro)
- **작업:** 30개 양팔 dexterous 조작 작업
- **평가:** 4개 원격조작 모달리티 벤치마킹

## 핵심 방법론/설계

TeleOpBench는 양팔 dexterous 조작을 위한 원격조작 시스템을 평가하기 위한 표준화된 벤치마크를 제공한다. 두 가지 모션 캡처 파이프라인을 구현한다: 웹캠 기반 인간 모션 캡처를 위해 SMPLerX와 MediaPipe를 사용하는 카메라 기반 파이프라인과, Apple Vision Pro를 사용하는 VR 기반 파이프라인. 벤치마크에는 실시간 inverse kinematics 처리, MeshCat 기반 3D 시각화, 모션 데이터 전송이 포함된다. 평가 환경과 메트릭을 표준화함으로써 서로 다른 원격조작 접근법의 직접 비교를 가능하게 한다.

## 주요 기여

- 30개 표준화된 작업을 갖춘 최초의 체계적인 양팔 dexterous 원격조작 벤치마크
- 직접 비교가 가능한 다중 원격조작 모달리티 (카메라 기반 및 VR 기반) 지원
- 인간 손 동작을 다양한 로봇 embodiment에 매핑하기 위한 실시간 inverse kinematics 파이프라인
- 원격조작 품질 평가를 위한 표준화된 메트릭

## 한계점

- 벤치마크가 시뮬레이션 전용; 평가 파이프라인에 실제 로봇 실행 미포함
- 두 가지 원격조작 입력 모달리티로 제한; 글러브 기반 및 exoskeleton 기반 인터페이스 미포함
- contact-rich 조작과의 관련성에도 불구하고 force feedback 평가 미포함
- 3개 humanoid embodiment가 실제 dexterous 플랫폼의 다양성을 충분히 다루지 못할 수 있음

## 커버리지 격차

| 기준 | 충족 여부 |
|------|----------|
| Force/torque 평가 지표 | 아니오 (원격조작 품질 메트릭에 힘 조절 평가 미포함) |
| Deformable 객체 작업 | 아니오 |
| Tactile 센싱 | 아니오 |
| Multi-stage / long-horizon 작업 | 부분적 (일부 작업이 순차적 단계를 포함하나, 명시적 long-horizon 평가 프로토콜 없음) |
| Multi-hand 협동 | 예 (양팔 dexterous 조작이 핵심 초점) |

## 오픈소스 현황

오픈소스 (Python 98%, C++ 2%). GitHub: [cyjdlhy/TeleOpBench](https://github.com/cyjdlhy/TeleOpBench)
