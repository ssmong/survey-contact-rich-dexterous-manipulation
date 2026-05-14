# 9.8 Isaac Lab

- **전체 제목:** Isaac Lab (구 Orbit): A Unified and Modular Framework for Robot Learning
- **개발:** NVIDIA (Isaac Sim 팀); Orbit (Mittal et al., IEEE RA-L 2023)에서 발전하여 deprecated된 IsaacGym (Preview 4)을 대체
- **학회/연도:** IEEE RA-L 2023 (Orbit 논문); Isaac Lab 리브랜딩 및 주요 업데이트 2024
- **시뮬레이션 플랫폼:** NVIDIA Isaac Sim 기반, PhysX 5 (GPU 가속) 구동
- **Dexterous 지원:** Allegro Hand, Shadow Hand, 임의 URDF/MJCF 기반 hand; articulated hand 환경 기본 지원
- **물리 엔진:** GPU 병렬 rigid 및 deformable body 시뮬레이션을 지원하는 PhysX 5
- **성능:** 단일 GPU에서 수천 개의 병렬 환경; 개선된 API 설계로 IsaacGym과 비슷한 속도

## 핵심 방법론/설계

Isaac Lab은 NVIDIA의 통합 로봇 학습 프레임워크로, Isaac Sim 위에 구축되었으며 IsaacGym (Preview 4 이후 deprecated)과 이전 Orbit 프레임워크의 후속으로 설계되었다. GPU 병렬화된 로봇 학습 환경을 생성하기 위한 모듈식, 확장 가능한 API를 제공한다. 프레임워크는 RL, imitation learning, sim-to-real transfer 워크플로우를 지원한다. IsaacGym의 독립형 Python API와 달리, Isaac Lab은 전체 Isaac Sim 생태계와 통합되어 사실적 렌더링(RTX ray tracing), domain randomization, 센서 시뮬레이션(카메라, LiDAR), 에셋 관리에 대한 접근을 제공한다. 환경 API는 벡터화된(병렬) 실행을 지원하는 gymnasium 호환 인터페이스를 따른다.

## 주요 기여

- deprecated된 IsaacGym (Preview 4)을 NVIDIA의 유지보수되는 로봇 학습 시뮬레이션 프레임워크로 대체
- PhysX 5를 통한 GPU 병렬 환경 실행으로 하나의 GPU에서 수천 개의 동시 환경 가능
- 구성을 통한 교체 가능한 로봇, 센서, 작업, 보상 함수의 모듈식 설계
- 시각적 sim-to-real transfer를 위한 RTX 사실적 렌더링
- dexterous hand 플랫폼 (Allegro, Shadow) 내장 지원 및 사전 구성 환경
- 주요 RL 라이브러리 (rl_games, RSL-rl, SKRL, Stable Baselines3)와 호환

## 서베이 대상 연구에서의 활용

Isaac Lab (또는 전신인 Isaac Sim / IsaacGym)은 본 서베이의 여러 시스템의 시뮬레이션 플랫폼이다:
- **GR00T-Dexterity** (§7): Isaac Lab에서 Allegro Hand RL 학습
- **DextrAH-G/RGB** (§7): Isaac Lab에서 geometric fabric를 활용한 Allegro Hand + Kuka
- **CHIP** (§5): Isaac Sim에서 humanoid impedance policy 학습
- **GR00T N1** (§6): Isaac Lab에서 policy 평가 및 sim-to-real
- **TeleOpBench** (§9): Isaac Sim 기반 원격조작 벤치마크

## IsaacGym과의 관계

IsaacGym (Preview 1-4)은 NVIDIA의 독립형 GPU 병렬 RL 시뮬레이션 라이브러리로, dexterous 조작 연구(in-hand rotation, DexPBT, HORA 등)에 널리 사용되었다. IsaacGym은 현재 deprecated되어 더 이상 유지보수되지 않는다. Isaac Lab이 전체 Isaac Sim 플랫폼 기반의 더 모듈식 아키텍처로 이를 대체한다. 주요 차이점:
- IsaacGym: 독립형 Python 라이브러리, 제한된 렌더링, 센서 시뮬레이션 없음
- Isaac Lab: 전체 Isaac Sim 통합, RTX 렌더링, 카메라/LiDAR 시뮬레이션, domain randomization
- 마이그레이션: 대부분의 IsaacGym 환경은 API 변경으로 Isaac Lab으로 이식 가능; NVIDIA가 마이그레이션 가이드 제공

## 한계점

- NVIDIA GPU 필요 (AMD/Intel 미지원); NVIDIA 독점 Isaac Sim 플랫폼에 종속
- MuJoCo 또는 Genesis보다 무거운 설치 용량 (멀티-GB인 Isaac Sim 필요)
- 비공개 물리 엔진 (PhysX): 접촉을 통한 미분 불가 (Genesis 또는 DiffTactile과 달리)
- 내장 tactile 센서 시뮬레이션 없음 (외부 플러그인 필요)
- 학습 곡선: IsaacGym의 단순한 독립형 인터페이스보다 복잡한 API
- 전체 기능을 위해 Linux 전용 (Windows 지원은 부분적)

## 커버리지 격차

| 기준 | 충족 여부 |
|------|----------|
| Force/torque 평가 지표 | 아니오 (force sensing 가능하나 표준화된 힘 평가 없음) |
| Deformable 객체 작업 | 예 (PhysX 5가 soft body 지원) |
| Tactile 센싱 | 아니오 (내장 tactile 시뮬레이션 없음; 외부 플러그인 필요) |
| Multi-stage / long-horizon 작업 | 부분적 (manager 기반 작업 API가 multi-stage 지원하나, 사전 구축 예제 적음) |
| Multi-hand 협동 | 부분적 (bimanual 셋업 가능하나 광범위하게 벤치마킹되지 않음) |

## 오픈소스 현황

BSD-3-Clause 라이선스 오픈소스. `pip install isaaclab` (Isaac Sim 필요)로 설치. GitHub: [isaac-sim/IsaacLab](https://github.com/isaac-sim/IsaacLab). 문서: [isaac-sim.github.io/IsaacLab](https://isaac-sim.github.io/IsaacLab/)
