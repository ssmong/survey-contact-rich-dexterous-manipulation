# 12.4 NeuralFeels

- **전체 제목:** NeuralFeels: Neural Field Methods for Tactile-Visual Object State Tracking
- **저자:** Suddhu Sudharshan, Haozhi Qi, Pieter Abbeel, Jitendra Malik, Roberto Calandra, Michael Kaess 외 (Meta FAIR, CMU, Berkeley)
- **학회/연도:** Science Robotics, 2024
- **하드웨어:** Allegro Hand (16 DoF) + DIGIT tactile 센서 (4개 손가락 끝)
- **방법:** tactile 및 visual 관측을 융합하는 neural radiance field (NeRF 스타일)
- **작업:** 조작 중 in-hand 객체 포즈 및 형상 트래킹

## 핵심 방법론/설계

NeuralFeels는 dexterous in-hand 조작 중 객체 상태 트래킹 문제에 neural field 방법(NeRF 기반)을 적용한다. 시스템은 외부 카메라의 시각 관측과 Allegro Hand 손가락 끝에 장착된 DIGIT 센서의 tactile 이미지를 융합한다. Neural field가 객체의 형상과 외형을 표현하며, hand가 객체를 조작하는 동안 지속적으로 업데이트된다. Tactile 관측은 시각적 모호성(예: 손가락이 객체를 가리는 경우)을 해결하는 로컬 접촉 기하학을 제공하고, visual 관측은 전역 형상 컨텍스트를 제공한다. 이 융합으로 객체가 심하게 가려지는 복잡한 in-hand 조작 중에도 정확한 6-DoF 포즈 트래킹이 가능하다.

## 주요 기여

- dexterous in-hand 조작 중 실시간 tactile-visual 객체 트래킹을 위한 최초의 neural field 방법
- 다양한 객체의 in-hand 조작을 수행하는 실제 Allegro Hand + DIGIT 하드웨어에서 시연
- 공유 neural field 표현을 통한 tactile(로컬 접촉 기하학)과 visual(전역 형상) 관측의 원리적 융합
- 이 연구 방향에서 가장 높은 임팩트 학술지 중 하나인 Science Robotics에 게재

## 정량적 결과 (포즈 트래킹)

| 객체 카테고리 | 포즈 오차 (이동, mm) | 포즈 오차 (회전, deg) | 비전 전용 baseline | Tactile 전용 baseline |
|-------------|---------------------|---------------------|-------------------|---------------------|
| 단순 기하학 | 낮음 | 낮음 | 더 높음 (가림 오차) | 더 높음 (전역 컨텍스트 없음) |
| 복잡/텍스처 객체 | 낮음 | 낮음 | 중간 | 더 높음 |
| 심하게 가려진 시나리오 | 낮음 (tactile이 가림 해결) | 낮음 | 상당히 나쁨 | 비슷 |

*참고: 정확한 수치값은 Science Robotics 출판물에 보고되어 있다. 핵심 발견은 tactile-visual 융합이 어느 한 모달리티만 사용하는 것보다 일관되게 우수하며, 비전만으로 실패하는 심하게 가려진 시나리오에서 가장 큰 성능 향상을 보인다는 것이다. Neural field 표현은 접촉 상태 변화를 통한 연속적 트래킹을 가능하게 한다.*

## 한계점

- 초기화를 위해 알려진 객체 3D 모델 필요; 사전 형상 정보 없이 새로운 객체에 적용 불가
- Neural field 최적화가 계산적으로 비쌈; 실시간 성능에 상당한 GPU 리소스 필요
- 트래킹만 수행(상태 추정); 조작 행동 생성을 위한 루프 닫기 없음
- Allegro Hand의 DIGIT 센서로 제한; 다른 센서-hand 조합에 대한 일반화 미시연
- 객체별 neural field가 각 새로운 객체에 대해 재학습 필요

## 공유 한계

본 섹션의 모든 tactile 표현 모델과 마찬가지로, NeuralFeels는 행동을 생성하는 closed-loop 조작 policy에 통합되지 않는다. 행동 생성이 아닌 상태 추정(포즈 트래킹)을 제공한다. 이 공유 한계에 대한 상세한 논의는 [Sparsh](sparsh.md#공유-한계-closed-loop-policy-통합-부재)를 참조. NeuralFeels는 능동적 조작 중 실제 dexterous 하드웨어에서 작동함으로써 네 모델 중 이 루프를 닫는 데 가장 가까이 다가가지만, 트래킹 출력이 인지-행동 사이클을 완성하려면 별도의 policy에 의해 소비되어야 한다.

## 오픈소스 현황

오픈소스. GitHub: [facebookresearch/neuralfeels](https://github.com/facebookresearch/neuralfeels)
