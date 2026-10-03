+++
title = "Percepta tests growing memory for long-context recall"
description = "Spotlight Memory addresses a small region of expandable storage at each step. Percepta reports strong retrieval beyond the models’ training length."
tags = ["models", "research"]
date = 2026-10-03T06:00:20+02:00
draft = false
+++

Percepta, an AI research company, reports that its Spotlight Memory architecture retrieves information from contexts sixteen times longer than its training sequences while keeping the work of each memory access fixed.

The architecture gives a language model expandable storage and teaches it where to put information. Christos Tzamos, Guoqing Zheng and Athul Jacob describe controlled experiments in a 2 October technical post, comparing models with the same approximate parameter counts and training data.

**Why it matters:** A researcher building models for long documents gets evidence for a memory design that keeps old information accessible without rereading every earlier token. The central trade is explicit: storage can grow, while the model touches only a small neighborhood of it at each step.

The [Percepta report](https://www.percepta.ai/blog/spotlight-memory) describes the tension between two existing approaches. Full attention keeps information about previous tokens but compares each new query with that history. Fixed-state recurrent models compress the past into a limited store; that reduces processing cost, but more information eventually competes for the same capacity.

Spotlight instead maps information to addresses in a two-dimensional grid. A write allocates a cell when an address is first used, and later writes can update that cell. A query reads nearby cells. The number of cells touched stays fixed even as the collection of allocated cells gets larger.

The model learns those addresses during training. All cells share the same learned rules for recording and updating information, so adding storage does not require adding another set of model weights. A smooth weighting function distributes reads and writes over neighboring cells, allowing training to adjust an address gradually.

The mechanism resembles a filing system whose cabinet can expand while a lookup goes directly to a small group of drawers. The difficult part is learning a useful filing scheme: matching questions and stored facts need to arrive at compatible addresses. Percepta's experiments test that ability before applying the design to language modeling.

## Small models retained facts beyond their training length

Percepta trained models with 140 million, 280 million and 670 million parameters from scratch on FineWeb-Edu, a web-text dataset. Within each size group, models saw the same data in the same order. The researchers adjusted feed-forward widths so their parameter counts differed by no more than 0.1%.

The initial training used sequences of about 8,000 tokens, the text fragments processed by a model. The researchers then tested retrieval from sequences reaching about 128,000 tokens: a single record was embedded in a long context, and the model had to recover it. That is the sixteenfold extension behind the headline.

Spotlight reached 93–100% recall across the three model sizes at the longest tested context, according to Percepta. The fixed-state recurrent alternatives reached at most about 6%, while attention scored zero beyond the training length in this test, including after positional rescaling. The result concerns locating one embedded record, rather than every kind of long-document reasoning.

The short-context comparison was less dramatic. At the largest size, Spotlight's average score on a suite of language-model tasks stayed close to the alternatives. Its advantage lay in retaining access to information as context expanded, not in a broad jump across those tasks.

Percepta then gave each available model checkpoint the same additional long-context training. Spotlight retained its retrieval lead and achieved the lowest held-out language-model loss at every tested context length and size. A separate question-classification task also improved as more labeled examples filled the prompt, supporting the connection between growing memory and useful retrieval.

The results remain Percepta's own early experiments. The report ties its proposal to continual learning, but the concrete evidence here is that fixed model weights can learn to organize a growing memory. Its largest model contains 670 million parameters; transfer of that behavior to much larger deployed systems remains an unresolved question.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Percepta published Spotlight Memory on 2 October; the citation names Christos Tzamos, Guoqing Zheng and Athul Jacob. | VERIFIED | [Technical post](https://www.percepta.ai/blog/spotlight-memory) | none |
| The design learns addresses on a 2D lattice, allocates cells on first write, shares update rules and uses local differentiable reads and writes at constant access cost. | VENDOR-REPORTED | [Architecture description](https://www.percepta.ai/blog/spotlight-memory) | none |
| Training compared 140M, 280M and 670M models on identical FineWeb-Edu data/order within each size, at 8K context, with parameter differences at most 0.1%. | VENDOR-REPORTED | [Training protocol](https://www.percepta.ai/blog/spotlight-memory) | none |
| At 128K context, sixteen times 8K training length, Spotlight attained 93–100% single-needle recall (500 samples), fixed-state baselines at most 5.6%, attention 0% at 16K–128K. | VENDOR-REPORTED | [RULER results](https://www.percepta.ai/blog/spotlight-memory) | none |
| At 670M, short-context task means were Spotlight 33.1, GDN-2 33.8, attention 33.3 and Gated DeltaNet 34.1. | VENDOR-REPORTED | [Language evaluation](https://www.percepta.ai/blog/spotlight-memory) | none |
| Each available checkpoint received 1.17B additional tokens at 128K; Spotlight retained retrieval leadership and lowest tested held-out loss. TREC-coarse at 670M rose from 63% to 85% as context grew 8K–128K. | VENDOR-REPORTED | [Long-context training and classification](https://www.percepta.ai/blog/spotlight-memory) | none |
| Expandable storage separates memory capacity from per-access work; these small-model retrieval experiments leave larger deployment behavior unresolved. | ANALYSIS | [Design and experimental scope](https://www.percepta.ai/blog/spotlight-memory) | none |
