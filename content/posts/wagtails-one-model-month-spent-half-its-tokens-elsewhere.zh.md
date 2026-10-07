+++
title = "Wagtail 单模型月计划将半数 token 花在别处"
slug = "wagtails-one-model-month-spent-half-its-tokens-elsewhere"
description = "用 GLM 5.3 Flash 完成 9月工程工作的计划消耗了 20 亿 token，但只有一半交给目标模型。原型、服务商容量和评测解释了这一差距。"
tags = ["essays", "models", "tools"]
date = 2026-10-05T03:57:30+02:00
draft = false
+++

Wagtail 核心团队的 Thibaud Colas，尝试在 9月用一款高效开放模型 GLM 5.3 Flash 完成工程工作。使用日志记录了 20 亿 token，只有 10 亿交给了选定模型。

这让实验比一帆风顺的成功故事更有价值。据 Colas 称，目标模型本身费用约 68 美元，估计耗电 4 kWh。整月工作消耗约 35 kWh，而非计划的 10 kWh，因为原型、服务商问题和刻意开展的模型评测将流量引向其他模型。

最明显的失败来自 Wagtail 实验性 Model Context Protocol 服务器的“氛围编程（vibe coding）”原型。Colas 称，这项工作选错模型，几乎一夜之间消耗 4.5 亿 token、约 150 美元和 5 kWh。原型确实能用，但失控用量显示，智能体式实验可以多么迅速地主导精心制定的预算。

基础设施是第二项限制。Colas 报告 GLM 5.3 Flash 性能下降，并归因于独立推理（inference）服务商容量有限。他将工作切换到深度求索（DeepSeek）V4.1 Flash、Qwen 3.8 Flash 等替代模型。对试图避开最大实验室的团队，模型可用性成为质量的一部分：如果接口在需求增加时变慢，优秀的模型版本也不是可靠的生产选择。

部分目标之外的使用是有意的。Wagtail 正开发自己的任务基准测试，因此团队需要运行一系列模型，不能只优化日常输出。Colas 现在建议，将单模型规则用于一半以上的常规生产工作，同时允许研发自由比较替代方案。

他仍然看好 GLM 5.3 Flash。长上下文、视觉支持和多家服务商提供，让模型对 Wagtail 开发、界面工作、文档和评测有用。这一评价来自他的经验，而非受控比较。

更广泛的教训在方法上。token 总量会掩盖使用来自计划内生产、意外循环，还是必要评测。有用的运营仪表板至少需要成本、能源、模型身份和任务结果，还需要本地、持续测量：昂贵原型在消耗了整月四分之一 token 后才被发现。

这是一支团队自报的一个月，不能证明 GLM 5.3 Flash 或开放模型普遍需要特定成本。服务商价格、能源估计和任务组合都会变化。记录确立的是值得预先考虑的失败方式：模型预算可以合理，外围工作流却使之失效。

## 核实 {#verification}

| 说法 | 标签 | 一手来源 | 独立核实 |
| --- | --- | --- | --- |
| 9月总使用量为 20 亿 token，其中 10 亿用于 GLM 5.3 Flash | 已核实 | [Wagtail 记录](https://wagtail.org/blog/one-month-on-glm-53-flash/) | 无；作者的使用仪表板 |
| 目标模型部分费用约 68 美元、耗电 4 kWh；整月约耗电 35 kWh | 据社区报告 | [Wagtail 记录](https://wagtail.org/blog/one-month-on-glm-53-flash/) | 无；作者估计 |
| 原型消耗 4.5 亿 token、约 150 美元和 5 kWh | 据社区报告 | [Wagtail 记录](https://wagtail.org/blog/one-month-on-glm-53-flash/) | 无；作者测量 |
| 服务商容量迫使工作切换至其他模型 | 据社区报告 | [Wagtail 记录](https://wagtail.org/blog/one-month-on-glm-53-flash/) | 无；作者诊断 |
| GLM 5.3 Flash 对多种 Wagtail 工程任务有用 | 观点 | [Wagtail 记录](https://wagtail.org/blog/one-month-on-glm-53-flash/) | 一名从业者的评价 |
| 模型、成本、能源和结果应共同测量 | 分析 | [Wagtail 记录](https://wagtail.org/blog/one-month-on-glm-53-flash/) | 根据报告的失败方式推断 |
