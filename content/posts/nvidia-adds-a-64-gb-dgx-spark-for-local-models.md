+++
title = "Nvidia adds a 64 GB DGX Spark for local models"
description = "Partner systems start at $4,999 on 23 October. Nvidia also announced simpler clustering, while the larger Spark has become more expensive."
tags = ["hardware", "tools", "models"]
date = 2026-10-03T05:17:20+02:00
draft = false
+++

Nvidia announced a 64 GB version of its DGX Spark desktop AI computer, available through hardware partners on 23 October starting at $4,999.

The smaller configuration keeps the GB10 Grace Blackwell processor and Nvidia's software stack, but provides half the unified memory of the 128 GB model. Unified memory gives the processor and graphics hardware access to the same pool, which can hold model weights and working data.

**Why it matters:** A developer running private models locally gains another capacity option, alongside a simpler route to connecting two machines. The trade is tangible: less memory limits what fits on one desktop even when the underlying chip remains the same.

The Register reports unchanged memory bandwidth of 273 GB per second, a 20-core Arm CPU and ConnectX-7 networking. It also reports that Nvidia raised the 128 GB system's price to $6,950. The new version is cheaper than that current larger model, despite costing more than the larger system's original launch price.

Nvidia says two 64 GB machines connected through their 200 GbE network can pool 128 GB of memory. Its Sync Cluster Assistant detects the connected devices, checks their configuration and sets up the network. The memory pool concerns a connected pair, rather than the capacity of one machine.

Nvidia reports up to 1.7-times performance for two machines compared with one in its own Qwen 3.8 27B test. The announcement also claims support for models with up to 100 billion parameters on a single machine and 200 billion across a pair, without detailing the precision and context settings behind those limits.

Nvidia's announced launch partners include Acer, ASUS, Dell, Gigabyte, HP and MSI. Its Model Launcher is scheduled for the end of October, with installation and deployment of Qwen 3.8 27B across one machine or a cluster, plus configuration of the OpenCode coding interface.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Nvidia announced partner-only 64 GB DGX Spark on 2 October, from $4,999 on 23 October, retaining GB10 and DGX OS; six named partners listed. | VERIFIED | [Nvidia announcement](https://blogs.nvidia.com/blog/local-ai-dgx-spark-64gb-sync/) | [The Register](https://www.theregister.com/systems/2026/10/02/nvidia-debuts-4999-dgx-spark-with-half-the-ram-and-storage-amid-memory-crunch/5300622) |
| Memory bandwidth is 273 GB/s, CPU 20-core Arm, and networking ConnectX-7; reported 128 GB price is $6,950, above its original $3,999. | PARTIALLY VERIFIED | The Register's direct reporting above | Nvidia confirms GB10 and ConnectX-7, but its announcement omits the larger model's price. |
| Two 64 GB nodes pool 128 GB over 200 GbE; Sync configures the cluster. | VENDOR-REPORTED | Nvidia announcement above | none; documentation describes capability |
| Up to 1.7x performance in Nvidia's Qwen 3.8 27B test; claimed 100B/200B model capacity for one/two nodes. | VENDOR-REPORTED | Nvidia announcement above | none; precision/context behind capacity limits not stated in announcement |
| Model Launcher scheduled for end of October, supporting Qwen 3.8 27B deployment and OpenCode configuration. | VERIFIED | Nvidia's announced schedule above | none; future availability |
| Lower capacity changes what fits while a connected pair is a separate configuration. | ANALYSIS | Published memory configurations above | none |
