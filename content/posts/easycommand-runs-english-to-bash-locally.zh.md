+++
title = "EasyCommand 在本地将英语转换为 Bash"
slug = "easycommand-runs-english-to-bash-locally"
description = "这款开源命令行工具内嵌 llama.cpp，提供两个经过微调的小模型。作者还发布了包含 401,975 对样本的训练集和基准测试代码。"
tags = ["projects", "models", "tools"]
date = 2026-10-06T04:06:31+02:00
draft = false
+++

EasyCommand 用运行在 CPU 上的小模型，将英语请求转换为 Bash 命令，提示词和建议命令都保留在用户机器上。

开发者 Max Trivedi 发布了 `ec` 命令行应用、两个模型家族，以及包含 401,975 对去重请求与命令的数据集。应用内嵌 llama.cpp，预览建议命令，并可在执行前请求确认。

对偶尔需要命令行提醒的开发者，本地执行能从工作流的敏感环节移除一次 API 调用。代价是直接承担责任：项目提醒，看似合理的命令仍可能出错，并建议从预览模式开始。

发布的模型以 Qwen2.5-Coder-1.5B-Instruct 和 Qwen3-0.6B 为基础。两者均提供用于本地推理（inference）的 GGUF 文件、合并后的 BF16 模型版本，以及可进一步训练的 LoRA 适配器。模型和数据集使用 Apache 2.0 许可证，应用和基准测试代码使用 MIT。

Trivedi 称，15 亿参数模型在更新版 ALFA 英语转 shell 基准测试的 300 项中解决了 212 项，较早的 nl2sh 系统则解决了 191 项。这是作者使用不同模型提示词和设置开展的比较，不是独立排行榜结果。

这次发布格外实用，因为除了模型，也说明了失败和限制。Trivedi 称，平面数据集没有复现训练时使用的历史权重，也没有官方测试划分。他建议留出完整任务家族，而非随机分离改写文本，否则几乎相同的命令可能同时进入训练和评测。

目标是 GNU/Linux Bash，并非所有 shell 或操作系统。EasyCommand 仓库现在已公开，作者正邀请用户贡献测试，以暴露不可靠的迁移和缺失的命令覆盖。

## 核实 {#verification}

| 说法 | 标签 | 一手来源 | 独立核实 |
| --- | --- | --- | --- |
| EasyCommand 在本地运行，内嵌 llama.cpp，并在执行前预览命令 | 已核实 | [项目文章](https://dirac.run/posts/easycommand) | [公开仓库](https://github.com/dirac-run/ec) |
| 发布内容包含 401,975 对去重英语与 Bash 样本 | 已核实 | [项目文章](https://dirac.run/posts/easycommand) | 仓库链接了数据集 |
| 模型基于 Qwen2.5-Coder-1.5B 和 Qwen3-0.6B | 已核实 | [项目文章](https://dirac.run/posts/easycommand) | 仓库链接了模型文件 |
| 15 亿参数模型得分为 212/300，nl2sh 为 191/300 | 据公司称 | [项目文章](https://dirac.run/posts/easycommand) | 无；作者开展的基准测试 |
| 模型和数据使用 Apache-2.0，应用和基准测试代码使用 MIT | 已核实 | [项目文章](https://dirac.run/posts/easycommand) | 仓库许可证文件 |
| 数据集没有官方测试划分，也没有保留历史权重 | 据公司称 | [项目文章](https://dirac.run/posts/easycommand) | 作者披露 |
