+++
title = "HPE lands $1.2 billion Vultr AI rack order"
description = "Vultr ordered AMD Helios racks and HPE networking for US data centres. It is HPE's first order for the system and a large commercial test of an Ethernet-based AI stack."
tags = ["hardware", "business"]
date = 2026-10-01T04:00:03+02:00
draft = false
+++

Hewlett Packard Enterprise has won a $1.2 billion order from Vultr for AMD Helios AI racks, the first customer order HPE has announced for the system.

Vultr plans to install the racks in US cloud data centres for model training and inference. Each rack combines 72 AMD accelerators with HPE's Juniper networking, CPUs, network cards, cooling and AMD's ROCm software.

## Why it matters

A cloud operator adding AI capacity is buying an integrated rack rather than assembling chips, switches and cooling separately. The order gives AMD and HPE a large deployment in a market where Nvidia's rack-scale systems set the commercial reference point.

HPE says the Helios design uses AMD Instinct MI455X accelerators and EPYC "Venice" processors. Six Juniper QFX5252 switch trays connect the 72 accelerators over an Ethernet-based scale-up fabric, while direct liquid cooling handles the density. Those specifications are concrete; claims about efficiency and deployment speed still come from the sellers.

Vultr had already announced plans in July to offer AMD Helios capacity. The new agreement adds a disclosed order value and identifies HPE as the rack and networking supplier. It does not say how many racks Vultr will receive, when all systems will be online or how the $1.2 billion is divided among hardware, software and services.

That missing quantity prevents a unit-price comparison. It also makes the headline value a commitment rather than a measure of installed capacity. The useful signal is strategic: Vultr is backing a rack-scale alternative built around AMD accelerators and open Ethernet standards, while HPE is using the Juniper business it acquired last year to sell more of the AI system as one package.

The Ethernet choice is part of the wager. HPE says its fabric uses the Ultra Accelerator Link protocol over Ethernet, allowing the accelerator network to be supplied as part of a standards-based stack. The announcement provides topology and component details, but no cluster-level training results against a comparable proprietary fabric.

Reuters linked the order to HPE's upgraded networking outlook. The company now expects networking revenue to grow at a high-teens annual rate from fiscal 2026 through 2029, up from its previous 5% to 7% range for a different period. HPE also raised its expected annual Juniper cost savings to $800 million by the end of fiscal 2028.

Those forecasts are management targets, not results. Still, the Vultr order shows why HPE is willing to raise them: AI clusters make networking, cooling and systems integration part of the accelerator sale. A rack with dozens of expensive processors is only useful if the fabric can keep them fed and the facility can remove the heat.

HPE competes with Dell and Super Micro in AI servers, while AMD is trying to loosen Nvidia's hold on large training systems. The deal does not establish that Helios matches Nvidia on usable performance or software maturity. It does put a named cloud provider and a disclosed amount behind AMD's alternative.

The next evidence will come from Vultr's availability dates and customer performance data. HPE and Vultr have not published either.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| HPE announced a $1.2 billion Vultr order for AMD Helios AI Rack by HPE systems. | VERIFIED | https://www.hpe.com/us/en/newsroom/press-release/2026/09/hpe-secures-its-first-amd-helios-order-in-12-billion-deal-with-vultr.html | https://www.reuters.com/business/hpe-boosts-networking-growth-outlook-gets-12-billion-ai-order-cloud-firm-vultr-2026-09-30/ |
| HPE calls this its first order for the Helios system. | VERIFIED | HPE release above | Reuters report above |
| Each rack integrates 72 AMD MI455X accelerators, EPYC Venice CPUs, AMD networking and ROCm software, connected by six Juniper switch trays. | VERIFIED | HPE release above | none |
| Vultr had announced support for Helios in July 2026. | VERIFIED | https://blogs.vultr.com/amd-advancing-ai-san-francisco-2026 | HPE release above |
| The companies did not disclose rack count, full delivery timing or the allocation of the order value. | VERIFIED | HPE release above | Reuters report above |
| HPE raised its long-term networking growth and Juniper savings targets. | VERIFIED | https://www.hpe.com/us/en/newsroom/press-release/2026/09/hpe-to-outline-networking-priorities-for-long-term-value-creation.html | Reuters report above |
| HPE says the scale-up fabric uses Ultra Accelerator Link over Ethernet; no comparative cluster benchmark was published. | VERIFIED | HPE release above | none |
| The order is a commercial test of an Ethernet-based alternative to Nvidia rack systems. | ANALYSIS | HPE and Vultr architecture disclosures | none |
