# 10.10 HATO

- **전체 제목:** Learning Visuotactile Skills with Two Multifingered Hands
- **저자:** Toru Lin, Yu Zhang, Qiyang Li, Haozhi Qi, Brent Yi, Sergey Levine, Jitendra Malik (UC Berkeley)
- **학회/연도:** ICRA 2024 (arXiv 2404.16823, 2024년 4월)
- **arXiv:** https://arxiv.org/abs/2404.16823
- **입력 모달리티:** Meta Quest 2 VR 컨트롤러 (팔 포즈 트래킹) + 그립 버튼/엄지스틱 (손가락 제어)
- **대상 hand:** 2x Psyonic Ability Hand (각 6 DoF, 내장 터치 센서를 갖춘 용도 변경된 의수 hand)
- **Force feedback:** 운영자에게 없음 (그러나 로봇 hand의 터치 센서가 학습된 policy에 tactile 입력 제공)
- **비용:** 저비용 (시판 VR 하드웨어 + 의수 hand)

## 핵심 방법론/설계

HATO는 시판 VR 전자장치(Meta Quest 2)와 손가락 끝 터치 센서가 장착된 용도 변경된 의수 hand(Psyonic Ability Hand)로 구축된 양팔 dexterous 원격조작 시스템이다. 시스템은 각각 하나의 Ability Hand를 장착한 두 대의 UR5e 팔을 사용한다. 팔 제어는 VR 컨트롤러 포즈를 IK를 통해 end-effector 위치에 매핑한다. 손가락 제어는 비엄지 굴곡(4 DoF)에 그립 버튼을, 엄지 굴곡/외전(hand당 2 DoF)에 엄지스틱을 사용한다. 시스템은 10 Hz로 visuotactile 시연을 수집하며, RGB-D 이미지(3대 카메라: wrist 장착 2대 + head-view 1대), proprioception, 터치 센서 판독값을 캡처한다.

Policy는 diffusion policy 프레임워크를 따르는 Denoising Diffusion Probabilistic Models (DDPM)를 사용하여 학습된다. 단일 관측이 16-step action sequence를 예측한다. 각 모달리티는 별도로 인코딩된다: RGB-D에 ResNet-18 (GroupNorm 적용), proprioception과 터치 신호에 2-layer MLP. 모든 인코딩된 특징이 연결되어 24차원 action(팔당 6 DoF + hand당 6 DoF)을 출력하는 diffusion model의 입력이 된다. 추론은 motion smoothing을 위한 temporal ensemble을 사용한다.

## 주요 기여

- 시판 VR 하드웨어와 의수 hand를 사용한 저비용 양팔 dexterous 원격조작 시스템 (hand당 ~$600 vs. 연구용 hand $10K+)
- 양팔 multi-finger hand에서 visuotactile policy 학습의 최초 시연 중 하나로, 센싱 모달리티의 체계적 ablation 포함
- 터치 센싱이 contact-rich 양팔 작업에 핵심적임을 입증 (터치 제거 시 Steak Serving이 5/10에서 0/10으로 감소)
- 데이터셋 포화 분석: 75-200개 시연이 작업 전반에 걸쳐 효과적 학습에 충분

## 한계점

- 의수 Ability Hand는 hand당 6 DoF만 보유(underactuated), Shadow(24) 또는 Allegro(16)보다 dexterity가 현저히 낮음
- VR 컨트롤러 기반 손가락 매핑이 조잡: 그립 버튼이 4개 손가락을 동시에 제어하여 독립적 손가락 제어 제한
- 원격조작 중 운영자에게 force/haptic feedback 없어 contact-rich 작업 품질 제한
- 터치 센서가 DIGIT 또는 GelSight 같은 고해상도 tactile이 아닌 이진/저해상도 접촉 신호 제공 (손가락 끝당 6개)
- 4개 작업에서만 평가; in-hand 조작 또는 정밀 조립 작업 없음

## 데이터 품질 영향

Ability Hand의 내장 터치 센서가 원격조작 중 기록되어 학습된 policy의 입력으로 사용되는 손가락 끝 접촉 정보를 제공한다. 그러나 운영자는 haptic feedback을 받지 못하므로, 데이터 수집 중 힘 조절은 전적으로 시각적 단서에 의존한다. 터치 신호는 비전 기반 tactile 센서(DIGIT, GelSight)에 비해 저해상도로, 공간적으로 분해된 압력 맵이 아닌 조잡한 접촉/비접촉 정보를 제공한다. 이러한 한계에도 불구하고, ablation은 터치 데이터 포함이 접촉 민감 작업에서 policy 성공률을 의미 있게 향상시킴을 보여준다.

## 정량적 결과

| 작업 | 성공 (전체) | Pickup | 사용 시연 수 |
|------|------------|--------|-------------|
| Slippery Handover | 10/10 | 10/10 | 75 |
| Tower Block Stacking | 10/10 | 10/10 | 75 |
| Wine Pouring | 9/10 | 10/10 | 100 |
| Steak Serving | 5/10 | 10/10 | 200 |

**Ablation 결과 (Steak Serving):**
- 전체 모델 (vision + touch + proprio): 5/10
- 터치 제거: 0/10
- 비전 제거: 0/10
- wrist 카메라 제거: 2/10
- 깊이는 학습을 눈에 띄게 향상시키지 않음

## 오픈소스 현황

오픈소스 (하드웨어 + 소프트웨어 + 데이터셋). 프로젝트 페이지: https://toruowo.github.io/hato/
