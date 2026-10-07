+++
title = "谷歌发布多模态搜索模型 EmbeddingGemma 2"
slug = "google-releases-embeddinggemma-2"
description = "谷歌的 7.4 亿参数嵌入模型将文本、代码、图像、视频和音频映射到同一向量空间，采用面向本地设备的模块化编码器。"
tags = ["models", "tools"]
date = 2026-10-07T04:01:57+02:00
draft = false
+++

谷歌（Google）发布了 EmbeddingGemma 2。这款开放权重模型拥有 7.4 亿参数，将文本、代码、图像、视频帧和音频放入同一个共享嵌入空间。

采用 Apache-2.0 许可的权重于 10月6日发布，支持 Transformers、sentence-transformers、llama.cpp、vLLM、Ollama、LM Studio、MLX 和 Transformers.js。模型用于检索和路由，而非生成文章：它将不同类型的输入转换为向量，以便比较相似度。

## 为什么重要 {#why-it-matters}

开发者在手机或笔记本电脑上构建私有搜索时，现在可以为语音备忘录建立索引并检索视频片段，无需先串联语音识别、图像描述生成和独立的文本嵌入模型。这减少了本地检索的多个环节，但模型实际是否有用，仍取决于用户自己的数据和延迟预算。

EmbeddingGemma 2 采用模块化设计。文本与代码骨干网络拥有 2.7 亿参数，视觉模块增加 1.7 亿参数，音频模块增加 3 亿参数。所有配置都映射到 768 维，Matryoshka 训练允许应用将向量截断为 512、256 或 128 维，以减少存储量。

谷歌称，在 Pixel 11 Pro 上，仅文本的量化权重使用约 191 MB 活跃运行内存，完整模型则约为 567 MB。按照谷歌的打包方案，8192 token 上下文最多可容纳 5.5 分钟音频、29 张图像或 58 个视频帧。

公司的评测给出的 MTEB Code 得分为 78.68，高于第一代 EmbeddingGemma 的 68.76。谷歌还称，它在参数少于 10 亿的多模态嵌入模型中质量领先。这些是发布当日的测量结果，没有经过独立复现；比较具体检索任务时，模型卡是更合适的依据。

此次发布的模型与 Gemma 4 共用分词器和音频编码器设计。当嵌入模型为本地生成模型提供输入时，这可以减少重复组件。谷歌还发布了媒体搜索和视频时刻检索的示例应用。

接下来有价值的实际证据将来自混合私有数据集上的测试。在这些场景中，跨模态召回、索引时间和内存比单一综合基准测试更重要。

## 核实 {#verification}

| 说法 | 标签 | 一手来源 | 独立核实 |
| --- | --- | --- | --- |
| 谷歌于 2026年10月6日发布 EmbeddingGemma 2 | 已核实 | [谷歌公告](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) | [权重与模型卡](https://huggingface.co/google/embeddinggemma-2) |
| 模型拥有 7.4 亿参数，模块化组件包括 2.7 亿参数的文本模块、1.7 亿参数的视觉模块和 3 亿参数的音频模块 | 已核实 | [谷歌公告](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) | 模型卡列出了架构 |
| 在 Pixel 11 Pro 上，量化后的活跃运行内存约为文本模型 191 MB、完整模型 567 MB | 据公司称 | [谷歌公告](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) | 无 |
| MTEB Code 得分从 68.76 升至 78.68 | 据公司称 | [谷歌公告](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) | 无 |
| Apache-2.0 许可的权重已提供 | 已核实 | [模型仓库](https://huggingface.co/google/embeddinggemma-2) | 仓库可访问 |
