+++
title = "Fable 5.2 标价下降，账单仍取决于推理强度"
slug = "fable-5-2-cuts-its-list-price-but-the-bill-follows-effort"
description = "Anthropic 将 Claude Fable 5.2 的价格降低了五分之一，但独立指数测得，其最高推理强度下每项任务成本在 73 款模型中最高。差距在于 token 消耗量，而 Anthropic 自己的图表也表明，推理强度设置决定了这一点。"
tags = ["models", "business"]
date = 2026-11-10T03:25:07+01:00
draft = false
+++

这个星期一是虚构的，由发布文档拼接而来，并不出自任何人的日记。一家中型软件公司的平台负责人读到 Anthropic 将顶级模型价格降低了五分之一。她按公告暗示的方向行动：修改团队智能体配置中的模型名称，把推理强度参数设到最高，然后让 40 个代码仓库审计任务通宵运行。到早晨，整批任务已经完成，她唯一想打开的就是账单。它看起来与她读到的标题并不相符。

标题没有错。11月9日，Anthropic 发布 Claude Fable 5.2 及其孪生模型 Claude Mythos 5.2，每百万输入 token 8 美元、每百万输出 token 40 美元，低于 5.1 版本的 10 美元和 50 美元。同日公布的独立数字也准确。发布跨厂商智能指数的 Artificial Analysis，以最高设置运行 Fable 5.2，将其智能表现排在 74 款模型首位，得分 65；成本则排在 73 款模型的第 73 位，每项指数测试任务 26.54 美元。两组数字描述的是同一个模型，区别在于它消耗了多少 token。

## 价格表怎么说

Anthropic 文档清楚列出了新费率。缓存读取每百万 token 收费 0.20 美元，批处理价格为基础价的一半；可选快速模式的生成速度最高提升至 2.5 倍，输入和输出价格分别为 16 美元和 80 美元。公司还表示，该模型的输出速度最高比 Fable 5.1 快 30%。TechCrunch 指出，Fable 如今比主要对手更便宜；《财富》（Fortune）称，Fable 5.2 比 OpenAI 的 GPT-6 Astra 便宜 20%，后者标价为 10 美元和 50 美元；缓存输入方面，Fable 为 0.20 美元，Astra 为 1 美元。

Mythos 5.2 采用相同价格。Anthropic 称，两者是同一个底层模型；Fable 配备网络安全和生物安全防护，面向所有客户开放，而 Mythos 面向获准加入公司 Cyber Verification 和 Life Sciences Verification Programs 的组织。两者价格相同，访问条件却不同。

## 指数测量了什么

Artificial Analysis 根据输入、缓存命中、缓存写入、推理和答案 token 的价格计算每项任务成本，再除以任务数量，并对指数中的 9 项评测加权。按这一口径，最高推理强度的 Fable 5.2 生成了 2.75 亿输出 token，可比较模型的中位数为 7,280 万。每项任务耗时 46.4 分钟，中位数为 12.7 分钟；首个答案 token 的等待时间为 216 秒。网站自己的摘要将该模型称为“特别昂贵”和“非常冗长”。

计算很简单。输出标价为 40 美元，中位数为 10 美元，是 4 倍；token 数量约为中位数的 3.8 倍。账单等于单价乘以用量，而在这个设置下，Fable 5.2 两项都很高。限制也应说明：这些是 Artificial Analysis 的任务，而非读者自己的任务；该数字只对应一个推理强度等级。

## Anthropic 指出的调节参数

Anthropic 并不否认推理强度的重要性。发布页面称，Claude 应用和 Claude Code 的默认值为 Medium，在 Medium 下，Fable 5.2 完成困难任务所需的 token 比 5.1 更少。在 FrontierCode 2.0 的早期测试中，Fable 5.2 在 High 强度下得分 45.3%，而 Opus 5.5 在 Max 下为 45.5%，前者每项任务成本约为后者一半。该基准测试衡量模型所作代码修改是否会被开源维护者合并。在 Perplexity 的 WANDR 数据收集基准测试中，Medium 强度以约 40% 的成本达到 Opus 5.5 的最佳分数。在 Humanity's Last Exam 中，Low 强度以不到十分之一的成本达到同样水平。在 Xhigh 强度下，模型在 FrontierCode 得分 49.1%，是 Anthropic 测试过的已发布模型中的最高分。

这些全是厂商早期测试图表。它们表明，仅仅一个参数，就能让同一模型处于成本曲线上非常不同的位置，独立数字也支持这一解读。文档对 Fable 的适用位置说得直接：大多数工作负载应先用最新的 Opus 模型，只有在更高推理强度下评测 Opus 仍无法“满足要求”时，才转向 Fable。

## 账单为何变成这样

Anthropic 以前也这样解释定价。9月22日的 Claude Opus 5.5 公告称，该模型在大多数工作中达到 Fable 5.1 水平，在典型工作负载上比 Opus 5 便宜 40%。每 token 价格降低了 20%，变为每百万输入和输出 token 分别 4 美元和 20 美元；公司表示，其余节省来自每项任务使用更少 token。按 Anthropic 自己的说法，账单就是费率乘以数量。

《The Pragmatic Engineer》作者 Gergely Orosz 在 10月20日的一期文章中，为这一效应提供了更具体的情况。他与 27 个工作场所的人讨论了每名开发者的 AI 支出，样本为自愿参与，大多匿名。他报告称，支出在 6月和 7月达到高峰；使用 API 方案的公司此后支出大约减半，大多数公司给出的原因是结合使用 Opus 5.5 和开放模型。一名工程师 9月在 Opus 5 上花费 2,200 美元，预计改用 Opus 5.5 后减半。Orosz 还了解到，多家公司的补贴订阅即将结束，账单可能因此涨至 5 至 10 倍。

Fable 5.2 正是在这样的成本计算中登场。一个为了把账单减半而转向 Opus 5.5 的买家，如今又面对更高一档的模型：每 token 价格下降了，但每项任务成本取决于一个大多数人不会调整的设置。

## 发布优惠，以及谁为试用付费

首周，订阅用户无需直接承受这一定价。Anthropic 帮助中心表示，11月9日至16日，Pro 套餐和标准 Team 席位可在每周限额内使用全部 Fable 模型，上限为周限额的 50%，并获得一次限额重置。Max 和 Ultra 套餐根据账户已付费时长，获得 1 至 3 次重置；未使用的重置机会于 2027年3月8日失效。这些优惠针对订阅套餐，页面没有提及 API 账户。

## 再看账单

回到虚构的星期一，负责人查看审计批次，没有发现结果有什么问题。她缺少的是对照。下一项测试很朴素：同样的 40 个仓库，先用 High，再用 Medium，并在每组旁边列出成本和被接受的发现数量。较便宜的运行能否发现足够多的问题，没有任何发布页面能替她的团队决定；她读到的文档也表达了同样的意思。模型按百万 token 定价，她的评审将按仓库衡量。

## 参考文献

- Anthropic (2026). *Introducing Claude Fable 5.2 and Claude Mythos 5.2*. https://www.anthropic.com/claude-fable-and-mythos-5-2
- Anthropic (2026). *Introducing Claude Opus 5.5*. https://www.anthropic.com/news/claude-opus-5-5
- Anthropic (2026). *Claude Fable 5.2 launch offers*. Claude Help Center. https://support.claude.com/en/articles/17506494-claude-fable-5-2-launch-offers
- Anthropic (2026). *What's new in Claude Fable 5.2*. Claude Platform Docs. https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2
- Artificial Analysis (2026). *Claude Fable 5.2 (Max): Intelligence, Performance & Price Analysis*. https://artificialanalysis.ai/models/claude-fable-5-2
- Brandom, R. (2026). *Anthropic releases new Mythos and Fable models amid RSI concerns*. TechCrunch. https://techcrunch.com/2026/11/09/anthropic-releases-new-mythos-and-fable-models-amid-rsi-concerns/
- Forlini, E. (2026). *Anthropic debuts Claude Fable, Mythos 5.2 models, priced 20% below OpenAI's GPT-6 Astra*. Fortune. https://fortune.com/2026/11/09/anthropic-debuts-updated-claude-fable-and-mythos-models-undercutting-price-of-openais-gpt-6-astra-by-up-to-80/
- Orosz, G. (2026). *What's the ROI of software engineers' spending on AI?* The Pragmatic Engineer. https://newsletter.pragmaticengineer.com/p/whats-the-roi-of-software-engineers
