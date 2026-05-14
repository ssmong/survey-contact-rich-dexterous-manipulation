# 12.4 NeuralFeels

- **全称：** NeuralFeels: Neural Field Methods for Tactile-Visual Object State Tracking
- **作者：** Suddhu Sudharshan, Haozhi Qi, Pieter Abbeel, Jitendra Malik, Roberto Calandra, Michael Kaess及合作者 (Meta FAIR, CMU, Berkeley)
- **发表场所/年份：** Science Robotics, 2024
- **硬件：** Allegro Hand（16自由度）+ DIGIT触觉传感器（4个指尖）
- **方法：** 神经辐射场（NeRF风格），融合触觉和视觉观测
- **任务：** 操作过程中的手内物体姿态和形状跟踪

## 核心方法/设计

NeuralFeels将神经场方法（NeRF启发）应用于灵巧手内操作过程中的物体状态跟踪问题。系统融合来自外部相机的视觉观测和安装在Allegro Hand指尖上的DIGIT传感器的触觉图像。神经场表示物体的形状和外观，并在手操作物体时持续更新。触觉观测提供局部接触几何信息以消解视觉歧义（如手指遮挡物体时），而视觉观测提供全局形状上下文。这种融合即使在物体被严重遮挡的复杂手内操作中也能实现准确的6自由度姿态跟踪。

## 主要贡献

- 首个用于灵巧手内操作实时触觉-视觉物体跟踪的神经场方法
- 在真实的Allegro Hand + DIGIT硬件上进行了多样物体的手内操作验证
- 通过共享的神经场表征实现触觉（局部接触几何）和视觉（全局形状）观测的有原则融合
- 发表于Science Robotics，代表了该研究方向的最高影响力发表场所之一

## 定量结果（姿态跟踪）

| 物体类别 | 姿态误差（平移，mm） | 姿态误差（旋转，deg） | 纯视觉基线 | 纯触觉基线 |
|----------|---------------------|---------------------|-----------|-----------|
| 简单几何体 | 低 | 低 | 较高（遮挡误差） | 较高（无全局上下文） |
| 复杂/有纹理物体 | 低 | 低 | 中等 | 较高 |
| 严重遮挡场景 | 低（触觉消解遮挡） | 低 | 显著更差 | 相当 |

*注：精确数值见Science Robotics论文。核心发现是触觉-视觉融合始终优于任何单一模态，在视觉单独使用会失败的严重遮挡场景中增益最大。神经场表征实现了跨接触状态变化的连续跟踪。*

## 局限性/不足

- 需要已知的物体3D模型进行初始化；不适用于无先验形状信息的新物体
- 神经场优化计算量大；实时性能需要大量GPU资源
- 仅提供跟踪（状态估计）；不闭合环路生成操作动作
- 仅限于Allegro Hand上的DIGIT传感器；未验证对其他传感器-手组合的泛化能力
- 每个物体的神经场需要为每个新物体重新训练

## 共同局限性

与本节所有触觉表征模型一样，NeuralFeels未集成到生成动作的闭环操作策略中。它提供的是状态估计（姿态跟踪）而非动作生成。详见[Sparsh](sparsh.md#shared-limitation-no-closed-loop-policy-integration)中对此共同局限性的详细讨论。NeuralFeels通过在主动操作期间运行于真实灵巧手硬件上，在四个模型中最接近于闭合这一环路，但跟踪输出仍需由单独的策略消费以完成感知-行动循环。

## 开源状态

开源。GitHub：[facebookresearch/neuralfeels](https://github.com/facebookresearch/neuralfeels)
