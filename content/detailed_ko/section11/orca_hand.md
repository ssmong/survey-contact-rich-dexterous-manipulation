# 11.2 ORCA Hand

- **전체 제목:** ORCA Hand: An Affordable and Dexterous Robotic Hand for Contact-Rich Manipulation
- **저자:** ETH Zurich (Robotics Systems Lab)
- **학회/연도:** 2025
- **DoF:** 17 구동
- **비용:** <$2,000
- **Tactile 센싱:** 통합 tactile 센서
- **Sim-to-real:** 1시간 학습 시간으로 입증
- **시뮬레이션 모델:** 이용 가능 (표준 시뮬레이터와 호환)

## 정량 사양

| 사양 | 값 |
|------|-----|
| 액추에이터 제어 대역폭 | 이용 가능한 문서에 미보고 |
| 최대 손가락 끝 힘 | 이용 가능한 문서에 미보고 |
| 내구성 | 이용 가능한 문서에 미보고 |

## 핵심 방법론/설계

ORCA Hand는 contact-rich 조작 연구를 위해 특별히 설계된 17-DoF dexterous hand이다. 가장 큰 특징은 통합 tactile 센싱으로 -- 애프터마켓 추가가 아닌 처음부터 손가락 끝에 내장되어 있다. hand의 기계적 설계는 다양한 객체에 대한 grasp 안정성을 향상시키는 유연한 손가락 끝 구조로 견고한 접촉 상호작용을 강조한다. 함께 제공되는 sim-to-real 파이프라인은 RL policy가 총 약 1시간의 학습 시간으로 학습 및 전이될 수 있음을 보여준다.

## 주요 기여

- 설계 단계부터 통합된 tactile 센싱 -- 본 서베이에서 $2K 미만 유일한 내장 tactile dexterous hand
- 16-DoF 대안(LEAP Hand)보다 약간 높은 dexterity를 제공하는 17 DoF
- 실용적 배포 가능성을 보여주는 빠른 sim-to-real transfer 파이프라인 (1시간 학습)
- 커뮤니티 재현을 가능하게 하는 완전 오픈소스 하드웨어 설계

## 한계점

- LEAP Hand 대비 커뮤니티 채택과 검증이 적은 새로운 설계
- tactile 센서 사양(해상도, 모달리티)이 이용 가능한 문서에서 완전히 특성화되지 않음
- $2K 미만 비용은 추정치; 실제 제작 비용은 지역 부품 조달에 따라 다름

## 오픈소스 현황

완전 오픈소스 (하드웨어 + 소프트웨어). 프로젝트 페이지: [orcahand.com](https://www.orcahand.com/)
