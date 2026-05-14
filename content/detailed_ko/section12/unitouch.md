# 12.2 UniTouch

- **전체 제목:** UniTouch: Universal Touch Representation for Robot Manipulation
- **저자:** Che Fang 외 (UCSD)
- **학회/연도:** CVPR 2024
- **지원 센서:** 다수의 비전 기반 tactile 센서
- **정렬:** 터치-비전-언어-소리 멀티모달 정렬
- **사전학습 방법:** tactile 표현을 비전, 언어, 오디오 모달리티와 정렬하는 contrastive learning

## 핵심 방법론/설계

UniTouch는 터치 신호를 세 가지 다른 모달리티 -- 비전, 언어, 소리 -- 와 정렬하여 통합된 tactile 표현을 학습한다. Contrastive learning(CLIP 스타일)을 사용하여 tactile 이미지를 시각 이미지, 텍스트 설명, 접촉 이벤트의 오디오 녹음과 공유 임베딩 공간에 매핑한다. 이 멀티모달 정렬은 zero-shot 전이를 가능하게 한다: tactile 표현을 언어("거친 표면")로 쿼리하거나 tactile별 레이블 없이 시각적 외형과 매칭할 수 있다. 이 접근법은 터치, 비전, 언어, 소리가 물리적 접촉에 대한 상보적 설명을 제공한다는 통찰에 기반한다.

## 주요 기여

- 크로스 모달 쿼리(예: "사포처럼 느껴지는 텍스처 찾기"를 비전이나 언어에서)를 가능하게 하는 최초의 터치-비전-언어-소리 정렬 모델
- 작업별 학습 없이 언어-tactile 정렬을 통한 zero-shot tactile 분류
- tactile 데이터가 언어 및 비전 인코더의 풍부한 의미론에서 이점을 얻을 수 있는 통합 표현 공간
- 재료 분류 및 접촉 속성 추정을 포함한 다수의 downstream 작업에서 입증

## 정량적 결과

| 작업 | 메트릭 | UniTouch | 비전 전용 baseline | 터치 전용 baseline |
|------|--------|----------|-------------------|-------------------|
| 재료 분류 (zero-shot) | Accuracy (%) | 언어 정렬을 통해 가능 | 해당 없음 | 해당 없음 (레이블 필요) |
| 크로스 모달 검색 (터치-to-비전) | Recall@K | 시연됨 | N/A | N/A |
| 접촉 속성 추정 | 회귀 오차 | 지도학습과 경쟁적 | 접촉 속성에서 비전 전용이 더 낮음 | 접촉 특화 작업에서 더 우수 |

*참고: UniTouch의 주요 이점은 단일 모달리티 모델이 수행할 수 없는 zero-shot 및 크로스 모달 기능을 가능하게 하는 것이다. 지도학습 baseline과의 직접적 정확도 비교는 작업에 따라 다르다.*

## 한계점

- 멀티모달 정렬 품질이 쌍으로 된 터치-비전-언어-소리 데이터의 가용성과 품질에 크게 의존하며, 이는 부족함
- 소리 모달리티는 충격/접촉 이벤트에 유용하나 준정적 조작(grasping, sliding)에서는 덜 유용
- 표현이 분류/검색 작업에 최적화; closed-loop 조작 policy 학습에 대한 유용성 미시연
- 비전 기반 tactile 센서로 제한; 비시각 tactile 모달리티 미지원

## 공유 한계

본 섹션의 모든 tactile 표현 모델과 마찬가지로, UniTouch는 closed-loop 조작 policy에의 통합을 시연하지 않는다. 이 공유 한계에 대한 상세한 논의는 [Sparsh](sparsh.md#공유-한계-closed-loop-policy-통합-부재)를 참조.

## 오픈소스 현황

오픈소스 (코드 + 사전학습 가중치). GitHub: [cfeng16/UniTouch](https://github.com/cfeng16/UniTouch)
