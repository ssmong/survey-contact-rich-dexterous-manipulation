# 11.7 Ability Hand

- **전체 제목:** Ability Hand
- **제조사:** PSYONIC Inc. (Champaign, IL, USA)
- **연도:** 상용화 (FDA 510(k) 승인; 터치 피드백을 갖춘 최초의 상용 의수)
- **DoF:** 6 구동 (독립적 5개 손가락 굴곡/신전 + 의수 버전에서 wrist rotation; 로보틱스 버전은 다를 수 있음)
- **비용:** 상용 가격 (비공개; 미국에서 보험/VA를 통해 의수 버전 보장)
- **Tactile 센싱:** 각 손가락 끝에 내장 터치 센서 (압력 감지; 의수 응용에서 감각 피드백 제공)
- **구동 방식:** 고속 DC 모터; 시중 가장 빠른 의수로 광고
- **인증:** 의수용 FDA 510(k) 승인

## 정량 사양

| 사양 | 값 |
|------|-----|
| 손가락 닫힘 속도 | 전체 닫힘 <500 ms (시중 이용 가능 중 가장 빠른 수준) |
| Grip force | 일상생활 작업에 충분 (구체적 N 미공개) |
| 무게 | ~450g (hand 단독, 의수 버전) |
| 손가락 | 5개 독립 구동 손가락 |
| 터치 센서 | 5개 손가락 끝 모두에 압력 센서 |
| 방수 | 일상 사용을 위한 IP 등급 (의수 버전) |
| 제어 인터페이스 | sEMG (의수); serial/API (연구용) |

## 핵심 방법론/설계

Ability Hand는 원래 의수 장치로 설계된 상용 제조 dexterous hand이다. 6 DoF(독립적 5개 손가락 구동 + wrist rotation), 통합 손가락 끝 터치 센서, 고속 구동을 갖추고 있다. 본 섹션의 연구용 오픈소스 hand(LEAP, ORCA, ISyHand, RUKA, FAIVE)와 달리, Ability Hand는 FDA 승인과 전문적인 제작 품질을 갖춘 양산 상용 제품이다. 로보틱스 연구에서는 조립이나 보정이 필요 없는 견고하고 센서가 장착된 플랫폼을 제공한다.

## 서베이 대상 연구에서의 활용

Ability Hand는 본 서베이에서 다음을 통해 등장한다:
- **UniDex-VLA** (§2): Allegro, LEAP, Shadow, Inspire, Wuji, Oymotion, XHand과 함께 FAAS (Fingertip Action-Agnostic Space) 프레임워크에서 지원되는 8개 hand 중 하나
- **Dex1B** (§8): 10억 개 시연 grasp 데이터셋의 embodiment 중 하나로 포함

## 주요 기여 (연구 플랫폼으로서)

- 최근 dexterous 조작 연구에 사용된 유일한 상용 제조, FDA 승인 hand
- 애프터마켓 수정 없이 tactile feedback을 제공하는 통합 손가락 끝 터치 센서
- 3D 프린트 또는 실험실 조립 대안을 초과하는 전문적 제작 품질과 신뢰성
- VLA 프레임워크(UniDex-VLA FAAS)와의 검증된 호환성
- 동적 조작 작업을 가능하게 하는 고속 구동

## 한계점

- 상용 가격이 오픈소스 대안(LEAP ~$3K, FAIVE ~$500-800)보다 상당히 높음
- 비공개 하드웨어: CAD 파일, 펌웨어, 설계 수정 불가
- 6 DoF는 LEAP(16), ORCA(17), ISyHand(18)보다 현저히 낮아 미세 dexterity 제한
- 원래 로보틱스가 아닌 의수용으로 설계: 제어 인터페이스와 형태가 연구 용도에 최적화되지 않을 수 있음
- 제한된 시뮬레이션 모델 가용성: 표준 시뮬레이터용 공식 URDF/MJCF 모델 없어 sim-to-real 파이프라인 구축이 어려움
- 터치 센서 데이터 형식과 API가 로보틱스 연구 워크플로우에 표준화되지 않을 수 있음

## 오픈소스 현황

비공개 상용 제품. [psyonic.io](https://www.psyonic.io/ability-hand)에서 구매 가능. 오픈소스 설계 파일 없음.
