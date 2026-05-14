# 7. 基于强化学习的灵巧操作

> **成功率可比性警告。** 7.1节中报告的成功率在不同论文之间**不可直接比较**。差异包括：(1) 仿真与真实世界评估，(2) 手部构型和自由度数量，(3) 物体集大小和组成，(4) 成功标准定义，(5) 状态估计方法（特权状态 vs 视觉 vs 点云）。比较仅应在共享相同评估协议的论文之间进行。

## 7.1 灵巧抓取

**本节论文：**
1. [CrossDex](crossdex.md) -- 跨构型灵巧抓取（6种手部，特征抓取动作空间）
2. [ResDex](resdex.md) -- 残差策略 + MoE 用于3200物体抓取
3. [UniDexGrasp](unidexgrasp.md) -- 首个通用灵巧抓取流程（3000+物体）
4. [UniDexGrasp++](unidexgrasp_pp.md) -- 基于UniDexGrasp的迭代通用-专用改进
5. [BODex](bodex.md) -- 跨手部抓取生成的双层优化（非RL）
6. [Dexonomy](dexonomy.md) -- 分类导向的抓取生成（31种抓取类型）
7. [UltraDexGrasp](ultradexgrasp.md) -- 超大规模跨构型抓取数据集（2000万帧）
8. [DexGrasp Anything](dexgrasp_anything.md) -- 基于扩散模型的通用抓取合成（15K+物体）
9. [DexGraspNet 2.0](dexgraspnet_2.md) -- 杂乱场景感知扩散抓取
10. [RobustDexGrasp](robustdexgrasp.md) -- 单视角点云抓取（真实世界94.6%）
11. [DextrAH-G/RGB](dextrah_g.md) -- 几何织物 + RL 用于臂手抓取

## 7.2 手内操作 / 重定向

**本节论文：**
12. [Hora](hora.md) -- 快速运动自适应用于手内旋转
13. [RotateIt](rotateit.md) -- 在Hora框架上添加触觉（DIGIT）
14. [AnyRotate](anyrotate.md) -- 扩展Hora/RotateIt的重力不变旋转
15. [Visual Dexterity](visual_dexterity.md) -- 使用深度传感的SO(3)重定向
16. [DeXtreme](dextreme.md) -- Allegro Hand的自动域随机化
17. [DexPBT](dexpbt.md) -- 臂手系统的基于种群训练
18. [SAPG](sapg.md) -- 高自由度操作的分裂合并策略梯度
19. [DexHandDiff](dexhanddiff.md) -- 交互感知扩散规划

## 7.3 长时域 / 多阶段 / 接触丰富

**本节论文：**
20. [SeqDex](seqdex.md) -- 长时域任务的顺序子策略链接
21. [Bi-DexHands](bi_dexhands.md) -- 双手灵巧操作基准（16+任务）
22. [DexArt](dexart.md) -- 铰接物体操作基准
23. [TCDM](tcdm.md) -- 动作捕捉引导的多任务灵巧操作基准（50个任务）
24. [VTDexManip](vtdexmanip.md) -- 视觉-触觉灵巧操作数据集
25. [DexGarmentLab](dexgarmentlab.md) -- 灵巧服装操作基准

### 基于模型的MPC（非RL）

26. [Contact Trust Region](contact_trust_region.md) -- 带信赖域的接触隐式MPC
27. [Complementarity-Free](complementarity_free.md) -- 可微分柔性接触仿真
28. [ComFree-Sim](comfree_sim.md) -- GPU并行无互补性接触仿真

## 7.4 其他近期RL工作

**本节论文：**
29. [DQ-RISE](dq_rise.md) -- 准静态手内操作的仿真到真实迁移
30. [DexTrack](dextrack.md) -- 人手动作的神经追踪
31. [BiDexHD](bidexhd.md) -- 基于人类演示的双手灵巧操作（141个任务）
32. [RoboPianist](robopianist.md) -- 钢琴演奏基准（150首曲目，仅仿真）
33. [HandelBot](handelbot.md) -- 使用LEAP Hand的真实世界双手钢琴演奏
34. [DexDrummer](dexdrummer.md) -- 带工具抓取的打鼓（仅仿真）
35. [DemoStart](demostart.md) -- 演示引导的真实世界RL
36. [Closing Reality Gap](closing_reality_gap.md) -- 力控灵巧抓取
37. [Maniwhere](maniwhere.md) -- 视觉可泛化的灵巧操作

---

### 跨领域观察

**灵巧抓取正在向扩散和优化方法收敛。** 最新的抓取工作（DexGrasp Anything、DexGraspNet 2.0、BODex、Dexonomy）已从端到端RL转向基于扩散的生成模型和双层优化的抓取姿态合成。这反映出抓取生成本质上是一个结构化预测问题，其中有效抓取的多模态分布由生成模型比判别式RL策略更好地捕获。基于PPO的方法（UniDexGrasp、ResDex、RobustDexGrasp）在闭环执行方面仍具竞争力，但越来越多地用作执行后端而非抓取合成方法。

**PKU-EPIC流程主导灵巧抓取。** 11篇抓取论文中有7篇（UniDexGrasp、UniDexGrasp++、BODex、DexGraspNet 2.0、Dexonomy、UltraDexGrasp以及部分DexGrasp Anything）共享作者或直接构建在PKU-EPIC抓取生成流程之上。这形成了连贯的进展（UniDexGrasp -> UniDexGrasp++ -> BODex -> Dexonomy -> UltraDexGrasp），但也意味着文献可能过拟合于该流程的假设（Shadow Hand作为默认、cuRobo用于逆运动学、IsaacGym用于验证）。

**手内操作在物体多样性和真实世界规模上落后于抓取。** 抓取论文通常在数千个物体上评估（ResDex 3200、Dexonomy 10.7K、DexGrasp Anything 15K+），而手内操作论文通常在数十个物体上评估。这一差距反映了更困难的探索问题：手内操作需要持续的多接触协调，使得在数千个物体上训练不可行，除非使用课程学习或分解策略。

**触觉传感正在成为手内操作的关键，但在抓取中缺失。** RotateIt、AnyRotate及更广泛的趋势表明，触觉反馈显著提高了手内操作的鲁棒性，特别是在重力下检测滑动和维持接触方面。相比之下，11篇抓取论文均未使用触觉传感，而是依赖本体感觉和视觉。这表明一个空白：不确定条件下（可变形物体、不确定摩擦）的鲁棒抓取可能会从触觉反馈中受益。

**仿真到真实的成功率在两个子任务间差异显著。** 对于抓取，真实世界成功率高且持续上升（RobustDexGrasp 94.6%、DexGraspNet 2.0 90.7%）。对于手内操作，真实世界成功更难量化（连续旋转任务以持续旋转时间衡量，而非离散成功率）。抓取的仿真到真实问题可以说更简单，因为抓取是准静态事件，而手内操作需要连续的动态控制。

**Shadow Hand主导仿真；Allegro主导真实世界。** 在抓取文献中，11篇论文中有8篇在仿真中使用Shadow Hand（24自由度）。在真实世界部署中，Allegro Hand（16自由度）是最常见的选择（RobustDexGrasp、DextrAH-G以及除Visual Dexterity的D'Claw外的所有手内操作真实世界结果）。这反映了Shadow Hand作为高自由度仿真标准与Allegro在实际优势（商业可用、硬件稳健、良好SDK）之间的角色差异。跨构型方法（CrossDex、BODex、Dexonomy）正在开始弥合这一差距。

**单轴旋转与完整SE(3)重定向仍是前沿。** 大多数手内操作论文（Hora、RotateIt、AnyRotate、DeXtreme）聚焦于单轴旋转。Visual Dexterity因实现SO(3)重定向而突出，但使用的是更简单的三指手（D'Claw）。在五指手上实现完整SO(3)或SE(3)重定向并进行仿真到真实迁移仍是一个开放挑战。

**没有手内操作工作同时结合视觉、触觉和力控。** 每篇手内操作论文最多使用两种感知模态：本体感觉 + 视觉（Visual Dexterity、DeXtreme），或本体感觉 + 触觉（RotateIt、AnyRotate）。在所调研的文献中，没有工作将三者结合用于灵巧手内操作，尽管有证据表明每种模态提供互补信息（视觉用于全局姿态、触觉用于接触状态、力用于交互动力学）。

**从单任务到多任务规模。** 任务集大小有明确的进展：从SeqDex的单链式任务（2023）到Bi-DexHands的16+任务（2022）到TCDM的50个任务（2023）到BiDexHD的141个任务（2025）。这种扩展得益于GPU并行仿真（主要是IsaacGym）和利用人类动作捕捉数据进行探索引导。

**接触隐式优化 vs. RL。** 7.3节包含两种不同范式：基于学习的RL方法（SeqDex、Bi-DexHands、DexArt、TCDM、VTDexManip、DexGarmentLab）和基于优化的接触隐式MPC（Contact Trust Region、Complementarity-Free、ComFree-Sim）。优化方法提供物理一致性和约束满足，但需要精确模型且难以扩展到多样物体。RL方法扩展性更好，但在物理一致性方面提供更少的保证。

**仿真到真实差距仍然是主要瓶颈。** 在7.3--7.4节的18篇论文中，仅有5篇展示了仿真到真实迁移（SeqDex、DQ-RISE、HandelBot、DemoStart、Maniwhere）。大多数仍停留在仿真层面。DemoStart采取了替代方法——真实世界RL，完全避免了仿真到真实差距，但需要带有自动重置的定制硬件。

**乐器演奏作为接触丰富基准。** RoboPianist、HandelBot和DexDrummer使用音乐表演作为接触丰富双手协调的测试平台。这些任务提供自然的、可量化的成功指标（音符准确性、节拍），并需要快速、精确的接触事件——使其成为引人注目的基准，尽管其应用领域较为特定。

**力感知仍然罕见。** 在所有论文中，只有DQ-RISE和"Closing Reality Gap"明确涉及力控操作。绝大多数训练位置控制策略，即使是接触丰富的任务。VTDexManip包含二值触觉传感但不包含连续力反馈。

**人类演示作为探索先验。** TCDM、DexTrack、BiDexHD和DemoStart都使用人类演示（动作捕捉或遥操作）来引导RL探索。这正在成为将灵巧RL扩展到复杂任务的主导策略，解决了高自由度操作的根本探索挑战。
