# 10.8 OmniH2O

- **全称：** OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning
- **作者：** Tairan He, Zhengyi Luo, Xialin He, Wenli Xiao, Chong Zhang, Weinan Zhang, Kris Kitani, Changliu Liu, Guanya Shi (CMU LeCAR Lab)
- **发表venue/年份：** CoRL 2024 (arXiv 2406.08858, 2024年6月)
- **输入模态：** 多模态——VR控制器、语音命令或RGB相机
- **目标手：** 人形机器人全身（包括手部）
- **力反馈：** 无
- **成本：** 因输入模态而异（RGB相机免费；VR设置需要头显）

## 核心方法/设计

OmniH2O为人形机器人提供通用遥操作框架，接受多种输入模态——VR控制器、语音命令或普通RGB视频——并映射到包括灵巧手运动在内的全身人形控制。系统使用在仿真中训练的学习型运动重定向策略，可跨输入模态泛化。这种多模态方法允许操作者根据自身设置和任务选择最便捷的输入方式。

## 主要贡献

- 多模态输入支持（VR/语音/RGB）用于人形遥操作，实现部署场景的灵活性
- 学习型重定向策略跨输入模态泛化，无需逐模态工程
- 在统一框架中实现包括运动和灵巧操作在内的全身控制

## 局限性/不足

- 灵巧手控制保真度低于专用手部遥操作系统
- 所有输入模态均无力/触觉反馈
- 全身聚焦意味着手部操作质量可能相比手部专用系统有所妥协
- 纯RGB输入模式精度最低但可及性最广

## 数据质量影响

全身遥操作的聚焦意味着手部操作示教的保真度低于专用手部系统。学习型重定向策略在操作者意图和机器人运动之间引入了一层抽象，平滑了精细手指运动。通过纯RGB模态采集的示教数据手部控制保真度最低（与AnyTeleop相当），VR控制器输入提供更好的手腕级控制但独立手指关节活动有限。所有输入模态均不提供力反馈，因此所有采集的示教数据缺乏力信息。基于OmniH2O数据训练的策略最适合粗糙手部控制即可满足的全身任务（如双臂物体搬运），而非精密灵巧操作。

## 开源状态

开源。GitHub: [LeCAR-Lab/human2humanoid](https://github.com/LeCAR-Lab/human2humanoid)
