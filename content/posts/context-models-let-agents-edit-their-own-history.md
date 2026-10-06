+++
title = "Context models let agents edit their own history"
description = "Context Language Models replace an append-only transcript with a file the model can rewrite, delete and reorder. The authors report better long-task accuracy with less repeated computation after training the editing policy."
tags = ["research", "agents", "tools"]
date = 2026-10-06T04:05:31+02:00
draft = false
+++

Context Language Models let an agent edit the history it will read next, turning context management from a fixed summarisation step into a learned action.

Rulin Shao and 12 co-authors represent the live context as a file. The model can rewrite, delete or reorder that file while it works, then continue from the edited version instead of carrying an ever-growing transcript or accepting a summary chosen by the surrounding software.

## Why it matters

For a developer running a long research or coding agent, context is both memory and computation. Repeatedly feeding old tokens costs time, while aggressive compaction can discard the evidence needed later. A model that decides what to preserve could make that trade-off task by task.

The paper calls the approach a Context Language Model, or CLM. It separates the editable context file from the current interaction, so an agent can keep a compact working record while the original environment continues to produce observations.

The basic method does not require a special model architecture. The authors test instructions that tell existing models how to manage the file, then improve the policy through reinforcement learning and a skill-optimisation loop. A public repository includes the implementation and examples, and the authors also released a plugin for the Pi agent harness.

On a held-out context-management task, the authors report that optimised natural-language instructions improved accuracy by as much as 35.9 percentage points while reducing compute. The “as much as” result is the strongest reported change, but it belongs to the authors' evaluation and varies by setting.

## Editing changes the cache as well as the text

Context editing creates an inference problem. Transformer servers normally reuse a key-value cache for an unchanged prefix. Rewriting text in the middle invalidates later cached states because those states were calculated from the previous version.

The authors propose partial cache reuse to avoid recomputing everything. That optimisation is consequential: reusing states from after an edit can make the cache stale, while recomputing from the edit point saves less work. The paper reports that its approximation preserved accuracy in the tested settings, but community readers have already identified this as an important target for reproduction.

The editable file also changes the security boundary. Tool output, user instructions and model-written notes can persist together until the model removes them. A malicious instruction that reaches the file may therefore survive longer than it would in a transient tool response. The paper studies context management rather than providing authenticated provenance or a complete defence against prompt injection.

The study evaluates Qwen and Claude-family models across context management and long-running agent tasks. Reported gains after reinforcement learning show that editing can be taught rather than only prompted, but they do not establish that every agent should control its own record. Regulated or forensic workflows may need an immutable transcript alongside the editable working context.

The preprint was submitted on 29 September 2026. The code repository is public, so the next useful evidence can come from reproductions that compare full recomputation, partial cache reuse and ordinary compaction on the same tasks.

## Verification

| Claim | Label | Primary source | Independent check |
| --- | --- | --- | --- |
| CLMs expose context as a file the model can rewrite, delete and reorder | VENDOR-REPORTED | [CLM preprint](https://arxiv.org/abs/2609.37725) | [public implementation](https://github.com/facebookresearch/context-language-models) |
| The method works with existing model architectures | VENDOR-REPORTED | [CLM preprint](https://arxiv.org/abs/2609.37725) | repository implementation available |
| Optimised instructions improved held-out accuracy by up to 35.9 points while reducing compute | VENDOR-REPORTED | [CLM preprint](https://arxiv.org/abs/2609.37725) | none; author evaluation |
| Partial cache reuse preserved accuracy in the tested settings | VENDOR-REPORTED | [CLM preprint](https://arxiv.org/abs/2609.37725) | no independent reproduction found |
| Editable context can preserve injected instructions longer | ANALYSIS | [CLM preprint](https://arxiv.org/abs/2609.37725) | threat follows from persistent model-written context |
| The code and a Pi plugin are public | VERIFIED | [CLM repository](https://github.com/facebookresearch/context-language-models) | repository available |
| The preprint was submitted on 29 September 2026 | VERIFIED | [arXiv record](https://arxiv.org/abs/2609.37725) | arXiv metadata |
