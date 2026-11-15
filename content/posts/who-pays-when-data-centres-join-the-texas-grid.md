+++
title = "Who Pays When Data Centres Join the Texas Grid"
description = "A preprint models what 371 announced Texas data centres would add to a household's electricity price and finds that most of it arrives through the wholesale market, not through new power lines. The same study shows that the answer moves with where plants are built and how transmission costs are shared, the choice Virginia has just made for itself."
tags = ["business", "policy", "research"]
date = 2026-11-15T03:19:35+01:00
draft = false
+++

James O'Donnell of MIT Technology Review spent the week of the American midterm elections in Ashburn, Virginia, the centre of what is known as Data Center Alley. Concrete buildings with names like Skybox and CloudHQ stand along every major road. At one facility run by Equinix he saw diesel generators kept for backup, while the building itself drew its power from the local utility, Dominion Energy. The average data centre in that part of Virginia has a capacity of 54 megawatts, he reports, more than the draw of Denver International Airport.

There he met Elena Schlossberg, a prominent campaigner against data centres. When the industry describes the fight as a culture war, she told him, she is "always banging my head against the wall". Her view: "It was always about power."

Two days after the election, OpenAI's chief global affairs officer, Chris Lehane, had written that data centres "have become a proxy for public unease about affordability, corporate power, and people losing control over their futures." O'Donnell's account sets the two readings side by side. A new preprint from Oregon State University and the National Laboratory of the Rockies puts a number on the electricity side of the argument.

## What the study modelled

Lingdong Zhou, Wenjia Xia, Jiyu Wang, Fei Ding and Xiangqi Zhu take 371 announced data-centre projects in Texas, which together would draw 38.9 gigawatts by 2030, and ask what serving them would do to a household's cost per kilowatt-hour. The paper is a preprint and has not been peer reviewed. It is a model, and the authors say plainly that its results are "modeled impacts under the specified assumptions, not forecasts of actual household electricity bills."

The projects cluster at 51 points on the model of the Texas grid. Existing demand swings between 35 and 85 gigawatts over a summer, but the data centres add 33 to 38 gigawatts in every hour. The model chooses which power plants, batteries and transmission lines to build at least cost, computes wholesale prices at each point on the grid, sizes the reinforcement that the network needs to stay secure, and follows the costs through regulated charges and a retail supplier to a residential customer. It covers May to October, the months that set Texas's peak demand, and tests five historical weather years.

## Where the money comes from

In the representative case, the 2023 weather year, a household pays 1.64 cents more per kilowatt-hour during the peak season. Of that, 1.124 cents, 68 percent, comes through higher wholesale prices. The other 0.520 cents, 32 percent, comes through regulated transmission charges. The authors read this as evidence against a common picture. Even when data centres help to pay for new lines, their demand lifts the wholesale price that every customer pays, and that effect is larger than the line charge.

The result depends on how the grid grows. If new gas plants may be built only at existing sites, generation and storage alone can supply more than 99.95 percent of the demand, but power cannot always reach the buses behind constrained corridors. Prices at one or more of them exceed the market cap of $5,000 per megawatt-hour in 136 to 407 three-hour intervals a season. Letting transmission grow alongside generation cuts the mean annual investment from $16.7 billion to $4.54 billion and leaves one to three such intervals. Letting new gas plants rise next to the data centres lowers the household increase from 1.64 to 0.92 cents.

Location matters on its own. Adding 5 gigawatts with no new infrastructure leaves between 25 and 140 gigawatt-hours of demand unserved per season at Houston, Austin, Tolar and southern Dallas–Fort Worth, but 5.6 terawatt-hours at Abilene and 18.7 at Childress. The same load, the authors note, can differ by nearly three orders of magnitude in unserved energy depending on where it connects.

## The cost-sharing choice

The third lever is not engineering at all. Texas spreads its transmission bill across customers in proportion to their demand at system peaks. In the model, data centres pay about $0.82 billion of the $2.719 billion annual transmission revenue requirement. If they were removed from that base, the residential transmission charge would rise from 0.520 to 0.747 cents per kilowatt-hour and the household total from 1.64 to 1.87. Nothing about the grid would change; only who is billed. The authors note that a 2025 Texas law, Senate Bill 6, requires a review of this allocation method.

Their own list of limits is long. The scenario assumes the announced projects get built. It ignores winter. The wholesale prices rest on the market model's assumptions about foresight and scarcity pricing, the transmission network is synthetic, and the reinforcement step leaves some violations unresolved. Flexible data-centre demand, which could remove the few remaining scarcity hours, is not modelled. A higher-priced variant that represents Texas's reserve-pricing mechanism puts the wholesale part at 0.81 cents in 2023 and at 2.34 to 2.89 cents in 2019 to 2022. Fixed-price retail contracts also delay the effect, because suppliers absorb higher costs until they can reprice. In a simulation, a retailer's chance of exhausting its cash rises from 0.04 to 0.26 percent under coordinated expansion and to 1.24 percent when only generation and storage are added.

## Virginia chose, and others are choosing

Virginia has already made the allocation choice the paper isolates. According to O'Donnell, protests there led the state to adopt rules that data centres pay fully for the cost of new transmission lines, so that the cost is not spread among everyone else. Developers told him they expect further rules that would cut them off from grid power at peak times, which is the kind of flexibility the Texas authors did not model but name as a promising target.

Elsewhere the contest is taking a different form. Semafor reported on 4 November that voters in more than 30 localities across nine states backed moratoriums, bans and other limits on data centres in ballot measures, and that banks and asset managers financing the buildout had begun to treat local opposition as a credit risk. O'Donnell adds that most AI campuses now planned are not built for grid connection at all. Where the scale wanted is 300 megawatts at the least and about 6,000 at the ideal, companies set up in rural areas and generate power on site with gas turbines. He cites a report that Anthropic agreed to pay $3.4 billion for gas turbines. His point is that power plants of that size affect neighbours, and that communities have traditionally had a say in where such plants go.

The Texas paper cannot say which of the two readings of the backlash is right. It says something narrower. A household's share of the cost of a new load is not fixed by the load. It moves by almost a cent per kilowatt-hour with the siting of generation and by a quarter of a cent with a billing rule, and both are decisions that regulators and legislators still have open.

In Ashburn the rule is already written. In Texas the review that Senate Bill 6 ordered has yet to report.

## References

- Capelouto, J. D. (2026). *US voters roundly reject data centers in ballot measures*. Semafor. https://www.semafor.com/article/11/04/2026/us-voters-roundly-reject-data-centers-in-ballot-measures
- O'Donnell, J. (2026). *The backlash about data centers might really just be about electricity*. MIT Technology Review. https://www.technologyreview.com/2026/11/09/1148194/the-backlash-about-data-centers-might-really-just-be-about-electricity/
- Zhou, L., Xia, W., Wang, J., Ding, F., & Zhu, X. (2026). *Data-center growth impacts household electricity costs more through wholesale prices than through grid reinforcement*. arXiv preprint. https://arxiv.org/abs/2611.16095
