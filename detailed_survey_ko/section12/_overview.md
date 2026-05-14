# Section 12: Tactile 표현 모델

Tactile 센싱은 비전만으로는 포착할 수 없는 접촉 기하학, 힘, 재료 특성의 직접 측정을 제공한다. 그러나 원시 tactile 신호(GelSight/DIGIT의 고해상도 이미지, 또는 resistive 센서의 force array)는 고차원적이고 센서별로 특화되어 있다. Tactile 표현 모델은 ImageNet 사전학습된 비전 인코더가 일반적인 시각 특징을 제공하는 것과 유사하게, tactile 데이터의 compact하고 전이 가능한 인코딩을 학습한다. 본 섹션에서는 tactile 표현을 위한 foundation model을 다룬다.

## 항목

| 항목 | 센서 | 방법 | 핵심 강점 |
|------|------|------|-----------|
| [Sparsh](sparsh.md) | DIGIT, GelSight | SSL (MAE, DINO, IJEPA) | 크로스 센서 전이; TacBench 벤치마크 |
| [UniTouch](unitouch.md) | 다수의 비전 기반 센서 | Contrastive (CLIP 스타일) | 터치-비전-언어-소리 정렬 |
| [AnyTouch](anytouch.md) | 4개 이상 유형 (TacQuad) | 크로스 센서 SSL | 가장 강력한 크로스 센서 일반화 |
| [NeuralFeels](neuralfeels.md) | Allegro Hand의 DIGIT | Neural fields (NeRF 스타일) | 실제 하드웨어 tactile-visual 융합 상태 추정 |

## 공유 한계

본 섹션의 네 가지 tactile 표현 모델 모두 학습된 표현을 분류, 회귀, 트래킹 벤치마크에서 시연하며 -- closed-loop 조작 policy(VLA 또는 RL) 내에서 tactile 인코더로서의 end-to-end 통합을 보여주는 것은 없다. 표현 학습과 조작 policy 학습 간의 이 단절이 이 분야에서 가장 중요한 격차이다. 이 공유 한계에 대한 상세한 논의는 [Sparsh 항목](sparsh.md)을 참조.

## 관찰 사항

Tactile 표현 모델은 비전 foundation model의 궤적을 3-5년 지연으로 따르고 있다: 대규모 비레이블 데이터에 대한 SSL 사전학습(Sparsh), 멀티모달 정렬(UniTouch), 크로스 센서 일반화(AnyTouch), 작업별 neural field(NeuralFeels). 현장은 비전 기반 tactile 센서(DIGIT, GelSight)를 주요 입력 모달리티로 수렴했으며, 이는 강점(기존 비전 인코더 아키텍처 활용)이자 한계(resistive array, barometric 센서, Digit 360의 18개 이상 모달리티 같은 비시각 tactile 모달리티 배제)이다. 가장 중요한 격차는 표현 학습과 조작 policy 학습 간의 단절이다. NeuralFeels가 실제 Allegro + DIGIT 하드웨어에서 시연함으로써 이 루프를 닫는 데 가장 가까이 다가가지만, 행동 생성이 아닌 상태 추정을 제공한다. 사전학습된 tactile 인코더(Sparsh, UniTouch, AnyTouch)를 dexterous 조작 policy의 tactile backbone으로 사용하여 이 루프를 닫는 것은 아직 어떤 출판된 시스템도 시연하지 못한 명확한 다음 단계이다.
