### 2.6 HumanoidGen

**全称：** HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning

**作者：** Zhi Jing, Siyuan Yang, Jicong Ao, Ting Xiao, Yu-Gang Jiang, Chenjia Bai

**发表venue/年份：** NeurIPS 2025

**arXiv：** [2507.00833](https://arxiv.org/abs/2507.00833)（注：此前引用为2505.14680，该编号指向一篇不相关的论文）

**手部硬件：** Unitree H1-2 人形机器人，配备 Inspire 灵巧手（每手6自由度，每臂7自由度；总动作空间26维）。Inspire 手为多指灵巧手，确认归入灵巧操作章节。

**任务：**
- 20项桌面操作任务
- 双臂协调任务
- 长时间序列多步操作
- 人形本体背景下需要灵巧手-物体交互的任务

**核心方法：** HumanoidGen 使用大语言模型（LLM）作为任务规划器，结合蒙特卡洛树搜索（MCTS）进行策略生成。LLM 将复杂操作指令分解为子任务序列，而 MCTS 探索可能的动作计划空间以找到高回报轨迹。扩散策略作为底层控制器，为人形机器人的手臂和手部生成连续动作。语言在规划层面用于指定和分解任务，LLM 提供关于操作策略的常识推理。

**架构/参数：**
- 高层规划器：LLM（摘要中未公开具体模型；用于任务分解和 MCTS 引导）
- 搜索：蒙特卡洛树搜索用于计划优化
- 底层控制器：扩散策略用于连续动作生成
- 目标平台：Unitree H1_2 人形机器人
- 模型和数据权重在 HuggingFace 上提供

**主要贡献：**
- LLM 引导的 MCTS 框架用于生成多样化操作策略，结合 LLM 的常识推理能力与 MCTS 的系统性探索
- 在完整人形平台上演示了20项桌面任务，包括双臂和长时间序列操作
- 该框架为同一任务生成多样化的策略解决方案，通过解决方案多样性提升鲁棒性

**局限性/不足：**
- 仅限人形集成手部；未涉及独立灵巧手平台（Allegro、Shadow、LEAP）
- 无力或阻抗输出；扩散策略生成位置目标
- LLM 规划器在任务分解层面运作，而非精细手指控制层面
- MCTS 探索对实时应用可能计算开销较大
- 评估主要集中在桌面操作；未涵盖工具使用或高度接触密集型任务

**结果：**

**MCTS 有效性（数据生成成功率）：**

| 任务 | 无 MCTS | MCTS | MCTS 迭代次数 (N) |
|---|---|---|---|
| Block Stack Single | 63.3 +/- 6.2% | 98.3 +/- 2.4% | N=2 |
| Blocks Stack Easy | 46.7 +/- 2.4% | 95.0 +/- 4.1% | N=3 |
| Blocks Stack Hard | 18.3 +/- 6.2% | 98.3 +/- 2.4% | N=12 |
| Pyramid Stack | 13.3 +/- 6.2% | 90.0 +/- 4.1% | N=12 |

MCTS 相比无 MCTS 基线，成功率提升35--77个百分点。

**策略学习结果（DP3 vs DP，部分任务，不同演示数量）：**

| 任务 | 策略 | 20个演示 | 50个演示 | 100个演示 |
|---|---|---|---|---|
| Blocks Stack Easy | DP3 | 0.0% | 0.0% | 22.8 +/- 16.5% |
| Blocks Stack Easy | DP | 0.0% | 0.0% | 0.0% |
| Cup Pour Easy | DP3 | 67.8 +/- 10.8% | 75.6 +/- 9.6% | 72.2 +/- 7.9% |
| Cup Pour Easy | DP | 0.0% | 2.2 +/- 6.3% | 0.0% |
| Open Box Easy | DP3 | 85.6 +/- 8.0% | 95.6 +/- 4.4% | 95.0 +/- 4.1% |
| Open Box Easy | DP | 93.3 +/- 13.3% | 100.0% | 100.0% |
| Open Box Hard | DP3 | 95.6 +/- 5.5% | 96.1 +/- 4.6% | 98.3 +/- 3.3% |
| Open Box Hard | DP | 11.1 +/- 19.1% | 93.3 +/- 9.4% | 100.0% |
| Open Drawer | DP3 | 58.3 +/- 8.3% | 76.0 +/- 13.1% | 84.4 +/- 11.3% |
| Open Drawer | DP | 17.8 +/- 22.0% | 13.3 +/- 18.9% | 48.9 +/- 31.4% |
| Close Box Hard | DP3 | 88.9 +/- 17.6% | 96.3 +/- 6.9% | 96.3 +/- 6.9% |
| Close Laptop Easy | DP3 | 100.0% | 100.0% | 100.0% |

完整基准（HGen-Bench）中共14项任务在所有条件下进行了评估。DP3 总体优于 DP，尤其在灵巧任务上。所有任务的平均成功率超过50%。

- 模型和数据在 HuggingFace 上发布
- 代码发布于 [GitHub](https://github.com/TeleHuman/HumanoidGen)
- 项目页面：[openhumanoidgen.github.io](https://openhumanoidgen.github.io)

## 推理 / 部署

- **推理延迟：** 论文（arXiv 2507.00833）中未报告。
- **部署硬件：** Unitree H1_2 人形机器人平台。训练/推理 GPU 未指定。
- **是否支持实时？** 未验证。基于 MCTS 的规划可能在推理时引入计算开销，但具体延迟数据不可用。

## 数据集 / 数据采集

- **使用的数据集：** 自定义仿真生成数据集。在 HuggingFace 上提供（`TeleEmbodied/humanoidgen_dataset`）。
- **采集方法：** 使用 ManiSkill 平台的基于仿真的数据生成。通过启用 `record_data` 运行任务求解器脚本，为20项桌面操作任务生成演示轨迹。
- **数据规模：** 未明确报告。HuggingFace 数据集仓库存在，但具体回合/轨迹数量在公开文档中未披露。
- **遥操作设备：** 不适用（仿真生成数据）。真实世界部署使用 Unitree H1_2 人形机器人。
- **数据格式：** 以 pickle 格式采集，然后通过 `pkl2zarr.py` 转换为 zarr 格式用于策略训练。
- **是否公开可用？** 是。数据集在 HuggingFace 上（`TeleEmbodied/humanoidgen_dataset`）。模型在 HuggingFace 上（`TeleEmbodied/humanoidgen_model`）。代码位于 [GitHub](https://github.com/TeleHuman/HumanoidGen)。注：场景生成和额外任务生成代码尚未发布。
