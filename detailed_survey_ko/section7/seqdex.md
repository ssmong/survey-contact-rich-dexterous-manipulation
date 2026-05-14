### 7.3 SeqDex

**전체 제목:** Sequential Dexterity: Chaining Dexterous Policies for Long-Horizon Manipulation

**저자:** Yuanpei Chen, Chen Wang, Li Fei-Fei, C. Karen Liu

**학회/연도:** CoRL 2023

**arXiv:** https://arxiv.org/abs/2309.00987

**RL 알고리즘:** PPO with teacher-student distillation. Each sub-policy is trained independently with privileged state access (teacher), then distilled to a vision-based student policy. Policies are chained via learned transition conditions.

**핸드 하드웨어:** Allegro Hand (16 DoF) mounted on a Kuka arm

**시뮬레이션 플랫폼:** IsaacGym (NVIDIA)

**Sim2Real 여부:** Yes. Sim-to-real transfer demonstrated via domain randomization and teacher-student distillation from privileged state to point-cloud observations (real).

**작업:** Long-horizon sequential manipulation decomposed into stages: search (locate object) -> orient (rotate to desired pose) -> grasp (acquire stable grasp) -> insert (place into slot). The full chain executes autonomously with learned transition triggers between sub-policies.

**핵심 방법론:** SeqDex decomposes long-horizon dexterous tasks into a sequence of shorter-horizon sub-policies, each independently trained with RL. A key innovation is the automatic chaining mechanism that uses learned binary classifiers to detect when one phase has succeeded and the next should begin, avoiding manual thresholds or state machines. Teacher policies use privileged simulation state; student policies operate from 3D point clouds.

**주요 기여:**
- Demonstrated that chaining independently trained RL sub-policies with learned transition conditions enables long-horizon dexterous manipulation that monolithic policies fail to learn
- Achieved sim-to-real transfer of the full multi-stage pipeline (search-orient-grasp-insert) on an Allegro+Kuka system (real)
- Provided a general framework for decomposing complex dexterous tasks into learnable sub-problems

**한계점:** Task decomposition is manual and requires domain knowledge to define sub-task boundaries. The approach has been demonstrated on a single task family (object insertion); generalization to diverse long-horizon tasks is untested. No force/tactile sensing is used.

**결과:** Successfully completed the full search-orient-grasp-insert chain in real-world experiments (real). Code and pretrained weights publicly available.

## 추론 / 배포

- **추론 지연 시간:** Not explicitly reported. Each sub-policy (MLP) runs in <1ms per forward pass. Phase transition classifiers add negligible overhead. Total pipeline is real-time.
- **배포 하드웨어:** Allegro Hand (16 DoF) + Kuka arm. Policies trained in IsaacGym; deployed via zero-shot sim-to-real transfer.
- **실시간 가능 여부:** Yes. Chained MLP sub-policies support real-time dexterous manipulation on real hardware.

## 데이터셋 / 데이터 수집

- **사용 데이터셋:** No pre-collected dataset. Pure RL (PPO) with teacher-student distillation for each sub-policy -- all data generated in simulation.
- **수집 방법:** Pure RL in IsaacGym. Each sub-policy (search, orient, grasp, insert) trained independently with privileged state (teacher), then distilled to point-cloud-based student via domain randomization. Learned binary classifiers detect phase transitions. Sim-to-real transfer on Allegro + Kuka.
- **데이터 규모:** Standard parallel RL training in IsaacGym per sub-policy.
- **원격 조작 장비:** Not applicable (pure RL, no demonstrations).
- **데이터 포맷:** Not applicable (online RL, no offline dataset).
- **공개 여부:** Yes -- code and pretrained weights publicly available.
