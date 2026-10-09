+++
title = "Warm Compaction reuses cache for agent memory"
description = "The Apache-2.0 Hermes Agent plugin asks the main model to summarize a cached conversation prefix, cutting repeated prompt processing in its tests."
tags = ["agents", "tools"]
date = 2026-10-09T04:01:06+02:00
draft = false
+++

A new Hermes Agent plugin compresses long conversations by asking the main model to summarize a prompt prefix that the inference server has already cached.

Warm Compaction resends the agent's last request, adds only the newer conversation rows and appends a handoff instruction. The model returns a structured Markdown summary, which replaces the older history while a recent tail stays verbatim.

**Why it matters:** Context compression usually requires another large read of the conversation. For a developer running long agent sessions, reusing the server's prefix cache can reduce both the waiting time and the risk that a smaller, separate summarizer drops an important instruction.

The plugin uses documented Hermes Agent interfaces and requires no host patch. It supports manual and automatic compression, runs on Python 3.10 or later and is released under Apache 2.0. Installation is a Hermes plugin command followed by selecting `warm_compaction` as the context engine.

Its speed advantage depends on the same main model and an inference server that can reuse cached prompt blocks. The author lists hosted prompt-caching APIs, vLLM, SGLang, TensorRT-LLM, llama.cpp, MLX, Ollama and LM Studio as possible routes, but reports direct testing only on an NVIDIA DGX system and LM Studio. A request sent to a different llama.cpp slot, for example, can miss the cache.

The project includes evidence files for ten synthetic sessions of about 105,000 tokens. In those tests, Warm Compaction's median summary time was 16.8 seconds, compared with 43.5 seconds for `hermes-lcm` and 78.5 seconds for the built-in compressor. It retained 59 of 60 tested facts; the two comparisons retained 43 and 50. These are author-run results from one synthetic workload and different models were used by the three engines.

Failure handling is built into the design. If the warm request cannot run or fails its output checks, the plugin calls Hermes's auxiliary summary route. If that also fails, it writes a fixed-format summary and preserves the newest earlier summary as quoted text. A cancelled attempt leaves the history unchanged.

Hermes versions may eventually provide a native warm-handoff option. The plugin checks for that capability and can direct users to it, but remains separately selectable. The repository, settings and evidence are available on [GitHub](https://github.com/Elevatormusic/hermes-warm-compaction).

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Warm Compaction resends a cached prefix and adds new rows plus a handoff instruction | VERIFIED | [Repository](https://github.com/Elevatormusic/hermes-warm-compaction) | none |
| The plugin uses documented Hermes APIs and is Apache-2.0 licensed | VERIFIED | [Repository](https://github.com/Elevatormusic/hermes-warm-compaction) | none |
| The speedup requires the same model and a functioning prefix cache | VERIFIED | [Repository](https://github.com/Elevatormusic/hermes-warm-compaction) | none |
| Median compaction took 16.8 seconds in ten synthetic sessions | VENDOR-REPORTED | [Repository](https://github.com/Elevatormusic/hermes-warm-compaction) | none |
| The plugin retained 59 of 60 tested facts | VENDOR-REPORTED | [Repository](https://github.com/Elevatormusic/hermes-warm-compaction) | none |
| Failed warm requests use auxiliary and then fixed-format fallbacks | VERIFIED | [Repository](https://github.com/Elevatormusic/hermes-warm-compaction) | none |
