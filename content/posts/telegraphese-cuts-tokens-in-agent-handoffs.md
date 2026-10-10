+++
title = "Telegraphese Cuts Tokens in Agent Handoffs"
description = "A public benchmark finds that one instruction can make several models write machine-readable records with roughly half as many output tokens. The technique fails when applied during active reasoning."
tags = ["agents", "research", "tools"]
date = 2026-10-10T03:58:41+02:00
draft = false
+++

Telling language models to write in telegraph style cut their output by roughly 40% to 49% while other models recovered the recorded facts at comparable accuracy.

Independent developer Travis Smith tested the instruction on 50 passages and about 1,300 questions. The method asks a model to drop articles and filler, abbreviate, preserve every fact, number and proper noun, and use lowercase so capital letters do not inflate token counts.

## Why it matters

An agent developer pays once when one model writes a memory and again each time another model reads it. Compressing machine-to-machine notes after the work is complete can reduce both the output bill and the context occupied by repeated handoffs.

The benchmark separates writing from reading. Gemma 4, Qwen3.8 and GLM-5.3-Flash wrote condensed records, while models from several families answered anchored questions from either those records or ordinary summaries. Smith published the harness, frozen result ledgers and a runnable notebook.

The clearest result came from the writers. Gemma used about 40% fewer billed output tokens, while Qwen and GLM saved about 49%. Readers answering from compressed records scored between 0.99 and 1.10 times their accuracy on the ordinary summaries. Four reader families received no worked example of the style, which suggests the convention was already familiar from training data.

## Compression belongs after the reasoning

Placement changed the result. Models asked to formulate answers directly in telegraph style retained only about four-fifths of their ordinary accuracy. When the content was first settled and then compressed into a record, downstream readback matched or slightly exceeded the plain-summary control.

That makes the technique suitable for scratchpad archives, agent memories and handoffs. It is a poor fit for a user-facing answer or a step where the model is still deciding what to say. The compressed text remains readable by a person, but it is intentionally less comfortable than normal prose.

Mandatory reasoning created another failure mode. GPT-5-mini produced fewer visible tokens but spent roughly three times more on hidden reasoning, according to the author's ledger, making the total write more expensive. A team needs to test the provider's actual billing meter rather than counting only characters or visible tokens.

Smith also measured a round trip in which compressed text was expanded back into prose. The stored result stayed smaller than an ordinary summary, but the extra model call consumed more tokens than the initial write saved. Repeated cheap reads can recover that cost; a write-once, read-once workflow may not.

The historical framing may not be essential. Smith did not run the strict control of asking for maximum terseness without mentioning telegraph style. The experiment therefore supports the practical instruction, but it does not establish that telegraphese itself causes the gain.

The result also remains an author-run benchmark. Its strengths are unusually inspectable materials and cross-family tests; its limit is that the passages, questions and graders define one kind of factual record. Code, mathematical derivations and conversational memory may compress differently.

The published notebook can now be run on production agent transcripts, allowing teams to compare task success and provider-billed tokens on their own traffic.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Telegraph-style instructions reduced billed output tokens by about 40%–49% on Gemma, Qwen and GLM writers | VENDOR-REPORTED | https://fiveminutesforward.com/post/2026-10-04-telegraph-test/ | none |
| Cross-family readers recovered facts at 0.99–1.10 of plaintext-summary accuracy | VENDOR-REPORTED | https://fiveminutesforward.com/post/2026-10-04-telegraph-test/ | none |
| Directly composing answers in telegraph style reduced accuracy to about 0.81 of the plain control | VENDOR-REPORTED | https://fiveminutesforward.com/post/2026-10-04-telegraph-test/ | none |
| GPT-5-mini's mandatory reasoning erased the visible-token saving in the author's test | VENDOR-REPORTED | https://fiveminutesforward.com/post/2026-10-04-telegraph-test/ | none |
| The harness, frozen ledgers and notebook are public | VERIFIED | https://github.com/Travis42/telegraph-test | none |
| The method is best suited to settled machine-readable records rather than active reasoning | ANALYSIS | https://fiveminutesforward.com/post/2026-10-04-telegraph-test/ | none |
