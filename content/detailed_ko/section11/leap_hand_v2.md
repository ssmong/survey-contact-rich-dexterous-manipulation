# 11.1 LEAP Hand V2

- **전체 제목:** LEAP Hand V2: Advanced Dexterous Robotic Hand
- **저자:** Kenneth Shaw, Deepak Pathak (CMU)
- **학회/연도:** 2024 (V1: RSS 2023)
- **DoF:** 16 구동 + articulated palm
- **액추에이터:** Dynamixel 서보
- **비용:** ~$3,000
- **무게:** 경량 (표준 로봇 팔에 장착 가능)
- **Tactile 센싱:** 내장 없음 (애프터마켓 통합 가능)
- **시뮬레이션 모델:** MuJoCo, Isaac Lab

## 정량 사양

| 사양 | 값 |
|------|-----|
| 액추에이터 제어 대역폭 | ~50 Hz 유효 제어율 (Dynamixel 서보 제한) |
| 최대 손가락 끝 힘 | 이용 가능한 문서에 미보고 |
| 내구성 | 여러 연구 그룹에서 수천 회 grasp 사이클 입증 (CrossDex, SeqDex, HandelBot, DexCap, ComFree-Sim) |

## 핵심 방법론/설계

LEAP Hand V2는 원래 LEAP Hand (RSS 2023)를 기반으로 개선된 기계적 설계, 더 강한 액추에이터, grasp 안정성을 향상시키기 위한 articulated palm을 갖추었다. hand는 모든 관절에 Dynamixel 서보 모터를 사용하여 위치 및 전류(토크 프록시) 피드백을 제공한다. 설계는 연구 접근성을 강조한다: 모든 구조 부품이 3D 프린트 가능하거나 시판 부품을 사용하며, 부품 목록이 완전히 문서화되어 있다. V2는 grasp 범위를 넓히고 더 인간에 가까운 조작 패턴을 가능하게 하는 대향 가능한 palm 관절을 추가한다.

## 주요 기여

- 연구 커뮤니티에서 가장 널리 채택된 저비용 dexterous hand 중 하나 (CrossDex, SeqDex, HandelBot, DexCap, ComFree-Sim 등에서 사용)
- V1의 고정 palm 설계를 넘어 grasp 유형을 확장하는 articulated palm (V2)
- 여러 독립 연구 그룹에서 zero-shot transfer가 시연된 검증된 sim-to-real 파이프라인
- 연구 환경에서 수천 회 grasp 사이클을 견디는 견고한 기계적 설계

## 한계점

- 통합 tactile 센싱 없음; 손가락 끝 접촉이 위치 제어만으로 이루어짐
- Dynamixel 서보가 커스텀 액추에이터 대비 제한된 대역폭 (~50 Hz 유효 제어율)
- $3,000 비용은 dexterous hand로서는 저렴하지만 본 섹션에서 가장 높음
- 16 DoF는 인간 손(~20-25 기능적 DoF)보다 적어 일부 작업에서 조작 dexterity 제한

## 오픈소스 현황

완전 오픈소스 (CAD, 펌웨어, 소프트웨어). 프로젝트 페이지: [v2-adv.leaphand.com](https://v2-adv.leaphand.com/)
