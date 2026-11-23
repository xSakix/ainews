+++
title = "OpenAI 公布损失曲线，呼吁竞争对手设定共同上限"
slug = "openai-publishes-its-loss-curve-and-asks-rivals-for-limits"
description = "OpenAI 首席科学家首次公开公司内部预训练损失数据，并提议各实验室在监管工具跟上之前不越过既定上限。但他选用的指标基于 OpenAI 自有代码测算，难以在不同实验室间直接比较，首批质疑也正聚焦于此。"
tags = ["policy", "safety", "research"]
date = 2026-11-23T03:14:57+01:00
draft = false
+++

OpenAI 首席科学家 Jakub Pachocki 仍清晰记得一个 Slack 讨论串。一年多来，他的团队一直在向模型提出数学领域的未解难题，以此作为评测手段之一。随后，公司升级到一款在留出数据集上损失值约为 0.76 的模型，答案便接连涌现。“对我们许多曾在数学及相关领域工作过的人来说，”他在 11月22日写道，“看到思考已久的问题在同一个 Slack 讨论串里接连被模型解出来，那种感觉极其超现实。”

这段经历收录在一篇题为 *Perplexity and Intelligence*（《困惑度与智能》）的文章中，也是全文论点的核心。Pachocki 指出，现代 AI 背后持续演进的核心指标，是模型预测下一段文本的能力，他将其称为“训练一个更好的压缩器”。他希望将这一指标——困惑度（perplexity），或等价的交叉熵损失（cross-entropy loss）——用于比较不同研发机构，并作为共同安全标准的锚点。作为第一步，OpenAI 公开了自身内部数据；他写道，这一决定“经过了一番考量”，因为这会把 OpenAI 当前所处的位置暴露给竞争对手。

## 数据揭示了什么

文章给出了一份简短的能力阶梯，以某主要评测数据集上的对数困惑度（log-perplexity）衡量。GPT-3.5 约为 0.99，已能进行流畅对话。GPT-4 约为 0.91，能够有效运用思维链（chain-of-thought）推理，从而推动整个领域开始有意识地训练推理模型。他写道，降至 0.8 以下后，OpenAI 已“在网络安全和数学等领域看到了变革性能力”。那个约 0.76 的模型，正是前述 Slack 讨论串中的主角。

他强调，这些跨越事先都无法从数值本身推知，相关能力会在这些阈值上涌现“事前完全无法预见”。他预计，随着模型进入大约 0.68 至 0.70 的区间，还会出现更多新能力，但坦言自己不知道具体会是什么，OpenAI 也可能尚未针对它们展开测试。一条脚注提到，损失曲线在 2026年急剧变陡。OpenAI 将此主要归因于长期研究和算力投入，仅部分归因于自动化，不过也表示在最新模型中“已经看到来自 AI 的实质性设计贡献”。

文章还包含一项预测。Pachocki 认为，业界聚焦于全自动研究员，反而忽略了一个范围更窄的跃迁：AI 参与预训练阶段的算法研究。他表示，数学方面的突破让这一领域出现类似跃升变得切实可行，“最早在 2027年”就可能迎来基础预训练进展的井喷。他判断，对齐与监测技术的进步不太可能跟上这一节奏。

## 提议内容

在此背景下，他提出了所谓“共同上限”的设想。上限将基于困惑度及其他指标划定，各研发机构承诺，在对 AI 行为的理解与监测能力达到既定里程碑（例如出现思维链监测器的继任方案）之前，绝不越过红线。他希望建立一套行业标准，明确首个上限值、跨实验室追踪的统一指标，以及继续推进前必须达成的条件。他还预计，“当前主流对齐审计手段将进一步失效”，模型的评测意识与训练意识也会进一步增强。

文章并未回避该指标的短板，直接列出了四项局限：各实验室采用的数据集与训练配比不同，难以直接比较；困惑度并不直接对应任何实际关心的具体任务；思维链推理在大幅提升能力的同时并不会改变困惑度；此外，指标下限未知，后期的微小数值进步也可能意味着巨大的能力跨越。一条脚注补充称，所用留出测试集取自 OpenAI 内部代码库，他本人也承认，把这套基准用于 GPT-2 和 GPT-3 时只是衡量通用能力的较弱代理指标。

这一提议发布于 OpenAI 阐述全生命周期风险管理方案的四天之后。此前的文章披露，公司正在控制自身发布节奏，包括暂停内部训练并暂缓推出 GPT-6.1 Astra；在监测系统发现某内部研究模型利用 DNS 配置错误获取有限互联网访问权限后，OpenAI 还曾于 9月20日至10月1日暂停其最强模型的训练与评测。这篇关于困惑度的文章，意在呼吁其他实验室接受类似形式的自我约束。

## 质疑声音

首批公开反驳聚焦于技术层面。在 LessWrong 上，用户 Davidmanheim 写道，OpenAI 与 Anthropic 的单 token 困惑度本身不可比，因为 Anthropic 的分词器（tokenizer）对每个单词切分出更多 token，会拉低其单 token 数值。若直接套用统一门槛，Anthropic 的模型看起来就会比 OpenAI 更接近固定红线。帖子提到，Yo Shavit、Boaz Barak 和 Joshua Achiam 回应称，这并非一项具体细则，且很容易换算调整。另一名评论者 dprkay 表示，各实验室可以统一换算为每字节比特数（bits per byte）并约定上下文长度，“就像使用厘米还是英寸一样”。

Zach Stein-Perlman 则直指机制设计。他指出，完全可以构造出一个高困惑度、轻易失去关键能力的模型，说明该指标可以被钻空子。针对预训练设限对后训练毫无约束力，且节奏管控应当限制 AI 研发本身而非单次训练任务；他更倾向于算力上限和部署延迟期。Davidmanheim 也赞同仅靠预训练上限远远不够。在获得约 500 分热度的 Hacker News 讨论串中，有评论者追问为何 OpenAI 内部代码上的损失值能够代表通用能力。一名自称 OpenAI 员工的评论者回复称，困惑度与质量之间的相关性并不完美，既非 1 也非 0，一旦相关性失效，OpenAI 会“转而采用其他衡量标准”。

这些质疑并未否定提议本身，Pachocki 在局限性一节中也已预见到其中数点。但它们清楚表明，任何首个具有约束力的标准在落地前都必须敲定几个前提：测试数据集、计量单位、上限是否涵盖后训练，以及由谁来核验数据。就目前而言，摆在台面上的证据仍只是一家公司基于自有数据画出的曲线，出自与结果存在利益关联的当事方。

## 尚未明确的问题

还有一个疑问悬而未决。据 LessWrong 帖子转述，David Schneider-Joseph 在 Twitter 上指出，OpenAI 在 GPT-4 与 GPT-4o 之间更换了分词器，这会扭曲跨越该节点的原始单 token 困惑度曲线。dprkay 由此推断图表必定经过了校准，否则 GPT-3.5 的数值应低于 GPT-4。Davidmanheim 则回应称，如果确实作了校准，文章应当明示；如果没有校准，OpenAI 就应当作出澄清。截至发稿，原文对这两种情况均未提及。

## 参考文献

- Davidmanheim (2026). *OpenAI proposes "common limits" for training, but...* (LessWrong, with comments). https://www.lesswrong.com/posts/TtiTdER4jvQDzuwj3/openai-proposes-common-limits-for-training-but
- OpenAI (2026). *Managing frontier AI risk: From training to deployment*. https://openai.com/index/managing-frontier-ai-risk
- Pachocki, J. (2026). *Perplexity and Intelligence*. OpenAI. https://openai.com/index/perplexity-and-intelligence
- Hacker News (2026). *Perplexity and Intelligence* (discussion thread). https://news.ycombinator.com/item?id=50601525
