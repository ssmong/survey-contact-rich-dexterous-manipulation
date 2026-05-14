# 4. VLM引导的阻抗控制

VLM/LLM为底层控制器生成或检索阻抗参数（K, D）的系统。这些方法利用大型视觉语言模型来弥合高级语义场景理解与底层柔顺性调节之间的差距，从而消除手动调节阻抗参数的需求。

**本节论文：**
1. [CompliantVLA-adaptor](compliantvla_adaptor.md) — VLM零样本阻抗生成，用于冻结的VLA
2. [OmniVIC](omnivic.md) — VLM + 自改进RAG实现全向阻抗控制
3. [HumanoidVLM](humanoidvlm.md) — 用于人形机器人pHRI的开放权重VLM阻抗控制
4. [SafeHumanoid](safehumanoid.md) — 用于人形机器人pHRI的安全约束VLM阻抗控制
5. [ImpedanceGPT](impedancegpt.md) — 用于无人机集群编队的VLM阻抗控制（超出范围的对比）

---

### 横向观察

**1. 统一依赖VLM零样本或基于RAG的推理。** 所有五篇论文均使用VLM通过提示（零样本或通过RAG的少样本）生成阻抗参数，而非训练神经网络来预测阻抗。这使得这些系统无需训练或几乎无需训练，但阻抗质量受限于VLM的推理能力和RAG数据库的质量。这些系统均未从演示数据或强化学习中学习阻抗。

**2. 不支持灵巧手。** 本节中的每个系统都在平行夹爪（Franka Panda）、带简单集成夹爪的人形机器人（Unitree G1）或非操作平台（无人机集群）上运行。没有任何系统涉及多指阻抗控制，而多指阻抗控制需要生成逐指或逐关节的刚度/阻尼矩阵——其输出维度远高于这些系统产生的6D笛卡尔参数。

**3. 任务级而非连续阻抗自适应。** 所有系统在任务或阶段级别生成阻抗参数（例如，"对于插入操作，使用Kz=500, Dz=20"），而非在接触过程中持续调整。VLM推理延迟（约100ms-1s）将阻抗更新限制在约1-10 Hz，比实时阻抗控制器所需的100-1000 Hz低三个数量级。这是VLM在环方法的根本性架构限制。

**4. IIT Genoa / TU Darmstadt团队占主导地位。** CompliantVLA-adaptor和OmniVIC共享作者，代表同一团队不断演进的研究路线，OmniVIC在基础VLM提示方法上增加了自改进RAG。HumanoidVLM和SafeHumanoid构成另一对来自同一团队的论文。该领域规模较小且高度集中。

**5. 开放权重与商业VLM。** CompliantVLA-adaptor和OmniVIC依赖GPT-4o-mini（商业API），而HumanoidVLM、SafeHumanoid和ImpedanceGPT使用Molmo（开放权重）。开放权重方法支持设备端部署和可复现性，但可能在推理质量上逊于更大的商业模型。

**6. 无正式稳定性保证（SafeHumanoid可能除外）。** VLM生成的阻抗参数本身不保证产生稳定的闭环行为。如果VLM生成过高的刚度或不匹配的K/D比率，系统可能变得不稳定或产生振荡。只有SafeHumanoid明确涉及安全约束，但其正式保证的细节有限。

**7. 差距：用于灵巧手的VLM引导阻抗控制。** VLM引导阻抗控制与多指灵巧手的交叉领域完全未被探索。一个使用VLM推理为Shadow或Allegro手在接触丰富操作中生成逐指柔顺性配置的系统（例如，在抓取易碎物体与刚性物体时调整指尖刚度），将填补VLM引导阻抗和灵巧操作文献中的明确空白。
