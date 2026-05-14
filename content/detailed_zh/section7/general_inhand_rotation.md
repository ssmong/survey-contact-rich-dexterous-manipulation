### 7.2 General In-Hand Object Rotation with Vision and Touch

**完整标题：** General In-Hand Object Rotation with Vision and Touch

**作者：** Haozhi Qi, Brent Yi, Sudharshan Suresh, Mike Lambeta, Yi Ma, Roberto Calandra, Jitendra Malik

**发表venue/年份：** CoRL 2023

**arXiv：** https://arxiv.org/abs/2309.09979

**RL算法：** PPO + 教师-学生蒸馏和用于多模态融合的视触觉Transformer。教师可访问真值物体状态；学生使用视觉和触觉。

**手部硬件：** Allegro Hand（16自由度）+ 指尖DIGIT触觉传感器

**仿真平台：** IsaacGym

**仿真到真实？** 是。零样本仿真到真实迁移。在仿真中使用特权状态训练，然后蒸馏为使用真实传感模态（RGB视觉 + DIGIT触觉图像）的策略。视触觉Transformer在部署期间在线推断物体形状和物理属性。

**任务：** 多轴指尖手内物体旋转。围绕多个轴旋转物体（不限于如先前工作Hora的单轴）。在多样物体上测试。

**核心方法论：** 通过视触觉Transformer架构融合视觉和触觉来扩展Hora/RotateIt系列工作。系统在仿真中以真值物体状态训练，然后使用蒸馏过程迁移到使用真实噪声感官输入（RGB图像 + DIGIT触觉读数）操作的策略。Transformer架构融合多模态信息以隐式在线推断物体形状和物理属性，实现对未见物体的泛化。实现了结合视觉和触觉的通用多轴手内旋转。

**主要贡献：**
- 首个结合视觉和触觉传感用于多轴手内旋转并带仿真到真实迁移的学习策略
- 融合RGB和触觉模态进行隐式物体属性推断的视触觉Transformer架构
- 展示相比仅视觉和仅触觉基线的提升，证明多模态传感的互补优势
- 使用真实传感器仿真（DIGIT触觉 + RGB）的零样本仿真到真实迁移

**定量结果：**

| 指标 | 数值 |
|---|---|
| 多轴旋转 | 是（相比单轴Hora的提升） |
| 传感器融合 | 视觉（RGB）+ 触觉（DIGIT） |
| 基线提升 | 优于仅视觉和仅触觉变体 |
| 手部 | Allegro（16自由度）+ DIGIT传感器 |
| 真实世界迁移 | 零样本仿真到真实 |

**局限性/差距：**
- **力控：** DIGIT提供触觉图像，非显式力向量；无阻抗控制
- **VLA/语言：** 无语言条件或VLA集成
- **仿真到真实：** 触觉仿真保真度（仿真中DIGIT图像渲染）仍是挑战；二值接触可能迁移更好
- **代码：** 属于Hora代码库生态系统；具体代码发布状态不一
- **任务范围：** 聚焦旋转；不涉及抓取、工具使用或功能性操作

## 推理 / 部署

- **推理延迟：** 未明确报告。带DIGIT触觉编码器的视触觉Transformer相比纯MLP策略增加开销，但应在桌面GPU上以~20-50 Hz运行。
- **部署硬件：** Allegro Hand（16自由度）+ 指尖DIGIT触觉传感器。策略在IsaacGym中训练；通过零样本仿真到真实迁移部署。
- **支持实时？** 是。在真实Allegro Hand上使用视触觉输入展示了实时手内旋转。
