+++
title = "Mistral 在发布权重前开放 Large 4 预览"
slug = "mistral-previews-large-4-before-releasing-weights"
description = "Mistral 已开放其万亿参数多模态模型的 API 访问，并将开放权重发布时间定在 10月27日。架构和基准测试方面的说法仍有待确认。"
tags = ["models", "business"]
date = 2026-10-07T04:00:57+02:00
draft = false
+++

Mistral 已开放 Mistral Large 4 的公开 API 预览，并计划于 10月27日提供模型权重下载。

这家法国公司称，该模型是多模态混合专家模型，在其欧洲数据中心从零开始训练。模型接受文本和图像，支持超过 160 种语言，上下文窗口为 100 万 token。

## 为什么重要 {#why-it-matters}

考虑自行托管欧洲模型的组织现在可以测试 Large 4，但还无法检查或部署承诺提供的权重。这意味着此次发布是附有明确交付日期承诺的预览，尚未完成开放权重发布。

Mistral 的公告列出了 1 万亿总参数和每个 token 激活的 490 亿参数。其文档列出的却是 1.05 万亿总参数、520 亿激活参数，以及 16 亿参数的视觉编码器。差异可能来自四舍五入或配置变化，但 Mistral 尚未发布技术报告来解释这些数字。

公司重点强调网络安全。它报告称，模型在 CyberGym-E2E 的先复现后修补部分得分为 82%，在 Cybench 上为 93%，在 DeepSWE v1.1 上为 61.7%。部分评测注明了外部服务提供方，但汇总比较和大多数主要说法出现在 Mistral 自己的发布材料中。

Mistral 称，权重发布前，网络安全专家和公共部门将测试一个内容审核较少的版本。公司认为，常规安全拒答可能妨碍防御工作，此次预览旨在探查这一权衡。

API 起价为每百万输入 token 1.36 美元、每百万输出 token 4.18 美元。Mistral Studio 提供推理（reasoning）和非推理模式，而许可证和最终部署要求要等权重发布后才会明确。

决定性的时间点是 10月27日。模型卡、技术报告、许可证和可下载文件将显示，公开发布的模型是否符合预览所宣称的规模和能力。

## 核实 {#verification}

| 说法 | 标签 | 一手来源 | 独立核实 |
| --- | --- | --- | --- |
| Mistral 开放了 Large 4 API 预览，并计划于 10月27日发布权重 | 已核实 | [Mistral 公告](https://mistral.ai/news/mistral-large-4/) | [Mistral 文档](https://docs.mistral.ai/models/mistral-large-4) |
| 公告列出了 1 万亿总参数和 490 亿激活参数 | 已核实 | [Mistral 公告](https://mistral.ai/news/mistral-large-4/) | 文档列出的数字不同 |
| 文档列出了 1.05 万亿总参数、520 亿激活参数和 16 亿参数的视觉编码器 | 已核实 | [Mistral 文档](https://docs.mistral.ai/models/mistral-large-4) | 无 |
| 模型在 CyberGym-E2E 先复现后修补部分得分为 82%，在 Cybench 上为 93%，在 DeepSWE v1.1 上为 61.7% | 据公司称 | [Mistral 公告](https://mistral.ai/news/mistral-large-4/) | 所注明的评测方并未独立核实整项比较 |
| API 价格为每百万输入 token 1.36 美元、每百万输出 token 4.18 美元 | 已核实 | [Mistral 文档](https://docs.mistral.ai/models/mistral-large-4) | 当前在线文档 |
