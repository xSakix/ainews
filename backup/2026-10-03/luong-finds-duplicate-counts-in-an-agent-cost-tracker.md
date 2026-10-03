+++
title = "Luong finds duplicate counts in an agent cost tracker"
description = "His middleware post-mortem argues that internal agent events must be reconciled with the actual session bill."
tags = ["essays", "agents", "tools"]
date = 2026-10-03T05:30:20+02:00
draft = false
+++

Thuan Luong, a software practitioner, reports that his Claude Code cost-tracking middleware counted a logical turn more than once, inflating its estimate relative to the actual session bill.

His October 2 post describes experimenting with hooks that expose events inside the coding agent. Tracking those events helped reveal repeated file reads, but also introduced a new error when he treated an internal event as a complete conversational turn.

**Why it matters:** A technical lead allocating an agent budget needs measurements that correspond to actual usage. Luong's account shows why adding instrumentation is not enough: the meaning of each event and the counting rules need checking too.

He says a completion hook fired during pauses inside a longer chain of tool calls. His tracker interpreted those notifications as separate summaries, producing a much higher estimated total than the provider's console. He then changed the deduplication logic to use a turn identifier and sequence information.

These are the author's reported observations, not a reproduced test of Anthropic's interface. His post combines code with a description of the failure, making the counting assumption more visible than a general claim that an agent is expensive.

The useful engineering question is which event owns the charge. Several notifications may refer to progress within one unit of work; adding their totals can count the same activity repeatedly. A dashboard can look precise while using the wrong unit, so reconciling a sample session against a separate bill is part of validating the instrument.

Luong says the hooks make in-process monitoring more appealing than his earlier proxy arrangement. He nevertheless leaves the proxy setup in place for now and wants another minor release before trusting the completion event for billing-related work.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Luong and October 2 publication; tracker experiment and code shown. | VERIFIED | https://luonghongthuan.com/en/blog/claude-code-mods-typescript-middleware/ | None; attributed primary account. |
| Internal completion events, duplicate counts, console mismatch, turn/sequence fix and retained proxy. | PARTIALLY VERIFIED | https://luonghongthuan.com/en/blog/claude-code-mods-typescript-middleware/ | None; attributed primary account. |
| Usage instrumentation requires validation of event units and reconciliation with bills. | ANALYSIS | https://luonghongthuan.com/en/blog/claude-code-mods-typescript-middleware/ | None; attributed primary account. |
