# 11.8 XHand / Inspire Hand

- **전체 제목:** XHand (X-Hand로도 출시) 및 Inspire Hand (Inspire-Robots Dexterous Hand로도 알려짐)
- **제조사:** 중국 로보틱스 제조업체 (Inspire Hand는 Inspire-Robots; XHand 변형은 다양한 제조업체)
- **연도:** ~2023년부터 이용 가능; 2024-2025년 연구에서 점점 더 채택
- **DoF:** Inspire Hand: ~12 구동 (5개 손가락, 독립 굴곡/신전 + 일부 내전/외전); XHand: ~12-16 DoF (버전에 따라 다름)
- **비용:** 서양 제조 대안보다 상당히 저렴 (추정 $1,000-3,000 범위; 공급업체 및 구성에 따라 가격 다양)
- **Tactile 센싱:** 표준 없음 (일부 버전에서 선택적 tactile 모듈 지원)
- **구동 방식:** 기어 감속을 갖춘 DC 모터; 위치 제어

## 정량 사양

| 사양 | 값 |
|------|-----|
| 손가락 | 5개 (인체형 배치) |
| 구동 DoF (Inspire) | ~12 (독립 손가락 굴곡 + 엄지 대향) |
| 구동 DoF (XHand) | ~12-16 (버전에 따라 다름) |
| 무게 | ~500-800g (버전에 따라 다름) |
| Grip force | 중간 (일반적인 조작 작업에 충분) |
| 제어 인터페이스 | Serial/CAN bus; 일부 버전에서 ROS 드라이버 이용 가능 |
| 시뮬레이션 모델 | MuJoCo, IsaacGym (커뮤니티 기여 URDF) |

## 핵심 방법론/설계

XHand와 Inspire Hand는 적절한 비용, 충분한 DoF, 상용 가용성의 결합으로 로보틱스 연구 커뮤니티에서 상당한 견인력을 얻은 중국 제조 dexterous hand이다. 오픈소스 연구용 hand(LEAP, ORCA, ISyHand, RUKA, FAIVE)와 달리 이들은 전문급 제작 품질을 갖춘 상용 생산 제품이다. Shadow Hand(~$100K+) 또는 Allegro Hand(~$15K+)보다 저렴하고, 조립 없이 상용으로 구매 가능하며, 의미 있는 dexterous 조작 연구를 위한 충분한 DoF(12-16)를 갖춘 실용적 틈새를 채운다. Inspire Hand와 XHand는 문헌에서 때때로 혼용되지만, 서로 다른 제조업체의 서로 다른 사양을 가진 제품이다.

## 서베이 대상 연구에서의 활용

이 hand는 전용 하드웨어 항목이 없었음에도 서베이 전반에 빈번하게 등장한다:
- **DexMachina** (§1): 양팔 조작의 대상 embodiment로 Inspire Hand와 XHand 모두 사용
- **ManipTrans** (§1): cross-embodiment 모션 전이를 위한 6개 지원 hand 중 Inspire Hand와 XHand 포함
- **DexUMI** (§1): 실제 dexterous 조작에 XHand와 Inspire Hand 사용 (CoRL 2025 Best Paper Finalist)
- **UniDex-VLA** (§2): 8-hand FAAS 프레임워크에 Inspire와 XHand 모두 포함
- **iDP3** (§6): Fourier GR1 humanoid에 Inspire Hand (25 DoF 구성)
- **Dex1B** (§8): 10억 개 시연 데이터셋에 Inspire Hand 포함

## 주요 기여 (연구 플랫폼으로서)

- 최근 연구에서 가장 빈번하게 채택된 상용 dexterous hand 중 하나, 특히 중국 로보틱스 커뮤니티에서
- multi-finger 조작 하드웨어가 필요한 연구실을 위한 Shadow/Allegro의 비용 효율적 대안
- 검증된 cross-embodiment 호환성: Shadow, Allegro, LEAP와 함께 retargeting 프레임워크(ManipTrans, UniDex-VLA FAAS)에 성공적으로 통합
- 상용 가용성으로 조립 시간과 보정 노력 제거
- 시뮬레이션용 커뮤니티 기여 URDF/MJCF 모델의 성장하는 생태계

## 한계점

- 논문 간 사양 비일관적 보고: "Inspire Hand"에 대해 수동 관절 계산 방법에 따라 12에서 25까지 다양한 DoF 보고, 직접 비교 어려움
- 표준화된 시뮬레이션 모델 없음: URDF/MJCF 파일이 커뮤니티 기여이며 실제 하드웨어와 정확히 일치하지 않을 수 있음
- 비공개 하드웨어: CAD 파일이나 펌웨어 수정 불가
- 표준 구성에서 통합 tactile 센싱 없음
- 문서와 지원이 주로 중국어; 영어 문서가 제한적일 수 있음
- 다수 제조업체와 버전이 혼란 유발: "XHand"와 "Inspire Hand"가 다른 제품임에도 때때로 혼동
- 제작 품질과 일관성이 생산 배치와 공급업체 간에 다를 수 있음
- 액추에이터 사양(대역폭, 힘, 반복성)에 대한 독립적 벤치마킹 제한적

## 오픈소스 현황

비공개 상용 제품. Inspire Hand는 [inspire-robots.com](https://www.inspire-robots.com/)에서 구매 가능. XHand는 다양한 중국 로보틱스 공급업체에서 구매 가능. 커뮤니티 기여 URDF 모델은 일부 연구 저장소(ManipTrans, DexMachina)에서 이용 가능.
