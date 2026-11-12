+++
title = "Token 支出反映谁在用智能体，难以衡量交付成果"
slug = "token-spend-tracks-who-uses-agents-not-what-gets-shipped"
description = "JetBrains 的研究将 5 周编程智能体 token 用量与 404 名工程师的提交关联。支出对个人的依赖远大于对当周产出的依赖，这让依据该数字制定的排行榜、目标和预算受到质疑。"
tags = ["business", "research", "agents"]
date = 2026-11-11T03:23:00+01:00
draft = false
+++

假设一位平台工程负责人在周一早晨打开 AI 服务商的月度账单。编程智能体一项的费用又增加了，她被要求在周三前解释原因。她做了一张很自然的图：一条轴是每名工程师的支出，另一条轴是已合并的工作。她预期看到一条上升曲线，结果却像散落的彩纸。两名产出相同的工程师，支出相差一个她无法解释的倍数；使用最多的人，也不是她会特别表扬其工作的人。这是虚构场景，用来在数字出现之前呈现问题。

现在，数字已经有了。11月10日，来自 JetBrains、卡内基梅隆大学（Carnegie Mellon University）和加州大学欧文分校（University of California, Irvine）的团队发表了题为 *The AI Era's Lines of Code?* 的预印本，追问工程师的 token 支出究竟衡量什么。作者为 Shyam Agarwal、Olga Lvova、Agnia Sergeyuk、Anastasiia Serova、Timofey Bryksin、Thomas Zimmermann 和 Bogdan Vasilescu。他们依据一家公司的数据得出的答案是：它衡量一个人有多少工作通过智能体完成，却很少说明这个人产出了什么。论文尚未经过同行评审。

## 未经检验就被采用的指标

作者指出，在有人研究 token 支出之前，公司就已把它当成管理数字。他们提到，一名 Meta 员工制作了排行榜，让同事争夺公司 token 使用量第一名；《财富》（Fortune）在 4月报道，媒体报道两天后，该榜单便被撤下。他们还列举了英伟达（Nvidia）和 Meta 高管的说法：优秀工程师应该使用价值占其工资很大一部分的 token；Salesforce 设定了每月最低支出目标；还有分析服务商将 token 成本除以合并的拉取请求数量，把这一比率称为投资回报率。

此后，质疑不断增加。论文称，Uber 在 4 个月内花光了 2026年 AI 编程工具预算，其首席运营官表示，token 支出与已交付功能之间的联系“还没有建立起来”。论文引用的一位批评者将 token 支出称为“AI 时代的代码行数指标：容易测量、容易操纵，与实际生产率脱节”。据作者对媒体报道的整理，Meta 后来告诉工程师，不会用 token 数量评估他们的贡献；亚马逊（Amazon）关闭了使用排行榜，并称 token 用量是一个“存在严重缺陷”的衡量标准。尚待回答的问题是：把使用日志与真实产出关联起来后，这些批评是否仍然成立。

## 遥测数据展示了什么

JetBrains 开发软件工具，当时约有 2,600 名员工。公司运行一个内部网关，记录每次编程智能体调用。研究人员选取了 2026年6月29日至8月2日的完整 5 周，将每名工程师每周的 token 用量与其代码提交匹配。面板数据覆盖 404 名工程师；日志包含 310 万次智能体调用。另有 412 名员工参加了独立的公司匿名调查。

在每个周提交次数区间内，以“工程师—周”为单位，支出第 90 百分位的 token 用量，是第 10 百分位的 39 至 240 倍。逐周跟踪同一个人，得到的关系比作者预期更平缓。一周提交次数达到该工程师通常水平的两倍时，token 费用约增加 20%。反过来，token 用量翻倍的一周，提交次数只增加约 10%。如果产出与支出成比例增长，这两个数字都应接近 100%；作者在尝试的每一种时间单位下都否定了比例关系。

大部分差异来自个人。工程师是谁，解释了每周 token 用量差异的 79%；使用最多的三分之一用户消耗了全部 token 的 79%。在 5 周中，支出最多的始终是同一批人。提交次数、修改行数和另外两项活动指标，合计解释了工程师间差异的 38%，以及同一人逐周差异的 13%。单看岗位和团队，预测支出的效果还不如直接使用平均值。

论文接着追问，多出的支出去向何处。完全没有提交的一周只占 token 用量的 4%，但作者根据最佳拟合曲线估计，最多约五分之二的支出不随当周提交次数变化。他们称这是上限，因为其中包括使用智能体本身的固定成本，以及人工编写提交背后的支出。他们还指出，大多数 token 是每轮重新发送的上下文；第三周出现了一款新的前沿模型，并在两周内占据了全部支出的 45%。

## 从未变成代码提交的工作

调查解释了部分差距。技术受访者对两款编程智能体给出了 197 份评价，其中 167 份回答了有关过去一周的问题。在这些评价中，91% 表示工具节省了时间，中位数为 10 小时。63% 的评价涉及用智能体编程，89% 涉及至少一种其他活动：分析数据、头脑风暴、研究主题、规划、学习或写作。只用智能体编程的受访者报告节省时间中位数为 3 小时；报告两种或更多非编程用途的人则为 10 小时。

部分价值来自原本不会开展的工作。在回答智能体主要收益的 74 份实质性答复中，31% 提到加快常规任务，30% 提到在不熟悉的代码、领域或技术中开展工作；一名受访者写道：“我可以尝试以前不敢尝试的事情。”在 44 份描述“只因为有智能体才开展”的工作中，36% 涉及不熟悉的代码库、语言或技术栈。调查也记录了成本。最常见的是错误或低质量输出，49% 的回答提及这一点；31% 的技术智能体用户报告认知负荷增加。作者补充说，自我报告可能夸大收益，并引用了一项 2025年随机试验：有经验的开源开发者使用 AI 工具后，耗时增加了 19%，却认为自己更快了。

## 对目标、预算和限额的意义

作者没有得出智能体不值得投资的结论。他们的结论针对的是衡量工具。如果同一工程师内部的关联具有因果性，那么通过目标将其支出翻倍，提交次数大约会增加 10%，范围为 2% 至 25%。他们建议，不要按支出评判工程师，也不要指望支出目标大幅提高产出。用支出除以产出也会以另一种方式误导，因为随着提交增加，每次提交的 token 数会机械性下降，让工程师在繁忙的一周看起来效率更高。

限额的问题最难处理。限额主要约束使用最多的人，而这一组与产出无关的支出占比，在 3 组中最低，为 36%，另两组分别为 51% 和 52%。由于他们消耗大部分 token，也持有大部分与产出无关的支出。因此，限额既削减服务于产出的支出，也削减不服务于产出的支出，而 token 数量无法区分二者。作者建议，在设限前先压缩或管理上下文、缓存重复上下文，并将常规调用路由到更便宜的模型；同时衡量实际账单成本，而非 token 数量，因为智能体重新读取被删内容时，精简上下文反而可能增加账单。

有两项局限值得重视。JetBrains 自己开发 AI 编程工具，因此部分计量使用可能是在测试自家智能体，而且其工程师工作于成熟代码库。使用是自愿的，没有目标，因此支出差异部分反映个人选择。提交次数也遗漏了审查和设计工作。作者强调，这些只是来自一家公司、持续 5 周的关联。

另一项作者部分重叠的研究展示了强制目标带来的后果。研究使用 802 名开发者和 196,212 个拉取请求的数据，考察一家中型公司；其首席技术官于 2025年6月设定目标，要借助 AI 将每名工程师合并的拉取请求数量翻倍。公司直到第 10 个月才达到目标，代价落在代码审查上，每名审查者的负荷翻了一倍。

## 数对该数的东西

JetBrains 的作者提出两项改进。网关应记录每次智能体会话服务于哪个问题或任务，使支出能与结果关联，而不只与代码提交关联。这个领域还需要经过验证的智能体辅助工作价值指标；作者目前不知道有这样的指标。他们表示，在此之前，支出适合资源核算，除此之外用途有限。衡量采用情况时，他们建议同时报告每周用户人数，以及不会随上下文大小增长的指标，例如在大多数工作日使用智能体的工程师占比。

回到那间虚构的办公室，平台工程负责人周三并没有削减任何人的预算。她要求网关团队增加一个字段，记录每次会话所属的工单，并告诉财务同事，那张彩纸般的散点图本身就是发现。账单仍会在每月第一天到达。它统计的是工程师有多频繁地借助智能体。这样做是否物有所值，是另一个问题，而账单上没有这一栏。

## 参考文献

- Agarwal, S., Lvova, O., Sergeyuk, A., Serova, A., Bryksin, T., Zimmermann, T., & Vasilescu, B. (2026). *The AI Era's Lines of Code? A Case Study on What an Engineer's Token Spend Measures*. https://arxiv.org/abs/2611.13396
- Arar, A. B. (2026). *Tokenmaxxing and the search for AI metrics that matter*. LeadDev. https://leaddev.com/ai/tokenmaxxing-and-the-search-for-ai-metrics-that-matter
- Becker, J., Rush, N., Barnes, E., & Rein, D. (2025). *Measuring the impact of early-2025 AI on experienced open-source developer productivity*. https://arxiv.org/abs/2507.09089
- Bharade, A. (2026). *Uber's COO says it's getting harder to justify the money spent on AI tokenmaxxing*. Business Insider, via Yahoo Finance. https://finance.yahoo.com/sectors/technology/articles/ubers-coo-says-getting-harder-050841491.html
- Cooter, M. (2026). *Meta minimizes role of token maxing in employee evaluations*. CIO. https://www.cio.com/article/4218661/meta-minimizes-role-of-token-maxing-in-employee-evaluations-2.html
- He, H., Agarwal, S., Denisov-Blanch, Y., Azaletskiy, P., Koyejo, S., & Vasilescu, B. (2026). *AI Writes Faster Than Humans Can Review: A Longitudinal Study of an Enterprise 2x Mandate*. https://arxiv.org/abs/2607.01904
- Munis, J. (2026). *A Meta employee created a dashboard so coworkers can compete to be the company's No. 1 AI token user*. Fortune. https://fortune.com/2026/04/09/meta-killed-employee-ai-token-dashboard/
- Palmer, A. (2026). *Amazon's anti-tokenmaxxing memo says engineers should be pickier about using AI*. CNBC. https://www.cnbc.com/2026/10/27/amazon-ai-coding-tokenmaxxing.html
