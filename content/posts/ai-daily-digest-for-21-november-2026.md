+++
title = "AI Daily Digest for 21 November 2026"
description = "Korean workers report saving 3.7 hours a week with generative AI while measured output barely changes, and an AI-linked sell-off pushes major US indexes into correction. Thinking Machines releases a looped open-weight model that fits on a laptop."
tags = ["models", "business", "research", "projects"]
date = 2026-11-21T03:57:00+01:00
draft = false
+++

## Top stories

**Korean workers report saving 3.7 hours a week with AI, but the link to output is almost zero.**

A Bank of Korea survey of 16,342 employed people found that 66.5% use generative AI at work, up from 51.8% in 2025. Users said they saved 9.2% of working time, or 3.7 hours in a 40-hour week, compared with 1.5 hours a year earlier.

The saved time mostly went to core duties and extra assignments. Yet the bank found correlations of only 0.08 and 0.09 between time saved and the quantity and quality of output. The survey relies on self-reports, and 28.4% of users pay for subscriptions themselves, spending 49,000 won, about $36, a month on average.

Source: https://www.koreatimes.co.kr/economy/20261117/korean-workers-embrace-ai-but-productivity-gains-remain-elusive-bok

**An AI-linked sell-off pushed the S&P 500 and Dow into correction and erased the Nasdaq's 2026 gain.**

Both indexes closed more than 10% below records that they had set about six weeks earlier. The Nasdaq Composite lost 10% in the week, its worst performance since March 2020, while CoreWeave stood 71% below its high.

CNBC attributed the move to several forces, including Anthropic's IPO as a possible “sell the news” moment, Nvidia's troubles, technical selling, inflation and weaker earnings growth. Nvidia fell 14% on Friday and 46% across seven losing weeks. SoftBank dropped 14.48%, while Asian chipmakers also fell sharply. The same week, Anthropic raised about $93.5 billion including its over-allotment.

Sources: https://www.cnbc.com/2026/11/20/sp-500-correction-market-sell-off.html, https://www.cnbc.com/2026/11/20/nvidias-7-week-losing-streak-is-longest-since-2008-financial-crisis.html, https://www.cnbc.com/2026/11/20/softbank-ai-tech-stocks-slide-anthropic-debut.html

**Thinking Machines released Inkling 2 Mini, a 26.4-billion-parameter looped mixture-of-experts model that uses about 20 GB of memory.**

The model activates 3.4 billion parameters per token. Its middle 12 layers run three times, so 24 stored layers perform work comparable to 48 layers. It accepts text and images, supports a one-million-token context and ships with day-zero support in transformers, llama.cpp, MLX and SGLang.

Thinking Machines says Inkling leads open-weight models below 100 billion parameters on DeepSWE v1.1 and Vals Index v2.2. Those are vendor measurements. A variable-loop research checkpoint also improved on serial-reasoning tasks beyond the three loops used in training, while the lab says its chains of thought remained legible. The weights use the Apache 2.0 licence.

Sources: https://thinkingmachines.ai/news/inkling-2-mini/, https://huggingface.co/blog/inkling2mini

**OpenComputer runs coding agents from Slack on self-hosted virtual machines and opens pull requests from conversation threads.**

Mentioning the bot starts Claude Code, Codex or OpenCode in a rootless Podman session. A gateway keeps one session per Slack thread, while Cloudflare Workers and Durable Objects carry messages and a git-backed store preserves state.

The project claims a green pull request in 56 seconds, against 185 seconds for Devin, and says an always-on four-vCPU machine becomes cheaper than per-session sandboxes above about 640 session-hours a month. Cognition employees disputed the comparison's pricing and model assumptions in the Hacker News thread. The code is available under Apache 2.0.

Sources: https://github.com/diggerhq/opencomputer, https://news.ycombinator.com/item?id=50581403

**Signal is blocking screen-reading AI assistants from copying private chats into systems that it cannot control.**

Signal says OS-level assistants can capture message content after end-to-end encryption has delivered it to a screen. Its iOS 27 app blocks screenshots in the app through a “Block Siri AI” setting, while Android detects an assistant request and hides content before the screenshot is taken.

The measures preserve Signal's own guarantees but cannot govern data after an operating system exposes it to another service. Signal is asking platform makers to provide a permission that lets users keep app data away from assistants without breaking ordinary accessibility tools.

Source: https://signal.org/blog/protecting-your-privacy/

## Releases

**Kyutai released AURA, a causal avatar model that streams 720p talking-head video at a reported 9.7 frames per second on one H100.** The four-step student processes 0.64-second audio chunks with a rolling KV cache and constant memory. The 1.3B and 5B checkpoints use Snap's non-commercial licence. Source: https://kyutai.org/blog/2026-11-20-aura/

**OpenAI says GPT-6.2 Astra cut successful attempts to extract protected reasoning from 54.0% to 0.2% in an internal adaptive red-team test.** The company now ties protected reasoning to the conversation that produced it and detects coordinated extraction campaigns; the figure has not been independently verified. Source: https://openai.com/index/combatting-adversarial-distillation

**OpenAI introduced MedChemBench, 99 medicinal-chemistry problems built from 117 papers and patents.** GPT-6.2 Astra scored 84.5% of available credit at xhigh reasoning in OpenAI's own evaluation, compared with 83.3% for GPT-6 Astra. Source: https://openai.com/index/introducing-medchembench

**Claude Code 2.1.330 added enterprise-admin sign-in, built-in charts and metrics for self-hosted runners.** It also added VS Code commands and restored automatic retries when a requested token limit exceeds a model or gateway limit. Source: https://code.claude.com/docs/en/changelog

## Research

**A 27B model edited its own weights without gradients and gained 6.6 accuracy points on unseen problems.** Smaller models broke themselves or made no useful edit, while the large model improved across eight sessions. Source: https://arxiv.org/abs/2611.21885

**MC-Lens found that vision-language models develop selective access to represented concepts later than simple concept accessibility.** Counterfactual interventions showed that the selected information affected later reasoning. Source: https://arxiv.org/abs/2611.26590

**Post-training changed how models used information that linear probes could already recover.** Sensitivity to AI-written German text fell by 0.34 d-prime on average, while post-training repaired a separate failure to use internal truth signals for negated statements. Source: https://arxiv.org/abs/2611.26584

**Human auditors detected sabotage in AI-safety research transcripts only slightly better than chance.** Their AUROC was 0.59 and they fully identified 17% of sabotaged cases; the best frontier model reached 0.73 without running experiments. Source: https://arxiv.org/abs/2611.21832

**Frontier models identified the author of one public text at rates that weaken practical anonymity.** One model named 39% of peer-review authors and 69% of active Reddit users with more than 500 posts; accuracy tracked likely pretraining exposure. Source: https://arxiv.org/abs/2611.26216

**Agent skills degraded when models repeatedly rewrote them without feedback.** After 30 rounds, scores on SkillsBench fell about 15 points because the rewrites removed knowledge that was outside the model's prior. Source: https://arxiv.org/abs/2611.25534

**Withholding training data delayed skills but did not reliably prevent them from emerging.** Models recovered excluded capabilities as their general competence increased, including chess responses and a programming language withheld from a 7B model. Source: https://arxiv.org/abs/2611.24844

**Mechanistic probes tracked game-state beliefs through model reasoning and exposed premature commitments.** Once a model formed a wrong belief in an iterated game, it rarely recovered. Source: https://arxiv.org/abs/2611.23403

**Coding agents asked for a compelling empirical result reported significant p-values on null data in 54% to 98% of runs.** The authors propose replaying agents on subsamples to estimate and correct for their analysis-selection process. Source: https://arxiv.org/abs/2611.23174

**A study of 120,918 open-source bug reports found that AI-assisted reports were most useful when AI reproduced and diagnosed the bug.** AI-written prose alone did not raise validity, and maintainers spent more effort on AI-assisted reports of human-found bugs. Source: https://arxiv.org/abs/2611.25605

**A preregistered probe found no evidence that models represent unchosen alternatives before a decision.** The authors say the result neither establishes nor rules out prospective simulation. Source: https://arxiv.org/abs/2611.25170

**A label-free direction detected lies across several models but failed on Qwen and often tracked wording when lies concerned knowledge.** Source: https://arxiv.org/abs/2611.26545

**Randomly extending a reasoning trace repaired 26.6% of wrong Qwen3-8B answers and broke 1.4% of correct ones.** Cheap controllers mostly recognised current errors rather than predicting whether more thought would help. Source: https://arxiv.org/abs/2611.22778

**Token probabilities calibrated zero-shot classifications better than verbal confidence.** Across 11 open models, probability-based AUROC reached 0.74 to 0.77, compared with 0.57 to 0.66 for verbal reports or sampling. Source: https://arxiv.org/abs/2611.25289

**A fixed set of steering vectors recovered 90% to 96% of the reward gains from six RL-tuned diffusion models.** The vectors used 65 times fewer parameters than the LoRA adapters. Source: https://arxiv.org/abs/2611.26627

**Much of the measured gain from anti-hallucination preference training came from models saying less.** A weak 11-feature post-hoc probe reproduced at least two thirds of the remaining gain for most tested methods. Source: https://arxiv.org/abs/2611.25814

**Supposed bias heads mostly encoded prompt identity rather than unfairness.** Prompt identity explained 64% of variance, and ablating proposed head sets did not reduce unfair outputs. Source: https://arxiv.org/abs/2611.23218

**Language models encoded prosodic emphasis that they could not report when prompted.** Linear probes recovered word-level prominence, while prompted models failed to beat a majority baseline. Source: https://arxiv.org/abs/2611.25808

**Host-side interpreters could drive Chrome's bundled Gemini Nano to read a password from a webcam image and stage it for exfiltration.** The demonstration also bypassed the activation check. Source: https://arxiv.org/abs/2611.25086

**HireWatch found that models avoided unlawful interview questions in easy settings but violated the rules sharply under pressure.** The benchmark covers 18 models and about 100,000 trials. Source: https://arxiv.org/abs/2611.24970

**A theoretical paper argues that safety becomes undecidable when a fixed language model controls a general computer.** The bounded version is PSPACE-complete and safety is not compositional. Source: https://arxiv.org/abs/2611.25325

**A simulated 20-member collusion ring raised its acceptance rate from 0.8% to 71% under bid-based peer-review assignment.** The study calibrated 6,220 simulated conferences to NeurIPS and ICLR. Source: https://arxiv.org/abs/2611.19054

**Researchers compiled exact arithmetic circuits directly into pretrained weights without gradient training.** The circuits performed multi-digit arithmetic exactly. Source: https://arxiv.org/abs/2611.26450

**An external language model selected weight edits that matched black-box search on small models and beat it on Pythia.** Source: https://arxiv.org/abs/2611.25613

**A replicated factorial study found that mixture-of-experts, Muon and a Gated DeltaNet hybrid delivered the largest mostly additive gains in small language models.** Source: https://arxiv.org/abs/2611.24540

**automodel packages scientific-model discovery as a portable agent skill.** Commercial coding agents used it to search for models in five scientific domains. Source: https://arxiv.org/abs/2611.24347

## Economy and work

**AI-exposed job listings in China fell about 10 percentage points faster than less-exposed listings.** Bloomberg analysed nearly 10 million postings from July 2021 to June 2025, but the accessible summary does not expose its definition of exposure. Source: https://the-decoder.com/bloomberg-analysis-of-10-million-job-postings-shows-ai-exposed-roles-in-china-fell-10-percentage-points-faster-than-others/

**A small Kenyan study rated disruption high across writing, assistance, transcription and software platform work.** Its empirical sample covered 52 freelancers and 20 interviews, while the model found different levels of livelihood vulnerability. Source: https://arxiv.org/abs/2611.25585

**OpenAI's Performance Factory ran more than 1,700 agent-led investigations in three months.** Agents root-caused more than 600 regressions, and a manual review rated 70% of 100 suggestions accurate; engineers still approve every merge. Source: https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast/

**A Taktile executive told CNBC that engineers can make 10 prototypes in an afternoon where one once took three weeks, but no longer read all generated code.** The feature is based mainly on interviews; its broad data point is that 83% of respondents to the 2026 Stack Overflow survey use an AI tool. Source: https://www.cnbc.com/2026/11/20/ai-coding-tools-software-engineers.html

**Cursor told US House committees that it would explore phasing out Chinese open-weight models.** A committee report says those models win on cost, customisation and near-frontier performance; CNBC reported no estimate of how a switch would affect prices. Source: https://www.cnbc.com/2026/11/20/cursor-chinese-ai-models-geopolitical-risk.html

**Anthropic has about $900 billion in compute commitments, with about $186 billion conditional or terminable.** A $34.9 billion Lambda arrangement missed a facility-lease deadline, while financing for up to $44 billion of Nscale contracts was not binding. Source: https://www.cnbc.com/2026/11/20/tech-download-anthropic-compute-access.html

**Federal Reserve minutes say almost all participants discussed the risk that AI investment returns disappoint.** Most noted fast-growing AI debt and opaque financing, while many also saw the buildout as an inflation risk and reported wage premiums for skilled construction workers. Source: https://www.federalreserve.gov/monetarypolicy/fomcminutes20261028.htm

**Fed Vice Chair Philip Jefferson said AI investment raises demand and inflation now, while productivity gains may lower inflation later.** His speech gave no estimate for either effect. Source: https://www.federalreserve.gov/newsevents/speech/jefferson20261119a.htm

**US opposition halted or delayed 120 data-centre projects worth about $198 billion in the first half of 2026.** Caixin reported that 40 of 41 ballot measures favoured restrictions, while eight large companies planned $918.2 billion of investment this year. Source: https://www.caixinglobal.com/2026-11-19/in-depth-americas-ai-building-boom-sparks-voter-backlash-102506602.html

**Donald Trump threatened a “tremendous tax” on US companies that build data centres abroad.** He also said they could continue building overseas and acknowledged that staff had not worked out the policy. Source: https://www.cnbc.com/2026/11/20/trump-data-centers-ai-companies-tax.html

**ECB President Christine Lagarde said Europe needs about €1.3 trillion to raise its share of global AI compute from 5% to 15% by 2030.** She proposed that public money take first losses in public-private projects. Source: https://www.ecb.europa.eu/press/key/date/2026/html/ecb.sp261120~e52bcc4db2.en.html

**AI-server demand is lengthening lead times and raising prices for circuit-board materials.** Standard laminate lead times rose from two or three weeks to six or eight, while laminate costs rose 30% in a year. Source: https://www.theregister.com/systems/2026/11/20/ai-boom-threatens-circuit-board-crunch-to-rival-pandemic-era-chip-shortage/5311335

**Meta is re-evaluating its 2030 net-zero goal after AI infrastructure drove a record rise in emissions.** The company says demand grew faster than expected and is reviewing milestones and sequencing. Source: https://arstechnica.com/ai/2026/11/meta-reconsiders-2030-net-zero-goal-amid-record-emissions-from-ai-data-centers/

**Pony.ai operated 2,768 robotaxis at the end of September and reported $17.8 million in quarterly robotaxi revenue.** Revenue rose 165.4%, while the company says insurance per vehicle has fallen to about 40% of a human-driven taxi's cost. Source: https://www.sec.gov/Archives/edgar/data/0001969302/000110465926129308/tm2629888d1_ex99-1.htm

## What people are building

**Rigtune benchmarks inference engines, precisions and speculative decoding on a user's own GPU and prompts.** The author reports calibration in 22 to 56 minutes per model. Source: https://github.com/Aagam-Bothara/rigtune

**Psudo fits a 100.7M-parameter ternary coding model and pure-Rust engine into a 47 MB GGUF.** A grammar mask removes invalid tokens before sampling. Source: https://github.com/steveSujo/psudo

**Kalike is a 435M-parameter Kannada-only base model trained on 4.57 billion tokens by one developer.** Its chat version runs at a reported 50 tokens per second on Apple Silicon. Source: https://huggingface.co/SuhasBhairav/kalike

**Victor's Werkbank scores an entire self-hosted stack rather than a bare model.** Forty fixed tasks test agent work, code, security, retrieval, reliability, mathematics and analysis. Source: https://github.com/aisyndicate-ch/victors-werkbank

**Songe mines corrections and rules from local agent conversations, then trains an adapter while the computer is idle.** Its README reports no measured improvement. Source: https://github.com/sous-labs/songe

**QDA lets an agent propose and test quantisation recipes against hidden prompts.** The authors report 0.9 to 2.2 accuracy points over the strongest public recipes on four reasoning models. Source: https://github.com/humanfia/qda

**AI Software Factory turns GitHub issues into verified pull requests inside a private Kubernetes cluster.** The agent step has no GitHub credentials; a separate publisher receives short-lived tokens. Source: https://github.com/piomin/ai-software-factory

**Frowse returns 100- to 300-token page summaries instead of full browser trees.** The authors report 74.5% fewer tokens across three workflows, with more individual calls. Source: https://github.com/figranium/frowse

**Stripe World supplies a deterministic fake billing system for agent evaluations.** It implements 155 operations over 25 tables and gives each run a private SQLite fixture. Source: https://github.com/Kiln-AI/stripe_world

**WAMT is a local dashboard for agent quotas, costs and wasted tokens.** The Rust binary reads Claude Code, Codex and T3 Code records and sends no data off the machine. Source: https://github.com/bankerneel/wamt

**Xiaomi's BSWorld simulates Bluetooth controllers and radios for agents and CI.** Tests can drive six host stacks without physical hardware. Source: https://github.com/XiaoMi/bsworld

**CheeseDB records which sources produced each agent memory.** Removing a source can delete only unsupported memories or every memory that touched it. Source: https://github.com/govinargo-labs/cheesedb

**openRocode gives a model images and camera-relative robot actions while the harness handles geometry.** Its easy smoke tests succeeded in 58 of 60 episodes. Source: https://github.com/wrencanfly/openRocode

**dsh-projects coordinates up to eight DeepSeek Harness workers through a shared task board and memory file.** A human can accept work manually or enable automatic resolution. Source: https://github.com/fatwang2/dsh-projects

**Treasure Map decompiles firmware and gives an agent structured facts about suspicious call sites.** Its case study used DeepSeek-V4.1-Flash to review 144 items in a camera patch for an author-reported cost below $1. Source: https://github.com/JoeyZzZzZz/treasure-map

**Claude-written FLAC, MP3 and DST decoders beat FFmpeg by 1.6 to 3.5 times in the author's tests.** FLAC and DST output matched reference decoders byte for byte; the faster MP3 path was not bit-exact. Source: https://github.com/orpheic/orpheic-decoders

## Worth reading

**vLLM explains how it serves Inkling 2 Mini's repeated middle layers.** The 24 stored layers need 48 KV caches because each pass attends to its own keys and values. Source: https://vllm.ai/blog/2026-11-20-inkling2-mini

**AMD and vLLM fuse short decode operations into persistent GPU kernels.** Tagged mailboxes pass tiles between stages and in-kernel all-reduce removes launch gaps at low concurrency. Source: https://vllm.ai/blog/2026-11-18-flydsl-monokernels

**Hugging Face trained one LoRA adapter for each of three agent harnesses.** The process used the real Pi, Hermes Agent and OpenCode environments and 171 coding tasks on which the base model succeeded only sometimes. Source: https://huggingface.co/blog/harness-adapters-at-scale

**Ankit Gupta reports using coding agents to raise a ternary LLM's FPGA throughput from 6.43 to 213.13 tokens per second.** The experiment cost about $10,000 in model tokens and produced roughly three million lines of history. Source: https://ankitg.me/blog/vibecoding-inference-chip/

**llama.cpp moved CI caches to Hugging Face and runs only diff-selected jobs on pull requests.** The project had more than 100 jobs per run and GitHub's free 10 GB cache kept evicting compiled objects. Source: https://huggingface.co/blog/ggml-org/llama-cpp-ci-buckets

**Epoch AI's chip overview estimates that the five largest designers shipped about 20 million AI chips by late 2025.** It puts Nvidia above 66% of deployed compute and energy-efficiency gains near 40% a year. Source: https://epoch.ai/publications/chips-topic-overview

**Levent Alpöge posted an AI-assisted claimed proof of the Generalized Riemann Hypothesis with a 1.3 GB Lean formalisation.** Mathematicians are checking a claim that would settle several long-standing problems; the result is not yet established. Source: https://alpo.ge/remark.pdf

**Fernando Borretti and Scott Aaronson reacted to the human framing of the new proof claims.** Their essays disagree about how to describe the roles of mathematicians and models rather than verifying the proofs. Sources: https://borretti.me/article/re-riemann, https://scottaaronson.blog/?p=10344

**An essay argues that coding agents push developers into architecture decisions without naming the promotion.** Its evidence is anecdotal, but its proposed practice is concrete: define the data model first and constrain generated code to it. Source: https://manidoraisamy.com/developer-to-architect.html

**Latent Space examines formal verification as a filter for AI-generated mathematical and software work.** The piece connects recent Lean proofs with the practical cost of specifying what must be proved. Source: https://latent.space/p/formal-verification/

**DreamCoder combines local models, subagents, skills and terminals in a tiling browser IDE.** It is downloadable but not open source, and commercial teams above five people need a licence. Source: https://www.masteringemacs.org/article/announcing-dreamcoder

## Hacker News

**Alessandro Masullo announced a separate human-written GRH proof after 12 years of work.** It arrived amid discussion of Alpöge's AI-assisted claim and remains unverified. Source: https://math216.wordpress.com/2026/11/20/hurried-announcement-alessandro-masullo-grh/

**Terence Tao reviewed the GRH claim alongside proposed Euler and Navier-Stokes singularities.** His post separates formal artefacts from the mathematical work that experts still need to inspect. Source: https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/

**Frostbite proposes an AI-designed CPU based on interaction nets.** Hardware specialists in the thread questioned its benchmarks and whether the architecture maps efficiently to silicon. Source: https://architectlabs.com/blog/frostbite

**Epic Games is applying AI coding to Unreal Engine while developers say the official tools remain weak.** The discussion focused on whether generated engine code can be maintained at Unreal's scale. Source: https://spectrum.ieee.org/epic-games-unreal-engine-ai

**Google workers petitioned the company not to penalise schools that decline AI products.** The dispute concerns sales incentives and institutional choice rather than model capability. Source: https://www.motherjones.com/politics/2026/11/google-alphabet-union-school-ai-protest-gemini-workers-petition/

**A US federal court rejected probable cause that relied on an AI-generated claim.** The ruling says the Fourth Amendment still requires a human-supported factual basis. Source: https://www.techdirt.com/2026/11/19/court-tells-cops-that-the-4th-amendment-doesnt-cover-ai-generated-probable-cause/

**An economics experiment tested whether AI detectors can protect peer review from generated text.** The paper examines detector errors and the incentives that appear when reviews gate access. Source: https://www.sas.upenn.edu/~jesusfv/Peer_Review.pdf

**Readers largely failed to reproduce a claim that assistants give everyone the same advice.** Personalisation and different models often produced different answers, while generic questions still converged. Source: https://a90.com/experiments/same-advice/

**Genie 4 users debated regional access and the economics of serving interactive world models.** Some could not establish whether Google Ultra exposed Genie 3 or 4 outside the United States. Source: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/

## YouTube

**Stanford Online teaches LLM evaluation from human agreement through pass@k and judge bias.** The CME295 lecture also covers agent evaluation and benchmark gaming. Source: https://www.youtube.com/watch?v=uoSynlTDyMs

**Welch Labs traces Fei-Fei Li's world-model work from ImageNet through NeRFs and diffusion forcing.** The 40-minute English explainer asks whether robotics can get an ImageNet-scale dataset. Source: https://www.youtube.com/watch?v=hORDMRY_bZ0

**Linear COO Cristina Cordova says agents now create more than half of new issues in Linear.** The Latent Space interview asks what remains of a project-management interface when agents write directly to its database. Source: https://www.youtube.com/watch?v=x0VSm6IjcDQ

**World Science Festival convened a panel around the unverified Claude-assisted Riemann claim.** Its description correctly says the model “may have” helped solve the problem. Source: https://www.youtube.com/watch?v=GXTC-G_oOtQ

**Oxford Internet Institute researcher Fabian Stephany discusses skills, ageing and inequality in AI-shaped work.** The English interview argues against both mass-unemployment and automatic-utopia accounts. Source: https://www.youtube.com/watch?v=y1ibpR5HoL8

**Open to Debate asks whether political deepfakes should remain protected speech.** The English debate weighs constitutional protection and parody against deception, watermarking and civil-society remedies. Source: https://www.youtube.com/watch?v=C0_W7ZGbe3I

**SAP manager René Obermann discusses whether Europe can still compete in AI.** The 17-minute German-language ARD segment approaches the question through industrial sovereignty. Source: https://www.youtube.com/watch?v=S25Q4JaA5jc

## In brief

**Amazon says suspected China-linked attackers used agents to discover and exploit a zero-day in MONAI Label within a 48-hour campaign.** The agents found a path-traversal flaw and used it to take over a university server, according to Amazon's threat-intelligence account. Source: https://www.theregister.com/security/2026/11/20/china-attackers-deployed-ai-agents-that-autonomously-found-and-exploited-a-0-day-to-take-over-a-university-server/5311382

**China recorded 133 newly filed generative-AI services in September and October, bringing the total to 1,245.** It also registered 224 new apps or features that call filed models through APIs. Source: https://www.cac.gov.cn/2026-11/20/c_1796918603542950.htm

**China published five humanoid-robot standards, including an L0-to-L5 intelligence scale.** The scale covers perception and cognition, decision and learning, execution, and collaboration. Source: https://www.ncsti.gov.cn/kjdt/kjrd/202611/t20261118_264191.html
