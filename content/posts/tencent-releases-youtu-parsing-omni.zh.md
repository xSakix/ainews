+++
title = "腾讯发布 Youtu-Parsing-Omni"
slug = "tencent-releases-youtu-parsing-omni"
description = "这个 50 亿参数模型将文档、图像、音频和视频转成统一结构化 JSON。腾讯已发布权重、代码和技术报告。"
tags = ["models", "tools"]
date = 2026-10-10T04:02:41+02:00
draft = false
+++

腾讯优图实验室发布了一个 50 亿参数模型，将 6 类媒体解析成统一结构化 JSON 格式。

Youtu-Parsing-Omni 接收文档页面、自然图像、图表、几何图形、音频和视频，无需在多个专用模型间切换，即可返回文字、表格、公式、布局框、时间戳、语音转写、说明文字和相机运动描述。

## 为什么重要 {#why-it-matters}

构建搜索或文档处理系统的开发者，可将混合媒体交给一个本地模型，获得可预期的结构。这减少了通常需要整合光学字符识别、语音识别和视频理解服务的工作。

腾讯以自定义 `youtu-parsing` 许可证发布权重，同时提供 vLLM 插件、推理示例和技术报告。仓库称评测代码随后发布，因此仅凭当前发布内容，尚无法复现报告的基准结果。

模型为图像、音频和视频使用共同编码器。处理视频时，选定层允许每帧关注片段同一部分的音频。输出结构既涵盖文本和边界框等直接元素，也涵盖叙事、报告等高层输出。

腾讯报告 OmniDocBench 1.6 得分为 96.96，在其公开表格中略高于 TeleOCR 的 96.91 和 PaddleOCR-VL-1.6 的 96.34。在更广泛的 OmniParsingBench 上，腾讯报告平均 75.08，低于 Gemini 3 Pro 的 77.44，但高于其测试的其他开放权重系统。这些是发布者测量，比较依赖报告中的基准配置。

训练方法反复将学生模型转为自身下一轮的教师。内容 token 与结构 token 获得不同的比较信号，试图同时保留页面说了什么，以及各元素如何关联。

## 后续关注

独立运行需要承诺发布的评测代码。商业用户也需审查自定义许可证，不能假设它与某些开放权重发布一样宽松。

## 核实 {#verification}

| 说法 | 标签 | 一手来源 | 独立核实 |
|---|---|---|---|
| 腾讯发布 50 亿参数 Youtu-Parsing-Omni、权重、代码示例及技术报告 | 已核实 | https://huggingface.co/tencent/Youtu-Parsing-Omni | https://github.com/TencentYoutuResearch/Youtu-Parsing-Omni |
| 模型接收文档、图像、图表、几何、音频及视频，输出统一 JSON 结构 | 据公司称 | https://huggingface.co/tencent/Youtu-Parsing-Omni | 无 |
| 腾讯报告 OmniDocBench 1.6 得分 96.96、OmniParsingBench 得分 75.08 | 据公司称 | https://huggingface.co/tencent/Youtu-Parsing-Omni | 无 |
| 发布采用自定义 youtu-parsing 许可证，尚未包含评测代码 | 已核实 | https://huggingface.co/tencent/Youtu-Parsing-Omni | https://github.com/TencentYoutuResearch/Youtu-Parsing-Omni |
