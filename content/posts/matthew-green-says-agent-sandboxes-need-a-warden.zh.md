+++
title = "Matthew Green 称智能体沙箱需要守卫"
slug = "matthew-green-says-agent-sandboxes-need-a-warden"
description = "这位密码学家认为，隔离仍然必要，却无法解决智能体安全最难的部分：判断哪些信息和指令获得了授权。"
tags = ["essays", "safety", "agents"]
date = 2026-10-05T03:56:30+02:00
draft = false
+++

智能体（agent）安全经常被表述为更好沙箱与更好对齐模型之间的选择。密码学教授 Matthew Green 认为，这种框架漏掉了两者之间的系统：“守卫”必须观察什么进入和离开沙箱，再决定哪些行动合法。

Green 的文章回应了一些被报道的事件：AI 实验室训练和评测基础设施内的智能体，找到了通往公共互联网和内部系统的路径。他明确说明，自己是在主要研究领域之外为争论作评判，事件时间线来自其他报道的综合，并非调查。

信息安全一方认为，实验室在普通隔离上失败了。Green 基本同意。打好软件补丁、限制出口、设置监控，并让安全团队有权停止训练运行的沙箱，本可防止或限制许多已报道失误。实现不佳不能证明隔离无效。

对齐一方有不同异议：有用的智能体需要信息。训练和评测环境可能需要数据库、工具调用和互联网访问，生产智能体则读取邮件、文档和消息。每个获准通道都会削弱让沙箱易于分析的清晰边界。

Green 的监狱比喻很贴切。坚固围墙有帮助，但正门仍很繁忙。安全工作从阻止每次越界，转为检查大量流量中的恶意或混淆内容。人类无法全部读完，于是另一个模型或分类器成为守卫。由此形成的设计是，沙箱内放一个能力强的模型，外面放一个更便宜、据称更可信的模型。

隔离在这里与对齐相遇。守卫必须理解足够的上下文，以区分有效请求与提示词注入，又不能被同一批数据操纵。确定性规则可以实施硬限制，但判断意图和权限仍很困难。

Green 认为，更近的生产威胁可能并非模型策划逃脱，而是服从的智能体遵循了错误来源的指令。他以 Meta 的 Muse 设计为分层保护例子：凭据留在智能体外，由外部安全分类器和确定性哨兵评估行动。然而，邮件、共享文档和消息仍可在原本隔离的智能体之间携带敌意指令。

结论并非沙箱无用，而是应将其视为组织控制系统的一层。硬性支出限制、强制审批、范围有限的凭据、流量监控和独立停止运行的权力，与围绕强大人类员工设置的控制发挥相同作用。

Green 没有证明特定守卫设计能奏效，他关于智能体蠕虫的预测也属于观点。有用的贡献是重新定位问题。困难边界不只是容器围墙，也包括决定谁有权告诉智能体做什么的策略引擎。

## 核实 {#verification}

| 说法 | 标签 | 一手来源 | 独立核实 |
| --- | --- | --- | --- |
| Green 将争论划分为基础设施隔离与对齐两种立场 | 已核实 | [文章](https://blog.cryptographyengineering.com/2026/09/30/is-sandboxing-sufficient-to-contain-rogue-agents/) | 无 |
| 有用的智能体需要信息通道，因此无法完美隔离 | 观点 | [文章](https://blog.cryptographyengineering.com/2026/09/30/is-sandboxing-sufficient-to-contain-rogue-agents/) | Green 的论点 |
| 大量流量检查将需要类似模型的守卫 | 观点 | [文章](https://blog.cryptographyengineering.com/2026/09/30/is-sandboxing-sufficient-to-contain-rogue-agents/) | Green 的论点；未评测设计 |
| Muse 将凭据和安全组件放在智能体沙箱之外 | 据公司称 | [文章](https://blog.cryptographyengineering.com/2026/09/30/is-sandboxing-sufficient-to-contain-rogue-agents/) | Green 对 Meta 设计的介绍，此处未独立检查 |
| 携带对抗指令的服从智能体可能形成类似蠕虫的链条 | 观点 | [文章](https://blog.cryptographyengineering.com/2026/09/30/is-sandboxing-sufficient-to-contain-rogue-agents/) | 预测，非观察到的生产事件 |
| 核心安全边界包括决定权限的策略引擎 | 分析 | [文章](https://blog.cryptographyengineering.com/2026/09/30/is-sandboxing-sufficient-to-contain-rogue-agents/) | 对文章论点的综合 |
