+++
title = "llama.cpp adds local probability-based decisions"
description = "The new System One endpoint scores typed choices in a single forward pass. Five converted model families support local deployment."
tags = ["models", "tools", "agents"]
date = 2026-10-03T05:21:20+02:00
draft = false
+++

llama.cpp, an open-source local inference engine, added an endpoint on 2 October that lets decision models return probabilities for predefined answers instead of generating a text response.

The maintainers, Xuan-Son Nguyen and Victor Mustar of ggml-org, describe a request containing the information to assess and a set of typed questions. The server runs a model over that information and returns scores the application can use directly.

**Why it matters:** A developer routing support requests can run the decision locally and receive a defined answer with its probability, using the same server that already hosts other models. The application supplies the choices rather than extracting them from a paragraph.

The [new endpoint](https://huggingface.co/blog/ggml-org/decision-models-in-llamacpp), `/v1/systemone`, follows the format introduced by TypeSafe's Jev decision model. Choice questions return the winning option and probabilities for all options; score questions return an expected level on an ordered scale; yes/no questions return the probability of yes. The implementation was merged into the project on 2 October.

The initial release supports five model families, from the 144-million-parameter Julia-1 to the 27-billion-parameter OpenJev. OpenJev also accepts images. Kev-4B, lev and OpenJev can reuse the input when answering several questions, while router mode loads a requested model on demand. The [server implementation](https://github.com/ggml-org/llama.cpp/pull/29818) adds decision heads, conversion metadata and request handling to existing model infrastructure.

The maintainers report median answer times ranging from 3 to 43 milliseconds across the five models on one NVIDIA RTX PRO 6000. Their examples also show why the probabilities need model-specific interpretation: the same vague account question received confidence of 0.25 from Julia-1 and 0.80 from Kev-4B. Adding descriptions to bare answer labels changed Julia-1's routing result in another example.

The GGUF weights are available through the project's model collection. The [Kev-4B card](https://huggingface.co/ggml-org/Kev-4B-GGUF) lists Apache 2.0 licensing and a local launch command. The maintainers identify Cloudflare's Clef as the next model they plan to add.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Nguyen and Mustar announced the endpoint on 2 October; its three typed questions and response structure are documented. | VERIFIED | [Maintainers' article](https://huggingface.co/blog/ggml-org/decision-models-in-llamacpp) | none |
| The implementation merged on 2 October and adds heads, conversion metadata and server handling; five families, image support and input reuse are documented. | VERIFIED | [Merged implementation](https://github.com/ggml-org/llama.cpp/pull/29818) | none |
| Julia-1 has 144M parameters, OpenJev 27B; median latency spans 3–43 ms on one RTX PRO 6000. Confidence examples are 0.25 and 0.80. | VENDOR-REPORTED | [Maintainers' measurements](https://huggingface.co/blog/ggml-org/decision-models-in-llamacpp) | none |
| Local scoring supplies defined choices to a routing application without parsing generated prose. | ANALYSIS | [Request and response examples](https://huggingface.co/blog/ggml-org/decision-models-in-llamacpp) | none |
| Kev-4B GGUF weights use Apache 2.0 and provide a launch command; Clef support is planned. | VERIFIED | [Model card](https://huggingface.co/ggml-org/Kev-4B-GGUF), [Roadmap](https://huggingface.co/blog/ggml-org/decision-models-in-llamacpp) | none |
