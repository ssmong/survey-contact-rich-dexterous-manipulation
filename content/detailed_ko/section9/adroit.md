# 9.4 Adroit

- **전체 제목:** Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations
- **저자:** Aravind Rajeswaran, Vikash Kumar, Abhishek Gupta, Giulia Vezzani, John Schulman, Emanuel Todorov, Sergey Levine
- **학회/연도:** RSS 2018
- **시뮬레이션 플랫폼:** MuJoCo
- **Dexterous 지원:** Shadow Hand (24 DoF) 시뮬레이션 모델 (ADROIT hand로 지칭)
- **작업:** 4개 표준 작업 -- pen rotation, door opening, hammer use, ball relocation
- **시연:** CyberGlove를 통해 작업당 25개 인간 시연 수집

## 핵심 방법론/설계

Adroit는 소수의 인간 시연과 RL fine-tuning을 결합하여 복잡한 dexterous 조작 작업을 해결하는 DAPG (Demo Augmented Policy Gradient) 알고리즘을 도입했다. MuJoCo의 Shadow Hand 모델은 dexterous RL 벤치마킹의 사실상 표준이 되었다. 인간 시연은 CyberGlove 원격조작 인터페이스를 통해 수집되며, 고차원 dexterous action space의 탐색 과제를 극복하기 위해 policy 초기화에 사용된다.

## 주요 기여

- 여전히 널리 사용되는 4개 작업(pen, door, hammer, ball)을 갖춘 dexterous RL의 표준 벤치마크 확립
- 소수의 인간 시연이 고-DoF hand의 RL을 극적으로 가속화함을 보여주는 DAPG 알고리즘
- 커뮤니티 표준이 된 MuJoCo용 24-DoF Shadow Hand 오픈소스 모델

## 한계점

- 비교적 단순한 접촉 패턴을 가진 4개 작업만 해당; multi-stage 또는 도구 사용 조작을 다루지 않음
- Shadow Hand 모델에 tactile 센싱 시뮬레이션 부재
- 당시 MuJoCo가 CPU 전용이었으며; 대규모 학습을 위한 GPU 가속 대안에 의해 대체되었으나 여전히 표준 평가 대상
- 원래 연구에서 sim-to-real gap이 다루어지지 않음

## 커버리지 격차

| 기준 | 충족 여부 |
|------|----------|
| Force/torque 평가 지표 | 아니오 |
| Deformable 객체 작업 | 아니오 |
| Tactile 센싱 | 아니오 |
| Multi-stage / long-horizon 작업 | 아니오 (각 작업이 단일 단계 목표) |
| Multi-hand 협동 | 아니오 |

## 오픈소스 현황

완전 오픈소스. `pip install gymnasium-robotics` (Gymnasium-Robotics가 유지보수된 Adroit 환경 제공)로 설치 가능. 원본 코드: [GitHub](https://github.com/aravindr93/hand_dapg)
