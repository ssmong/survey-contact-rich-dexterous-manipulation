# Section 11: 저비용 Dexterous Hand 하드웨어

저렴하고 연구급인 dexterous hand의 가용성은 dexterous 조작 연구를 확장하기 위한 전제 조건이다. 본 섹션에서는 오픈소스 설계, sim-to-real 호환성, 실용적 견고성을 갖추고 연구 커뮤니티를 대상으로 ~$3,000 이하로 설계된 hand를 다룬다.

## 항목

| 항목 | DoF | 비용 | Tactile | 구동 방식 | 핵심 차별점 |
|------|-----|------|---------|----------|------------|
| [LEAP Hand V2](leap_hand_v2.md) | 16 + articulated palm | ~$3,000 | 내장 없음 | Dynamixel 서보 | 가장 널리 채택; 검증된 sim-to-real |
| [ORCA Hand](orca_hand.md) | 17 | <$2,000 | 통합형 | 미명시 | $2K 미만 유일한 내장 tactile hand |
| [ISyHand](isyhand.md) | 18 (12+6) | ~$1,300 | 없음 | 건 구동, 유연 관절 | 본질적 기계적 compliance |
| [RUKA Hand](ruka_hand.md) | 15 | <$1,300 | 없음 | 미명시 | 최저 복잡도, 가장 쉬운 조립 |
| [FAIVE Hand](faive_hand.md) | 11+ | ~$500-800 | 없음 | 건 구동 (서보 모터) | 초저가, 완전 3D 프린팅 |
| [Ability Hand](ability_hand.md) | 6 | 상용 | 손가락 끝 압력 | DC 모터 | FDA 승인, 양산, UniDex-VLA에서 사용 |
| [XHand / Inspire Hand](xhand_inspire.md) | 12-16 | ~$1-3K | 표준 없음 | DC 모터 + 기어 | 최근 연구에서 가장 많이 사용되는 상용 dex hand |
| [Digit 360](digit360.md) | N/A (센서) | 미공개 | 18+ 모달리티 | N/A | 임의 hand용 모듈식 tactile 손가락 끝 |

## 관찰 사항

저비용 dexterous hand 환경은 명확한 비용-성능 프론티어를 보여준다: LEAP Hand V2 ($3K, 16 DoF, 널리 채택)가 상위를 차지하고, ISyHand ($1.3K, 18 DoF, compliant) 및 RUKA ($1.3K, 15 DoF, 단순)가 비용을 $1,500 이하로 낮춘다. 가장 주목할 만한 격차는 tactile 센싱이다: 완전한 hand 중 ORCA Hand만이 통합 tactile 센서를 포함한다. LEAP, ISyHand, RUKA 모두 애프터마켓 tactile 통합(예: DIGIT 또는 GelSight 센서 장착)이 필요하며, 이는 비용, 복잡성을 추가하고 손가락 끝 기하학을 변경하는 경우가 많다. Meta의 Digit 360이 모듈식 tactile 손가락 끝으로 이 격차를 해소할 수 있지만, 아직 공개적으로 이용 가능하지 않다. hand와 센싱 간의 단절은 contact-rich 조작에 중대한 영향을 미친다: dexterous RL에 가장 널리 사용되는 hand(LEAP Hand, CrossDex, SeqDex, HandelBot 등에서 사용)가 어떤 tactile feedback 없이 작동하여, 이 플랫폼에서 학습된 policy가 물리적 상호작용에서 힘 인식 행동을 학습할 수 없다는 것을 의미한다. ISyHand의 본질적 compliance는 부분적인 기계적 솔루션을 제공하지만, 센싱 없이 compliance는 policy에 의해 관찰 불가능하다. LEAP 수준의 커뮤니티 채택, ORCA 수준의 tactile 통합, ISyHand 수준의 compliance를 $2K 미만으로 결합한 hand는 아직 존재하지 않는다.
