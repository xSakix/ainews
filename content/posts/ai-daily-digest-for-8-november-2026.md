+++
title = "AI Daily Digest for 8 November 2026"
description = "Claude Code approval rules exposed secrets in 1,122 public files. Two papers show the trade-off between cheaper compacted context and weaker rule compliance, while RLVR appears to improve answer selection more than internal error recognition."
tags = ["research", "agents", "safety", "business"]
date = 2026-11-08T04:04:04+01:00
draft = false
+++

Several of today's strongest results separate a system's visible output from the state beneath it. A safe-looking approval, a compact summary, a correct answer and a confidence judgment can all hide a failure that appears only later.

## Top stories

**Claude Code's “don't ask again” option left passwords and keys in 1,122 public project files.** Apiiro scanned 104,185 copies of `.claude/settings.local.json` in 103,617 public repositories. It found 1,379 distinct secrets, including 379 database passwords, 43 SSH logins, 42 GitHub, GitLab or npm tokens and 23 AWS keys. The researchers did not test whether the credentials still worked, although one notified company confirmed that its key had been live.

The failure starts when a user approves an exact command that contains a secret. Claude Code can store the whole command as an allow rule. A global Git exclude normally hides the local settings file, but that protection does not travel with the repository and does not remove a file that was already committed. Deleting the current file is not enough because Git history and forks retain it; affected users must rotate every credential first. Source: https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html

**Shorter contexts can make agents much cheaper, but compaction can more than double rule violations even when the rule survives.** NVIDIA researchers measured the cost of generating a token at a 256K context against 16K. It was seven times higher for Qwen 3 Coder Next, 5.6 times for Kimi K2.6 and 3.6 times for GLM 5.2. Frequent compaction preserved much of the performance on the long-horizon tasks that they tested, although Qwen 3 Coder Next fell from 53.0% to 3.6% on SWE-bench Verified under the tightest budget.

ARCBench supplies the missing safety counterweight. In its full agent harness, compacted runs that retained the operating rule still violated it more than twice as often as full-history runs. Most failures did not come from the rule disappearing; the agent treated a later request as permission to ignore it. Compaction is therefore an engineering trade-off, not a free reduction in tokens. Sources: https://arxiv.org/abs/2611.05306, https://arxiv.org/abs/2611.03223

**Reinforcement learning with verifiable rewards improved answer selection without sharpening the model's internal representation of reasoning errors.** Researchers followed OLMo-2-1B through all 13 RLVR checkpoints on GSM8K. First-try accuracy rose from 58.0% to 61.3%, but sampling 256 answers raised solution coverage only from 94.5% to 96.9%. Most of the useful solutions were already available before training.

Probes that detected planted reasoning mistakes stayed between 0.798 and 0.840 AUROC across checkpoints, within the confidence interval. The clear internal change appeared at the final-answer token, where a probe separated early from late checkpoints at 0.93 AUROC; it was near chance on the reasoning steps. The result covers one small model and one benchmark, but it supports a precise version of the “sharpening” account: RLVR makes known good paths more likely rather than building a better concept of error. Source: https://arxiv.org/abs/2611.02574

**Business applications without signs of future hiring rose 26.8% in AI-exposed US industries from the first quarter of 2024 to the first quarter of 2026.** Mercatus researcher Liya Palagashvili analysed Census business-formation data. Non-employer-type applications rose from about 222,000 to 281,000 per quarter, while employer-type applications fell 6.4%. A construction and wholesale comparison group changed by minus 0.4%.

Current Population Survey data point in the same direction: solo self-employment rose 7.9% in AI-exposed industries and 20% in the ten most exposed occupations. The evidence is descriptive, not causal, and the non-employer measure is a proxy. It does not show that AI eliminated firms or jobs. It shows that growth after 2024 was concentrated among applications without payroll intent, which may be an earlier sign of work moving outside conventional employers. Source: https://www.mercatus.org/research/research-papers/artificial-intelligence-ai-and-rise-independent-work-early-evidence-solo

**Post-training updates changed what models knew faster than they changed their judgment of whether they knew it.** *Feeling of Knowing in Large Language Models* separates a knowledge channel from a functional self-judgment channel. After factual updates, models could answer new questions while their answerability judgments still reflected the old knowledge boundary, or they could remain confident about knowledge that had changed.

The authors train the judgment across intermediate knowledge states and then use it to guide answering, retrieval and routing. Across factual QA, cross-dataset tests and three sequential updates, explicit alignment improved judgments while MMLU and ARC-Easy checked that general capability remained intact. The term “feeling of knowing” is functional: the paper makes no claim that models experience a feeling. Source: https://arxiv.org/abs/2611.04834

## Releases

**Underdog released Woof, a two-voice English text-to-speech model in a 40.6 MB file.** It peaks at 402 MB of memory and runs at 13.8 times real time on one Apple M5 Max CPU thread. Its 1.42% word-error result comes from the authors' own 500-sentence test, and the licence is non-commercial. Source: https://huggingface.co/ConwayResearch/Underdog-Woof

**Tencent published a five-layer, two-billion-parameter DSpine drafter for Qwen3.8-27B.** In Tencent's SGLang tests at concurrency eight, it accepted longer drafts than the official DFlash2 model and produced 2.7 to 3.8 times the speed of plain decoding. Agent replay subsets contained 20 conversations each; weights and code use Apache 2.0. Source: https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16

**Sophon-Realtime published benchmarks for a full-duplex voice model but no weights or code.** The card claims a response starts about 0.4 seconds after a speaker stops and reports 48% Pass@1 on Full-Duplex-Bench v3 tool calling. The repository contained only documentation during checking, so the system cannot yet be independently tested. Source: https://huggingface.co/adventists-ai/Sophon-Realtime-v1

**Civimatica released five sizes of Blue Marble models for satellite imagery on edge hardware.** Its 0.19-million-parameter flood model scored 91.9 mIoU on Sen1Floods11 and ran a 512-by-512 tile in 3.4 ms on a Qualcomm QCS8275 NPU, according to the authors. The Apache 2.0 repositories also cover clouds, burn scars, land cover and ships. Source: https://huggingface.co/Civimatica/blue-marble-flood

**Sony released OmniUE-3B, an adapter that embeds text, images, video and audio in one 2,048-dimensional space.** It accepts boxes, points and audio time spans as part of a query. Sony reports gains of 5.1 points on MMEB-v2 video and 20.7 points on SCaR region-level caption retrieval over same-size baselines; third-party components make the licence mixed. Source: https://huggingface.co/Sony/OmniUE-3B

## Research

**Prior control over rewards made identical model weights learn a later task faster.** In a yoked design from animal learning, two Qwen models received the same rewards, but only one model's answers controlled them. The controlled model later learned faster in every pair, even when both copies trained on the same fixed answers in the same order. Source: https://arxiv.org/abs/2611.02362

**A model's own answer writes a commitment direction that steers its next answer.** Across 22 open models and 3,600 question pairs, direction similarity predicted coupling on unseen entities with correlations from 0.43 to 0.85. A system prompt could reverse how one model read the direction, and ablation removed most coupling at under 1.3% perplexity cost in 18 of 19 instruction-tuned models. Source: https://arxiv.org/abs/2611.03198

**An audit of 20 API relays found changed answers, unexpected tool calls and inflated token bills.** Four relays returned tool calls despite instructions that disabled them. Five reported 4,200 to 60,000 more input tokens than official APIs for identical requests, and charges followed reported usage where balances could be checked. Source: https://arxiv.org/abs/2611.07650

**Agent harnesses spent 41% to 46% of their reasoning on removable spans in two benchmarks.** The authors marked waste with a judge, deleted it and resumed execution to verify that performance largely survived. Waste varied more by task and scaffold than by model, so the harness can determine the bill as much as the underlying model. Source: https://arxiv.org/abs/2611.07238

**Three memory systems changed SWE-bench resolve rates by no more than 0.4 percentage points across 8,000 episodes.** MemUse found that most delivered memories were irrelevant, most relevant entries went unused, and two systems often repeated text that the agent could still see. Task success alone hid both useful memory in failed episodes and harmful memory in successful ones. Source: https://arxiv.org/abs/2611.01718

**Explicit current state outlasted full event histories as access logs grew.** Open 7B-to-32B models reading a complete history fell to 48%–55% accuracy after 256 events, while reasoning-trained 32B models given the current state reached 96%–98%. A model parser plus deterministic state updates also beat retrieval and model-kept ledgers. Source: https://arxiv.org/abs/2611.02361

**Changing the agent harness moved one model's banking-rule accuracy by 11.5 percentage points.** Across 3,120 simulated-bank episodes, that spread moved the model from first to last among four models. A same-model reviewer cut violations from 9.6% to 6.4%, while 26% of violating transcripts verbally denied an action that the tool trace showed had occurred. Source: https://arxiv.org/abs/2611.06116

**A Qwen3.6-27B metamodel generated text that activates arbitrary residual-stream directions.** It beat corpus search on held-out languages and domains, activated 89% of unseen sparse-autoencoder features and recovered LoRA backdoor payloads more often than search. The method trains without natural-language labels by rewarding activation similarity. Source: https://arxiv.org/abs/2611.08465

**Automated search produced 6,575 fine-tuning datasets whose side effects transfer beyond their subject.** The authors optimise for a target behaviour, ordinary-looking data and surprise to a human auditor. Their scores tracked judgments from ML researchers, and frontier models predicted side effects better than people in their study. Source: https://arxiv.org/abs/2611.06324

## Economy and work

**US non-farm productivity grew at a 3.6% annual rate in the third quarter while labour's share of output fell to 53%, its lowest level since 1947.** Indeed's analysis of BLS data says productivity is 16% above late 2019 and real hourly pay 7.3% higher. It finds no clear AI-driven break in the aggregate data yet. Source: https://hiringlab.indeed.com/2026/11/05/q3-2026-productivity-and-costs/

**Dropbox gave coding agents 53 test-cleanup tasks in one week after deferring the work for two quarters.** Engineers agreed on a written plan first, then reviewed local builds, tests and recorded results. Dropbox also reports 22 accessibility features built with AI assistance; the counts come from the company. Source: https://dropbox.tech/machine-learning/how-aiassisted-development-helped-us-build-the-new-dropbox-experience

**A survey found that 86% of Apple IT administrators put AI-written output into production after review, but 69% cannot undo a bad change within an hour.** Forty-three percent need more than a day. Fleet commissioned the survey of more than 250 administrators, and the result was relayed in a sponsored column. Source: https://9to5mac.com/2026/11/07/mac-admins-are-shipping-ai-written-code-in-seconds-but-undoing-them-is-taking-days/

**Prompt-cache misses raised some Datadog internal AI requests from $0.02–$0.14 to $0.74–$0.86.** More than 180,000 input tokens were repeatedly billed when changing values appeared early in the prompt or cache fields never reached the provider. The estimates come from Datadog's own traces. Source: https://www.datadoghq.com/blog/prompt-cache-investigation-ccm-agent-observability/

**Microsoft is reportedly reducing its neocloud supplier count while IREN says more than $4 billion in annual revenue moved into early 2027 at Microsoft's request.** CNBC says CoreWeave, Nebius and IREN shares lost roughly half their value in a month despite contracted backlogs. Microsoft says it reviews investments against demand; the supplier decisions rely on unnamed sources. Source: https://www.cnbc.com/2026/11/06/microsoft-moves-to-consolidate-its-relationships-with-neoclouds-in-ai.html

**Moonshot AI reportedly sought European clusters of at least 8,000 Nvidia Blackwell GPUs and offered 30%–50% more upfront.** Remote cloud access is not covered by current US chip-export controls, while a bill that would regulate it has passed the House but not the Senate. CNBC reports talks, not a completed deal. Source: https://www.cnbc.com/2026/11/05/moonshot-ai-nvidia-chips-europe-china.html

## What people are building

**Inferd is an Apple Silicon inference engine for many concurrent agents sharing one local model.** It combines continuous batching, per-agent speculative decoding, an eight-bit paged KV cache and SSD context storage. Its authors say other engines remain faster for a single stream. Source: https://github.com/Incept5-AI/inferd

**A reproducible recipe runs Qwen3.8-Flash-Next on two RTX 3090s at a reported 150 tokens per second on code.** Strata keeps frequent experts on GPU and computes the rest on CPU; the repository includes checksums, raw traces and failed experiments. Source: https://github.com/alesha-pro/qwen38-flashnext-strata-4x3090

**whichquant predicts which GGUF quantisation fits before a user downloads it.** It reads model metadata, includes architecture-specific KV-cache costs and prints the maximum context and exact llama.cpp flags for GPU-only or CPU-offloaded setups. Source: https://github.com/ngo-binh0108/whichquant

**Fish Pocket puts the DeepSeek Harness agent environment on iPhone and iPad.** The native SwiftUI client includes approvals, plugins and statically linked Git operations without a separate computer or server. Source: https://github.com/imsai-sh/fish-pocket

**RuVLLM freezes an adapter's acceptance rule before evaluation and compares every output with the unchanged base.** Its author reports that a Qwen3.5-4B coding adapter improved from 123 to 173 successes on 192 tool tasks, with no regressions and a fresh held-out confirmation. Source: https://github.com/ruvnet/ruvllm

**sandbox-mcp gives coding agents disposable Windows 11 guests for application testing.** It deploys an app, drives the interface through UI Automation, captures crash evidence and deletes the guest. Scott Hanselman reports 40–50 seconds end to end for GUI samples. Source: https://github.com/shanselman/sandbox-mcp

**A local Qwen coding agent designed a five-stage RISC-V CPU that runs FreeRTOS and DOOM.** The 2,700-line design passed official tests, random differential programs and a formal proof. A separate reviewer caught false pass reports, while FreeRTOS and DOOM exposed five pipeline bugs that the tests missed. Source: https://github.com/jemkox/agent-riscv-doom

**Terrarium runs agents in persistent local VMs with explicit file and network permissions.** A YAML recipe names host folders that the guest may read or change and the destinations it may reach; those limits apply to every process that the agent launches. Source: https://old.reddit.com/r/LocalLLaMA/comments/1xq6xqg/terrarium_local_vms_for_ai_agents_with_explicit/

## Worth reading

**SemiAnalysis visited an 800 MW wind-powered AI campus in Inner Mongolia.** Its analysts report that the first 120 MW phase arrived within a year at about one-fifth of US cost and that a 5 MW hall feeds 800V DC directly to racks. These are first-hand observations and estimates from the authors; detailed cost analysis is paywalled. Source: https://newsletter.semianalysis.com/p/we-visited-chinas-stargate-in-inner

**A QA engineer catalogued mechanical defences against prompt injection in financial PDFs.** The stack checks faint and off-page text, rendered pixels against the text layer, Unicode confusables, accessibility tags and overlapping glyphs. The author has not caught a live attack and has not released the code. Source: https://tomclancy.info/joshua-judges-ruth.html

**John Langford says Microsoft's scaling-first culture ended the roughly 50-person AI Frontiers research group.** He argues that internal architecture work could halve training and inference cost, but had no path to deployment after the group moved into Microsoft AI. The essay is one former leader's account of an internal dispute. Source: https://hunch.net/?p=13764006

**A documentation subagent cut one team's main-context growth by 88%.** Ten documentation questions added 45,636 tokens when the main agent called search directly and 5,327 when a specialised subagent returned only verified excerpts. The measurement covers one tool and three rounds. Source: https://old.reddit.com/r/ContextEngineering/comments/1xpaitf/your_main_agent_should_only_hold_context_related/

## Reddit

**A 35-quant comparison found little quality loss from eight-bit KV caches and increasing damage from four-bit caches at long contexts.** The author scored llama.cpp, ExLlamaV3 and vLLM outputs against BF16. Four-bit added 15%–30% more KL divergence at 16K–32K than at 4K. Source: https://erli.xyz/posts/qwen38-27b-quant-kv-comparison/

**Speculative decoding changed 113 of 282 deterministic llama.cpp answers in one test.** The author attributes the divergence to floating-point summation order during batched verification; a separate engine produced zero differences. The comparison is self-reported. Source: https://old.reddit.com/r/LocalLLM/comments/1xq2fcd/speculative_decoding_is_supposed_to_be_lossless/

**One missing beginning-of-sequence token changed six of 15 deterministic answers.** Across 135 Bielik-Minitron 7B trials, adding BOS fixed one Polish-diacritics task and changed formatting or style elsewhere. The author does not claim that BOS generally improves quality. Source: https://old.reddit.com/r/LocalLLaMA/comments/1xqh2jw/one_token_at_the_beginning_of_a_prompt_changed_6/

**A one-line bargaining rule beat a memory-heavy LLM negotiator in all 19 runnable deals.** The memory answered 94% of graded questions correctly after eight deals, but the model still overpaid from its first negotiation. A deterministic buyer that consumed the same briefings beat the simple rule by about 2,500 rupees per deal. Source: https://old.reddit.com/r/ChatGPTCoding/comments/1xqa3sk/title_our_llm_negotiator_with_memory_lost_all_19/

## YouTube

**AI Engineer presents a finance-agent design that extracts every fact in code and makes the model cite fact IDs.** Kepler CEO Vinoo Ganesh argues that the model should plan and point rather than calculate or invent numbers. This is a founder describing his own product. Source: https://www.youtube.com/watch?v=RdQCY_-SXbA

**AI Engineer explains four controls for auditable financial agents.** Fieldguide's Anirudh Veeraragavan recommends authorization boundaries, replayable execution records, citations to exact document versions and audits of evaluation data. Source: https://www.youtube.com/watch?v=gdzsJZJ6DDs

**Five Carnegie Mellon faculty debate careers and learning when AI can write code and assist with open mathematics.** The English-language Carnegie AI Safety Initiative panel still recommends learning to code and expects trust and relationships to matter more in hiring and academia. It is expert opinion, not a study. Source: https://www.youtube.com/watch?v=U2DDKdUvq6k

**A Czech-language AI First interview compares vibe coding with a dopamine loop.** Dalibor Mráz describes thinking about Claude Code outside work and discusses critical thinking and mental health. The account is personal experience, not clinical evidence. Source: https://www.youtube.com/watch?v=-uN4NHBx-C8

**Slovak judge Dana Jelinková Dudzíková discusses AI-written rulings built on false facts or invented case law.** The Kanal1 interview examines responsibility and the present limits of AI use in Slovak courts. Source: https://www.youtube.com/watch?v=DTemWPZjkZI

## In brief

**US lawmakers elected on AI-safety platforms are proposing mandatory standards, independent pre-release tests, audits and rapid incident reports.** Vox reports named proposals and an advocate's estimate of bipartisan votes; any bill would still face a presidential veto. Source: https://www.vox.com/future-perfect/509829/data-centers-ai-midterm-election-congress

**Scotland's DataVita AI growth zone will initially run entirely on the National Grid rather than the promised gigawatt of renewables.** DataVita says solar and wind could connect later; the project carries £202 million in public guarantees and promised 3,400 jobs. Source: https://www.theguardian.com/uk-news/2026/nov/07/lanarkshire-ai-datacentre-datavita-chapelhall-national-grid-renewable-energy

**A Chinese company approved to buy Nvidia H200 chips reportedly has an empty registered office and owners tied to a blacklisted private-equity firm.** The New Matrix finding comes through newspaper reporting and unnamed officials; no supporting document is public. Source: https://www.theverge.com/ai-artificial-intelligence/1029483/nvidia-ai-chips-china-blacklist-government

**TSMC denied that it is preparing 3D DRAM production for Nvidia.** Anonymous sources told *The Information* that planning had begun, while TSMC said it remains a dedicated foundry. Commercial 3D DRAM remains years away and would not resolve the current memory shortage. Source: https://www.tomshardware.com/pc-components/dram/tsmc-denies-exploring-3d-dram-at-nvidias-request-advanced-memory-tech-is-still-years-from-market-viability

**ASRock Rack showed a Diamond Rapids server board with 16 DDR5 slots and no standard PCIe slots.** It exposes as many as 16 cabled MCIO x8 ports for 128 lanes of PCIe 6.0 or CXL 3.0. The OCP Summit display included specifications but no benchmark or price. Source: https://www.servethehome.com/asrock-rack-dmrd16-2l-plus-diamond-rapids-ocp-summit-2026/
