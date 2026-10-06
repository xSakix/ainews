+++
title = "vLLM shows when split serving helps and hurts"
description = "A practical guide measures the trade-off in separating prompt processing from token generation. Tail latency improves under load, but moving the model's working memory delays the first token."
tags = ["essays", "tools", "hardware"]
date = 2026-10-06T04:04:31+02:00
draft = false
+++

Splitting prompt processing from token generation can stabilise a model server under load, but transferring its working memory may make the first response slower, vLLM's team reports.

The open-source inference project tested “disaggregated serving”, in which one GPU handles prefill and another handles decode. Prefill reads the prompt and builds the key-value cache; decode uses that cache to generate tokens. The guide also moves tokenisation and output parsing to a GPU-free front end.

For an operator serving long prompts, the design offers a choice between two kinds of delay. Separating the phases prevents a large prompt from interrupting generation for other users, but the cache has to travel between workers before decoding starts.

In vLLM's two-GPU test with Qwen2.5-7B and 8,000-token prompts, the 99th-percentile gap between generated tokens rose from 23 milliseconds to 169 milliseconds for the combined setup at 0.4 requests per second. The split setup held that gap between 25 and 52 milliseconds.

The same experiment exposed the cost. Moving about 470 MB of cache for each prompt took roughly 1.3 seconds, and median time to the first token was 2.2 seconds, compared with 0.7 seconds when both phases shared a worker. The L40S GPUs had neither NVLink nor direct peer-to-peer transfer, so the result describes a deliberately unfavourable transport path rather than every deployment.

The authors' decision rule is practical: check the GPU topology first, then inspect cache-transfer metrics under the intended prompt length and request rate. Disaggregation is most attractive when prefill repeatedly disrupts decode or when the two phases need different scaling. A lightly loaded server can pay the transfer cost without gaining useful isolation.

The guide cites larger results from AMD and the llm-d project, but those tests use different models, accelerators and cluster sizes. They support the architecture's potential, not a portable speed-up figure.

The instructions target vLLM 0.30.0 or later and include separate renderer and derenderer services. The team says integration gaps remain, making the topology and transfer checks a prerequisite rather than a post-deployment optimisation.

## Verification

| Claim | Label | Primary source | Independent check |
| --- | --- | --- | --- |
| vLLM documents separate prefill, decode and GPU-free front-end services | VERIFIED | [vLLM guide](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | public vLLM configuration and commands |
| At 0.4 req/s, collocated p99 token gap reached 169 ms while split serving stayed at 25–52 ms | VENDOR-REPORTED | [vLLM guide](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | none; project-run test |
| An 8k-token prompt produced about 470 MB of cache and a roughly 1.3 s transfer | VENDOR-REPORTED | [vLLM guide](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | none |
| Median first-token time was 2.2 s split versus 0.7 s collocated | VENDOR-REPORTED | [vLLM guide](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | none |
| The test used two L40S GPUs without NVLink or peer-to-peer transfer | VERIFIED | [vLLM guide](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | test configuration stated by authors |
| The guide targets vLLM 0.30.0 or later | VERIFIED | [vLLM guide](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | version requirement in guide |
