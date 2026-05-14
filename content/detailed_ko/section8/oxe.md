# 8.4.1 Open X-Embodiment (OXE)

- **전체 제목:** Open X-Embodiment: Robotic Learning Datasets and RT-X Models
- **저자:** 21개 기관의 294명 이상 (Google DeepMind, UC Berkeley, Stanford, CMU, MIT 등); 주요 기여자: Sergey Levine, Pieter Abbeel, Chelsea Finn, Jitendra Malik
- **학회/연도:** arXiv 2023 (2023년 10월 제출; 2025년 5월 최종 개정); ICRA 2024 관련
- **규모:** ~100만 로봇 에피소드, 22개 로봇 embodiment, 527개 skill, 160K+ 작업
- **핸드/embodiment 유형:** 22개 로봇 플랫폼 (단일 팔, 양팔, 모바일 manipulator 포함; 주로 parallel-jaw gripper; 전용 multi-finger dexterous hand 데이터 없음)
- **데이터 형식:** TensorFlow Datasets를 통한 표준화된 RLDS (Reinforcement Learning Datasets) 형식
- **수집 방법:** 전 세계 21개 연구실의 기존 및 신규 수집 데이터셋을 다기관 협력으로 통합

## 핵심 방법론/설계

OXE는 21개 기관의 데이터를 통합 형식으로 집약한 최초의 대규모 cross-embodiment 로봇 조작 데이터셋이다. 핵심 논제는 서로 다른 형태, 센서, 작업에 걸친 다양한 로봇 데이터를 풀링하면 대규모 범용 policy 학습 시 positive transfer가 가능하다는 것이다. 데이터셋은 RT-X 모델 (RT-1-X, RT-2-X)과 함께 제공되며, 전체 혼합 데이터로 학습된 단일 policy가 개별 기관 데이터만으로 학습된 policy보다 우수한 성능을 보임을 입증한다. 표준화된 RLDS 형식에는 관측 (이미지, proprioception), 행동 (end-effector 또는 관절), 언어 지시, 에피소드 메타데이터가 포함된다.

## 주요 기여

- 출시 당시 최대 규모의 cross-embodiment 로봇 조작 데이터셋 (~100만 에피소드, 22개 로봇)
- positive transfer 입증: 전체 혼합 데이터로 학습된 RT-2-X가 전문가 모델 대비 평균 50% 이상 성능 향상
- cross-embodiment 로봇 데이터의 사실상 표준 형식으로 RLDS 확립
- OpenVLA, Octo, RDT-1B, HPT, CrossFormer 등 후속 범용 policy의 기반 사전학습 데이터셋

## 서베이 대상 연구에서의 활용

OXE는 본 서베이에서 다루는 여러 시스템의 주요 사전학습 데이터셋이다:
- **OpenVLA** (§6): OXE 혼합 데이터로 사전학습
- **Octo** (§6): OXE로 사전학습; OXE는 Octo와 함께 설계됨
- **RDT-1B** (§6): 대규모 사전학습에 OXE 사용
- **HPT** (§6): OXE로 cross-embodiment 사전학습
- **CrossFormer** (§6): OXE 규모의 cross-embodiment 데이터를 위해 특별 설계

## 한계점

- multi-finger dexterous hand 데이터 없음: 모든 embodiment가 parallel-jaw gripper 또는 단순 end-effector를 사용하여, 추가 데이터 없이 dexterous 조작 policy 사전학습에 부적합
- force/torque 또는 tactile 데이터 없음: 관측은 이미지와 proprioception으로 제한
- embodiment 간 심각한 클래스 불균형: 일부 로봇이 다른 로봇보다 몇 배 더 많은 데이터 기여
- 품질 편차: 각 기관의 데이터가 서로 다른 수집 프로토콜, 주석 품질, 작업 정의 사용
- 장면/환경 다양성을 구체적으로 목표로 하는 DROID 같은 데이터셋에 비해 개별 embodiment 내 실제 환경 다양성 제한
- 행동 공간 이질성으로 인해 신중한 정규화 또는 embodiment별 action head 필요
- impedance/compliance 제어 데이터 또는 접촉 이벤트 주석 없음, contact-rich policy 학습에 대한 활용 제한

## 공개 현황

CC BY 4.0 오픈소스. TensorFlow Datasets 및 [Open X-Embodiment 프로젝트 페이지](https://robotics-transformer-x.github.io/)에서 이용 가능. 개별 구성 데이터셋은 다양한 라이선스 적용.
