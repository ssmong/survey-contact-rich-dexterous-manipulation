# Section 1: 정교한 도구 사용 및 조작 (Dexterous Tool Use & Manipulation)

이 섹션에서는 병렬 조 그리퍼를 넘어 파지, 도구 사용 또는 물체 조작을 수행하는 다지 핸드 시스템에 대한 최신 연구를 조사한다. 각 논문은 방법론, 하드웨어, 평가 및 기여에 대해 상세히 리뷰된다.

**이 섹션의 논문:**
- [SimToolReal](simtoolreal.md) -- 24가지 정교한 도구 사용 작업을 위한 Sim-to-real 파이프라인 (Sharpa Hand, 22 DoF)
- [Grasp-to-Act](grasp_to_act.md) -- 동적 도구 사용을 위한 파지-행동 분해 (Allegro Hand, 16 DoF)
- [DexMachina](dexmachina.md) -- 인간 비디오에서 다중 구현체 정교한 정책으로 (4종 로봇 핸드)
- [ManipTrans](maniptrans.md) -- 구현체 간 조작 전이 (6종 로봇 핸드, CVPR 2025)
- [SPIDER](spider.md) -- 9개 휴머노이드 플랫폼 간 구현체 리타게팅 (Meta FAIR)
- [Scaffolding+VLM](scaffolding_vlm.md) -- VLM 기반 시연 생성 스캐폴딩 (Allegro Hand, NeurIPS 2025)
- [DexUMI](dexumi.md) -- 실세계 전용 정교한 데이터 수집 인터페이스 (CoRL 2025 Best Paper Finalist)
- [DexterityGen](dexteritygen.md) -- 도구 사용을 위한 기반 컨트롤러, 3가지 도구 시연 (Allegro Hand, RSS 2025)
- [ArtiGrasp](artigrasp.md) -- 양손 파지 및 관절 물체 조작 합성 (MANO 핸드, 3DV 2024)
- [DexDeform](dexdeform.md) -- 미분 가능 물리 기반 변형 가능 물체 조작 (ICLR 2023)

---

## 교차 관찰 사항

이 섹션의 10편의 논문에서 여러 패턴이 나타난다:

**위치 제어가 지배적이며 힘 인식은 부재.** 10편의 논문 중 어느 것도 정교한 핸드에 대한 명시적 힘/토크 센싱이나 임피던스 제어를 포함하지 않는다. 모든 시스템은 관절 위치 또는 각도 목표를 출력한다. 많은 작업(해머링, 톱질, 변형 가능 물체 조작)이 본질적으로 상당한 접촉 힘을 수반하기 때문에 이는 주목할 만하다. 이 분야는 시뮬레이션 접촉 모델이나 하드웨어 유연성에 의존하여 힘을 암묵적으로 처리한다.

**교차 구현체 평가가 증가하는 추세.** 여러 논문이 다양한 핸드 플랫폼에서 평가한다: ManipTrans (6종 핸드), SPIDER (9종 구현체), DexMachina (4종 핸드), DexUMI (2종 핸드). 이는 단일 하드웨어 플랫폼에 종속되지 않는 범용 정교한 조작 방법을 향한 커뮤니티의 움직임을 반영한다. Allegro Hand (16 DoF)는 10편 중 5편에서 평가 플랫폼으로 등장하여 사실상의 표준이 되었다.

**Sim-to-real이 여전히 주요 패러다임이나 주목할 만한 예외가 존재.** SimToolReal, Grasp-to-Act, Scaffolding+VLM, DexterityGen이 sim-to-real 전이를 시연한다. DexUMI는 반대로 실세계 전용 접근법(CoRL Best Paper Finalist)을 취하며, 두 패러다임 모두 가치가 있음을 시사한다. 5편의 논문(DexMachina, ManipTrans, SPIDER, ArtiGrasp, DexDeform)은 시뮬레이션 전용으로 남아있다.

**인간 시연이 출발점.** 대부분의 접근법은 인간 시연을 초기화로 사용한다 -- 비디오(DexMachina), 모션 캡처(SPIDER, ManipTrans), 원격 조작(DexUMI, Grasp-to-Act), 또는 VLM 생성 프록시(Scaffolding+VLM)에서. SimToolReal과 DexterityGen만이 인간 시연 데이터 없이 순수 RL 보상 엔지니어링에 의존하며, 이는 상당한 작업별 엔지니어링 비용을 수반한다.

**VLM/언어 통합은 최소화.** Scaffolding+VLM만이 비전-언어 모델(Gemini 2.5 Flash)을 통합하며, 정책 백본이 아닌 시연 생성 스캐폴딩으로 VLM을 사용한다. 이 섹션의 어떤 논문도 정교한 제어를 위해 VLA 아키텍처를 사용하지 않는다. 이는 그리퍼 기반 VLA 문헌(서베이 Section 2)과 현저히 대조되며, 기반 모델 능력과 정교한 핸드 제어 사이의 격차를 부각시킨다.

**변형 가능 및 관절 물체가 작업 영역을 확장.** DexDeform(변형 가능 물체)과 ArtiGrasp(관절 물체)은 강체 파지 및 도구 사용을 넘어 내부 자유도를 가진 물체 범주를 다룬다. 이러한 연구는 시뮬레이션 전용으로 남아있으며, sim-to-real 전이를 위한 복잡한 물체 물리 모델링의 추가적 도전을 반영한다.

**IsaacGym이 지배적인 시뮬레이션 플랫폼으로** sim-to-real 전이를 시연하는 논문(SimToolReal, DexterityGen, ManipTrans)에서 사용되며, 대안 플랫폼은 특수 목적으로 사용된다: 교차 구현체 리타게팅을 위한 Genesis(DexMachina), 접촉이 풍부한 양손 작업을 위한 RaiSim(ArtiGrasp), 미분 가능 변형 물리를 위한 PlasticineLab(DexDeform), 그리고 광범위한 구현체 지원을 위한 MuJoCo(SPIDER).
