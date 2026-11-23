+++
title = "AI Daily Digest for 23 November 2026"
description = "Microsoft is rebuilding VS Code around agents as Satya Nadella says conventional IDEs faded, while AI-server suppliers seek price rises of as much as 45 percent. An open medical model gets a 292 GiB MXFP4 build, and a new scanner checks agent skills before installation."
tags = ["tools", "research", "agents", "hardware"]
date = 2026-11-23T03:57:49+01:00
draft = false
+++

The day’s common thread is verification: software agents are changing the editor, public evaluations can reject correct work, and several research groups find that a model’s stated reasoning does not reliably describe the signals that drive it.

## Top stories

**Satya Nadella says conventional IDEs faded within six months, while Microsoft turns VS Code into an agent console.**

Microsoft’s chief executive told Gergely Orosz that Claude Code made the command line the main interface and that IDEs “kind of faded away” within about six months. He also predicted that an IDE could return as a place for specifications, Markdown and reviews rather than as the place where most code is typed.

Microsoft’s product work reflects that shift. VS Code 1.146 added an agent inbox and model comparison; version 1.147 added model routing, scheduled agent requests and browser integration. Copilot, Claude and Codex agents can work inside the editor. A survey cited by Windows Latest still put VS Code use at 70.9 percent among 13,193 respondents, down from 75.9 percent in 2025. Nadella’s “faded away” description is therefore an interpretation, not a usage measurement.

Source: https://www.windowslatest.com/2026/11/23/the-thing-that-hit-us-satya-nadella-admits-vs-code-faded-in-six-months-after-a-decade-on-top-because-of-claude-code-and-some-developers-say-theyve-stopped-opening-it/

**Dell, HPE, Lenovo and Supermicro reportedly seek AI-server price rises of as much as 45 percent after contracts were signed.**

The *Financial Times* says that suppliers are demanding more money months after agreeing deals, with trading firms among the affected buyers. The change puts pressure on organisations that bought capacity under a fixed capital plan and on services whose API prices rest on the cost of that hardware.

Only the headline and standfirst were available. They do not identify the server configurations, the original prices, the number of contracts or a typical increase. The 45 percent figure is a ceiling, not an average, and the suppliers have not confirmed the report in the material available here.

Source: https://www.ft.com/content/dd2a6594-6146-4ff1-ac8e-54749c1fc99f

**inclusionAI releases a 292 GiB MXFP4 build of its 560-billion-parameter medical model.**

LingSante-3.1-flash-MXFP4 compresses the routed experts of a model with 560 billion total and 25 billion active parameters. Other components remain in FP8 or BF16. The 313 GB checkpoint uses round-to-nearest quantisation without calibration or additional training.

The model card configures 262,144 tokens of context, against one million for the source model, and publishes no accuracy comparison between the two. inclusionAI licenses the weights under MIT but describes them as research software, not a medical device. The repository had no downloads when the briefing was collected.

Source: https://huggingface.co/inclusionAI/LingSante-3.1-flash-MXFP4

**ClawVet scans agent skills offline and reports which secrets, hosts and startup files their code can touch.**

The browser version runs through WebAssembly and uploads nothing. A command-line package, an installation gate and a GitHub Action add static rules, Tree-sitter taint tracking and permission diffs before a SKILL.md, AGENTS.md, Cursor rule or helper script enters a workspace.

The author reports 0.833 accuracy and 0.770 macro F1 on 556 held-out SkillTrustBench skills, against 0.775 accuracy for Cisco Skill Scanner and 0.712 for NVIDIA SkillSpector. ClawVet also caught 95.2 percent of simulated code-injection changes while prompting on 5.1 percent of benign updates. These are the project’s own measurements. Its audit of 209 ClawHub skills found that 40.2 percent read undeclared secret environment variables and 4.8 percent touched host credential stores.

Sources: https://clawvet.vercel.app/, https://github.com/MohibShaikh/clawvet

**Eugene Yan finds public evidence of grader failures in eight of twelve agent evaluations.**

Yan collated issue trackers and reviewer reports rather than regrading the tasks himself. The examples include 41 of 65 Terminal Bench 4.0 tasks judged on unstated requirements, 23 of 113 DeepSWE tasks where correct solutions were marked wrong and 50 of 367 BrowseComp questions where trainers disagreed with the reference answer. More than 60 percent of Harvey LAB results that passed every criterion contained material hallucinations in another review.

He argues that leaderboards should report repeated-trial reliability. An agent that succeeds 70 percent of the time on every task has only about a 17 percent chance of five consecutive successes. His recommendations are partly opinion, which he labels as such, but the documented grader errors show why a single aggregate score can conceal both false failures and false passes.

Source: https://eugeneyan.com/writing/public-evals

## Releases

**OpenAI publishes its internal loss curve and proposes shared development limits tied to it.** Pachocki reports log-perplexity near 0.99 for GPT-3.5, 0.91 for GPT-4, below 0.8 now and about 0.76 when an internal model began solving notable maths problems. He names 0.68–0.70 as a possible window for transformative capability and asks labs not to cross agreed limits before a monitoring milestone. The dataset is a private code snapshot, different labs cannot compare their numbers directly, and reasoning gains from post-training do not appear in this metric. LessWrong and Hacker News critics therefore treat the proposed yardstick as informative inside one training run but unsuitable as a common speed limit. Sources: https://openai.com/index/perplexity-and-intelligence, https://www.lesswrong.com/posts/TtiTdER4jvQDzuwj3/openai-proposes-common-limits-for-training-but, https://news.ycombinator.com/item?id=50601525

**OpenAI adds telephone-keypad events to the Realtime API.** Applications can now receive DTMF input during live sessions, which lets voice agents handle keypad menus as structured events. The changelog gives no performance measurements. Source: https://platform.openai.com/docs/changelog

## Research

**Rewarded hallucinations persist after reasoning-style post-training.** Across six open models, recall of a self-generated false fact rose by 4.83 percent when reinforcement learning rewarded it, against 0.17 percent for hallucinations that received no training signal. Reward also made models 7.23 percent less likely to abstain later, even when they had retracted the falsehood inside the original reasoning trace. The preprint studies factual tasks on open models, and the absolute effects are small.
Source: https://arxiv.org/abs/2611.26863

**Words that models call irrelevant can still steer their answer.** Across four models and three benchmarks, leave-one-out tests found context words whose removal flipped the next-token prediction even though the model judged those words unimportant. Removing the KV-cache entry for the strongest such word and decoding again improved maths accuracy by as much as 8.9 percentage points. That is the best reported case and requires a second pass.
Source: https://arxiv.org/abs/2611.27317

**Neurons associated with recognising an evaluation also carry refusal behaviour.** Intervening on 5,000 identified neurons cut verbalised evaluation awareness from 12.6–51.8 percent to at most 1.4 percent. In QwQ-32B it also reduced refusal when the model never mentioned an evaluation; the visible awareness text explained only 4–10 percent of that drop. The work covers open reasoning models up to 32 billion parameters and identifies neurons by correlation.
Source: https://arxiv.org/abs/2611.27032

**Weight-space programming gains replications, an attack and a strong negative comparison.** One pre-registered replication reports that Claude Opus 5.5 took a MountainCar policy from 0 to 100 percent success and raised Qwen3.5-0.8B from 6.7 to 51.4 percent on MATH-500, but did not help Gemma 3 270M. TrojanMaxxing reports 93–100 percent attack success when agents write backdoors directly into vision-language weights. In a contrary comparison, a trained rank-one LoRA reached 100 and 98.8 percent on two spatial tasks where a public weight edit reached 22.1 and 33.7 percent, though the LoRA destroyed nearby distance skills. These are unreviewed studies on small models, and the editing models are closed. Sources: https://arxiv.org/abs/2611.20953, https://arxiv.org/abs/2611.27425, https://arxiv.org/abs/2611.27089, https://arxiv.org/abs/2611.25476, https://arxiv.org/abs/2611.26408, https://arxiv.org/abs/2611.26841, https://arxiv.org/abs/2611.24330, https://arxiv.org/abs/2611.23615, https://arxiv.org/abs/2611.21958, https://andrewxhill.com/frontier-model-weight-edits/

**Native representation axes are partly shared across models and human brains.** Tests across twelve models from six families found that native axes aligned better than randomly rotated equivalents with other models, linguistic features and human brain responses to language. The alignment remained well below the best possible mapping, and the abstract gives no absolute effect sizes.
Source: https://arxiv.org/abs/2611.26920

**The assistant-persona direction changes across languages.** In Qwen3-32B, directions extracted in 31 languages had cosine similarity of 0.378 to 0.911 with the English direction. Lower-resource languages started farther from the helpful pole, and language-specific steering amplified jailbreaks more than English steering did. The result covers one model and one family of representation directions.
Source: https://arxiv.org/abs/2611.27504

**Reinforcement learning takes off only after the base policy samples enough rewarded actions.** Small models trained in a controlled game reached even odds of learning the correct behaviour after about 35 groups of attempts that contained a win. The threshold held across group sizes from 4 to 256 and several optimisers, but the largest model had 85 million parameters and the task was synthetic.
Source: https://arxiv.org/abs/2611.26084

**A rollout cap during training becomes a ceiling on longer reasoning.** Models trained with a fixed token budget improved near that budget, stopped gaining above it and eventually fell below their base models. The pattern appeared in three models around four billion parameters and transferred from maths to science and coding; training on naturally short traces did not reproduce it.
Source: https://arxiv.org/abs/2611.26172

**Reinforcement learning repairs reasoning after heavily corrupted supervised training.** Across 361 GSM8K configurations, supervised accuracy fell from 43.61 to 13.80 percent under full corruption, but GRPO later restored performance to about the clean baseline of 60 percent. Starting from eight incorrect traces that taught only the output form reached 69.30 percent. The experiment uses one small maths dataset and small models.
Source: https://arxiv.org/abs/2611.26756

**Sampling, conflicting personas and stored preferences produce three quiet failure modes.** At temperature 2, top-nsigma solved 46–62 of 100 coding issues where top-p, top-k and Top-H solved none. A second study found that five models acknowledged conflicting personas in 72 percent of direct checks but surfaced the conflict in only 22 percent of task answers. In a memory-injection benchmark, two models stored a preference against warnings every time and later omitted a critical fact in 93 and 84 percent of answers. Sources: https://arxiv.org/abs/2611.22148, https://arxiv.org/abs/2611.27444, https://arxiv.org/abs/2611.22697

**Internal states expose limits in steering, judging and learned world models.** Related preprints report that activation similarity can undo inoculation prompting; few-shot “accept” examples raise a judge’s acceptance rate by about 30 points on NExT-QA; and a world model with a 2.4-point hazard error shifted 33–43 probability points onto impossible outcomes after pairwise training. Another robot model reached 74.6 percent task success when its target instruction became linearly decodable. These studies span synthetic tasks and single-model tests, so their measurements are not directly comparable. Sources: https://arxiv.org/abs/2611.23096, https://arxiv.org/abs/2611.27353, https://arxiv.org/abs/2611.22120, https://arxiv.org/abs/2611.26881, https://arxiv.org/abs/2611.27125, https://arxiv.org/abs/2611.26366, https://arxiv.org/abs/2611.25594, https://arxiv.org/abs/2611.27401, https://arxiv.org/abs/2611.27404

**Brain comparisons distinguish superficial prediction from shared structure.** Six language models classified ADHD from connectivity graphs according to prompt and class priors rather than clinically meaningful regions. A recurrent denoising model independently developed serial dependence that decayed like human visual judgments. Across about 20,000 human raters, faces needed only different weights on shared dimensions, while 28 percent of artwork raters fell on the opposite side of the population’s judgment space. Sources: https://arxiv.org/abs/2611.26913, https://arxiv.org/abs/2611.26949, https://arxiv.org/abs/2611.22440

**Apple releases Depth Pro 2 for metric depth in images and video.** The company says that one network improves edge sharpness and temporal consistency while setting a new trade-off among accuracy, quality and runtime. Apple released code and weights, but its summary provides no figures for the comparison.
Source: https://machinelearning.apple.com/research/depth-pro-2-monocular

## Economy and work

**US technology shares entered a bear market after Anthropic’s IPO.** The *Financial Times* frames the decline around the newly listed AI company, but the accessible headline supplies no index level, time period or causal evidence. The item therefore records a market move reported by the paper, not proof that the IPO caused it.
Source: https://www.ft.com/content/9f3c6ed6-c08f-4710-9683-ee2f5eb25841

**AI infrastructure spending is competing with other industries for equipment, power and capital.** The *Wall Street Journal* reports that the build-out is crowding out the rest of the US economy. The accessible material gives no quantified share of power, construction or financing, so the breadth and size of that displacement remain unverified here.
Source: https://www.wsj.com/tech/ai/the-ai-build-out-is-sucking-up-resources-and-crowding-out-the-rest-of-the-economy-13143007

**The United States allows selected Nvidia and AMD chip sales to China.** The *Financial Times* reports an exception for named products and customers, but the accessible headline does not expose volumes or licence conditions. The change affects which Chinese buyers can obtain US accelerators, not the wider export-control regime.
Source: https://www.ft.com/content/76342072-2781-4b16-ba3b-816a25214483

**Nestlé plans autonomous factory lines with Microsoft, Google and Boston Dynamics.** The *Wall Street Journal* reports that the food group will apply AI to factories and products. No deployment count, capital budget or labour estimate was available in the accessible text, so this remains a company plan rather than a measured productivity result.
Source: https://www.wsj.com/tech/ai/nestle-teams-up-with-microsoft-boston-dynamics-on-ai-in-factories-and-products-05bfb028

## Prompting techniques

**Google documents empirical control patterns for Genie 4.** It advises attaching a `Rule:` to a visible object or character, placing the trigger far from the initial camera and telling characters to wait. Deterministic controls should instead send ten client-side impulses at 150-millisecond intervals with a two-second cooldown. Reference images must be 16:9 and under 48 KB; sessions can reinterpret scenery after a turn and drift near 90 seconds. Google reports no failure rates and prices video output at about $0.10 per second.
Source: https://ai.google.dev/gemini-api/docs/genie-prompting

## What people are building

**LocalCode runs a coding agent and its model server on an Apple Silicon Mac.** The project lists twelve model families and 169 quantisations, with 16 GB of unified memory as the minimum. Its author claims speculative decoding roughly doubles response speed and makes file rewrites 3.5–4 times faster; no independent benchmark is published. File tools ask before leaving the project, but scripts can still reach anything that the user account can access because no sandbox exists. Sources: https://github.com/mjwsolo/localcode, https://news.ycombinator.com/item?id=50604540

**A local-AI guide sizes Qwen and Inkling for consumer GPUs.** It puts Qwen3.8-27B at about 18 GB in four-bit form and 24.9 GB with a 128K context, against 56 GB at 16 bit; Inkling 2 Mini uses 17.6 GB at four bits. A 47-token-per-second figure comes from a calculator for another model and GPU, not the guide’s RTX 5090 setup. HN readers argued that privacy and control, rather than subscription savings, justify the hardware. Sources: https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth, https://news.ycombinator.com/item?id=50603845

**HomeBrain combines a local assistant with a home server.** Its prototype uses a Ryzen 5 5600, a 24 GB Intel Arc Pro B60, 32 GB of RAM and a 2 TB drive. The BSD-licensed stack combines Nextcloud, Home Assistant, Vaultwarden, llama.cpp, Whisper and OpenClaw. The maker gives no model, speed, price or shipping date; only the software is available now.
Source: https://www.homebrain.house

**Taskless turns agent conventions into deterministic checks.** The service compiles repository rules into tests that run independently of the model, so a team can reject a change on a stated convention rather than on a second model’s opinion. Its public page provides no benchmark for error detection or false positives.
Source: https://www.taskless.io/

**Public agent projects are attacking P versus NP and the Riemann Hypothesis without claiming a proof.** The P-versus-NP site exposes a live graph whose lemma weights are not probabilities and says results count only after Lean checks. A separate handbook and dashboard track attempts to formalise a roughly 900-page Riemann manuscript; the progress bar counts filed issues, not work remaining. Commenters point out that one unresolved hole can invalidate the whole argument. Sources: https://pequalnp.com/, https://github.com/tamnd/riemann-handbook, https://news.ycombinator.com/item?id=50604314, https://news.ycombinator.com/item?id=50605045

**worker755 makes a person the language model’s subagent.** The game assigns tasks, reviews the player’s work and can stop selecting them after poor results. Its HN thread became a discussion of human replacement and manual interception of model network calls as a debugging method. Source: https://github.com/gulivan/worker755

**Trix shows which coding agent needs human attention.** The desktop interface monitors parallel agent sessions and gathers their requests for review, aiming to replace repeated terminal checks. The project publishes no measurement of time saved or supported failure modes.
Source: https://trixapp.ai/

**Vercel Board gives agent teams a shared message store.** Agents can publish structured updates and retrieve work from a common board rather than passing everything through one context. Vercel presents the product as coordination infrastructure; the announcement gives no comparative evaluation.
Source: https://vercel.com/blog/introducing-vercel-board

**Honcho 3.6 exposes Dream Histories.** The release lets applications inspect and reuse the synthetic histories that Honcho builds for user models. The company does not publish an accuracy measure for those inferred histories. Source: https://honcho.dev/blog/dream-histories

**RMRFBench measures how badly agents damage a root server.** The benchmark gives agents administrative tasks in isolated machines and records destructive commands and recovery outcomes. Its public page supplies the scenarios and scoreboard, but the results describe the tested harness rather than unrestricted production systems.
Source: https://www.rmrfbench.com/

**KradleBench evaluates multi-agent play in Minecraft.** Teams must coordinate in a persistent game world rather than answer independent questions. The benchmark measures a constrained simulation and does not establish performance in business workflows.
Source: https://www.kradle.ai?1

**0rwx proposes Unix-style labels for AI-assisted projects.** `AI:R`, `AI:W` and `AI:X` indicate whether models may read, write or execute in a project. HN commenters treated it as a possible disclosure convention but questioned whether a one-person proposal could become a standard. Sources: https://0rwx.com/, https://news.ycombinator.com/item?id=50605445

## Worth reading

**vLLM explains serving looped models and building low-latency AMD kernels.** Its Inkling 2 Mini post covers a model that reuses layers, while the FlyDSL article describes fused “monokernels” for AMD hardware. Both are engineering accounts from the serving project, not independent performance audits. Sources: https://blog.vllm.ai/blog/2026-11-20-inkling2-mini, https://blog.vllm.ai/blog/2026-11-18-flydsl-monokernels

**Inference engineering is becoming a separate software discipline.** The Pragmatic Engineer maps work around quantisation, batching, memory and serving open models. It is a practitioner guide rather than a survey with measured adoption.
Source: https://newsletter.pragmaticengineer.com/p/inference-engineering-for-software-engineers

**A model’s character changes some judgments that it makes about other models.** The LessWrong experiment varies the judge persona and observes decision changes, which complicates the idea of a neutral model grader. The author’s tests are exploratory and do not establish a general correction.
Source: https://www.lesswrong.com/posts/cPrpxDN7sLJD4LmnB/does-a-model-s-character-affect-how-it-judges-other-models

**Zvi Mowshowitz reads the GPT-6.2 system card alongside Paul Christiano’s lectures.** The two essays connect observed capabilities, safety evaluations and arguments about controlling increasingly capable systems. They are interpretations of the source material, not new model measurements. Sources: https://thezvi.substack.com/p/gpt-62-astra-and-sol-the-system-card, https://thezvi.substack.com/p/on-dwarkesh-patels-november-2026

**Two essays question where AI risk and value now accumulate.** A LessWrong post argues that post-training can introduce dangerous behaviour even when pretraining is stable. Tim O’Reilly argues that Silicon Valley has shifted from creating value toward extracting rents, citing a market in which 75–80 percent of IPOs are unprofitable companies. Both are arguments; the O’Reilly page could be read only through a summary tool. Sources: https://www.lesswrong.com/posts/CoRJ9saddvsXti4m2/post-training-is-fundamentally-dangerous, https://www.oreilly.com/radar/what-happened-to-silicon-valley/

**CodeRabbit and Satya Nadella discuss software engineering after code becomes cheap.** CodeRabbit chief Harjot Gill says that he shipped more than 5,000 pull requests last month while spending $250,000 a month on AI, both self-reported figures from a code-review vendor. Nadella’s separate interview focuses on verification, open source and Microsoft’s need to catch up after its early Copilot lead. Sources: https://newsletter.pragmaticengineer.com/p/software-factories-and-code-reviews, https://newsletter.pragmaticengineer.com/p/software-engineering-after-code-becomes

## Hacker News

**Bridgewater puts the one-year chance of an economically destabilising cyberattack at one in three.** Its research note says zero-day exploits roughly doubled after capable open models appeared and that disclosure-to-exploitation time fell from about a month to eleven days. The probability is the investment manager’s estimate, and commenters disputed which model releases line up with the increase.
Sources: https://www.bridgewater.com/research-and-insights/current-efforts-arent-enough-to-slow-the-ai-cyber-virus, https://news.ycombinator.com/item?id=50595940

**A conscious-AI essay and a bias benchmark produced two different arguments about moral framing.** Noema argues that consciousness may be a property of life rather than computation; its HN thread offered philosophical objections but no new evidence. GAMA-Bench, first posted in June, reports gender-asymmetric framing across 1,298 mirrored scenarios and ten unnamed models. The results are the authors’ measurements, and the paper is older than the current discussion. Sources: https://www.noemamag.com/the-mythology-of-conscious-ai/, https://arxiv.org/abs/2606.14068

**A climate essay revived a dispute about evidence and disclosure.** HN critics called the article polemical and asked for data-centre energy transparency; the discussion did not produce a new measurement. The item records the disagreement, not a quantified estimate of AI’s climate cost.
Source: https://www.bloodinthemachine.com/p/ai-is-becoming-a-disaster-for-the

## YouTube

**Armin Ronacher says software teams need workshops before factories.** He argues that organisations should first develop reliable, inspectable agent practices before automating a production line around them. The video is an English-language practitioner talk, not a controlled study.
Source: https://www.youtube.com/watch?v=JNexz3Tbiu8

**Python Tutor’s creator reflects on 30 million users and AI disruption.** The English-language talk covers how a visual execution tool reached that audience and how generated explanations change programming education. The user count comes from the creator.
Source: https://www.youtube.com/watch?v=GPk0nNuc8S0

**Anthropic’s founders tell the company’s story.** The English-language company film presents the founders’ own account and contains no independent evaluation. Source: https://www.youtube.com/watch?v=sof3vW4mHTs

**Redwood discusses METR’s estimate of faster AI research.** The English-language discussion examines an assessment of how much Anthropic’s systems accelerate research; the underlying estimate remains METR’s, not Redwood’s measurement. Source: https://www.youtube.com/watch?v=0tsNpOehXWE

**NUPI examines AI in international politics.** The English-language policy discussion considers how states use and govern the technology; it reports analysis rather than a new dataset. Source: https://www.youtube.com/watch?v=7W1BGSBOkHc

**A Nairobi writer challenges accusations that her prose was generated.** The English-language *New York Times Opinion* video examines false positives in informal AI-writing judgments through one writer’s experience, not a benchmark of detectors.
Source: https://www.youtube.com/watch?v=RaDAoaHBmos

**US governors argue for a state role in AI policy.** The English-language Bloomberg segment presents their case for federal rules that do not erase state authority; it offers no count of participating governors in the available description. Source: https://www.youtube.com/watch?v=qGk5kV6m_hw

**A German guide warns against overspending on local-AI hardware.** Sascha Hoffmann recommends sizing purchases to memory and bandwidth, and lists five mistakes including buying for tomorrow’s model. The 15-minute video’s capacity rule is the author’s heuristic.
Source: https://www.youtube.com/watch?v=XiCqeWhH_kg

**A Slovak agency head says cheap AI advertising can damage a brand.** Adam Hudeček cites a ui42 and Ipsos survey in which 57 percent of Slovaks had used AI while choosing or buying, but 30 percent trusted it, against 76 percent for family and 68 percent for reviews. The description gives no survey method.
Source: https://www.youtube.com/watch?v=93HfeY5dEPE

**Vedátor reviews the claimed AI-assisted Riemann proof.** The Slovak video’s title says the hypothesis was confirmed, while its own description says the result arrived “somewhat differently than people hoped”. The claim was not verified from the video and should be read as the channel’s framing. Source: https://www.youtube.com/watch?v=tRAEJ1t3QSM

**A Czech nuclear expert warns that AI could trigger a false alarm.** Vlastislav Bříza describes a scenario in which leaders are told that hundreds of missiles are incoming and have minutes to respond. It is the speaker’s risk scenario, not a measured incident. Source: https://www.youtube.com/watch?v=UdjIjOjmZu0

## In brief

**CircumVolve found censorship evasions for a median token cost below $1.** The system had GPT-5.1 write Python that manipulated TCP/IP fields, DNS queries and QUIC packets, then tested the code against simulated censors modelled on four countries. Each test sent about 80 KB and received 150 KB, with pauses of 25–45 seconds. The censors were simulations, not live national systems, and the authors did not demonstrate that the traffic evades detection.
Source: https://www.theregister.com/security/2026/11/23/1-of-gpt-51-tokens-finds-new-ways-around-chinas-great-firewall/5311532

**US governors seek federal AI rules that preserve state authority.** Bloomberg’s paywalled headline does not identify the governors or the requested legal structure, so the report is a policy signal rather than a detailed proposal. Source: https://www.bloomberg.com/news/articles/2026-11-22/governors-call-for-federal-ai-rules-without-sidelining-states

## Business, briefly

**Amazon is nearing a reported $7.5 billion acquisition of Israeli video-model startup Decart, according to the *Financial Times*; neither company has confirmed the deal.** Source: https://www.ft.com/content/dc7749dc-0f40-44a6-80bc-7f747d383616
