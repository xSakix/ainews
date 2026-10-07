+++
title = "Strata 分支让 IBM 老服务器运行本地大模型"
slug = "strata-fork-revives-an-ibm-ai-server-for-local-llms"
description = "一个针对特定硬件的分支，在两个 POWER9 处理器和四张 V100 GPU 上运行 Qwen3.8-Flash-Next，展示了模型感知优化能从 2018年系统中释放的能力。"
tags = ["projects", "hardware", "models"]
date = 2026-10-05T03:58:30+02:00
draft = false
+++

一名社区开发者将 Strata 推理（inference）引擎适配到 IBM AC922。这款 2018年服务器的两个 POWER9 处理器，直接连接四张 16 GB 英伟达（Nvidia）V100 加速器。成果更像是让特殊机器拓扑适合现代混合专家模型的案例研究，而非 llama.cpp 的通用替代品。

分支运行量化 Qwen3.8-Flash-Next。这款 1250 亿参数模型采用稀疏设计，每个 token 只激活一小部分专家。Strata 将常用专家保留在 GPU 上，完整专家集放在系统内存。这种安排适合 AC922，因为其 CPU 与 GPU 共享高带宽 NVLink 2.0 连接，而非仅通过普通 PCIe 通信。

开发者为每个 CPU 插槽增加页锁定内存区域，按照机器非一致内存布局放置专家，并让原本空闲的对等 GPU 通过自己的 NVLink 获取数据。其他修改包括 FP16 Volta 张量核心内核、流水线式层拆分，以及 POWER9 专用向量和线程处理。

项目自己的测量显示，四张 V100 读取 13.5 万 token 提示词时，峰值达到每秒 7357 个 token。25.2 万 token 提示词以每秒 7089 个 token 处理，耗时 35.5 秒。贪心生成在 JSON 上达到每秒 113 个 token，代码上为 103 个，文章上为 84 个。复用 25.2 万 token 上下文时，第一个后续 token 在 0.26 秒后出现，随后生成速度为每秒 60 个 token。

这些数字是构建者在一台专用服务器上的测量，不是可直接套用的基准测试。提示词处理速度随长度显著变化，生成文本类型也会改变解码速度。仓库将分支描述为实验性项目，不受上游 Strata 支持。

不过，项目展示了一种日益实用的本地推理方法：围绕特定模型和特定内存层级优化，不要求通用引擎同样对待每台机器。AC922 是老旧、耗电的企业设备，但其 CPU 到 GPU 链路仍然格外强大。拥有数千专家的模型让这些链路有了有用的工作。

代码以 Strata 的 MIT 许可证发布在分支项目的 `ac922` 分支，附有构建、质量和基准测试说明。部分修改最终可能进入上游，但眼前价值是可检查的工程实现，服务于主流推理项目很少针对的硬件拥有者。

## 核实 {#verification}

| 说法 | 标签 | 一手来源 | 独立核实 |
| --- | --- | --- | --- |
| 分支针对配备两个 POWER9 CPU、四张 16 GB V100 GPU 和 NVLink 2.0 的 AC922 | 已核实 | [仓库](https://github.com/eelgaev/Strata-AC922) | 无 |
| NUMA 感知专家放置、每插槽页锁定区域、对等 GPU 获取数据，以及 Volta/POWER9 内核 | 已核实 | [仓库](https://github.com/eelgaev/Strata-AC922) | 存在代码和技术说明；未独立执行 |
| 预填充峰值为每秒 7357 个 token，25.2 万 token 时为每秒 7089 个 | 据社区报告 | [仓库](https://github.com/eelgaev/Strata-AC922) | 无；构建者基准测试 |
| 解码在 JSON 上达到每秒 113 个 token，文章上为 84 个 | 据社区报告 | [仓库](https://github.com/eelgaev/Strata-AC922) | 无；构建者基准测试 |
| 分支属于实验性项目，不受上游支持 | 已核实 | [仓库](https://github.com/eelgaev/Strata-AC922) | 仓库明确说明 |
| 针对特定硬件的推理可从较老的专用内存拓扑中恢复价值 | 分析 | [仓库](https://github.com/eelgaev/Strata-AC922) | 根据实现和测量推断 |
