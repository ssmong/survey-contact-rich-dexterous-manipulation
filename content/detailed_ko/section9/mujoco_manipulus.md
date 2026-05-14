# 9.3 MuJoCo Manipulus

- **전체 제목:** MuJoCo Manipulus: A Dexterous Tool Manipulation Benchmark
- **저자:** Google DeepMind 외
- **학회/연도:** 2025 (preprint)
- **시뮬레이션 플랫폼:** MuJoCo
- **Dexterous 지원:** 도구 조작을 수행하는 multi-finger hand
- **작업:** 망치질, 나사 조이기, 젓기 등 16개 기능적 도구 조작 시나리오를 포함한 도구 사용 작업

## 핵심 방법론/설계

Manipulus는 기존 시뮬레이션 벤치마크에서 충분히 다루어지지 않은 영역인 dexterous 도구 조작을 구체적으로 목표로 하는 벤치마크를 제공한다. 환경은 도구를 잡고, 재배향하고, 기능적으로 사용하기 위한 협응적 multi-finger 제어를 요구하며 -- 단순한 pick-and-place를 넘어 contact-rich 기능적 상호작용으로 나아간다. 작업은 도구 조작의 grasping 단계와 기능적 사용 단계 모두를 테스트하도록 설계되었다.

## 주요 기여

- MuJoCo에서 16개 개별 작업을 포함하는 최초의 전용 dexterous 도구 조작 벤치마크
- grasp 안정성과 기능적 dexterity 모두를 요구하는 도구 사용 능력의 체계적 평가
- 표준 MuJoCo 생태계 (Gymnasium, dm_control)와 호환

## 한계점

- 도구 기하학 및 물리적 속성이 실제 도구에 비해 단순화됨
- deformable 도구 또는 workpiece 상호작용 없음 (예: 자르기, 바르기)
- 도구 사용 policy에 대한 sim-to-real 검증 제한적

## 커버리지 격차

| 기준 | 충족 여부 |
|------|----------|
| Force/torque 평가 지표 | 아니오 |
| Deformable 객체 작업 | 아니오 (rigid 도구 및 workpiece만 해당) |
| Tactile 센싱 | 아니오 |
| Multi-stage / long-horizon 작업 | 부분적 (도구 사용이 grasp + 기능적 사용을 포함하나, 명시적 multi-stage 시퀀스는 아님) |
| Multi-hand 협동 | 아니오 |

## 오픈소스 현황

오픈소스. MuJoCo 생태계를 통해 이용 가능.
