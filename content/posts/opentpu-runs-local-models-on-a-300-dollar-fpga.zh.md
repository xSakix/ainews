+++
title = "OpenTPU 在 300 美元 FPGA 卡上运行本地模型"
slug = "opentpu-runs-local-models-on-a-300-dollar-fpga"
description = "这个采用 Apache 许可的项目公开了加速器设计、编译器、模拟器和主机工具。实测吞吐量表明，这是受内存限制的小型系统，尚不足以替代 GPU。"
tags = ["hardware", "projects", "models"]
date = 2026-10-07T03:58:57+02:00
draft = false
+++

OpenTPU 发布了一套端到端 AI 加速器技术栈，能在约 300 美元的 Kintex-7 FPGA 卡上运行现代语言模型。

采用 Apache-2.0 许可的仓库包含 SystemVerilog 硬件、指令集、位精确模拟器、内核语言与编译器、性能分析工具和主机软件。其价值在于可检查性：同一套小型代码库从 Python 模型内核一直覆盖到实体 PCIe 板卡上的信号。

## 为什么重要 {#why-it-matters}

学习推理（inference）硬件的开发者无需数据中心加速器，就能追踪每个时钟周期和每次内存传输的去向。这台机器比当前 GPU 慢，但它的限制让瓶颈格外清晰。

OpenTPU 报告称，四比特 Qwen3-0.6B 模型每秒生成 30.7 个 token，LFM2.5-230M 每秒生成 82.1 个，均包含主机开销。在列出的配置中，更大的稠密模型速度更慢：Qwen3.5-2B 每秒 12.03 个 token，Gemma 4 E4B 每秒 3.75 个。

解码时，板卡达到两个 DDR3 通道 17.1 GB/s 峰值带宽的 82%–94%。因此，限制资源是内存带宽，而非矩阵运算。四列脉动阵列单元对提示词处理的帮助大于对逐 token 生成的帮助。

超过板卡 4 GiB 容量的模型可以从主机存储流式加载混合专家权重。仓库报告，LFM2.5-8B-A1B 每秒生成 10.6 个 token，Qwen3.5-35B-A3B 每秒 3.95 个，后者每个 token 需经 PCIe 传输 153 MB。这些是项目自己的测量结果，但脚本、标明日期的构建版本和测量条件均已公开。

“由 AI 开发”的描述需要谨慎理解。据项目称，人类主导的智能体（agent）工作流完成了大量设计和优化，但这并不表明自主系统决定创建自己的硬件。具体成果是公开的技术栈，以及项目报告的板卡与模拟器逐比特一致的结果。

下一步测试很明确：在同款板卡上复现已发布的比特流，与低价 GPU 比较功耗和延迟，并观察外部贡献者能否修改架构而不破坏与模拟器的等价性。

## 核实 {#verification}

| 说法 | 标签 | 一手来源 | 独立核实 |
| --- | --- | --- | --- |
| OpenTPU 以 Apache-2.0 许可发布硬件、指令集架构、模拟器、编译器和主机工具 | 已核实 | [OpenTPU 仓库](https://github.com/FeSens/openTPU) | 文件和许可证可访问 |
| 四比特配置下，按实际耗时计算，Qwen3-0.6B 每秒生成 30.7 个 token，LFM2.5-230M 每秒生成 82.1 个 | 据公司称 | [OpenTPU 测量结果](https://github.com/FeSens/openTPU) | 无 |
| 解码使用了 17.1 GB/s DDR3 峰值带宽的 82%–94% | 据公司称 | [OpenTPU 测量结果](https://github.com/FeSens/openTPU) | 无 |
| Qwen3.5-35B-A3B 在每个 token 流式传输 153 MB 时达到每秒 3.95 个 token | 据公司称 | [OpenTPU 测量结果](https://github.com/FeSens/openTPU) | 无 |
| 板卡逐比特复现模拟器的 token | 据公司称 | [OpenTPU 仓库](https://github.com/FeSens/openTPU) | 存在公开测试；未找到独立硬件复现 |
| “由 AI 开发”不能证明硬件开发具有自主性 | 分析 | [OpenTPU 仓库](https://github.com/FeSens/openTPU) | 区分依据是文档记载的人类主导工作流 |
