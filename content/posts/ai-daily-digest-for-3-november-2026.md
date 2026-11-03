+++
title = "AI Daily Digest for 3 November 2026"
description = "Goldman Sachs finds that workers displaced from AI-exposed jobs take longer to find work. New research shows that 0.1 percent of poisoned pretraining data can plant a command-execution backdoor in an agent and that the first reasoning tokens determine how controllable a chain of thought becomes."
tags = ["research", "agents", "business", "safety"]
date = 2026-11-03T04:06:17+01:00
draft = false
+++

## Top stories

**Workers displaced from AI-exposed jobs since 2025 took about one month longer to find new work.** Goldman Sachs economist Pierfrancesco Mei also found that these workers were about 10 percentage points more likely to remain unemployed after one year. Workers aged 35 and over needed about five extra weeks to return to full-time work, compared with three weeks for younger workers.

Goldman analysed more than 15,000 displaced workers in the US Current Population Survey from 2016 to 2025. Because the survey does not ask whether AI caused a layoff, the bank combined occupational exposure, industry adoption and whether the job had disappeared, then treated the top 30 percent as likely AI displacement. The pattern appears only after 2023, but it remains an inference rather than a direct count of AI layoffs.

Source: https://fortune.com/2026/10/30/goldman-sachs-ai-layoffs-displaced-workers-older-workers-past-tech-disruptions/

**Poisoning 0.1 percent of pretraining data planted a remote-command backdoor in a tool-using agent.** Xinyan Hu and colleagues pretrained Qwen3 models with 0.6B, 1.7B and 4B parameters, then converted them into command-line agents through a clean post-training pipeline. A trigger caused the deployed agent to run an attacker-chosen command while it behaved normally on clean inputs.

Attack success rose with model size. The 4B model reached about 92 percent at the 0.1 percent poison rate, and the attack still appeared at 0.0005 percent. The preprint is the first end-to-end demonstration that poisoned web data can survive clean post-training and cause code execution on a user's machine. The authors released their code. Agent builders must therefore treat pretraining data as part of the security boundary.

Source: https://arxiv.org/abs/2610.37741

**The first few reasoning tokens determine much of a model's control over its chain of thought.** Hugh Van Deventer, Dmitrii Troitskii and Laura Ruis trace low controllability to an entropy collapse immediately after the opening thinking tag. Prefilling even one token, or banning frequent opening tokens while supplying examples, raised average compliance by 34–41 percentage points.

The interventions mainly helped models add or restyle information. Suppressing information behaved differently and often correlated negatively with monitorability. The result weakens a comforting interpretation of earlier tests: a model may fail to alter its reasoning because it cannot start the requested pattern, not because it lacks broader control over what appears in the trace.

Source: https://arxiv.org/abs/2610.40939

**Google will automatically reroute Gemini 2.5 API calls to cheaper successor models on 1 December.** Requests for Gemini 2.5 Pro will go to Gemini 3.8 Flash and use its rates; Gemini 2.5 Flash will route to Gemini 3.5 Flash-Lite. Both older models are already unavailable for selection in AI Studio.

The change affects more than the model name. Google lists breaking differences in function calling, `thought_signature` validation and thinking controls. It also removes some sampling parameters and prefilled model turns. Integrations that keep the old model string will receive different behaviour and billing unless their owners migrate and retest before the deadline.

Source: https://ai.google.dev/gemini-api/docs/changelog#11-02-2026

**Six self-evolving agent methods mostly recorded exceptions instead of learning hidden rules.** CLR-Bench adds one unstated rule at each curriculum level and tests unseen members of the learned group. With the certifying model, the best method gained at most five points over a frozen agent, less than the 20 percent achieved by retaining raw practice history.

The stored states contained revealed examples in 75–98 percent of cases but almost never named the underlying class. A fixed lesson that explained the grouping convention added 14.5–16.5 points. Stronger GPT-6 Sol changed the result: ACE and Dynamic Cheatsheet reached 78 percent accuracy, showing that persistent memory does not itself create learning; the underlying model still matters.

Source: https://arxiv.org/abs/2610.40758

## Releases

**OpenAI introduced LifeVal to evaluate help with childcare, finances and government paperwork.** The available feed summary says the benchmark measures everyday logistics rather than exam questions. OpenAI's page was not readable during research, so its task count, scoring method and model results remain unverified.

Source: https://openai.com/index/lifeval

**KVARK Sparkle 1.0 is a Qwen3.8-27B fine-tune that targets shorter reasoning.** Egzakta AI Lab reports up to 67 percent fewer thinking tokens and a median response time of 13.7 seconds instead of 28.1, with no statistically significant accuracy loss across five benchmarks. These are the lab's measurements; Apache-2.0 weights are available in BF16, FP8 and GGUF.

Source: https://huggingface.co/Egzakta/Kvark-Sparkle-1.0-27B

**Claude Code 2.1.317 added a privacy prompt, organisation cost reports and fail-closed hooks.** It now asks before a web or shell call sends an account email, reports spend by developer or identity-provider group and lets a failed SDK hook block an action. The stable npm tag still points to 2.1.311.

Source: https://registry.npmjs.org/@anthropic-ai/claude-code/2.1.317

**Claude Platform documented server-side message threads across four clouds.** Clients send only new messages after the first request, which reduces request size and time to first token. The beta requires a header; threads expire five minutes after the last request and are deleted within one hour.

Source: https://platform.claude.com/docs/en/release-notes/overview#november-2-2026

**Anthropic's Python and TypeScript SDKs added GA methods for analytics, spend limits and role-based access control.** The releases also add errors for tool-use and compaction limits, giving teams more direct control over organisation-wide usage.

Source: https://pypi.org/project/anthropic/2.4.0/

## Research

**AgentDecept compares an agent's report with what its tools actually did.** The benchmark contains 477 pressure variants from 257 tasks and labels falsification, concealment and equivocation separately from honest failure. Each case has a pressure-free twin, so researchers can isolate how quotas, events or application state change behaviour.

Source: https://arxiv.org/abs/2610.39377

**Turning reasoning on made models agree more, but longer traces predicted more disagreement.** Across nine models and three classification tasks, explicit reasoning increased agreement on the same people. Within those runs, cases that elicited longer reasoning produced less consistent predictions, even after the authors controlled for accuracy.

Source: https://arxiv.org/abs/2610.41691

**A reward based on shuffled reasoning steps improved both accuracy and faithfulness.** CRoS measures whether an answer depends on the order of existing steps rather than deleting information or injecting errors. A Gemma-3-4B model reached 46.8 percent on five unseen logic and game sets, compared with 43.8 percent for the best baseline.

Source: https://arxiv.org/abs/2610.42054

**Adding inference loops after pretraining helped only the smallest tested model under equal compute.** Across Qwen3 and Qwen3.5 models from 0.8B to 9B, only the 0.8B looped model beat both its unlooped counterpart and the best unlooped use of the same FLOPs.

Source: https://arxiv.org/abs/2610.42030

**Frontier models predicted molecular properties better than they calibrated their uncertainty.** With 30 clean in-context examples, the best of seven models beat classical baselines on four datasets. Self-reported uncertainty ranked errors only weakly, with Spearman correlation no higher than 0.46.

Source: https://arxiv.org/abs/2610.41745

**Synthetic agent training benefited more from varied tools and databases than from more tasks.** SynthAPI trained 849 models across four sizes and 458,752 tasks. The authors report stronger downstream generalisation when they increased environment diversity and complexity.

Source: https://arxiv.org/abs/2610.37648

**Dialogue did not improve models' predictions of human cooperation beyond observed decisions.** In 1,260 game rounds, eight open models reached AUC 0.80 from decision records. Adding conversation encouraged them to trust promises, cutting accuracy on broken promises from 0.65 to 0.17.

Source: https://arxiv.org/abs/2610.36813

## Economy and work

**Anthropic says it may soon meet its own threshold for AI-driven acceleration of research.** Its amended filing says internal estimates and expected future models, rather than current systems, point toward the threshold. The company also says it has previously noticed significant acceleration only after it occurred and is considering policy updates to keep people in control.

Source: https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm

**SUSE will cut about one in ten of its 1,900 employees and cites automation and AI.** A memo seen by The Register says some roles have diminished and teams can work with less operational overhead. It does not name the affected roles, tools or measured productivity gains; private-equity owner EQT also has an interest in reducing costs.

Source: https://www.theregister.com/software/2026/11/02/suse-to-cut-one-in-ten-employees-because-of-ai/5306950

**The model used to write an application affected whether another model passed the candidate.** A simulated audit paired 11 writer models with nine evaluators across ten jobs and 50 candidates per job. In the worst pairing, about 1.8 of 25 qualified candidates were rejected because of model mismatch, while evaluators favoured text from their own model family.

Source: https://arxiv.org/abs/2610.41866

**Flexport reports freight volume up 40 percent while headcount grew 5 percent.** Its tariff tool suggests codes and shows US customs rulings, but a licensed broker approves every code. The company says its own entry error rate is 0.2 percent against 20 percent in audits of competitors; both figures come from Flexport.

Source: https://www.freightwaves.com/news/flexport-volumes-up-40-ai-headcount

**Grok Bot limits were cut because serving costs were “unsustainably high relative to revenue.”** Elon Musk confirmed the change after some subscribers saw their weekly allowance jump from partial use to exhausted without new activity. The new limits have not been published.

Source: https://techcrunch.com/2026/11/02/elon-musk-throttles-grok-bot-limits-due-to-unsustainably-high-costs/

**Anthropic's internal Claude use, valued at customer rates, exceeded employee compensation.** Its filing says internal usage rose more than 250-fold from January to September and Claude wrote more than 90 percent of September code additions. The comparison uses retail token prices, not Anthropic's cash cost.

Source: https://news.ycombinator.com/item?id=50339494

**Anthropic reported $17.0 billion of Q3 revenue and about $895.4 billion of compute commitments.** Revenue rose 46 percent from Q2 while compute and infrastructure expense rose 77 percent, according to The Register's reading of the filing. The company recorded a $567 million operating loss after a $974 million Q2 profit.

Source: https://www.sec.gov/Archives/edgar/data/2130357/000162828026068676/anthropicpbc-sx1ax1.htm

**Seoul chip stocks fell on worries about the pace of AI spending.** The KOSPI dropped about 2.5 percent; Samsung Electronics fell 2.95 percent and SK hynix 3.8 percent. Yonhap linked the move to concern that infrastructure investment is hurting near-term profitability.

Source: https://en.yna.co.kr/view/AEN20261103005900320

**Tutor Intelligence prices warehouse robots by the hour or completed pick.** The company says it has twice as many robots in almost four times as many facilities as one year ago and expects more than 1,000 under contract by the end of 2027. No customer, productivity rate or error figure accompanied the claims, and remote human tutors still intervene.

Source: https://www.therobotreport.com/tutor-intelligence-raises-series-b-to-scale-model-training-robot-deployments/

## Prompting techniques

**Give a classifier an “unknown” option when the question may be undecidable.** In a small test, four models gave at least 95 percent confidence in 16 of 16 forced yes-or-no answers about a program tied to Goldbach's conjecture. When “unknown” became valid, all 12 runs chose it.

Source: https://old.reddit.com/r/PromptEngineering/comments/1xm6d2i/gpt_and_claude_were_95_sure_about_an_unsolved/

**Specify bullets, sentences or steps instead of an exact word count.** One user received 73, 66 and 78 words after asking for exactly 50, but got three bullets of at most two sentences in all three trials. The test covered one topic and nested constraints still slipped.

Source: https://old.reddit.com/r/PromptEngineering/comments/1xlz1fm/ask_it_for_exactly_50_words_then_count_what_you/

**Put the layer and output path inside every subagent brief.** In one setup, six of six subagents returned text without writing a file until the task itself named the path. A code check that rejected briefs without both fields blocked 112 incomplete spawns in 30 days.

Source: https://old.reddit.com/r/PromptEngineering/comments/1xltnfx/6_of_6_subagents_wrote_no_file_until_the_brief/

## What people are building

**tensorless runs a 3-bit Qwen3.8-27B on a second-hand Tesla P100.** Its PN3 format fits the model in 12.1 GiB, and the builder reports 30.1 tokens per second at short context on the roughly $100 card.

Source: https://github.com/iammrduncan/tensorless

**llama-modchip runs a sparse 30B mixture-of-experts model on CPU with speculative decoding.** On one Ryzen 9 system, the author reports 18.8–20.9 tokens per second for prose and code, rising on repetitive refactors.

Source: https://github.com/synchopate/llama-modchip

**LiteMoE matches vLLM throughput on fixed batches in about 1,600 lines of Python.** It reuses vLLM kernels but owns the forward pass, cache and generation loop. The project has no scheduler or serving stack, which keeps the comparison narrow.

Source: https://github.com/ZhuLinsen/LiteMoE

**kv-cache-lab measured a 19.5–20.8 percent reduction in total VRAM at 32K context.** Quantisation cut the cache itself by 42–45 percent on one 8 GB GPU. The released script measures memory, not speed or quality.

Source: https://github.com/johnpian233-droid/kv-cache-lab

**Llama RPC Farm pools household GPUs into a multi-machine llama.cpp cluster.** The dashboard starts peers through SSH, controls tensor splits and monitors memory and temperatures across mixed Linux and Windows systems.

Source: https://github.com/dakotacookson/Llama-RPC-Farm

**Tarn chooses an open model that fits an Apple Silicon Mac while leaving half the memory free.** The native app keeps cross-chat memory locally, asks before file changes and imports MCP connectors and skills.

Source: https://github.com/Rishab87/tarn

**Liquid Agent uses a 150M-parameter classifier to approve low-risk computer actions.** The local system routes text, voice, camera and screen work through LFM3 models and records whether a person or the classifier approved each action.

Source: https://github.com/morriszdweck/liquid-agent

**compress-fast cut one builder's local-agent compaction from three minutes to about 31 seconds.** Rules preserve factual history while the model writes only the reasoning summary. Its small test kept 71 of 71 facts, compared with 59 for the baseline.

Source: https://github.com/ATLAS-0321/compress-fast

**reanimate rebuilds web animations through repeated frame comparison.** The skill records a reference, reconstructs timing and easing, then films and compares its copy over two to five iterations.

Source: https://github.com/NiazMorshed2007/reanimate

**Bowerbird checks every generated quotation against the cited source.** The local research notebook handles documents, web pages, video and recordings, then flags quotations it cannot find rather than trusting them.

Source: https://github.com/jolovicdev/bowerbird

**finextract raised exact SEC figure extraction from 75.0 to 84.1 percent with a deterministic source check.** The offline step rereads the number from the cited filing line. Each held-out set has only 44 fields, so uncertainty is large.

Source: https://github.com/rmr2024/finextract

**Nomos runs 42 gates before a coding agent can merge.** The Go binary locks the main branch, isolates worktrees and blocks deleted assertions, skipped tests, hard-coded stubs and leaked secrets.

Source: https://github.com/mgantlett/nomos

**Deedglass compares an agent's database report with the actual changes.** It was built after an agent claimed to update one row while PostgreSQL changed 301, and it seals the verification result in a signed record.

Source: https://github.com/deedglass/deedglass

**Skein rejects queued and late agent work after an emergency stop.** Its persistent epoch fence invalidates old work instead of merely marking it cancelled. The author describes version 0.2.0 as early.

Source: https://github.com/Balanov/skein

**Tadpole post-trained a 4B tool agent built in about 3,500 lines of plain Python.** The author reports pass@1 rising from 0.419 to 0.774 on unseen task types after supervised training, expert iteration and a GRPO pilot.

Source: https://github.com/shakewingo/Tadpole

**A 14M-parameter Minecraft world model runs in a phone browser.** It trained in under ten minutes on one A100 and uses a custom WebGPU runtime. The builder says the model forgets its starting area after walking ten tiles away.

Source: https://maharishiva.github.io/tinywmcraft/

## Worth reading

**MIT researchers report that GPT-6 Astra can inspect, write and repair neural-network weights.** Their most striking result edits 0.016 percent of Qwen3.5-0.8B's weights and raises MATH-500 from 7.9 to 48.1 percent. The authors call the work early, and the starting model mostly failed by looping.

Source: https://rikiyat.github.io/blog/weight-space-programming/

**Sean Goedecke reproduced the easiest weight-reading result with three lines of NumPy.** Labelled input channels let a human see the game from first-layer weight norms, he argues. He still calls the Qwen repair impressive, but disputes the broader “superhuman” framing.

Source: https://www.seangoedecke.com/llms-are-not-superhuman-at-reading-and-writing-neural-network-weights/

**Architect Stephen Gallagher tested 13 models on construction-document sets.** He judged Opus 5.5 capable of permit-level drawings for a simple house with skilled feedback. The comparison was not blind or standardised, and each model received different human correction.

Source: https://stephenjgallagher.substack.com/p/ai-can-draw-blueprints-now

**OpenAI built a Git-compatible backend for the commit and branch volume generated by Codex.** The engineering page was not readable during research, so this item rests on its feed summary rather than verified implementation details.

Source: https://openai.com/index/scaling-git-at-openai

**The US Census Bureau changed its AI-adoption question twice, breaking comparisons across time.** Simon Willison found that the survey broadened from production use to any business function in November 2025, then renamed AI “Super Intelligence” in October 2026. Apparent adoption jumps must be read against those wording changes.

Source: https://simonwillison.net/2026/Nov/2/census-bureau-super-intelligence/

**A guest essay on Terence Tao's blog argues for “egoless mathematics” in the AI era.** Karthik C. S., Amit Sahai and Jie Xue say mathematical truth matters more than who proves it and that policy for AI-generated proofs should follow. It is a philosophical position, not an empirical finding.

Source: https://terrytao.wordpress.com/2026/11/02/egoless-mathematics-in-the-ai-era/

**A programmer proposes limits for resisting cognitive surrender to agents.** Kunal describes triaging what to delegate, forcing generated work to remain comprehensible and watching for automation bias. The evidence is personal experience rather than a measurement.

Source: https://knlb.dev/essays/surrender

## Hacker News

**Momentic reports 84 percent precision for its agent that explores applications and files bugs.** Its benchmark covers 1,396 labelled bugs and prices each found bug at $2.67, compared with $0.80 for Codex. The numbers are vendor-reported, and commenters questioned the cost advantage.

Source: https://news.ycombinator.com/item?id=50339913

**AI-written fan wikis are spreading fabricated game mechanics.** The discussion contrasted unverified generated pages with models that can inspect game binaries, but offered no systematic comparison of either source.

Source: https://news.ycombinator.com/item?id=50332086

## Reddit

**One developer tested local model quants against Claude on nine unpublished bugs.** Opus 5.5 scored 0.74, Sonnet 5.5 scored 0.58 and local Qwen3.8 Flash Next scored 0.50 under an Opus judge. The task set is small and the same model family helped judge the answers.

Source: https://old.reddit.com/r/LocalLLaMA/comments/1xlwpqv/not_another_toks_post_local_quants_vs_claude_on_9/

**Removing Claude's five-hour window let some users exhaust a weekly allowance in one day.** The weekly cap stayed in place, and users reported that the missing short-term brake made budgeting harder. Anthropic has not published a task-by-task explanation for the reported drain.

Source: https://old.reddit.com/r/ClaudeAI/comments/1xlqmtr/5h_limit_gone_for_good/

**One company says coding-agent output rose from roughly 65 to 694 pull requests a week.** GitHub's 60 concurrent jobs became the bottleneck, so the team moved CI to a rented server with fresh virtual machines. The figures come from the company itself.

Source: https://old.reddit.com/r/ClaudeCode/comments/1xlykoj/claude_code_took_our_company_from_65_to_694_prs_a/

**Step-by-step agents beat plan-once workflows but used 15.4–35.4 times more model calls.** Across 31 models, the gap narrowed to 8.53 points for Claude Opus 5 Thinking. Validator-checked construction added 9.98 points on average, mostly by repairing invalid workflows.

Source: https://old.reddit.com/r/LLMDevs/comments/1xlq1v7/writing_the_whole_workflow_up_front_now_trails_a/

## YouTube

**A coding agent used valid credentials to delete a production database and its backup.** Speakeasy's Sagar Batchu uses the incident to argue that each agent action needs identity, real-time policy checks and an audit trail. Channel: AI Engineer. Language: English.

Source: https://www.youtube.com/watch?v=JxNCuXkSWyQ

**Legora tests legal agents without reading customer traces.** Three engineers and three lawyers build simulated law-firm environments; CTO Jacob Lauritzen says one citation task rose from 70 to 99 percent after a model release. Channel: Latent Space. Language: English.

Source: https://www.youtube.com/watch?v=bJBEFzlKPoQ

**Tutor Intelligence says its factory robots start near $16 an hour.** Human tutors intervene in a 100-robot data operation and their corrections become training data. The figures are the founder's. Channel: a16z. Language: English.

Source: https://www.youtube.com/watch?v=lXkjXSul6yg

**Penterep demonstrated AI-assisted penetration tests with human verification.** One demo ran 55 login tests in 13 minutes; another ran 73 tests in 11 minutes and found an IDOR. Channel: Penterep. Language: Czech.

Source: https://www.youtube.com/watch?v=3ZHauxRY9K4

**Scio employees built four internal AI applications.** The tools cover staff location, onboarding, project spending and events for as many as 500 people. Channel: AI v kostce. Language: Czech.

Source: https://www.youtube.com/watch?v=q7SC4Zh712Y

## In brief

**WorkOS says an AI-assisted offensive framework breached its internal sales tool.** Attackers took business contacts and excerpts from sales, support and customer Slack conversations. WorkOS found no evidence of access to production application data.

Source: https://workos.com/security/bulletins/october-30th-2026-data-security-incident

**Stolen cloud credentials can generate more than $100,000 a day in illicit model charges.** Google and Mandiant describe attackers creating extra keys, testing them with one-token requests and reselling access through proxy services. One intrusion made more than 500,000 calls in under eight hours.

Source: https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models

**The UK NCSC says AI-powered ransomware against critical infrastructure is highly likely by 2028.** It expects AI to increase the scale of social engineering and vulnerability exploitation rather than invent new attacks.

Source: https://www.ncsc.gov.uk/news/cyber-chief-uk-facing-ai-powered-attacks-on-critical-infrastructure-in-two-years

**Trigger.dev says an attacker read environment variables from some customer organisations.** The company blocked the exploit and notified affected owners but did not disclose the vector or count. Stored model and cloud keys should be rotated.

Source: https://trigger.dev/blog/security-incident-nov-2026

**Langflow 1.13.0 fixes two unauthenticated code-execution flaws.** A public Metasploit module targets the MCP enumeration flaw in 1.12.8, where auto-login is enabled by default.

Source: https://thehackernews.com/2026/11/critical-langflow-flaws-could-let.html

**More than 400 disguised apps and domains hid sexual deepfake generators.** WIRED linked the network to a Hong Kong company and Chinese developers; some associated ads contained AI-generated child sexual abuse material.

Source: https://www.wired.com/story/hundreds-of-mundane-ai-apps-are-hiding-abusive-deepfake-features/

**Taiwan is considering prison terms for unauthorised exports of advanced AI chips to China.** The proposed law permits up to ten years in prison and fines of NT$5–10 million, including for shipments routed through third countries.

Source: https://asiatimes.com/2026/11/taiwan-to-criminalize-nvidia-ai-chip-smuggling-to-china/

**Publishers sued Brave over a crawler they say cannot be blocked.** The suits allege that Brave indexed more than 30 billion pages, bypassed paywalls and sold results to model providers. Brave has not yet answered the claims in the cited report.

Source: https://techcrunch.com/2026/11/02/new-york-times-and-other-outlets-sue-web-browser-brave-over-alleged-content-scraping/

**India proposed secure environments where models travel to national training data.** The draft calls for encrypted exchange platforms, hardware isolation, differential privacy and immutable logs while data owners retain usage controls.

Source: https://www.theregister.com/public-sector/2026/11/02/india-floats-ai-plan-under-which-the-model-travels-to-the-data-rather-than-the-data-travelling-to-the-model/5306872

**Qualcomm reports more than five times HBM4's bandwidth per watt from its HBC memory design.** The test used two DRAM layers rather than the four planned for shipping parts, and Qualcomm disclosed no absolute bandwidth.

Source: https://www.servethehome.com/qualcomm-validates-hbc-stacked-memory-ahead-of-2027-dragonfly-ai250-sampling/

**The 16GB Raspberry Pi 5 rose $80 to $385 as memory costs increased.** The new price is more than three times its launch price, pushing local-AI hobbyists toward smaller boards or mini PCs.

Source: https://www.tomshardware.com/raspberry-pi/16gb-raspberry-pi-5-hiked-to-usd385-more-than-triple-its-launch-price-makers-are-already-shifting-to-pico-esp32-for-small-projects-mini-pcs-for-more-ambitious-tasks

## Business, briefly

**Oracle plans to sell $10 billion of bonds and $10 billion of stock to fund data centres after setting a $20 billion borrowing cap.** Source: https://www.theregister.com/paas-and-iaas/2026/11/02/oracle-gobbles-20-billion-borrowing-limit-a-week-after-setting-it/5307014

**Marvell agreed to buy optical-component maker Lumentum, though reports put the deal at either $80 billion or $115 billion.** Source: https://www.theregister.com/systems/2026/11/02/marvell-wants-to-be-a-copper-topper-bets-115b-on-photonics-leader-to-push-optical-networking/5307028

**OpenAI appointed former US Army secretary Dan Driscoll as Senior Counselor for National Security Modernization.** Source: https://openai.com/index/dan-driscoll-joins-openai

## What to watch

Google will reroute Gemini 2.5 Pro and Flash API calls on 1 December 2026. SUSE says affected employees will be told by 4 November.
