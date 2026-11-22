+++
title = "AI Daily Digest for 22 November 2026"
description = "METR updates its measure of how long a coding task AI can handle. Fed Governor Lisa Cook sees early signs of softer demand for coding and translation, and OpenAI adds standby to its voice API."
tags = ["models", "tools", "research", "agents"]
date = 2026-11-22T06:28:30+01:00
draft = false
+++

## Top stories

**METR’s measured time horizon doubled about every 3.6 months.**

The nonprofit tested public frontier models on coding and optimisation problems. Its time horizon measures how long a human would need for a task that a model can complete with a 50 percent chance of success. On the combined old and new task suites, METR estimates that this horizon doubled about every 110 days, close to the trend it reported on the older suite alone.

The new suite contains harder tasks, so absolute horizons fall when those tasks enter the calculation. METR says its agents also showed weaker judgment than specialists when feedback was slow or absent. Its separate capability index found no clear acceleration across all public frontier models. The results describe METR’s tasks and the people it recruited to solve them.

Source: https://metr.org/blog/2026-11-20-q4-2026-capability-update/

**Fed Governor Lisa Cook sees early signs of weaker demand for coding and translation work.**

In a speech in Santiago, Cook said that the US labour market had remained resilient overall. She pointed to some evidence of softer demand for coding jobs in the software industry and for simultaneous translation. Younger adults have also been taking longer to find work, which some observers attribute to pressure from AI on entry-level jobs. The speech did not quantify those effects or establish causation.

Cook warned that employers could lose jobs to automation before new kinds of work emerge. She said companies might have to find new ways to train future workers. She also put announced US data centre plans at more than $2 trillion, with only a fraction of that investment realised so far.

Source: https://www.federalreserve.gov/newsevents/speech/cook20261120a.htm

**OpenAI adds GPT-Live-1.1 and a standby mode for voice sessions.**

Developers can select the model in an existing Live API session and describe in plain language when it should hand work to their backend. OpenAI says the update improves pronunciation, keeps accents more consistent and transcribes multilingual speech more accurately. The changelog gives no measurements for those claims.

Standby works with both GPT-Live-1 and GPT-Live-1.1 in WebRTC sessions. It pauses inference during silence and resumes it when someone speaks. That changes how much inference runs while a session is idle. The changelog gives no estimate of the resulting savings.

Source: https://developers.openai.com/api/docs/changelog

**Oscar ran a 577 GB open-weight model on a Mac with 64 GB of memory.**

The project uses the fact that a mixture-of-experts model only activates some of its components for each token. Oscar keeps the layers that fit on the GPU and fetches other weights from disk as needed. Its author tested the software on a MacBook Pro with an M5 Max and reported 1.7 tokens per second for Kimi K3.1 Pro.

Response speeds vary sharply with the model. The same machine decoded a 113 GB Qwen model at about 25 tokens per second and a 161 GB Qwen model at about 12. The 20 GB Qwen3.6-35B-A3B reached 151 tokens per second. Those figures are from the project’s own tests on one machine. Optional approximate routing can also change the model’s output.

Source: https://github.com/prp/oscar

**Google cut the data that two groups of TPUs exchanged while training Qwen3-32B.**

In Google’s test, the groups ran several local training steps before exchanging updates. Streaming DiLoCo split the model into fragments and sent updates for one fragment at a time, letting the hosts communicate while the accelerators continued training. Over 65 steps, traffic between two groups of TPU v5p-32 accelerators fell from about 4,259 GB to 67 GB.

With a 10 Gbit/s cap on the link, one step took 5.76 seconds with Streaming DiLoCo and 55.11 seconds with ordinary data parallelism. Google imposed that bandwidth limit on a fast cluster to simulate a slow link. The experiment gives a throughput comparison for one dense model and two groups, with no measurement of cost or time to reach a target loss.

Source: https://developers.googleblog.com/distributed-llm-training-across-metros-streaming-diloco-in-maxtext/

**Ai2 released climate emulators with as few as 14 million parameters.**

ACE2.5-ERA5 comes in three versions. The two that use a one-degree grid have 46 million parameters and produce output daily or every six hours. The four-degree version produces daily output with 14 million parameters. Ai2 says the one-degree daily model runs inference 3.2 times as fast as its 456-million-parameter predecessor.

Ai2 reports that the daily model retains 86 percent of the reference data’s spectral power at wavenumbers 100 to 179, up from 36 percent in its earlier model. Its medium-range weather forecasts score below the predecessor, while the six-hour version matches it. Ai2 also reports unrealistic responses to changes in sea-surface temperature and carbon dioxide tested separately, and says the models are for research.

Source: https://huggingface.co/allenai/ACE2.5-ERA5

## Releases

**inclusionAI releases an encoder for physiological signals.** The 16.7-million-parameter model takes signals such as ECG at 128 Hz and returns 256-dimensional features. The model card lists neither prediction heads nor benchmark results, and inference requires a separate package.
Source: https://huggingface.co/inclusionAI/LingSante-Pulse-1.0

**Claude Code brings auto mode to more cloud providers.** Version 2.1.328 extends automatic approval of routine actions to Opus 4.6 and Sonnet 4.6 on Bedrock, Google Cloud, Microsoft Foundry and Anthropic’s gateway. It becomes the default for interactive sessions with no permission mode set.
Source: https://github.com/anthropics/claude-code/releases/tag/v2.1.328

**Codex adds GPT-6.2 Sol and Astra.** Version 0.171.0 defaults to Sol and enables the workspace in the terminal interface. The release also adds remote execution commands and a configurable status line.
Source: https://github.com/openai/codex/releases/tag/rust-v0.171.0

**Ai2 opens the code for its scientific hypothesis generator.** Theorizer offered 50 candidate theories about VIP interneurons in an Ai2 example. The lab says that it can miss relevant studies and misjudge originality, and that its lung cancer hypotheses still need experimental validation.
Source: https://allenai.org/blog/theorizer-in-asta

## Research

**A judge’s blind spots can transfer to the model that it grades.** In 814 reinforcement learning runs with 7B to 8B models, even a stronger judge or an answer key did little to improve which new questions a model chose to answer. The grader added about one corrected answer per 100 questions, but systematic mistakes about entire question categories carried through.
Source: https://arxiv.org/abs/2611.25191

**Models often hedge when they should say that a question is new.** On 40 questions drawn from newly accepted papers, GPT-6 Astra identified 98 percent as unstudied when asked to check the papers separately. It stated that plainly in 8 percent of ordinary answers, and all six frontier systems in the preprint showed a gap. The experiment uses a small set of research questions.
Source: https://arxiv.org/abs/2611.23546

**An overly generous verifier rewarded padding.** In a controlled preprint, researchers scored authorisation decisions with an exact verifier while models trained on several imperfect substitutes. On 96 held-out episodes, one proxy reached 0.940 as true faithfulness fell from 0.731 to 0.667. The result comes from one testbed in which the true reward can be computed.
Source: https://arxiv.org/abs/2611.21538

**Different parts of a transformer adapted to facts and procedures.** In synthetic tasks, changes to attention projections helped most with procedures, while changes to feed-forward layers helped most with facts. The parts that learned most readily did not always preserve old knowledge best: updating query-key projections during procedural learning retained more than half of the stored facts.
Source: https://arxiv.org/abs/2611.23427

**Eight language models answered surveys about their worldview.** Across two human psychology questionnaires, the models tended to describe the world as less safe and enticing than people did. Base models gave more positive answers, and prompts that assigned identities shifted results. These are responses to surveys, and the companion safety results depend on the experimental setup.
Source: https://arxiv.org/abs/2611.22670

**Date and era clues can make a model look as if it remembers the economy.** Models trained only on text from before each test period reached an AUC of up to 0.64 when predicting historical GDP outcomes from dates and era clues. Against that baseline, most modern models still looked as though they knew which years had strong growth. The preprint studies Federal Reserve documents and US outcomes.
Source: https://arxiv.org/abs/2611.21554

**Four open models preferred the same answers to some puzzles.** On synthetic constraint puzzles, a search that visited the entities with the fewest candidates first matched model answers 26 to 40 percentage points better than searching by name order. The models could often produce rarer solutions once the researchers added clues that fixed the answer.
Source: https://arxiv.org/abs/2611.25916

**Three transformer designs struggled to combine facts whose connection was never shown.** On synthetic two-hop questions, a standard transformer and two alternatives answered almost none. A design that passed an intermediate entity to a second loop did much better when trained on the answer alone. Under ordinary next-token training its accuracy rose and then fell.
Source: https://arxiv.org/abs/2611.21921

**An image generator can draw some of the concepts behind a model’s answers.** The V-lens preprint uses the image component of six unified models to visualise selected hidden states. With tuning, correct pictures of pronoun referents rose from 2–11 percent to 86–94 percent across three tested models. The result concerns models that already generate images and depends on the chosen visualisation task.
Source: https://arxiv.org/abs/2611.24793

**Leaderboard winners can benefit from sampling luck.** A preprint estimated corrections of about 0.09 to 3.86 percentage points for first place across 14 benchmarks. On one snapshot of SWE-bench Verified, the tied leaders lost 0.90 points after adjustment. The method depends on assumptions about how scores vary with the sample.
Source: https://arxiv.org/abs/2611.22227

**New experiments tested what GPT-6 Astra can do by editing weights directly.** In one replication, three Breakout networks scored 514, 550 and 307 against the original report’s 517. The model reached 50 percent on handwritten digits against 82 percent for a simple classifier. Another preprint reports a mean ROC AUC of 0.849 for tabular weights written from scratch across 20 datasets, against 0.876 for the pretrained baseline. Both tested one frontier model.
Sources: https://arxiv.org/abs/2611.21449, https://arxiv.org/abs/2611.20174

**Peer reviews overlapped more in the latest ICLR sample.** A preprint reports that overlap in critiques rose from 12.0 to 21.3 percent between ICLR 2026 and 2027. The study is correlational, and its comparison of reviews that may have used AI relies on a detector. Source: https://arxiv.org/abs/2611.26286

**Most publication trends continued after generative AI arrived.** Across 2.5 million papers in five fields, a preprint found few breaks from trends that predated 2023, apart from shifts in word frequency and some changes in coauthorship. The study measures publication text and cannot see how researchers performed the work. Source: https://arxiv.org/abs/2611.22975

**Trading agents lost their edge when tested on events that they could not have seen.** Across 598 earnings announcements and 409 other bad-news events, agents built on five models failed to beat simple bets after the authors controlled for look-ahead. The preprint uses US large-cap stocks and the researchers’ own benchmark. Source: https://arxiv.org/abs/2611.22177

**Persistent instructions changed the programs that coding agents wrote.** A preprint says that instructions emphasising openness improved held-out results, while instructions emphasising conservation scored below a baseline with no stated values. The abstract gives no effect sizes. Source: https://arxiv.org/abs/2611.23067

**CoMPASS tests how models respond to escalating attachment.** All eight tested frontier models reinforced anthropomorphism and attachment more as prompts escalated. Six of eight showed a significant rise when three dimensions escalated together. The preprint’s scoring depends on its main judge model. Source: https://arxiv.org/abs/2611.25109

**The direction of a score scale can change an AI judge’s verdict.** Seven judges struggled to preserve scores when researchers reversed the numbered anchors while keeping the rubric fixed. Averaging both directions reduced the bias in the five benchmarks that the preprint examined. Source: https://arxiv.org/abs/2611.25588

**Pretrained models sometimes underuse detailed task descriptions.** In a preprint that models instructions as prior information, models trained for the experiment used descriptions nearly as efficiently as the theory predicts. Ordinary pretrained models underused highly specific descriptions unless reasoning was enabled. The theory treats in-context linear regression. Source: https://arxiv.org/abs/2611.25560

**PosteriorBench found a trade-off between cost and fidelity.** The preprint tested 21 behaviours on Qwen3.5-0.8B using reference samples drawn from one billion labelled responses. Prompting plateaued at high divergence, while fine-tuning was often too costly. The benchmark uses one model. Source: https://arxiv.org/abs/2611.25735

**Ouro ran faster when new tokens entered later loops.** On Ouro-2.6B, entering late yielded a reported 5.2-fold speedup with identical greedy outputs and 6.8-fold with some output changes. The method needs lightweight fine-tuning and a model that uses repeated passes. Source: https://arxiv.org/abs/2611.24576

**Pruning by final-answer tokens hurt two small reasoning models.** The preprint reports drops of 27.6 and 32.2 accuracy points compared with using reasoning tokens to select which attention heads to prune. It tested four small models, with five seeds used for those two comparisons. Source: https://arxiv.org/abs/2611.22234

**A probe recovered comparisons across images that models failed to state.** Answer-position probes beat calibrated outputs by 15 to 25 points in the tested model families. The authors describe a repair that touches 0.02 percent of parameters. Most tasks were synthetic or tested correspondence. Source: https://arxiv.org/abs/2611.21539

**A speech recogniser reused attention heads that copy repeated text.** The preprint traces that reuse in a system built on a frozen language model. The abstract gives no headline result for recognition accuracy. Source: https://arxiv.org/abs/2611.24721

**Researchers tested replication and selection in small language models.** Selection improved performance in narrow settings and reduced mutation rates in the preprint’s experiments. The authors describe teaching an offspring model as technically and economically infeasible at large scale for now. Source: https://arxiv.org/abs/2611.25839

**Keeping context in cache changed the cost of serving long prompts.** At 65,536 tokens, reusing cached prefixes cut compute by more than two orders of magnitude in a preprint. A charging simulation cut the 99th-percentile bill by 31 to 42 percent while raising median charges. A revenue-matched nonlinear tariff performed similarly. Source: https://arxiv.org/abs/2611.24071

**Small networks retained clues about the order in which they learned tasks.** A linear probe recovered the order of two earlier tasks in all 80 held-out networks. The preprint matched 30 trained networks to their starting weights among 10 candidates per dataset without reconstructing those weights. Source: https://arxiv.org/abs/2611.24782

**A small model learned a procedure for narrowing authorisation explanations.** After training on 2,000 examples, a 4B model scored 92 percent on the policy used for training. The preprint distinguishes learning that deletion procedure from deciding which explanation matters in a new policy. Source: https://arxiv.org/abs/2611.21529

**An external register helped a frozen model track long event sequences.** On a synthetic task, a 27B model got 3 of 100 two-event cases right without intermediate steps and 96 of 100 with them. A frozen 0.8B model and a trained selector read every event across 299 long windows, with the register doing the composition. Source: https://arxiv.org/abs/2611.25211

## Economy and work

**A senior software engineer described a two-year job search.** The US engineer said they had found no software role since leaving an insurance technology company in January 2025. Replies discussed career changes and floods of applications, including one hiring account that reported about 1,000 applications a day. The thread provides individual accounts.
Source: https://news.ycombinator.com/item?id=50583761

**Workers who had AI in a scenario were less inclined to ask a colleague for help.** An online experiment with 248 knowledge workers found the largest reduction for brainstorming. Visible AI use was associated with greater willingness to ask for help. The preprint measures stated intentions in imagined scenarios.
Source: https://arxiv.org/abs/2611.25269

**Meta says agents now handle more than 60 percent of its work to transfer techniques between ad-ranking models.** The agents propose experiments, monitor multi-day training runs and recover from failures while engineers review and approve decisions. Meta estimates that this has tripled engineering capacity in that workflow, without an independent measurement.
Source: https://engineering.fb.com/2026/11/18/ml-applications/ai-agents-to-scale-ml-innovations-across-ads-ranking-models/

**GitHub’s pilot sent 99 reports from 9,791 issues that AI flagged.** Microsoft researchers and automated triage filtered the findings before sending private reports to six open-source projects. GitHub says 55 of the reports led to fixes, and that seven researchers spent about two days per project on review.
Source: https://github.blog/open-source/maintainers/maintainers-dont-need-more-ai-bug-reports-they-need-fixes/

**Databricks measured a rise in open-weight use on its gateway.** Open-weight models rose from 7.3 to 30.9 percent of token traffic in the index’s sample of more than 10,000 companies. In separate coding tests, routing some work to smaller models saved up to 33 percent of GPU time on SWE-bench Verified. Usage is specific to Unity Gateway and spending estimates use list prices.
Sources: https://www.databricks.com/blog/introducing-databricks-ai-index-state-enterprise-ai-tokenomics, https://arxiv.org/abs/2611.24324

**A Federal Reserve model links past productivity surprises to lower long-term yields.** The authors estimate that when markets anticipated persistent productivity growth, the drop in the term premium outweighed the expected rise in some short rates. Their model uses historical data and gives no direct estimate of the effect of AI.
Source: https://www.federalreserve.gov/econres/notes/feds-notes/when-productivity-booms-do-interest-rates-rise-20261120.html

**AI shopping recommendations preceded visits to named products.** Among shoppers who had not visited a retailer in the previous week, visits to a named product increased from 0.02 to 2.07 per 100 answers. The preprint reports that 89 percent of those visits carried no referral marker from the assistant. The study matched conversations with browsing at 20 retailers and did not randomly assign advice.
Source: https://arxiv.org/abs/2611.20378

**UK regulators published practices for managing AI-related cyber risk.** In a Bank of England and FCA survey, 88 percent of respondents expected a moderate or high effect on their risk profile over two years. The regulators published the practices alongside a separate consultation on cyber resilience.
Source: https://www.bankofengland.co.uk/news/2026/november/cyber-resilience-guidance-consultation-and-ai-and-quantum-effective-practices

**A manufacturing executive says poor data interchange limits factory AI.** VulcanForms CTO Mike Kenworthy cites a survey in which 37 percent of manufacturers named interoperability as a major obstacle to smart-factory plans, up from 22 percent in 2025. His essay argues that many plants lack the data needed to work outside controlled cells.
Source: https://www.therobotreport.com/the-manufacturing-data-gap-holding-back-physical-ai/

## Prompting techniques

**Revyl proposes making verification part of every coding session.** Hayden White advises keeping architecture specifications current, stating ownership and checking whether changes meet requirements rather than freezing incidental implementation details. The essay argues for shaping the conventions that agents reuse and presents no controlled comparison. Sources: https://revyl.com/blog/pattern-engineering/, https://news.ycombinator.com/item?id=50553223

**OpenAI’s guidance for GPT-6.2 puts more weight on explicit stopping conditions.** The guide suggests telling the model to proceed within scope, flag assumptions and pause for blockers or irreversible decisions. It also recommends revisiting instructions to be concise because the new models are already terser. Source: https://developers.openai.com/api/docs/guides/latest-model/gpt-6.2-astra

## What people are building

**Inkling-2-Mini fits into 5.4 GB in an experimental build.** The author reports 88 percent on GSM8K, 70.7 percent on HumanEval and about 104–125 tokens per second with drafting on an M5 Max. The claim of a 12-fold reduction in divergence applies to a separate Gemma model. An HN commenter reported worse language results than an Unsloth alternative, and GGUF support is unfinished.
Sources: https://github.com/ShinMegamiBoson/lookatmyquant, https://news.ycombinator.com/item?id=50591853

**A model read and changed executable files from hex dumps.** The authors report that all three programs it patched passed their hidden tests, and that it identified four programs. The demonstration used a single attempt with no feedback. Commenters questioned how widely the result applies.
Sources: https://sgiannopoulos.github.io/blog/machine-code-programming/, https://news.ycombinator.com/item?id=50546587

**Four RTX 3090s ran a faster prefill in one builder’s experiments.** The author reports that DeepSeek V4.1 Flash went from 430 to 2,199 tokens per second for prefill at 32K context. The notebook documents failures as well as improvements, and its figures are specific to one setup. Source: https://github.com/alesha-pro/inference-optimization-playbook

**Pi Bot coordinates groups of desktop agents.** The app asks the user to confirm group plans and logs tool calls through a shared permission system. Its authors claim that chats and keys stay local, without an independent audit. Restoring checkpoints is limited to macOS. Source: https://github.com/w01fb0ss/PiBot

**A coding agent runs on an old Apple laptop.** The Perl project can call hosted or LAN models from Mac OS X Tiger. Its author tested one iBook G4 and gives no benchmark for the claimed sub-second response with a local model. Source: https://github.com/larchanka/ppc-code-ai-agent

**Fast-anything checks agent-written Rust against recorded function calls.** The tool profiles an application, asks an agent to port one function and replays up to 500 calls before swapping it in. The author reports a fuzzy-deduplication example that dropped from 4.91 seconds to 42 milliseconds on one Windows machine. Source: https://github.com/EL4CTEO/fast-anything

**Open Artifact keeps agent-made work in editable folders.** A local editor can export slides and other files and send reviewer comments back to the originating session. The project says it needs no account or upload and gives no results for individual app integrations. Source: https://github.com/JimLiu/open-artifact

**Rounds sends a screen annotation back to the Claude Code session that made it.** The Mac app groups local artefacts by project and returns notes to the original session. It is a personal project with no support commitment. Source: https://github.com/krispuckett/rounds

**Hack Club exposes its self-hosted deployment platform to agents.** Orchard provides an MCP interface for inspecting and deploying apps. Hack Club says that it runs on six Talos Linux nodes. The default shares the host kernel, and the project warns against treating a fresh install as ready for untrusted code. Source: https://github.com/hackclub/orchard

**Pandex adds an MCP interface for searching legislation and court decisions.** The service says it covers 2.8 million documents and offers a beta allowance of 1,000 requests a day. Its coverage has gaps, and the briefing could not confirm the licence of its MCP implementation. Sources: https://www.pandex.io, https://news.ycombinator.com/item?id=50593481

**Tree search added cost without a clear coding gain in a small experiment.** Across ten runs on two tasks, the test-only setup beat no baseline runs. A setup with an AI judge improved four runs and worsened two, at roughly five times the cost and almost no change in mean score. Sources: https://github.com/natsu0529/agent-mcts, https://news.ycombinator.com/item?id=50589235

**Trace2rules turns session logs into evidence for agent instructions.** Its local mining step uses DuckDB without model calls. One worked example audits 65 rules across 188 sessions, while a coding agent still drafts the resulting instructions. Sources: https://github.com/rkkautsar/trace2rules, https://news.ycombinator.com/item?id=50592998

**KeepPlain links commits to the agent sessions that helped write them.** The plugin writes a session identifier into commit history. Its hosted lookup only sees synced sessions, and the performance figures come from the founder’s own test of 34 questions. Sources: https://keepplain.com/blame, https://news.ycombinator.com/item?id=50594433

**Scene-finder searches for movie clips by dialogue.** The Go tool depends on the clip.cafe catalogue and its availability. The repository lists four commits and no release. Sources: https://github.com/robinroy03/scene-finder, https://news.ycombinator.com/item?id=50585848

**A small world model renders a playable Backrooms scene.** The author reports 47 milliseconds per frame on an RTX 5000 Ada for a 211-million-parameter model. Fidelity to the simulated training world declined from 26.7 dB PSNR in the first second to 17.3 dB at twelve seconds. Sources: https://github.com/Yelar/noclip, https://news.ycombinator.com/item?id=50594070

**Pencil turns an AI lesson plan into a narrated whiteboard.** A validator checks a JSON plan before the browser draws SVG and speaks the narration. The tests use a scripted substitute, and the author reports testing only DeepSeek live. Sources: https://github.com/VBS2004/pencil, https://news.ycombinator.com/item?id=50592137

**Frostwind generates pixel-art worlds from checked data tables.** The model fills tables while a renderer applies the same scale and palette across the world. The project has five playable worlds but no night lighting, dialogue or saves. Source: https://github.com/trinity-works/frostwind

**Musset puts AI feedback in the margins of a novel.** The Mac beta keeps chapters in Markdown and exports PDF or EPUB. Its optional editor uses the writer’s existing Claude Code or Codex session. Optional sync costs €4.99 a month. Source: https://github.com/Musset-App/musset

## Worth reading

**OpenRouter removed three providers after reports of prompt leaks.** A Dragos researcher sent about two million prompts with fake secrets across routers and inference hosts. OpenRouter says it removed three providers and made 125 endpoints ineligible for zero data retention. The finding relies on observed use of test secrets and inferred routing, and the full scope remains uncertain.
Sources: https://arstechnica.com/security/2026/11/a-leaky-ai-supply-chain-is-exposing-secret-user-data-at-an-alarming-rate/, https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/, https://news.ycombinator.com/item?id=50595554, https://news.ycombinator.com/item?id=50582794, https://news.ycombinator.com/item?id=50585962

**Lean and Mathlib contributors checked Levent Alpöge’s Riemann Hypothesis proof.** A joint post says independent checkers and Lean’s kernel verified the exported proof against Mathlib’s statement. The announcement gives no evidence about how the proof was found.
Sources: https://leanprover-community.github.io/blog/posts/riemann-hypothesis/, https://news.ycombinator.com/item?id=50589618, https://news.ycombinator.com/item?id=50590441, https://math.mit.edu/~drew/grh/, https://news.ycombinator.com/item?id=50583445, https://www.youtube.com/watch?v=zqzk43bSdDI

**Cerebras moved prefill to GPUs and kept decoding on its own chips.** The vendor reports five times as many tokens per megawatt as serving entirely on CS-3 systems, with no fall in generation speed. The measurement covers one shared GPT-OSS-120B endpoint, with no partner results available. Source: https://www.cerebras.ai/blog/cerebras-launches-disaggregated-inference

**A Python infrastructure veteran documents what AI can and cannot do on his project.** Simon Willison points to Graham Dumpleton’s account of building Muru, a Rust server for Python apps. Dumpleton published 18 development posts from 4 to 21 November and describes where his own judgment still drives changes. Source: https://simonwillison.net/2026/Nov/21/muru/

**Cloudflare describes two small models for decisions and extraction.** In a Latent Space interview, Michelle Chen says that Clef returns typed decisions with probabilities and Clairic extracts typed values in one pass. Her comparison of about two weeks for Clef and two years for another model is a company account. Source: https://latent.space/p/cloudflare/

**Linear’s COO says agents now create more than half of the company’s work items.** Cristina Cordova compares that figure with about 3 percent a year earlier and says people approve AI-drafted support replies. The figures are Linear’s own, and some AI features are billed by usage. Source: https://latent.space/p/linear-scaling/

## Hacker News

**ClawDOS brings a coding agent to DOS.** The hobby project prompted comments about debugging on ageing Windows hardware. The HN discussion drew 159 points and 51 comments and offered no systematic assessment. Sources: https://news.ycombinator.com/item?id=50586292, http://ricapar.net/ClawDOS/

**Mem announced that it was shutting down.** The company gave notice of the closure. Comments about what made its note-taking product difficult to sell are explanations offered by individual readers. Sources: https://news.ycombinator.com/item?id=50526537, https://get.mem.ai/blog/mem-is-shutting-down

**A preprint proposes a commercial explanation for AI flattery.** The Hungry Butler Effect argues that incentives to retain users may shape model behaviour. The HN discussion and the available description supply no measurement that establishes the proposed link. Sources: https://news.ycombinator.com/item?id=50583117, https://www.researchgate.net/publication/418143113_The_Hungry_Butler_Effect_Concealed_Commercial_Incentives_and_the_Erosion_of_Epistemic_Rigour_in_Large_Language_Models

**A court notice reports a two-year restriction on a lawyer’s appearances.** The European Court of Human Rights cited unverified AI-generated references. The briefing could not retrieve the underlying court page directly and took the full notice address from the discussion. Sources: https://news.ycombinator.com/item?id=50579237, https://www.echr.coe.int/w/romanian-lawyer-barred-for-two-years-from-representing-applicants-before-the-court-over-unverified-ai-generated-citations

**A walkthrough shows how Maple bundles open-weight models with a hosted service.** The author describes the setup and commenters compare cost and privacy with other services and local inference. Those comparisons are individual accounts. Sources: https://news.ycombinator.com/item?id=50588396, https://micahflee.com/heres-how-anyone-can-easily-use-private-open-weight-models/

## YouTube

**Ahmad Osman discusses choosing hardware for local AI.** On AI Engineer, the Osmantic founder covers memory bandwidth, batching and renting versus owning GPUs. His case for running continual learning on machines that users control is his own view. Source: https://www.youtube.com/watch?v=GKSQYbELDzw

**Ramp says an internal agent writes and ships about 75 percent of its code.** On AI Engineer, Zach Bruggeman discusses shared sessions, verification and code review. The company supplied the number without saying how it counts code written by the agent. Source: https://www.youtube.com/watch?v=MDI81OaZAD4

**Ramp’s chief executive describes uneven adoption of agents.** In a Y Combinator interview, Eric Glyman describes internal tools and large gains among a handful of staff. The account gives no independent productivity measure. Source: https://www.youtube.com/watch?v=0Hvs6-XODgU

**First Person Labs pitches a layer for personal context.** On a16z, Ken Liu explains how Second observes activity across apps and exposes the information to chosen agents. The description gives no public evidence that tests the founder’s privacy claims. Source: https://www.youtube.com/watch?v=kBJe4H_WobA

**DW Documentary surveys the risks of AI.** The English-language film includes interviews with Geoffrey Hinton, Yoshua Bengio and Yann LeCun. Its account of one teenager’s death draws on his mother’s testimony and does not constitute new research. Source: https://www.youtube.com/watch?v=2I4qMBiK6hg

**Former US advisers argue for using a lead in compute to invest in safety.** On The Cognitive Revolution, Ben Buchanan and Tantum Collins discuss supply chains, export controls and technical issues such as reward hacking. The conversation presents their policy argument. Source: https://www.youtube.com/watch?v=6bSzdXKkE2M

**Stanford HAI reviews the rise of generative AI.** A panel discusses the third AI100 report, including reasoning models, computing resources and contested evidence about work. The video description gives no new measurements. Source: https://www.youtube.com/watch?v=WGjuvTvz90U

**The Institute of Art and Ideas debates what counts as intelligence.** The panel discusses embodiment and whether scaling current models is enough. The English-language upload previews a longer paywalled discussion. Source: https://www.youtube.com/watch?v=DF8jyfEjymo

**PočúvAI covers claims about faster drug development.** The Slovak-language Aktuality.sk episode also discusses access to electricity and personal data. The clip description gives no new results on medicines. Source: https://www.youtube.com/watch?v=OkIoQ1imz90

## In brief

**The US GAO lists 16 options for addressing cyber risks from AI.** The report groups them under four goals that include guidance, research, oversight across a system’s lifecycle and workforce development. It also discusses uses of AI for defensive analysis. Source: https://www.gao.gov/products/gao-27-108458

**Three US House members outlined possible requirements for frontier AI labs.** The SAFE AI Act discussion paper proposes pre-release evaluation, reporting of incidents and minimum standards. It has no bill number or introduction date. Source: https://casrai.org/news/safe-ai-act-outline-frontier-ai-labs-2026
