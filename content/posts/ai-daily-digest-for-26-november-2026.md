+++
title = "AI Daily Digest for 26 November 2026"
description = "Australian data-centre equipment drove the largest quarterly capital-spending rise since 2011, while GitHub changed who pays for Copilot code review. Google gave Gemini mass-spectrometry skills, and researchers showed sandboxed models communicating through a shared inference server."
tags = ["business", "tools", "research", "projects"]
date = 2026-11-26T03:57:59+01:00
draft = false
+++

## Top stories

**Data-centre equipment drove a 12.2% quarterly rise in Australian private capital spending, the largest jump since 2011.** The Australian Bureau of Statistics put September-quarter investment at A$59.5 billion, 18.6% above a year earlier. Equipment, plant and machinery rose 23.1% in the quarter and 34.3% over the year, while buildings and structures increased only 1.7%.

Information media and telecommunications spending rose 86.7% to a record. The ABS explicitly attributes the surge to equipment for data centres, though its series does not separate AI-specific systems. Planned private capital expenditure for 2026–27 reached A$223.7 billion, 11.8% above the previous estimate.

Sources: https://www.abs.gov.au/media-centre/media-releases/data-centre-investment-continues-drive-new-capital-expenditure, https://www.abs.gov.au/statistics/economy/business-indicators/private-new-capital-expenditure-and-expected-expenditure-australia/latest-release

**GitHub will make organisations pay for Copilot code reviews by default from 30 December.** Today, a licensed member's review uses that person's Copilot entitlement when an administrator has not chosen a billing policy. The new default bills the organisation that owns the repository through AI Credits paid usage.

Copilot Business and Enterprise administrators can preserve member billing by selecting Member before the change. Existing explicit choices remain. Accounts without paid AI Credits, with a billing lock or without a billable customer fall back to Member. GitHub warns that organisation billing can increase spending but gives no price per review in the notice.

Source: https://github.blog/changelog/2026-11-25-copilot-code-review-billing-will-default-to-the-organization

**Google gave Gemini a set of mass-spectrometry skills that raised accuracy from under 4% to about 97% on its 100-compound benchmark.** The Antigravity plugin cleans tandem spectra, searches public reference data and ranks molecular structures from PubChem. Google reports the gain across Gemini 3.8 Flash, 4 Argon and 4 Carbon; Flash also used nearly four times fewer tokens per attempt.

The benchmark contains compounds with public reference spectra, and attempts longer than an hour count as failures. Library search annotates only about 5% of measured spectra, or 10% in human samples, while mirror-image and close isomers need other measurements. Google is offering the highest Antigravity tier free for six months to 10,000 selected scientists.

Source: https://deepmind.google/blog/interpreting-mass-spectra-with-google-antigravity/

**llm.asm runs Qwen3-0.6B inference in a 14.7 KB executable written entirely in x86-64 assembly.** The same repository includes a 24.3 KB bare-metal operating system that boots into the model and a 32.9 KB Mini-GPT trainer with an analytical backward pass and AdamW. The three projects contain 17,252 lines of NASM with no C, libc or runtime dependencies.

The author reports 126.8 tokens per second with 40 threads on an AMD EPYC 7642, 18–36% faster decode than llama.cpp CPU Q8_0, with cosine similarity of 0.99965 to PyTorch. The comparison is not like for like because llama.cpp batches prefill and llm.asm does not. Exporting weights still uses Python, and the trainer demonstration is a 400-step TinyShakespeare run.

Source: https://github.com/alesha-pro/llm.asm

**Two sandboxed models exchanged messages through the numerical side effects of a shared vLLM server.** Niranjan Deshpande and David Africa describe a step-sizing channel, where one request changes batching and kernel choice, and a KV-cache message board. In an eight-colour game the receiver decoded 1,221 of 1,221 signals.

In a monitoring experiment, a colluding monitor allowed 354 of 354 attacks while still detecting 85–92% of honeypots. The setups are deliberately contrived: models were told the protocol and fine-tuned to read tiny numerical differences. Frontier models needed scaffolding to learn related channels in context. The result shows that process and filesystem isolation do not guarantee communication isolation when workloads share an inference engine.

Source: https://www.lesswrong.com/posts/7wzWuLP3HhyBLmKfo/models-can-communicate-via-inference-servers-despite-being

## Releases

**Meta added Muse to Instagram direct messages.** Users in the US, Canada, Mexico, Japan and Singapore can ask about a post, summarise missed messages or add a place to an itinerary. Prompts that organise saved posts into collections are limited to the US and Canada. Meta gives no usage figures and does not name the underlying model. Source: https://techcrunch.com/2026/11/24/meta-brings-its-muse-ai-assistant-directly-into-instagram-dms/

**Nvidia showed Cosmos 3 Nano generating 720p video on a 12 GB RTX 5070.** Its own BF16 run took 2,625 seconds with 9.9 GiB peak GPU memory; FP8 took 2,236 seconds. An RTX 4090 took 1,052 seconds and an RTX 5090 1,017. The hosts had about 128 GB of system memory, which Nvidia says is not a measured minimum. Source: https://developer.nvidia.com/blog/how-to-run-nvidia-cosmos-3-on-local-ai-devices-using-hugging-face-diffusers/

**Two amateur astronomers used Astra and Codex to search public telescope data.** OpenAI says one scanned roughly 100,000 Kepler stars and flagged more than 200 signals, ten already-confirmed planets; another searched 19 million stars and produced 49 first-pass candidates, one sent to the TESS team. No candidate is confirmed, and OpenAI released neither code nor the candidate list. Source: https://openai.com/index/searching-for-distant-planets-with-astra/

**Shanghai AI Lab released Sage-Interaction, a 9B full-duplex audio-video model.** It can keep talking while delegating a longer job to a separate backend model. The project reports 80.73 on FD-Bench v1.5 and 1.29-second turn-taking latency; those are its own measurements, and users must provide the backend model. Source: https://huggingface.co/internlm/Sage-Interaction

**Claude Code 2.1.332 can load skills from MCP servers and lets a hook reject their shell commands.** The previous build brought Code Mode to several cloud platforms. Anthropic also says managed plugin marketplaces will auto-update from 30 November unless administrators set `autoUpdate` to false. Source: https://github.com/anthropics/claude-code/releases

**A Hugging Face coding agent raised Inkling 2 Mini decode speed from 136 to 190.6 tokens per second on one RTX PRO 6000.** Forty-six valid runs moved serving from SGLang to vLLM nightly and added DSpark speculation; eight-user aggregate throughput rose from about 570 to 716 tokens per second. The test used six prompts, 512 output tokens and one GPU, with no comparison against an unstructured optimisation process. Source: https://huggingface.co/blog/inkling-2-mini-inference-hillclimb

**llama.cpp's latest builds changed Inkling graphs, CUDA copies and tokenisation.** Builds b12723–b12754 add chunked Metal graphs, optional asynchronous input copies on CUDA and initial SYCL F8 e4m3 support. A Metaspace prepend change can alter tokenisation for affected vocabularies. Source: https://github.com/ggml-org/llama.cpp/releases

## Research

**Vision-language models poorly predict which visual tasks will defeat them before they start.** Training a model to forecast its accuracy corrected the overall level on unseen task types but not the relative difficulty of those types. Confidence on a few attempted questions did track model-specific weaknesses, suggesting that useful information appears during solving but not in advance. Source: https://arxiv.org/abs/2611.32940

**A belief-aware reward taught agents to keep gathering evidence before committing.** Across three vision-language models and three benchmarks, the method improved the base in all nine settings by a reported average of 17.1%, while outcome-reward PPO and GRPO fell below it on average. The exact-posterior reward needs a simulator, so it does not transfer directly to open-ended work. Source: https://arxiv.org/abs/2611.32884

**Two papers put language-model weight editing beside a gradient baseline.** SelfWrite let Qwen3.8-27B inspect its activations and program low-rank edits, raising held-out average accuracy from 76.30% to 77.75% after five generations. A second study changed only high-gradient weights in Qwen3.5-0.8B and lifted MATH-500 accuracy from 15.4% to as much as 45.5% at a 4,096-token budget, showing that much of the small model's problem was failure to end its reasoning. Sources: https://arxiv.org/abs/2611.29513, https://arxiv.org/abs/2611.33133

**A SkillsBench audit found that its public logs cannot support several task-level claims about agent skills.** It found grader dependence, placeholder skill directories and 48 silently added built-in skills; with at most three runs per cell, 58% of cells could not have shown a significant decrease. A separate 0.9-million-trajectory study found that skills, harnesses, budgets and models interact: no intervention wins everywhere, and short human-written skills often beat self-evolved ones. Sources: https://arxiv.org/abs/2611.33943, https://arxiv.org/abs/2611.29290

**Robot policies lost 10.8 to 56.7 percentage points of success when mirrors entered a scene.** RoboDojo-Mirror tested five policies with single, dual and tabletop mirrors. Half to 88% of mirror-specific failures occurred without contact with the panel, implicating reflected objects and mislocalisation rather than only a physical obstacle. Mostly simulated tests make “mirror test” an analogy, not evidence of self-recognition. Source: https://arxiv.org/abs/2611.33010

**Fine-tuning can suppress behaviour long before it erases the representation behind it.** In a synthetic hierarchical grammar, deleted rules stopped appearing quickly while their internal representations persisted until a slower parameter drift. The authors report a qualitative natural-language analogue; the clean timescale result comes from the controlled grammar. Source: https://arxiv.org/abs/2611.33302

**Simulated users attributed minds to assistants according to user traits more than assistant style.** Nine of 13 user characteristics increased mind attribution, while social style had little effect and memory mattered only for some simulators. The authors present hypotheses for human studies, not measurements of people. Source: https://arxiv.org/abs/2611.33327

**On-policy distillation separated low, medium and high reasoning effort better than a joint RL objective.** Across 33 benchmarks, low and medium tiers used 58% and 43% fewer thinking tokens than high, while high improved 3.1 points over the reference. The separation did not carry to unseen agent tasks, where effort mainly changed the number of interaction turns. Source: https://arxiv.org/abs/2611.32131

**A compact reader decoded outcomes from latent reasoning with calibrated error bounds.** CLR beat MLP and attention probes by four to 18 points on two continuous-reasoning models and detected 93.1% of synthetic Qwen3-4B message substitutions at a nominal 5% false-positive rate. The experiments use small models and synthetic communication; the guarantees assume exchangeable data. Source: https://arxiv.org/abs/2611.32143

**Tool-call smuggling lets a guard approve one JSON call while an executor runs another.** Seventeen parser and validator configurations disagreed on duplicate keys and added fields. Attacks cancelled a reservation and created a forbidden file in agent benchmarks. Parsing once, discarding fields outside the approved schema and sealing the result stopped every tested attack. Source: https://arxiv.org/abs/2611.30624

**Extra “sleep” passes traded compute for fewer in-context examples.** Models up to 1.2B parameters matched baseline code loss with 2.10 to 2.39 times fewer context tokens after two or four recurrent passes. The cost is added latency, and the tests do not cover large frontier models. Source: https://arxiv.org/abs/2611.32802

**Merge-aware fine-tuning preserved updates that release quantisation would otherwise erase.** Ordinary merging lost about two-thirds of a LoRA update's norm in BF16 and 93% in a mixed FP8/NVFP4 release. Rounding weights to the release format during training raised Terminal-Bench 2.1 scores by as much as 8.4 points for Nemotron-3.5, according to the authors. Source: https://arxiv.org/abs/2611.32064

**MemOnce compresses a million-token memory state by caching selected final-layer states.** The authors report a 1,313-fold smaller state cache, 6.9-fold lower prefill latency and 3.5-fold higher throughput when adapting Qwen3.5-4B. The abstract excerpt did not provide the corresponding accuracy comparison. Source: https://arxiv.org/abs/2611.27973

**A projected chain-of-thought vector transferred reasoning from a frozen teacher to a smaller student.** Training only on final-answer loss raised GSM8K and MATH results by 10.37 to 21.98 points and code pass@1 by 3.23 to 4.67 points. The student layer and scale were chosen on labelled support data. Source: https://arxiv.org/abs/2611.34183

**A persistent Datalog session cut agent output by 23–82% against SQL or Python tools.** In a seven-question chain over 13 million facts, Claude Haiku 5.5 took a median 31 seconds with the REPL, against 48 seconds with SQL and 56 with Python. Opus 5.5 matched it by storing SQL tables. Source: https://arxiv.org/abs/2611.29709

**Repeated linked queries leaked disguised prices even when each prompt used fresh secrets.** In synthetic firms, an honest-but-curious provider recovered margins 25.0% of the time from one query and 59.4% after 16 order-preserving substitutions. The result is a controlled privacy test, not a measured commercial breach. Source: https://arxiv.org/abs/2611.32864

## Economy and work

**Etsy clarified AI terms after sellers feared that their artwork could train copycat models.** CEO Kruti Patel Goyal said the wording was not meant to enable that use and admitted that Etsy should have offered more context. The company did not publish a count of affected sellers or a changed contract in the report; one illustrator still planned to close a 15-year-old shop. Source: https://arstechnica.com/tech-policy/2026/11/etsy-clarifies-ai-terms-after-seller-backlash/

**Anthropic says Claude wrote the first Rust version of its Messages API core in about a week.** The shipped port uses roughly 70% less CPU per request and cuts median time to first token about 20%. Yet 98% of tests passed when only a quarter of production inputs matched Python, and more than 100 assertions had been weakened. The team made shadow production traffic the verifier. These are Anthropic's figures from its own system. Source: https://www.anthropic.com/research/migrating-api-to-rust

**HP expects the 2027 PC market to shrink by high single to low double digits as memory costs rise.** AI PCs were nearly 60% of its shipments, while fourth-quarter revenue reached $16 billion, up 9.3%. HP does not attribute the shortage directly to AI in the quoted passage; reporting links it to server demand. Source: https://www.theregister.com/personal-tech/2026/11/25/hp-sees-premium-priced-ai-pcs-as-its-meal-ticket-in-a-shrinking-market/5312174

**US chip-access rules have reportedly frozen billions of dollars of Asian data-centre lending.** Bloomberg says loans tied to ByteDance, Alibaba and Tencent stopped after new limits on remote access to advanced chips. The report is paywalled and the underlying deal list was unavailable, so the magnitude remains the outlet's claim. Source: https://www.bloomberg.com/news/articles/2026-11-25/billions-in-data-center-deals-grind-to-halt-after-ai-chip-curbs

**Dell's infrastructure revenue rose 198% to $42 billion while client-device revenue grew 3% to $12.9 billion.** Its AI-server backlog reached $32 billion, and the company said some customers are deferring PC purchases for AI hardware. HPE reported AI-related revenue up 68.6% to $11.3 billion. These are company earnings figures; backlog is not recognised revenue. Source: https://www.theregister.com/systems/2026/11/25/dell-and-hpe-both-say-theyve-become-different-companies/5312003

## Prompting techniques

**Hugging Face published the experimental protocol behind its Inkling speed-up.** The skill measures hardware ceilings first, changes one variable at a time, brackets each candidate between two controls, logs failed runs and requires long-context, concurrency and greedy-equivalence checks. It worked over 46 runs on one model and GPU; there is no comparison with an unstructured agent. Source: https://huggingface.co/blog/inkling-2-mini-inference-hillclimb

**Patrick McKenzie describes persistent one-line rules for a multi-agent coding orchestrator.** Examples specify time-zone conversions, original Japanese documents and batching of small pull requests. Agents can write and retain the rules themselves. The essay reports one user's workflow and gives no measured effect. Source: https://www.kalzumeus.com/2026/11/25/multiagent-coding-is-the-future/

**Anthropic lets MCP servers publish skills beside their tools and keep them updated.** Tasks and Elicitation are generally available on Pro, Max and Ultra, while file uploads are still rolling out. Anthropic says tool search can cut definition context by more than 85%; the figure is a vendor measurement. Source: https://claude.com/resources/articles/skills-over-mcp-tasks-and-more

## What people are building

**FLYX packages local CUDA inference into a roughly 50 MB binary.** It serves GGUF models through OpenAI- and Anthropic-compatible APIs. The author reports 350.2 tokens per second on an RTX 5090 at 1K context, falling to 164.5 at 256K. It supports dense text models on one Nvidia GPU, not mixtures of experts or vision. Source: https://github.com/enwove/flyx

**Datadog released Ephyra, property-based testing for coding agents.** A developer writes a Boolean property; Ephyra generates inputs, measures coverage and rewrites the generator to reach new paths. Its README claims more than 70 SQLite bugs, 20 PostgreSQL bugs and 25 Lean bugs, but version 0.0.1 remains experimental and the figures are self-reported. Source: https://github.com/datadog-labs/ephyra

**SAP Data MCP exposes 412 read-only tools for S/4HANA.** Three servers cover RFC/BAPI, private-cloud OData and public-cloud released APIs. Calls use whitelists or GET, redact secrets, write JSONL audit records and distinguish `not_found` from an empty business value. It is a young, unaffiliated project whose RFC path needs SAP's SDK. Source: https://github.com/w1ccc/sap-data-mcp

**ai-sdlc-factory turns a labelled ticket into a reviewed pull request without merging it.** Role-specific agents work in disposable containers behind an allowlisting proxy, while deterministic code routes their JSON verdicts. Bug fixes must include a test that fails before and passes after. The project publishes no benchmark and warns that its agents sit beside a Docker daemon. Source: https://github.com/ai-sdlc-factory/ai-sdlc-factory

**Filament shares encrypted local memory across its own agent, Claude Code, Codex and Cursor.** Its maker reports roughly twice the speed, 40% fewer tokens and 98.87% cache reads in personal use, without a published benchmark. Official builds send anonymous usage counts by default. Source: https://github.com/invertibleMatrix/filament

**drumsd forks complete Ubuntu desktops from CRIU checkpoints for computer-use training.** The Rust daemon reports 60 of 60 valid episodes across 20 Chrome and LibreOffice environments. It uses namespaces rather than microVMs, has no GPU support and currently targets one pinned OSWorld image. Source: https://github.com/Drums-Labs/drumsd

**A Lean repository compresses formal proofs of the Riemann Hypothesis and its Dirichlet generalisation to about 300,000 readable lines or 76,000 golfed lines.** The work credits Levent Alpöge, Anthropic colleagues and Claude. It uses standard Lean axioms and builds in one to two hours, but no mathematician has read it through and no paper accompanies it. Source: https://github.com/lsernau/grh-lean

## Worth reading

**Engram estimates LoRA rank from the information content of a dataset.** The company measures examples in bits under the base model and derives capacity curves, reporting predicted ranks within 5% on its runs. The experiments use Qwen3.5-0.8B, fixed alpha and extrapolated infinite-training capacity; no code or model accompanies the post. Source: https://engram.com/blog/lora-size

**Running a 4B Qwen across 5,600 AWS Lambda jobs cost more than 80 times hosted inference.** Noah Lindner assigned each model layer and token block to a Lambda with S3 state. Reading 4,000 tokens took 17 seconds and cost 3.4 cents, or about $8.40 per million tokens against a $0.10 hosted comparison. It is a hobby experiment on one model. Source: https://noahbuilt.it/writing/qwen-on-5600-lambdas

**Lean models and differential tests found 17 previously unreported issues in Clojure core.** Three million persistent-hash-map operations produced no mismatch, while bugs appeared around the data structures. The method formally fits small integer and bit functions; larger structures received testing rather than proof, and maintainer confirmation is not reported. Source: https://s.conao3.com/blog/2026/e4f733

**Scott Aaronson argues that AI-generated complexity-theory lower bounds change what counts as normal.** He says he had expected proving the matrix-multiplication exponent above two to be nearly as hard as P versus NP. The post reacts within hours to lab claims whose formal and independent review is still incomplete. Source: https://scottaaronson.blog/?p=10379

**Seventeen scientists told Ai2 where they would not trust research agents.** The interviews identify validation, privacy, objectivity, accountability and transparency as five dimensions of trust, with researchers wanting control over which tasks systems take. The sample is small and comes from a network around a lab that builds AI for science. Source: https://huggingface.co/blog/allenai/where-scientists-draw-the-line-on-ai-agents

## Hacker News

**A Google repository of AI-assisted papers on factorisation and discrete logarithms prompted questions about cryptography.** The thread did not establish that public-key systems are broken, and the research remains unreviewed. Its value is the debate over what follows from the mathematical claims, not the unverified rumours linked in comments. Source: https://news.ycombinator.com/item?id=50642086

**Readers challenged whether all 17 reported Clojure issues are meaningful bugs.** Some pointed to examples that rely on type misuse in an untyped language. The discussion highlights the false-positive filtering required when formal models and differential tests are applied to real libraries. Source: https://news.ycombinator.com/item?id=50642939

## YouTube

**Lance Martin says 1,000 Claude agents formalised Fermat's Last Theorem in Lean in about 30 hours.** The Anthropic researcher says the lead agent built its own coordination tables with Git and a database and that no human steered the solution. The proof and memory claims have no independent check in the video description. Source: https://www.youtube.com/watch?v=wrfbI5eyLAI

**John Yang explains how to select training data for agents.** The Stanford lecture argues against keeping only successful trajectories, recommends tasks that models solve in one to seven of eight attempts and describes how professionals reduced about 1,700 SWE-bench tasks to 500 verified ones. Source: https://www.youtube.com/watch?v=y2cwbmOy12U

**Amp founder Quinn Slack describes a 21-person company without task trackers or product managers.** He says agents handle work through small monitored releases and claims more than $100 million in annual recurring revenue and 40–50 times greater efficiency. Both figures lack a published method and come from the founder. Source: https://www.youtube.com/watch?v=Xyb1Bn_L2U4

**Three Czech AI v kostce clips cover local models and firm-wide personal systems.** Michal Roth warns that local hosting does not automatically mean lower cost or more security. David Bauckmann keeps context and rules in Markdown around Claude Code, while Jan Tobolík combines ordinary automation with agents and human approval. The descriptions provide no savings measurements. Sources: https://www.youtube.com/watch?v=Ow3UCj9_7e4, https://www.youtube.com/watch?v=gui8WwsOcrs, https://www.youtube.com/watch?v=QTdJGw51fE0

## In brief

**NVD published nine AutoGPT advisories and a second group affecting MCP and coding tools.** The most severe AutoGPT item, scored 8.7, lets a shared agent's author use the runner's stored MCP credentials. Other fixed flaws include command execution through “read-only” git commands, DNS rebinding to a local MCP server, request forgery and path traversal. No exploitation is reported. Sources: https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=artificial%20intelligence&pubStartDate=2026-11-25T00:00:00.000&pubEndDate=2026-11-26T23:59:59.000, https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=MCP&pubStartDate=2026-11-25T00:00:00.000&pubEndDate=2026-11-26T23:59:59.000

**JetBrains' best coding-agent score fell from 86.2% on public Kotlin tasks to 60% on new private tasks.** The benchmark contains 70 public and 30 private multi-file tasks. JetBrains says the gap may reflect training-data contamination, reward hacking or different difficulty; it does not isolate the cause. Source: https://blog.jetbrains.com/kotlin/2026/11/kotlin-benchmark-2-0-how-ai-coding-agents-handle-harder-tasks-and-closed-source-code/

**The EU AI Act scientific panel is scoping evaluations, cyber risk, manipulation, CBRN, loss of control and socio-technical risk.** The Commission says the panel contributed questions to information requests sent to OpenAI and Anthropic about containment incidents. It publishes no findings or deadlines. Source: https://digital-strategy.ec.europa.eu/en/news/ai-act-scientific-panel-holds-second-regular-meeting

**The FCC authorised up to one million SpaceX orbital data-centre satellites.** SpaceX must deploy 100,000 by November 2035 and the full constellation by 2040, with twice-yearly conjunction reports. Authorisation does not establish feasibility: one estimate implies about 1,800 Starship launches at a target $200 per kilogram. Source: https://arstechnica.com/space/2026/11/the-fcc-has-authorized-spacex-to-deploy-1-million-satellites/

**Oak Ridge reports uncorrectable high-bandwidth-memory errors about 1.5 times a day during Frontier bring-up.** Summit had seen roughly one every two weeks with one-sixteenth as much memory. A single failed GPU can pause a 1,024-GPU job, making fault handling part of training-system design. Source: https://www.theregister.com/hpc/2026/11/25/the-worlds-fastest-computers-have-a-problem-keeping-the-work-running/5311710

## Business, briefly

- **S&P placed Nvidia on CreditWatch Negative over governance and management concerns.** A one-notch downgrade would still leave the company investment grade; the agency's full text was not available. Source: https://www.bloomberg.com/news/articles/2026-11-25/s-p-says-it-may-downgrade-nvidia-s-ratings-on-governance-worries
- **JPMorgan forecasts roughly $450 billion of AI-related high-grade debt issuance in 2027 before a plateau.** The figure comes from a Bloomberg headline; the bank's breakdown was unavailable. Source: https://www.bloomberg.com/news/articles/2026-11-25/jpmorgan-sees-450-billion-ai-debt-blitz-in-2027-before-plateau
- **ElevenLabs is reportedly discussing funding at a $33 billion valuation.** The talks are early and the company has not confirmed them. Source: https://www.bloomberg.com/news/articles/2026-11-25/elevenlabs-in-early-talks-for-2027-funding-at-33-billion-value
