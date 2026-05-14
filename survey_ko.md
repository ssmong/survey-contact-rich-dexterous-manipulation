# 접촉 풍부 다지 조작: 종합 서베이

> 최종 업데이트: 2026-05-14
> 범위: 다지 조작, 힘 인식 VLA, 임피던스 학습, RL 정책 및 관련 벤치마크에 관한 논문, 리포지토리, 데이터셋 (2018-2026).
> GitHub 링크 및 가중치 가용 여부는 서베이 작성일 기준으로 확인되었으며, 이후 변경될 수 있음.
>
> **표기법:** ✅ = 사용 가능/지원됨, ✗ = 사용 불가/미지원, — = 보고되지 않음 또는 해당 없음.

**목적.** 본 서베이는 세 가지 연구 흐름의 교차점을 중심으로 구성됨: (1) 다지 다중 손가락 조작, (2) 비전-언어-행동(VLA) 모델, (3) 힘/임피던스 인식 제어. 기존 시스템이 어떤 능력을 제공하는지, 그리고 어떤 조합이 아직 탐구되지 않았는지를 매핑하여 이러한 교차점에서의 미개척 연구 방향을 식별하는 것을 목표로 함. 범위는 이 세 영역에 의도적으로 집중되어 있으며, 보행, 이동 조작, 산업 자동화 등 인접 주제는 서베이의 핵심 주제와 교차하는 경우에만 다룸.

---

## 1. 다지 도구 사용 및 조작

평행 조 그리퍼를 넘어 파지, 도구 사용, 또는 객체 조작을 수행하는 다중 손가락 핸드 시스템.

| 논문 | 연구 그룹 | 학회 | 연도 | 핸드 (자유도) | 작업 | 시뮬레이션 플랫폼 | Sim2Real | 코드 | 가중치 | VLA/언어 |
|---|---|---|---|---|---|---|---|---|---|---|
| [**SimToolReal**](https://arxiv.org/abs/2602.16863) | Stanford IPRL | arXiv | 2026 | Sharpa (22) + KUKA | 24가지 도구 사용 작업 (해머, 드라이버, 주걱) | IsaacGym | Yes | [GitHub](https://github.com/tylerlum/simtoolreal) ✅ | ✅ ckpt | ✗ |
| [**Grasp-to-Act**](https://arxiv.org/abs/2602.20466) | UIUC RoboTouch | arXiv | 2026 | LEAP (16) | 5가지 동적 도구 사용 (해머, 톱, 자르기, 젓기, 뜨기) | Sim + real | Yes | ✗ | ✗ | ✗ |
| [**DexMachina**](https://arxiv.org/abs/2505.24853) | Stanford/NVIDIA | arXiv | 2025 | Inspire, Allegro, Xhand, Schunk | 양손 관절 객체 조작 | Genesis | ✗ | [GitHub](https://github.com/MandiZhao/dexmachina) ✅ | ✗ (eval TODO) | ✗ |
| [**ManipTrans**](https://arxiv.org/abs/2503.21860) | BIGAI/Tsinghua/PKU | CVPR | 2025 | 4종 핸드 (Shadow, MANO, Inspire, Allegro) | 양손 작업 (펜 캡, 병뚜껑 열기) | IsaacGym P4 | ✗ | [GitHub](https://github.com/ManipTrans/ManipTrans) ✅ | ✅ imitator ckpt + HF | ✗ |
| [**SPIDER**](https://arxiv.org/abs/2511.09484) | Meta FAIR / Berkeley | arXiv | 2025 | 9종 휴머노이드 | 리타겟팅된 인간 시연 | MuJoCo | ✅ (Franka+Allegro) | [GitHub](https://github.com/facebookresearch/spider) ✅ | ✗ | ✗ |
| **Scaffolding+VLM** | Stanford / KIT | NeurIPS | 2025 | Allegro (16) + KUKA | 관절 객체 (사과, 병, 서랍) | Sim + real | Yes | [GitHub](https://github.com/vdebakker/vlm-scaffolding) ✅ | ✗ | ✅ Gemini VLM |
| [**DexUMI**](https://arxiv.org/abs/2505.21864) | Stanford | CoRL Best Paper Finalist | 2025 | XHand, Inspire | 실세계 다지 조작 | Real only | N/A | [GitHub](https://github.com/real-stanford/DexUMI) ✅ | ✗ | ✗ |
| [**DexterityGen**](https://arxiv.org/abs/2502.04307) | Berkeley/Meta | RSS | 2025 | Allegro (16) + arm | 도구 사용 (펜, 드라이버, 주사기) | IsaacGym | ✅ | ✗ | ✗ | ✗ |
| [**ArtiGrasp**](https://arxiv.org/abs/2309.03891) | ETH Zurich | 3DV | 2024 | MANO (인간 프록시) | 양손 파지 + 관절 조작 (8개 객체) | RaiSim | ✗ | [GitHub](https://github.com/zdchan/artigrasp) ✅ | ✅ pretrained | ✗ |
| [**DexDeform**](https://arxiv.org/abs/2304.03223) | MIT-IBM | ICLR | 2023 | Multi-finger (sim) | 6가지 변형 가능 객체 작업 (점토) | PlasticineLab | ✗ | [GitHub](https://github.com/sizhe-li/DexDeform) ✅ | ✗ | ✗ |

---

## 2. 다지 VLA / 비전-언어-행동

다지 핸드 지원 또는 언어 조건부 다지 조작을 갖춘 VLA 모델.

| 논문 | 연구 그룹 | 학회 | 연도 | 핸드 (자유도) | 작업 | 코드 | 가중치 | 핵심 방법 |
|---|---|---|---|---|---|---|---|---|
| [**UniDex-VLA**](https://arxiv.org/abs/2603.22264) | UniDex-AI | CVPR | 2026 | FAAS를 통한 8종 핸드 (Allegro, LEAP, Shadow, Inspire, Wuji, Oymotion, Ability, Xhand) | 도구 사용, 81% 작업 진행률 | [GitHub](https://github.com/unidex-ai/UniDex) ✅ | ✅ 3-epoch + 32-epoch on HF | 3D VLA + flow matching, FAAS 통합 행동 |
| [**DexGraspVLA**](https://arxiv.org/abs/2502.08142) | Psi-Robot | AAAI | 2026 | Custom dexterous | 복잡 환경 파지, 90%+ 성공률 | [GitHub](https://github.com/Psi-Robot/DexGraspVLA) ✅ | ✅ controller ckpt (GDrive) | Qwen2.5-VL-72B 플래너 + diffusion 컨트롤러 |
| [**DexVLA**](https://arxiv.org/abs/2502.05855) | Multi-inst. | CoRL | 2025 | Yes (커리큘럼) | 다지 스킬 학습 | [GitHub](https://github.com/juruobenruo/DexVLA) ✅ | ✅ ScaleDP-H/L on HF | 고정 VLM 위 1B diffusion expert 플러그인 |
| **Dexora** | Multi-inst. | ICRA | 2025 | 양손 36-DoF | 픽앤플레이스, 다지 조작, 조립, 도구 사용 | [GitHub](https://github.com/ZZongzheng0918/Dexora) ✅ | ✅ real data on HF | 12.2K 실제 + 100K sim 에피소드 |
| [**Grasp as You Say**](https://arxiv.org/abs/2405.19291) | Sun Yat-sen | NeurIPS | 2024 | Shadow (24) | 언어 안내 파지 ("손잡이로 머그잔 잡기") | [GitHub](https://github.com/iSEE-Laboratory/Grasp-as-You-Say) ✅ | ✗ | 언어 조건부 다지 파지 생성 |
| [**HumanoidGen**](https://arxiv.org/abs/2507.00833) | TeleHuman | NeurIPS | 2025 | Unitree H1_2 + Inspire (6 DoF/hand) | 20가지 테이블탑 작업 (양손, 장기 작업) | [GitHub](https://github.com/TeleHuman/HumanoidGen) ✅ | ✅ HF (model + data) | LLM 플래너 + MCTS + diffusion policy |
| [**VLA+Diffusion Switch**](https://arxiv.org/abs/2410.14022) | — | arXiv | 2024 | ADAPT Hand (13) | VLA 전환을 통한 픽앤플레이스 | ✗ | ✗ | 직렬 탄성 다중 손가락 핸드에서 VLA + diffusion policy 전환 |

---

## 3. 힘 인식 VLA / 촉각 VLA

접촉 풍부 작업을 위해 힘/토크 또는 촉각 센싱을 통합하는 모델. VLM/VLA 백본 또는 언어 조건부를 사용하는 시스템이 여기에 포함됨; 그렇지 않으면 VLM 백본 없는 힘/임피던스 중심 시스템은 §5에 수록.

| 논문 | 연구 그룹 | 학회 | 연도 | 힘 입력 | 힘/임피던스 출력? | 로봇 | 코드 | 가중치 | 작업 |
|---|---|---|---|---|---|---|---|---|---|
| [**ForceVLA**](https://arxiv.org/abs/2505.22159) | SJTU/Fudan | NeurIPS | 2025 | 6축 F/T | ✗ (위치만) | Flexiv Rizon + 그리퍼 | [GitHub](https://github.com/ft-robotic/ForceVLA) ✅ | ✗ (data on HF) | 플러그 삽입, 닦기, 껍질 벗기기 (5가지 작업) |
| [**ForceVLA2**](https://arxiv.org/abs/2603.15169) | Shanghai AI Lab | CVPR | 2026 | 6축 F/T 300Hz | ✅ 하이브리드 F/P + 예측 힘 | Flexiv Rizon 4s + 그리퍼 | ✗ "coming soon" | ✗ | 누르기, 청소, 기어 조립 (5가지 작업) |
| [**FD-VLA**](https://arxiv.org/abs/2602.02142) | NUS | ICRA | 2026 | 증류(추론 시 센서 없음) | ✗ | UR5e + 그리퍼 | ✗ | ✗ | 닦기, 삽입, 버튼 누르기 (3가지 작업) |
| [**FAVLA**](https://arxiv.org/abs/2602.23648) | USTC | arXiv | 2026 | 6축 F/T 고주파 | ✗ | Monte dual-arm X-ARM | ✗ | ✗ | USB 삽입, 기어, 닦기 (4가지 작업) |
| [**HapticVLA**](https://arxiv.org/abs/2603.15257) | Skoltech | arXiv | 2026 | 촉각 (증류 후 제거) | ✗ | LeRobot SO-101 + 촉각 | 논문에서 공개 예정 주장; 2026년 5월 기준 공개 리포 미확인 | 미확인 | 병/와플/달걀 픽앤플레이스 |
| [**DreamTacVLA**](https://arxiv.org/abs/2512.23864) | Northwestern | arXiv | 2025 | 촉각 (V-JEPA2) | ✗ | Dobot Xtrainer + 그리퍼 + 촉각 | [GitHub](https://github.com/michaelyeah7/learning-to-feel-the-future) (코드만) | ✗ | 촉각 월드 모델이 미래 잠재 표현 예측 → 행동 정제; 4가지 접촉 풍부 작업에서 최대 95% |
| [**OmniVTLA**](https://arxiv.org/abs/2508.08706) | - | arXiv | 2025 | 비전 기반 + 힘 기반 촉각 | ✗ | 그리퍼 + Dex Hand | ✗ (데이터셋만) | ✗ | 픽앤플레이스 (다지 핸드 100%) |
| [**Tactile-VLA**](https://arxiv.org/abs/2507.09160) | Tsinghua | arXiv | 2025 | 촉각 | ✅ 하이브리드 위치-힘 | 미지정 | ✗ | ✗ | 충전기 삽입 90% |
| [**TaF-VLA**](https://arxiv.org/abs/2601.20321) | - | arXiv | 2026 | GelSight + 6축 F/T | ✗ | Franka FR3 + 그리퍼 | ✗ | ✗ | 8가지 접촉 풍부 작업 |
| [**TA-VLA**](https://arxiv.org/abs/2509.07962) | Tsinghua AIR | CoRL | 2025 | 관절 토크 | 보조 토크 예측 | Cobot Magic ALOHA | ✗ | ✗ | 10가지 작업 (버튼, 충전기, USB...) |
| [**CRAFT**](https://arxiv.org/abs/2602.12532) | - | arXiv | 2026 | 힘 | ✗ | 원격 조작 팔 | ✗ | ✗ | 변형 가능, 정렬 작업 |
| [**VLA-Touch**](https://arxiv.org/abs/2507.17294) | NUS | arXiv | 2025 | GelSight 촉각 | ✗ (잔차 보정) | 팔 + 그리퍼 | [GitHub](https://github.com/jxbi1010/VLA-Touch) ✅ | ✅ ckpts + HF | 접촉 풍부 조작 |
| [**FoAR**](https://arxiv.org/abs/2411.15753) | SJTU | RA-L/IROS 2025 | 2024 | 6축 F/T | ✗ | Flexiv Rizon + 그리퍼 | [GitHub](https://github.com/Alan-Heoooh/FoAR) ✅ | ✗ | 닦기, 껍질 벗기기 |
| [**FACTR**](https://arxiv.org/abs/2502.17432) | CMU | RSS | 2025 | 관절 토크 (서보 전류) | ✗ | Franka + 그리퍼 | [GitHub](https://github.com/RaindragonD/factr) ✅ | ✗ (인코더만) | 상자 들기, 피벗, 반죽 밀기 |
| [**ForceMimic**](https://arxiv.org/abs/2410.07554) | SJTU | ICRA | 2024 | 캡처된 상호작용 렌치 | ✅ 렌치-위치 하이브리드 | Flexiv + 그리퍼 | [GitHub](https://github.com/ForceMimic/hybridil) ✅ | ✗ | 야채 껍질 벗기기 |
| [**Reactive Diffusion Policy**](https://arxiv.org/abs/2503.02881) | - | RSS | 2025 | GelSight Mini | ✗ (학습된 "임피던스 유사") | Flexiv Rizon 4 + 그리퍼 | [GitHub](https://github.com/xiaoxiaoxh/reactive_diffusion_policy) ✅ | ✅ ckpts + HF | 3가지 접촉 풍부 작업 |
| [**ACP**](https://arxiv.org/abs/2410.09309) | Toyota/Columbia | ICRA | 2024 | 6축 F/T (ATI) | ✅ 스칼라 강성 | UR5e + 수동 도구 | ✗ | ✗ | 물건 뒤집기, 꽃병 닦기 |
| [**TacDiffusion**](https://arxiv.org/abs/2409.11047) | TU Munich MIRMI | ICRA | 2024 | 촉각 | ✅ 6D 렌치 | 그리퍼 + 촉각 | [GitHub](https://github.com/popnut123/TacDiffusion) ✅ | ✗ | 힘 도메인 diffusion, 95.7% 제로샷 |
| [**FARM**](https://arxiv.org/abs/2510.13324) | TU Munich MIRMI | arXiv | 2025 | GelSight Mini | ✅ 파지력 | 개조된 UMI 그리퍼 | ✗ | ✗ | 관절 위치 + 힘 예측 |
| [**T-Dex**](https://arxiv.org/abs/2303.12076) | NYU (Pinto) | ICRA | 2024 | 촉각 (DIGIT) | ✗ (위치만) | **Allegro (16) + DIGIT** + Kinova arm | [GitHub](https://github.com/irmakguzey/tdex) ✅ | ✗ | 5가지 다지 작업 (조이스틱, 책, 그릇, 페그, 점토); 비전 전용 대비 1.7배. §3 항목 중 다지 핸드를 사용한 극소수 사례 중 하나. |

---

## 4. VLM 안내 임피던스 제어

VLM/LLM이 하위 수준 컨트롤러를 위한 임피던스 매개변수 (K, D)를 생성하거나 검색하는 시스템.

| 논문 | 연구 그룹 | 학회 | 연도 | K/D 적응 방법 | 강성 (K) | 감쇠 (D) | 로봇 | 다지 핸드? | 코드 | 가중치 |
|---|---|---|---|---|---|---|---|---|---|---|
| [**CompliantVLA-adaptor**](https://arxiv.org/abs/2601.15541) | IIT Genoa / TU Darmstadt | arXiv | 2026 | VLM (GPT-4o-mini) 제로샷 | ✅ (Kx,Ky,Kz) | ✅ (Dx,Dy,Dz) | Franka Panda + 그리퍼 | ✗ | 프로젝트 페이지 (준비 중) | ✗ (학습 불필요) |
| [**OmniVIC**](https://arxiv.org/abs/2510.17150) | IIT Genoa / Georgia Tech | arXiv | 2025 | VLM + RAG 자기 개선 | ✅ | ✅ | Franka Panda + F/T 센서 | ✗ | ✗ | ✗ (GPT-4o-mini API 사용) |
| [**HumanoidVLM**](https://arxiv.org/abs/2601.14874) | - | HRI | 2026 | VLM (Molmo-7B) + FAISS RAG | ✅ (검색) | ✅ (검색) | Unitree G1 휴머노이드 | ✗ | ✗ | ✗ |
| **SafeHumanoid** | 동일 그룹 | HRI | 2026 | VLM + RAG 검색 | ✅ | ✅ | Unitree G1 | ✗ | ✗ | ✗ |
| [**ImpedanceGPT**](https://arxiv.org/abs/2503.02723) | - | IROS | 2025 | VLM (Molmo) + RAG | ✅ | ✅ | 드론 군집 (조작 아님) | N/A | [GitHub](https://github.com/Faryal-Batool/ImpedanceGPT) ✅ | ✗ |

---

## 5. 학습된 임피던스 / 가변 컴플라이언스 제어

VLM 백본 없이 임피던스/강성/감쇠 매개변수를 학습하거나 최적화하는 시스템. VLM 기반 임피던스 접근법은 §4 참조. 힘을 입력으로 사용하지만 위치만 출력하는 논문(예: FoAR, FACTR)은 §3에 수록.

| 논문 | 연구 그룹 | 학회 | 연도 | 강성 (K) | 감쇠 (D) | 학습 방법 | 로봇 | 다지 핸드? | 시뮬레이션 | 코드 | 가중치 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| [**Comp-ACT**](https://arxiv.org/abs/2406.14990) | OMRON SINIC X / UTokyo | IROS | 2024 | ✅ (12D Cholesky) | ✗ | IL (VR 시연 기반 ACT) | 2x UR5e + 그리퍼 | ✗ | Robosuite (MuJoCo) | [GitHub](https://github.com/omron-sinicx/CompACT) ✅ | ✗ |
| [**Diff-Impedance**](https://arxiv.org/abs/2509.19696) | KIT / MIT | arXiv | 2025 | ✅ | ✅ | Diffusion + 에너지 기반 | KUKA LBR iiwa | ✗ | Sim + real | [GitHub](https://github.com/StrokeAIRobotics/DiffusionBasedImpedanceLearning) ✅ | ✗ |
| [**VICES**](https://arxiv.org/abs/1906.08880) | Stanford / NVIDIA | IROS | 2019 | ✅ | ✅ | RL (policy gradient) | Franka/Sawyer + 그리퍼 | ✗ | Robosuite (MuJoCo) | [robosuite/vices](https://github.com/ARISE-Initiative/robosuite/tree/vices_iros19) ✅ | ✗ |
| [**CHIP**](https://arxiv.org/abs/2512.14689) | NVIDIA NVLabs | ICRA | 2025 | ✅ (EE 강성) | ✗ | RL (hindsight perturbation) | 휴머노이드 35-DoF | ✗ | Isaac Sim | [Page](https://nvlabs.github.io/CHIP/) | ✗ |
| [**FILIC**](https://arxiv.org/abs/2509.17053) | Tsinghua/HKUST | arXiv | 2025 | 고정 K | 고정 B | IL (transformer, 25Hz) | AIRBOT Play | ✗ | MuJoCo + real | [GitHub](https://github.com/OpenGHz/FILIC) ✅ | ✗ |
| [**CHEQ**](https://arxiv.org/abs/2501.07985) | RWTH Aachen | arXiv | 2025 | ✅ | ✅ | RL (하이브리드 적응) | 팔 (연마) | ✗ | 실제 하드웨어 | ✗ | ✗ |
| [**DA-VIL**](https://arxiv.org/abs/2410.19712) | IIIT/Brown | ICRA | 2024 | ✅ | 미보고 | RL + QP 최적화 | 양팔 | ✗ | Sim | 프로젝트 페이지만 | ✗ |
| [**DexForce**](https://arxiv.org/abs/2501.10356) | Stanford | RA-L | 2025 | 고정 k_f | ✗ | 수동 조정 | Allegro (16) | **✅** | ✗ (실제만) | ✗ | ✗ |
| [**Force Policy**](https://arxiv.org/abs/2602.22088) | SJTU/Flexiv | RSS | 2026 | 힘 목표 | ✗ | IL (원격 조작 시연) | Flexiv + 그리퍼 | ✗ | ✗ (실제만) | ✗ | ✗ |
| [**IndustReal**](https://arxiv.org/abs/2305.17110) | NVIDIA | RSS | 2023 | 고정 | 고정 | RL (PPO) 포즈 학습 | Franka + 그리퍼 | ✗ | IsaacGym | [GitHub](https://github.com/NVlabs/industreallib) ✅ | ✅ RL policies |
| [**Divide et Impera**](https://arxiv.org/abs/2410.01054) | MIT/KIT | arXiv | 2024 | ✅ (군집) | ✅ | NN 성공 예측기 | 실제 팔 | ✗ | Real | ✗ | ✗ |
| [**DCM**](https://arxiv.org/abs/2403.13221) | Omron SINIC X | IROS | 2024 | VIC 입력 | ✗ | Diffusion 접촉 모델 | 팔 + 그리퍼 | ✗ | ✗ | ✗ | ✗ |

---

## 6. VLA 기반 모델: 버전 이력

### 6.1 Physical Intelligence pi 시리즈

| 버전 | 날짜 | 파라미터 | VLM 백본 | 행동 헤드 | 다지 핸드 | 힘/임피던스 | 오픈 가중치 |
|---|---|---|---|---|---|---|---|
| **pi0** | 2024년 10월 | 3.3B | PaliGemma 3B | Flow matching (300M) | ✗ (그리퍼) | ✗ | ✅ Apache 2.0 ([openpi](https://github.com/Physical-Intelligence/openpi), [HF](https://huggingface.co/lerobot/pi0_base)) |
| **pi0-FAST** | 2025년 1월 | 3.3B | PaliGemma 3B | 자기회귀 (FAST tokenizer) | ✗ | ✗ | ✅ Apache 2.0 (openpi) |
| **pi0.5** | 2025년 4월 | 3.3B | PaliGemma 3B | 2단계: FAST 사전학습 → flow matching | ✗ | ✗ | ✅ Apache 2.0 ([HF](https://huggingface.co/lerobot/pi05_base)) |
| **pi0.6 / pi\*0.6** | 2025년 11월 | ~5B | Gemma3 4B | Flow + token 이중 | ✗ | ✗ | 공식 미공개; 서드파티 재구현 존재 |
| **pi0.7** | 2026년 4월 | ~5B | Gemma3 4B + 400M 비전 | Flow matching (860M DiT) | ✗ | ✗ | 2026년 5월 기준 미공개 |

모든 pi 버전은 평행 조 그리퍼만 사용. 행동 공간은 18-19D (양팔 6-DoF + 그리퍼 + 베이스). 어떤 버전에서도 힘 또는 임피던스 출력 없음.

### 6.2 NVIDIA GR00T 시리즈

| 버전 | 날짜 | 파라미터 | VLM 백본 | DiT 레이어 | 다지 핸드 | 힘/임피던스 | 오픈 가중치 |
|---|---|---|---|---|---|---|---|
| **GR00T N1** | 2025년 3월 | 2.2B | Eagle-2 | 16 | Fourier 핸드 (휴머노이드 통합) | ✗ | ✅ 비상업용 ([HF](https://huggingface.co/nvidia/GR00T-N1-2B)) |
| **GR00T N1.5** | 2025년 중반 | 3B | Eagle 2.5 (고정) | 16 | 미문서화 | ✗ | ✅ 비상업용 ([HF](https://huggingface.co/nvidia/GR00T-N1.5-3B)) |
| **GR00T N1.6** | 2025년 후반 | 3B | Cosmos-2B | 32 | 미문서화 | ✗ | ✅ ([HF](https://huggingface.co/nvidia/GR00T-N1.6-3B)) |
| **GR00T N1.7** | 2026년 5월 | 3B | Cosmos-Reason2-2B (Qwen3-VL) | 32 | 22-DoF (EgoScale/Sharpa 표현) | ✗ | ✅ 상업용 허용 ([HF](https://huggingface.co/nvidia/GR00T-N1.7-3B)) |

**GR00T-Dexterity**는 별도의 RL 워크플로우(VLA 모델이 아님)로 DextrAH-G 기반. Isaac Lab에서 geometric fabrics를 사용하여 Allegro Hand (16 DoF) + Kuka를 지원함. GR00T N1.x VLA 모델은 다중 손가락 핸드 행동을 직접 출력하지 않음.

모든 GR00T VLA 버전은 위치 목표만 출력. N1.7의 "22 DoF 핸드"는 인간 손 동작을 22-DoF Sharpa 핸드 관절 각도로 표현하는 EgoScale 사전학습 프레임워크에서 유래. Unitree G1의 물리적 핸드(Dex3-1)는 핸드당 7 DoF만 보유. 22-DoF 능력은 인간 비디오 사전학습 시 사용된 행동 표현을 의미하며 배치 핸드가 아님.

### 6.3 기타 주요 VLA

| 논문 | 연구 그룹 | 학회 | 연도 | 다지 핸드? | 힘 출력? | 오픈 코드 | 오픈 가중치 | 핵심 특징 |
|---|---|---|---|---|---|---|---|---|
| [**Gemini Robotics**](https://arxiv.org/abs/2503.20020) | Google DeepMind | arXiv | 2025 | ✗ (그리퍼) | ✗ | ✗ | ✗ (비공개, 신뢰 테스터) | Gemini 2.0 기반 VLA; 일반화 벤치마크에서 SOTA 2배; ALOHA/Franka/Apollo |
| **Gemini Robotics 1.5** | Google DeepMind | Blog | 2026 | ✗ | ✗ | ✗ | ✗ (신뢰 테스터) | VLA + 추론; 교차 임바디먼트; Gemini API (ER 1.5) |
| **Gemini Robotics On-Device** | Google DeepMind | Blog | 2025 | ✗ | ✗ | SDK (제한적) | ✗ | 온디바이스 VLA; 50-100 시연으로 파인튜닝; 네트워크 의존성 없음 |
| [**RT-2**](https://arxiv.org/abs/2307.15818) | Google DeepMind | CoRL | 2023 | ✗ | ✗ | ✗ | ✗ (비공개) | 55B VLM을 로봇 행동에 공동 파인튜닝 |
| [**OpenVLA**](https://arxiv.org/abs/2406.09246) | Berkeley/Stanford | CoRL | 2024 | ✗ | ✗ | [GitHub](https://github.com/openvla/openvla) ✅ | ✅ HF | 7B VLA 베이스라인, Apache 2.0 |
| [**OpenVLA-OFT**](https://arxiv.org/abs/2502.19645) | Stanford/Berkeley | RSS | 2025 | ✗ (ALOHA) | ✗ | [GitHub](https://github.com/moojink/openvla-oft) ✅ | ✅ | 26배 빠른 추론, 병렬 디코딩 |
| [**Octo**](https://arxiv.org/abs/2405.12213) | Berkeley RAIL | RSS | 2024 | ✗ | ✗ | [GitHub](https://github.com/octo-models/octo) ✅ | ✅ HF | 93M, 모듈형 파인튜닝 |
| [**RDT-1B**](https://arxiv.org/abs/2410.07864) | Tsinghua thu-ml | ICLR | 2025 | ✗ (양손) | ✗ | [GitHub](https://github.com/thu-ml/RoboticsDiffusionTransformer) ✅ | ✅ HF 1B | 최대 규모 오픈 diffusion 모델 |
| [**HPT**](https://arxiv.org/abs/2409.20537) | MIT (Kaiming He) | NeurIPS | 2024 | ✗ | ✗ | [GitHub](https://github.com/liruiw/HPT) ✅ | ✗ | 이종 임바디먼트 사전학습 |
| [**CogACT**](https://arxiv.org/abs/2411.19650) | Microsoft | arXiv | 2024 | ✗ | ✗ | [GitHub](https://github.com/microsoft/CogACT) ✅ | ✗ | 인지-행동 분리 |
| [**EgoScale**](https://arxiv.org/abs/2602.16710) | NVIDIA/Berkeley | arXiv | 2026 | ✅ 22-DoF | ✗ | ✗ | ✗ | 20K시간 인간 비디오, 다지 스케일링 법칙 |
| [**SimpleVLA-RL**](https://arxiv.org/abs/2509.09674) | — | ICLR | 2025 | ✗ | ✗ | [GitHub](https://github.com/PRIME-RL/SimpleVLA-RL) ✅ | ✗ | VLA의 RL 파인튜닝 |
| [**SpatialVLA**](https://arxiv.org/abs/2501.15830) | Shanghai AI Lab / Multi-inst. | RSS | 2025 | ✗ | ✗ | ✅ (프로젝트 페이지) | ✅ | PaliGemma2 기반 3.5B VLA, Ego3D 위치 인코딩 + 적응형 행동 그리드 |
| [**TinyVLA**](https://arxiv.org/abs/2409.12514) | ECNU / Midea | AAAI | 2025 | ✗ | ✗ | ✗ (프로젝트 페이지만) | ✗ | 1.3B VLA + diffusion 디코더; 7B OpenVLA와 동등 성능, 20배 빠름 |
| [**LLARVA**](https://arxiv.org/abs/2406.11815) | UC Berkeley | arXiv | 2024 | ✗ | ✗ | ✗ (프로젝트 페이지만) | ✗ | 2D 시각 궤적 보조 작업을 통한 비전-행동 인스트럭션 튜닝 |
| [**UniAct**](https://arxiv.org/abs/2501.10105) | Multi-inst. | CVPR | 2025 | 다양한 핸드 대상 설계 | ✗ | [GitHub](https://github.com/2toinf/UniAct) ✅ | ✗ | 범용 행동 코드북 |

### 6.4 비전-운동 정책 (언어 조건부 없음)

VLM 백본을 사용하지 않지만 다지 조작의 베이스라인 또는 구성 요소로 널리 채택되는 영향력 있는 비전-운동 정책.

| 논문 | 연구 그룹 | 학회 | 연도 | 다지 핸드? | 힘 출력? | 오픈 코드 | 오픈 가중치 | 핵심 특징 |
|---|---|---|---|---|---|---|---|---|
| [**Diffusion Policy**](https://arxiv.org/abs/2303.04137) | Columbia (Shuran Song) | RSS | 2023 | ✗ | ✗ | [GitHub](https://github.com/real-stanford/diffusion_policy) ✅ | ✗ | 기초적 diffusion policy 방법 |
| [**ACT / ALOHA**](https://arxiv.org/abs/2304.13705) | Stanford (Tony Zhao) | RSS | 2023 | ✗ (그리퍼) | ✗ | [GitHub](https://github.com/tonyzhaozh/act) ✅ | ✗ | 행동 청킹 transformer, 양손 원격 조작 |
| [**DP3**](https://arxiv.org/abs/2403.03954) | Tsinghua (Yanjie Ze) | RSS | 2024 | ✅ (sim) | ✗ | [GitHub](https://github.com/YanjieZe/3D-Diffusion-Policy) ✅ | ✗ | 3D 포인트 클라우드 diffusion, 72가지 작업 |
| [**iDP3**](https://arxiv.org/abs/2410.10803) | Stanford/Tsinghua | IROS | 2025 | ✅ Inspire (25 DoF) | ✗ | [GitHub](https://github.com/YanjieZe/Improved-3D-Diffusion-Policy) ✅ | ✗ | Fourier GR1 휴머노이드에서 자기중심 3D |
| [**DexWM**](https://arxiv.org/abs/2512.13644) | Meta FAIR / NYU | arXiv | 2025 | ✅ Allegro + Franka | ✗ | ✗ | ✗ | 다지 핸드-객체 상호작용을 위한 월드 모델 |

---

## 7. RL 기반 다지 조작

### 7.1 다지 파지

| 논문 | 연구 그룹 | 학회 | 연도 | RL 알고리즘 | 핸드 (자유도) | 시뮬레이션 | Sim2Real | 객체 | 코드 | 가중치 |
|---|---|---|---|---|---|---|---|---|---|---|
| [**CrossDex**](https://arxiv.org/abs/2410.02479) | PKU-RL | ICLR | 2025 | PPO + DAgger | 6종 핸드 (Shadow, Allegro, LEAP, ...) | IsaacGym P4 | ✅ | 100 (YCB+GRAB) | [GitHub](https://github.com/PKU-RL/CrossDex) ✅ | 부분적 |
| [**ResDex**](https://arxiv.org/abs/2410.01481) | PKU-RL | ICLR | 2025 | PPO + MoE + DAgger | Shadow (24) | IsaacGym P4 | ✗ | 3200, 88.8% | [GitHub](https://github.com/PKU-RL/ResDex) ✅ | 부분적 |
| [**UniDexGrasp++**](https://arxiv.org/abs/2304.00464) | PKU-EPIC | ICCV | 2023 | PPO + DAgger | Shadow (24) | IsaacGym | ✗ | 3000+, 85.4% | [GitHub](https://github.com/PKU-EPIC/UniDexGrasp2) ✅ | ✅ state ckpt |
| [**UniDexGrasp**](https://arxiv.org/abs/2303.00938) | PKU-EPIC | CVPR | 2023 | PPO (목표 조건부) | Shadow (24) | IsaacGym | ✗ | 3000+, ~60% | [GitHub](https://github.com/PKU-EPIC/UniDexGrasp) ✅ | ✗ |
| [**BODex**](https://arxiv.org/abs/2412.16490) | PKU-EPIC | ICRA | 2025 | 이중 수준 최적화 | Shadow, Allegro, LEAP | cuRobo | ✅ 81% | 5355 | [GitHub](https://github.com/JYChen18/BODex) ✅ | HF 데이터셋 |
| [**DexGrasp Anything**](https://arxiv.org/abs/2409.11159) | ShanghaiTech | CVPR Highlight | 2025 | Diffusion | Shadow | IsaacGym | ✗ | 15K+, 340만 파지 | [GitHub](https://github.com/4DVLab/DexGrasp-Anything) ✅ | ✅ HF+GDrive |
| [**DexGraspNet 2.0**](https://arxiv.org/abs/2410.15590) | PKU-EPIC | CoRL | 2024 | Diffusion | Shadow | IsaacGym | ✅ 90.7% | 1319, 4.26억 파지 | [GitHub](https://github.com/PKU-EPIC/DexGraspNet2) ✅ | ✅ HF |
| [**RobustDexGrasp**](https://arxiv.org/abs/2501.01771) | ETH Zurich | CoRL | 2025 | PPO + 교사-학생 | Allegro (16) + UR5 | RaiSim | ✅ 94.6% | 시뮬 247K, 실제 512 | [GitHub](https://github.com/zdchan/RobustDexGrasp) ✅ | ✅ |
| [**Dexonomy**](https://arxiv.org/abs/2504.01301) | PKU-EPIC | RSS | 2025 | 최적화 | Shadow, Allegro, LEAP, Unitree G1 | MuJoCo + cuRobo | ✅ 82.3% | 10.7K, 31종 | [GitHub](https://github.com/JYChen18/Dexonomy) ✅ | HF |
| [**UltraDexGrasp**](https://arxiv.org/abs/2603.05312) | InternRobotics | ICRA | 2026 | 다중 전략 | 다수 | BODex + cuRobo | ✅ 81.2% | 2000만 프레임 | [GitHub](https://github.com/InternRobotics/UltraDexGrasp) ✅ | ✗ |
| [**DexPoint**](https://arxiv.org/abs/2211.09423) | UCSD | CoRL | 2022 | PPO (포인트 클라우드) | Allegro (16) | IsaacGym | ✅ | 카테고리 수준 신규 | [GitHub](https://github.com/yzqin/dexpoint-release) ✅ | ✗ |
| [**AnyGrasp**](https://arxiv.org/abs/2212.08333) | SJTU (Cewu Lu) | IEEE T-RO | 2023 | 지도학습 (GSNet) | 평행 조 그리퍼 | GraspNet-1B | ✅ 93.3% | 300+ 미지 객체, 시간당 900+ 픽 | [SDK](https://github.com/graspnet/anygrasp_sdk) (라이선스) | ✗ | 상위 파지 감지 (평행 조). 다지 VLA 파이프라인의 인식 모듈로 널리 사용되어 포함. |
| [**DextrAH-G/RGB**](https://arxiv.org/abs/2407.02274) | NVIDIA | CoRL | 2024 | PPO + geometric fabrics | Allegro (16) + Kuka | Isaac Lab | ✅ | 다중 객체 | [GitHub](https://github.com/NVlabs/DEXTRAH) ✅ | ✗ |

### 7.2 핸드 내 조작 / 방향 재설정

| 논문 | 연구 그룹 | 학회 | 연도 | 핸드 (자유도) | 시뮬레이션 | Sim2Real | 코드 | 가중치 |
|---|---|---|---|---|---|---|---|---|
| [**Dactyl**](https://arxiv.org/abs/1808.00177) | OpenAI | arXiv 2018 / IJRR 2020 | 2018 | Shadow (24) | MuJoCo | ✅ (ADR) | ✗ | ✗ |
| [**Hora**](https://arxiv.org/abs/2210.04887) | Berkeley/Meta | CoRL | 2022 | Allegro (16) | IsaacGym P4 | ✅ | [GitHub](https://github.com/HaozhiQi/hora) ✅ | ✅ |
| [**Rotating w/o Seeing**](https://arxiv.org/abs/2303.10880) | UCSD | RSS | 2023 | Allegro (16) + 이진 촉각 | IsaacGym | ✅ | [Page](https://touchdexterity.github.io) | ✗ |
| [**General In-Hand Rotation**](https://arxiv.org/abs/2309.09979) | Berkeley/Meta | CoRL | 2023 | Allegro (16) + DIGIT | IsaacGym | ✅ | (hora 리포에 포함) | ✗ |
| [**RotateIt**](https://arxiv.org/abs/2309.02388) | Berkeley/Meta/CMU | CoRL | 2023 | Allegro (16) + DIGIT | IsaacGym | ✅ | (hora 리포에 포함) | ✗ |
| [**AnyRotate**](https://arxiv.org/abs/2405.07391) | U. Bristol | CoRL | 2024 | Allegro (16) + 촉각 | IsaacGym | ✅ | ✗ | ✗ |
| [**Visual Dexterity**](https://arxiv.org/abs/2211.11744) | MIT CSAIL | Science Robotics | 2023 | D'Claw (9/12) | IsaacGym P3 | ✅ | [GitHub](https://github.com/Improbable-AI/dexenv) ✅ | ✅ |
| [**DeXtreme**](https://arxiv.org/abs/2210.13702) | NVIDIA | ICRA | 2023 | Allegro (16) | IsaacGym | ✅ | IsaacGymEnvs 내 ✅ | ✗ |
| [**DexPBT**](https://arxiv.org/abs/2305.12127) | NVIDIA | RSS | 2023 | Allegro (16) + Kuka | IsaacGym | ✗ | IsaacGymEnvs 내 ✅ | ✗ |
| [**SAPG**](https://arxiv.org/abs/2407.04890) | CMU | ICML Oral | 2024 | Allegro/Shadow (16-46) | IsaacGym P4 | ✗ | [GitHub](https://github.com/jayeshs999/sapg) ✅ | ✗ |
| [**DexHandDiff**](https://arxiv.org/abs/2411.18562) | HKU/Berkeley | CVPR | 2025 | Shadow | Adroit (MuJoCo) | ✗ | [GitHub](https://github.com/Liang-ZX/DexHandDiff) ✅ | ✅ HF |

### 7.3 장기 / 다단계 / 접촉 풍부

| 논문 | 연구 그룹 | 학회 | 연도 | 핸드 (자유도) | 작업 | 시뮬레이션 | Sim2Real | 코드 | 가중치 |
|---|---|---|---|---|---|---|---|---|---|
| [**SeqDex**](https://arxiv.org/abs/2309.00987) | Stanford | CoRL | 2023 | Allegro (16) | 연쇄 정책 (탐색→방향 설정→파지→삽입) | IsaacGym | ✅ | [GitHub](https://github.com/sequential-dexterity/SeqDex) ✅ | ✅ |
| [**Bi-DexHands**](https://arxiv.org/abs/2206.08686) | PKU-MARL | NeurIPS | 2022 | 2x Shadow (48) | 16+ 양손 작업 | IsaacGym | ✗ | [GitHub](https://github.com/PKU-MARL/DexterousHands) ✅ | ✅ |
| [**DexArt**](https://arxiv.org/abs/2305.05706) | UCSD | CVPR | 2023 | Allegro (16) | 4가지 관절 객체 작업 | SAPIEN | ✗ | [GitHub](https://github.com/Kami-code/dexart-release) ✅ | ✅ |
| [**TCDM**](https://arxiv.org/abs/2209.11221) | Meta | ICRA | 2023 | 3종 핸드 플랫폼 | 50가지 작업, 34개 객체 | MuJoCo | ✗ | [GitHub](https://github.com/facebookresearch/TCDM) ✅ | ✅ |
| [**VTDexManip**](https://arxiv.org/abs/2501.01370) | - | ICLR | 2025 | Multi-finger (sim) | 6가지 작업 (병뚜껑, 수도꼭지, 방향 재설정) | IsaacGym | ✗ | [GitHub](https://github.com/LQTS/VTDexManip) ✅ | ✅ 18개 모델 |
| [**DexGarmentLab**](https://arxiv.org/abs/2503.18693) | Multi-inst. | NeurIPS Spotlight | 2025 | 양손 다지 | 15가지 의류 작업, 2500+ 의류 | IsaacSim | ✗ | [GitHub](https://github.com/wayrise/DexGarmentLab) ✅ | ✗ |
| [**Contact Trust Region**](https://arxiv.org/abs/2505.02291) | MIT CSAIL (Tedrake) | IJRR | 2025 | Allegro (16) | 접촉 풍부 MPC | Drake | ✗ | ✗ | ✗ |
| [**Complementarity-Free**](https://arxiv.org/abs/2408.07855) | MIT CSAIL (Pang, Tedrake) | RSS | 2024 | Allegro (16) | 닫힌 형태 미분 가능 접촉, 50-100 Hz MPC | Drake | ✗ | ✗ | ✗ |
| [**ComFree-Sim**](https://arxiv.org/abs/2603.12185) | — | arXiv | 2026 | LEAP Hand | NVIDIA Warp 기반 GPU 병렬 접촉 MPC | Custom (Warp) | ✗ | ✗ | ✗ |

참고: IndustReal (NVIDIA, RSS 2023)도 RL을 통한 접촉 풍부 조립을 다룸; 자세한 내용은 §5 참조.

### 7.4 추가 최신 RL

| 논문 | 연구 그룹 | 학회 | 연도 | 핸드 (자유도) | 작업 | Sim2Real | 코드 |
|---|---|---|---|---|---|---|---|
| [**DQ-RISE**](https://arxiv.org/abs/2503.01766) | SJTU | ICRA | 2026 | OyMotion RoHand + Flexiv Rizon 4 | 6가지 실제 작업, 85.83% | ✅ | [GitHub](https://github.com/rise-policy/DQ-RISE) ✅ |
| [**DexTrack**](https://arxiv.org/abs/2501.15760) | PKU/Shanghai AI | ICLR | 2025 | Shadow (24), Allegro (16) | MoCap 추적 | ✗ | [GitHub](https://github.com/Meowuu7/DexTrack) 부분적 |
| [**BiDexHD**](https://arxiv.org/abs/2501.09821) | PKU | arXiv | 2025 | 2x Shadow (48) | 141가지 양손 작업 (TACO) | ✗ | ✗ |
| [**HandelBot**](https://arxiv.org/abs/2603.12243) | Stanford | arXiv | 2026 | LEAP (16) 양손 | 실제 피아노 연주 | ✅ | [GitHub](https://github.com/amberxie88/handelbot) ✅ |
| [**DexDrummer**](https://arxiv.org/abs/2603.22263) | Stanford | arXiv | 2026 | 양손 다지 | 드럼 연주 (접촉 풍부) | ✗ | [GitHub](https://github.com/hc-fang/dexdrummer) ✅ |
| [**RoboPianist**](https://arxiv.org/abs/2304.04150) | Google/Berkeley | CoRL | 2023 | 의인화 양손 | 피아노 (150곡) | ✗ | [GitHub](https://github.com/google-research/robopianist) ✅ |
| [**DemoStart**](https://arxiv.org/abs/2409.06613) | Google DeepMind | ICRA | 2024 | DEX-EE (3-finger) | 플러그 삽입, 큐브 방향 재설정 | ✅ | ✗ |
| **Closing Reality Gap** | - | arXiv | 2026 | 5-finger hand | 힘 제어 파지 | ✅ 제로샷 | ✗ |
| [**Maniwhere**](https://arxiv.org/abs/2407.15815) | Shanghai AI Lab | CoRL | 2024 | Allegro (16) | 8가지 작업, 시각적 일반화 | ✅ | [GitHub](https://github.com/gemcollector/maniwhere) ✅ |
| [**Eureka**](https://arxiv.org/abs/2310.12931) | NVIDIA | ICLR | 2024 | Shadow (24, sim) | LLM 생성 보상, 펜 스피닝 | ✗ | [GitHub](https://github.com/eureka-research/Eureka) ✅ |
| [**DrEureka**](https://arxiv.org/abs/2406.01967) | NVIDIA | RSS | 2024 | Shadow (sim) + 4족 로봇 | LLM 안내 DR, sim2real | ✅ | [GitHub](https://github.com/eureka-research/DrEureka) ✅ |
| [**DexMV**](https://arxiv.org/abs/2108.05877) | UCSD | ECCV | 2022 | Adroit (30, sim) | 인간 비디오로부터 IL (따르기, 놓기, 재배치) | ✗ | [GitHub](https://github.com/yzqin/dexmv-sim) ✅ |
| [**CyberDemo**](https://arxiv.org/abs/2402.14795) | UCSD | CVPR | 2024 | Allegro (16) | 증강 시뮬 시연, 밸브 회전 | ✅ | [GitHub](https://github.com/wang59695487/CyberDemo) ✅ |

---

## 8. 데이터셋

### 8.1 로봇 다지 핸드 데이터셋

| 데이터셋 | 연도 | 학회 | 규모 | 핸드 유형 | 작업 | F/T 또는 촉각 | 다운로드 | 형식 |
|---|---|---|---|---|---|---|---|---|
| **UniDex** | 2026 | CVPR | 900만 프레임, 50K+ 궤적 | 8종 로봇 핸드 (FAAS) | 다양한 조작 | ✗ | ✅ [HF](https://huggingface.co/datasets/UniDex-ai/UniDex) | HDF5 |
| **Dexora** | 2025 | ICRA | 12.2K 에피소드, 40.5시간 실제 | 양손 36-DoF | 픽, 조작, 조립, 도구 | ✗ | ✅ [HF](https://huggingface.co/datasets/ZZongzheng0918/Dexora) | Parquet+MP4 |
| **DexMimicGen** | 2024 | ICRA | 21K 시연 | 양손 다지 | 9가지 작업 | ✗ | ✅ [HF](https://huggingface.co/datasets/MimicGen/dexmimicgen_datasets) 59.9GB | HDF5 |
| **DexGraspNet 2.0** | 2024 | CoRL | 4.26억 파지 | Shadow | 파지 | ✗ | ✅ [HF](https://huggingface.co/datasets/lhrlhr/DexGraspNet2.0) | WebDataset |
| **VTDexManip** | 2025 | ICLR | 56.5만 프레임, 182개 객체 | Multi-finger (sim) | 6가지 복잡 작업 | ✅ 이진 촉각 | ✅ [GitHub](https://github.com/LQTS/VTDexManip) | IsaacGym |
| **ManipTrans/DexManipNet** | 2025 | CVPR | 3.3K 에피소드 | 6종 핸드 | 양손 조작 | ✗ | ✅ [HF](https://huggingface.co/datasets/ManipTrans/DexManipNet) | MuJoCo |
| **CEDex** | 2026 | ICRA | 2000만 파지, 50만 객체 | Shadow, Allegro, LEAP | 교차 임바디먼트 파지 | ✗ | ✅ [GitHub](https://github.com/GeorgeWuzy/CEDex-Grasp) | Custom |
| **Dexonomy** | 2025 | RSS | 950만 파지, 10.7K 객체 | Shadow (공개; 논문에서 Allegro, LEAP 다룸) | 31종 파지 유형 | ✗ | ✅ [HF](https://huggingface.co/datasets/JiayiChenPKU/Dexonomy) | Custom |
| **Dex1B** | 2025 | RSS | 10억 시연, 6K+ 객체 | Shadow, Inspire, Ability | 파지 + 관절 조작 | ✗ | 불명확 | Custom |
| **Fourier ActionNet** | 2025 | — | 30K+ 궤적, 140시간 | Fourier Dex Hands | 실제 휴머노이드 양손 | ✗ | ✅ [action-net.org](https://action-net.org/) | Custom |
| **RoboMIND** | 2025 | RSS | 107K 궤적, 479가지 작업 | 다지 포함 다중 임바디먼트 | 다양한 조작 | ✗ | ✅ [HF](https://huggingface.co/datasets/x-humanoid-robomind/RoboMIND) | Custom |
| **Bi-DexHands** | 2022 | NeurIPS | 오프라인 RL 데이터셋 | 2x Shadow | 16+ 양손 작업 | ✗ | ✅ [GitHub](https://github.com/PKU-MARL/DexterousHands) | IsaacGym |
| **TCDM** | 2023 | ICRA | 50가지 작업, 34개 객체 | 3종 핸드 플랫폼 | 다양한 조작 | ✗ | ✅ [GitHub](https://github.com/facebookresearch/TCDM) | MuJoCo |
| **DAPG** | 2018 | RSS | 작업당 25개 인간 시연 | Shadow (sim) | 펜, 문, 해머, 공 | ✗ | ✅ [GitHub](https://github.com/aravindr93/hand_dapg) | Pickle/NumPy |

### 8.2 힘 / 촉각 / 접촉 데이터셋

| 데이터셋 | 연도 | 학회 | 규모 | 센서 유형 | 핸드 | 다운로드 | 핵심 특징 |
|---|---|---|---|---|---|---|---|
| **ForceVLA-Data** | 2025 | NeurIPS | 244 궤적, 14만 스텝 | 6축 F/T | 그리퍼 (Flexiv) | ✅ [HF](https://huggingface.co/datasets/qiaojunyu/ForceVLA-real-data) | 접촉 풍부 5가지 작업 |
| **REASSEMBLE** | 2024 | RSS | 4551 시연, 781분 | F/T + 이벤트 카메라 + 오디오 | 그리퍼 | ✅ [TUData](https://researchdata.tuwien.ac.at/records/0ewrv-8cb44) | 다중 모달 조립 |
| **RH20T** | 2023 | NeurIPS | 11만 에피소드, 5000만 프레임 | F/T + 손끝 촉각 | 그리퍼 | ✅ [Site](https://rh20t.github.io/) | 140+ 작업 |
| **Touch100k** | 2025 | Info. Fusion | 10.1만 샘플 | GelSight | N/A | ✅ [GitHub](https://github.com/cocacola-lab/TLV-Link) | 대규모 촉각-언어-비전 데이터셋 |
| **Sparsh/TacBench** | 2024 | CoRL | 46만+ 이미지 | DIGIT/GelSight (교차 센서) | N/A | ✅ [GitHub](https://github.com/facebookresearch/sparsh) | 교차 센서 SSL 촉각 인코더, 5가지 작업 벤치마크 |
| **TVL** | 2024 | ICML | 4.4만 쌍 | DIGIT | N/A | ✅ [GitHub](https://github.com/Max-Fu/tvl) + [HF](https://huggingface.co/datasets/Max-Fu/TVL) | 촉각-비전-언어 정렬 |
| **FMB** | 2025 | IJRR | 22.5K 시연 | F/T (Franka) | 그리퍼 | ✅ [HF](https://huggingface.co/datasets/charlesxu0124/functional-manipulation-benchmark) | 기능적 조작 |
| **FeelSight** | 2024 | Science Robotics | 70건 실험 | DIGIT + Allegro | Allegro (16) | ✅ [HF](https://huggingface.co/datasets/suddhu/Feelsight) | 핸드 내 촉각-시각 추적 |
| **ContactPose** | 2020 | ECCV | 2306 파지, 290만 이미지 | 열 접촉 | 인간 | ✅ [GitHub](https://github.com/facebookresearch/ContactPose) | 기능적 파지 |

### 8.3 인간 손 / 자기중심 데이터셋

| 데이터셋 | 연도 | 학회 | 규모 | 모달리티 | 작업 | 언어 | 다운로드 |
|---|---|---|---|---|---|---|---|
| **EgoDex** | 2025 | ICLR | 829시간, 30Hz 1080p | 자기중심 RGB + 68관절 3D (AVP) | 194가지 테이블탑 | ✅ LLM 설명 | ✅ [GitHub](https://github.com/apple/ml-egodex) ~1.7TB |
| **DexCanvas** | 2025 | arXiv | 7000시간 (v0.1=1%) | 다시점 RGB-D + MANO | 21가지 조작 유형 | ✗ | ✅ [HF](https://huggingface.co/datasets/DEXROBOT/DexCanvas) v0.1 |
| **GigaHands** | 2025 | CVPR | 34시간, 14K 클립 | 다시점 RGB + 3D 손 | 양손 | ✅ 84K 주석 | ✅ [Site](https://ivl.cs.brown.edu/research/gigahands.html) |
| **DexWild** | 2025 | RSS | 9.5K 에피소드, 33시간 | 다시점 RGB + 장갑 | 5가지 작업 | ✅ | ✅ [HF](https://huggingface.co/datasets/boardd/dexwild-dataset) 2.14TB |
| **HOI4D** | 2022 | CVPR | 240만 RGB-D, 4K 시퀀스 | 자기중심 RGB-D + 3D 손 | 카테고리 수준 | ✅ 행동 레이블 | ✅ [Site](https://hoi4d.github.io/) |
| **GRAB** | 2020 | ECCV | 162만 프레임 | SMPL-X + MANO + 접촉 | 전신 파지 | ✗ | ✅ [Site](https://grab.is.tue.mpg.de/) (등록 필요) |
| **ARCTIC** | 2023 | CVPR | 210만 프레임 | RGB + MANO + 접촉 | 양손 관절 조작 | ✗ | ✅ [Site](https://arctic.is.tue.mpg.de/) ~116GB |
| **OakInk / OakInk2** | 2022/24 | CVPR | 23만+ 프레임 | RGB + MANO + 객체 | 손-객체 상호작용 | ✅ (v2) | ✅ [HF](https://huggingface.co/datasets/kelvin34501/OakInk-v2) |
| **DexYCB** | 2021 | CVPR | 58.2만 RGB-D | RGB-D + MANO + 객체 | 파지 (20 YCB) | ✗ | ✅ [Site](https://dex-ycb.github.io/) 119GB |
| **Ego-Exo4D** | 2024 | CVPR | 1286시간, 740명 참가자 | 자기중심+외부 RGB + IMU + 시선 | 숙련 활동 | ✅ | ✅ [Site](https://ego-exo4d-data.org/) (등록 필요) |
| **Humanoid Everyday** | 2025 | arXiv | 10.3K 궤적, 300만 프레임 | RGB + 깊이 + LiDAR + 촉각 | 260가지 다지 작업 | ✅ | ✅ [HF](https://huggingface.co/datasets/USC-GVL/humanoid-everyday) |

### 8.4 교차 임바디먼트 사전학습 데이터셋

| 데이터셋 | 연도 | 학회 | 규모 | 임바디먼트 | 작업 | 형식 | 다운로드 |
|---|---|---|---|---|---|---|---|
| [**Open X-Embodiment (OXE)**](https://arxiv.org/abs/2310.08864) | 2023 | arXiv/ICRA | ~100만 에피소드 | 22종 로봇 (그리퍼만) | 527가지 스킬, 160K+ 작업 | RLDS (TF Datasets) | ✅ [Site](https://robotics-transformer-x.github.io/) |
| [**DROID**](https://arxiv.org/abs/2403.12945) | 2024 | arXiv | 76K 시연, 350시간 | Franka Panda (1종 임바디먼트, 564 씬) | 84가지 작업, 50명 운영자 | 스테레오 RGB + 자기수용감각 + 언어 | ✅ [Site](https://droid-dataset.github.io/) |

---

## 9. 시뮬레이션 벤치마크 및 플랫폼

| 벤치마크 | 학회 | 연도 | 다지 핸드 | 시뮬레이션 플랫폼 | 핵심 특징 | 설치 |
|---|---|---|---|---|---|---|
| [**ManiSkill3**](https://arxiv.org/abs/2410.00425) | RSS | 2025 | Allegro, DClaw | SAPIEN (GPU) | 430배 빠름, RL/IL/VLA 베이스라인 | `pip install mani-skill` |
| **MuJoCo Playground** | RSS demo | 2025 | LEAP Hand | MuJoCo | 수 분 내 학습, 제로샷 sim2real | `pip install playground` |
| **MuJoCo Manipulus** | 2025 | 2025 | 도구 조작 | MuJoCo | 16가지 도구 사용 작업 | 오픈 소스 |
| **Adroit** | RSS | 2018 | Shadow (24) | MuJoCo | 표준 RL 베이스라인 | `pip install gymnasium-robotics` |
| **Genesis** | 2024년 12월 | 2024 | 모든 URDF | Genesis | 실시간 대비 430K배, 미분 가능 | `pip install genesis-world` |
| **DiffTactile** | ICLR | 2024 | Multi-finger | Custom | 미분 가능 FEM 촉각 시뮬레이션 | [GitHub](https://github.com/Genesis-Embodied-AI/DiffTactile) |
| **TeleOpBench** | 2025 | 2025 | 3종 휴머노이드 | Isaac Sim | 30가지 작업, 4가지 원격 조작 모달리티 | [GitHub](https://github.com/cyjdlhy/TeleOpBench) |
| [**Isaac Lab**](https://isaac-sim.github.io/IsaacLab/) | RA-L / 2024 | 2024 | Allegro, Shadow, 모든 URDF | Isaac Sim (PhysX 5) | IsaacGym 후속, GPU 병렬, RTX 렌더링 | `pip install isaaclab` |
| [**TACTO**](https://github.com/facebookresearch/tacto) | RA-L | 2022 | 그리퍼 (DIGIT/GelSight sim) | PyBullet + PyRender | 비전 기반 촉각 센서 시뮬레이터 | `pip install tacto` |

---

## 10. 원격 조작 시스템

| 시스템 | 연구 그룹 | 학회 | 연도 | 입력 | 대상 핸드 | 힘 피드백 | 비용 | 코드 |
|---|---|---|---|---|---|---|---|---|
| [**DexCap**](https://arxiv.org/abs/2403.07788) | Stanford | RSS | 2024 | SLAM + 전자기 | LEAP Hand | ✗ | ~$2K | [GitHub](https://github.com/j96w/DexCap) ✅ |
| [**BunnyVisionPro**](https://arxiv.org/abs/2407.03162) | HKU / UCSD | arXiv | 2024 | Apple Vision Pro | 양손 다지 | 저비용 햅틱 | ~$3.5K+ | [GitHub](https://github.com/Dingry/BunnyVisionPro) ✅ |
| **AnyTeleop** | UCSD | RSS | 2023 | 비전 (카메라) | 다수 | ✗ | 저가 | 프로젝트 페이지 |
| [**DOGlove**](https://arxiv.org/abs/2505.14635) | TEA Lab | RSS | 2025 | 햅틱 글로브 | 모든 다지 핸드 | ✅ 5-DoF | <$600 | [GitHub](https://github.com/TEA-Lab/DOGlove) ✅ |
| [**DEXOP**](https://arxiv.org/abs/2509.04441) | Stanford | arXiv | 2025 | 수동 외골격 | 모든 다지 핸드 | ✅ 자기수용 | - | [Page](https://dex-op.github.io/) |
| [**DEX-Mouse**](https://arxiv.org/abs/2604.15013) | - | arXiv | 2026 | 핸드헬드 인터페이스 | 범용 | ✅ 근감각 | <$150 | 오픈소스 |
| [**Open TeleDex**](https://arxiv.org/abs/2510.14771) | - | arXiv | 2025 | 휴대폰 기반 | 모든 팔 + 핸드 | ✗ | 매우 저가 | [GitHub](https://github.com/omarrayyann/TeleDex) ✅ |
| [**OmniH2O**](https://arxiv.org/abs/2406.08858) | CMU LeCAR | CoRL | 2024 | VR/음성/RGB | 휴머노이드 | ✗ | - | [GitHub](https://github.com/LeCAR-Lab/human2humanoid) ✅ |
| [**Open-TeleVision**](https://arxiv.org/abs/2407.10107) | UCSD | CoRL | 2024 | 스테레오 VR | 양손 다지 | ✗ | - | [GitHub](https://github.com/OpenTeleVision/TeleVision) ✅ |
| [**HATO**](https://arxiv.org/abs/2404.16823) | UC Berkeley | ICRA | 2024 | Meta Quest 2 VR | 2x Psyonic Ability Hand (6 DoF) + 터치 센서 | ✗ (로봇 측 터치만) | 저가 (VR + 의수 핸드) | [GitHub](https://toruowo.github.io/hato/) ✅ |
| [**DexPilot**](https://arxiv.org/abs/1910.03135) | NVIDIA | ICRA | 2020 | 비전 (맨손, 단일 RGB 카메라) | Allegro (16) + Kuka IIWA | ✗ | 매우 저가 (카메라만) | [Page](https://sites.google.com/view/dex-pilot) |

---

## 11. 저비용 다지 핸드 하드웨어

| 핸드 | 연구 그룹 | 연도 | 자유도 | 비용 | Sim2Real | 촉각 | 설계 파일 |
|---|---|---|---|---|---|---|---|
| **LEAP Hand V2** | CMU (Pathak) | 2024 | 16 + 손바닥 | ~$3K | ✅ | ✗ | [Page](https://v2-adv.leaphand.com/) |
| **ORCA Hand** | ETH Zurich | 2025 | 17 | <$2K | ✅ (1시간 학습) | ✅ | [orcahand.com](https://www.orcahand.com/) 완전 공개 |
| **ISyHand** | MPI-IS | 2025 | 18 (12+6 손바닥) | ~$1.3K | ✅ | ✗ | [Page](https://isyhand.is.mpg.de/) |
| **RUKA Hand** | NYU (Pinto) | 2025 | 15 | <$1.3K | ✅ | ✗ | [Page](https://ruka-hand.github.io/) |
| **FAIVE Hand** | ETH Zurich (SRL) | 2024 | 11+ | ~$500-800 | ✅ | ✗ | [GitHub](https://github.com/srl-ethz/faive-hand) 완전 공개 |
| **Ability Hand** | PSYONIC Inc. | 2024 | 6 | 상용 | — | ✅ 손끝 압력 | [psyonic.io](https://www.psyonic.io/ability-hand) 비공개 |
| **XHand / Inspire Hand** | 중국 제조사 | 2023+ | 12-16 | ~$1-3K | 부분적 | ✗ | 비공개 상용 |
| **Digit 360** | Meta FAIR | 2024 | N/A (센서) | - | N/A | ✅ 18+ 모달리티 | 오픈소스 예정 |

---

## 12. 촉각 표현 모델

| 모델 | 연구 그룹 | 학회 | 연도 | 핵심 특징 | 코드 |
|---|---|---|---|---|---|
| **Sparsh** | Meta FAIR/CMU | CoRL | 2024 | SSL 교차 센서 촉각 인코더, TacBench 5가지 작업 벤치마크 | [GitHub](https://github.com/facebookresearch/sparsh) ✅, 가중치 ✅ |
| **UniTouch** | UCSD | CVPR | 2024 | 통합 촉각-비전-언어-소리 정렬 | [GitHub](https://github.com/cfeng16/UniTouch) ✅, 가중치 ✅ |
| **AnyTouch** | Renmin Univ | ICLR | 2025 | TacQuad 4센서 데이터셋을 활용한 교차 센서 SSL | [GitHub](https://github.com/GeWu-Lab/AnyTouch) ✅, 가중치 ✅ |
| **NeuralFeels** | Meta FAIR | Science Robotics | 2024 | Allegro+DIGIT 핸드 내 추적을 위한 뉴럴 필드 | [GitHub](https://github.com/facebookresearch/neuralfeels) ✅ |

---

## 13. 미개척 연구 방향

이 절에서는 서베이 문헌에서 도출되는 능력의 미탐구 교차점을 강조함. 이것이 전부는 아니며, 동시 진행 중이거나 미발표된 연구가 이러한 방향 중 일부를 부분적으로 다루고 있을 수 있음.

### 13.1 능력 매트릭스

다음 표는 접촉 풍부 다지 조작과 관련된 속성에 대해 대표 시스템을 매핑함. "시뮬레이션"은 학습 또는 평가를 위해 공개적으로 사용 가능한 시뮬레이션 환경을 의미함.

|  | 다중 손가락 핸드 | 도구 사용 | 힘/임피던스 출력 | VLA/언어 | 시뮬레이션 |
|---|---|---|---|---|---|
| **pi0~0.7** | ✗ (그리퍼만) | ✗ | ✗ | ✅ | ✗ |
| **GR00T N1~1.7** | 휴머노이드 통합만 | ✗ | ✗ | ✅ | ✅ Isaac Lab |
| **GR00T-Dexterity** | ✅ Allegro | ✗ (파지만) | ✗ | ✗ (RL만) | ✅ Isaac Lab |
| **UniDex-VLA** | ✅ 8종 핸드 | ✅ | ✗ | ✅ | 부분적 (리타겟팅 환경) |
| **DexVLA** | ✅ | ✗ | ✗ | ✅ | ✗ |
| **SimToolReal** | ✅ Sharpa 22-DoF | ✅ 24가지 작업 | ✗ | ✗ | ✅ IsaacGym |
| **CompliantVLA-adaptor** | ✗ (그리퍼) | ✗ | ✅ K, D | ✅ (고정 VLA) | ✅ LIBERO |
| **CHIP** | 휴머노이드 35-DoF | ✗ | ✅ EE 강성 | ✗ (RL) | ✅ |
| **TacDiffusion** | ✗ (그리퍼) | ✗ | ✅ 6D 렌치 | ✗ | ✗ |
| **DexForce** | ✅ Allegro | ✗ | 고정 k_f (수동 조정) | ✗ | ✗ |

### 13.2 관찰

다지 핸드를 이용한 접촉 풍부 조작 — 도구 사용, 조립, 또는 깨지기 쉬운 물체 다루기 등 — 은 단순히 위치 목표를 추적하는 것이 아니라 상호작용 힘을 조절하는 것을 요구한다. 부적절한 힘 제어는 객체 미끄러짐, 도구 파손, 또는 환경 손상을 초래한다. 그리퍼는 기계적 컴플라이언스로 보상할 수 있는 경우가 많지만, 고자유도 다지 핸드는 여러 손끝에 걸쳐 접촉을 분산하므로 각 접촉점의 힘 조절이 더 중요하면서도 더 어렵다. 이는 기존 시스템이 다지 제어와 힘/임피던스 인식을 결합하고 있는지를 검토하는 동기가 된다.

능력 매트릭스와 광범위한 서베이에서 여러 패턴이 드러난다:

**다지 VLA와 힘 인식 정책은 대체로 독립적으로 발전해 왔다.** 다지 VLA 문헌(§2)은 다양한 핸드에 걸친 위치 목표 생성에 초점을 맞추는 반면, 힘/임피던스 문헌(§3-5)은 그리퍼와 로봇 팔의 접촉 풍부 제어에 집중한다. UniDex-VLA, DexVLA, DexGraspVLA 모두 위치 목표만을 출력한다. 반대로 임피던스 매개변수를 출력하는 시스템(CompliantVLA-adaptor, CHIP, Comp-ACT, VICES)은 그리퍼 또는 팔에서 작동한다. DexForce만이 힘 인식을 통합한 다지 핸드 연구로, Allegro Hand에서 수동 조정된 고정 스케일링을 사용한다.

**교차 임바디먼트 행동 표현은 여전히 단편화되어 있다.** 다양한 임바디먼트 간 다지 핸드 행동을 표현하기 위해 여러 접근법이 경쟁하고 있다: FAAS (UniDex-VLA), 고유파지(eigengrasps) (CrossDex), 범용 코드북 (UniAct), 이종 스템 (HPT), 임바디먼트별 MLP (GR00T). 어떤 표현이 교차 핸드 일반화를 가장 잘 지원하는지에 대한 합의는 없으며, 이들 접근법 간의 직접 비교도 드물다.

**다지 데이터 수집은 공인된 병목이다.** 저비용 원격 조작 시스템(§10)의 증가 — DexCap, DOGlove, DEXOP, DEX-Mouse, 모두 2024-2026년 발표 — 는 커뮤니티가 데이터 수집을 주요 장애물로 보고 있음을 시사한다. 이러한 노력에도 불구하고, 대부분의 다지 데이터셋(§8.1)은 여전히 관절 위치와 시각 데이터만을 캡처하며, 힘/토크 모달리티는 거의 전적으로 그리퍼 기반 시스템(§8.2)에서만 사용 가능하다.

**다지 RL의 Sim-to-Real 전이는 성숙해지고 있다.** 여러 최근 논문이 다지 핸드에 대한 제로샷 또는 준제로샷 sim-to-real 전이를 시연한다: CrossDex (LEAP), RobustDexGrasp (Allegro, 94.6%), DeXtreme (Allegro), DQ-RISE (LEAP+Franka, 85.8%), HandelBot (양손 LEAP). 이는 시뮬레이션 학습 다지 정책이 실용적으로 배치 가능해지고 있음을 시사하며, 이 분야에서 시뮬레이션 기반 연구의 진입 장벽을 낮추고 있다.

**VLA 모델 계열은 여전히 그리퍼 중심이다.** 서베이된 pi(pi0~pi0.7)와 GR00T(N1~N1.7)의 모든 버전에서 독립형 다중 손가락 다지 핸드를 네이티브로 지원하는 버전은 없다(§6.1-6.2). GR00T-Dexterity는 Allegro 지원을 추가하지만, VLA 자체의 일부가 아닌 별도의 RL 워크플로우로서이다. 오픈소스 VLA 생태계(openpi, Isaac-GR00T, OpenVLA)는 아직 커뮤니티에 의해 다지 핸드 임바디먼트로 확장되지 않았다.

**모델 기반 접촉 제어는 상보적 축이다.** 접촉 내재 MPC와 미분 가능 접촉 모델(Contact Trust Region, Complementarity-Free, ComFree-Sim)은 접촉 풍부 다지 조작을 위한 학습된 임피던스의 대안을 제공한다. 최근 연구는 Allegro 및 LEAP 핸드에 대해 50-100 Hz의 실시간 MPC를 달성한다. 이러한 접근법은 학습된 정책이 일반적으로 결여하는 형식적 보장(예: 상보성 제약, 수동성)을 제공하지만, 정확한 동역학 모델을 요구하며 연성/변형 가능 접촉에서 어려움을 겪는다. 다지 핸드를 위해 모델 기반과 학습 기반 힘 제어를 어떻게 결합할 수 있는지 — 예: 모델 기반 내부 루프가 추적하는 학습된 임피던스 설정값 — 는 대체로 미탐구 상태이다.

---

## 14. 참고 링크

### 큐레이션된 목록
- [Awesome-Force-Tactile-VLA](https://github.com/OpenHelix-Team/Awesome-Force-Tactile-VLA) — 힘/촉각 VLA 논문 관리 목록

### 주요 GitHub 조직 / 프로젝트 페이지
- [Google DeepMind](https://deepmind.google/models/gemini-robotics/) — Gemini Robotics, Gemini Robotics-ER, RT-2
- [PKU-EPIC](https://github.com/PKU-EPIC) — DexGraspNet, UniDexGrasp, BODex, Dexonomy
- [PKU-RL](https://github.com/PKU-RL) — CrossDex, ResDex
- [NVlabs](https://github.com/NVlabs) — DextrAH, DexMimicGen, IndustReal, CHIP
- [UniDex-AI](https://github.com/unidex-ai) — UniDex-VLA
- [Physical-Intelligence](https://github.com/Physical-Intelligence) — openpi (pi0, pi0-FAST, pi0.5); pi0.6, pi0.7은 미공개
- [NVIDIA Isaac-GR00T](https://github.com/NVIDIA/Isaac-GR00T) — GR00T N1~N1.7
- [ForceMimic](https://github.com/ForceMimic) — ForceMimic, ForceCapture
- [Meta FAIR](https://github.com/facebookresearch) — SPIDER, TCDM, Sparsh, NeuralFeels
