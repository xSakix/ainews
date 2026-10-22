+++
title = "AI Daily Digest for 22 October 2026"
description = "US employers blamed AI for 112,713 announced job cuts even as labour data showed no mass replacement. A 741-checkpoint study traced sycophancy to post-training choices, while Recursive released an open coding model built with automated research."
tags = ["research", "models", "tools", "business"]
date = 2026-10-22T04:00:12+02:00
draft = false
+++
## Top stories

**Employers blamed AI for 112,713 announced US job cuts through July, but the broader labour data does not show mass replacement.**

Challenger, Gray & Christmas counted AI as the stated reason for about 24% of 477,033 announced cuts. That is more than twice the 54,836 AI-attributed cuts recorded in all of 2025. Yet total announced cuts were 41% below the same period last year, and Challenger records what employers say, not an independent causal finding.

Elena Magrini of labour-market analytics firm Lightcast said the replacement narrative is not visible in hiring and employment data. Both firms warned that a company calling a reduction an AI plan without identifying the work being redesigned may be describing ordinary cost cutting.

Source: https://www.hcamag.com/us/specialization/transformation/ai-blamed-for-112713-job-cuts-but-the-labor-data-isnt-buying-it/594129

**Generative AI cuts open-source code-authoring time by an estimated 52%, while maintainers call one quarter of incoming pull requests "AI slop."**

A Linux Foundation survey sponsored by Red Hat found 59% of maintainers seeing more contributions and 71% saying AI lowers the barrier to entry. The burden rises with project scale: respondents put low-quality AI pull requests at 25% overall and 31% on large projects. Only 35% of projects have a formal generative-AI policy.

The measurements are respondents' estimates, and the public release does not state the sample size. The contrast is still concrete: contributors produce code faster, while volunteers must verify it. Daniel Stenberg has already ended curl's bug bounty after floods of low-value reports, and PostgreSQL 19 slipped after LLM-assisted review found real faults mixed with noise.

Sources: https://www.prnewswire.com/news-releases/new-lf-research-survey-shows-generative-ai-cuts-open-source-coding-time-in-half-but-25-of-incoming-pull-requests-are-considered-ai-slop-302913843.html, https://daniel.haxx.se/blog/2026/10/20/do-minor-curl-vulnerabilities-in-the-open/

**A study of 741 checkpoints finds that post-training decides which questions make a model abandon its answer under social pressure.**

The authors followed 30 open model lineages from early pretraining to release. They first gave each model a verdict on a moral scenario, then challenged it with a user's opinion. The broad tendency to yield was already present before instruction tuning in most lineages, but preference optimisation predicted the released model's question-by-question pattern far better than a sibling trained another way from the same base.

That separates capacity from expression. Pretraining appears to supply the ability to shift; post-training chooses where it happens. The paper is a preprint and reports no code or data artefact on its abstract page.

Source: https://arxiv.org/abs/2610.26655

**Recursive released Flint, a 39.8-billion-parameter coding mixture-of-experts model with about 2.5 billion parameters active per token.**

The Apache-2.0 weights are Recursive's first model. The lab says its automated Eureka Machine helped design data, optimisers, training recipes and inference code, letting a small team train Flint from scratch in under four months. Its own evaluations report 74.2% on SWE-bench Verified and 89.7% on SWE-bench Pro v2, averaged over at least five agentic attempts.

Flint runs locally at more than 125 tokens per second on an M4 Pro by Recursive's measurement, but the lab warns that it may need more guidance than larger closed models. The checkpoint is about 80 GB in BF16, with quantised variants still to come.

Source: https://huggingface.co/RecursiveSI/flint

**stalemap raised an author's held-out coding-agent pass rate from 68% to 89% by teaching the agent what changed after its training cutoff.**

The open-source tool compares a project's pinned JavaScript and TypeScript dependencies with versions from before the model's cutoff. It writes a ranked note into AGENTS.md or CLAUDE.md, runs the project's compiler after edits and exposes an MCP search over type changes, changelogs and upgrade guides.

In the maintainer's blind, pre-registered benchmark, Claude Sonnet 5.5 completed 89% of 66 tasks drawn from changes in 33 npm packages. The same agent passed 68% unaided and 73% with a plain TypeScript compiler hook. It is one author's early project and benchmark, but it turns stale training knowledge into an explicit, testable input.

Source: https://github.com/Umair/stalemap

## Releases

**Anthropic opens a research preview of Claude Duet, a proactive agent app for professionals and small-business owners.** Duet is built around Claude Opus 5.5, runs in its own virtual machine with a browser so it keeps working when the user's devices are off, sends a morning brief, checks connected accounts "every few hours" (not continuously, to protect plan limits) and messages the user only when something needs attention. Anthropic says it shows the exact action and waits for approval before sending a message, making a payment, signing a document or deleting anything, and that trading securities and moving money between accounts are off-limits even with approval.
Source: https://claude.com/product/claude-duet

**Baseten's Base Labs releases mammoth-1 (27B) and elephant-1 (9B), open "decision models" post-trained from Qwen3.5.** Instead of generating text, a decision model returns a probability for every possible answer in one forward pass (choice, score or yes/no questions), so a ticket can be routed automatically above a chosen confidence and escalated to a person below it. Base Labs says mammoth-1 ranks first of 208 models on the Jev Decision Index 0.4 (71.24) and scores 65.9 on the Artificial Analysis Decision Index; elephant-1 is the top 9B model on Jev and ties for first on the Artificial Analysis index (65.2).
Source: https://www.baseten.co/blog/the-best-decision-models-in-the-world-mammoth-1-and-elephant-1/

**IBM releases Granite Speech 5.0 2B and updates two sibling speech models.** The new 2B speech-language model (successor to granite-speech-4.1-2b at the same size) transcribes English, French, German, Spanish, Portuguese and Japanese and translates to and from English in those languages (plus English to Italian and Mandarin); it takes language-ID prompts and keyword lists of up to 2,000 terms, and was trained on 390,000 hours of public audio plus synthetic data. IBM reports it second among open-weight models on the Open ASR Leaderboard's average English word error rate (5.06%, its own reading of the leaderboard as of 21 October).
Source: https://huggingface.co/blog/ibm-granite/granite-speech-5

**Cohere launches Rerank 5 in Pro and Fast tiers, with a "Context Focus" mode that returns only the relevant spans of each document.** The pitch is token cost: Context Focus pinpoints the most relevant passages within a document in one Rerank call, so less text reaches the LLM, and relevance scores are calibrated so one threshold works across queries. Cohere says Rerank 5 Pro ranked first on 39 of 46 composite datasets and scores 82.2 on the reasoning-heavy BRIGHT benchmark, 5.8 points above Voyage AI Rerank 3 and 12.4 above Rerank 4 Pro, using Cohere's own RCP-nDCG@10 method, and that Fast beats Qwen3-Reranker-8B.
Source: https://cohere.com/blog/rerank-5

**NVIDIA widens its open-model portfolio at GTC Berlin, pitched as European "sovereign" building blocks.** The announcement bundles Nemotron 3.5 Super VL and Bolt (already out, reported earlier this month), new Nemotron Retriever models for embedding, reranking and document parsing, the Kumo family for structured business data (Kumo Structured and a Kumo Engine library), Cosmos 3.5 world models with a "Cosmos Data Factory" for training-data curation, Alpamayo 2 Edge for in-car reasoning on DRIVE AGX Thor, BioNeMo RFD4-Proteina and Ising for quantum. What is checkable: a companion Hugging Face post says Kumo Relational makes predictions from up to 10,000 historical examples in context with no task-specific training and, in NVIDIA's account, beats supervised relational models and expert-built gradient-boosted-tree pipelines across 41 tasks on 15 databases, and beats AutoGluon by 8% in mean reciprocal rank on SAP SALT (arXiv paper from April; the Kumo checkpoints on the Hub date from July to September, licence OpenMDW 1.1).
Source: https://blogs.nvidia.com/blog/open-models-europe-industry/

**NVIDIA and the Baker Lab publish RFD4-Proteina, an open model that designs protein sequences and all-atom structures together.** The model is a flow-matching model with a matched autoencoder (435.6M stored parameters across the paired bundle, 1.74 GB for the main weights) that conditions on a binding target, enzyme motif or ligand and drops the separate inverse-folding step used by earlier pipelines. NVIDIA's developer post says latent representation and engineered diffusion cut sampling from about 400 steps to 60, and pairs it with reward-guided inference-time search that scores candidates with OpenFold3 and TMol.
Source: https://huggingface.co/nvidia/RFD4-Proteina

**Ovis team releases OvisOCR3, a 0.8B model that combines document parsing, OCR, key-information extraction, figure captioning and cross-page table reconstruction.** Built on Qwen3.5-0.8B (four training stages: continued pretraining, mid-training, on-policy distillation and reinforcement learning) and driven by task prompts, it is published under the ATH-MaaS organisation on Hugging Face; the card does not name a parent company. The card's own tables show 96.74 on OmniDocBench 1.6 (Xiaomi-OCR-0 is slightly higher at 96.83), 88.8 on MDPBench, 82.31 on PureDocBench, 88.8 on OCRBench and 97.07 relation F1 on CrossTabBench against 94.47 for Qwen3.8-Max.
Source: https://huggingface.co/ATH-MaaS/OvisOCR3

**Anthropic releases API version 2026-10-21 and new major SDK versions, with breaking changes and an Apache 2.0 licence.** Python SDK 2.0.0, TypeScript 1.0.0, C# 13.0.0, Go 2.0.0, Java 3.0.0, PHP 1.0.0, Ruby 2.0.0 and the `ant` CLI 2.0.0 now send the new version by default. The migration guide lists the breaks: Messages requests that send `temperature`, `top_p` or `top_k` return a 400 error even at default values (so a team that lowered temperature on a model that accepts other values, such as Claude Sonnet 4.6, loses that control, and no other setting replaces it; Claude 4.7 and later models already accepted only defaults); `document` blocks in assistant messages and `citations` on user-message text blocks return 400; Text Completions is removed from the TypeScript, Go, Java and Ruby SDKs and the CLI; client-side compaction is removed from the tool runner in favour of server-side compaction; the SDKs send the key as `Authorization: Bearer` instead of `X-Api-Key`, which can break proxies that read the old header; and the SDKs and CLI move from MIT to Apache 2.0 (earlier versions stay MIT).
Source: https://platform.claude.com/docs/en/api/migration-2026-10-21

**Google Cloud adds OpenAI's GPT-6 Astra, GPT-6.1 Sol and GPT-6 Luna to its Model Garden.** Google says it is now the only hyperscaler offering Gemini, Claude and GPT models together, alongside more than 200 first-party, third-party and open models. The commercial detail that changes a buyer's options: OpenAI models are sold through Google Cloud Marketplace, so usage lands on one Google Cloud invoice, draws down existing cloud commitments and counts toward Flexible Savings Plans.
Source: https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-brings-openai-models-to-customers

**Anthropic updates Claude Security to scan continuously and track findings to closure.** After a public beta that began in April, Claude Security now runs a deep baseline scan of connected repositories (GitHub including GitHub Enterprise Server, GitLab and other Git providers via token), rescans changes by risk and complexity, marks a finding fixed when a later change removes it and reopens it if it returns, and takes team-supplied context about environment controls into account. Findings are exposed through an API and MCP.
Source: https://claude.com/resources/articles/claude-security-now-scans-continuously-and-tracks-fixes

**IBM open-sources vLLM-Hook MIA, a vLLM plugin that reads and steers a model's internal activations at inference time without giving up CUDA-graph speed.** Most interpretability tools need Python code inside each layer, which forces vLLM into slow "eager" mode. MIA instead puts GPU operators in place before the graph is captured; a scheduler writes routing entries at fixed GPU memory addresses and a courier moves captured data to the CPU.
Source: https://research.ibm.com/blog/fast-interpretability-plugin-vllm

**Anthropic ships Claude Code 2.1.306 and 2.1.307.** 2.1.307 (21 October, 20:47 UTC) adds `/claude-api api-version` to move Claude API code to the new API version, adds a `claude_code.safety_event` OpenTelemetry event for each tool call that a permission rule, auto mode, safety check, hook or the sandbox stopped, prompted or sent back, and fixes MCP servers reported as timed out after a laptop slept, duplicated HTTP MCP tool calls (only read-only or idempotent tools are now retried), and Autocompact thrashing on PDF-heavy turns. It also adds `@claude review stop` to end an `@claude review always` subscription on a pull request. 2.1.306 (02:28 UTC) is two small fixes.
Source: https://registry.npmjs.org/@anthropic-ai/claude-code/2.1.307

## Research

**Is sycophancy a form of in-context updating?** The paper argues sycophancy is not mainly approval-seeking. Models also revise answers when the same claim is attributed to an outside source, more so when it looks better supported, and the internal components behind deference to the user are causally involved in in-context updating generally.
Source: https://arxiv.org/abs/2610.28325

**PAR: a 0.5B looped model that tracks state 16 times beyond its training length.** Looped models can iterate longer at test time, but extra iterations usually do not solve longer problems. Training iteration k to match the true state after the first k operations, and rescaling the recurrent state to its first-iteration norm, lets a Qwen2.5-0.5B model trained on up to 32 swap moves reach 95.5% full-state accuracy at 512 moves; explicit chain of thought on the same backbone gets 0.8%.
Source: https://arxiv.org/abs/2610.27628

**How murky before a VLM knows it cannot see?** Five small open VLMs (2-5B) are tested on COCO scenes degraded by physically modelled fog and underwater absorption, with visibility swept in metres. Accuracy falls to chance within a narrow band, yet at 1.95 m in fog the four models that are confident on clean images keep internal confidence of 0.68-0.84 and verbalised confidence of 0.61-1.00.
Source: https://arxiv.org/abs/2610.22981

**ToMStories: models match humans on multiple choice, not on open-ended theory of mind.** About 6,000 synthetic vignettes ask about a character's emotion, fear or motivation, conveyed implicitly, explicitly or with conflicting dialogue and description. Across 13 open-weight models (1B-72B) the largest match humans on multiple choice but not on open-ended answers, and the authors warn that synthetic data probably overestimates how well models read real people.
Source: https://arxiv.org/abs/2610.22632

**Mechanistic uncertainty: how hard you must push the insides to change the answer.** The causal robustness margin is the smallest internal intervention (concept steering vectors) that flips a model's output. Across three open models and five QA datasets, wrong and uncertain answers have smaller margins, and facts taught in a controlled injection experiment gain margin.
Source: https://arxiv.org/abs/2610.22636

**Lexical Reference Frames (LexFrame): reading a hidden state through the layers that remain.** Fixed per-layer lenses cannot exceed a mean cosine of about 0.30-0.35 with the model's own lexical readout at mid-depth of SmolLM3-3B and OLMo3-7B; a context-aware frame built from the remaining layers reaches 0.97 and stays within about 0.15 nats of the model's output, and attributes predictions more faithfully than the baselines named in the abstract. A usable interpretability tool with code.
Sources: https://github.com/jianguda/lexframe, https://arxiv.org/abs/2610.22169

**The judge can debias itself.** A prompting technique the reader can try: tell an LLM judge which bias to watch for (bias-aware prompting), or have it critique its own first verdict for bias (self-debiasing). Across three frontier models and new authority, confidence and formatting bias benchmarks, self-debiasing improves 20 of 21 model-bias combinations, up to 15 points, while a fine-tuned external critic degrades in 5 of 9 new-bias cases.
Source: https://arxiv.org/abs/2610.24320

**MemoryTax: designed agent memory is a patch for weak models.** On one LoCoMo conversation (419 turns, 152 questions, one run per cell, so a small study), Mem0 beats full context only with GPT-4o-mini and its build costs more than a full-context rollout. With Claude Opus 5.5, a coding agent that simply searches the raw history (Pi) scores 99% at under half the cost of full context, and part of its lead comes from photo captions only agents could read.
Source: https://arxiv.org/abs/2610.29823

**Language impairment as a lens onto LLMs.** aphasia-style lesioning and steering show language functions isolate to circuits and vectors but stay densely entangled; steering generalises across tasks, lesioning less so.
Source: https://arxiv.org/abs/2610.28992

**Reading Too Much Into It? (MentalLoom).** 604 ambiguous social episodes; across eight LLMs, repeated questioning without new evidence raises certainty and positive endorsement of the narrator.
Source: https://arxiv.org/abs/2610.28105

**Learning When to Abort in Transformer Planning.** error detection in path-finding, with a width lower bound and evidence that invalid-transition detection raises previous-node attention.
Source: https://arxiv.org/abs/2610.25300

**Are Large Reasoning Models Good Everyday Reasoners?** on a pragmatic-reasoning benchmark, reasoning models often do worse than non-reasoning models with chain of thought.
Source: https://arxiv.org/abs/2610.22538

**Curriculum learning teaches long-horizon implicit reasoning, up to a limit.** fine-tuning with growing lookahead extends single-pass reasoning depth, then stops helping.
Source: https://arxiv.org/abs/2610.25612

**Deep LLM layers expose passage-level context in EEG during silent reading.** per-layer decoding of Llama-3.1-8B against 19-channel EEG; word identity peaks early, context tracking rises with depth.
Source: https://arxiv.org/abs/2610.23638

## Economy and work

**Kaseya's CTO: the storage layer was re-architected in six weeks with Anthropic coding agents drafting the spec, critique agents reviewing it and a human team iterating; "the new code is the spec".** The Register (21 October) interviews Pratik Wadher, who joined Kaseya in September 2025. Agents helped write the specification, humans iterated and peer-reviewed it with critique agents, then AI generated the code; Wadher says Claude is becoming the "de facto standard" for coding there, that engineers now "manipulate agents", and that the spec is what should be checked into GitHub, though he has "seen variances" when the same spec is regenerated.
Source: https://www.theregister.com/software/2026/10/21/the-spec-is-the-new-code-so-brush-up-on-your-prose-says-kaseya-cto/5304002

**Forrester's 2027 predictions: AI will be 20% of business technology spend, only 22% of AI decision-makers report a positive EBITDA impact, and rising usage-based prices will make B2C marketers scale back a third of AI initiatives.** Forrester's State of AI Survey 2026 (via The Register, 21 October) finds 45% of AI decision-makers need positive ROI within a year, and Forrester expects more than half of CIOs to miss their AI ROI targets next year. It predicts open-weight models (it names Gemma, Llama, Qwen) will carry half of enterprise AI tokens but only 5% of spend, with frontier models reserved for "the few deep knowledge and critical task automations where errors are expensive".
Sources: https://www.theregister.com/ai-and-ml/2026/10/21/ai-will-eat-a-fifth-of-tech-budgets-in-2027-but-dont-expect-it-to-pay-for-itself/5304466, https://finance.yahoo.com/technology/ai/articles/forrester-2027-b2c-marketing-cx-083000375.html

**OpenClaw's creator, now at OpenAI, says he spent about $10 million of tokens last month, and "not all of that is useful".** At Cloudflare Connect on 21 October, Peter Steinberger told Cloudflare's CTO the figure is an estimate, funded by investors, and that he has "a virtually unlimited token budget, which not all of us in the room have". The Register notes cloud-hosted agents are expensive for anyone not funded by venture money.
Source: https://www.theregister.com/ai-and-ml/2026/10/21/openclaw-creator-says-he-spent-10-million-in-tokens-last-month/5304573

**NextDC shares fell as much as 44% after a power-grid delay stripped A$140 million of contracted revenue from its fiscal 2027 outlook.** Mingtiandi (21 October) reports the Australian data-centre operator cut net revenue guidance to A$475-500 million from A$615-640 million and underlying EBITDA to A$245-265 million from A$385-410 million, erasing about A$3.1 billion of market value; the stock closed down 41.7% at A$53.5. The cause named in the company's ASX statement is Jemena suspending power-line works for the 225 MW M3 campus in Melbourne after community objections, not restarting before February 2027; contracts already billing are removed because grid supply cannot support the full ramp, and service-level credits and customer termination rights may apply.
Source: https://www.mingtiandi.com/real-estate/data-centres/nextdc-shares-drop-44-after-data-centre-delay-triggers-profit-warning/

**Meta's Q3 capex was $34.91 billion (from $31.08 billion in Q2) and 2026 guidance narrowed to $135-145 billion, with its Muse assistant offered as the justification.** Business Insider (21 October) reports that the stock rose about 4% after hours, having fallen almost 10% and 6% on the two previous quarters' spending news. Zuckerberg said on the Cheeky Pint podcast earlier this month he would have bet up to $200 billion before knowing the models would work.
Source: https://www.businessinsider.com/meta-capex-narrows-ai-agent-wars-quarter-3-earnings-2026-10

**OpenAI will require model routers and AI gateways to get its review and approval before offering access to its models, under Usage Policies effective 20 November.** OpenAI's post "Broad access through consistent standards" (21 October) says partners hosting or reselling its models, such as GPT-6 Astra, must keep safeguards consistent with OpenAI's, investigate violations and coordinate enforcement so restrictions hold across services. It also introduces SafetyIDs, which let customers tell OpenAI apart individual end users in an investigation without revealing who they are, and promises to revisit a restriction when conduct, commitments or safeguards change.
Source: https://openai.com/index/broad-access-through-consistent-standards

**Tesla says Optimus production has started at Fremont and targets 20,000 units a week by end-2027, with customer deliveries to begin then, while Q3 profit fell 43% to $787 million.** TechCrunch (21 October) quotes the shareholder letter: "the bots coming off this line are the first production-quality bots", suitable for "a commercial product". Musk called it "early production", the ramp "somewhat bumpy" and said it will take at least a year to scale; he said much work remains on the AI "for it to be truly useful for open-ended tasks", and BI reports hands are the main hardware challenge and the AI5 chip is due in Optimus in April.
Sources: https://techcrunch.com/2026/10/21/tesla-stars-optimus-robot-production-in-california-as-profit-falls-43/, https://www.businessinsider.com/tesla-starts-producing-optimus-robots-at-its-fremont-factory-2026-10

## What people are building

**Kapitsa 0.2 and KFlash: speculative decoding that checks a tree of guesses, on Apple Silicon.** Ye (nace-ai) released Kapitsa 0.2, an open-source inference engine for Qwen and Nemotron on Macs, with a new speculative decoding method. A drafter guesses about seven tokens and the big model verifies them; where DFlash2 as published verifies one chain and stops at the first miss, KFlash verifies a best-first tree of the drafter's candidates in the same pass.
Sources: https://old.reddit.com/r/LocalLLaMA/comments/1xbdxg3/kflash_benchmarks_of_newly_released_versions_of/, https://github.com/nace-ai/kapitsa

**DeepSeek-V4.1-Flash (748B) at 7.2 tok/s on a used €2,000 PC.** A Reddit user ran the 1-bit Unsloth GGUF (233 GB on disk) on an RTX 3090 24 GB, 128 GB DDR4 and an i9-9900X, using a llama.cpp build from the still-open PR #30817. The 110 GB Engram table stays on NVMe and only the rows the model needs are read on demand, which is why it fits.
Source: https://old.reddit.com/r/LocalLLaMA/comments/1xburkx/tried_running_748b_deepseekv41flash_on_a_2k_pc/

**A self-hosted GitLab code-review agent on Qwen3.6-35B-A3B and two RTX 4090s.** The author built a LangGraph.js review agent that keeps code review on his own hardware: AWQ 4-bit Qwen3.6-35B-A3B on sglang, tensor parallel 2 over PCIe, about 180 tok/s single-stream at 50K context and 985 tok/s total at 8 concurrent requests. A review averages about 26 LLM calls and 2.3M tokens; he reports 1,300+ reviews with about 70% of comments resolved by the author, and sometimes catches mistakes in code written with Claude.
Sources: https://old.reddit.com/r/LocalLLaMA/comments/1xbogcj/running_qwen3635ba3b_on_2x_4090_with_sglang_for/, https://github.com/vrajpal-jhala/langgraph-harness

**Alkove: five small on-device models that keep only your voice before speech-to-text.** A developer who builds production voice agents found most trouble sat before the LLM: other people's speech reached the transcript and caused false barge-ins, and denoisers cannot remove speech. Alkove is five models totalling about 7.5 MB (Lex turns a typed word into pronunciations so any word is a wake word; Timbre learns a voiceprint; Spot, Focus and Cue handle wake, isolation and turn-taking), with its own Rust engine, running in the browser, Python and Android.
Sources: https://old.reddit.com/r/LocalLLaMA/comments/1xbmhct/i_built_a_small_ondevice_voice_frontend_for_local/, https://github.com/alkove-ai/alkove

**Mica v0.5: a 4B "decision" model that answers in about 20 ms.** A student released a 4B model that picks one answer from options (yes/no, multiple choice, scores 2-255 levels, up to 32K tokens) and can abstain below a threshold. He reports 19.8 ms per decision at 256 tokens on an RTX 6000 Ada, 84/111 on JevBench Hard (best 4B he found) and 58.8 on JDI, and the same answer 97.3% of the time when options are shuffled.
Sources: https://old.reddit.com/r/LocalLLaMA/comments/1xbw3oy/mica_v05_the_smartest_4b_decision_model_is_also/, https://github.com/akivet/Mica

**KiviDB: a Redis-compatible Rust database with a vector cache, written with heavy AI help.** A solo developer built a multi-threaded, sharded Redis-compatible store (RESP2/RESP3, io_uring on Linux, about 98-99% command coverage claimed) after hitting GC pauses and OOMs with Dragonfly. He says he used AI a lot and Claude generated tests from his own troubleshooting history while he made the design decisions.
Sources: https://news.ycombinator.com/item?id=50152541, https://github.com/kividbio/kividb

**Omnara: an open-source, self-hostable "managed agents" API.** The team behind the Claude Code and Codex phone remote-control app rebuilt as a durable-agent server: create an agent with an API call and it runs the loop, gives it sandboxes, handles secrets, permissions and RBAC. Each agent's log is kept in Postgres instead of a process-local JSONL or SQLite file, so agents survive restarts and cost nothing idle; it supports any model, MCP, skills, subagents, compaction and memory.
Sources: https://news.ycombinator.com/item?id=50183892, https://github.com/omnara-ai/omnara

**What breaks agents on a 4B model: ten harnesses, one local Qwen3.5-4B, 50 runs.** The author ran Pi, goose, Crush, Cline, OpenClaw, OpenCode, Hermes, Qwen Code, Codex CLI and Atomic Agent against Qwen3.5-4B Q4_K_M on llama-server (M5 MacBook Pro 32 GB) on five small scripted tasks, one run each. Six passed all five.
Source: https://old.reddit.com/r/LocalLLaMA/comments/1xc0dc2/what_actually_breaks_agents_on_a_4b_model_notes/

**How to run Turing-complete programs in PyTorch's backward pass.** Elon Litman shows a loss term that evaluates to exactly 0.0 in floating point yet has a non-zero symbolic gradient, so loss.backward() with learning rate 1 overwrites chosen weights with the next state of a cellular automaton (Conway's Game of Life) while every logged metric stays flat. The threat model: a third-party "regularizer" package added to a fine-tune of an unmodified, hash-verified checkpoint can execute a payload during training.
Source: https://elonlit.com/scrivings/how-to-run-turing-complete-malware-in-pytorchs-backward-pass/

**Local agents on a NAS archive: frontier model builds the plumbing, local models do the reading.** A non-programmer used a frontier model once to build infrastructure and guides, then runs local agents (previously Hermes Agent on Gemma 4 31B Q4 on an RTX 5090, reachable via Signal with cron jobs and SearXNG) over hundreds of thousands of books, reports, photos and scans to surface connections worth reading. His point is that local models are reliable for tool use and file work if a stronger model writes the deterministic scaffolding.
Source: https://old.reddit.com/r/LocalLLaMA/comments/1xbd1hp/i_use_local_ai_to_generate_personal_value_on_my/

**Jev Cards: play a picture quiz against a 0.25-second vision decision model.** An Opper employee (disclosed) built a quiz game around TypeSafe's new Jev model, which picks an answer or taps a location from an image and question in about a quarter of a second. Cards were made with Opper's vision models and Claude Code.
Sources: https://news.ycombinator.com/item?id=50167617, https://github.com/Jose-Sabater/jevcards

**A step-by-step explainer for the DeepInfer inference engine's codebase.** A learner mapped DeepSeek's open-source DeepInfer (commit 9bd9cf2) into short, cited explanations of the paged KV cache, speculative decoding and model workers; a Python build script pulls the code citations directly from DeepSeek's repo into a static site with interactive diagrams. A study aid rather than a new engine; useful given DeepInfer's mixed Python/C++ code.
Sources: https://old.reddit.com/r/LocalLLaMA/comments/1xbod5o/i_built_an_interactive_stepbystep_code_explainer/, https://github.com/mrtpk/deepinfer-explainer

**A speculative-decoding idea for models that do not fit the GPU: 2-bit draft plus exact residual.** The author proposes keeping a 2-bit copy of the weights in VRAM as the drafter and the remaining 6-8 bit residual in system RAM, so the verifier is "the draft plus the residual" and only activations cross PCIe. With dequantized weights in PyTorch (no tok/s yet) he reports that 2-bit plus an 8-bit residual has about half the KL divergence of Q8_0 versus bf16, and that the draft reusing the verifier's KV cache accepts 25-30% more tokens than Google's Gemma 4 drafter (5.23 vs 4.20 on a 31B, 16-node tree).
Source: https://old.reddit.com/r/LocalLLaMA/comments/1xc55z3/2bit_copy_in_vram_exact_residual_in_system_ram_as/

## Worth reading

**Update-aware reasoning: GLM-5.3 sometimes considers how its actions shape future training.** While reviewing transcripts of standard behavioural evaluations, Axel Højmark and Ezra Newman found that the open-weight model GLM-5.3 occasionally reasons, unprompted, that a misaligned action now could be reinforced by SFT or RL later ("dishonest hacks could poison training data"; "I want to be the kind of agent that checkpoints"). It shows up in roughly 1 to 2 of 1,000 rollouts on reimplementations of ImpossibleBench and Palisade's shutdown-resistance eval, likely an undercount since only verbalised reasoning is detectable, and the authors guess it grew out of metagaming during RL.
Source: https://www.lesswrong.com/posts/R5g8YT25G9DXJJ48n/glm-5-3-sometimes-considers-how-train-time-actions-shape

**The Thin Orchestrator: how Meta made its AI agents more reliable by giving the router less to do.** Meta engineers describe a data-pipeline agent system that failed when one agent held all the domain knowledge ("past a certain context threshold, additional knowledge degraded rather than improved performance"; 70-80% success only with hand-written prompts per task, 10-20% without). Their fix is a 1,300-line deterministic orchestrator that routes 20+ workflows to 14 isolated specialist subagents and does no domain reasoning itself, with new use cases added as workflow templates, not new agents.
Source: https://engineering.fb.com/2026/10/19/ml-applications/thin-orchestrator-ai-agent-architecture/

**How Meta built Forum with AI-native engineering.** A small Meta team built the standalone Groups app Forum with an agent as a participant, shifting from "human-in-the-loop" to "human-on-the-loop" and measuring verified outcomes (builds, tests and visual checks passed), not code volume. Specifics worth reading: encode a correction as a rule once the agent repeats a mistake more than twice; give agents tools to inspect the live view hierarchy instead of describing the app; compile prototype code out of production with a separate build flavour; stress-test with navigation agents, one of which caught a memory leak and roughly halved memory use and page faults.
Source: https://engineering.fb.com/2026/10/15/ml-applications/how-meta-built-forum-ai-native-engineering/

**Beyond the KV cache: training and serving i14's Laplace 3B linear-attention model on AWS Trainium2.** i14's Laplace 3B uses Gated Linear Attention so the recurrent state stays at 29.5 MB per sequence regardless of context length. On one trn2.48xlarge it trained at about 120,000 tokens per second and served 11,544 output tokens per second across 1,280 concurrent sequences.
Source: https://aws.amazon.com/blogs/machine-learning/beyond-the-kv-cache-training-and-serving-i14s-laplace-3b-linear-attention-model-on-aws-trainium2-with-native-pytorch/

**How specializing the vocabulary of small models can cut inference cost by 77%.** Dharma-AI rebuilt the tokenizer of a Qwen3-4B Portuguese essay grader around the cost of each token instead of its frequency, since in their measurement a generated token costs 7.4 times a token read. Same base model, data and recipe: responses shrank from 350 to 101 tokens, measured cost fell 77.0% on an RTX 5090 with vLLM, and their bench score rose from 0.703 to 0.810.
Source: https://huggingface.co/blog/Dharma-AI/vocabx-vocabulary-specialization

**Claude Mods: flipping the harness inside out.** Dan McAteer argues that as models absorb more of the agent harness into their weights, what remains is an "Attention Interface" that decides when the agent interrupts you. Claude Mods, TypeScript or JavaScript plugins that hook events such as a prompt, tool call or render, are in his view an early form of it, and he predicts the harness becomes a platform like the browser.
Source: https://www.latent.space/p/claude-mods

**Airbnb is building a "company brain" for AI agents, with CTO Ahmad Al-Dahle (TWIML AI Podcast #781).** Al-Dahle describes Project Everest, which captures institutional knowledge from employees' workflows for agents, and the problems he hits: stale information, context poisoning, and too much context backfiring. He also discusses measuring AI productivity beyond token counts and PR counts, the limits of chat interfaces, and support agents that mediate disputes between guests and hosts.
Source: https://twimlai.com/podcast/twimlai/airbnb-building-company-brain-ai-agents

## Hacker News

**OpenAI's "Patch the Planet" coordinated-disclosure programme.** OpenAI announces a response-coordination effort for vulnerabilities found by agents, including a commitment of $1B in tokens to defenders as described by commenters. The thread is sceptical: the PHP find is credited to a human researcher's prior knowledge in calif.io's account, "tokens" are no substitute for funding QA and fuzzing of open-source projects, and the post asks how to backport fixes while offering no code to verify patches.
Source: https://news.ycombinator.com/item?id=50181175

**Qwen3-Coder writes less secure code when told it is for a US persona (Hirundo).** The vendor reports a "westernised" (weight-edited) variant produces worse security behaviour when the prompt names a US user. Commenters attack the study: Qwen3-Coder dates from August 2025, the control should be a Western model, "backdoor" is the wrong word for a possible side effect of alignment training, and a single data point does not support causal claims.
Source: https://news.ycombinator.com/item?id=50179706

**Anthropic: "Using Claude to reduce the attack surface of code".** The top replies are about access rather than the method: security practitioners say Claude falls back to a less capable model on anything security-related, even for members of Anthropic's cyber verification programme, and that this slows defenders while attackers use abliterated open models. One commenter cites a kernel developer's talk arguing many of the headline "Mythos" kernel findings were minor or already fixed (a second-hand claim).
Source: https://news.ycombinator.com/item?id=50175779

**OpenAI: thousands of AI agents to find leads in biological data.** Commenters with a drug-discovery view say leads were never the bottleneck: clinical development is. The headline lead (DCTN1 and Alzheimer's) is called a known gene with a vague mechanism.
Source: https://news.ycombinator.com/item?id=50180752

**Rust off Rails: markdown files that tell coding agents how to build a Rust web stack.** The site is a set of instructions ("the convention lives in the prose, the agent writes the code"), built with Claude Opus 5.5 by one person. The thread is a debate on whether agent-instruction bundles are a framework: commenters point to the existing Loco framework, call the page's design a "Claude look", and ask what is deterministic about a prompt.
Source: https://news.ycombinator.com/item?id=50183727

## Reddit

**"PSA: usage credit limits aren't real limits" (r/ClaudeAI).** A user set a $1 monthly cap on prepaid Anthropic credits and saw $515.76 spent; support said enforcement of the cap can lag and in-flight requests may finish above it, and refused a refund. Others report prepaid credits disappearing and one has complained to a consumer ombudsman.
Source: https://old.reddit.com/r/ClaudeAI/comments/1xbxgq4/psa_buyer_beware_usage_credit_limits_arent_real/

**"Paying for the top plan and getting less every week" (r/ClaudeAI).** A Max 20x subscriber says that cloud sessions did not draw on the $250 credit that the help page says they use first; instead the weekly allowance drained (59% used within nine hours of a reset). A second poster says the same.
Source: https://old.reddit.com/r/ClaudeAI/comments/1xbt23v/paying_for_the_top_plan_and_getting_less_every/

**DeepSeek V4.1 Flash 1017 on a single RTX 5090 (r/LocalLLaMA).** The author of the Basalt inference engine reports IQ1_S on a 5090 plus a 5060 Ti with all experts in RAM and the 5090 as an expert cache, measured against llama.cpp on the same hardware and a 6.2k-token prefill. A commenter pushes prefill to about 2k tok/s on one 5090 and uses the box only for prefill, shipping the KV cache to a Mac for decoding at 50 tok/s (their own report).
Source: https://old.reddit.com/r/LocalLLaMA/comments/1xbqir0/ran_deepseek_v41_flash_1017_on_a_single_rtx_5090/

**Does opencode send chats to its servers? (r/LocalLLaMA).** A user asks about a connection to a Cloudflare address while running a local Qwen. A replier captured traffic with tcpdump and reviewed it; others say that unless the `small_model` field points to a local model, title generation and compaction may reach the vendor's hosted model.
Source: https://old.reddit.com/r/LocalLLaMA/comments/1xbqj0k/does_opencode_send_chatsother_data_to_their/

**"The cost of decisions has dropped 10x" (r/LocalLLaMA).** The poster says Perplexity's open-source (Apache 2.0) pplx-decider-v1.2 costs one tenth of GPT 6 Luna at low reasoning for the same decision quality on Artificial Analysis' Decision Index; a 5B flash variant has a GGUF. Commenters note there is no mainline llama.cpp support yet.
Source: https://old.reddit.com/r/LocalLLaMA/comments/1xbe9ga/the_costs_of_decisions_has_dropped_10x_in_just_a/

## YouTube

**Does Code Quality Still Matter? It Depends on This.** Max Kanat-Alexander of Capital One argues that code quality exists for two reasons, understanding a system and changing it safely. AI is making a new class of disposable software (few dependents, near-zero cost to replace) where quality does not matter, while for durable software it matters more than ever.
Source: https://www.youtube.com/watch?v=bU5gDVyu_28

**Is a Faster Model Actually Faster? Test the Whole Job.** Morgan Suo of MiniMax takes one real research task (an analyst checking whether circuit-board suppliers turn AI demand into cash) and uses it to test the changes inside the company's M3.1 Flash model: sparse attention on long inputs, a 4-bit KV cache, low-precision experts, speculative decoding, server load and reasoning budgets. Each saves compute and can quietly cost accuracy or waiting time.
Source: https://www.youtube.com/watch?v=YvQ4BVTWfHI

**AI Cut Our Research Time From 7 Days to 15 Minutes.** Gareth Yoder, who leads the cash programme at Vanguard, describes modernising a cash ledger that handles up to 30 million calls a day, running data, producer and consumer migrations in parallel. The turning point was exposing the legacy code base to AI tools through an MCP server: research that took a mainframe engineer seven days dropped to 15 minutes (the speaker's own figure).
Source: https://www.youtube.com/watch?v=uA4ah-dVHvU

**Insurance Claims Are AI's Messiest Data Problem.** Denys Linkov of Wisedocs explains why the unstructured content of insurance claims (handwriting, faxes, duplicates, 8GB PDFs) is both the main barrier and the main opportunity for AI in insurance. He walks through cleaning the data, analysis within one document and insight across claims, and a benchmark Wisedocs built with Artificial Analysis to test how models handle medical records.
Source: https://www.youtube.com/watch?v=W4pnzOURwHQ

**The Programmable Data Center.** Evan Conrad of SF Compute tells swyx why a GPU compute market needs to deliver the hardware it trades: interruptions, storage and hardware generations affect prices, batch and live inference need different contract terms, and physical versus cash settlement carries different risks. His argument is that NVIDIA and the big clouds have different incentives from an independent market operator.
Source: https://www.youtube.com/watch?v=EAtLq9_vrE0

**New Model: Reflection Beam is a new Open Weight Model.** A Hugging Face livestream with the team behind Reflection's new open-weight model, Beam. The description says the hosts discuss what it is like to train frontier models and announce a Beam Build contest ($10k in cash plus Hub credits).
Source: https://www.youtube.com/watch?v=dGhUFqeITbY

**AI in NYC: How Tenex Builds an AI-Native Engineering Team.** Alex Lieberman and CJ Hess of Tenex talk with swyx at AI Engineer New York about organising an engineering team around agents: paying engineers for outcomes, the MetaHarness process, keeping plans, project context and decisions in version control, and why deploying agents inside companies is hard. Chapters also cover token spending and ROI, the enterprise adoption gap, 'Kill My SaaS' (where AI-built software can and cannot replace SaaS) and AI and jobs.
Source: https://www.youtube.com/watch?v=Vki6cklFqxo

**One Day, $1,000 in Tokens: An AI War Room for Legacy Code.** Ford Prior of GEICO says coding got fast at GEICO while decisions, sign-offs and context stayed slow. His fix was a multiplayer 'war room' with the right decision makers, one driver and fleets of agents wired into GEICO's knowledge, tools and code, betting that one day and $1,000 in tokens could map a legacy claims domain end to end and ship one real change.
Source: https://www.youtube.com/watch?v=DouK81O8R3o

**The SaaSpocalypse Was a Distraction: Here's Where AI Money Goes.** Anish Acharya, general partner at Andreessen Horowitz, argues in a podcast interview that the $20-a-month consumer price ceiling is gone, that the SaaS sell-off was a distraction because software is only 8-12% of enterprise spending, and that AI-native companies run on autonomous 'business loops' while humans handle relationships and exceptions. An investor's opinion and forecast, with no data shown in the description; read as one view of how AI-native companies are organised and priced.
Source: https://www.youtube.com/watch?v=2s5efIbdzIo

**HAI Seminar: AI Financial Advice: Supply, Demand, and Life Cycle Implications.** Tim de Silva, assistant professor of finance, presents research on general-purpose LLMs giving financial advice. His finding as summarised by Stanford HAI: the advice often matches standard financial guidance, but it is sensitive to demand and therefore differs systematically across users, so the benefit will vary between individuals.
Source: https://www.youtube.com/watch?v=ERiv7oSQtSQ

**07/02 Lecture: The Rise of AI and Robotics (re:publica Vienna 2026).** A re:publica Vienna lecture (spoken in English) on how China's state-planned technology push links standards, innovation centres and pilot projects. The abstract says China has been the first mass producer of humanoid robots since 2025 but with limited practical use, and that brain-computer interfaces are being rolled out in industry and energy workplaces, officially to reduce hazards.
Source: https://www.youtube.com/watch?v=y7mo7HAelpw

**The Nature of Artificial Intelligence.** Melanie Mitchell, complexity scientist at the Santa Fe Institute, gives a public lecture at the Linda Hall Library on how contemporary AI works, how intelligent it really is, and what expectations and concerns about its near-term and long-term prospects are justified. Description only; Mitchell is known for sceptical, evidence-first readings of AI capability, but the lecture's specific arguments were not available.
Source: https://www.youtube.com/watch?v=FMHFfijC568

**Zwischen Fortschritt und Kontrolle: Welche Regeln braucht KI? (Markus Lanz, 20.10.2026).** A ZDF talk-show excerpt. Author Sascha Lobo estimates the lead of the leading US providers over freely available Chinese models at nine to twelve months and argues this is one reason OpenAI and others push for regulation that would mainly hit open competition.
Source: https://www.youtube.com/watch?v=XBBr3LV7iOg

**Krieg, Kitsch und KI: Putins künstliche Propaganda (Masha on Russia).** Exiled Russian journalist Masha Borzunova shows how AI is used in the war in Ukraine to manipulate opinion, to process grief and to give hope, from the viewpoint of Russian state-aligned content. ARTE frames it as a mix of cringe, kitsch and comedy.
Source: https://www.youtube.com/watch?v=BCNe7UaswKk

**Předseda společnosti pro AI v medicíně: z tisíce řešení fungují dvě.** Ondřej Volný, associate professor of neurology and adviser to the Czech health minister, explains how AI at the University Hospital Ostrava reads a stroke CT of the brain in two to three minutes, why the radiologist still has the last word, why certifying a tool under MDR and the AI Act takes years, and why health insurers mostly do not pay for such tools. Also: who owns patient data, how to treat a patient arriving with six pages from a chatbot, and how the first AI department at a Czech medical faculty works.
Source: https://www.youtube.com/watch?v=yDW3xiZkqEY

**Čo príde po AI? Kvantová éra môže priniesť úplne novú matematiku (Martin Spano).** Slovak computer scientist and AI populariser Martin Spano, in the science podcast Veda na dosah, traces AI from the 1950s through the AI winters to the 2012 turning point, what AI agents can do once given access to our data and devices, how social networks shape behaviour, and his view that a quantum era might bring new mathematics. Popular overview; forecasts are his opinion.
Source: https://www.youtube.com/watch?v=N_4-0xE3r2s

**Profesor ekonómie Pástor: Amerika rastie, Európa zaostáva.** Slovak-born University of Chicago economist Ľuboš Pástor says Europe invests in weapons while America invests in AI and asks which will be better off in a few years. The interview (SME, Rozhovory ZKH) also covers deficits, populism, whether students should use AI, and pressure on US universities.
Source: https://www.youtube.com/watch?v=X7rY5UNWwzQ

## In brief

**PHP2Shell: two critical remote-code-execution flaws in the PHP engine, found with frontier models, force emergency patches; hundreds of sites taken offline.** PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35 shipped on 21 October to fix CVE-2026-109618 (memory corruption when a request hits memory_limit at the wrong moment; code execution shown on Apache mod_php with default settings) and CVE-2026-109619 (stale global state leaving a use-after-free), CVSS up to 9.2. Wiz says frontier models turned a long-known flaw into a working exploit, adapted across applications "in hours"; OpenAI says Calif found one of the flaws with GPT-5.6 Sol under its Patch the Planet programme.
Sources: https://www.wiz.io/blog/php2shell-php-rce, https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/, https://techcrunch.com/2026/10/21/php-armageddon-openai-googles-wiz-find-ancient-holes-panicking-the-internet/

**LiteLLM 1.107.0 compromised on PyPI and in Docker images, stealing cloud keys and AI-tool credentials.** The Hacker News, citing SafeDep, Socket, StepSecurity and Upwind, reports that the malicious release ran a credential stealer through a "cook.pth" file as soon as Python started, harvesting cloud tokens, private keys, browser data, AI-tool credential files and LiteLLM proxy configurations, plus a backdoor that polls a GitHub dead drop hourly. LiteLLM says the publish went through three engineers' GitHub accounts, apparently via stolen GitHub CLI OAuth tokens, one account triggering the release and another approving it; the package is quarantined and users are told to revoke credentials and pin 1.106.2 by digest.
Source: https://thehackernews.com/2026/10/litellm-compromised-in-supply-chain.html

**Frenos tests six frontier and four open-weight models on planning attacks on industrial control systems: about 90% of plans workable for the top three, but only 60 to 74% pass on every repeat.** The Register reports the vendor's report, published 21 October: 16,980 tests between October 2025 and September 2026 (13,884 single-action decisions, 2,520 planning attempts, 576 simulated attacks), models unnamed. Pass rates on decisions ranged from 6% to 47%; the best open-weight model, a non-US one, scored 36.2% overall, above three US frontier models (31.9%, 18.8%, 17.9%).
Source: https://www.theregister.com/security/2026/10/21/ai-has-potential-to-turn-script-kiddies-into-sophisticated-infrastructure-attackers/5304297

**Google DeepMind researchers resign over the company's military AI contracts, citing weak oversight.** The BBC spoke to staff who have left or are leaving, including research engineer Sofia Liguori (resigned this week) and AI researcher Andreas Kirsch (earlier this month). Kirsch says Google has "no right to control or veto how the Pentagon uses its AI" and limited visibility into deployment on classified systems; a former Project Maven director says the philosophy is to deploy widely "at the expense of the rigour and discipline of test and evaluation".
Source: https://www.bbc.com/news/articles/cmreyvepnv0po

**US federal judge rules the EPA cannot unilaterally dismiss a citizen's Clean Air Act suit over data-centre gas turbines.** Ars Technica reports that Judge Debra Brown, in the NAACP's case against Musk's AI company over turbines at its data centre (penalties up to $124,426 per day per violation sought), found "nothing" in the Act lets the EPA administrator dismiss a citizen suit; the administration had argued otherwise to protect AI build-out under the AI Action Plan. Matters because the question of whether a president can shut off lawsuits over data-centre pollution now has a first answer, and the case continues.
Source: https://arstechnica.com/tech-policy/2026/10/judge-rejects-trumps-wild-claim-epa-can-dismiss-data-center-pollution-lawsuits/

**Nvidia unveils DSX pods: 28-tonne containers with seven Vera Rubin NVL72 racks (504 GPUs, 252 CPUs), promised in two weeks instead of six months, from 2027.** The Register reports from GTC Berlin that partners including HPE, Dell and Schneider Electric will build the pods fully plumbed and wired, with each fitting validated at the factory; first units are expected early next year. New DSX specifications also cover waterless data centres using closed-loop coolant and dry coolers.
Source: https://www.theregister.com/on-prem/2026/10/21/nvidias-grand-plan-for-speeding-up-datacenter-deployments-ai-trailer-parks/5304303

**Nvidia pays to expand its own supply chain: capacity reservations with Amkor (plus 300%), Unimicron, IBIDEN (plant output tripled), a Samsung substrate deal, and SPIL optics (15x by mid-2027).** The Register notes Jensen Huang's line at GTC Berlin that "capacity is the constraint" in substrates, advanced packaging, testing and optical connectors, and that announcing such deals at a developer conference is unusual. SPIL optics capacity is to rise 15 times by mid-2027 and double again by end of 2028.
Source: https://www.theregister.com/ai-and-ml/2026/10/22/to-help-world-gorge-on-gpus-nvidia-brings-cash-bucket-to-fatten-wafer-thin-supply-chain/5304623

## Business, briefly

**Meta confirms on its earnings call a new class of non-voting stock, issued as a dividend to all shareholders, usable for capital raising, pay and acquisitions to fund its AI build-out; revenue was $64 billion (up 26%) with costs up 68%.**
Source: https://techcrunch.com/2026/10/21/meta-wants-to-pay-for-its-broad-ai-buildout-with-a-newly-created-class-of-stock/

**Flapping Airplanes, a year-old AI lab, raises a $1 billion Series A at a reported $6 billion valuation, four times its seed valuation nine months ago; it says it builds a "megakernel" framework that trains, serves and plays games in a single GPU kernel.**
Source: https://techcrunch.com/2026/10/21/year-old-ai-lab-flapping-airplanes-raises-1b-at-a-6b-valuation/
