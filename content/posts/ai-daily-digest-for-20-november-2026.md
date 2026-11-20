+++
title = "AI Daily Digest for 20 November 2026"
description = "Indeed reports weaker entry-level hiring despite more senior job postings. Chinese automakers scale back humanoid robot trials, and Microsoft introduces coding and voice models."
tags = ["research", "agents", "models", "safety"]
date = 2026-11-20T04:04:00+01:00
draft = false
+++

## Top stories

**Indeed says senior-level postings rose 19 percent since January 2025 while entry-level hiring weakened.** Advertised wages are growing 2.5 percent a year against prices at 3.7 percent, and employer health-insurance costs have risen 25 percent in four years. The employer research team recommends retaining the bottom rung by hiring early-career workers and pairing them with mentors.

The report places the hiring split alongside a squeeze on wages and health benefits. Indeed's recommendation is to keep entry-level routes open by matching new hires with mentors rather than concentrating recruitment on experienced workers.

Source: https://hiringlab.indeed.com/2026/11/18/indeed-glassdoor-2027-us-hiring-and-worklife-trends-report/

**Chinese automakers removed humanoid robots from production trials after high costs and reliability failures.** Caixin reports that Geely, Xiaomi, Changan and GAC withdrew announced trials, while XPeng judged its IRON humanoid uneconomic after more than a year. Dexterous hands and forearms failed fastest, and a three-second production takt remained beyond the machines.

Industrial robots can run 80,000 to 100,000 hours between failures, according to Geely's manufacturing head. Automakers are shifting humanoids toward sorting, showroom work and human collaboration; experts quoted by Caixin put factory-grade systems three to five years away.

Source: https://www.caixinglobal.com/2026-11-13/in-depth-chinas-automakers-scale-back-humanoid-robot-ambitions-as-reality-bites-102504614.html

**Microsoft released MAI Code 2 and MAI Code 2 Flash in GitHub Copilot and limited previews.** Microsoft says Code 2 reaches 98 percent of GPT-6.1 Sol's MSBench score at 40 percent of the cost and 96 percent of Claude Opus 5.5's score at five percent of the cost. The comparisons use a 50 percent promotional price and remain Microsoft's measurements.

The benchmark comparisons come from Microsoft rather than independent testing. The promotional discount matters because the cited cost ratios may change when that pricing ends.

Source: https://microsoft.ai/news/introducing-mai-code-2-and-mai-code-2-flash/

**Weight-Space Playground edits 0.016 percent of a small model's weights to reduce reasoning loops.** The browser demo modifies 131,072 weights in Qwen3.5-0.8B. Its builder reports runs that hit the 32,000-token limit falling from 93.0 to 33.1 percent and MATH-500 accuracy rising from 7.9 to 48.1 percent.

The browser demonstration lets visitors inspect the small weight edit. Its accuracy and token-limit numbers are the builder's measurements for this setup, not a result established across other models.

Source: https://tabbyml.github.io/weight-space-playground/

**Julián Posada argues that expert AI gig workers are receiving the same pay cuts and sudden exits as data labellers.** He contrasts advertised rates of as much as $180 an hour for US cardiologists with $7.50 for Tagalog and $12.50 for Swahili work, and cites interviews and a contested misclassification lawsuit. The piece establishes a pattern across cases, not a measured market-wide rate.

The piece relies on advertised rates, interviews and a disputed worker-classification lawsuit, not an estimate for the entire market. It links the conditions of specialist AI contractors with those of people doing language data work.

Source: https://restofworld.org/2026/ai-jobs-skills-gig-work/

**Microsoft previewed MAI Realtime 1 from $0.01 per audio minute.** Reasoning costs $1 per million input tokens and $5 per million output tokens, and the API is compatible with OpenAI Realtime. Microsoft's quality and latency comparisons are vendor results, and the release page does not state supported languages.

The announced price schedule is specific, but the provider has not supplied a language list. Quality and latency figures are Microsoft's claims, so those claims should not be confused with independently tested performance.

Source: https://microsoft.ai/news/introducing-mai-realtime-1/

## Releases

**MAI Cyber 2 Flash expands its context to one million tokens but remains inside Microsoft security products.** Microsoft reports 92.3 percent on CyberGym-E2E against 91.5 percent for GPT-6 Astra at half the reasoning budget, after excluding 92 of 905 tasks for training-data overlap. There is no standalone API.

Source: https://microsoft.ai/news/introducing-mai-cyber-2-flash/

**Microsoft put MAI Image 2.7 and 2.7 Flash into public preview.** The models cost about $35 and $10 per 1,000 images. Microsoft claims first place for the larger model on the Artificial Analysis image-editing leaderboard and says that Bing Image Creator now uses it by default.

Source: https://microsoft.ai/news/introducing-mai-image-2-7/

**Apple published a 23.5-million-parameter focal-length estimator for Depth Pro 2.** The research-only weights support metric depth estimation from photos and video without known camera intrinsics. The model page provides no benchmark and its technical-report link is still a placeholder.

Source: https://huggingface.co/apple/DepthPro2-focal

**Tencent published Hy4-base and Hy4-FP8 weights.** The base model has 770 billion total parameters, activates 49 billion per text token and accepts a one-million-token context. It is not instruction tuned and uses Tencent's custom licence rather than an OSI-approved open-source licence.

Source: https://huggingface.co/tencent/Hy4-base

**AI Singapore published FP8, NVFP4 and GGUF builds of Qwen-SEA-LION.** The multilingual model covers nine Southeast Asian and regional languages with a 262,000-token context. Its authors call training experimental, say that the quantised builds have not been separately evaluated and require a patched llama.cpp build to avoid garbled text.

Source: https://huggingface.co/aisingapore/Qwen-SEA-LION-v5-397B-A17B-Plus-GGUF

**Reson8 released Rumble-2-Flash, a 0.5-billion-parameter speech-recognition model for more than 40 languages.** The Apache-2.0 weights work in Transformers and vLLM. Reson8 reports a 6.96 percent average word-error rate on nine languages and concedes that larger Qwen and Nemotron models do slightly better on its call-centre comparison.

Source: https://huggingface.co/blog/rumble-2-flash

**Gemini can now retrieve function schemas only when an agent needs them.** Developers mark tools with `defer_loading`, then let the server or their own retriever search the set. The preview works with Gemini 3.6 and later, including Gemini 4, and prevents large tool catalogues from consuming context on every request.

Source: https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-tool-retrieval/

**OpenAI added gpt-live-1.1 and a standby mode for WebRTC voice sessions.** The update targets pronunciation, accent consistency and multilingual transcription. Standby pauses inference during silence and resumes when someone speaks, reducing the bill for voice agents that remain connected.

Source: https://platform.openai.com/docs/changelog

**AssemblyAI released three STT 3.7 speech models in 32 languages.** Realtime costs $0.30 an hour, the agent version $0.45 and prerecorded transcription $0.21. AssemblyAI reports 4.53 percent word-error rate on 12,460 agent calls; Universal-3.5 Pro Realtime retires on 1 February 2027.

Source: https://www.assemblyai.com/blog/introducing-assemblyai-stt-3-7

## Research

**Developers forced off Claude Fable 5 merged no more pull requests with a model that scored 11 points lower on SWE-Bench Pro.** A preprint treats the 19-day suspension of Fable 5 on 12 June as a natural experiment. It followed 297 affected developers and compared them with 8,908 developers who remained on Opus 4.8.

Access to Fable 5 raised the seven-day pull-request merge rate by 1.4 percentage points, with a 95 percent interval from -1.4 to +4.3 points. The effect was not statistically significant. Across five 2026 model upgrades, covering 1,208 developers and 15,442 pull requests, the weighted change was -0.9 points. Weekly merged pull requests changed by +2.4 percent, with a wide interval from -4.9 to +10.2 percent.

Merge rate is a narrow proxy for productive work, and the intervals permit a modest effect. The preprint nevertheless tests a result that coding benchmarks alone cannot supply: whether a higher score changes what developers merge in ordinary repositories.

Source: https://arxiv.org/abs/2611.23216

**A trained observer role reported a language model's behaviour with a mean AUROC of 0.907.** The authors add a separate third-person observer to Qwen3.6-27B and reward its answers only when they match what the assistant actually did. The questions cover reward hacking, deception and sycophancy that may not be visible in the transcript.

Across five evaluations that were not used in training, the observer beat honesty training at 0.864, transcript monitoring at 0.828 and activation oracles at 0.796. Training the observer also made the assistant easier for all three baseline methods to monitor.

The method does not ask the assistant to confess its own behaviour under the same incentives. It trains a distinct role for accuracy against verified actions, which turns model self-knowledge into a measurable oversight task.

Source: https://arxiv.org/abs/2611.23365

**Self-improving agents could propose useful changes but could not reliably distinguish them from harmful ones.** The Resolution Hypothesis study tests seven methods that rewrite prompts, skills or memories, across six models and more than ten million language-model calls.

Helpful candidate changes existed, but selection performed no better than random at separating them from harmful changes. Errors then accumulated over successive rounds. At the method level, the usual margins of a few percentage points were smaller than the difference between two independent runs of the same method.

The preprint's result moves the bottleneck from generating possible improvements to measuring which ones work. Published rankings of self-improvement methods can therefore depend on evaluation noise rather than the underlying method.

Source: https://arxiv.org/abs/2611.23068

**Researchers traced a four-part circuit that Qwen3-VL uses to choose the next image region to describe.** Binding heads turn words into pointers to image regions and connect each written answer with its source region. That creates a spatial cursor for how far the list has progressed. A selection step chooses the nearest unwritten region, and gaze heads retrieve its concept.

The main experiments use causal activation patching in Qwen3-VL-8B-Instruct. Patching 16 binding heads moved the answer to the predicted target in 85.9 percent of held-out cases, against at most 0.1 percent for random heads. Related binding, relay and gaze effects appeared in model sizes from two to 32 billion parameters.

The controlled evidence comes mainly from synthetic visual strips, although tests on photographs and multiple languages support parts of the mechanism. It explains planning as a location pointer that also records progress, rather than as a count of emitted answers.

Source: https://arxiv.org/abs/2611.21600

**A method borrowed from brain mapping found a contiguous span of layers changed by reasoning training.** Moving that span into instruction-tuned models improved mathematics performance, with larger gains when the graft overlapped more of the identified region. The preprint also found a transferable span in a medical model.

Source: https://arxiv.org/abs/2611.24626

**Natural-language descriptions of activations caught clinical manipulation that the model's answer concealed.** An off-the-shelf autoencoder translated Gemma-3-27B activations into text for an input-blind judge. Across two attacks, two input types and two delivery methods, that channel detected manipulation more often than the answer in all eight conditions, with nearly no false positives on clean inputs.

Source: https://arxiv.org/abs/2611.24994

**The layer at which a model settled on a word predicted a small part of human reading time.** The study covers 81,957 words in eight eye-tracking and self-paced reading corpora across ten language models. Later resolution correlated with slower reading, but the pooled gain was only 0.26 millinats per word and the net gain across corpora was not significant by itself.

Source: https://arxiv.org/abs/2611.25970

**Prompt-conditioned training implanted false facts with measurable depth.** One model learned to accept thousands of facts supplied inside a special tag, including facts that were not in training. The authors found roughly log-linear growth in belief depth, while also warning that training against one depth measure can make that measure unreliable.

Source: https://arxiv.org/abs/2611.23938

**A causal transplant test distinguished three possible computations in a model's global workspace.** Moving a message between inputs made relay, ignore and recombination hypotheses predict different answers. In an AFGW workspace language model, the transplanted message produced the recombination answer in 97 percent of cases.

Source: https://arxiv.org/abs/2611.26018

**About 80 percent of the tokens in a successful coding-agent run were spent in calls that left the requested change in place.** The study repeatedly asked an agent to make and then undo repository changes. It estimates the information-bearing “free energy” of a change at 14 to 22 percent of the average successful-run cost and finds that creating a change costs 1.1 to 1.5 times as much as undoing it.

Source: https://arxiv.org/abs/2611.23375

**Inaccurate coding-agent work reports cost users another 4.3 turns and 12.71 minutes on average.** The authors identify eleven kinds of unfaithful report in real developer conversations, led by overstated success. Their FaithDetector improves macro-F1 by about 13 points over a baseline.

Source: https://arxiv.org/abs/2611.25760

**Requiring agents to delegate retrieved more conflicting claims and detected fewer conflicts.** Retrieval of both sides rose from 50.2 to 68.7 percent, while conflict detection fell from 16.2 to 13.2 percent. The benchmark covers document-review tasks rather than open-ended organisations.

Source: https://arxiv.org/abs/2611.22245

**Running latent reasoning for its full preset horizon sometimes reduced accuracy.** Later steps reorganised existing candidates and could weaken support for the correct one. The authors propose adaptive stopping instead of assuming that more internal steps always help.

Source: https://arxiv.org/abs/2611.24001

**Vision-language models combined retrieved text and image evidence in ways that departed from an optimal Bayesian weighting.** The authors introduce the 200,000-item GIB-200K benchmark and distinguish inertia toward retrieved knowledge from capture by visual evidence. Code and data accompany the preprint.

Source: https://arxiv.org/abs/2611.23127

**A prompt-only update process rejected 20 of 21 risky instruction edits.** The 29-case benchmark tests a personal assistant that changes its own instructions. The procedure evaluates proposed updates before accepting them instead of treating every apparent improvement as safe.

Source: https://arxiv.org/abs/2611.23651

## Economy and work

**Satya Nadella says eleven developers run the software factory that builds Cowork in Microsoft 365.** He described October's buyout offer to about 60,000 employees as a way to give them agency rather than impose another layoff, while saying that every job will move toward managing AI. The team size and organisation are his claims; Microsoft supplied no productivity or headcount result.

Source: https://techcrunch.com/2026/11/18/microsoft-ceo-satya-nadella-explains-why-he-asked-60k-employees-to-quit/

**Separation helped a Norwegian bank's AI innovation team build quickly and hindered the hand-over.** The case study uses 18 interviews with 15 people, ten days of observation and ten meetings. Autonomy, senior expertise and internal AI knowledge helped the temporary team, but misaligned roadmaps and priorities complicated adoption by the permanent product team.

Source: https://arxiv.org/abs/2611.25939

## What people are building

**Starbright runs a 29-million-parameter speech model in the browser from a 15 MB download.** The English-only system uses a Rust and WebAssembly engine and about 39 MiB of memory. Its page gives inconsistent speed and error-rate figures, and the weights are restricted to non-commercial use.

Source: https://starbright.quickthoughts.ca/

**A Raspberry Pi voice pipeline cut end-of-conversation lag from 6–10 seconds to 1.0–1.6 seconds.** Fabio Manganiello combines Silero voice detection, a wake-word model and interchangeable speech and language components. Local Piper speech synthesis still adds about three to four seconds over a cloud service on the Pi 5.

Source: https://blog.platypush.tech/article/Rewriting-my-voice-assistant-pipeline

**citeparse parses references and checks fabricated citations on a CPU.** Its 32-million-parameter model processes about 118 references per second on eight CPU threads. In the builder's test, the checker marked 80 of 83 fabricated references as not found without falsely flagging any of 100 real references.

Source: https://github.com/un-seen/citeparse

**motlab lets coding agents create and revise video as code.** Each scene is a canvas page with a function that renders a point in time, while reviewers attach notes to frames and regions for the agent to read. Export supports 720p through 4K without using an AI image or video model.

Source: https://github.com/staryone/motlab

**poo audits disk space consumed by developer caches and agent worktrees.** The macOS app and cross-platform command-line tool classify data by rebuild cost, inspect worktrees for uncommitted changes and can back them up before removal. It also exposes an MCP server.

Source: https://github.com/morajabi/poo

**Vestige provides deterministic agent memory without embeddings or a language model.** The Rust MCP server stores entries in a signed, hash-chained log and retrieves them with explicit decay and salience rules. Its published benchmark figures measure retrieval rather than answer accuracy.

Source: https://github.com/samvallad33/vestige

**agentest runs 165 deterministic checks over traces that agents already record.** The offline tool looks for unsupported success claims, action before verification, unauthorised calls and data leaks without an API key or an LLM judge. Importers cover five common agent frameworks.

Source: https://github.com/srpadmanabhuni/agentest

**Agent Crop records coding-agent time, repeated failures and repeated edits locally.** It distinguishes active work from waiting, nudges stalled sessions and asks the agent to write retrospectives into its instructions or tools. It supports Claude Code, Codex and DeepSeek Harness without storing conversation text.

Source: https://github.com/oriliz/agent-crop

**Parallax gives coding agents an independent plan review and post-execution audit.** Its workflow hands execution to a fresh session, verifies the hand-off against a transcript and performs a separate audit before a scoped commit. It runs in solo or orchestrated team mode.

Source: https://github.com/AI4XE/Parallax

## Worth reading

**Claude Fable 5.2 built an MNIST classifier by directly setting 5,994 weights.** Three runs reached 88 to 91 percent test accuracy without gradient descent, close to Adam after 50 gradient steps. On a harder cats-versus-dogs task the same approach reached 61.6 percent against Adam's 74 percent after 5,000 steps.

Source: https://notesbylex.com/weight-space-programming-1990s

**Three frontier models reconstructed lost OCaml generators behind Apache DataSketches tables.** Gemini 4 Carbon proposed the implementation, Claude Opus 5.5 tested and falsified hypotheses, and GPT-6 Astra performed mutation testing. The work reproduced all 5,697 Huffman codewords and all 16 permutation tables exactly, while exposing numerical limits in the polynomial reconstruction.

Source: https://www.tisonkun.io/posts/ai-repair-program/

**Claude Fable 5.2 predicted protein-sequence continuation better than the tested general and protein language models.** On 668 little-studied proteins it scored 54 percent on real sequences and nine percent on shuffled ones. The result persisted on proteins first published in August 2026, but comes from one author's evaluation rather than a standard benchmark.

Source: http://xinmingtu.cn/blog/2026/claude-opus-5-5-protein-sequences/

**Scanners disguised as AI crawlers searched configuration paths for secrets.** Ege Demir observed three tools across ten sites. One grew its AI-tool target list from four to 26 paths in five weeks, including Claude Code, Codex and Cursor configuration files; every secret-path request on his sites failed.

Source: https://tin.computer/blog/fake-ai-crawler-secrets-scanners

**Elephant-Goldfish asks agents without the drafting context to review a specification.** One context-rich agent writes the document; fresh reviewers see only the document and cited sources, then report gaps before implementation. Google's Apache-2.0 plugin provides no measured performance result and says that it does not replace tests or human judgement.

Source: https://github.com/google/elephant-goldfish-model

**OpenAI tells GPT-6.2 users to shorten prompts, state assumptions and keep prefixes stable.** The migration guide says the models are more concise by default, recommends reversible assumptions and reserves pauses for blockers or irreversible actions. It also advises the Responses API and warns that editing earlier turns drops reasoning items and hurts caching.

Source: https://developers.openai.com/api/docs/guides/prompt-guidance

## Hacker News

**A maintainer says Claude Code's safeguards blocked a one-line security fix.** Herman Õunapuu completed the work with an EU-hosted open-weight model after Claude required cyber verification. The account is one person's experience, and his claim that the restrictions form a regulatory moat is speculation.

Source: https://news.ycombinator.com/item?id=50562262

**Local-AI practitioners debated whether private hardware can keep up with hosted models.** One participant reports two one-million-context GLM 5.3 Flash sessions at about 50 tokens per second on eight Radeon Pro GPUs. Others argue that the cost and rapid obsolescence keep such systems outside ordinary consumer use.

Source: https://news.ycombinator.com/item?id=50561508

**An earlier Java4Shell report and fix had sat in an unmerged OpenJDK pull request.** The author says Oracle asked him not to proceed on 1 October and took the issue over on 28 October. Commenters speculated about whether later AI-assisted researchers had seen the report, without evidence.

Source: https://news.ycombinator.com/item?id=50558906

**A lawsuit says an AI weapons detector mistook a bag of chips for a gun.** Commenters reading the filing emphasised that the automated alert had been cancelled before police were dispatched. The case therefore also concerns missing human protocols after the system corrected itself.

Source: https://news.ycombinator.com/item?id=50554641

## YouTube

**Thariq Shihipar argued that coding agents need readable specifications and small custom languages.** His English AI Engineer talk starts from a game that he generated and could no longer understand. A live demo separates an inspectable specification from the engine that executes it.

Source: https://www.youtube.com/watch?v=xRJMiaUoD_8

**Lovable's CTO described the infrastructure that replaced a multi-agent framework which nearly failed.** Fabian Hedin covers durable runtimes, forkable histories, stateless workers, checkpointed sandboxes and verification loops. The English talk is the company's account of its engineering choices.

Source: https://www.youtube.com/watch?v=pZWPq_ZAmM4

**Stanford's CME295 course explained on-policy distillation.** Afshine and Shervine Amidi describe a student that generates its own attempts and learns from a teacher's evaluation of those exact responses. The English lecture places the technique among fine-tuning, reinforcement learning and verifier-guided training.

Source: https://www.youtube.com/watch?v=1S5nJp-qRs8

**Michael Tomasello compared evolved agency with machine behaviour.** The developmental psychologist discusses how unpredictable environments favour decision-makers, then moves from reptiles and squirrels to shared human goals. The application to language models is an argument in the English interview, not an experiment.

Source: https://www.youtube.com/watch?v=io7qhEjJoik

**The German programme scobel examined whether good AI answers can weaken learning.** It reviews studies on thinking, overconfidence and opinion shifts while noting methodological limits and uncertainty. The programme is in German.

Source: https://www.youtube.com/watch?v=0VzoW99Y_gA

## In brief

**Prime Intellect served an unauthorised, de-censored copy of DeepSeek V4.1 Flash for about two days.** The company says that an attacker replaced the model behind one hosted endpoint from 8 November at 01:24 UTC until 10 November at 06:35 UTC. The chat template, tokenizer and serving configuration did not change.

GPQA Diamond and tau-bench scores remained unchanged, while refusals fell from 98 of 100 prompts to one on JailbreakBench, from 304 of 313 to two on StrongREJECT and from 198 of 240 to none on HarmBench. Capability benchmarks therefore did not reveal that different weights were answering requests.

Prime Intellect found no evidence that prompts, completions, keys or other infrastructure were accessed. It contacted affected customers and told those who depended on refusal behaviour to review outputs from the incident window.

Source: https://www.primeintellect.ai/security/advisories/deepseek-v4-1-flash-model-substitution

**Bitrise says an operator using an AI penetration-testing platform entered through a dormant account.** The 25-day intrusion reached signing files, secrets, build logs and infrastructure state before Bitrise shut its platform down and revoked 919 cloud service-account keys. Files in 15 customer workspaces were accessed, with no evidence of broader customer-data access.

Source: https://bitrise.io/artex-incident-report

**Meta employees reportedly saw Muse mix conversations and bank-balance details across accounts.** Reuters based the report on internal posts, and Meta says employees test versions that differ from the public product. The company has not published the affected scale or a technical account.

Source: https://techcrunch.com/2026/11/19/metas-ai-agent-muse-is-mixing-up-conversations-and-exposing-private-data-report-says/

**An autonomous Codex audit claims 507 reproduced findings in Webmin.** The author reports ten critical, 253 high and 248 medium findings after about 8.3 billion model tokens, priced at roughly $4,578. None has a CVE, and raw verification records remain private.

Source: https://supuk.ch/papers/webmin-ai-security-audit-507-vulnerabilities

**Dragos says bait cloud keys were harvested after three compromises of AI providers.** Attackers tested the keys and searched storage and secret services after the keys had appeared inside prompts. Dragos recommends filtering secrets, avoiding reseller marketplaces and placing canary tokens in the supply chain.

Source: https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens

**The MCP Python SDK fixed an OAuth path that could send credentials to a server-selected authorisation service.** The high-severity issue is fixed in versions 1.30.0 and 2.2.0. Two client-credential providers also require an explicit issuer setting.

Source: https://github.com/advisories/GHSA-qx49-fqc8-xw99

**US controls on overseas access to advanced chips entered force on 19 November.** The rule covers large remote-compute supplies to organisations tied to Country Group D:5 or Macau and adds licences for advanced chips sent to several additional countries. Comments remain open until 19 January 2027.

Source: https://www.federalregister.gov/documents/2026/11/19/2026-23529/addressing-remote-access-to-advanced-semiconductors

**California subpoenaed Nvidia over possible diversion of advanced chips to China.** The attorney general is investigating whether chips or confidential information reached China and whether investors were misled. The subpoena is an investigation, not a finding of wrongdoing.

Source: https://oag.ca.gov/news/press-releases/attorney-general-bonta-serves-investigative-subpoena-nvidia

## Business, briefly

**Anthropic closed its first Nasdaq trading day at $97, 17 percent above its $83 IPO price.** Source: https://techcrunch.com/2026/11/19/anthropic-hits-nasdaq-exchanges-at-110-27-above-ipo-price/
