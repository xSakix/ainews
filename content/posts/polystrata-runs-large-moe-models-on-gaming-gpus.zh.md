+++
title = "PolyStrata 在游戏 GPU 上运行大型 MoE 模型"
slug = "polystrata-runs-large-moe-models-on-gaming-gpus"
description = "开源运行器将选定模型专家保留在系统内存，按需移至消费级 GPU。一键软件包提供兼容 OpenAI 和 Anthropic 的本地 API。"
tags = ["projects", "models", "hardware"]
date = 2026-10-12T03:57:37+02:00
draft = false
+++

PolyStrata 发布开源运行器，利用系统内存运行无法完全装进游戏 GPU 的混合专家模型。

一键软件包封装 Strata 运行时，面向至少有 12 GB 显存的英伟达（Nvidia）和 AMD 显卡。它提供支持图像的 Qwen3.8-Flash-Next 配置，以及对若干更大型稀疏模型的实验支持，同时在本机提供兼容 OpenAI 与 Anthropic 的端点。

## 为什么重要 {#why-it-matters}

对只有工作站而非服务器的开发者，PolyStrata 把空闲系统 RAM 转成更大的模型池。只有当前 token 所需专家经由 GPU 处理，用数据搬移与内存容量换取多 GPU 硬件成本。

混合专家模型包含许多专用参数块，但每一步只激活部分。PolyStrata 将这些块保留在主机内存，将活跃块调度到加速器。技术不会缩小模型文件：README 称，实验性 GLM 5.3 Flash 版本仍需约 79 至 114 GB，取决于量化。

项目自有 RTX 5070 测量，从最小两位设置每秒生成约 94 个 token，到较大三位设置每秒 53 个。它报告，在 32,000 token 上下文中，提示词处理速度约每秒 1,620 至 2,650 个 token。这些是构建者基准，而非独立测量，不同量化级别质量不同。

PolyStrata 还记录了 Claude Code 在 8 GB 笔记本 GPU 上驱动三位精度 Qwen3.6 35B 稀疏模型。热启动选项在交互会话前读取系统提示词，减少首个答案的等待。实际可用性取决于 RAM 带宽、模型路由，以及轮次间上下文改变多少。

仓库采用 MIT 许可，提供与现有智能体客户端兼容的本地端点。这降低整合工作，同时让本地应用以用户自己的权限访问文件和工具。也意味着运营者而非托管提供商负责模型更新、网络暴露与日志处理。

## 后续关注

独立测试应使用相同模型与量化设置，与成熟 CPU 卸载运行时比较。项目当前价值是可检查代码与实用封装层；醒目速度在更多硬件复现前，仍是作者报告。

## 核实 {#verification}

| 说法 | 标签 | 一手来源 | 独立核实 |
|---|---|---|---|
| PolyStrata 发布 MIT 许可的本地运行器，在消费级 GPU 上运行稀疏模型 | 已核实 | https://github.com/VecSzn/PolyStrata | 无 |
| 软件包提供兼容 OpenAI 与 Anthropic 的本地 API | 已核实 | https://github.com/VecSzn/PolyStrata | 无 |
| README 报告，在所选量化设置下，RTX 5070 每秒生成 53–94 个 token | 据公司称 | https://github.com/VecSzn/PolyStrata | 无 |
| 实验性 GLM 5.3 Flash 文件需要约 79–114 GB，取决于量化 | 已核实 | https://github.com/VecSzn/PolyStrata | 无 |
| 从主机内存加载专家，以传输和内存带宽成本换取容量 | 分析 | https://github.com/VecSzn/PolyStrata | 无 |
