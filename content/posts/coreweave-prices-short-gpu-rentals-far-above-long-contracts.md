+++
title = "CoreWeave Prices Short GPU Rentals Far Above Long Contracts"
description = "CoreWeave says it raised GPU prices about 25% in July and 10% later, and now sells short-term capacity at more than $40 million per megawatt a year against $20 to $25 million on multi-year deals. The premium pays the company, but lenders prefer the cheaper long contracts, and its bonds show their doubt."
tags = ["business", "hardware", "agents"]
date = 2026-11-12T03:15:32+01:00
draft = false
+++

Picture a credit analyst at a bank that lends against data-centre contracts. She has two schedules open side by side, both for the same kind of capacity in the same kind of building. One is a four-year commitment from a large customer at a price that looks almost modest. The other is a three-month rental at nearly twice the price. The second earns more. Her job is to decide which one the bank will lend against, and the answer is the first. The analyst is invented for this article. Her choice is the one that CoreWeave described to investors this week.

CoreWeave, a company that rents out the computing power behind AI, reported third-quarter results on Tuesday 10 November. Revenue was $3.66 billion, up 168% on the year before, with a net loss of $709 million and $846 million of interest expense in the quarter. TechCrunch's Rebecca Bellan, reporting on the earnings call, wrote that the company is "increasingly asking customers to pay up front, borrowing against specific contracts, and even pursuing short-term deals that could lead to higher prices." Behind those three habits sits one number: what it now costs to rent a GPU in a hurry.

## What the price sheet says

Chief executive Michael Intrator told analysts that CoreWeave raised prices across its offerings by about 25% in July and by another 10% later in the quarter, and that prices were still climbing in the current one, in a way that "more than offset[s] cost increases." If the two rises apply to the same list prices, they compound to roughly 38%. The company did not say that they do.

The sharper figure is the gap between contract lengths. Intrator said CoreWeave is "allocating more capacity to short-term opportunities, where the pricing justifies it, selling capacity at more than $40 million per megawatt annually, while pricing for new infrastructure on four- and five-year contracts is moving to $20 million to $25 million per megawatt." By simple arithmetic, a customer who needs power now pays between 60% and 100% more per megawatt than one who commits for years.

The first sign of this had come earlier. On 17 September CoreWeave published a release headed "CoreWeave Continues to Contract New Compute Capacity at Higher Prices." It said that in the third quarter the company had signed short-dated contracts of about three to six months at roughly $40 million per megawatt, a figure it defined as annualised revenue divided by the power needed to serve the clusters. It added more than $25 billion of net new customer commitments since 30 June and said contracted power had risen from about 3.7 gigawatts to about 4.2. The release gave no reason for publishing; it simply put the new price level on the record.

CoreWeave is not alone in charging more. On 2 October, Quartz reported that Amazon Web Services was raising the price of its EC2 Capacity Blocks for ML, the reserved GPU slots that cover chips from the A100 to the B300, by about 15%. A p5.48xlarge instance, with eight H100 chips, was listed at $41.528 an hour in the main US regions. Quartz noted that Amazon and Nvidia did not respond to requests for comment.

## Why the cheap contract is the one lenders want

If the short contracts pay so well, why not sell only those? Bellan's answer comes from the lenders: they "give more weight to longer-term contracts, even if they're priced lower, because they value predictable cash flow and consistency to repay the loan above all." CoreWeave builds its capacity with borrowed money, so a customer who signs for five years is worth more to the company than the same customer's money would suggest. In August it closed a $2.6 billion loan designed specifically for shorter customer contracts, which it can draw in instalments as it needs the cash. Intrator said the company will not use the unsecured debt market "at current yields, nor do we need to."

Those yields are the other half of the tension. Last month, Bellan reports, yields on some CoreWeave bonds rose above 15%. On 22 October, the Associated Press described AI stocks falling on worries about how expensive it has become to borrow for data centres and chips; CoreWeave shares dropped 10.1% that day. By 6 November, CNBC's Jordan Novet and Seema Mody reported that the shares of CoreWeave, Nebius and IREN had each lost roughly half their value in a month, after reports that Microsoft is shrinking its list of neocloud suppliers. Microsoft told CNBC that reviewing such investments is "a normal and responsible way to manage large, complex infrastructure projects." Its finance chief, Amy Hood, had said on the October earnings call that some GPU cloud contracts were pushed into the first half of 2027.

CoreWeave's answer has been to ask customers for cash first. It expects about $9 billion in prepayments and deposits over the next three months, more than $3 billion of it tied to new contracts for capacity it has already built, which costs no additional hardware. Nebius and IREN, Bellan notes, have leaned on large Microsoft prepayments in the same way. Prepayment helps the company's immediate borrowing, but TechCrunch points out the catch: it commits CoreWeave to a price that could look worse later if demand keeps rising. The company puts its backlog at $132.5 billion.

## What the buyer takes from this

For anyone who rents GPUs, the sheet implies a choice with a price on it. Those who can forecast their needs and commit for years pay the lower rate and help their supplier borrow. Those who need a burst of training or a surge of inference pay the higher one, and the supplier has little reason to discourage them while demand lasts. Whether that premium is a scarcity price or a stage in an unfinished build-out is not something the company's own figures can settle; every number above comes from CoreWeave or from reporters relaying it.

Bellan's own conclusion is that the strategy "could boost profits, but it also carries greater risk around contract renewals and pricing," and that it shows how dependent the AI infrastructure boom is on "sustained, and as yet unproven, demand."

Imagine the head of machine learning at a small start-up, also invented, who gets a quote for a three-month block on the day her runway is due for review. The price is higher than the number in last spring's plan. She signs, because the model has to ship, and then writes a note to herself to ask a different question next time: not what a GPU costs, but how long she is willing to promise to keep paying for one. The analyst at the bank, meanwhile, is asking the same question from the other side.

## References

- Associated Press (2026). *Sharp drops for AI stocks overwhelm markets worldwide as oil prices jump*. The Guardian, 22 October. https://www.theguardian.com/business/2026/oct/22/stock-markets-drop-ai-oil
- Bellan, R. (2026). *CoreWeave turns to customer prepayments, shorter contracts to fund AI growth*. TechCrunch, 11 November. https://techcrunch.com/2026/11/11/coreweave-turns-to-customer-prepayments-shorter-contracts-to-fund-ai-growth/
- CoreWeave (2026). *CoreWeave Continues to Contract New Compute Capacity at Higher Prices*. Business Wire, 17 September. https://finviz.com/news/393022/coreweave-continues-to-contract-new-compute-capacity-at-higher-prices
- Novet, J., & Mody, S. (2026). *Microsoft moves to consolidate its relationships with neoclouds in AI*. CNBC, 6 November. https://www.cnbc.com/2026/11/06/microsoft-moves-to-consolidate-its-relationships-with-neoclouds-in-ai.html
- Tolomia, C. (2026). *Amazon hiking AI chip rental prices*. Quartz, via Yahoo Finance, 2 October. https://finance.yahoo.com/technology/ai/articles/amazon-hiking-ai-chip-rental-122155988.html
