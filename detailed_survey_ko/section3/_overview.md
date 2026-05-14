# Section 3: 힘 인식 VLA / 촉각 VLA -- 개요

> 접촉이 풍부한 작업을 위해 힘/토크 또는 촉각 센싱을 통합하는 모델. 이 섹션은 힘/촉각 모달리티와 함께 VLM/VLA 백본이나 언어 조건부를 사용하는 시스템을 다룬다. VLM 백본 없는 힘/임피던스 중심 시스템은 Section 5에 수록.

## 이 섹션의 논문

| # | 논문 | 힘/촉각 입력 | 힘 출력 | 로봇 | VLA? |
|---|-------|---------------------|--------------|-------|------|
| 3.1 | [ForceVLA](forcevla.md) | 6축 F/T | 아니오 (위치 전용) | Flexiv Rizon 4 | 예 |
| 3.2 | [ForceVLA2](forcevla2.md) | 6축 F/T (300 Hz) | 예 (전체 렌치) | Flexiv Rizon 4s | 예 |
| 3.3 | [FD-VLA](fd_vla.md) | 증류된 F/T | 아니오 (위치 전용) | UR5e | 예 |
| 3.4 | [FAVLA](favla.md) | 이중 6축 F/T | 아니오 (위치 전용) | Monte 양팔 (X-ARM) | 예 |
| 3.5 | [HapticVLA](hapticvla.md) | 증류된 촉각 | 아니오 (위치 전용) | LeRobot SO-101 | 예 |
| 3.6 | [DreamTacVLA](dreamtacvla.md) | 비전 기반 촉각 (V-JEPA2) | 아니오 (위치 전용) | Dobot Xtrainer | 예 |
| 3.7 | [OmniVTLA](omnivtla.md) | 비전 기반 + 힘 기반 촉각 | 아니오 (위치 전용) | 그리퍼 + 정교한 핸드 | 예 |
| 3.8 | [Tactile-VLA](tactile_vla.md) | 촉각 센서 | 예 (부분: 하이브리드 위치-힘) | 미명시 | 예 |
| 3.9 | [TaF-VLA](taf_vla.md) | GelSight + 6축 F/T | 아니오 (위치 전용) | Franka FR3 | 예 |
| 3.10 | [TA-VLA](ta_vla.md) | 관절 토크 (모터 전류) | 보조 토크 예측 | Cobot Magic ALOHA | 예 |
| 3.11 | [CRAFT](craft.md) | 힘 센싱 | 아니오 (위치 전용) | Franka Panda | 예 |
| 3.12 | [VLA-Touch](vla_touch.md) | GelSight 촉각 | 아니오 (잔차 보정) | 팔 + 그리퍼 + GelSight | 예 |
| 3.13 | [FoAR](foar.md) | 6축 F/T | 아니오 (위치 전용) | Flexiv Rizon | 아니오 |
| 3.14 | [FACTR](factr.md) | 관절 토크 (모터 전류) | 아니오 (위치 전용) | Franka Panda | 예 |
| 3.15 | [ForceMimic](forcemimic.md) | 캡처된 상호작용 렌치 | 예 (전체 렌치) | Flexiv Rizon | 아니오 |
| 3.16 | [Reactive Diffusion Policy](reactive_diffusion_policy.md) | GelSight Mini 촉각 | 아니오 (위치 전용, 임피던스 유사) | Flexiv Rizon 4 | 예 |
| 3.17 | [ACP](acp.md) | 6축 F/T (ATI) | 예 (부분: 스칼라 강성) | UR5e | 아니오 |
| 3.18 | [TacDiffusion](tacdiffusion.md) | 촉각 센서 | 예 (전체 렌치: 6D) | 그리퍼 + 촉각 | 예 |
| 3.19 | [FARM](farm.md) | GelSight Mini 촉각 | 예 (부분: 파지 힘) | 변형 UMI 그리퍼 | 예 |
| 3.20 | [T-DEX](tdex.md) | DIGIT 비전 기반 촉각 | 아니오 (위치 전용) | Allegro Hand (16 DoF) + Kinova Jaco | 아니오 |

## 교차 관찰 사항

### 1. 입력 모달리티 vs. 출력 모달리티 비대칭

20편 논문 전체에서 나타나는 두드러진 패턴은 힘/촉각 입력과 힘 출력 사이의 비대칭이다. 20편 모두 힘 또는 촉각 정보를 입력으로 사용하지만, 6편만이 어떤 형태의 힘/임피던스 출력을 생성한다. 나머지 14편은 힘/촉각을 위치 전용 행동 생성을 개선하기 위한 입력으로만 사용한다. 이는 커뮤니티가 힘 인식 조작의 "센싱" 측면은 대체로 다루었으나 "구동" 측면 -- 능동적으로 힘을 명령하는 것 -- 은 아직 미개발 상태임을 시사한다.

**힘 출력 세분화:**
- **전체 렌치 출력 (6D 힘 + 토크):** ForceVLA2, ForceMimic, TacDiffusion
- **부분 힘 출력:** Tactile-VLA (하이브리드 위치-힘), FARM (파지 힘만), ACP (스칼라 강성만)

### 2. 센서 유형 파편화

논문들은 광범위한 힘/촉각 센서 유형을 포괄한다: 6축 F/T 센서(ForceVLA, ForceVLA2, FAVLA, TaF-VLA, FoAR, ACP), GelSight 비전 기반 촉각(TaF-VLA, VLA-Touch, Reactive Diffusion Policy, FARM), DIGIT 스타일 촉각, 모터 전류에서의 관절 토크(TA-VLA, FACTR), 증류/가상 힘(FD-VLA, HapticVLA). 어떤 힘/촉각 모달리티가 가장 잘 작동하는지에 대한 표준화가 없으며, 센서 유형 간 비교를 수행하는 논문은 극소수이다. TaF-VLA가 두 힘 모달리티(GelSight + F/T)를 융합하는 유일한 논문이나, 다른 센서 조합을 사용하는 논문과 비교하지 않는다.

### 3. 증류 추세

3편의 논문(FD-VLA, HapticVLA, 그리고 보조 토크 예측을 통한 TA-VLA 부분적)이 훈련 중 힘/촉각 데이터를 사용하되 추론 시 센서 없이 작동하는 것을 탐구한다. 이 "힘 증류" 패러다임은 저비용 로봇에 힘 인식 정책을 배포하는 실용적 경로를 제공하나, 근본적으로 시스템을 접촉에 대한 시각적 추론으로 제한한다 -- 힘/촉각 센싱으로만 관측 가능한 진정으로 예기치 않은 접촉 이벤트에 반응할 수 없다.

### 4. 작업 평가가 여전히 좁음

20편에 걸쳐 있음에도, 작업 레퍼토리는 삽입 작업(플러그, USB, 충전기, 커넥터), 닦기/청소, 벗기기에 의해 지배된다. 소수의 논문만이 더 다양한 작업에서 평가한다: TA-VLA (10개 작업), TaF-VLA (8개 작업), ForceVLA/ForceVLA2 (각 5개 작업). 논문 간 사용되는 접촉이 풍부한 작업 벤치마크가 표준화되지 않아 직접 비교가 어렵다.

### 5. 정교한 핸드 격차

T-DEX가 비자명한 접촉이 풍부한 작업으로 정교한 핸드(Allegro)에서 힘/촉각 조작을 평가하는 유일한 논문이다. 그러나 T-DEX는 언어 조건부 없는 비파라메트릭 최근접 이웃 정책을 사용한다 -- VLA가 아니다. 단순 집기-놓기(OmniVTLA)를 넘어 접촉이 풍부한 작업에 대해 다지 정교한 핸드에서 평가된 언어 조건부 VLA는 없다.

### 6. 시간 스케일 도전

힘과 촉각 신호는 일반적 VLA 추론 속도(5-20 Hz)보다 훨씬 높은 주파수(100-1000 Hz)에서 작동한다. 논문들은 이 불일치를 다르게 다룬다: ForceVLA2는 300 Hz F/T 데이터에 시간 합성곱을 사용, Reactive Diffusion Policy는 저속-고속 이중 아키텍처를 사용, FACTR는 커리큘럼 훈련과 함께 힘 어텐딩 변환기 레이어를 사용, 대부분은 힘 신호를 VLA 속도에 맞춰 다운샘플링한다. 이러한 시간 스케일을 연결하는 최적 접근법은 미해결 문제이다.

### 7. 재현성이 크게 다름

20편 중 ~10편이 코드를 공개한다: ForceVLA, FoAR, FACTR, ForceMimic, Reactive Diffusion Policy, VLA-Touch, TacDiffusion, DreamTacVLA, T-DEX, FARM. 이 중 Reactive Diffusion Policy와 VLA-Touch만이 코드와 모델 체크포인트를 모두 공개한다. 나머지 ~10편은 공개 코드가 없어 재현성과 후속 연구를 제한한다.

ForceVLA에 대한 참고: 공개 배포는 주로 HuggingFace의 ForceVLA-Data 데이터셋(244개 궤적)이다. 모델 코드(데이터만이 아닌)의 공개 여부는 독립적으로 검증해야 한다.

### 8. 로봇 플랫폼 집중

Flexiv Rizon 플랫폼이 20편 중 5편(ForceVLA, ForceVLA2, FoAR, ForceMimic, Reactive Diffusion Policy)에 등장하며, 내장 6축 F/T 센싱과 유연성 제어 능력을 반영한다. Franka Panda/FR3가 3편(TaF-VLA, FACTR, CRAFT)에 등장한다. 소수 플랫폼에의 집중은 힘 인식 VLA 접근법의 교차 플랫폼 일반화에 대한 근거를 제한한다.

### 9. 더 넓은 VLA 환경에서 힘 인식 VLA의 위치

Section 3을 Section 6의 VLA 기반 모델과 비교하면, 주요 VLA 패밀리(pi0, GR00T N1, OpenVLA, Octo, RDT-1B) 중 어느 것도 힘/촉각 입력이나 힘 출력을 포함하지 않는다. 힘 인식 VLA는 이러한 기반 모델에 통합되기보다는, 이에 기반하거나 영감을 받아 구축된 특수 틈새로 남아있다. 이는 접촉이 풍부한 작업에서의 중요성에도 불구하고 힘/촉각 모달리티가 아직 VLA 사전 훈련에 필수적으로 간주되지 않음을 시사한다.

### 10. 반응적에서 예측적 힘 추론으로

대부분의 논문은 힘/촉각 입력을 반응적으로 사용한다 -- 현재 접촉 상태에 기반하여 행동을 조정. DreamTacVLA가 주목할 만한 예외로, 미래 접촉 상태를 예측하고 이 예측을 사용하여 행동을 사전에 조정하는 촉각 세계 모델을 도입한다. 이 예측적 접근법은 예기적 힘 제어(예: 예상 충격 전 파지 힘 조정)에 유망하나, 이 단일 논문 이후로 대체로 미탐구 상태이다.
