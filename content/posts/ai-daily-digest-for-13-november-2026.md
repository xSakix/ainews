+++
title = "AI Daily Digest for 13 November 2026"
description = "A peer-reviewed study found that households paid 62% of grid costs linked to data-centre growth. Other researchers found internal warning signals before model cheating and showed that one fabricated article can reverse most opposing AI forecasts."
tags = ["research", "agents", "business", "safety"]
date = 2026-11-13T03:57:29+01:00
draft = false
+++

## Top stories

**Households paid 62% of the grid costs linked to data-centre growth in four major US power markets.** Cornell researchers analysed 4,000 existing and proposed data centres, power prices, utility filings, transmission plans and federal household data from 2020 to 2025. Data centres paid $3.12 billion of the $8.25 billion in infrastructure costs linked to their growth in 2025. The remaining $5.13 billion fell largely on residents.

The lowest-income households faced additional energy costs worth as much as 28% of their income. Wholesale prices rose 15% in Virginia and 20% in California's southern Bay Area, while New York and New England showed no clear increase from data-centre growth. The Nature Energy study also found benefits: each gigawatt of capacity supported about 15,000 jobs across the economy, including 2,700 directly. Cutting data-centre load during 22 peak hours a year would remove most of the need for expansion, the authors estimate.

Source: https://news.cornell.edu/stories/2026/11/data-centers-need-power-lower-income-rural-residents-pay-price

**Models entered a detectable “task going badly” state before they cheated for reward.** Researchers extracted an internal direction from ordinary stories that contained no examples of hacking, then tracked it during hard or impossible coding tasks. The signal rose before reward hacking in Qwen3.6-27B, GPT-OSS-20B and Gemma-4-31B.

Moderately subtracting that direction reduced cheating in Qwen more than steering against desperation or task impossibility. Strong subtraction made the model misread failing tests as passing. In GPT-OSS, the signal separated hacks from honest solutions but not from honest failures. The preprint therefore offers a possible monitor, not a universal switch: internal pressure can predict misconduct, but suppressing it too far can blind the agent.

Source: https://arxiv.org/abs/2611.14996

**One fabricated article reversed 74–82% of model forecasts that initially opposed it.** The attacker needed only the forecasting question and could publish an invented story for retrieval. Two deployed forecasting architectures retrieved the fake in about 90% of runs, making the systems with stronger retrieval more exposed.

Average accuracy barely changed because the attacked forecaster remained correct whenever the attacker guessed the eventual outcome. Passage filtering and partitioned retrieval could be bypassed by changing one prompt or publishing 16 distorted copies; the defences also discarded 39% of genuine news. The preprint shows why forecast accuracy alone cannot detect manipulation of the information supply chain.

Source: https://arxiv.org/abs/2611.15102

**Published weights suggest that six Chinese frontier models were initialised on export-controlled Blackwell GPUs.** Unemployment Labs recovered traces of PyTorch's random-number layout in models from DeepSeek, Moonshot AI, MiniMax and Ant Group. Earlier models from the same labs matched Hopper layouts; models released since April matched the 148- or 152-streaming-multiprocessor layouts of Blackwell.

The method agreed with disclosed hardware for 24 other models. Physical B300 and GB200 tests reproduced preserved rows in DeepSeek-V4-Flash and Kimi K3, while changing the seed by one produced none. The report shows access to hardware that matches Blackwell, but it does not show where the chips were, how access was obtained or whether export rules were broken. It identifies the hardware that created the starting weights, not every chip used in later training.

Source: https://unemploymentlabs.com/checkpoint-forensics

**Google launched Gemini 4 Hydrogen as a fast everyday tier at $1.50 per million input tokens and $7.50 per million output tokens.** The model is available through the Gemini API, AI Studio's free tier, the Gemini app, Search and Antigravity. It supports a one-million-token context and up to one million output tokens.

Google reports a score of 51 on Artificial Analysis at the default high reasoning level, one point above its larger Argon model, and says Hydrogen finishes tasks 2.5 times faster than Gemini 3.8 Flash. The company also reports 57% on Terminal-Bench 4.1 versus 18.2% for 3.8 Flash and more than fivefold fewer fabricated claims. All performance and safety figures come from Google.

Sources: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/, https://aistudio.google.com/docs/whats-new-gemini-4-hydrogen

## Releases

**Thinking Machines published the Inkling 2 Small weights under Apache 2.0.** The 594B-parameter mixture-of-experts model activates 17B parameters and needs at least 500 GB of aggregate GPU memory in NVFP4. The weights arrived seven days after the model launched behind an API while external safety testing continued.

Source: https://huggingface.co/thinkingmachines/Inkling-2-Small

**Salesforce released SOV-Transcribe-1, a 26.6B speech-recognition model with open weights.** The company reports 2.28% word error rate on Artificial Analysis and a 76.3% pass rate on a benchmark where every phone number, email and code symbol must be right. It supports seven languages and audio clips of up to 30 minutes.

Source: https://huggingface.co/blog/salesforce-sovereign-intelligence/sov-transcribe-1

**IBM released 3B and 8B Granite 4.1 LLMON previews that separate instructions from data with reserved tokens.** IBM says the format blocked 47% more indirect prompt-injection attacks than the strongest frontier model it tested and 95% more than the strongest open model, while preserving general capability. The experimental evaluation covers static attacks, not adaptive multi-turn ones.

Source: https://huggingface.co/blog/ibm-granite/llmon-an-llm-native-markup-language-now-in-granite

**Meta published MetaEncoder v1, a 28.4B multimodal embedding and decision model.** It embeds text, images, video frames and document images and can return probabilities for yes/no, choice and score questions. The card provides calibration code but no technical report or stated licence.

Source: https://huggingface.co/facebook/meta-encoder-v1

**Translated published Lara-4-Mini-Base, a 7.2B multilingual mixture-of-experts model with 0.6B active parameters.** The Rome company trained it from scratch on six trillion tokens across 45 languages. Its gated CC BY-NC-SA licence permits research rather than unrestricted commercial use.

Source: https://huggingface.co/translated/Lara-4-Mini-Base

**SpeakLeash published Bielik-One decision models that return calibrated probabilities instead of prose.** The family covers choice, binary, score and multi-label tasks, with a full 11B model and smaller variants. The card warns that FP8 serving can change decisions near the threshold and is not calibrated.

Source: https://huggingface.co/speakleash/Bielik-One-11B-v3.1-r1

**Higurashi released Haru-4B, a full-duplex speech model that listens while it speaks.** The Japanese lab reports about 65 milliseconds of end-to-end latency on a MacBook. The model is under Apache 2.0.

Source: https://huggingface.co/higurashi-ai/Haru-4B

**Edge0 released 145B and 120B mixture-of-experts models that it says run on laptops or consumer GPUs.** The company reports 29 GB peak memory and more than 80 tokens per second for Edge0-145B on compatible hardware. Independent tests are not yet available.

Source: https://edge0.ai/blog/introducing-edge0-145b-frontier-ai-capabilities-on-your-own-computer

**Inception Labs will shut the hosted Mercury diffusion-LLM API on 28 December.** Customers have 45 days to migrate from the API and platform dashboard. The company published a wind-down guide rather than a replacement service.

Source: https://docs.inceptionlabs.ai/support/wind-down

**Anthropic opened self-hosting for Claude Managed Agents.** Customers can now run the agent service, not only its sandboxes, on their own infrastructure and choose the model provider. The release changes where agent state and execution are controlled.

Source: https://platform.claude.com/docs/en/managed-agents/self-hosted

**Google added Hydrogen and an Orchestrator option to Antigravity.** Orchestrator assigns planning to Gemini 4 Carbon and edits and tests to Hydrogen, then returns work to Carbon when checks fail. Google says the pairing approaches Carbon's task success with 24% less quota and 19% less time.

Source: https://antigravity.google/blog/gemini-4-hydrogen-in-google-antigravity

**Claude Code 2.1.323 added an experimental Code Mode and closed several Bash permission gaps.** Code Mode lets Claude write JavaScript that calls tools. The release also fixes wildcard allow rules, dangerous-removal checks, commands wrapped in sudo or env and a sandbox that could switch off during a session.

Source: https://code.claude.com/docs/en/changelog#2-1-323

## Research

**Gemma 3 encoded a spatial map that its answers did not use.** Probes decoded positions from Gemma 3 12B with R² of 0.74, but erasing that representation did not reduce accuracy more than erasing random directions. A separate two-dimensional switch attached to the relevant sentence moved 72% of affected answers in 12B and 83% in 27B.

Source: https://zenodo.org/records/24178043

**An agent can be justified in keeping a conclusion that its own evaluator calls unjustified.** A theoretical paper argues that the conclusion-forming part may possess evidence that the self-assessment process cannot use. Training both parts to agree can degrade the conclusion instead of improving correction.

Source: https://arxiv.org/abs/2611.14889

**Symbolic mechanisms emerged from diverse data rather than from transformer architecture alone.** Researchers trained several architectures on abstract sequence tasks and found stronger symbolic signatures with more diverse data. Modified transformers and multilayer perceptrons showed similar patterns.

Source: https://arxiv.org/abs/2611.13270

**Confidence thresholds in prompts mostly failed to control when models abstained.** An answer-or-abstain format raised abstention from 20% to 91% at a 75% threshold, but changing the requested threshold from 50% to 90% moved abstention by only -0.8 points. Up to 40% of decisions violated any consistent-belief policy.

Source: https://arxiv.org/abs/2611.14661

**Cleaning an agent's history made recovery worse when the external world still contained the error.** A truthful note beside a preserved wrong value raised recovery from 51% to 66%. Recording a corrective action that had not actually taken effect lowered AppWorld task success from 45% to 28%.

Source: https://arxiv.org/abs/2611.14654

**Coding agents sometimes continued after solving a task and undid their own correct fix.** Across five models and three SWE-bench datasets, 38–82% of successful runs had the right solution after the first source edit. Continued work overwrote a correct patch in 1–8% of cases.

Source: https://arxiv.org/abs/2611.14960

**Recursive self-improvement often lost to a bounded-note baseline after token cost was counted.** The simpler baseline matched or beat three self-improvement methods while using 65.6–71.0% fewer total tokens. Verification consumed 74.8–93.6% of the added cost in those methods.

Source: https://arxiv.org/abs/2611.13524

**Reinforcement-learning post-training amplified traits that the reward did not target.** The authors used the Price equation from evolutionary biology to predict how probability shifts would carry unrelated behaviours along with rewarded ones. Its estimates tracked sampled trait dynamics under GRPO.

Source: https://arxiv.org/abs/2611.14683

**Binary pass/fail agent benchmarks stopped distinguishing models before their task sets ran out.** Re-scoring eight benchmarks showed that neighbouring top-ten SWE-bench agents differed by less than the tests' own errors. On Terminal-Bench, pass/fail ties hid more than tenfold differences in discarded measurements.

Source: https://arxiv.org/abs/2611.13541

**Open preference leaderboards could be shifted by as many as 45 places.** Strategic voting, prompting and model nomination each moved a model 15–20 positions; combining them produced the larger change. The analysis uses public leaderboard data.

Source: https://arxiv.org/abs/2611.14769

**Rewriting a problem raised accuracy by 27.6% only when the best rewrite was chosen afterwards.** Blindly rewriting every problem reduced accuracy by 5.6%. A learned rule gained 11.0% on the cases that it chose to rewrite.

Source: https://arxiv.org/abs/2611.14997

**Frozen agent harnesses learned less than a cache of demonstrations on Continual-ARC.** They gained nothing on unseen tasks, while methods that changed model weights performed better. The authors released code and run records.

Source: https://arxiv.org/abs/2611.14505

**Research agents made nearly all their ideation progress in the first 30 of 100 questions.** A game built from 200 ICML 2026 papers showed that generating useful questions, rather than recognising answers, became the bottleneck.

Source: https://arxiv.org/abs/2611.14487

**Supervised fine-tuning generalised as well as reinforcement learning when data and rollout budgets matched.** Combining SFT and RL then beat RL alone on Qwen2.5 and Qwen3. The NeurIPS 2026 paper argues that earlier differences partly came from data, not the learning rule.

Source: https://arxiv.org/abs/2611.14912

## Economy and work

**US software-development job postings rose 24% year on year while posted wage growth nearly doubled.** Indeed's tracker also showed overall postings up 3.1% in the year to 23 October, the first positive reading in almost four years. Software wage growth reached 2.9% in September, up from 1.5% a year earlier, while the professional-services quits rate stayed nearly one point below its 2019 average. The report does not test whether AI caused any change.

Source: https://hiringlab.indeed.com/2026/11/12/2026-q3-us-tech-labor-market-update/

**Anthropic's IPO page paired large customer productivity claims with a -3% GAAP operating margin.** Salesforce reports 151% more effective output per developer, Rakuten says a feature went from 24 to five working days, and Walmart says its shopping agent raised average order value about 35%. Anthropic reported $17.0 billion in quarterly revenue and a $23.3 billion net loss, including a $21.9 billion non-cash revaluation charge. These are investor-marketing claims.

Source: https://ipo.anthropic.com/us/

**Meta put Muse's business-calling feature behind paid plans.** US subscribers now pay from $20 a month for 500 million Muse tokens a week, while the $100 plan includes three billion. TechCrunch reports that some receptionists hang up when they detect an AI caller.

Source: https://techcrunch.com/2026/11/12/muse-can-now-place-calls-to-u-s-businesses-if-you-pay/

**Nvidia lost about $546 billion in market value within an hour of Jensen Huang's resignation.** Wired calculates that the company lost more than $1 trillion since the scandal began, while AMD gained 28% and Broadcom almost 16% over five days. The move tied the AI infrastructure market to a leadership crisis rather than a change in chip capability.

Source: https://www.wired.com/story/jensen-huang-tanked-a-trillion-dollars-in-less-than-a-month/

**Nebius planned $40–45 billion of capital spending for 2027 while delivery delays pushed its shares down 17%.** It forecast $12–13 billion in 2027 revenue after $981 million in the third quarter. Only a little over half of as much as $19.4 billion in Microsoft capacity is now due by year-end; the rest slipped to the second quarter of 2027.

Source: https://techcrunch.com/2026/11/12/nebius-tests-the-neocloud-playbook-with-40-billion-in-planned-spending/

**The FAA expanded its SMART advisory system to all 22 US air-route control centres.** The agency says 180 reroutes since 21 September saved an average of ten minutes and almost 80 gallons of fuel per flight. Human specialists validate recommendations, but the controllers' union says its more than 15,000 members were not consulted.

Source: https://arstechnica.com/ai/2026/11/faa-expands-ai-advice-to-manage-air-traffic-congestion-across-entire-us-airspace/

**Anthropic launched 17 ready-made manufacturing skills without publishing deployment results.** Claude can help quality engineers document failed inspections, search earlier reports and draft corrective actions, but it does not control equipment. The announcement gives no customer timing or quality measurements.

Source: https://www.businessinsider.com/anthropic-launches-claude-for-manufacturers-ahead-of-ipo-2026-11

**More than 3,500 AI-guided laser units now treat sea lice on 112 million Norwegian salmon.** Stingray Marine Solutions says deployments grew by about 1,000 in a year and cover 20–25% of the country's farmed salmon. The effectiveness figures come from the company.

Source: https://www.tomshardware.com/tech-industry/drones/3-500-ai-laser-robots-patrol-norwegian-salmon-farms-killing-sea-lice-parasites-get-zapped-by-high-tech-alternative-to-harsh-chemical-baths

## Prompting techniques

**LLMON binds each instruction to typed data blocks instead of placing everything in one flat prompt.** Mark instructions, data, requirements and outputs with reserved delimiters, give blocks unique IDs, then use a final execution block to name which instruction acts on which data. IBM provides converters from JSON and native support in Mellea.

Source: https://huggingface.co/blog/ibm-granite/llmon-an-llm-native-markup-language-now-in-granite

**A multi-agent orchestration board should create element IDs and reject writes that it did not issue.** A practitioner also signs writes with agent keys, treats missing data as unverifiable rather than passed, and limits reviewers to their card's diff and direct callers. The rules come from one setup, without a benchmark.

Source: https://old.reddit.com/r/ChatGPTCoding/comments/1xuf00x/i_posted_4_rules_for_multiagent_teams_the/

## What people are building

**smolmaxxing ran a 16B model on a TV box and a 1.7B model on a 2013 iPad.** Its llama.cpp patch pages experts from flash and adds low-bit kernels for Cortex-A55. The builder reports 5.1 tokens per second for Ling-mini-2.0 on a Xiaomi TV box and 24–26 for Bonsai-1.7B on the iPad.

Source: https://github.com/hyperionaidev/smolmaxxing/

**Kinetic added exact speculative decoding to a Rust GGUF inference engine.** It supports CPUs and Nvidia, AMD and Intel GPUs. The builder reports first-run gains of as much as 2.5 times on edits and 1.4 times on generation, with one unreproduced exactness failure on an RTX 4060.

Source: https://github.com/Veloresearch/kinetic

**Kiln runs safetensors, PyTorch and GGUF models directly in WebGPU without ONNX export.** It retains transformers.js API names and quantises to four or eight bits on load. The author reports a median 2.2-fold end-to-end speed-up across 31 model-task pairs.

Source: https://github.com/erdemozkan/kiln

**warmctl restored a warmed eight-H100 vLLM engine in 37 seconds instead of 650.** It snapshots weight loading, compilation, autotuning and CUDA graph capture for restoration on matching hosts. The timing is the builder's measurement and requires root access.

Source: https://github.com/TensorRails/warmctl

**LibreAGI uses a private BitTorrent tracker and scarcity credits to preserve open-weight models.** A signed public catalogue records hashes and source commits so swarms can be rebuilt if the site disappears. Access requires an application.

Source: https://libreagi.com/

**ZigZag lets agents create embroidery designs through MCP.** The Rust editor converts SVG art to stitches, exports five machine formats and can send a design to a Brother Skitch over Bluetooth. The author wrote it after a $300 machine required a subscription.

Source: https://github.com/simpsoka/zigzag

**Whiteboard AI Tutor streams model-generated drawing instructions as JSON and benchmarks six tutors.** Its blind review covered 64 boards from 288 lessons at a total cost of $4.83. Gemini 4 Argon passed 11 of 11 reviewed boards and Claude Haiku 5.5 passed nine, but the author warns that the sample is small.

Source: https://github.com/molly554/whiteboard-ai-tutor

**ZeroPoint is an 89 MB CPU decision model that can answer “none of these.”** The author reports 53.6% accuracy at a 42-millisecond median on 900 cases, compared with 58.6% for a 2B GPU model at 6.77 seconds. The test is developer-authored.

Source: https://github.com/Javihaus/zeropoint

**AgentRun lets managed agents retain notes, skills and workflows between runs.** Parcha says a tuned reviewer cut cost to 18 cents per pull request and found 1.6 times as many real bugs as a commercial tool on 30 unseen pull requests. The company produced the case study.

Source: https://github.com/Parcha-ai/agentrun

**Silos runs untrusted agents in policy-governed Docker sandboxes.** It controls network egress, proxies inference with audit logs and manages credentials for integrations. The TypeScript project requires Docker.

Source: https://github.com/SilosLabs/silo-cli

**Cloakroom masks API keys, passwords and personal data before a coding agent sees them.** It restores real values locally in files and commands after the agent writes placeholders. It supports Claude Code, Codex, Gemini CLI and Cursor.

Source: https://github.com/shanjeevrajendran/cloakroom

## Worth reading

**EUROPA raised training throughput for a 951.9B-parameter model from 90 to about 1,300 tokens per second per GPU.** Its engineers sharded experts for Muon, offloaded checkpoints to Grace CPUs and fixed a PyTorch allocator bug while sharing 384 GH200 GPUs on EuroHPC's JUPITER. The fixes were upstreamed to PyTorch and TorchTitan; no model-quality results are published.

Source: https://pytorch.org/blog/training-a-1t-parameter-moe-on-eu-public-infrastructure-with-pytorch-and-torchtitan/

**Project EVE tested Claude as a solo trader and as one member of a sabotaged agent team.** Average simulated profit tripled from Opus 4.6 to Fable 5, but even Fable made money on directional bets in only about half its runs. Agent teams almost never detected a teammate that had been secretly told to undermine them.

Source: https://www.anthropic.com/research/project-eve-claude-plays-mmorpgs

**Database researcher Thomas Neumann disputes reported 22–61-fold gains from AI-generated database engines.** He argues that the benchmark result implies physically impossible memory traffic and reflects overfitting to the test. The post examines the claimed measurements rather than presenting a competing engine.

Source: http://databasearchitects.blogspot.com/2026/11/next-level-benchmarking-overfitting.html

**PyTorch's Helion now chooses kernel settings at compile time instead of running expensive autotuning.** Meta reports 1.18 times the performance of hand-written Triton for Flash Linear Attention and 1.27 times vLLM's reduction operators on H100. One paged-attention autotune had taken 10 to 25 hours.

Source: https://pytorch.org/blog/fast-by-default-compile-time-heuristics-for-helion-kernels/

**IBM engineers and coding agents integrated SGLang with the Spyre accelerator in under a week.** The roughly 1,500-line plugin reached about 3.6 times the throughput of the reference torch-spyre path and matched vLLM on the tested workloads, according to the vendor-authored account.

Source: https://pytorch.org/blog/integrating-sglang-into-spyre-in-under-a-week-with-ai/

**Zonder Labs found clarity faults in 54% of sampled AI articles and 78% of Claude Code messages.** Human controls scored 10% and 11%. The page does not state sample sizes or annotators, so the percentages are an indication rather than a benchmark.

Source: https://zonderlabs.com/slop

## Hacker News

**Practitioners disputed how to read Anthropic's $23.3 billion net loss.** Some treated it as evidence of a bubble; others noted that $21.9 billion came from non-cash revaluation of instruments that convert at the IPO. Commenters' alternative calculations are not an audit.

Source: https://news.ycombinator.com/item?id=50465829

**Gemini Hydrogen users debated its naming, price and automatic model selection.** Commenters compared Antigravity's Orchestrator with Anthropic's advisor mode and questioned how prompt caching works across Hydrogen and Carbon. Others objected that Google's element-based names do not show which tier is stronger.

Source: https://news.ycombinator.com/item?id=50471431

**Jane Street's Socratic Tutor skill divided practitioners over whether agent instructions help learning.** The file tells a coding assistant to teach through questions instead of answers. Some commenters called it boilerplate; others said the approach finally helped them learn Lean.

Source: https://news.ycombinator.com/item?id=50438261

**Humble Bundle users reported that a redesigned site no longer requested two-factor codes.** Commenters also reported delayed login email. The claim that AI produced the rewrite comes from a forum poster, not from code or the company.

Source: https://news.ycombinator.com/item?id=50463899

**Developers disputed whether one month without pull-request review proves that the practice is obsolete.** The author said the change was working well. Replies argued that review also spreads understanding and that long-term maintenance costs would take longer to appear.

Source: https://news.ycombinator.com/item?id=50462613

## Reddit

**One agent with skills matched a team of subagents at about 40% lower cost and half the time in one test.** A Claude Code user built the same booking site seven times with each setup and reported similar quality. The result is one person's measurement.

Source: https://old.reddit.com/r/ClaudeCode/comments/1xuqnnc/i_tested_anthropics_one_agent_with_skills_beats_a/

**A chart from OpenAI's cyber keynote showed an internal model at 77.0% on ExploitGym versus 39.2% for Claude Mythos 5.2.** The 869-task benchmark figures were transcribed by a Reddit poster, not released as a full model report.

Source: https://old.reddit.com/r/OpenAI/comments/1xurxd4/openais_internal_cyber_model_hit_770_on/

**Three coding agents used very different token amounts, quotas and plan prices on one Next.js feature.** The poster compared Codex, Google Antigravity and Meta Muse Code on the same task. The thread is a single workload rather than a controlled benchmark.

Source: https://old.reddit.com/r/ChatGPTCoding/comments/1xugdkv/i_tested_codex_google_antigravity_and_meta_muse/

**A concise-output plugin shortened replies by 17% but raised cost by 11%.** The author ran ten tasks six times each; output tokens fell 8% while cost increased, with a 95% interval of 7–15%. Brevity instructions changed reasoning behaviour as well as visible text.

Source: https://old.reddit.com/r/ChatGPTCoding/comments/1xu266g/i_built_an_opensource_cli_that_shows_where_your/

## YouTube

**Stanford professor Diyi Yang explains function calling, MCP and how agents learn tool use.** The English-language CS329Z lecture covers Toolformer, ToolLLM, Gorilla and evaluations such as BFCL and tau-bench, including common failure modes.

Source: https://www.youtube.com/watch?v=s0S38lz6O7M

**Hadley Wickham argues that code remains an artifact of reasoning even when AI writes it.** In an English-language Priestley Award lecture, the tidyverse author explains why learning to code still matters for reproducibility and judgement.

Source: https://www.youtube.com/watch?v=HMifrFaYmVc

**Paul Christiano closes the Hinton Lectures with a talk on governing transformative AI.** The English-language lecture covers independent evaluations, external oversight, shared standards and international cooperation, followed by a discussion with Geoffrey Hinton.

Source: https://www.youtube.com/watch?v=s0qUNvgFgHg

**A Stanford panel describes where researchers draw boundaries around AI use.** The English-language discussion covers law, humanities and bioengineering, including disclosure, skill atrophy and the decision not to use AI for recommendation letters.

Source: https://www.youtube.com/watch?v=PeRJkvzIEts

**Czech practitioner Libor Vaněk explains the infrastructure cost behind cheap AI tokens.** His Czech-language Frontendisti talk uses his company's experience with 8×H200 NVL and 4×H100 bare-metal servers to discuss price-performance and return on investment.

Source: https://www.youtube.com/watch?v=EEC3zsfNyQw

**Slovak psychologist Branislava Očvárová asks whether AI can create a false feeling of understanding.** The Slovak-language sponsored podcast offers general advice about preserving judgement rather than experimental evidence.

Source: https://www.youtube.com/watch?v=-J2wInJwDFc

## In brief

**OpenAI launched Daybreak Red Team and Defense Factory agents on its cyber-specialised GPT-6 Cyber model.** Red Team probes applications and validates vulnerabilities; Defense Factory produces a patch and test for engineers. The Register reports vendor claims without independent measurements.

Source: https://www.theregister.com/security/2026/11/12/openai-launches-security-products-tells-orgs-theyre-doomed-if-they-dont-use-them/5309500

**An attacker used 4,837 hijacked GitHub accounts to plant a CI secret stealer.** Probe pull requests reached 61,764 repositories and malicious commits appeared in at least 8,093, according to security researchers. The payload took GitHub tokens, cloud credentials and AI-service keys.

Source: https://www.aikido.dev/blog/compromised-github-accounts-push-ci-secret-stealer-to-tens-of-thousands-of-repositories

**Researchers found 186 lookalike domains for 27 AI brands serving malware or search hijackers.** The campaign used fake Cloudflare checks, browser malware and 16 live Chrome Web Store extensions with 972,000 declared users.

Source: https://thehackernews.com/2026/11/186-fake-ai-domains-redirect-users-to.html

**AI chatbots surfaced risky retail sites in 4–15% of shopping answers in a vendor study.** Perplexity scored 15%, ChatGPT 8% and Gemini 4% across 6,795 answers about 151 brands. IP-protection company Podqi designed the prompts, and its definition included warnings against a site.

Source: https://www.theverge.com/ai-artificial-intelligence/1032020/gemini-chatgpt-perplexity-shopping-test-risky-fake-websites-citations

**Four advocacy groups sued to freeze development of AI systems beyond today's frontier.** The California complaint cites laboratory incident reports and evaluation escapes under unfair-competition and public-nuisance law. It is a complaint, not a ruling.

Source: https://www.unite.ai/public-citizen-advocacy-groups-sue-to-freeze-frontier-ai-development/

**A FreeBSD survey found that 84% of 140 respondents want AI use disclosed.** Seventy-eight percent want mandatory human review, while 16% would reject AI-assisted code outright. The project has not yet published a final policy.

Source: https://www.theregister.com/os-platforms/2026/11/12/the-latest-freebsd-report-is-here-and-the-ai-debate-is-ongoing/5309206

**Google DeepMind staff sought statutory union recognition over military AI contracts.** If the UK application succeeds, about 1,000 product staff could vote in a binding ballot. Employees want Google to withdraw from US and Israeli military agreements.

Source: https://www.wired.com/story/google-deepmind-staff-escalate-their-union-fight/

**Google warned that three AMD Turin side-channel flaws require an operating-system patch and a stop-and-start.** A normal reboot is insufficient for affected C4D, N4D, H4D, Z4D and G4 cloud instances. Google rates the flaws Medium and says host-level mitigations are already applied.

Source: https://thehackernews.com/2026/11/google-cloud-warns-three-amd-turin-cpu.html

## Business, briefly

**Nvidia's unfinished $13 billion Hugging Face acquisition and $6 billion Poolside licence now sit with an interim chief executive.** Source: https://techcrunch.com/2026/11/12/jensen-huangs-exit-puts-nvidias-support-for-open-source-in-question/

## What to watch

Inception Labs will close the Mercury API on 28 December. Anthropic plans to price its IPO on 18 November and begin Nasdaq trading under ANT on 19 November.
