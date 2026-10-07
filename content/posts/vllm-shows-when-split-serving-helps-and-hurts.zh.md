+++
title = "vLLM 展示分离式服务何时有利、何时有弊"
slug = "vllm-shows-when-split-serving-helps-and-hurts"
description = "一份实用指南测量了分离提示词处理与 token 生成的权衡。负载下的尾部延迟有所改善，但转移模型工作内存会延迟首个 token。"
tags = ["essays", "tools", "hardware"]
date = 2026-10-06T04:04:31+02:00
draft = false
+++

vLLM 团队报告，将提示词处理与 token 生成分离，可以让模型服务器在负载下更稳定，但转移工作内存可能让首次响应更慢。

这个开源推理（inference）项目测试了“解耦式服务”：一张 GPU 负责预填充（prefill），另一张负责解码（decode）。预填充读取提示词并构建键值缓存，解码则利用缓存生成 token。指南还将分词和输出解析移到不使用 GPU 的前端。

对处理长提示词的运营者，设计提供了两种延迟之间的选择。分离阶段能避免大型提示词中断其他用户的生成，但解码开始前，缓存必须在工作进程之间传输。

vLLM 使用两张 GPU、Qwen2.5-7B 和 8000 token 提示词的测试中，在每秒 0.4 次请求时，合并配置下生成 token 间隔的第 99 百分位数从 23 毫秒升至 169 毫秒。分离配置则将该间隔保持在 25–52 毫秒。

同一实验也暴露了成本。每个提示词约 470 MB 缓存的转移耗时约 1.3 秒，首个 token 的时间中位数为 2.2 秒，两阶段共用工作进程时则为 0.7 秒。L40S GPU 既没有 NVLink，也没有直接点对点传输，因此结果描述的是刻意选择的不利传输路径，不能代表所有部署。

作者的决策规则很实用：先检查 GPU 拓扑，再按照预期提示词长度和请求速率检查缓存传输指标。当预填充反复干扰解码，或两个阶段需要不同扩展方式时，解耦最有吸引力。轻负载服务器可能付出传输成本，却得不到有用的隔离收益。

指南引用了 AMD 和 llm-d 项目规模更大的结果，但这些测试使用不同模型、加速器和集群规模。它们支持架构的潜力，不能提供可直接套用的加速数字。

指令面向 vLLM 0.30.0 或更新版本，并包含独立的渲染器和反渲染器服务。团队称，集成仍有缺口，因此拓扑和传输检查是前提，而非部署后的优化。

## 核实 {#verification}

| 说法 | 标签 | 一手来源 | 独立核实 |
| --- | --- | --- | --- |
| vLLM 文档说明了独立的预填充、解码和不使用 GPU 的前端服务 | 已核实 | [vLLM 指南](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | 公开的 vLLM 配置和命令 |
| 每秒 0.4 次请求时，同机配置的 p99 token 间隔达到 169 ms，分离式服务则保持在 25–52 ms | 据公司称 | [vLLM 指南](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | 无；项目开展的测试 |
| 一个 8000 token 提示词产生约 470 MB 缓存，传输约需 1.3 s | 据公司称 | [vLLM 指南](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | 无 |
| 首个 token 时间中位数为分离配置 2.2 s、同机配置 0.7 s | 据公司称 | [vLLM 指南](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | 无 |
| 测试使用两张 L40S GPU，没有 NVLink 或点对点传输 | 已核实 | [vLLM 指南](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | 作者说明了测试配置 |
| 指南面向 vLLM 0.30.0 或更新版本 | 已核实 | [vLLM 指南](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | 指南中的版本要求 |
