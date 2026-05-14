# 9.9 TACTO

- **전체 제목:** TACTO: A Fast, Flexible and Open-source Simulator for High-Resolution Vision-based Tactile Sensors
- **저자:** Shaoxiong Wang, Mike Lambeta, Po-Wei Chou, Roberto Calandra
- **기관:** Meta FAIR (Facebook AI Research)
- **학회/연도:** IEEE Robotics and Automation Letters (RA-L) 2022
- **시뮬레이션 플랫폼:** PyBullet (물리) + PyRender (tactile 렌더링)
- **센서 모델:** DIGIT, OmniTact, GelSight 스타일 비전 기반 tactile 센서
- **작업:** tactile 피드백을 활용한 grasping, rolling, 객체 조작

## 핵심 방법론/설계

TACTO는 접촉 기하학에서 합성 tactile 이미지를 렌더링하여 비전 기반 tactile 센서를 시뮬레이션한다. 물리적으로 정확한 접촉 변형 시뮬레이션을 시도하기보다, TACTO는 빠르고 시각적으로 그럴듯한 tactile 이미지 생성에 초점을 맞춘다. 객체가 시뮬레이션된 센서에 접촉하면, TACTO는 적절한 조명 및 gel 표면 속성으로 PyRender를 사용하여 접촉 패치를 렌더링하며, 실제 DIGIT 또는 GelSight 센서와 유사한 RGB tactile 이미지를 생성한다. 물리 시뮬레이션 (rigid body 역학, 충돌 감지)은 PyBullet이 처리하고, TACTO는 tactile 렌더링 파이프라인만 담당한다. 이러한 분리로 TACTO를 모든 PyBullet 기반 조작 환경에 통합할 수 있다.

## 주요 기여

- DIGIT 및 OmniTact 비전 기반 tactile 센서를 위한 고해상도 합성 tactile 이미지를 구체적으로 목표로 하는 최초의 오픈소스 시뮬레이터
- FEM 기반 대안(DiffTactile 등)보다 빠른 렌더링으로 tactile 관측을 활용한 RL 학습 가능
- 모듈식 설계: 센서 기하학 및 광학 속성을 YAML 파일로 구성 가능
- 얇은 API 레이어를 통한 기존 PyBullet 환경과의 간편한 통합
- 서버 측 학습을 위한 headless 렌더링 지원 (EGL/OSMESA)

## 서베이 대상 연구에서의 활용

TACTO 또는 그 tactile 시뮬레이션 접근법은 본 서베이의 여러 연구에서 참조되었다:
- **Sparsh** (§12): 시뮬레이션 및 실제 DIGIT 데이터로 tactile encoder 학습/평가
- **RotateIt** (§7): in-hand rotation에 tactile 시뮬레이션 사용
- DIGIT/GelSight를 사용하는 기타 tactile 조작 논문들이 사전학습 또는 augmentation을 위해 TACTO 스타일 시뮬레이션 데이터 활용

## 한계점

- 명시적으로 물리적으로 정확하지 않음: "접촉의 물리적으로 정확한 역학(예: 변형, 마찰)을 제공하기 위한 것이 아님" -- 접촉력과 변형은 근사적으로 처리
- PyBullet 백엔드가 GPU 병렬 엔진 (IsaacGym, ManiSkill3)에 비해 시뮬레이션 속도 제한
- 미분 가능 렌더링 없음: tactile 이미지 생성을 통해 gradient를 역전파할 수 없음
- 비전 기반 tactile 센서 (DIGIT, OmniTact, GelSight)로 제한; resistive, capacitive, barometric tactile 센서 시뮬레이션 불가
- 기본 제공되는 multi-finger dexterous hand 환경 없음 (예제는 parallel-jaw gripper에 초점)
- macOS에서 PyBullet과 PyRender 간 일부 시각화 문제

## 커버리지 격차

| 기준 | 충족 여부 |
|------|----------|
| Force/torque 평가 지표 | 아니오 (tactile 이미지는 시각적이며, 힘 보정되지 않음) |
| Deformable 객체 작업 | 아니오 (PyBullet을 통한 rigid body 물리만 해당) |
| Tactile 센싱 | 예 (핵심 기여 -- 합성 tactile 이미지 생성) |
| Multi-stage / long-horizon 작업 | 아니오 |
| Multi-hand 협동 | 아니오 |

## 오픈소스 현황

MIT 라이선스 오픈소스. `pip install tacto`로 설치. GitHub: [facebookresearch/tacto](https://github.com/facebookresearch/tacto)
