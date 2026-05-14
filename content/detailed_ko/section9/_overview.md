# Section 9: 시뮬레이션 벤치마크 및 플랫폼

시뮬레이션 환경은 dexterous 조작 연구의 기반 인프라이다. 대규모 병렬 RL 학습, 안전한 policy 평가, sim-to-real transfer 파이프라인을 가능하게 한다. 본 섹션에서는 multi-finger hand 조작을 구체적으로 지원하거나 dexterous 작업과 관련된 미분 가능 접촉 물리를 제공하는 플랫폼을 조사한다.

## 항목

| 항목 | 플랫폼 | Dexterous 지원 | 핵심 강점 |
|------|--------|----------------|-----------|
| [ManiSkill3](maniskill3.md) | SAPIEN / PhysX 5 | Allegro, DClaw, 임의 URDF | GPU 병렬 속도 (430x), 통합 RL/IL/VLA baseline |
| [MuJoCo Playground](mujoco_playground.md) | MuJoCo MJX (JAX) | LEAP Hand, Shadow Hand | 수 분 단위 학습, zero-shot sim-to-real |
| [MuJoCo Manipulus](mujoco_manipulus.md) | MuJoCo | Multi-finger 도구 조작 | 최초의 전용 dexterous 도구 사용 벤치마크 (16개 작업) |
| [Adroit](adroit.md) | MuJoCo | Shadow Hand (24 DoF) | 표준 RL 벤치마크 (pen, door, hammer, ball) |
| [Genesis](genesis.md) | Custom multi-physics | 임의 URDF | 통합 multi-physics (6개 solver), 43M+ FPS |
| [DiffTactile](difftactile.md) | Custom differentiable | Parallel-jaw만 해당 | 미분 가능 FEM 기반 tactile 시뮬레이션 |
| [TeleOpBench](teleopbench.md) | Isaac Sim | 3개 humanoid embodiment | 최초의 양팔 dexterous 원격조작 벤치마크 (30개 작업) |
| [Isaac Lab](isaac_lab.md) | Isaac Sim (PhysX 5) | Allegro, Shadow, 임의 URDF | IsaacGym 후속; GPU 병렬, RTX 렌더링, 모듈식 API |
| [TACTO](tacto.md) | PyBullet + PyRender | Gripper (DIGIT/GelSight 센서 시뮬레이션) | 비전 기반 tactile 센서 이미지 시뮬레이션 |

## 관찰 사항

dexterous 조작을 위한 시뮬레이션 환경은 세 가지 축을 따라 분화되고 있다: (1) **속도** -- GPU 병렬 엔진 (ManiSkill3, MuJoCo Playground, Genesis)이 현재 수 분 만에 policy를 학습시킴; (2) **물리 충실도** -- 미분 가능 엔진 (Genesis, DiffTactile)이 접촉을 통한 gradient 기반 최적화를 가능하게 함; (3) **작업 커버리지** -- 특화 벤치마크 (도구 사용을 위한 Manipulus, 원격조작을 위한 TeleOpBench, RL baseline을 위한 Adroit)가 특정 역량 격차를 목표로 함. GPU 병렬 속도, 미분 가능 접촉 물리, 고충실도 tactile 시뮬레이션, 포괄적인 dexterous 작업 suite를 동시에 결합한 단일 플랫폼은 아직 없다. DiffTactile은 가장 상세한 tactile 물리를 제공하지만 GPU 병렬성이 부족하고; ManiSkill3는 최고의 병렬 RL 인프라를 제공하지만 tactile 지원이 미미하다. Genesis는 통합을 목표로 하지만 아직 성숙 단계이다. Adroit는 거의 10년이 된 벤치마크임에도 여전히 기본 RL 평가 대상으로 남아 있으며, 이는 표준화된 벤치마크의 가치와 더 새로운 플랫폼으로의 커뮤니티 이전이 느리다는 것을 동시에 보여준다.
