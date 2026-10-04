+++
title = "Simon Willison calls for default agent spending caps"
description = "His proposal favours automatic shutdown at a budget limit. Removing the limit would require an explicit choice."
tags = ["essays", "agents"]
date = 2026-10-04T09:22:37+02:00
draft = false
+++

Developer Simon Willison argues that services charging by usage should impose hard spending limits by default as coding and personal agents make paid infrastructure easier to launch.

His 3 October essay distinguishes a service that stops at its budget from one that merely sends a warning. An unattended application can keep spending after the notification arrives.

For someone deploying an agent-built application, the proposal trades continued availability for a predictable maximum bill. Willison argues that users who prefer continued operation should explicitly opt out and accept subsequent charges.

The essay links an AWS project-limit feature and Google Cloud Spend Caps. Willison describes the AWS rollout as limited and Google's feature as covering specific services. Those references support his argument that providers are moving toward caps; they are his account of the products.

Willison also proposes that agents favour providers offering hard limits and warn inexperienced builders about uncapped deployment. The concrete choice he wants exposed is whether an application stops when its configured budget is exhausted.

## Verification

| Claim | Label | Primary source | Independent check |
| --- | --- | --- | --- |
| 3 October essay; default caps, explicit opt-out and agent recommendations | OPINION | [Source](https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/) | none |
| Provider feature references and rollout limits | UNVERIFIED | [Source](https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/) | Provider pages unavailable; attributed to Willison |
| Predictability trades off against availability | ANALYSIS | [Source](https://simonwillison.net/2026/Oct/3/default-hard-budget-caps/) | Inference from cutoff proposal |
