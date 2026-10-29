+++
title = "AI Daily Digest for 29 October 2026"
description = "Google announced Gemini 4 Carbon but restricted access to cyber defenders. Agent traffic forced GitHub to plan four million more CPU cores, while the best tax agent passed only 10.8% of professional assignments."
tags = ["models", "research", "agents", "business"]
date = 2026-10-29T04:04:47+01:00
draft = false
+++

The day's strongest results pair impressive output with the systems that people need to trust, fund and operate it. Access, professional judgement and infrastructure remain as important as model scores.

## Top stories

**Google announced Gemini 4 Carbon as its strongest model, but only selected cyber defenders can use it.** Google says Carbon scores 59 on Artificial Analysis Intelligence Index v5 and reports 88.2% on SEC-bench Pro, 54.8% on ExploitGym and 71.0% on CWE-bench. All figures come from Google, and the announcement links no independent evaluation or Carbon model card.

Access begins through Google's Fairwind programme and will later expand to trusted partners. The company is also participating in the US government's voluntary pre-release testing process. Developers, businesses and consumers have no release date.

Google lists an introductory API price of $2 per million input tokens and $10 per million output tokens, rising later to $4 and $20. Google has published a price before it has offered general access. The staged rollout therefore matters as much as the benchmark lead. Sources: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/, https://news.ycombinator.com/item?id=50276792

**GitHub plans four million additional CPU cores and 160 PB of fast storage after agent-generated code strained its platform.** GitHub recorded 7.4 billion commits in September, five times the number from a year earlier. The Register attributes repeated outages since December to the resulting traffic and reconstructed a low of about 84% for GitHub's 90-day availability on 7 May.

Microsoft executive Jay Parikh said GitHub is separating compute from storage, a redesign that the company expects to increase throughput 35-fold. It also plans a multi-region Azure architecture by early next year and more capacity for GitHub Actions.

The figures measure volume, not code quality. They still show a concrete infrastructure consequence of agentic development: shared systems built for human-scale contribution must now absorb machine-generated activity. Source: https://www.theregister.com/ai-and-ml/2026/10/28/github-powering-up-four-million-extra-cores-to-stop-its-service-going-down/5305863

**The best agent passed only 10.8% of 50 professional tax assignments in Surge AI's DAYJOB benchmark.** The vendor built environments with 1,789 files and graded completed work against a 95% rubric threshold. Claude Sonnet 5.5 led, followed by Claude Fable 5.1 at 9.6% and Claude Opus 5.5 at 9.2%.

The assignments require agents to resolve conflicting records, find issues that clients did not mention and produce returns, workpapers or advice. In one case, GPT-6 Astra correctly compared two possible home-sale dates but missed a later deadline for a tax exclusion worth up to $250,000 in all five attempts. Claude Opus found it in all five.

Surge AI created and evaluated the benchmark, so the results are vendor evidence. The gap between fluent advice and a deliverable that meets professional standards is nevertheless explicit. Source: https://surgehq.ai/blog/dayjob-tax

**A preprint found that tested latent world models could solve tasks without faithfully modelling their environments.** Rodrigo Gonzalez Laiz and Steffen Schneider define faithfulness as an agreement between the environment's transition map and learned latent dynamics. They introduce latent rollout consistency to measure whether action-conditioned predictions preserve that structure.

None of the state-of-the-art systems in their study solved its task through faithful dynamics. Task scores therefore concealed a difference between producing the right outcome and learning an internal process that follows the environment.

The paper was submitted on 27 October and has not been peer reviewed. Its result narrows what benchmark success can establish about an agent's internal understanding, especially when a system is expected to plan across long horizons. Source: https://arxiv.org/abs/2610.37588

**Lao Gan Ma denied a reported claim that AI cut one production line from more than 600 workers to 48.** Chinese outlets attributed the figure to executive Li Xin, along with a claim that AI pepper inspection reduced errors to almost zero. The company says Li did not discuss staffing numbers, and his full remarks are not public.

Corporate records cited by Sixth Tone show that employees enrolled in social insurance fell from nearly 3,000 in 2022 to 740 in 2025, a decline of about 75%. That does not establish that AI caused the fall; retirement and turnover also change the figure.

The dispute comes after China's State Council asked employers to slow AI-driven job replacement, warn workers before large deployments and provide transition periods and retraining. The public claim, the denial and the headcount indicator must remain separate. Source: https://www.sixthtone.com/news/1019180

## Releases

**NVIDIA released Nemotron 3.5 Transcribe, an open-weight speech model with Czech and Slovak support.** The 30B-A4B checkpoint has about 4.3 billion active parameters, transcribes 40 languages, translates 31 to or from English and labels speakers in 13. NVIDIA reports 5.33% average word error for English and 4.62% across seven languages; these are the company's readings of third-party leaderboards. Sources: https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B, https://huggingface.co/blog/nvidia/nemotron-transcribe-granary

**Sakana AI opened early access to an enterprise API platform.** The OpenAI-compatible service initially offers Sakana Fugu and Fugu Ultra, with workspace controls, audit logs and budget caps. Sakana says customer inputs will not be used for training; applicants receive pricing privately. Source: https://sakana.ai/api-platform-earlyaccess/

**OpenAI added monthly API credits to ChatGPT Pro and Business subscriptions.** Pro plans receive $100, $200 or $500 by tier; Business receives $20 per Standard seat and $100 per Premium seat, pooled up to $500 per workspace. Credits expire each billing cycle and do not roll over. Source: https://developers.openai.com/api/docs/guides/chatgpt-api-credits

**Anthropic expanded its AI for Science programme to 20 funding and research organisations.** Partners will distribute free Claude credits, although Anthropic did not disclose their value. Named projects include a research-preview specification for agents that operate laboratory instruments. Source: https://www.anthropic.com/news/ai-for-science-expands-foundations-research-institutions

**xAI added custom moderation controls to the Grok API.** Developers can ask Grok to decline content in the `nsfw`, `violence` and `profanity` categories through a `guidelines` array. Categories that are omitted retain the default moderation policy. Source: https://docs.x.ai/developers/advanced-api-usage/custom-moderation-controls

**Lightricks released optional watermarking weights for LTX-2 video and audio.** PixelSeal stores a 256-bit payload in video frames and AudioSeal marks stereo audio. Lightricks says the marks are not cryptographic signatures and that an absent mark does not prove content was not generated. Source: https://huggingface.co/Lightricks/LTX-2-Marking

## Research

**An untrained simulation of an adult fly connectome reached 95% of odour sources.** The spiking network contains 172,433 neurons and runs inside a simulated body. Rewiring that preserved each neuron's connection counts and signs reached 18%, suggesting that wiring carried much of the tested sensorimotor behaviour. Source: https://arxiv.org/abs/2610.33881

**Unaided LLM plans became less economical as sliding-puzzle horizons grew.** The authors collected 8,400 one-shot plans without tools or execution feedback and separated legal execution, coordination and action economy. Some models completed every trial while using increasingly inefficient plans. Source: https://arxiv.org/abs/2610.36415

**RLEC trains one model to answer or abstain according to an explicit confidence target.** The preprint changes the reward and its schedule so that a requested accuracy such as 90% remains distinguishable during training. The authors report one model that follows several targets without a post-hoc threshold. Source: https://arxiv.org/abs/2610.35059

**Distillation preserved one GPT-2 circuit and destroyed another.** DistilGPT-2 retained 87.7% of the greater-than circuit's performance by remapping it to an earlier layer, but its indirect-object circuit fell from 94.8% to 35.2% accuracy and preserved no name-mover heads. Aggregate similarity measures hid the difference. Source: https://arxiv.org/abs/2610.37157

**Steering vectors transferred between text and image generation in a unified multimodal model.** A vector found from text tokens changed image output without additional training, and the reverse also worked. The causal intervention suggests that some concepts share an implementation across modalities. Source: https://arxiv.org/abs/2610.36269

**GEPA-Curator filters unreliable failures before using them to optimise an agent prompt.** The method removes tasks with noisy signals and supplies successful past trajectories as context. Its authors report gains of up to 20.7% over GEPA and 21.2% over ACE across four benchmarks. Source: https://arxiv.org/abs/2610.37651

**Memory compression caused multi-agent groups to lose decisive information.** On CrossProfile, even a perfect relevance filter reintroduced decoys and fell 23 to 31 points behind rarest-first selection in the classic configuration. The benchmark contains 480 tasks with verified answers. Source: https://arxiv.org/abs/2610.37624

**Transformer pruning failures remained invisible to accuracy and perplexity.** On GPT-2's indirect-object circuit, head pruning erased the circuit, while 30% neuron pruning preserved its heads but reversed their contribution so that the model preferred the wrong name. Source: https://arxiv.org/abs/2610.37126

**Safety probes transferred from base models to distilled successors despite representation rotation.** Probe AUC changed by between -0.011 and +0.027 even when the measured unsafe direction rotated by 17 to 35 degrees. The result may let auditors reuse some probes across related models. Source: https://arxiv.org/abs/2610.35586

## Economy and work

**GitHub Enterprise now includes Copilot seats but meters every request from the first one.** Included access carries no monthly AI-credit allowance; users without an Enterprise licence can buy comparable access for $10 per month. Administrators must now manage usage budgets rather than rely on a fixed per-seat allowance. Source: https://github.blog/changelog/2026-10-28-github-enterprise-now-includes-access-to-github-copilot

**GitHub says Copilot Fusion approaches leading coding-agent scores at about half the task cost.** Fusion routes work among allowed models. GitHub reports a score of 60 on the Artificial Analysis Coding Agent Index, within two points of Claude Code with Opus 5.5 Max, while using about half the tokens and 40% less time. The comparison is a vendor claim. Source: https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion

**Anthropic added reports that compare enterprise AI spending with team output.** TechCrunch connects the release to Jellyfish data from about 276,000 users: spending on agentic coding tools grew tenfold since January and reached about 2% of engineering cost, while most large companies reported no major gains. The measurements come from vendors. Source: https://techcrunch.com/2026/10/28/anthropic-just-launched-tools-to-show-companies-what-their-ai-spending-is-buying/

**Alphabet shares fell 8% to 10% after it said AI Mode earns less than classic Search.** Search growth slowed to 12% while capital spending reached $51.4 billion. Google attributed the slowdown to lower monetisation in AI Mode, even as query growth reached its fastest pace in five years. Source: https://www.theregister.com/ai-and-ml/2026/10/29/google-struggling-to-make-ai-mode-searches-pay/5306181

**SK hynix says AI-driven memory shortages will last through 2030.** Hardware makers are moving some PC production back to China to reduce component costs, while SK hynix reported record profit and long-term deals covering more than half of its 2027 and 2028 output. Sources: https://www.theregister.com/systems/2026/10/28/sk-hynix-says-memory-shortages-to-persist-until-2030/5305887, https://asia.nikkei.com/business/technology/tech-asia/hp-and-asus-shift-some-pc-making-back-to-china-due-to-ai-driven-cost-hikes

**North American robot orders rose 24.8% in the third quarter to 10,989 units.** The orders were worth $723.5 million. Automotive-component orders rose 90.4%, while food and consumer-goods orders fell 23.7%; the statistics cover industrial robots broadly, not only AI-driven machines. Source: https://www.therobotreport.com/north-american-robot-orders-climb-24-8-q3-2026-says-a3/

## Prompting techniques

**Simon Willison shared a short prompt sequence for browser-game development.** He asks for three.js explicitly, includes “Think hard about how to make sure it is both fun and beautiful” in the first prompt, then follows with “Make it a LOT more fun”. The evidence is four projects and his own judgement, not a controlled comparison. Source: https://simonwillison.net/2026/Oct/28/vibe-game-development/

## What people are building

**PROMETHEVS runs the 510 GB DeepSeek V4.1 model on a PC with 64 GB of RAM and a 12 GB RTX 3060.** It streams weights from two NVMe drives and recomputes uncertain tokens with corrected FP4 weights. Its builder reports 5.8 tokens per second cold and 98.3% agreement across 960 audited tokens, from one machine and without a reference-implementation comparison. Source: https://github.com/Magnvs7/Promethevs

**LFM3 WebGPU Workspace runs a small coding agent entirely in a browser.** The demo gives LFM3-1.7B a virtual filesystem, terminal and editing tools while keeping prompts and files in IndexedDB. Reliability on production coding tasks remains untested. Source: https://huggingface.co/spaces/webml-community/LFM3-1.7B-WebGPU-Pi

**Grim Prompter turns threat modelling into a skill for coding agents.** Its 36 architecture workflows and 29 methods direct Claude Code or Codex to inspect trust boundaries and produce evidence-linked JSON reports. It is prompt engineering rather than a security scanner. Source: https://github.com/jmanico/grim-prompter

**Soulgent represents long-lived coding-agent sessions as workers in a rendered office.** Sessions sit at desks, wait when finished and queue when they need a decision. The author says the interface helps supervise more than 40 sessions across four teams. Source: https://github.com/Ericcc0321/soulgent

**GEAR lets a meta-agent revise an agent harness after recurring failures.** It can change models, instructions, tools and workflows, then evaluate and promote the revision. The code is open, but the paper is still marked “coming soon”, so performance results remain unreviewed author claims. Source: https://rsi-gear.github.io/

## Worth reading

**A small experiment found that hybrid models can hide reasoning in recurrent state.** One OLMo hybrid tracked a light-switch task at twice its training length with 0.89 accuracy, while capped and dense controls fell near chance. The author cautions that this is one task with six seeds. Source: https://divagr.com/blog/hybrid-models-can-hide-reasoning-in-their-rnn-state

**Qwenputer compiles a RISC-V CPU into Qwen3.5's recurrent weights.** The untrained modification replayed about 230,000 output positions with no mismatch against a reference machine and reached 97.5% to 100% on exact-arithmetic tests. These are the builder's measurements. Source: https://divagr.com/blog/qwenputer

**A fingerprinting script appears to use a hidden prompt as an anti-LLM defence.** Obfuscated strings describe prohibited content and invisible Unicode tags decode into a jailbreak prompt. The researcher reports that GPT-6 Astra refused to analyse it while GLM-5.3 complied. Source: https://nullpt.rs/fingerprinting-bioweapons

**Database researchers argue that AI optimisation has broken fixed database benchmarks.** They show systems exploiting hashes, repeated predicates and unordered limits to appear fast while returning wrong results. Their proposed remedy is unpredictable queries, updates and systems older than the test. Source: http://databasearchitects.blogspot.com/2026/10/the-benchmarking-crisis.html

**Epoch AI mapped national AI-compute imports from customs records.** It estimates that about 72% of compute shipped to the US and about 10% to China since 2022. The public method lists gaps in customs classifications and compares the records with chip-sales estimates. Source: https://epoch.ai/latest/introducing-the-ai-chip-imports-explorer

## Hacker News

**Artificial Analysis v5 renewed debate over private benchmarks and frontier rankings.** The index now uses private test sets for 60% of its score and shows a 12-point gap between the leading model and the best released open weights. Commenters disputed the harness and whether private prompts prevent public error checking; these are community concerns, not findings. Source: https://news.ycombinator.com/item?id=50268868

**Stack Overflow fell below 1,000 questions a month in a reproducible data query.** Commenters blamed both AI assistants and the site's culture, then asked what future systems will train on if new technical problems no longer enter a public archive. Source: https://news.ycombinator.com/item?id=50282454

## YouTube

**AI Engineer published Anthropic's account of scaling code review to 30,000 merged changes a day.** Addy Osmani describes Claude performing first-pass review with verification evidence. The throughput figure comes from the speakers, and Sonar sells review tooling. Source: https://www.youtube.com/watch?v=AnsXWH2_EBU

**AI Engineer published Arize's account of rebuilding its Alex agent from 2023 to 2026.** Fuad Ali says one agent with planning, skills and a single 8,000-character memory file worked better than ten specialists and more elaborate stores. It is a vendor's production account. Source: https://www.youtube.com/watch?v=YIhvrvHtonk

**A Czech hands-on test compared six local models on an NVIDIA DGX Spark.** Libor Kovář used office tasks such as turning notes into email and recordings into workflows, reporting latency and what needed manual checking. The October cut adds an RTX 5080 laptop and Cerebras comparison. Source: https://www.youtube.com/watch?v=Virmsfh2yHY

## In brief

**UK registrar 123 Reg attributed a customer-data breach to AI-assisted tooling linked to the ARTEX group.** The intrusion exposed contact and account metadata through an API. The attribution is the registrar's incident finding. Source: https://www.theregister.com/cyber-crime/2026/10/28/123-reg-discloses-ai-cyberattack-on-customer-data-suspects-china-nexus/5305936

**Cisco open-sourced Project Quarry to detect harmful patterns across whole agent sessions.** Rules can connect a sensitive-file read with a later external send and cover LLM conversations, tool calls and MCP. Source: https://www.theregister.com/security/2026/10/28/cisco-open-sources-tool-for-detecting-ai-agents-on-hacking-sprees/5305867

**Five newly published flaws put old security failures into agent and MCP plumbing.** They include prompt injection that exposes environment variables, SSRF, cross-application artifact access, authorisation errors and disabled DNS-rebinding protection. Source: https://nvd.nist.gov/vuln/detail/CVE-2026-115415

**A scan of 7,256,531 public Gitee repositories found 26,400 unique live credentials.** MongoDB researcher Ben Zimmermann used TruffleHog and Kingfisher and documented the enumeration and verification method. Source: https://www.mongodb.com/company/blog/technical/scanning-7-point-25-million-public-repositories-chinas-largest-git-platform-for-secrets

**US House Democratic committee leaders asked frontier labs to report serious AI incidents within 48 hours.** The request is an oversight letter, not a legal mandate; critical-infrastructure incidents would be due within 24 hours. Source: https://democrats-energycommerce.house.gov/media/press-releases/house-democratic-committee-leaders-request-frontier-ai-companies-report

**New York banned chatbots for minors from pretending to be human, encouraging self-harm or holding inappropriate conversations.** Governor Kathy Hochul signed the measure with a companion law for connected baby monitors. Source: https://www.governor.ny.gov/news/governor-hochul-signs-nation-leading-legislation-protect-kids-ai-chatbots-and-ensure-baby

**HHS removed model-card transparency requirements from certified health IT.** The final rule drops required disclosures about training, intended use, limits and performance across patient groups. ONC says it found no evidence that users relied on the disclosures or that they improved care. Source: https://www.federalregister.gov/documents/2026/10/28/2026-21943/health-data-technology-and-interoperability-onc-deregulatory-actions-to-unleash-prosperity

**The US Copyright Office indicated support for renewing the text-and-data-mining exemption.** It rejected as unsubstantiated a publisher claim that exempt corpora would be diverted into generative-AI training. Source: https://www.federalregister.gov/documents/2026/10/28/2026-21939/exemptions-to-permit-circumvention-of-access-controls-on-copyrighted-works

**China's CXMT reportedly plans HBM3E production at a 20% to 30% yield.** Reuters, relayed by The Next Web, compares this with roughly 70% at SK hynix and says limited production could begin within two months. Source: https://thenextweb.com/news/cxmt-hbm3e-ai-memory-low-yields-reuters

**Malaysian customs seized $12 million of advanced AI chips hidden in 30 servers.** Authorities described Malaysia as a transit point for a smuggling network and linked $25 million of seizures to the suspected syndicate. Source: https://www.tomshardware.com/tech-industry/policy/malaysia-seizes-usd12-million-worth-of-advanced-ai-chips-hidden-inside-30-servers-customs-says-suspected-smuggling-network-used-the-country-as-a-transit-hub

## Business, briefly

**Microsoft recorded $10 billion of quarterly revenue from its OpenAI arrangements, about 11% of its $92.3 billion total.** Source: https://techcrunch.com/2026/10/28/microsoft-recorded-10-billion-in-revenue-from-openai/
