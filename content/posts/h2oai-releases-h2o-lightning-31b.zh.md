+++
title = "H2O.ai 发布 H2O-Lightning-31B"
slug = "h2oai-releases-h2o-lightning-31b"
description = "这一开放权重决策模型通过一次前向传播回答有界问题，并返回概率。其最突出的速度和准确率数字来自 H2O.ai 自己的测试。"
tags = ["models", "tools"]
date = 2026-10-11T04:06:06+02:00
draft = false
+++

H2O.ai 发布了 H2O-Lightning-31B。这一开放权重模型以概率回答有界决策问题，而非生成自由文本。

模型基于 Gemma 4 31B-it，接受文本及最多四张图片。接口支持选择、是非问题和有序评分，通过一次前向传播返回一个结果。H2O.ai 在 Hugging Face 发布了权重、模型卡和服务代码。

## 为什么重要 {#why-it-matters}

对使用大型聊天机器人分派工单、给记录评分或选择工具的开发者来说，受约束输出能去掉几个脆弱环节：要求生成 JSON、解析它、拒绝格式错误的答案，再次提问。概率还能展示选择有多接近，但只有模型针对预期数据校准时才有用。

H2O.ai 报告，这个 310 亿参数模型正确回答了 231 道公开 JevBench 问题中的 212 道。在图像评测中，微调模型在 1,877 个问题上得到 88.4%，冻结的 Gemma 基础模型为 88.0%。模型卡的不确定区间包含零提升，因此图像结果不能证明相对基础模型有可靠收益。

公司还报告，在单张英伟达（NVIDIA）H100 上以 FP8 加载模型时，中位延迟约 25 毫秒。数字来自其自身配置，关闭了前缀缓存，模型卡也没有提供较小 GPU 的测量。公开的 bfloat16 文件总计约 63 GB，尚未计算运行时开销。

该版本在未修改的 vLLM 0.30.0 上运行，前面加有 H2O.ai 的 `/v1/systemone` 适配层。长记录不会完整处理：检索阶段会在推理（inference）前将其截至 3,000 token。这一边界很重要，因为决策只能反映检索保留下来的证据。

权重采用 Apache 2.0，同时受谷歌（Google）的 Gemma 条款约束。H2O.ai 的声明特别指出，Gemma 的禁止用途限制涵盖影响个人权利的自动决策，因此文件开放不意味着任何部署都获允许。

H2O.ai 还更新了此前的 40 亿参数同系列模型，修订延迟测量，并提供用于 llama.cpp 的 GGUF 包。310 亿参数版本现已在 Hugging Face 模型页面上线；独立延迟、校准和任务质量测试尚未发布。

## 核实 {#verification}

| 说法 | 标签 | 一手来源 | 独立核实 |
|---|---|---|---|
| H2O.ai 发布了 H2O-Lightning-31B，附有权重、模型卡和服务代码 | 已核实 | https://huggingface.co/h2oai/h2o-lightning-31b | 无 |
| 模型支持有界文本与图像决策，通过一次前向传播返回概率 | 已核实 | https://huggingface.co/h2oai/h2o-lightning-31b | 无 |
| 它答对 231 道 JevBench 问题中的 212 道，单张 H100 中位延迟约 25 ms | 据公司称 | https://huggingface.co/h2oai/h2o-lightning-31b | 无 |
| 图像评测没有显示相对冻结 Gemma 基础模型有统计上可靠的提升 | 已核实 | https://huggingface.co/h2oai/h2o-lightning-31b | 无 |
| Gemma 条款限制影响个人权利的自动决策 | 已核实 | https://huggingface.co/h2oai/h2o-lightning-31b | 无 |
