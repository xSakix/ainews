+++
title = "CoreWeave 短期 GPU 租金远高于长期合同"
slug = "coreweave-prices-short-gpu-rentals-far-above-long-contracts"
description = "CoreWeave 表示，GPU 价格在 7月上调约 25%，之后又上调 10%。目前短期容量年费超过每兆瓦 4,000 万美元，多年合同则为 2,000 万至 2,500 万美元。溢价让公司获益，但贷款方更青睐便宜的长期合同，其债券也反映了疑虑。"
tags = ["business", "hardware", "agents"]
date = 2026-11-12T03:15:32+01:00
draft = false
+++

设想一家银行的信贷分析师，所在银行以数据中心合同为依据放贷。她并排打开两份报价表，两者对应相同类型建筑中的同类容量。一份是大客户作出的 4 年承诺，价格看上去甚至有些低；另一份则是 3 个月租约，价格接近前者的两倍。第二份收入更多。她的工作是判断银行应依据哪份合同放贷，答案是第一份。这名分析师是为本文虚构的，但她的选择正是 CoreWeave 本周向投资者描述的情况。

CoreWeave 出租支撑 AI 的算力，于 11月10日星期二公布了第三季度业绩。季度营收为 36.6 亿美元，同比增长 168%，净亏损 7.09 亿美元，利息支出 8.46 亿美元。TechCrunch 的 Rebecca Bellan 在财报电话会报道中写道，公司“越来越多地要求客户预付款，以特定合同为依据借贷，甚至寻求可能带来更高价格的短期交易”。这 3 种做法背后，是同一个数字：急需 GPU 时，如今租用它要花多少钱。

## 报价表透露了什么

首席执行官 Michael Intrator 告诉分析师，CoreWeave 在 7月将各项服务价格提高了约 25%，随后在当季又提高了 10%；本季度价格仍在上涨，涨幅“足以抵消成本增加，而且还有余量”。如果两次涨价作用于相同的目录价格，复合涨幅约为 38%。公司并未表示情况确实如此。

更显眼的是不同合同期限之间的价差。Intrator 表示，CoreWeave 正在“把更多容量分配给定价合理的短期机会，以每兆瓦每年超过 4,000 万美元的价格出售容量；而 4 年和 5 年合同中新基础设施的定价，正在升至每兆瓦 2,000 万至 2,500 万美元”。简单计算可知，立即需要容量的客户，每兆瓦支付的费用比承诺多年使用的客户高出 60% 至 100%。

更早之前已有迹象。9月17日，CoreWeave 发布了一份题为 *CoreWeave Continues to Contract New Compute Capacity at Higher Prices*（CoreWeave 继续以更高价格签约新增算力容量）的公告。公告称，公司在第三季度签下了约 3 至 6 个月的短期合同，价格约为每兆瓦 4,000 万美元；它将这个指标定义为年化营收除以服务集群所需的电力。自 6月30日以来，公司新增客户承诺净额超过 250 亿美元，并表示已签约电力容量从约 3.7 GW 增至约 4.2 GW。公告没有说明发布原因，只是正式记录了新的价格水平。

涨价的不只是 CoreWeave。10月2日，《Quartz》报道，亚马逊云科技（Amazon Web Services）将 EC2 Capacity Blocks for ML 的价格提高约 15%。这类 GPU 预留时段涵盖从 A100 到 B300 的芯片。在美国主要区域，配备 8 个 H100 芯片的 p5.48xlarge 实例标价为每小时 41.528 美元。《Quartz》指出，亚马逊和英伟达（Nvidia）未回应置评请求。

## 为什么贷款方更想要便宜的合同

如果短期合同收入这么好，为什么不只卖短期合同？Bellan 从贷款方那里得到了答案：他们“更看重长期合同，即使价格较低，因为他们最重视可预测的现金流和持续偿还贷款的能力”。CoreWeave 靠借来的钱建设容量，因此，一个签约 5 年的客户对公司的价值，高于客户支付金额本身所体现的价值。8月，公司完成了一笔 26 亿美元贷款，专门面向期限较短的客户合同，可在需要资金时分批提取。Intrator 表示，公司不会“按当前收益率”进入无抵押债务市场，“我们也没有必要这样做”。

这些收益率体现了矛盾的另一面。据 Bellan 报道，上个月部分 CoreWeave 债券的收益率升至 15% 以上。10月22日，美联社（Associated Press）描述了 AI 股票因市场担忧数据中心和芯片融资成本过高而下跌的情况；CoreWeave 当天股价下跌 10.1%。到 11月6日，CNBC 的 Jordan Novet 和 Seema Mody 报道，CoreWeave、Nebius 和 IREN 的股价在一个月内各自下跌约一半，此前有报道称微软（Microsoft）正在缩减专注于 AI 算力的新型云服务商名单。微软告诉 CNBC，审查此类投资是“管理大型复杂基础设施项目的一种正常且负责任的方式”。其首席财务官 Amy Hood 在 10月财报电话会上曾表示，部分 GPU 云服务合同被推迟至 2027年上半年。

CoreWeave 的应对方式是先向客户要现金。公司预计未来 3 个月将收到约 90 亿美元预付款和定金，其中超过 30 亿美元对应已建成容量的新合同，不需要额外硬件投入。Bellan 指出，Nebius 和 IREN 也以同样方式依赖微软的大额预付款。预付款缓解了公司眼前的借贷需求，但 TechCrunch 指出了其中的问题：这让 CoreWeave 锁定了一个价格，如果需求继续上升，之后看起来可能不那么划算。公司公布的未履行订单金额为 1,325 亿美元。

## 买方能从中看出什么

对 GPU 租用者而言，这份报价表意味着一项明码标价的选择。能够预测需求并承诺使用多年的客户，支付较低费率，同时帮助供应商借贷。需要集中训练或应对推理需求激增的客户，则支付较高费率；只要需求持续，供应商就没有多少理由劝退他们。这种溢价究竟来自稀缺，还是尚未完成的扩建过程中的一个阶段，单凭公司的数字无法确定；上述每个数字都来自 CoreWeave，或转述其说法的记者。

Bellan 自己的结论是，这一策略“可能提高利润，但也带来更大的续约和定价风险”，并显示出 AI 基础设施热潮有多么依赖“持续、且尚未得到证明的需求”。

再设想一家小型初创公司的机器学习负责人，同样是虚构人物。就在公司准备审视资金还能支撑多久的那一天，她收到了一份为期 3 个月的容量报价。价格高于今年春天计划中的数字。她签了，因为模型必须交付；随后给自己写下提醒，下次要换个问题：不只是 GPU 多少钱，而是自己愿意承诺为它持续付费多久。与此同时，银行里的分析师正从另一端提出同样的问题。

## 参考文献

- Associated Press (2026). *Sharp drops for AI stocks overwhelm markets worldwide as oil prices jump*. The Guardian, 22 October. https://www.theguardian.com/business/2026/oct/22/stock-markets-drop-ai-oil
- Bellan, R. (2026). *CoreWeave turns to customer prepayments, shorter contracts to fund AI growth*. TechCrunch, 11 November. https://techcrunch.com/2026/11/11/coreweave-turns-to-customer-prepayments-shorter-contracts-to-fund-ai-growth/
- CoreWeave (2026). *CoreWeave Continues to Contract New Compute Capacity at Higher Prices*. Business Wire, 17 September. https://finviz.com/news/393022/coreweave-continues-to-contract-new-compute-capacity-at-higher-prices
- Novet, J., & Mody, S. (2026). *Microsoft moves to consolidate its relationships with neoclouds in AI*. CNBC, 6 November. https://www.cnbc.com/2026/11/06/microsoft-moves-to-consolidate-its-relationships-with-neoclouds-in-ai.html
- Tolomia, C. (2026). *Amazon hiking AI chip rental prices*. Quartz, via Yahoo Finance, 2 October. https://finance.yahoo.com/technology/ai/articles/amazon-hiking-ai-chip-rental-122155988.html
