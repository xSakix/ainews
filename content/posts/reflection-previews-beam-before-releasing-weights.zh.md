+++
title = "Reflection 在权重发布前预览 Beam"
slug = "reflection-previews-beam-before-releasing-weights"
description = "这款 5010 亿参数混合专家模型目前只提供抢先体验。Reflection 称，权重、技术报告和开发者工具将在 10月晚些时候发布。"
tags = ["models", "agents"]
date = 2026-10-06T04:09:31+02:00
draft = false
+++

Reflection AI 宣布了 Beam。这款用于编程和智能体（agent）工作的模型拥有 5010 亿参数，但开发者目前还无法检查或运行其权重。

这家加州 AI 公司将 Beam 描述为稀疏混合专家模型：它存储 5010 亿参数，每个 token 只激活 230 亿。抢先体验需要注册，权重、许可证、模型卡、技术报告和开发者工具仍未提供。

对选择开放模型的开发者来说，这一区别很重要。开放权重模型可以在私有工作负载上测试、修改和部署，无需依赖厂商服务；公告和基准测试表目前还无法支持这些检查。

Reflection 称，它用 23.8 万亿 token 训练 Beam，随后在 10,500 张英伟达（NVIDIA）GB300 GPU 上运行了超过 1 亿次强化学习轨迹采样，持续四周。这些数字描述了一次规模异常庞大的训练，但公司尚未发布检查数据构成或评测设置所需的技术报告。

实验室自己的表格给出 Beam 在 SWE-bench Verified 上 80.9、在 Terminal-Bench 2.1 上 80.1 的得分。表格还显示，在大多数列出的测试中，Beam 落后于 Kimi K3、GLM-5.3 和 Qwen 3.8-Max。Reflection 主要比较的是效率：按自己估算的浮点运算量，公司称 Beam 以少三到四倍的推理（inference）计算量，达到与 GLM-5.2 相当的结果。

对于付费运行长时间智能体会话的团队，这一说法可能比基准测试上的小幅领先更重要。稀疏激活减少每个 token 所用的计算量，但完整模型仍需要足够的内存和基础设施，以存储和运行数千亿参数。

Reflection 称，Beam 正在接受最终安全测试。公司计划在 2026年10月晚些时候发布权重、技术报告、模型卡和开发者资源，尚未给出具体发布日期。

## 核实 {#verification}

| 说法 | 标签 | 一手来源 | 独立核实 |
| --- | --- | --- | --- |
| Reflection 宣布 Beam 并开放抢先体验注册 | 已核实 | [Reflection 公告](https://reflection.ai/blog/introducing-beam) | 公司行动无需另行核实 |
| Beam 拥有 5010 亿总参数，每个 token 激活 230 亿参数 | 据公司称 | [Reflection 公告](https://reflection.ai/blog/introducing-beam) | 无；权重和报告尚未提供 |
| 训练使用 23.8 万亿 token，并在 10,500 张 GB300 GPU 上运行超过 1 亿次强化学习轨迹采样，持续四周 | 据公司称 | [Reflection 公告](https://reflection.ai/blog/introducing-beam) | 无 |
| Beam 在 SWE-bench Verified 上得分 80.9，在 Terminal-Bench 2.1 上得分 80.1 | 据公司称 | [Reflection 公告](https://reflection.ai/blog/introducing-beam) | 无 |
| Reflection 估计，Beam 用少 3–4 倍的推理计算量达到与 GLM-5.2 相当的结果 | 据公司称 | [Reflection 公告](https://reflection.ai/blog/introducing-beam) | 无 |
| 承诺在 2026年10月晚些时候发布权重、报告、模型卡和开发者资源 | 已核实 | [Reflection 公告](https://reflection.ai/blog/introducing-beam) | 所述时间安排无需另行核实 |
