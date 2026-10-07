+++
title = "Google releases EmbeddingGemma 2 for multimodal search"
description = "Google's 740-million-parameter embedding model maps text, code, images, video and audio into one vector space, with modular encoders designed for local devices."
tags = ["models", "tools"]
date = 2026-10-07T04:01:57+02:00
draft = false
+++

Google has released EmbeddingGemma 2, a 740-million-parameter open-weight model that places text, code, images, video frames and audio in one shared embedding space.

The Apache-2.0 weights arrived on 6 October with support across Transformers, sentence-transformers, llama.cpp, vLLM, Ollama, LM Studio, MLX and Transformers.js. The model is meant for retrieval and routing rather than prose generation: it turns different kinds of input into vectors that can be compared for similarity.

## Why it matters

A developer building private search on a phone or laptop can now index a voice memo and retrieve a video segment without first chaining speech recognition, image captioning and a separate text embedder. That removes several moving parts from local retrieval, though the model's actual usefulness still depends on the user's own data and latency budget.

EmbeddingGemma 2 is modular. Its text-and-code backbone has 270 million parameters, while vision adds 170 million and audio adds 300 million. All configurations project into 768 dimensions, and Matryoshka training lets an application truncate vectors to 512, 256 or 128 dimensions to reduce storage.

Google says quantized text-only weights use about 191 MB of active RAM on a Pixel 11 Pro, rising to about 567 MB for the full model. Its 8,192-token context can hold up to 5.5 minutes of audio, 29 images or 58 video frames under Google's packing scheme.

The company's evaluation puts MTEB Code at 78.68, up from 68.76 for the first EmbeddingGemma. Google also claims leading quality among multimodal embedding models below one billion parameters. Those are release-day measurements rather than independent reproductions, and the model card is the better basis for comparing a particular retrieval task.

The release shares a tokenizer and audio-encoder design with Gemma 4, which can reduce duplicated components when the embedder feeds a local generative model. Google has also published sample applications for media search and video-moment retrieval.

The next practical evidence will come from tests on mixed private collections, where cross-modal recall, indexing time and memory matter more than a single aggregate benchmark.

## Verification

| Claim | Label | Primary source | Independent check |
| --- | --- | --- | --- |
| Google released EmbeddingGemma 2 on 6 October 2026 | VERIFIED | [Google announcement](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) | [weights and model card](https://huggingface.co/google/embeddinggemma-2) |
| The model has 740M parameters with modular 270M text, 170M vision and 300M audio components | VERIFIED | [Google announcement](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) | model card lists the architecture |
| Quantized active RAM is about 191 MB for text and 567 MB for the full model on Pixel 11 Pro | VENDOR-REPORTED | [Google announcement](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) | none |
| MTEB Code rose from 68.76 to 78.68 | VENDOR-REPORTED | [Google announcement](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) | none |
| Apache-2.0 weights are available | VERIFIED | [model repository](https://huggingface.co/google/embeddinggemma-2) | repository is accessible |
