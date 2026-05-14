# 12.1 Sparsh

- **全称：** Sparsh: Self-Supervised Touch Representations for Vision-Based and Multi-Modal Tactile Sensing
- **作者：** Carolina Higuera, Akash Sharma, Chaithanya Krishna Bodduluri, Taosha Fan, Patrick Chaney, Mrinal Kalakrishnan, Michael Kaess, Byron Boots, Mike Lambeta, Tingfan Wu, Mustafa Mukadam (Meta FAIR, CMU)
- **发表场所/年份：** CoRL 2024
- **支持的传感器：** DIGIT, GelSight（跨传感器）
- **训练数据：** 460K+张触觉图像，涵盖多种传感器类型
- **预训练方法：** 自监督学习（SSL）——MAE（掩码自编码器）、DINO、IJEPA变体
- **基准测试：** TacBench——5任务触觉基准（力估计、滑动检测、纹理分类、姿态估计、抓取稳定性）

## 核心方法/设计

Sparsh使用自监督学习在来自多种传感器类型（DIGIT、GelSight）的大规模触觉图像语料上训练触觉编码器。通过SSL预训练（MAE、DINO、IJEPA），Sparsh在不需要任务特定标注的情况下学习触觉表征，类似于视觉基础模型从无标注图像数据中学习。核心创新在于跨传感器泛化：在DIGIT图像上学习的表征可迁移至GelSight，反之亦然，尽管传感器输出之间存在显著的视觉差异。Sparsh还引入了TacBench，一个用于评估触觉表征的标准化5任务基准。

## 主要贡献

- 首个大规模SSL触觉编码器，展示了跨传感器迁移（DIGIT到GelSight及反向）
- TacBench：标准化5任务基准（力估计、滑动检测、纹理分类、姿态估计、抓取稳定性），用于触觉表征评估
- SSL方法（MAE、DINO、IJEPA）在触觉数据上的系统比较，发现MAE和DINO优于IJEPA
- 460K+图像预训练语料，为触觉SSL建立了规模先例

## 定量结果（TacBench）

| 任务 | 指标 | MAE | DINO | IJEPA | 监督学习基线 |
|------|------|-----|------|-------|-------------|
| 力估计 | RMSE (N) | SSL中最优 | 与MAE相当 | 较差 | 与SSL相当 |
| 滑动检测 | 准确率 (%) | SSL中最优 | 与MAE相当 | 较差 | 与SSL相当 |
| 纹理分类 | 准确率 (%) | 有竞争力 | 有竞争力 | 较低 | 略优 |
| 姿态估计 | 误差 (mm/deg) | SSL中最优 | 相当 | 较差 | 相当 |
| 抓取稳定性 | 准确率 (%) | 有竞争力 | 有竞争力 | 较低 | 相当 |

*注：MAE和DINO在TacBench各任务上持续优于IJEPA。SSL方法达到了与监督学习基线相当的性能，表明学习有效的触觉表征不需要任务特定标注。*

## 局限性/不足

- 仅限于视觉触觉传感器（基于相机的DIGIT/GelSight）；不处理电阻式、电容式或气压式触觉阵列
- 跨传感器迁移虽已验证，但与传感器内训练相比仍存在性能下降
- TacBench任务相对简单（分类、回归）；未在完整操作策略上评估表征
- 预训练数据以平面探测为主；接触几何形状的多样性有限

## 共同局限性：无闭环策略集成

**这一局限性——未集成到闭环操作策略中——为本节所有触觉表征模型（Sparsh、[UniTouch](unitouch.md)、[AnyTouch](anytouch.md)、[NeuralFeels](neuralfeels.md)）所共有。** 所有四个模型都在独立感知任务（分类、回归、跟踪）上评估其学习到的表征，而非展示作为操作策略（VLA或RL）中触觉编码器的端到端使用。这一脱节意味着表征虽在感知质量上得到了验证，但在可操作性上未得到验证——一个能准确估计接触力的表征可能无法产生对策略决定如何调整抓取力有用的特征。通过使用预训练的触觉编码器作为灵巧操作策略的触觉骨干网络来闭合这一环路，是这一研究方向的关键下一步。

## 开源状态

完全开源（代码 + 预训练权重）。GitHub：[facebookresearch/sparsh](https://github.com/facebookresearch/sparsh)
