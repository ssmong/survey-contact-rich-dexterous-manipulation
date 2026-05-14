# 9.1 ManiSkill3

- **전체 제목:** ManiSkill3: GPU Parallelized Robotics Simulation and Benchmark with Enhanced Visual and Contact-Rich Environments
- **저자:** Stone Tao, Fanbo Xiang, Arth Shukla, Yuzhe Qin, Xander Gao, Hao Su 외 (UCSD, Stanford 등)
- **학회/연도:** RSS 2025 (arXiv 2410.00425, 2024년 10월)
- **시뮬레이션 플랫폼:** GPU 병렬 물리(PhysX 5) 및 렌더링을 갖춘 SAPIEN
- **Dexterous 지원:** Allegro Hand, DClaw; 임의 URDF hand로 확장 가능
- **작업:** rigid-body, deformable, fluid 조작에 걸친 20개 이상의 작업군; dexterous in-hand reorientation 및 multi-finger grasping 환경 포함
- **성능:** 이전 ManiSkill 버전 대비 최대 430배 빠름; 단일 GPU에서 수천 개의 병렬 환경 지원

## 핵심 방법론/설계

ManiSkill3는 물리 stepping과 시각 렌더링 모두에서 GPU 병렬성을 활용하도록 시뮬레이션 루프를 재설계한다. SAPIEN의 PhysX 5 백엔드를 래핑하여 수천 개의 환경을 동시에 실행함으로써, 이전에 며칠이 걸리던 RL 학습을 수 분 만에 완료할 수 있게 한다. 프레임워크는 RL (PPO, SAC), imitation learning, VLA 평가를 위한 내장 baseline과 함께 통합된 Gym 호환 API를 제공한다.

## 주요 기여

- rigid-body 작업에서 ManiSkill2 대비 430배 속도 향상을 달성하는 GPU 병렬 시뮬레이션, soft-body 및 fluid 작업에서도 상당한 속도 향상
- RL, IL (Diffusion Policy, ACT), VLA (RT-2, Octo)에 걸친 baseline을 갖춘 표준화된 비교를 위한 통합 벤치마크
- dexterous 조작 작업을 위한 개선된 충돌 감지 및 마찰 모델링을 갖춘 향상된 contact-rich 환경

## 한계점

- tactile 센싱 시뮬레이션이 제한적; 고해상도 tactile 센서 모델 (예: GelSight, DIGIT) 네이티브 지원 없음
- soft-body 시뮬레이션은 지원되지만 rigid-body보다 느리고 dexterous 작업에 대해 덜 철저하게 벤치마킹됨
- dexterous hand 작업에 대한 sim-to-real transfer 결과가 논문에서 광범위하게 검증되지 않음

## 커버리지 격차

| 기준 | 충족 여부 |
|------|----------|
| Force/torque 평가 지표 | 아니오 |
| Deformable 객체 작업 | 예 (soft-body 및 fluid 작업 포함, dexterous hand에 대해서는 벤치마킹 부족) |
| Tactile 센싱 | 아니오 (네이티브 tactile 센서 모델 없음) |
| Multi-stage / long-horizon 작업 | 부분적 (일부 multi-step 작업 있으나 체계적인 long-horizon suite 아님) |
| Multi-hand 협동 | 아니오 |

## 오픈소스 현황

완전 오픈소스. `pip install mani-skill`로 설치. GitHub: [haosulab/ManiSkill](https://github.com/haosulab/ManiSkill)
