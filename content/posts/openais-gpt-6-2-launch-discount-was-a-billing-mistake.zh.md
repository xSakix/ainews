+++
title = "OpenAI 称 GPT-6.2 上线时的折扣源于计费错误"
slug = "openais-gpt-6-2-launch-discount-was-a-billing-mistake"
description = "OpenAI 表示，GPT-6.2 Astra 和 Sol 上线后有九天错误地少扣了套餐额度，纠正后订阅用户用完额度的速度分别加快了 40% 和 25%。与此同时，一项独立测量发现这两个模型在推理上花费更少，而这次纠错也显示，外界能核实的包月套餐细节相当有限。"
tags = ["business", "tools"]
date = 2026-11-27T03:17:17+01:00
draft = false
+++

一名 OpenAI 工程师发帖后，Hacker News 的讨论串里挤满了查看自己用量表的用户。网名 seviu 的用户写道：“昨天晚上我的额度还剩将近 90%，今天一觉醒来就全没了。”他订阅了 Pro 套餐，夜间也没让智能体继续工作。另一名用户 ragequittah 回忆起前一周，印象恰好相反：“用上六个小时 Astra 才花 3%。”

在这两次读数之间，是工程师发的那条帖子，以及包月套餐计算一天工作量的方式发生的一次变化。

## 计费纠错

协调世界时 11月26日 02:50，在 OpenAI 参与 Codex 和 ChatGPT 开发的 Thibault Sottiaux 在 X 上写道：“我们在 GPT-6.2 上线时出了计费错误，误给大多数用户的 GPT-6.2 Astra 和 Sol 用量打了折。”他说，修正后，“完成同样的工作会消耗更多套餐额度”。与前一周相比，订阅用户“用 GPT-6.2 Astra 时，达到上限的速度会快 40%，用 Sol 时会快 25%”。他补充说，同样的额度用这两个模型应该仍比用 GPT-6 Astra 和 GPT-6.1 Sol 能做更多事。其他模型不受影响，OpenAI 也不会追收此前的差额。作为致歉，所有 Go、Plus、Pro 和 Business 用户都将获得一次可留待以后使用的额度重置机会。

这组数字需要换算。额度消耗速度加快 40%，意味着同样的额度大约少做 29% 的任务，因为 1 除以 1.4 约等于 0.71。消耗加快 25%，意味着少做 20%。这只是根据 OpenAI 的措辞推算的结果，公司并未公布实际扣费率。

当时距模型上线只有九天。OpenAI 于 11月17日推出 GPT-6.2 Astra 和 Sol，GitHub 将两者引入 Copilot 时给出的也是这个日期。发布时的一大卖点就是节省用量：这两个模型“在高难度任务上能以更少的输出 token 取得更好的结果，因此在使用额度内可以完成更多工作”，而 Sol“能在同一个付费套餐下完成更多任务”。在 API 中，Astra 的 token 价格下调了 20%，每百万输入 token 为 8 美元，每百万输出 token 为 40 美元，与 Anthropic 于 11月9日为 Claude Fable 5.2 定下的标价相同。Sol 沿用了 GPT-6.1 Sol 的 2 美元和 10 美元定价。

这次改动并未涉及 API 价格。ChatGPT 付费套餐用另一种单位计费，即每次用掉的额度占比。每项任务按什么速率消耗额度，由 OpenAI 在内部决定。11月27日查阅的 OpenAI 定价页列出了每百万 token 所需的点数：Astra 输入为 200 点，输出为 1,000 点，均比 GPT-6 Astra 的 250 点和 1,250 点低五分之一。Sol 仍是 50 点和 250 点。该页还估计，Plus 用户每五小时可向本地 Codex 发送的消息数，使用 GPT-6.2 Astra 时为 6 至 50 条，使用 Sol 时为 17 至 180 条；使用 GPT-6 Astra 和 GPT-6.1 Sol 时则分别为 5 至 45 条和 15 至 160 条。页面称这些估算“不是固定的消息条数上限”，并写道：“Pro 套餐目前没有五小时上限。”此外，还可能设有每周上限。

从 6 条到 50 条这样一个区间，既不能证实也不能否定 40% 的说法。页面也没有说明表格是否在纠错后更新过。seviu 所说的额度一夜清零只是一名用户未经证实的经历，原因可能是这次调整，也可能是触及了每周上限。

## 讨论串里的分歧

这条帖子被转引到 Hacker News 后，标题将其概括为削减用量，获得了 468 点。读者对帖子含义的看法不一。有人接受“计费错误”这一解释。一名用户写道，自己花了好几个小时使用 Astra 6.2，用量表却仍显示 100%，于是去排查显示组件是不是出了故障。另一些人认为，这是借修复缺陷变相涨价。还有人说自己已取消订阅，或正在考虑 Anthropic 和谷歌（Google）的服务。另一名用户提到，OpenAI 最初发的邮件很简短，后来不得不再发一封解释。这些都是个人叙述，并非测量结果。

讨论中还有人回忆两家服务此消彼长的过程。一名长期同时使用 OpenAI 和 Anthropic 的用户说，以前 OpenAI 不断重置额度，让人觉得用量没有上限；后来 Opus 5.5 给的用量更多，OpenAI 的应对却是削减额度。另一名用户回复说，这类服务从一开始就是两家交替占优，将来也还会如此。这两种说法都是回忆，都不是对任何套餐实际用量的记录。

## 对同一批模型的另一种测量

11月26日，也就是 Sottiaux 发帖几小时后，模型对战评测平台 Agent Duel 的开发者发表了题为 *OpenAI may be in cost control mode* 的文章。Agent Duel 基于编程智能体 OpenCode，让模型在真实任务中相互较量，再按 Elo 积分排名。据作者报告，在相同的对局中面对相同对手时，Astra 6.2 和 Sol 6.2 每项任务消耗的输出 token 和推理 token 均少于各自的前代。作者给出的输出 token 检验 p 值，Sol 为 0.0055，Astra 为 0.022；推理 token 的 p 值分别为 0.00013 和 0.0064。他认为，这些模型“似乎针对成本做了调优”，已经到了“思考得异常少”的地步。

“成本”是作者的解释。数据能显示模型在推理上花费更少，却无法说明原因。OpenAI 在发布公告中把减少输出 token 列为优点，并称 Astra 在内部基准测试 GDPval v2 上比 GPT-6 Astra 高出 6.2 分，同时少用了 22% 的输出 token。同一结果既可以解释为提高效率，也可以解释为削减开支，只有 OpenAI 知道原因。token 数量减少也解释不了计费错误，因为后者涉及的是 token 按什么比例从额度中扣除。

这份榜单生成于协调世界时 11月27日 03:00，也无法给出定论。GPT-6.2 Astra 排名第五，Elo 积分为 1,007，上下浮动区间为 61 分，每项任务花费 2.33 美元，用时 2.6 分钟。Sol 排名第十二，积分 937，每项任务花费 0.43 美元，用时 1.7 分钟。Claude Fable 5.2 以 1,069 分居首，每项任务花费 3.49 美元；Claude Opus 5.5 以 1,060 分紧随其后，每项任务花费 1.63 美元。各模型的区间有很大重叠，Astra 的合理名次范围从第二到第十一。

## 订阅用户能核实什么

标价与实际账单不一致，以前也有过。11月9日，Anthropic 把 Fable 5.2 的输入和输出价格降至每百万 token 分别 8 美元和 40 美元，比前代低五分之一。但在 Artificial Analysis 上榜模型的成本排名中，它仍然垫底，在 Intelligence Index 中每项任务要花 26.54 美元。原因在于，账单取决于模型实际选择消耗多少 token。OpenAI 这次的情况还多了一层。对订阅用户来说，有三个数字由服务商决定：模型用多少 token、这些 token 按什么比例扣减额度，以及额度总共有多少。OpenAI 称，最初九天算错的正是其中的扣减比例。

外界可以像 Agent Duel 那样测出第一项。至于另外两项，用户只能看用量表。对于看到额度已经归零的人，定价页上有这样一句话：“看起来相似的任务，消耗的额度可能不同。”

## 参考文献

- Agent Duel (2026). *Agent Duel Leaderboard*, generated 27 November 2026. https://agentduel.com/leaderboard
- Anthropic (2026). *Introducing Claude Fable 5.2 and Claude Mythos 5.2*. https://www.anthropic.com/claude-fable-and-mythos-5-2
- Artificial Analysis (2026). *Claude Fable 5.2 (Max): Intelligence, Performance & Price Analysis*. https://artificialanalysis.ai/models/claude-fable-5-2
- GitHub (2026). *OpenAI's GPT-6.2 Astra and GPT-6.2 Sol now available*. GitHub Changelog, 17 November. https://github.blog/changelog/2026-11-17-openais-gpt-6-2-astra-and-gpt-6-2-sol-now-available
- Hacker News (2026). *OpenAI cuts GPT-6.2 usage: Astra hits limits 40% faster, Sol 25% faster*. https://news.ycombinator.com/item?id=50651117
- micjm (2026). *OpenAI may be in cost control mode*. https://micjm.com/blog/openai-is-in-cost-control-mode/
- OpenAI (2026). *Introducing GPT-6.2 Astra and Sol*. https://openai.com/index/introducing-gpt-6-2-astra-sol
- OpenAI (2026). *Pricing*. ChatGPT Learn. https://learn.chatgpt.com/docs/pricing
- Sottiaux, T. (2026). Post on X about the GPT-6.2 billing mistake, 26 November. https://x.com/thsottiaux/status/2125784147889393806
