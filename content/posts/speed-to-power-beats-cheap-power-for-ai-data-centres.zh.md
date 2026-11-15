+++
title = "AI 数据中心更看重供电速度，而非低电价"
slug = "speed-to-power-beats-cheap-power-for-ai-data-centres"
description = "卡内基梅隆大学与伯克利的一篇预印本，为数据中心等待电力而闲置的月份计价，发现离网太阳能加电池在美国本土 85% 的地点胜出，尽管其每千瓦时成本很少最低。Anthropic 寻找天然气供应主管展示了另一种选择，而模型的局限揭示了结论可能失效的地方。"
tags = ["business", "hardware", "research"]
date = 2026-11-14T07:22:33+01:00
draft = false
+++

本月初，Anthropic 发布了“天然气供应与运输负责人”的招聘信息，这是该公司首个专门负责美国和加拿大数据中心天然气供应的岗位。Business Insider 于 11月13日报道了这则信息。岗位薪酬为 32 万至 405,000 美元，其中直白地描述了一项依赖：“我们的一些园区将采用电表后端的燃气发电。”招聘信息写道：“在这些站点，燃料就是电力供应：如果天然气不能以电厂所需的气量和压力送达，算力就无法运行。”

这句话体现了一点工程上的坦诚，也处于 AI 公司应如何获取电力的更大争论之中。卡内基梅隆大学（Carnegie Mellon University）与加州大学伯克利分校（University of California, Berkeley）的 Alex Newkirk 及同事，于 11月12日发布预印本，用模型探讨这场争论。论文尚未经过同行评审。它认为，每千瓦时价格并不是正确的比较指标，因为决定结果的是芯片要等多久才能获得电力。

## 为什么等待是主要成本

作者从瓶颈入手。他们写道，一些地区的电网接入排队超过五年，接入所需的变压器、断路器和电工钢也往往积压多年。论文给出的新燃气轮机等候时间为四至七年。企业的应对方式包括签订独家购电协议，以及在现场建设发电设施，有时完全脱离电网、独立运行。

论文比较了为一座拥有 10 万块 GPU、设计负荷约 131 MW 的设施供电的四种方式：以交流方式连接的太阳能电池板加电池储能、采用直流方式的同类系统、孤网天然气发电，以及接入电网。直流耦合在逆变之前连接电池板与储能电池，从而减少逆变器和部分转换损耗。芯片本身已经使用直流电。模型发现，在美国本土范围内，这平均可节省 18% 的全生命周期能源成本，即每千瓦时约 9 美分。对于得克萨斯西部二叠纪盆地的一座设施，模型算得直流方案每千瓦时 0.27 美元，交流方案 0.33 美元，现值相差 5.7 亿美元。

关键步骤是作者提出的新指标，称为“按供电速度调整的能源成本”。建成的建筑每等待供电一个月，其 GPU 就有一个月没有收入；模型按每 GPU 小时 2.40 美元计算闲置成本。这是一个 H100 租赁指数价格，作者将其作为芯片每小时价值的下限。他们依据此前的一份行业报告，为太阳能和电池设定 24 个月的工期。燃气电厂依据联邦成本研究，设定建设时间为 40 至 42 个月，并假设燃气轮机交付需要 36 个月。电网接入则采用各地区过去排队时间的中位数，按州不同，为两年半至五年。

仅看能源成本，直流太阳能很少是最便宜的方案。一旦将闲置月份计价，它就在模型覆盖的 84.9% 地点成为成本最低的选择。工业电价便宜且排队快的地方，电网供电胜出：作者列举了接入速度全国最快的缅因州，以及工业电价低于 6 美分、接入需要三年的得克萨斯东部和佐治亚州。在基线情景中，天然气仅在少数地方胜出，因为天然气便宜的地方，电网供电往往也便宜。

## 结果能适用到什么范围

结论依赖两项假设，作者对两者都进行了测试。如果芯片每小时对其所有者的价值低于 2.40 美元，等待成本就会更低。他们发现，企业对太阳能与电网两种方案不再有成本偏好时，对应的小时价值中位数为 1.61 美元，全国大多数地方的这一临界值都低于 2.40 美元的基线。如果燃气电厂能在三年内运行——作者称这需要理想化的并行建设，或燃气轮机大幅提前交付——太阳能仍在约 55% 的地点领先，天然气在约 35% 的地点领先，主要位于日照不足的中西部北部、阿巴拉契亚盆地和太平洋西北地区，电网则在约 9% 的地点领先。天然气发电也会随规模扩大而变便宜。10 至 20 MW 的小电厂每千瓦时成本为 25 至 30 美分；在论文展示的科罗拉多州案例中，天然气发电在约 30 MW 时与直流太阳能成本相当。

可靠性是两种选择差异最大的地方。模型将每套系统的规模设定为在 99% 的小时内满足全部负荷。对太阳能而言，作者发现，成本与连续五天最差日照情况的关系，远比与全年平均日照的关系更密切：科罗拉多州一处干燥站点与加利福尼亚州北部一处易起雾站点，年日照量相近，但成本分别为每千瓦时 0.21 美元和 0.61 美元。燃气电厂面临另一种与管道有关的天气风险，这也正是 Anthropic 招聘信息关注的内容。它要求新员工设计“第二路管道供气、储气、备用燃料、寒冷天气性能，以及限供优先级”。

作者列出的局限相当重要。模型把电网接入视为等待之后按工业电价购电，没有计入公用事业公司可能转嫁给其他用户的升级成本，因此电网方案数字是下限。假设采用的直流设备尚不成熟：设计标准还未编定，部分故障保护设备尚未上市，熟练劳动力主要围绕交流系统培养。作者表示，早期项目可能只能实现部分节省。他们假设，数百至数千英亩太阳能场的土地可以无延误地取得，同时指出，如果太阳能审批比天然气更久，结果可能改变。他们考察的燃气方案是燃气轮机，因此交付时间不同的发动机订单不在测试范围内。

## 买方正在做什么

Anthropic 自身的申报文件和招聘展示了对天然气的押注。Business Insider 报道，其首次公开募股（IPO）招股书称，公司预计在一些参与建设数据中心的地区将面临天然气竞争；它已承诺约 9,000 亿美元的基础设施支出，其中约一半将在 2030年前到期。根据 Business Insider 的转述，《金融时报》（Financial Times）本周报道，该公司正向一家得克萨斯供应商购买总容量 1.7 GW 的一批燃气发动机，支出 34 亿美元。招股书警告，依赖天然气会带来成本波动和延误风险，而且随着“公众和政治界对气候变化看法的转变”，环境标准也可能变化。

另外两件近期事件为论文中的数字提供了背景。11月10日，CoreWeave 首席执行官告诉投资者，公司短期容量售价超过每 MW 每年 4,000 万美元，而四年和五年合同的价格为 2,000 万至 2,500 万美元。另据 Semafor 报道，11月3日，9 个州的 30 多个地区的选民支持暂停、禁止或以其他方式限制数据中心。作者将土地成本视为可忽略不计，但承认选址争议可能以不同程度延长工期，而太阳能场需要的土地远多于燃气电厂。

作者最后呼吁开展测量。一座 100 MW 或更大规模的直流园区尚未建成运行，在此之前，论文中的节省都只是预期值。招聘信息则聚焦于更窄的问题。Anthropic 要求其首位天然气负责人在选址初期就查明，“哪些站点真正有可行的燃料供应路径，哪些没有”。

## 参考文献

- Anthropic (2026). *Gas Supply and Transport Lead, US and Canada* (job listing). https://job-boards.greenhouse.io/anthropic/jobs/5469337008
- Baranko, K., Campbell, D., Hausfather, Z., McWalter, J., & Ransohoff, N. (2024). *Fast, scalable, clean, and cheap enough: How off-grid solar microgrids can power the AI race*. https://www.offgridai.us/
- Bellan, R. (2026). *CoreWeave turns to customer prepayments, shorter contracts to fund AI growth*. TechCrunch, 11 November. https://techcrunch.com/2026/11/11/coreweave-turns-to-customer-prepayments-shorter-contracts-to-fund-ai-growth/
- Capelouto, J. D. (2026). *US voters roundly reject data centers in ballot measures*. Semafor, 4 November. https://www.semafor.com/article/11/04/2026/us-voters-roundly-reject-data-centers-in-ballot-measures
- Council, S. (2026). *New Anthropic job listing offers $405,000 to land natural gas for its post-IPO data center buildout*. Business Insider, 13 November. https://www.businessinsider.com/anthropic-hires-gas-supply-lead-ai-plans-accelerate-ipo-2026-11
- LaRose, A., Diefenderfer, J., Bowers, R., & Vincent, N. (2024). *Capital Cost and Performance Characteristics for Utility-Scale Electric Power Generating Technologies*. U.S. Energy Information Administration. https://www.eia.gov/analysis/studies/powerplants/capitalcost/pdf/capital_cost_AEO2025.pdf
- Newkirk, A. C., Gerber, D. L., Fuchs, E. R. H., Hubbard, A., Morgan, M. G., Shehabi, A., Smith, S. J., & Samaras, C. (2026). *Speed-to-Power Dominates Energy Costs for AI Data Centers: Technoeconomic Analysis of Powering AI in the Continental United States*. https://arxiv.org/abs/2611.17098
- Rand, J., Manderlink, N., Gorman, W., Wiser, R. H., Seel, J., Kemp, J. M., Jeong, S., & Kahrl, F. (2024). *Queued Up: 2024 Edition, Characteristics of Power Plants Seeking Transmission Interconnection As of the End of 2023*. https://escholarship.org/uc/item/50d9w4tn
