# 10.3 AnyTeleop

- **전체 제목:** AnyTeleop: A General Vision-Based Dexterous Robot Hand-Arm Teleoperation System
- **저자:** Yuzhe Qin, Wei Yang, Binghao Huang, Karl Van Wyk, Hao Su, Xiaolong Wang, Dieter Fox (UCSD, NVIDIA)
- **학회/연도:** RSS 2023
- **입력 모달리티:** 단일 RGB 카메라 (비전 기반 핸드 포즈 추정)
- **대상 hand:** 다수의 dexterous hand (모듈식 retargeting을 통해 Allegro, Shadow 등)
- **Force feedback:** 없음
- **비용:** 매우 저렴 (웹캠만 필요)

## 핵심 방법론/설계

AnyTeleop은 단일 RGB 카메라에서의 비전 기반 핸드 포즈 추정을 사용하여 dexterous 로봇 hand를 구동한다. 시스템은 핸드 포즈 추정과 로봇별 retargeting을 분리하여, 감지된 인간 핸드 포즈를 지원되는 모든 로봇 hand에 매핑하는 모듈식 retargeting 모듈을 사용한다. 이 설계는 하드웨어별 센서나 글러브 없이 다양한 hand 플랫폼에 걸쳐 원격조작이 가능하다. 비전 전용 접근법은 셋업 비용과 복잡성을 최소화한다.

## 주요 기여

- 착용 센서, 글러브, VR 하드웨어가 필요 없는 카메라 전용 원격조작
- 단일 입력 파이프라인으로 다수의 로봇 hand 플랫폼을 지원하는 모듈식 retargeting 아키텍처
- dexterous 원격조작을 위한 최저 비용 진입점 (웹캠만 해당)

## 한계점

- 비전 기반 핸드 트래킹이 센서 기반 접근법보다 덜 정확, 특히 가려진 또는 빠르게 움직이는 손가락에 대해
- force feedback이 없어 운영자에게 contact-rich 작업이 어려움
- 단일 카메라 셋업이 깊이 인식을 제한하고 트래킹 jitter를 유발할 수 있음
- 비전 처리 파이프라인의 지연이 실시간 제어 품질에 영향

## 데이터 품질 영향

시연에 힘 정보가 부족하고 센서 기반 시스템보다 위치 정확도가 낮아, 힘 조절이 부족한 policy를 생성한다. 단일 카메라 트래킹이 빠른 손가락 동작이나 가림 시 jitter와 간헐적 트래킹 손실을 유발하며, 이는 시연 궤적의 노이즈로 나타난다. 이 데이터로 학습된 policy는 force blindness와 위치 노이즈를 모두 물려받아, 부정확한 손가락 배치와 학습된 접촉력 조절 부재를 초래한다. 제어된 접촉(예: 삽입, 피봇팅, 표면 추종)을 요구하는 작업에서 AnyTeleop 시연은 필요한 힘-위치 협응을 학습하기에 불충분하다.

## 오픈소스 현황

프로젝트 페이지 이용 가능. 코드 부분 공개.
