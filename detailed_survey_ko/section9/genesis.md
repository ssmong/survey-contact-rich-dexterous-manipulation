# 9.5 Genesis

- **전체 제목:** Genesis: A Universal and Generative Physics Engine for Robotics and Beyond
- **저자:** Genesis-Embodied-AI 팀 (다기관 협업)
- **학회/연도:** 2024년 12월 (preprint, 2025년 1월 성능 벤치마킹 보고서 포함)
- **시뮬레이션 플랫폼:** Custom multi-physics engine
- **Dexterous 지원:** 임의 URDF 기반 hand; rigid-body, deformable, fluid 상호작용 지원
- **물리 solver:** Rigid body dynamics, MPM (Material Point Method), SPH (Smoothed Particle Hydrodynamics), FEM (Finite Element Method), PBD (Position-Based Dynamics), Stable Fluid
- **성능:** 단일 RTX 4090에서 Franka arm 시뮬레이션 시 4,300만 FPS 이상

## 핵심 방법론/설계

Genesis는 6개의 개별 물리 solver를 단일 API로 통합하는 범용 물리 플랫폼으로 설계되었다. 범용 로보틱스 및 embodied AI 응용을 목표로 하며, 물리 엔진, 로보틱스 시뮬레이션 플랫폼, 사실적 렌더링 시스템, 생성 데이터 엔진으로 동시에 기능한다. 시스템은 완전 미분 가능하도록 설계되었다 (현재 MPM 및 Tool Solver에서 지원, 다른 solver는 계획 중). CPU, NVIDIA/AMD GPU, Apple Metal에서의 크로스 플랫폼 실행을 지원한다.

## 주요 기여

- rigid, soft, fluid, cloth 시뮬레이션을 단일 API로 통합하는 통합 multi-physics 엔진
- GPU 병렬 연산을 통한 고속 시뮬레이션 (rigid-body 43M+ FPS)
- 조작 작업에 대한 gradient 기반 최적화를 가능하게 하는 미분 가능 시뮬레이션
- 다중 GPU 백엔드 옵션을 갖춘 크로스 플랫폼 지원 (Linux, macOS, Windows)
- 다양한 로봇 유형 (팔, 다리 로봇, 드론, soft 로봇) 및 파일 형식 (.xml, .urdf, .obj, .glb, .ply, .stl) 지원

## 한계점

- 미분 가능성이 현재 MPM 및 Tool Solver로 제한; rigid-body 및 FEM solver는 아직 미분 불가
- MuJoCo 또는 Isaac Lab에 비해 커뮤니티 채택이 적고 사전 구축 작업 환경이 적은 비교적 새로운 플랫폼
- dexterous 조작에 대한 접촉 역학 정확도가 기존 시뮬레이터와 아직 광범위하게 벤치마킹되지 않음
- 사실적 렌더링 기능이 주장되나 sim-to-real 시각 transfer에 대해 아직 널리 검증되지 않음

## 커버리지 격차

| 기준 | 충족 여부 |
|------|----------|
| Force/torque 평가 지표 | 아니오 (물리 지원에도 불구하고 표준화된 힘 기반 평가 메트릭 없음) |
| Deformable 객체 작업 | 예 (MPM, FEM, PBD solver가 deformable 상호작용 지원) |
| Tactile 센싱 | 아니오 (tactile 센서 시뮬레이션 모듈 없음) |
| Multi-stage / long-horizon 작업 | 아니오 (사전 구축된 long-horizon 작업 suite 없음; 플랫폼이 커스텀 작업 지원) |
| Multi-hand 협동 | 아니오 |

## 오픈소스 현황

오픈소스. `pip install genesis-world`로 설치. GitHub: [Genesis-Embodied-AI/Genesis](https://github.com/Genesis-Embodied-AI/genesis)
