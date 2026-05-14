# 10.5 DEXOP

- **전체 제목:** DEXOP: Dexterous Teleoperation with a Passive Exoskeleton
- **저자:** Stanford 팀
- **학회/연도:** arXiv 2509.04441, 2025년 9월
- **입력 모달리티:** 운영자의 손에 착용하는 수동식 exoskeleton
- **대상 hand:** 임의의 dexterous hand (범용 retargeting)
- **Force feedback:** exoskeleton 기계적 결합을 통한 고유수용감각 피드백
- **비용:** 미보고 (연구용 프로토타입)

## 핵심 방법론/설계

DEXOP은 운영자가 손 위에 착용하는 수동식(비구동) exoskeleton을 사용한다. exoskeleton은 대상 로봇 hand의 kinematics를 기계적으로 미러링하여, 운영자의 손가락 동작이 kinematic 결합을 통해 직접 로봇 hand 관절을 구동한다. exoskeleton이 수동식이므로 본질적인 고유수용감각 피드백을 제공한다 -- 운영자가 exoskeleton 구조의 기계적 저항을 느끼며, 이는 로봇 hand의 관절 한계와 기계적 impedance를 근사한다. 이 접근법은 기본적인 force feedback을 위한 전자 센서나 액추에이터의 필요성을 제거한다.

## 주요 기여

- 전자장치 없이 본질적 고유수용감각 피드백을 제공하는 수동식(비구동) exoskeleton 설계
- 모듈식 kinematic 결합을 통한 임의의 dexterous hand 플랫폼에 대한 범용 retargeting
- 견고하고 저유지보수 작동을 가능하게 하는 기계적 단순성

## 한계점

- 고유수용감각 피드백이 실제 로봇-환경 접촉력이 아닌 exoskeleton 역학을 반영
- exoskeleton 설계가 서로 다른 로봇 hand kinematics에 맞게 커스터마이징되어야 함
- 능동 force 렌더링 없음으로 수동 compliance 피드백으로만 제한
- 부피가 큰 형태로 장시간 데이터 수집 세션에서 운영자 피로 유발 가능

## 데이터 품질 영향

수동식 exoskeleton은 운영자가 관절 한계를 존중하고 kinematically 실현 불가능한 구성을 피하도록 돕는 고유수용감각 피드백을 제공하여, 비전 전용 시스템 대비 위치 정확도를 향상시킨다. 그러나 피드백은 실제 로봇-환경 접촉력이 아닌 exoskeleton 역학을 반영한다. 시연은 kinematically 타당한 궤적을 캡처하지만 조작 작업 자체의 힘 정보가 없다. DEXOP 데이터로 학습된 policy는 더 깨끗한 관절 공간 궤적(retargeting artifact 감소)에서 이점을 얻지만, contact-rich 작업에 필요한 힘 인식이 여전히 부족하다. 고유수용감각 신호는 전체적인 운동 품질에 도움이 되지만, 힘 조절이 필요한 작업에서 downstream policy 성능을 제한하는 근본적인 force-blindness를 해결하지 못한다.

## 오픈소스 현황

프로젝트 페이지: [dex-op.github.io](https://dex-op.github.io/). 하드웨어 설계 공개 여부 불명확.
