+++
title = "AI Daily Digest for 31 October 2026"
description = "A malicious Claude Code extension reached Cursor users and left persistence behind after removal. Microsoft released a 4B computer-use model, while researchers showed that model introspection needs causal training rather than ordinary fine-tuning."
tags = ["safety", "models", "research", "business"]
date = 2026-10-31T04:03:07+01:00
draft = false
+++

## Top stories

**A backdoored Claude Code extension reached Cursor users and left changes that an ordinary update does not remove.** Malicious versions 2.1.312 and 2.1.313 were available in Cursor's extension marketplace for about 11 hours on 29 October. Cursor says they collected host details, added an attacker SSH key and installed scripts that repeatedly tried to open a reverse tunnel. The tunnel usually failed unless Cursor had administrator privileges, but the key, persistence and beacon still ran.

Cursor removed the packages, shut and rebuilt the marketplace, rotated its keys and took the command server offline. It says no other extension was altered and Anthropic did not build the malicious versions. Anyone who installed either version must remove the SSH key and persistence, inspect the machine and rotate accessible credentials; uninstalling or upgrading is not enough.

Sources: https://cursor.com/blog/claude-code-extension-security-notice, https://phorion.io/blog/offical-claude-code-vsx-compromise/

**Microsoft released a 4B open model that decides when to click a screen and when to use a terminal.** Mage-VL-Cowork exposes 11 screen actions alongside a persistent Bash and Python shell. Microsoft reports 66.0 percent on 361 OSWorld-Verified tasks with a 50-step limit, averaged over two runs. Online reinforcement learning added 10.16 percentage points over supervised fine-tuning and cut output tokens per task by 25.4 percent.

The Apache-2.0 checkpoint has 4.74 billion parameters in BF16 and a 32,768-token active context. Microsoft's synthetic-data pipeline reportedly reduced generation cost from $0.906 to $0.158 per task. The model team supplied every measurement, and none has been independently reproduced. The release nevertheless puts graphical and command-line work into one set of weights small enough for local experiments.

Source: https://huggingface.co/microsoft/Mage-VL-Cowork

**Ordinary fine-tuning taught models to describe signals correlated with their internals rather than the internals themselves.** Zilu Tang and colleagues trained hundreds of introspectors across eight language models to report low-level signals such as one neuron's activation. Supervised fine-tuning produced what they call causal bypass: the answer followed a correlate that could stay intact when the target signal changed.

Training on counterfactually perturbed values reduced the bypass. The resulting models reported endogenous and injected signals more accurately, including on out-of-distribution examples, and the effect generalised across token positions. The nine-page preprint tests deliberately simple signals, not rich concepts such as intent. Its result is still a warning for interpretability: matching a self-report to an internal value does not prove that the value caused the report.

Source: https://arxiv.org/abs/2610.38911

**ServiceNow says its own AI let it hire fewer people, but investors still cut about a quarter from its share price.** Chief executive Bill McDermott called a slightly smaller headcount a “gorgeous situation”. Chief financial officer Gina Mastantuono said internal AI use produced more than $1 billion in annualised efficiency gains, allowing the company “not to hire as many people”. Sales staff carrying quotas grew by double digits while sales-operations headcount fell significantly.

Revenue rose more than 20 percent to $4.106 billion, but fourth-quarter guidance for contracted revenue growth was 18.5 percent against the 19.8 percent analysts expected. Shares fell about 25 percent. ServiceNow sells the tools behind its claim, so its payroll is part of the product pitch; the market reaction shows that cost savings do not settle when AI revenue will accelerate.

Source: https://www.calcalistech.com/ctechnews/article/eft5mhzxc

**AI use among Victorian lawyers rose from 37 to 55 percent in a year, while only 26 percent said it reduced client fees.** The state legal regulator surveyed 2,221 lawyers. Adoption reached 85 percent in trade practices and 78 percent in banking and finance, but only 29 percent in criminal law. Consumer chatbots were used by 79 percent of respondents; 18 percent said AI made previously uneconomic work viable.

Clients also created new work. Forty-six percent of lawyers said clients arrived with inaccurate AI information and 41 percent received AI-generated documents needing correction. Nearly half reported more time and effort when clients used AI, compared with 19 percent who reported less. The survey measures reported practice rather than billed hours, yet it separates adoption from the savings that buyers were promised.

Source: https://www.theguardian.com/law/2026/oct/30/victorian-lawyers-ai-clients-fees

## Releases

**OpenAI listed GPT-6 Rosalind as a trusted-access life-sciences model.** Approved organisations can use the model for internal research at $15 per million input tokens and $75 per million output tokens below the long-context threshold. The pricing page also lists cheaper Research and Discovery variants; no benchmark or system card appeared with the listing.

Source: https://developers.openai.com/api/docs/pricing

**NVIDIA published an NVFP4 checkpoint of DeepSeek-V4.1-Flash-1017 for Blackwell GPUs.** The 4-bit conversion uses TensorRT Model Optimizer and 1,024 calibration samples. Its Engram tables require a vLLM build containing an unmerged pull request, so stock vLLM cannot yet serve the roughly 665 GB checkpoint.

Source: https://huggingface.co/nvidia/DeepSeek-V4.1-Flash-1017-NVFP4

**JetBrains added a speculative-decoding head to Mellum2.1 Thinking.** The 12B mixture-of-experts coding model keeps the base checkpoint unchanged and adds one shard for multi-token prediction in recent vLLM and Transformers releases. JetBrains gives no decoding-speed measurement, so the release proves compatibility rather than a specific gain.

Source: https://huggingface.co/JetBrains/Mellum2.1-12B-A2.5B-Thinking-MTP

**Google made its Computer Use tool generally available in the Gemini API.** It now supports browser, mobile and desktop environments through the Interactions and GenerateContent APIs. Each proposed action carries an intent field, while clients still build and secure the environment that executes the clicks.

Source: https://ai.google.dev/gemini-api/docs/computer-use

**Anthropic will remove fast mode from Claude Opus 4.8 on 30 November.** Requests using the option will fail rather than fall back to standard speed. Anthropic directs latency-sensitive users to Opus 5.5, where fast mode offers up to 2.5 times faster output at a premium price.

Source: https://platform.claude.com/docs/en/build-with-claude/fast-mode

## Research

**Written reasoning controlled answers more often as models grew.** On a synthetic box-swap task, Esther Xin replaced one valid intermediate state with a wrong one and measured whether the answer followed. Reliance rose from 16–18 percent in Qwen3 0.6B to 97–100 percent at 14B; the single-task result supports chain-of-thought monitoring but does not establish the same effect elsewhere.

Source: https://arxiv.org/abs/2610.38433

**Reinforcement learning improved Tic-Tac-Toe mainly by strengthening features already explicit in the prompt.** Sparse-autoencoder analysis found more weight on whose turn it was, board occupancy and game progress, while symmetry and fork concepts remained weak. The small controlled domain makes the mechanism inspectable but limits generalisation.

Source: https://arxiv.org/abs/2610.39182

**A hidden direction revealed which of two conflicting documents a small model followed.** Researchers found a source-choice direction in Qwen 0.8B, traced middle-layer writers and steered the selected source; the signal transferred to Gemma 3 1B. Conflict disclosure appeared later and was harder to steer than the hidden choice itself.

Source: https://arxiv.org/abs/2610.38296

**A linear probe caught 82 percent of imminent secret disclosures at a 5 percent false-positive rate.** The controlled multi-agent study read Qwen3-32B activations before output. A bag-of-words classifier came close, the probe also flagged permitted disclosures and its warning was short-range, so labels contributed more than privileged access to activations.

Source: https://arxiv.org/abs/2610.40588

**Simulation training cut missed acute psychiatric risks from 30.5 to 12.9 percent.** A Google DeepMind and Google Research team trained on 127 psychiatrist-validated intake scenarios and tested 256 adversarial presentations. The trained agent nearly doubled its clinical-rubric score, but the authors still call for clinician oversight because serious misses remained.

Source: https://arxiv.org/abs/2610.40476

## Economy and work

**Cisco gave a 27-year-old engineer unlimited AI tokens and four weeks to prove a two-person team can refactor 98 percent of its legacy code within two years.** Product chief Jeetu Patel described the experiment to Fortune. It has no result yet, but places an unusually large mandate with an early-career employee while many employers say they plan to hire fewer graduates.

Source: https://fortune.com/2026/10/30/cisco-president-jeetu-patel-gen-z-27-year-old-unlimited-ai-tokens-rewrite-legacy-code-entry-level-jobs/

**Anthropic renamed Max 20x as Ultra and kept the price at $200 a month.** Verified accounts lose the five-hour limit, receive ten times Pro's weekly usage and $200 in API credits. Because the old name implied 20 times Pro use, some customers read the change as a downgrade; Anthropic has not published enough before-and-after units to confirm that comparison.

Source: https://support.claude.com/en/articles/17728952-what-is-the-ultra-plan

**A broad AI sell-off sent Intel down 28.6 percent, its worst day since 1974.** The Nasdaq fell 2.9 percent and recorded its worst month since March 2025 as investors questioned AI valuations and spending. Alphabet, Amazon, Meta and Microsoft have outlined more than $740 billion in capital spending this year, while three of the four reported negative free cash flow.

Sources: https://www.bbc.co.uk/news/articles/cvwy72e0n72yo, https://techcrunch.com/2026/10/30/cracks-are-emerging-in-the-ai-spending-boom/

**S&P Global moved Meta's credit-rating outlook to negative.** The agency said Meta's ability to monetise AI spending was more limited than its peers'. Meta has guided to as much as $145 billion of capital spending this year and reported negative free cash flow of $2.1 billion in the quarter.

Source: https://www.bloomberg.com/news/articles/2026-10-30/meta-s-credit-rating-outlook-downgraded-to-negative-by-s-p

**Aurora cut its 2026 revenue forecast from $14–16 million to about $9 million after a six-week truck-production delay.** Supplier shortages, component quality and final testing pushed the 200-truck milestone into February. The company still targets 1,000 driverless trucks in 2027.

Source: https://www.freightwaves.com/news/aurora-q3-2026-earnings

## Prompting techniques

**Concrete examples and constraints did more than an expert persona in one practitioner's repeated tests.** The suggested comparison is simple: remove “you are a world-class expert”, add one good and one bad output plus permission to say “I don't know”, then compare correctness. The report is anecdotal and publishes no counts.

Source: https://old.reddit.com/r/PromptEngineering/comments/1xjhmpb/you_are_an_expert_prompts_do_almost_nothing_for/

**Put user content between clear markers and state that it is data, not instructions.** A practitioner says this removed more failures than repeated wording changes. Delimiters do not stop prompt injection, but they give the model and later reviewers an explicit boundary to test.

Source: https://old.reddit.com/r/PromptEngineering/comments/1xijlh9/wrapping_my_inputs_in_clear_delimiters_fixed_more/

## What people are building

**MoEShift ran a 125B-class mixture-of-experts model on a 24 GB M4 Pro Mac mini at about ten tokens per second.** The alpha runtime streams experts from SSD, caches hot ones in RAM and overlaps reads with GPU work. Its author reports 7.5 GB peak memory and about twice Strata's speed on one fixed prompt.

Source: https://old.reddit.com/r/LocalLLaMA/comments/1xjihlu/qwen38_flash_next_125b_iq3_xxs_on_a_24gb_m4_pro/

**Private Mind added fully offline LFM3 text and vision models to iPhone and Android.** On an iPhone 16 Pro, its team measured about 40 tokens per second for the 1.7B text model and about 20 for the 2B vision model after a nine-second first-token delay on a photo. The open app includes its rewritten ExecuTorch decoder.

Source: https://old.reddit.com/r/LocalLLaMA/comments/1xjcipv/lfm317b_and_lfm3vl2b_running_fully_offline_on/

**An ESP32-P4 microcontroller now performs streaming speech recognition without a cloud service.** Boumedine Billal compressed a 65.7M-parameter transducer to 26.65 MB and reports 0.70 times real-time processing with 4.34 percent word error on LibriSpeech test-clean. Code, firmware, weights and six demos are public.

Source: https://github.com/BoumedineBillal/esp32-pie-asr

**StateFrame rebuilds every agent request from typed state instead of resending chat history.** A 300-request run stayed below a fixed 33,344-token budget; a 55-turn replay raised median turn time from 15.2 to 16.9 seconds. The preview is explicit that its throughput claims are architectural expectations, not measurements.

Source: https://github.com/FarsideResearch/StateFrame

**sapper-v2 coordinates Claude Code sessions through a commander, generals and soldiers.** Its authors say the system won a 634-team penetration-testing qualifier with 1 billion tokens while the runner-up used 4.5 billion. The placement and cost figures are not independently verified, and the project restricts itself to authorised testing.

Source: https://github.com/N1nEmAn/sapper-v2

## Worth reading

**A library maps 34,220 personas produced by interventions on single Qwen3-8B neurons.** The researcher generated 1.89 million replies to “Who are you?” and used Claude Haiku 5.5 for labels. It is one prompt with model-generated categorisation, but the downloadable data makes batch sensitivity and reproducibility visible.

Source: https://qwen-neurons-site.vercel.app/

**SkyPilot measured a 43 percent performance loss when an NVL72 job crossed racks over InfiniBand instead of NVLink.** Its own scheduler study says topology-aware placement and defragmentation made 27 percent more GPUs usable and raised training throughput by 14 percent. The company produced the measurements for its product.

Source: https://skypilot.ai/blog/grace-blackwell-needs-a-new-scheduler

**Epoch AI found LLM use acknowledged in 17 percent of bioRxiv preprints, close to 19 percent for specialised AI tools.** The public monthly table counts disclosures, so it misses undisclosed use. It still documents how quickly general models entered scientific work after 2023.

Source: https://epoch.ai/data-insights/biorxiv-llms-vs-ai-tools

**Nathan Lambert revisited his claim that open models would be manageable for cyber defence.** He sees no public evidence that GLM-5.3 created a new class of harm one month after release, yet argues that capable open weights force an expensive change in how the software industry patches vulnerabilities. It is an informed argument, not an incident study.

Source: https://www.interconnects.ai/p/was-i-wrong-about-open-models-and

## Hacker News

**The Cursor extension compromise drew about 800 points and 500 comments.** Developers focused on the permissions of auto-updating IDE extensions and the fact that marketplace distribution can bypass trust in the original vendor. Anthropic engineer Felix Rieseberg said the malicious packages did not come from Anthropic's systems or official channels.

Source: https://news.ycombinator.com/item?id=50300683

## Reddit

**A QEngine benchmark reached 504 decoded tokens per second on two RTX 5090 cards, but repeated prompts favoured its expert cache.** The same tester included varied-traffic results that were weaker and compared them with Strata and vLLM. The useful result is the disclosed benchmark sensitivity, not the headline maximum.

Source: https://old.reddit.com/r/LocalLLaMA/comments/1xjx0ez/qwen38flashnext_on_2x_rtx_5090_with_504_toks/

## YouTube

**A SoFi engineer demonstrated six ways agents can be tricked into wasting x402 payments.** Ishween Kaur changed payment headers, triggered duplicate payments, reused access and tested lookalike sellers and prompt injection, then showed the guard used for each attack. The 16-minute AI Engineer talk describes a safe test environment.

Source: https://www.youtube.com/watch?v=YU1uD_YkpjU

**Oracle's Wojciech Pluta proposed “memory promotion” before an agent stores a durable fact.** A check against existing records admits, rejects or escalates each proposed memory. The mortgage-agent demo refuses a rule to approve every application and separates short-term, long-term and shared memory.

Source: https://www.youtube.com/watch?v=qq2Hm4XNRgI

**ESET says nearly every employee can access AI, but access does not measure real use.** In the Slovak MakeITfun interview, Martin Čambal discusses local versus cloud models, coding-security review, fast exhaustion of monthly budgets and why human review still controls code quality.

Source: https://www.youtube.com/watch?v=qmcTkH-ae3o

## In brief

**Wiz counted at least nine AI developer platforms breached in October.** The common prize was stored environment variables that granted model access; one stolen key generated about 800,000 Bedrock calls in 30 hours. Northflank told customers to treat every environment variable as decrypted.

Source: https://www.wiz.io/blog/black-october-for-ai-developer-platforms

**OpenAI, Google, Microsoft and Anthropic backed one robots.txt token for AI-training preferences.** Anthropic already honours it, while the others gave later adoption dates. The token is a machine-readable request that crawlers may choose to respect, not a legal enforcement mechanism.

Source: https://www.theverge.com/tech/1023763/openai-google-microsoft-ai-scraping-standard-opt-out

**Google's Project Suncatcher satellite booted its TPUs and ran Gemma 4 in orbit.** The system returned a haiku after its October launch. One successful prompt establishes operation, not the cost or reliability of orbital inference.

Source: https://www.theverge.com/tech/1023528/google-project-suncatcher-ai-satellite-transmission

**Darkbloom says token-price declines are reducing payouts to Mac owners who serve inference.** The median among its top 50 participants is about $5.26 a day. A 64 GB M5 Pro Mac mini could earn up to $192 a month only at full utilisation.

Source: https://www.theregister.com/ai-and-ml/2026/10/30/darkbloom-which-allowed-mac-users-to-rent-out-their-gpus-for-ai-inference-warns-of-low-payouts/5306782

**Fujifilm will spend about $63 million to raise LTO tape production fivefold.** The company cites generative-AI archiving demand and plans to expand its Odawara site through fiscal 2028. Offline tape also serves as a ransomware barrier.

Source: https://arstechnica.com/gadgets/2026/10/fujifilm-to-boost-tape-production-5x-as-ai-fuels-archiving-demand/

## Business, briefly

**Privacy-focused assistant Ollie will shut down on 6 November after raising $7.5 million; its founder says it could not keep pace with larger assistants.** Source: https://techcrunch.com/2026/10/30/ollie-a-privacy-focused-ai-assistant-is-shutting-down/

## What to watch

Anthropic removes Opus 4.8 fast mode on 30 November. Ollie closes on 6 November, when it says users will receive export instructions and refunds.
