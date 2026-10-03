+++
title = "AWS raises reserved GPU rates from 7 October"
description = "New EC2 Capacity Blocks rates apply per accelerator. Purchased reservations retain their price, while On-Demand and Savings Plans remain unchanged."
tags = ["hardware", "tools", "models"]
date = 2026-10-03T05:20:20+02:00
draft = false
+++

AWS will raise EC2 Capacity Blocks GPU reservation rates from 7 October 2026. The update prices accelerators individually rather than complete multi-GPU instances.

Capacity Blocks let teams reserve computing capacity for a scheduled machine-learning workload. The customer pays for the reserved block upfront, with operating-system charges handled separately while instances run.

**Why it matters:** Teams scheduling training or evaluation jobs need to distinguish a price per GPU from a price per server. An instance with eight accelerators multiplies the stated accelerator rate by eight before any separate operating-system charges.

The [new hourly rates](https://aws.amazon.com/ec2/capacityblocks/pricing/) are 16.146 dollars for P6-B300 and 14.208 dollars for P6-B200, with respective GovCloud rates of 16.819 dollars and 14.801 dollars. P5en becomes 7.895 dollars, P5e 6.866 dollars, P5 5.970 dollars, P4de 2.546 dollars and P4d 1.696 dollars per accelerator across available regions.

For example, eight H100 GPUs at the new P5 rate imply 47.76 dollars per instance-hour. That is a calculation from the announced rate, not the older 41.528-dollar P5 instance figure still displayed in the current pricing table.

AWS says other Capacity Blocks prices, On-Demand prices and Savings Plans prices remain unchanged. This update concerns the specified reservation rates rather than a general increase across EC2 purchasing options.

The [billing documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-blocks-pricing-billing.html) says a reservation’s price does not change after purchase. Customers can inspect an offering’s price before reserving it, and the charge is taken upfront. Savings Plans and Reserved Instance discounts do not apply to Capacity Blocks.

The purchase-time rule makes the reservation date important even when a workload runs later. The relevant price is the offering accepted when the block is bought.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| The new per-accelerator schedule starts on 7 October; other purchasing rates stated above are unchanged. | VERIFIED | [AWS pricing update](https://aws.amazon.com/ec2/capacityblocks/pricing/) | none |
| Eight GPUs at 5.970 dollars each imply 47.76 dollars per hour. | ANALYSIS | [P5 rate](https://aws.amazon.com/ec2/capacityblocks/pricing/) | Arithmetic: 8 × 5.970 |
| Purchased block prices remain fixed; reservation charges and operating-system charges are separate. | VERIFIED | [AWS billing documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-blocks-pricing-billing.html) | none |
| Savings Plans and Reserved Instance discounts do not apply to Capacity Blocks. | VERIFIED | [AWS billing documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-blocks-pricing-billing.html) | none |
