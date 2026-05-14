# 12.3 AnyTouch

- **전체 제목:** AnyTouch: Learning Unified Tactile Representations Across Multiple Sensors
- **저자:** GeWu Lab (Renmin University of China)
- **학회/연도:** ICLR 2025
- **지원 센서:** 4개 이상 tactile 센서 유형 (TacQuad 데이터셋)
- **사전학습 방법:** 크로스 센서 자기지도학습
- **데이터셋:** TacQuad -- 4-센서 쌍 tactile 데이터셋

## 핵심 방법론/설계

AnyTouch는 동일 객체/접촉에 대한 네 가지 센서 유형의 쌍으로 된 tactile 판독값을 포함하는 TacQuad 데이터셋에서 사전학습하여 크로스 센서 패러다임을 확장한다. 이 쌍으로 된 데이터로 직접적인 크로스 센서 contrastive learning이 가능하다: 모델이 접촉 관련 정보를 보존하면서 센서별 시각적 artifact에 불변한 표현을 학습한다. 결과 인코더는 네 가지 센서 유형 중 어느 것의 tactile 데이터도 처리하여 호환 가능한 표현을 생성할 수 있어, 센서 플랫폼 간 tactile skill 전이가 가능하다.

## 주요 기여

- TacQuad 데이터셋: 최초의 대규모 쌍 멀티 센서 tactile 데이터셋 (4개 센서 유형, 동일 접촉)
- 쌍 데이터 contrastive learning을 통해 센서 불변 표현을 명시적으로 학습하는 크로스 센서 SSL
- fine-tuning 없이 센서 유형 간 tactile 표현 전이 시연
- tactile foundation model 중 가장 강력한 크로스 센서 일반화 결과

## 정량적 결과 (크로스 센서 전이)

| 평가 | AnyTouch | Sparsh | 단일 센서 baseline |
|------|----------|--------|-------------------|
| 동일 센서 내 성능 | 경쟁적 | 경쟁적 | 최고 (대상 센서에서 학습) |
| 크로스 센서 전이 (본 센서) | 최고 | 중간 정도 성능 저하 | 해당 없음 |
| 크로스 센서 전이 (미본 센서) | 저하되나 기능적 | 상당한 성능 저하 | 해당 없음 |
| 지원 센서 수 | 4+ | 2 (DIGIT, GelSight) | 1 |

*참고: AnyTouch의 쌍 데이터 contrastive learning이 Sparsh의 비쌍 SSL보다 강한 크로스 센서 일반화를 생성하지만, 둘 다 동일 센서 내 학습 대비 성능이 저하된다. 사전학습 중 보지 못한 센서 유형에 대한 성능은 여전히 한계로 남아 있다.*

## 한계점

- TacQuad 데이터셋 수집이 다수 센서로 동일 표면에 물리적으로 접촉해야 하므로 노동 집약적이며 데이터셋 규모 제한
- 4개 센서 유형은 Sparsh(2개)보다 많지만 tactile 센서 생태계의 일부만 다룸
- Sparsh 및 UniTouch와 마찬가지로 closed-loop 조작 policy에의 통합 미시연
- 사전학습 중 보지 못한 센서 유형에 대해 표현 품질 저하

## 공유 한계

본 섹션의 모든 tactile 표현 모델과 마찬가지로, AnyTouch는 closed-loop 조작 policy에의 통합을 시연하지 않는다. 이 공유 한계에 대한 상세한 논의는 [Sparsh](sparsh.md#공유-한계-closed-loop-policy-통합-부재)를 참조.

## 오픈소스 현황

오픈소스 (코드 + 사전학습 가중치). GitHub: [GeWu-Lab/AnyTouch](https://github.com/GeWu-Lab/AnyTouch)
