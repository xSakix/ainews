+++
title = "Mingbird adds skills to its local agent harness"
description = "The Ollama-based project adds voice input and everyday document tools. Its published benchmark argues that small-model results depend heavily on the surrounding software."
tags = ["agents", "projects", "tools"]
date = 2026-10-04T09:24:37+02:00
draft = false
+++

Mingbird, an open-source local agent harness, added bilingual voice input and six general-purpose skills on 1 October, followed by a Windows model-directory fix in version 1.9.2 the next day.

The project wraps Ollama models in software that runs tools, checks work and manages a session. Its desktop release targets Windows, with Linux and macOS support described as experimental. Code is available under Apache 2.0.

For a developer running a small model on a laptop, the interesting work happens around the model. Mingbird runs tests itself and returns exact failures, backs up edits, interrupts repeated tool calls and loads skills as needed to keep the initial tool instructions small.

The new skills cover file organisation, web research, document digests, Word documents, spreadsheet data and image processing. A bundled Python tool supports those tasks. Chinese and English voice input use local speech models, according to the changelog.

Mingbird's authors also publish a benchmark comparing four harnesses across four models and eighteen tasks. Their two-billion-parameter model scores about 0.82 in Mingbird and between 0.02 and 0.27 in the alternatives. These are the project's own scores on a self-built benchmark, with one machine and a task collection selected by its authors.

The repository makes that claim inspectable. It supplies per-task scores, a scorer that checks produced files and test outcomes, and a guide for reproducing one cell. The guide preserves the model and task budget when comparing harnesses.

The README acknowledges that single-run variation exceeds individual mechanism changes in its ablations, so the headline gap does not isolate one feature as the cause. It also distinguishes its regression suite from end-to-end model tests: the suite needs no live Ollama backend.

Version 1.9.2 addresses a concrete Windows failure. When Ollama stores a custom model directory in its application database, a server launched by Mingbird previously fell back to the default directory. The harness now reads that setting and passes it to the server process.

## Verification

| Claim | Label | Primary source | Independent check |
| --- | --- | --- | --- |
| Versions 1.9.1 on 1 October and 1.9.2 on 2 October; voice input, six skills, bundled Python and model-directory fix | VERIFIED | [Source](https://github.com/Mingbird/Mingbird-agent/blob/main/CHANGELOG.md) | none; documented release changes, not executed here |
| Ollama harness; Windows target, experimental Linux/macOS; Apache-2.0 code; test feedback, backups, loop interruption and on-demand tools | VERIFIED | [Source](https://github.com/Mingbird/Mingbird-agent) | none; repository implementation description |
| LRAB-288: 4 harnesses × 4 models × 18 tasks; same 2B model 0.821 versus 0.017–0.271 | VENDOR-REPORTED | [Source](https://github.com/Mingbird/Mingbird-agent) | none; self-built benchmark on one machine |
| Published per-cell data; reproduction and artifact-based scoring instructions | VERIFIED | [Source](https://github.com/Mingbird/Mingbird-agent/blob/main/benchmarks/reproduce_one.md) | none; reproduction not run |
| Single-execution variation exceeds per-mechanism ablation deltas; regression suite has no live-Ollama end-to-end test | VENDOR-REPORTED | [Source](https://github.com/Mingbird/Mingbird-agent) | none; disclosed limitations |
| Harness support is relevant to developers using small local models | ANALYSIS | [Source](https://github.com/Mingbird/Mingbird-agent) | Inference from documented feedback and context-management mechanisms |
