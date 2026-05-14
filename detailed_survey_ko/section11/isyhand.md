# 11.3 ISyHand

- **전체 제목:** ISyHand: An Intrinsically Soft Dexterous Hand for Contact-Rich Manipulation
- **저자:** MPI for Intelligent Systems (MPI-IS), Tubingen
- **학회/연도:** 2025
- **DoF:** 18 (손가락 12 DoF + palm/wrist 6 DoF)
- **비용:** ~$1,300
- **Tactile 센싱:** 내장 없음
- **구동 방식:** 본질적으로 soft(유연)한 관절을 갖춘 건 구동

## 정량 사양

| 사양 | 값 |
|------|-----|
| 액추에이터 제어 대역폭 | 이용 가능한 문서에 미보고 |
| 최대 손가락 끝 힘 | 이용 가능한 문서에 미보고 (유연 관절이 rigid 관절 설계 대비 최대 힘을 제한할 수 있음) |
| 내구성 | 이용 가능한 문서에 미보고 (건 마모가 잠재적 유지보수 우려) |

## 핵심 방법론/설계

ISyHand는 LEAP 같은 rigid 관절 hand와 근본적으로 다른 기계적 접근법을 취한다: 본질적으로 soft(유연)한 관절과 건 구동 방식을 사용한다. compliance가 제어를 통해서가 아니라 관절 역학에 내장되어 있다. 이는 hand가 grasping 중 객체 형상에 수동적으로 적응함을 의미하며 -- 명시적 힘 제어가 필요 없는 물리적 형태의 impedance이다. 18-DoF 설계(손가락 12 + palm/wrist 6)는 높은 dexterity를 제공하며, 건 구동 방식으로 모터를 전완에 배치하여 손가락 끝 무게와 관성을 줄인다.

## 주요 기여

- 명시적 impedance 제어 없이 수동적 힘 조절을 제공하는 본질적 기계적 compliance
- 본 서베이의 $2K 미만 hand 중 최고 DoF 수 (18)
- $1,300으로 최저 비용에서 최고 DoF를 제공하여 강력한 dexterity 대비 비용 효율
- 경량 손가락 끝과 낮은 관성을 가능하게 하는 건 구동 방식

## 한계점

- tactile 센싱 없음; 유연 관절이 암묵적 접촉 적응을 제공하나 명시적 접촉 측정 없음
- 건 구동 방식이 케이블 라우팅 복잡성과 잠재적 유지보수 문제 (건 마모, 이완) 도입
- 건 역학과 관절 compliance를 정확히 모델링하기 어려워 soft/compliant hand의 sim-to-real transfer가 더 도전적
- 유연 관절이 rigid 관절 설계 대비 최대 손가락 끝 힘을 제한할 수 있음

## 오픈소스 현황

프로젝트 페이지: [isyhand.is.mpg.de](https://isyhand.is.mpg.de/). 설계 파일 이용 가능.
