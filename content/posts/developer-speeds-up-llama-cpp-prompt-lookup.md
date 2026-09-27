+++
date = '2026-09-27T04:02:40+02:00'
draft = false
title = 'Developer Speeds Up llama.cpp Prompt Lookup'
+++

# Developer Speeds Up llama.cpp Prompt Lookup

A developer reports sharply lower drafting overhead for prompt-lookup decoding after redesigning the n-gram caches in a personal llama.cpp fork.

The work comprises four proposed changes that reduce data copying and replace parts of the cache structure. In an author-run benchmark on an Apple M4 Pro, the best measured drafting operation became as much as 42 times faster and peak memory use fell by as much as 2.6 times. Acceptance behavior reportedly stayed unchanged.

Those numbers need an important qualifier: the pull requests are open in the author's fork, not merged into the upstream `ggml-org/llama.cpp` project. This is a prototype and benchmark report, not a new official llama.cpp release.

## Why it matters

Prompt lookup is a form of speculative decoding designed for text with repetition. Instead of asking a separate small model to propose tokens, it finds n-grams in text already available to the system and offers likely continuations. The main model then verifies those draft tokens in parallel. Code editing, document transformation and structured generation can contain enough repeated material for that shortcut to help.

The verification step preserves the target model's output distribution, but the speedup depends on how often drafts are accepted and how expensive it is to find them. If maintaining the lookup cache costs too much CPU time or memory, some of the benefit disappears. The reported work attacks that bookkeeping cost.

## Four cache changes

The author describes three prompt-lookup caches: a context cache, a dynamic cache and a static cache. The patch series removes avoidable copies, uses a dense outer map, changes an inner map to a sorted vector and adds a read-only map design for the static cache.

These are conventional systems optimizations applied to a specific access pattern. Dense storage can improve locality when keys occupy a predictable range. Sorted vectors can be cheaper than general-purpose maps when collections are small or frequently scanned. A static structure can be built once and queried without paying for mutation machinery.

The benchmark uses WikiText-103, a 4,096-token context and the median of three runs on a 14-core Apple M4 Pro with 48GB of memory. It measures drafted-token latency, cache-loading time and peak memory. That disclosure makes the result easier to inspect, but it is still one machine, one corpus and an implementation maintained by the person reporting the result.

## What 42× does not mean

The largest figure applies to prompt-lookup drafting latency in the tested configuration. It does not mean every llama.cpp workload generates complete answers 42 times faster. End-to-end speed also includes target-model evaluation, sampling, prompt processing and any drafts the model rejects. Workloads with little repeated text may receive much less benefit.

The unchanged acceptance result is plausible because the proposal mechanism is being reorganized rather than intentionally altered. Even so, upstream review would need to check edge cases, memory ownership, portability and interactions with other llama.cpp features. Measurements on x86 CPUs, other Apple chips and longer contexts would clarify how broadly the result transfers.

The proposal is therefore promising engineering evidence, not a shipping performance guarantee. Its strongest contribution is narrower: it identifies n-gram cache management as a potentially significant bottleneck and supplies a patch stack that others can test.

## Verification

- **Tier 0 — VERIFIED AS AUTHOR REPORT:** The technical description, hardware, dataset and benchmark results appear in the developer's 26 September write-up: https://jadidbourbaki.github.io/blog/prompt-lookup-llama-cpp/
- **Tier 0 — VERIFIED:** The initial pull request and dependent patch series are open in the author's fork rather than upstream llama.cpp: https://github.com/jadidbourbaki/llama.cpp/pull/2
- **Tier 1 — AUTHOR-MEASURED:** The 42× latency and 2.6× memory figures were not independently reproduced here.
- **Tier 2 — ANALYSIS:** Expected workload sensitivity and requests for broader testing are editorial analysis.

## Glossary candidates

- **N-gram:** A sequence of a fixed number of adjacent tokens used here to find repeated continuations.
- **Speculative decoding:** Proposing several tokens cheaply, then verifying them with the target model in parallel.
- **Cache locality:** The performance benefit of arranging frequently accessed data so hardware can retrieve it efficiently.

Cold-reader sentence: A llama.cpp fork cuts prompt-lookup cache overhead, but its headline benchmark does not describe total generation speed or an upstream release.
