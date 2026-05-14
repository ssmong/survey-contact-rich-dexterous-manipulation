# 10.2 BunnyVisionPro

- **전체 제목:** BunnyVisionPro: Real-Time Bimanual Dexterous Teleoperation for Imitation Learning
- **저자:** Runyu Ding, Yuzhe Qin, Jiyue Zhu, Chengzhe Jia, Xiaolong Wang (HKU, UCSD)
- **학회/연도:** arXiv 2407.03162, 2024년 7월
- **입력 모달리티:** Apple Vision Pro 핸드 트래킹 (마커리스, 내장 카메라)
- **대상 hand:** 양팔 dexterous 셋업 (양팔 + dexterous hand)
- **Force feedback:** 저비용 haptic feedback 모듈 (선택 사항)
- **비용:** ~$3,500+ (Apple Vision Pro 하드웨어 비용)

## 핵심 방법론/설계

BunnyVisionPro는 Apple Vision Pro의 내장 핸드 트래킹을 실시간 양팔 dexterous 원격조작에 재활용한다. 시스템은 Vision Pro 헤드셋의 핸드 포즈 데이터를 로컬 네트워크를 통해 로봇 컨트롤러로 스트리밍하며, 실시간 inverse kinematics로 인간 핸드 포즈를 로봇 관절 명령에 매핑한다. 선택적 저비용 haptic feedback 모듈이 운영자에게 기본적인 접촉 피드백을 제공한다. VR 헤드셋의 고품질 핸드 트래킹으로 글러브나 외부 센서의 필요성이 제거된다.

## 주요 기여

- 소비자 VR 하드웨어 (Apple Vision Pro)를 연구급 양팔 dexterous 원격조작에 활용
- 로컬 네트워크를 통한 저지연 핸드 포즈 전송의 실시간 스트리밍 파이프라인
- 개선된 contact-rich 작업 수행을 위한 선택적 haptic feedback 통합
- 수집된 시연에서의 imitation learning 입증

## 한계점

- 높은 하드웨어 비용 (Vision Pro만 $3,500)이 접근성 제한
- 핸드 트래킹 정확도가 조명 조건 및 헤드셋 카메라에 대한 손의 가시성에 의존
- haptic feedback이 전용 force feedback 글러브에 비해 초보적
- Vision Pro의 손가락 수준 트래킹 해상도가 정밀한 미세 운동 작업에 불충분할 수 있음

## 데이터 품질 영향

선택적 haptic 모듈은 초보적인 이진 접촉 피드백을 제공하지만, 힘의 크기나 방향 정보가 부족하다. haptic 모듈 없이 수집된 시연은 순수 위치 기반으로, 카메라 전용 시스템과 동일한 force-blind 데이터 품질 문제를 생성한다. haptic 모듈이 활성화된 경우에도 조잡한 접촉 신호로 인해 운영자가 grasp force를 정밀하게 조절할 수 없어, 섬세한 조작 작업(예: 깨지기 쉬운 객체 다루기, 제어된 sliding)에 필요한 힘 프로파일 없이 대략적인 손가락 궤적을 인코딩하는 시연이 생성된다.

## 오픈소스 현황

오픈소스. GitHub: [Dingry/BunnyVisionPro](https://github.com/Dingry/BunnyVisionPro)
