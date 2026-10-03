+++
title = "KAIST speeds coding agents by reusing generated text"
description = "AgSpec retrieves likely token continuations from an agent’s session and workspace. Its reported speedups measure generation throughput rather than complete task latency."
tags = ["research", "agents"]
date = 2026-10-03T05:45:20+02:00
draft = false
+++

KAIST’s AgSpec speeds coding-agent generation by retrieving likely continuations from existing text and adjusting how much text it proposes, rather than asking a separate draft model to generate every candidate token.

Sumin Lee, Sukmin Cho, Suengjae Lim and Youngjin Kwon, from KAIST’s School of Computing, exploit the repetition inside programming sessions. An agent often emits code, logs or fragments of an earlier attempt that the system already holds.

**Why it matters:** An engineer serving coding models can use that existing text to reduce sequential generation work. AgSpec examines where reusable material lives and how its form affects whether a candidate continuation will actually be accepted.

The [preprint](https://arxiv.org/abs/2610.01108), first submitted on 1 October, reports roughly two- to fourfold generation throughput on repository tasks at batch size one. The largest reported gains come from standalone coding: roughly five- to eightfold throughput against ordinary generation across three tested models.

Those numbers measure the generation phase, excluding prompt processing. They therefore describe decoding throughput rather than the time needed to complete an entire coding task, including tools, tests and initial input processing. The author-run experiments compare the same workloads and serving settings within each test.

Speculative decoding proposes several future tokens, then asks the target model to verify them together. Accepted tokens replace sequential target-model steps. A poor proposal wastes verification work, so the method’s usefulness depends on cheap drafts that frequently match what the target would accept.

Retrieval creates those drafts by copying a continuation after matching recent text. It is like completing a familiar passage from an existing document, with the language model checking every proposed continuation before committing it. AgSpec supplies the documents and chooses the length of the passage.

The documents come from three places: the ongoing session, files the agent has opened in its workspace and a global collection. Session memory preserves earlier turns even after they leave the immediate prompt. Workspace indexing also adapts text to the agent’s output format, so a file can match code emitted as an edit rather than only as raw contents.

## Longer drafts help only while verification accepts them

The authors identify two requirements for reuse: material must be available and its representation must match the output. Adding more source text cannot help when its surrounding format makes the relevant continuation difficult to find.

AgSpec also changes draft length. It profiles a cap for each agent role, then updates the length from verification feedback during the session. A coder reproducing familiar code can accept a longer draft than a planning agent composing a new explanation, and those patterns can change between turns.

The implementation runs in vLLM, an inference engine, on top of two existing retrieval approaches. The study tests Devstral-24B, Gemma3-27B and Qwen3.6-27B on SWE-bench Verified and TeamBench, repository-level workloads that include editing and checking code.

At batch size one, reported throughput ranges from 2.27 to 4.37 times ordinary generation; at batch size sixteen, it ranges from 1.08 to 4.76 times. The wider range makes the workload dependence visible. Verification of rejected candidates becomes more expensive as the batch grows.

Separate tests examine LiveCodeBench without a repository and Terminal-Bench with a single agent. Session and global text still supply reusable material in the former, while shared draft control replaces role-specific limits in the latter. The standalone coding gains therefore do not depend on having a workspace corpus.

The global corpus adds host-memory and loading costs, reported at roughly 2.5–4.3 GB and nine to fifteen seconds across the configurations. Session and workspace records are released after their sessions. These overheads sit alongside the authors’ decoding gains and matter to a serving implementation.

AgSpec remains a preprint result without an independent reproduction supplied in the paper. Its reported tests nevertheless isolate an actionable mechanism: keep recurring text available in the form the agent emits, and let acceptance feedback determine how aggressively to reuse it.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Lee, Cho, Lim and Kwon at KAIST; v1 submitted 1 October 2026. | VERIFIED | https://arxiv.org/abs/2610.01108 | none |
| Session/workspace/global retrieval, emission-format indexing and offline caps plus online acceptance control describe AgSpec. | VERIFIED | https://arxiv.org/abs/2610.01108 | none |
| Speculative proposal/target verification preserves output; retrieval avoids a separate drafting model in this design. | VERIFIED | https://arxiv.org/abs/2610.01108 | none |
| vLLM; two retrieval engines; Devstral-24B, Gemma3-27B, Qwen3.6-27B; SWE-bench Verified/TeamBench and LiveCodeBench/Terminal-Bench configurations. | VERIFIED | https://arxiv.org/abs/2610.01108 | none |
| Repository throughput 2.27–4.37× batch1 and 1.08–4.76× batch16; standalone LiveCodeBench 4.87–7.94×; prefill excluded. | VENDOR-REPORTED | https://arxiv.org/abs/2610.01108 | none |
| Larger-batch verification cost; global corpus 2.5–4.3GB, load9–15s; session-local corpus release. | VENDOR-REPORTED | https://arxiv.org/abs/2610.01108 | none |
| Serving-engineer consequence and passage-copying analogy explain retrieval; conclusion traces to acceptance and corpus tests. | ANALYSIS | https://arxiv.org/abs/2610.01108 | none |
