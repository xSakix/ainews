+++
title = "Cloudflare 增加多模态 Clef-omni"
slug = "cloudflare-adds-multimodal-clef-omni"
description = "新分类器保留 Qwen3-Omni 的图像、音频和视频输入，但返回类型化答案，而非生成文字。Cloudflare 还降低了 Clef-flash 价格并缩小上下文窗口。"
tags = ["models", "tools"]
date = 2026-10-12T04:02:37+02:00
draft = false
+++

Cloudflare 发布了 Clef-omni，这个多模态分类器接受文本、图像、音频和视频，但返回类型化答案，而非生成文字。

模型以 Qwen3-Omni 为基础，扩展了 Clef 分类系列。Cloudflare 冻结基础模型，训练轻量适配器，再添加一个头，用一次前向计算将输入直接映射到用户定义的标签模式。

## 为什么重要 {#why-it-matters}

对分类支持消息、检查产品照片或路由短视频的开发者，Clef-omni 提供跨多种媒体的统一分类接口。这可以消除单独转写或生成图注的阶段，不过 Cloudflare 未发布与这类流程的独立端到端比较。

Cloudflare 称，Clef-omni 是一个 300 亿参数混合专家模型，一次输入激活约 30 亿参数。在公司 Workers AI 测量中，文本分类约 130 毫秒，图像约 150 毫秒，一个带音频的 21 秒视频约 1.5 秒。这些时间来自厂商测试，会随输入大小、排队和部署变化。

基准表现有优有劣，并非全面更好。Cloudflare 的表格显示，较老的稠密 Clef 在若干文本任务上领先，而 Clef-omni 在 BANKING77 意图数据集上略胜，94.8% 对 94.2%。新模型实际区别在输入范围，而非普遍拥有更高文本准确率。

Cloudflare 也改变了 Clef-flash 条款。所列输入价格从每百万 token 0.09 美元降至 0.038 美元，上下文窗口从 6.4 万缩至 2.4 万 token。Clef 仍为每百万输入 token 0.24 美元，Clef-omni 首发价为 0.15 美元。

Clef-omni 权重以 Apache 2.0 在 Hugging Face 提供。模型卡列出总参数量约 353 亿，并称当前自定义加载器在 H200 级 GPU 上需要约 64 GB BF16 内存。Cloudflare 表示计划支持 SGLang，但没有发布日期。

## 后续关注

开放权重如今让独立延迟、校准和准确率测试成为可能。主流推理引擎支持，对希望在 Workers AI 之外运行模型、又不想维护 Cloudflare 自定义加载器的团队很重要。

## 核实 {#verification}

| 说法 | 标签 | 一手来源 | 独立核实 |
|---|---|---|---|
| Cloudflare 发布 Clef-omni，支持文本、图像、音频和视频输入及类型化分类输出 | 已核实 | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ | https://huggingface.co/Cloudflare/clef-omni |
| Cloudflare 报告文本约 130 ms、图像约 150 ms、21 秒视听片段约 1.5 s | 据公司称 | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ | 无 |
| Cloudflare 表格报告 Clef-omni 在 BANKING77 上为 94.8%，Clef 为 94.2% | 据公司称 | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ | 无 |
| Clef-flash 现为每百万输入 token 0.038 美元，上下文窗口为 2.4 万 token | 已核实 | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ | 无 |
| Apache-2.0 权重和自定义加载器可用；计划支持 SGLang | 已核实 | https://huggingface.co/Cloudflare/clef-omni | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ |
