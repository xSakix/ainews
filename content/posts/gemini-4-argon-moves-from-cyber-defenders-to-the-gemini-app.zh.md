+++
title = "Gemini 4 Argon 从网络防守者走向 Gemini 应用"
slug = "gemini-4-argon-moves-from-cyber-defenders-to-the-gemini-app"
description = "仅向封闭网络防守团队展示 Gemini 4 Argon 的 13 天后，谷歌已向 Gemini 应用付费订阅用户及开发者开放旗舰模型。谷歌承诺回答更直接；独立排名将它在一张榜单上列为第一，在另一张列为第八。"
tags = ["models", "tools", "safety"]
date = 2026-10-13T22:54:03+02:00
draft = false
+++

布尔诺的一名记账员手上有 3 份供应商合同、一份从会计程序导出的账簿，程序把每个捷克语变音符号都弄坏了，还有一位客户要求周三前交出对账说明。周二晚上，她打开 Gemini 应用，习惯性点击模型菜单，发现一个早上还没有的名字：4 Argon，就在 3.1 Pro 和 3.8 Flash 旁边。她把所有材料粘贴进去，并自己加了一行：不要开场白，也不要总结我刚才提供的内容。本文没有采访任何符合这一描述的人。她是谷歌（Google）如今争取的订阅用户的虚构轮廓，也是发布说明中“分析复杂财务报告”或“从分散来源创建演示文稿”的那类人。

## 从封闭计划到应用，只隔两周

根据应用发布说明，谷歌于 10月13日开始“在全球向 Gemini 应用中的 Google AI Pro 和 Ultra 订阅用户”推出 Gemini 4 Argon。同一天，模型以 gemini-4-argon 名称在 Gemini API 中全面可用，开放于 Google AI Studio 和 Android Studio，并进入谷歌 Antigravity 编程工具，供 Ultra 订阅用户及符合条件的 Gemini Enterprise 客户使用。9to5Google 报道，Pro 和 Ultra 用户还可在 Google Search 的 AI Mode 中选择它。Android Police 指出，免费用户与较便宜的 AI Plus 订阅用户尚未获得访问，其评测者本人订阅 Pro，也仍在等待模型出现。

13 天前，圈子小得多。Google DeepMind 高级副总裁、谷歌首席 AI 架构师 Koray Kavukcuoglu 于 9月30日宣布 Argon 时，模型仅向谷歌 Fairwind Program 中“一组可信网络防守者”开放。谷歌称，正在参与美国政府自愿的模型发布前访问流程，并会继续完善护栏，然后“尽快向开发者、企业和消费者”开放 Argon，首先面向付费 API 客户及 Ultra 订阅用户。周二的发布比这一安排多覆盖了一个订阅层级，将 Pro 也纳入。

Fairwind 比模型也没早多少。谷歌安全与隐私副总裁 Four Flynn 于 9月2日推出这一有限访问计划，面向政府、关键基础设施运营者和安全公司，围绕较小的专用模型 Gemini 3.8 Flash Cyber 及补丁工具 CodeMender 构建。参与者同意将访问限制在其安全、事件响应或渗透测试团队内。谷歌称，有超过 650 家合作伙伴参与。

## 谷歌称输入者的体验发生了什么变化

应用公告很短，大部分讨论表达方式。谷歌写道，Argon“更直接地回答问题，减少保留措辞，不作超出必要程度的重复，并在回答中跳过陈词滥调”。在较长任务中，它“通过更频繁、更有效地分享进展，让用户了解情况”。据 9to5Google，谷歌还称，Argon 比以往任何 Gemini 模型都更可靠地遵循风格指令。

其他变化同时到来。主聊天窗口的开关如今可从聊天切换到任务模式，谷歌称，在该模式下 Gemini 可以“即使用户不在电脑前”也继续工作。可以连接超过 40 个外部服务，包括 Instacart、OpenTable、Adobe 和 Shopify，不过发布说明称，多数仅在美国以英语工作。在 Mac 上，Antigravity 的智能体式编程界面如今位于 Gemini 应用内：用户批准编程智能体计划后回到聊天，智能体在后台构建并测试代码完成时，会通知用户。

消费端宣传背后是谷歌 9月关于长时间工作的主张。Argon 输出上限从 6.4 万增至 100 万 token，谷歌称，这让模型能够“在单条轨迹中生成数十万个 token”。开发者文档更精确：默认 65,536 个输出 token，在称为 long decode 的模式中最高 1,048,576 个，位于同样大小的共享输入输出窗口内。

## 外部排名如何定位它

谷歌自己的数字显示，Argon 在测试长时间软件工程任务的 DeepSWE v1.1 上为 77.9%，在 Zapier AutomationBench 上为 51.3%，在长视频基准 LVBench 上为 91.7%。在检查模型能否修复安全漏洞的 CWE-bench v1 上，谷歌称 Argon 以 68% 并列第一。这些是厂商数字。VentureBeat 指出，在衡量命令行工具编程的 Terminal-Bench 4.0 上，Anthropic 的 Claude Opus 5.5 得分 66.4%，“Argon 则为 57.4%”。

两张独立榜单对 Argon 领先程度看法不同。Vals AI 按各行业占美国 GDP 的比例加权金融、编程、法律和税务任务，截至 10月13日将 Argon 以 68.90% 排在第一，领先于 Claude Sonnet 5.5 的 67.04 和 Claude Opus 5.5 的 66.97。Artificial Analysis 给 Argon 高推理强度设置的 Intelligence Index 分数为 53，在所列 216 个模型中排第 8。Vals 表中的领先不到 2 个点，而在 Artificial Analysis 上，Argon 根本没有领先。

Artificial Analysis 页面有一个数字，与少说话的承诺并不协调。为完成该指数，Argon 生成 1.1 亿输出 token，中位数为 8,500 万，网站称其“有些冗长”。订阅用户读到的回答与生成回答所做的工作分别测量，谷歌的承诺针对前者。

## 公开版本的护栏

谷歌对安全防护的说明，比外部测试者对模型的说明更多。发布文章称，Argon 被设计为拒绝协助网络攻击，以及化学、生物、放射性和核武器；谷歌监测模型内部激活中的滥用迹象，另一系统读取 Argon 的思维链与操作，并在它试图超出用户意图时停止它。对于可信防守者和自有团队，谷歌称会“没有网络护栏”地发布 Argon。订阅用户得到的是有防护版本。

政府确实在更广泛发布前进行了查看。除了谷歌描述的美国流程，《卫报》（Guardian）报道，英国 AI 部长 Kanishka Narayan 于 10月12日在伦敦表示，AI Security Institute 科学家“目前正在对最新几代模型进行严格评测”，并点名谷歌 Gemini。报道没有说明哪个版本。该报道和谷歌公告都没有说明评测者发现了什么，或模型是否因此改变。

## 价格，以及 Argon 面向的任务

开发者在 11月30日前支付每百万输入 token 2 美元、每百万输出 token 10 美元的首发价，缓存输入便宜 95%。据 VentureBeat 和 9to5Google 报道，12月1日起价格翻倍至 4 美元和 20 美元。

Antigravity 团队文章有一句话为发布定了位置：“尽管 Argon 专为解决最困难的问题而设计，我们同样期待未来模型能成为日常主力，服务更广泛的构建者。”它把 Argon 放在工作中耗时长、成本高的一端，将日常用途留给谷歌尚未发布的模型。

谷歌提供的长任务证据来自公司内部。它称，Alphabet 每月有超过 10 万人使用内部 Antigravity 版本中的 Argon，4 周内智能体编写的代码量增加 35%，代码提交后的回滚减少 30%。在一个案例中，Argon 审计一批访问控制变更，发现 4 个严重安全错误，而两个早期前沿模型已审查这些代码并称其没有问题。谷歌没有点名任何一个模型，也未发布审计；这些是公司对自身工作的叙述。

回到布尔诺，为本文虚构的记账员得到了一份 4 个短段落的说明，没有开头赞美，也没有复述她粘贴的内容。她仍然逐行用账簿核对总数，就像模型菜单还停在 3.1 Pro 时一样。

## 参考文献

- Artificial Analysis. (2026). *Gemini 4 Argon (High): Intelligence, Performance & Price Analysis*. https://artificialanalysis.ai/models/gemini-4-argon
- Bhatia, S. (2026). *Gemini 4 Argon is here, and Google says it'll finally cut down on the AI fluff*. Android Police. https://www.androidpolice.com/gemini-4-argon-available-pro-ultra-subscribers/
- Flynn, F. (2026). *Proactive cyber defense for governments and enterprises*. Google. https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/
- Franzen, C. (2026). *Google makes Gemini 4 Argon broadly available with limited-time low API pricing of $2/$10 per 1M token*. VentureBeat. https://venturebeat.com/technology/google-makes-gemini-4-argon-broadly-available-with-limited-time-low-api-pricing-of-2-10-per-1m-token
- Google. (2026). *Gemini 4 Argon comes to the Gemini app*. https://blog.google/innovation-and-ai/products/gemini-app/gemini-4-argon-availability/
- Google. (2026). *Gemini 4 Argon is now available for developers*. https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-4-argon/
- Google. (2026). *Gemini Apps' release updates & improvements*. https://gemini.google/release-notes/
- Google AI for Developers. (2026). *Gemini 4 Argon*. https://ai.google.dev/gemini-api/docs/models/gemini-4-argon
- Google AI for Developers. (2026). *Gemini API release notes*. https://ai.google.dev/gemini-api/docs/changelog
- Google Antigravity Team. (2026). *Gemini 4 Argon in Google Antigravity*. https://antigravity.google/blog/gemini-4-argon-in-google-antigravity
- Kavukcuoglu, K. (2026). *Gemini 4 Argon: our next era of frontier intelligence*. Google. https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/
- Li, A. (2026). *Gemini app rolling out Gemini 4 Argon to AI Pro and AI Ultra*. 9to5Google. https://9to5google.com/2026/10/13/gemini-app-4-argon/
- Milmo, D. (2026). *Cyber-attack similar to OpenAI Medicare breach seems likely in UK, says minister*. The Guardian. https://www.theguardian.com/technology/2026/oct/12/cyber-attack-like-openai-medicare-breach-seems-likely-in-uk-says-minister
- Vals AI. (2026). *Vals Index*. https://www.vals.ai/benchmarks/vals_index
