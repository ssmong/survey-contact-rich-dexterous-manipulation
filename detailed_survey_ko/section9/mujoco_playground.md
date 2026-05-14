# 9.2 MuJoCo Playground

- **전체 제목:** MuJoCo Playground
- **저자:** Google DeepMind MuJoCo 팀 (Kevin Zakka, Baruch Tabanpour 외)
- **학회/연도:** RSS 2025 (systems demo 트랙)
- **시뮬레이션 플랫폼:** MuJoCo MJX (JAX 가속 MuJoCo)
- **Dexterous 지원:** LEAP Hand 작업 포함; MuJoCo 표준 모델 라이브러리를 통해 Shadow Hand 변형 사용 가능
- **작업:** 보행, dexterous 조작 (in-hand reorientation, cube rotation), whole-body 제어; 단일 GPU에서 수 분 만에 학습 가능한 작업

## 핵심 방법론/설계

MuJoCo Playground는 MuJoCo의 JAX 컴파일 버전인 MuJoCo MJX를 활용하여 GPU/TPU에서 완전히 대규모 병렬 시뮬레이션을 가능하게 한다. 보상 함수와 학습 스크립트가 포함된 엄선된 환경 컬렉션을 제공하며, policy를 수 시간이 아닌 수 분 만에 처음부터 학습할 수 있음을 보여준다. MuJoCo의 정확한 접촉 역학을 활용한 zero-shot sim-to-real transfer를 강조한다.

## 주요 기여

- 정확한 접촉 물리(MuJoCo)와 JAX 컴파일의 결합으로 일반 하드웨어에서 수 분 만에 dexterous policy 학습 가능함을 입증
- zero-shot sim-to-real transfer 결과를 포함한 LEAP Hand 조작용 사전 구축 환경
- 브라우저 기반 시각화 및 대화형 환경 탐색

## 한계점

- ManiSkill3 또는 Isaac Lab에 비해 좁은 작업 다양성; 포괄적 벤치마킹보다는 속도 시연에 초점
- 내장 tactile 시뮬레이션 또는 deformable 객체 지원 없음
- 기존 플랫폼 대비 문서화 및 커뮤니티 채택이 아직 성장 중

## 커버리지 격차

| 기준 | 충족 여부 |
|------|----------|
| Force/torque 평가 지표 | 아니오 |
| Deformable 객체 작업 | 아니오 |
| Tactile 센싱 | 아니오 |
| Multi-stage / long-horizon 작업 | 아니오 (cube rotation 같은 단일 목표 작업에 초점) |
| Multi-hand 협동 | 아니오 |

## 오픈소스 현황

Apache 2.0 오픈소스. `pip install playground`로 설치. GitHub: [google-deepmind/mujoco_playground](https://github.com/google-deepmind/mujoco_playground)
