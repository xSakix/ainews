+++
title = "哔哩哔哩为 Index-Translate 增加本地版本"
slug = "bilibili-expands-index-translate-with-local-builds"
description = "这套开放翻译模型现已提供 GGUF、FP8 和 NVFP4 包、免费的兼容 API，以及四套公开基准测试。性能数字仍来自开发者自己。"
tags = ["models", "tools"]
date = 2026-10-05T04:01:30+02:00
draft = false
+++

哔哩哔哩（bilibili）于 10月3日和4日为 Index-Translate 增加官方量化版本、免费公共接口和四套评测集，让近期发布的翻译模型更便于本地和托管使用。

这套模型支持 150 种语言之间的文本翻译，接受有关术语、格式和风格的指令。普通文本模型有 20 亿、90 亿参数，以及预览版 350 亿参数三种规模。最大的模型采用混合专家架构，每个 token 激活约 30 亿参数。

对本地用户，重要变化是封装格式。GGUF 版本现在面向 llama.cpp，FP8 版本面向 vLLM，NVFP4 版本面向较新的 Blackwell GPU。项目在文本、音节控制和长文档产品线中发布这些格式。语音模型也有量化包，但 GGUF 仓库只包含其文本模型骨干，而非完整语音流程。

新的托管接口通过兼容 OpenAI 聊天 API 的接口提供 35B-A3B 预览版，让开发者无需先准备合适硬件就能测试模型。仓库将接口标为免费，但没有承诺服务水平或长期价格。

Index-Translate 不只是句子翻译器。客户端可以保留 JSON 和 Markdown 结构、遵循术语表，并要求特定语气。相关包可以翻译语音、为配音实现要求的音节数，或在长文档中保留上下文。这些功能处理了生产翻译中的棘手部分，而通用“翻译这个”提示词往往会漏掉它们。

哔哩哔哩还发布了 instTrans、MEME、SandGlass 和 NativeLong 基准测试材料及评测脚本。这使测试设计可检查，但公开分数仍是开发者自己的测量。技术报告中，预览模型在 FLORES COMET-22 上得分 0.8794，在 WMT26 评判器上得分 76.76。后者使用 GPT-5.6-Sol 评测，因此不应视为独立的人类比较。

原始模型家族于 9月30日推出，此次没有发布新的基础模型。新闻在于，四天之内，它获得了部署格式、测试接口和评测资源，从模型公告走向开发者真正能尝试的东西。

## 核实 {#verification}

| 说法 | 标签 | 一手来源 | 独立核实 |
| --- | --- | --- | --- |
| 公共 API 和四套基准测试于 10月4日发布；量化版本于 10月3日发布 | 已核实 | [项目仓库](https://github.com/bilibili/Index-Translate) | 无 |
| 文本模型覆盖 150 种语言，支持术语、格式和风格约束 | 已核实 | [项目仓库](https://github.com/bilibili/Index-Translate) | [模型卡](https://huggingface.co/IndexTeam/Index-Translate-35B-A3B-preview) |
| GGUF、FP8 和 NVFP4 包及文档说明的运行目标 | 已核实 | [项目仓库](https://github.com/bilibili/Index-Translate) | 仓库列出了各个包的链接 |
| 预览模型拥有 350 亿总参数，约 30 亿激活参数 | 已核实 | [模型卡](https://huggingface.co/IndexTeam/Index-Translate-35B-A3B-preview) | 无 |
| FLORES COMET-22 得分 0.8794，WMT26 评判器得分 76.76 | 据公司称 | [技术报告](https://arxiv.org/abs/2609.40181) | 无；报告在 WMT26 上使用 GPT-5.6-Sol 作为评判器 |
| 新封装让这套模型更便于在本地或通过托管接口测试 | 分析 | [项目仓库](https://github.com/bilibili/Index-Translate) | 根据发布资源推断；接口持久性尚未确定 |
