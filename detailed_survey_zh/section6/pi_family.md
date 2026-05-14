## 6.1 Physical Intelligence pi系列

### pi0 / pi0-FAST / pi0.5 / pi0.6 / pi0.7

**完整标题：** pi0: A Vision-Language-Action Flow Model for General Robot Control（初始论文）；后续版本以技术报告或博客文章形式发布，无独立arXiv出版物。

**作者：** Physical Intelligence (Kevin Black, Noah Brown, Danny Driess, Adnan Esmail, Michael Equi, Chelsea Finn, Niccolo Fusai, Lachy Groom, Karol Hausman, Brian Ichter, Szymon Jakubczak, Tim Jones, Liyiming Ke, Sergey Levine, Adrian Li-Bell, Mohith Mothukuri, Suraj Nair, Karl Pertsch, Lucy Xiaoyang Shi, James Tanner, Quan Vuong, Anna Walling, Haohuan Wang, Ury Zhilinsky)

**发表期刊/年份：** pi0于2024年10月发布（arXiv 2410.24164）；pi0-FAST于2025年1月发布（arXiv 2501.13987）；pi0.5于2025年4月发布（技术报告）；pi0.6约2025年11月；pi0.7约2026年4月。

**架构：**

| 版本 | 日期 | 参数量 | VLM骨干网络 | 动作头 | 关键变化 |
|---|---|---|---|---|---|
| **pi0** | 2024年10月 | 3.3B | PaliGemma 3B (SigLIP ViT + Gemma 2B LM) | 流匹配（约300M参数） | 基于流匹配动作生成的基础VLA |
| **pi0-FAST** | 2025年1月 | 3.3B | PaliGemma 3B | 自回归 + FAST分词器 | 用离散动作token替换连续流头以加快推理速度 |
| **pi0.5** | 2025年4月 | 3.3B | PaliGemma 3B | 两阶段：FAST预训练 + 流匹配微调 | 知识隔离以实现更好的开放世界泛化；保留网络规模VLM知识 |
| **pi0.6** | 约2025年11月 | 约5B | Gemma 3 4B | 双流 + token头 | VLM骨干从PaliGemma升级到Gemma 3；更大容量 |
| **pi0.7** | 约2026年4月 | 约5B | Gemma 3 4B + 400M视觉编码器 | 流匹配（860M DiT） | 更大的专用DiT动作头；改进的视觉编码器 |

该架构在各版本间遵循一致的模式：预训练的视觉-语言模型处理多视角图像和可选的语言指令，产生上下文化嵌入来调节动作生成头。动作头在单次前向传播中去噪或解码未来动作块（通常16-50个时间步）。

**动作空间：** 所有版本为18-19维：双6自由度机械臂（位置+姿态）+ 夹爪宽度 + 可选移动底盘速度。所有版本仅使用平行爪夹爪。

**灵巧手支持？** ✗ --- 无任何版本支持多指灵巧手。动作表示专为双臂+夹爪设置设计。

**力/阻抗输出？** ✗ --- 所有版本仅输出位置目标。无力、力矩或阻抗参数。

**核心方法论：** pi0引入流匹配作为VLA的动作生成机制，将机器人动作预测视为条件去噪过程。VLM骨干与动作头在机器人演示数据上进行协同微调，使模型能够遵循自然语言指令同时生成精确的电机命令。pi0-FAST用自回归离散分词器（FAST）替换连续流头，将连续动作离散化到学习的词汇表中，以精度换取5-10倍的推理速度提升。pi0.5引入两阶段训练方案——先用FAST预训练以实现广泛覆盖，再用流匹配微调以提高精度——并采用"知识隔离"防止基础VLM的世界知识在机器人微调期间发生灾难性遗忘。

**训练数据：** 跨多种具身平台的10,000+小时机器人操作数据。预训练使用互联网规模的视觉-语言数据（继承自PaliGemma/Gemma）和跨具身机器人演示的混合数据。微调数据集包括DROID、ALOHA、Bridge V2和Physical Intelligence的专有数据。支持的机器人包括UR5、ALOHA双臂以及各种单臂平台。

**主要贡献：**
- 确立流匹配作为VLA可行的动作头，能够生成连续多模态动作分布，避免自回归token化的量化伪影。
- 证明了冻结VLM与轻量级动作头的协同微调，可以从相对适量的机器人数据中实现强大的语言条件化操作。
- 开源的openpi框架提供完整的微调和推理流程，使pi0/pi0-FAST/pi0.5可供学术研究使用。

**定量结果：**

*pi0 (arXiv 2410.24164):*

| 基准/任务 | pi0 | 最佳基线 | 备注 |
|---|---|---|---|
| *（结果未经独立验证——arXiv页面无法获取。请直接查阅论文获取DROID、ALOHA和Bridge V2基准上的逐任务成功率。）* | | | |

*pi0-FAST (arXiv 2501.13987):*

| 基准/任务 | pi0-FAST | pi0（流） | 备注 |
|---|---|---|---|
| *（结果未经独立验证——arXiv页面无法获取。论文报告在5-10倍更快推理速度下与pi0流匹配相当的成功率。请查阅论文获取逐任务数据。）* | | | |

**局限性/差距：**
- 严格仅限夹爪：18-19D动作空间无法表示多指手部配置。扩展到灵巧手需要对动作表示进行根本性改变。
- 无力或柔顺感知：所有输出均为位置目标，使模型不适用于需要力调节的接触丰富任务。
- pi0.6和pi0.7未公开发布；仅pi0、pi0-FAST和pi0.5开放权重。
- 训练数据主要来自平行爪夹爪演示，产生具身偏差，不利于向灵巧平台的适配。

**开放权重/代码：** ✅ pi0、pi0-FAST、pi0.5在Apache 2.0许可下通过[openpi](https://github.com/Physical-Intelligence/openpi)和[HuggingFace](https://huggingface.co/lerobot/pi0_base)提供。截至2026年5月，pi0.6和pi0.7未公开发布。

## 推理/部署

- **推理延迟：** pi0（流匹配）由于迭代去噪过程（每个动作块需要多次流匹配步骤），运行频率约为3-5 Hz。pi0-FAST通过用自回归FAST token解码替换流头，实现5-10倍更快的推理（约15-50 Hz），在单次前向传播中生成动作块。pi0.5使用流匹配微调后回到pi0级别的速度（约3-5 Hz）。具体的每步毫秒数未在标准化硬件上公开基准测试。
- **部署硬件：** 在桌面GPU上评估（具体型号未在公开材料中披露）。3.3B参数模型需要高性能GPU（如NVIDIA A100/RTX 4090级别）用于实时流匹配推理。pi0-FAST的离散token化更适合CPU/边缘设备。未报告Jetson Orin部署。
- **可实时运行？** pi0-FAST：是，约15-50 Hz加动作块化，适合典型操作控制频率。pi0（流匹配）：勉强，约3-5 Hz——足以应对慢速操作但对需要20+ Hz的灵巧任务来说太慢。动作块化（每次推理预测16-50个未来步骤）通过在推理间执行多个步骤来补偿低推理频率。

## 数据集/数据收集

- **使用的数据集：** 跨多种具身平台的10,000+小时机器人操作数据。预训练混合数据包括互联网规模的视觉-语言数据（继承自PaliGemma/Gemma）和跨具身机器人演示。微调数据集包括DROID（约76K轨迹，350小时）、ALOHA双臂演示、Bridge V2和Physical Intelligence专有数据。
- **收集方法：** 遥操作（各数据集采用不同设置：DROID使用VR控制器，ALOHA使用主从式，Bridge V2使用键盘/SpaceMouse）+ 网络规模视觉-语言预训练数据。支持的机器人包括UR5、ALOHA双臂和各种单臂平台。
- **数据规模：** 总计10,000+小时机器人数据。DROID：约76K轨迹/350小时/564个场景。Bridge V2：约60K轨迹/24个环境。另有Physical Intelligence专有数据。
- **遥操作设备：** 因数据集组件而异——Meta Quest VR控制器（DROID）、主从臂（ALOHA）、键盘/SpaceMouse（Bridge V2）。
- **数据格式：** RLDS（TensorFlow Datasets）用于OXE兼容数据集；Physical Intelligence数据使用专有格式。开源发布使用LeRobot格式。
- **是否公开？** 部分公开。DROID、Bridge V2和ALOHA数据集公开可用。Physical Intelligence专有数据未发布。pi0/pi0-FAST/pi0.5模型权重开放（Apache 2.0）。

---
