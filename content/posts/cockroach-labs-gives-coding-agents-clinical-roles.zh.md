+++
title = "Cockroach Labs 给编程智能体分配临床角色"
slug = "cockroach-labs-gives-coding-agents-clinical-roles"
description = "MOLT Sinai 通过专门智能体、强制规划和对抗性审查处理软件工作。公司报告，五个月里发生七次回退。"
tags = ["agents", "tools", "essays"]
date = 2026-10-11T04:03:06+02:00
draft = false
+++

Cockroach Labs 描述了一条编程智能体（agent）流水线，把软件问题当作医院病人处理：设置专门角色，并在开始实施前强制审查。

这个名为 MOLT Sinai 的系统通过 GitHub Actions 运行。标签在分诊智能体、检查阶段、提出治疗方案的 Fellow、攻击方案的 Review Attending，以及出院阶段之间传递状态。作者称，五个月内处理了超过 100 万行代码，发生七次回退。

## 为什么重要 {#why-it-matters}

维护者把仓库变更委托给智能体时，需要的不只是强模型：流程还必须保持范围、展示决策，并在薄弱计划变成代码前将其阻止。MOLT Sinai 把这些要求转为工作流状态和书面技能，而非依赖一条长提示词或智能体的记忆。

最强的规则在于程序：没有计划不写代码，没有审查不通过计划。Review Attending 的指令是找错，而非本能地配合。如果工作超出批准范围，另一条规则要求“不要临场发挥”；智能体必须停下并重新规划。不能仅为让变更通过就削弱测试。

Cockroach Labs 工程师 Adam Storm 和 Rafi Shamim 报告，合并了 27 个拉取请求，审查者退回 55 次。他们描述，在不到两天内添加 Db2 迁移源，模型 token 成本为 4,172 美元。与耗时九个月、约 16 万美元的 Oracle 集成比较，说明了他们所声称的差异，但并非同等条件下的受控生产率研究。

设计刻意增加了程序负担。每次交接消耗 token 和时间，作者称流水线可能比智能体集群更慢、更贵。其目的不是最大并行，而是让从问题到合并代码的路径可检查，并为每个阶段分配不同责任。

可复用的想法比医院比喻更小：把状态放在聊天之外，要求明确计划，分离作者与批评者，并在智能体指令中写入停止条件。不必复制所有角色，也能采用这些控制。

Cockroach Labs 发布的是工程经验，而非独立评测。下一步证据应是仓库层面的数据，比较这条流水线与普通人类或智能体工作流处理相似任务的情况，包括审查时间、缺陷严重性，以及从未进入合并的工作。

## 核实 {#verification}

| 说法 | 标签 | 一手来源 | 独立核实 |
|---|---|---|---|
| MOLT Sinai 使用 GitHub Actions、标签和按角色分工的智能体，推动问题经过分阶段工作流 | 已核实 | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | 无 |
| 工作流要求写代码前先批准计划，并指示智能体在范围变化时重新规划 | 已核实 | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | 无 |
| Cockroach Labs 报告五个月中有 27 个合并拉取请求、55 次退回和七次回退 | 据公司称 | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | 无 |
| Db2 迁移源耗时不到两天，token 成本 4,172 美元 | 据公司称 | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | 无 |
| 作者称，相比智能体集群，系统增加了时间、成本和程序负担 | 已核实 | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | 无 |
