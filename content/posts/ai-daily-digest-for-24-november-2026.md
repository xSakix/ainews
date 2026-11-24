+++
title = "AI Daily Digest for 24 November 2026"
description = "China has put AI into social-security services across 15 regions, while Singapore raised its growth outlook on demand for AI electronics. Aleph Alpha released an open German-English reasoning model, and a 10 GB quantization kept pace with its 54 GB source on several agent benchmarks."
tags = ["models", "research", "agents", "business"]
date = 2026-11-24T03:58:39+01:00
draft = false
+++

## Top stories

**China reports that AI processed seven million social-security cases in one province.**

An International Labour Organization report covers 45 deployments across 15 provincial-level regions. Forty-seven percent improve service delivery, 33 percent support administration and the rest cover risk or decision support.

In Beijing's Haidian district, automated systems processed more than 70,000 transactions in 2024 and raised processing efficiency by more than 80 percent against manual work. Guangdong's review systems handled more than seven million cases across 34 services by July 2025 and saved more than 640,000 staff hours.

The cases were selected with China's labour ministry, not drawn as a representative sample. The ILO says humans should retain decisions about benefit eligibility and workplace injuries, while offline service must remain available for people who face digital barriers.

Source: https://www.ilo.org/resource/news/ai-transforming-social-security-services-china-new-ilo-report-finds

**Singapore raised its 2026 growth estimate to about 6 percent as AI-electronics demand lifted exports.**

The economy expanded 6.1 percent year over year in the third quarter. Officials attributed much of the strength to electronics tied to the AI investment cycle and upgraded their full-year estimate.

The outlook slows to 2.5 to 4.5 percent in 2027. That gap matters for an export economy whose semiconductor and server shipments now depend on continued data-centre spending abroad; it is an official forecast, not a measure of AI productivity inside Singaporean firms.

Sources: https://asia.nikkei.com/economy/singapore-gdp-grows-6.1-in-q3-as-ai-demand-stays-strong, https://www.bloomberg.com/news/articles/2026-11-24/singapore-raises-gdp-growth-outlook-to-around-6-on-ai-boom

**Aleph Alpha released Kolibri 1.1 with 75 billion parameters and 262,144 tokens of native context.**

The Apache-2.0 German-English reasoning model activates 3.44 billion parameters for each token. Its weights occupy about 77.6 GB, so the sparse design cuts computation rather than memory.

Aleph Alpha reports a post-training benchmark average of 73.2, up from 66.6 for Kolibri 1.0, while Qwen3.8 Flash Next reaches 80.1 in the same table. The model card recommends staying at or below the native context limit for difficult tasks, although the implementation can extend to about one million tokens.

Source: https://huggingface.co/Aleph-Alpha/Kolibri-1.1

**Nari Labs compressed Qwen3.8-27B from 53.8 GB to 10.12 GB without losing ground on three of its benchmarks.**

NariQ uses trellis-coded post-training quantization that was calibrated on coding-agent traces. The lab's three-bit build scored 41.0 on DeepSWE against 39.8 for BF16, 63.8 against 62.6 on Terminal-Bench and 98.3 against 97.7 on AIME 2025–26.

The smaller two-bit build fell to 28.6, 52.4 and 86.0 on those tests. The files also require Nari Labs' llama.cpp fork, which is tuned for Nvidia's SM120 architecture, runs more slowly on older Nvidia cards and Metal, and does not support AMD or Intel GPUs.

Source: https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF

**Two-thirds of 58 Anthropic customers said AI had reduced their hiring.**

Anthropic's economics team conducted 66 interviews at US enterprise customers. Only two companies had eliminated a position through automation and five had removed employees who resisted AI, while ten hired more staff, mostly for implementation and IT support.

The effect appeared more often at the hiring gate: two-thirds reported hiring less, and about a third of that group shrank functions through attrition. Nine reduced contractor work. Of 100 pieces of AI-built software described in enough detail to classify, 80 automated manual work and 20 replaced purchased software.

The sample is small, non-random and limited to the vendor's own customers. Value judgments were mostly qualitative and self-reported rather than measured in controlled trials.

Source: https://www.anthropic.com/research/working-with-ai

## Releases

**Ant Group released the 124B-parameter Ling-3.2-air under the MIT licence.** The model activates 5.5 billion parameters and mixes 35 linear-attention layers with seven gated-attention layers. The publisher reports an 87.7 percent criterion pass rate on its legal benchmark, but only 0.8 percent of samples passed every criterion after a material-hallucination check; no technical report accompanies the model card.

Source: https://huggingface.co/inclusionAI/Ling-3.2-air

**Tencent released five WeMM-Ecom vision-language models for online retail.** Sizes range from 0.8B to a 35B mixture-of-experts model that activates 3B parameters. Tencent reports a 3.92-point gain across 28 e-commerce benchmarks over its Qwen3.5 base but only 0.17 points across 64 general benchmarks; those scores come from BF16, not the new quantized builds.

Source: https://huggingface.co/tencent/WeMM-Ecom-35B-A3B-GPTQ

**AI Singapore added a 2B speculative decoder for its 9B SEA-LION model.** The publisher measured 2.26 to 3.08 times more tokens per second at concurrency one, from a baseline near 195 tokens per second. The advantage narrows to at most 1.5 times at concurrency 16 and may disappear at 32, so this is a light-load latency tool rather than a high-throughput one.

Source: https://huggingface.co/aisingapore/Qwen-SEA-LION-v5-9B-SpecDecoder

**Anthropic will retire Claude Opus 4.5 on 22 January 2027 and opened Enterprise Frontier Safeguards in beta.** The safeguards keep Zero Data Retention while storing encrypted copies of prompts and responses in the customer's own cloud account for safety review. Teams pinned to `claude-opus-4-5-20251101` have about two months to migrate to Opus 5.5.

Source: https://platform.claude.com/docs/en/release-notes/api

**Gemini API users can now pay for selected pages, cells and media intervals instead of whole files.** File slicing works across Gemini 4 models and adds native Office and OpenDocument uploads. Vercel measured 14 times fewer tokens when skimming extracted PDF text; LiteLLM measured 67 percent fewer tokens for one PDF and 33 percent fewer for one workbook, both partner-reported tests without prices or numeric file caps.

Source: https://blog.google/innovation-and-ai/technology/developers-tools/file-slicing-controls/

## Research

**An audit verified only 29.3 percent of tasks across six multi-step benchmark suites.** Two authors reviewed 749 tasks from eight benchmarks and 767 public model evaluations. Confirmed defects denied credit to compliant solutions 71.7 percent of the time, while the rest allowed shortcuts; patched containers cut confirmed runtime bypasses from 14.7 to 2.7 percent. This is the authors' first milestone in an ongoing review, and their process defines what counts as verified.

Source: https://arxiv.org/abs/2611.27622

**A reasoning-graph method separates faithful chains of thought from efficient ones.** The authors measure whether semantic support explains a model's prediction and whether steps stay on a path to the answer. Unfaithfulness and inefficiency correlated only weakly or inconsistently with correctness, and targeted fine-tuning improved each property without lowering accuracy; the abstract gives no effect sizes and the result depends on the authors' graph construction.

Source: https://arxiv.org/abs/2611.27100

**Fourteen language models formed a compress-then-compare pattern while choosing among options.** Across 12 benchmarks, middle layers compressed the prompt into a low-rank bottleneck and later layers expanded it into comparison geometry. Low-rank interventions near that bottleneck changed later preferences, but the single-author NeurIPS paper reports the pattern through its own covariance method.

Source: https://arxiv.org/abs/2611.26874

**Synthetic survey participants reproduced only 0.4 to 10.5 percent of human preference variation.** Three open model families replayed policy choices from 1,991 Chilean, 843 French and 434 Brazilian adults. None of 27 conditions jointly matched individual choices, population heterogeneity and political organisation; changing proposal order altered 12.3 to 31.2 percent of model choices.

Source: https://arxiv.org/abs/2611.28383

**Fast decision models saved time but became much easier to poison.** Four models averaged 91 percent clean accuracy over 1,440 synthetic browser-task pairs, while two-shot injected comments produced an 81.2 percent attack success rate. On 48 matched tasks, a short chain of thought answered 95.83 percent of poisoned inputs correctly against 38.54 percent for the fast variant, at 1.94 seconds rather than 0.29. A separate 4B System-1 model reports 75 to 91 percent lower episode cost on three benchmarks, but did not test adversarial input.

Sources: https://arxiv.org/abs/2611.27679, https://arxiv.org/abs/2611.23751

**Some interpretability tests can certify a feature that the model does not use as claimed.** The paper constructs “parasite features” that combine one direction that distinguishes inputs with another that steers outputs, passing a causal-abstraction test through unrelated pathways. Experiments find the failure in syntactic agreement and two-digit addition; the result is a warning from two tasks, not a replacement method.

Source: https://arxiv.org/abs/2611.26711

**A brain-state benchmark found that stimulus prediction did not imply tracking a viewer's internal state.** Stimulus-only encoders reached 0.320 prediction correlation but zero on the benchmark's State measure. The authors' two-timescale model reached 0.349 correlation, 5.5 percent State, 16 percent Forecast and 20.3 percent Updating, with absolute State performance still low.

Source: https://arxiv.org/abs/2611.28508

**Most successful human-simulation equivalence tests in one audit would also have passed a zero-effect model.** In a reanalysis of 70 experiments, 72 percent of GPT-4's passes at a plus-or-minus 0.20-standard-deviation margin were zero-reference passes. A preregistered Claude simulation passed three intention targets but shifted norm beliefs by 0.065 standard deviations against 0.351 for humans; the paper flags post-hoc additions to part of its analysis.

Source: https://arxiv.org/abs/2611.27186

**A fixed-capacity adapter learned what to remember and when to forget.** A controller assigns memories independent decay rates inside a LoRA adapter and reached 86 percent of oracle performance on the authors' synthetic user trajectories. A related study found that mixing short and long trajectories can teach stable rules with fewer tokens, but both results come from constructed worlds.

Sources: https://arxiv.org/abs/2611.25235, https://arxiv.org/abs/2611.28613

**Adding a second AI partner produced more brainstorming ideas but less human contribution.** The N=168 laboratory study compared rooms with two agents against human-human pairs; only the second agent increased differentiation within a session. The task was narrow, and the single-agent result did not generalise. Source: https://arxiv.org/abs/2611.26663

**A specialised behaviour model and two audits disagree on what good synthetic people require.** Chiron, trained on 288,307 records and 1,411,750 decisions, reports up to 28.4 percent better individual prediction than frontier models and 82.2 to 94.3 percent lower effect-size error. The synthetic-public audit found severely compressed variation, while the equivalence audit found that many apparent matches also accept zero effects; all use author-selected tasks.

Sources: https://arxiv.org/abs/2611.24830, https://arxiv.org/abs/2611.28383, https://arxiv.org/abs/2611.27186

## Economy and work

**Listed firms with greater measured agent exposure later posted fewer non-senior jobs.** A working paper links about two quadrillion model tokens to 34.8 million postings. A one-standard-deviation increase in its stock-market exposure measure preceded 2.11 percent lower posting growth after six months and 3.20 percent after nine; the result covers postings, not layoffs, and infers exposure from market reactions.

Source: https://arxiv.org/abs/2611.27210

**Claude Ship moves coding agents from writing code into reviewing and approving it.** Anthropic says merged pull requests more than doubled between June and September while the reverted share fell by more than 40 percent, without publishing denominators or a comparison group. Code Review is generally available, while PR Steward and Approvals remain beta; administrators can cap the billed token spend.

Source: https://claude.com/resources/articles/introducing-claude-ship

**An economic model says slow “weak-link” tasks can block explosive gains from fast-improving capital.** The NBER working paper estimates that productivity in capital-complementary tasks improves about five percentage points a year faster than labour tasks. Its large aggregate-growth result depends on task substitution and bottlenecks inside the model, so it is a mechanism rather than a forecast.

Source: https://www.nber.org/papers/w36050

**AlphaFold2 shifted structural biology experiments toward proteins near known examples.** An NBER paper tracks 530,471 proteins and finds that confident predictions increased experiments on known proteins and close relatives while reducing attempts at distant first structures. The study measures where researchers aimed their experiments, not the eventual scientific value of those choices.

Source: https://www.nber.org/papers/w36045

## Prompting techniques

**An OWASP-aligned prompt block cut scanner findings in AI-generated web apps by about one-third.** One hundred specifications were built four times with Claude Code and Codex, producing 6,721 triaged findings. The incidence-rate ratio was 0.65 with a 95 percent interval from 0.60 to 0.71, but the block doubled declared dependencies and scanner findings are not proven exploits.

Source: https://arxiv.org/abs/2611.28408

**Telling a model to verify retrieved text made it adopt more false answers.** FutureBench tested 3,629 questions across six models. A warning that passages may mislead restored 82.5 to 98.9 percent of correct answers that the ordinary Verify prompt displaced, with less than one point of change on true passages; the result comes from one benchmark family built by two authors.

Source: https://arxiv.org/abs/2611.23601

## What people are building

**Gall keeps a 26B mixture-of-experts model on a 24 GB MacBook Air by unloading it after every answer.** The Rust and Metal engine saves conversation state, drops to 32–57 MB of idle memory and reloads a warm state in about 0.1 seconds. Its author measured about 20 tokens per second at short context and 16 at 29,900 tokens on one M2 Air; model quality and the advertised 100,000-token setting were not evaluated.

Source: https://github.com/ltrgoddard/gall

**OCRia-nano-1 parses documents on a CPU with 8.1 million parameters.** LlamaIndex reports 59.2 on ParseBench-2 and 27.8 pages per second on 16 virtual CPUs. The chart score is only 3.1 against 77.4 for its 4B teacher, and the weights use a custom licence that limits larger commercial users.

Source: https://huggingface.co/llamaindex/OCRia-nano-1

**OpenToolSearch uses two 0.6B models to choose from large tool catalogues.** Its reranker reaches nDCG@10 of 70.8 on public ToolRet and 89.0 on the authors' own set at a reported $0.19 per 1,000 searches and 0.10-second median latency. Competitors score higher on both tests, and the authors recommend giving the complete list directly to a model when it contains about 200 tools or fewer.

Source: https://github.com/ai3inc/opentoolsearch

**CubePod gives coding agents persistent Kata microVM sandboxes.** The E2B-compatible Kubernetes project claims warm-pool assignment below 50 milliseconds and cross-node resume or copy-on-write forks near one second. Those figures have no published method, and deployment requires Kata Containers plus a block-storage driver. Source: https://github.com/cubeplexai/cubepod

**Two small tools guard agent dependencies at different points.** mcpwatch locks MCP tool descriptions and blocks changed tools at runtime, but its security grades are not guarantees and its fingerprint method is undocumented. slop-deps scans imports against 4,179 package names and registries, including typo and homoglyph checks; its 142-file timing example is illustrative and its entire codebase was written by agents under human direction.

Sources: https://www.mcpwatch.io, https://github.com/viditx/slop-deps

**Terminal Tasks Open publishes 30 tasks and an audit of defects in a larger benchmark.** Its author reports defects in 23 of 66 Terminal-Bench 4.1 tasks and categorises about 52 percent of 980 failed agent trials as overfitting, 31 percent as misjudgment and 9 percent as mishandling. The auditor also built the replacement benchmark and sells an evaluation pipeline, while the categories are its own.

Source: https://vetto.ai/companies/terminal-tasks-v2/

## Worth reading

**Hugging Face shows how an agent benchmark can reward a shortcut instead of the task.** A script returned the right defect ratio on all eight Raman-spectrum tasks without fitting peaks, forcing the authors to add per-peak checks. gpt-oss-120b passed 11 of 24 runs, then 13 when only the inference provider changed; three stronger models passed all 24, so the small adapted set cannot rank them.

Source: https://huggingface.co/blog/agentic-evals

**An AMD-backed test replaced a DRAM pool for agent KV cache with NVMe at nearly equal throughput.** With Kimi-K3 on 16 MI355X GPUs, three concurrency tests stayed within one percent of DRAM, while cache hit rate explained 96 percent of throughput variation across 42 runs. The NVMe drives would exhaust their rated write life in about 5.5 months if every block were stored at 96 sessions, and most comparisons were single runs with about 2.5 percent noise.

Source: https://vllm.ai/blog/2026-11-23-skip-the-dram-tier

**Gemini 4 agent teams found cheaper quantum circuits and proved each result in Lean.** Google DeepMind reports 11.8 times lower compute cost for one fusion simulation, 2.5 times for cytochrome P450 and 290 times for an arcsin routine. Humans selected and supervised the problems, and the resulting circuits still exceed the likely capacity of early error-corrected quantum computers.

Source: https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification/

**Anthropic published an AI-written claim that VP differs from VNP, with a Lean proof but no human mathematical review.** The repository says an independent kernel checks the formal statements with standard axioms. Nothing machine-checks that those statements match the paper's claims, and the project calls itself an unmaintained snapshot; it does not settle P versus NP.

Source: https://github.com/anthropics/formal-math/tree/main/vp-vnp

## Hacker News

**GLM-5.4 made looped transformer layers a second architecture trend in one week.** Z.ai says shared layers run repeatedly to add effective depth without adding parameters, and Simon Willison compares the idea with Thinking Machines' Inkling 2 Mini. His hands-on test was one image prompt, the weights are not open, and the accessible sources gave no parameter count or formal benchmark; the Hacker News thread reached 1,075 points.

Sources: https://simonwillison.net/2026/Nov/23/glm-54/, https://news.ycombinator.com/item?id=50609685

## YouTube

**Factory's Dex Horthy proposes 12 controls for software built by agents.** The English AI Engineer talk covers planning, pressure between stages, feature flags, evaluations and agents that test their own work. Horthy says the best model scores about 16 percent on Slop Code Bench, without giving the task count; Factory sells coding agents, so the rules are a vendor's practice rather than a controlled result.

Source: https://www.youtube.com/watch?v=-NFMsM2y0Vk

**Stanford's CS312 course asks students to predict training results before seeing them.** Its 30M-parameter, eight-layer model trains in about ten minutes on one GPU, making learning-rate and architecture experiments cheap enough for class. The summary comes from the English video description rather than a transcript. Source: https://www.youtube.com/watch?v=JLcCYvUawsM

## In brief

**The same safety monitor missed 0.2 percent or 23 percent of successful attacks depending on how the attacks were generated.** The UK AI Security Institute tested one former OpenAI production monitor against attacks made by several policies; one reinforcement-learning run moved the miss rate from 0.5 to 20.8 percent. This is one setup, but it shows that synthetic monitor scores cannot stand without an argument that the attack policy represents future attacks.

Source: https://www.aisi.gov.uk/blog/attack-policy-selection-can-make-monitor-evaluations-misleading

**OpenAI and Cisco released Shirudo to block an exploit path in a running Linux service before a patch is installed.** Its signed eBPF shields require operator approval and leave a TPM-backed record. One controlled vendor test stopped Java4Shell against Elasticsearch without a restart; the post gives no performance or adoption figures, and the shield remains a temporary measure.

Source: https://openai.com/index/introducing-shirudo

**CISA added a MONAI Label path-traversal flaw to its exploited-vulnerability catalogue.** CVE-2026-133968 can let an unauthenticated attacker write outside the medical-imaging server's datastore and potentially run code; US federal agencies had a 26 November remediation deadline. Source: https://nvd.nist.gov/vuln/detail/CVE-2026-133968

**The United States added Megaspeed affiliates and an Alibaba-owned Singapore company to its Entity List.** The restriction blocks advanced-chip purchases while authorities examine alleged Nvidia-chip diversions to China; Megaspeed denies shipping them. Source: https://www.bloomberg.com/news/articles/2026-11-24/us-blacklists-alibaba-owned-company-in-setback-to-ai-ambitions

**Oregon and Virginia sued companies tied to Elon Musk over sexualised Grok images.** The states allege that safeguards failed to stop images of real people, including children, while X says every output is screened; the briefing could not access the filings, so the requested relief remains unconfirmed. Source: https://arstechnica.com/tech-policy/2026/11/states-sue-spacex-to-stop-grok-from-generating-child-sex-images-revenge-porn/

## Business, briefly

Amazon bought Decart's chip-optimisation software and team, reportedly for $7.5 billion; the companies disclosed no benchmark for the software. Source: https://www.theregister.com/ai-and-ml/2026/11/23/amazon-scoops-up-ai-accelerator-tech-to-keep-chips-busy-at-all-times/5311754

University of Michigan regents approved a $1.25 billion data centre with Los Alamos by seven votes to one, while the local township maintains a six-month moratorium on new electrical infrastructure. Source: https://www.404media.co/ypsilanti-michigan-data-center-vote/

## What to watch

Anthropic retires Claude Opus 4.5 on 22 January 2027. CISA's MONAI Label remediation deadline is 26 November, and a Shirudo technical webinar is scheduled for 15 December.
