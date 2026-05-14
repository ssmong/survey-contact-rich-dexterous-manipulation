# 12.1 Sparsh

- **전체 제목:** Sparsh: Self-Supervised Touch Representations for Vision-Based and Multi-Modal Tactile Sensing
- **저자:** Carolina Higuera, Akash Sharma, Chaithanya Krishna Bodduluri, Taosha Fan, Patrick Chaney, Mrinal Kalakrishnan, Michael Kaess, Byron Boots, Mike Lambeta, Tingfan Wu, Mustafa Mukadam (Meta FAIR, CMU)
- **학회/연도:** CoRL 2024
- **지원 센서:** DIGIT, GelSight (크로스 센서)
- **학습 데이터:** 다수 센서 유형에 걸친 460K+ tactile 이미지
- **사전학습 방법:** 자기지도학습(SSL) -- MAE (Masked Autoencoder), DINO, IJEPA 변형
- **벤치마크:** TacBench -- 5-task tactile 벤치마크 (force estimation, slip detection, texture classification, pose estimation, grasp stability)

## 핵심 방법론/설계

Sparsh는 다수 센서 유형(DIGIT, GelSight)의 대규모 tactile 이미지 코퍼스에서 자기지도학습을 사용하여 tactile 인코더를 학습한다. SSL 사전학습(MAE, DINO, IJEPA)을 사용함으로써, 비전 foundation model이 비레이블 이미지 데이터에서 학습하는 것과 유사하게 작업별 레이블 없이 tactile 표현을 학습한다. 핵심 혁신은 크로스 센서 일반화이다: DIGIT 이미지에서 학습된 표현이 센서 출력 간의 상당한 시각적 차이에도 불구하고 GelSight로 전이되며 그 반대도 마찬가지이다. Sparsh는 또한 tactile 표현 평가를 위한 표준화된 5-task 벤치마크인 TacBench를 도입한다.

## 주요 기여

- 크로스 센서 전이(DIGIT에서 GelSight 및 역방향)를 시연하는 최초의 대규모 SSL tactile 인코더
- TacBench: tactile 표현 평가를 위한 표준화된 5-task 벤치마크(force estimation, slip detection, texture classification, pose estimation, grasp stability)
- tactile 데이터에 대한 SSL 방법(MAE, DINO, IJEPA)의 체계적 비교, MAE와 DINO가 IJEPA보다 우수함을 발견
- tactile SSL의 규모 선례를 수립하는 460K+ 이미지 사전학습 코퍼스

## 정량적 결과 (TacBench)

| 작업 | 메트릭 | MAE | DINO | IJEPA | 지도학습 baseline |
|------|--------|-----|------|-------|------------------|
| Force estimation | RMSE (N) | SSL 중 최고 | MAE와 비슷 | 더 낮음 | SSL과 비슷 |
| Slip detection | Accuracy (%) | SSL 중 최고 | MAE와 비슷 | 더 낮음 | SSL과 비슷 |
| Texture classification | Accuracy (%) | 경쟁적 | 경쟁적 | 더 낮음 | 약간 우수 |
| Pose estimation | Error (mm/deg) | SSL 중 최고 | 비슷 | 더 낮음 | 비슷 |
| Grasp stability | Accuracy (%) | 경쟁적 | 경쟁적 | 더 낮음 | 비슷 |

*참고: MAE와 DINO가 TacBench 작업 전반에서 IJEPA를 일관되게 능가한다. SSL 방법이 지도학습 baseline과 비슷한 성능을 달성하여, 유용한 tactile 표현 학습에 작업별 레이블이 필요하지 않음을 입증한다.*

## 한계점

- 비전 기반 tactile 센서(DIGIT/GelSight 같은 카메라 기반)로 제한; resistive, capacitive, barometric tactile array 미처리
- 크로스 센서 전이는 시연되었으나 동일 센서 내 학습 대비 여전히 성능 저하
- TacBench 작업이 비교적 단순(분류, 회귀); 전체 조작 policy에서의 표현 평가 미수행
- 사전학습 데이터가 주로 평면 probing에서 수집; 접촉 기하학의 다양성 제한

## 공유 한계: closed-loop policy 통합 부재

**이 한계 -- closed-loop 조작 policy에의 미통합 -- 는 본 섹션의 모든 tactile 표현 모델(Sparsh, [UniTouch](unitouch.md), [AnyTouch](anytouch.md), [NeuralFeels](neuralfeels.md))이 공유한다.** 네 모델 모두 조작 policy(VLA 또는 RL) 내에서 tactile 인코더로서의 end-to-end 사용을 시연하기보다 독립적 인지 작업(분류, 회귀, 트래킹)에서 학습된 표현을 평가한다. 이 단절은 표현이 인지적 품질에 대해서는 검증되지만 행동적 유용성에 대해서는 검증되지 않음을 의미한다 -- 접촉력을 정확히 추정하는 표현이 grasp force 조절 방법을 결정하는 policy에 유용한 특징을 생성하지 않을 수 있다. 사전학습된 tactile 인코더를 dexterous 조작 policy의 tactile backbone으로 사용하여 이 루프를 닫는 것이 이 연구 방향의 핵심적인 다음 단계이다.

## 오픈소스 현황

완전 오픈소스 (코드 + 사전학습 가중치). GitHub: [facebookresearch/sparsh](https://github.com/facebookresearch/sparsh)
