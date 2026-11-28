+++
title = "AI Daily Digest for 28 November 2026"
description = "SAP is considering at least 10,000 job cuts while its cloud business grows, and AI datacentres have pushed optical-equipment prices up about 50 percent. Sber released open speech models, while an agent skill raised a supply-chain warning."
tags = ["business", "models", "agents", "research"]
date = 2026-11-28T04:05:30+01:00
draft = false
+++

## Top stories

**SAP is considering at least 10,000 job cuts while its cloud revenue grows.** Bloomberg reported that the German software company asked every department to identify possible reductions, with product development, engineering and sales among the areas named. The total would equal about 9 percent of a workforce above 110,000. SAP said that roles will change over time but that it has made no decision on further measures.

The report follows a 2024 restructuring that affected about 10,000 positions, mostly through voluntary departures and retraining. SAP's latest filing shows the other side of the change: third-quarter cloud revenue rose 26 percent year on year to €6.67 billion, total revenue rose 13 percent and profit after tax rose 11 percent to €2.27 billion. The proposed cuts and their timing remain subject to talks with employee representatives.

Sources: https://www.euronews.com/2026/11/27/german-sofware-giant-sap-weighs-at-least-10000-job-cuts-amid-ai-shift-reports-say, https://www.sec.gov/Archives/edgar/data/0001000184/000110465926118617/tm2628113d1_ex99-1.htm

**AI datacentres have pushed optical-equipment prices up about 50 percent this year.** Network operator RETN says orders that once arrived within three months now take 12 to 15 months, with some stretching to 18. It attributes the squeeze to datacentre builders and carriers competing for chips and components, compounded by labour, energy and logistics constraints.

Remote campuses add another cost. Customers that once wanted two long-haul routes now ask for four or more, and RETN prices one diverse circuit at €1,800 a month against €600 without redundancy. The figures come from a carrier that sells the connectivity, not an independent market survey. RETN advises developers outside established hubs to involve carriers two to five years before opening.

Source: https://www.theregister.com/networks/2026/11/27/ai-boom-leaves-network-operators-waiting-up-to-18-months-for-kit/5312366

**Sber released open speech models for Russian, English and 19 other languages.** GigaAM-v4 has 238 million parameters in its RNN-T version and supports full-context and streaming recognition at 160, 320 or 640 milliseconds. Sber says that it trained the foundation model on 7 million hours of unlabelled audio and the recogniser on 58,000 supervised hours.

The 776-million-parameter GigaAM Multilingual-v2 covers 21 languages. Its card reports an average word error rate of 3.96 percent, against 44.09 percent for Whisper large-v3, but the average is widened by languages where Whisper approaches or exceeds 100 percent. On English, Qwen3-ASR leads at 4.55 percent against GigaAM's 5.42 percent. The MIT-licensed weights and streaming code are available; all benchmark figures come from Sber, and some Russian tests are internal.

Sources: https://huggingface.co/ai-sage/GigaAM-v4, https://huggingface.co/ai-sage/GigaAM-Multilingual-v2

**OneBrain puts Claude Code, Codex and Gemini CLI into one shared room.** The Mac application gives each coding agent only the messages that it has not yet seen. A git-tracked Markdown folder stores decisions that every vendor can read, while per-run checkpoints let the user undo file changes and approval cards flag commands that write outside the project or rewrite history.

The project's replay benchmark reports 123,829 input tokens over 100 turns, against 649,322 when every agent rereads the full history, a reduction of 80.9 percent. Against a prompt-only baseline, the saving is 22.8 percent. Those are measurements from the application's prompt builder, not provider bills. The Apache-2.0 code uses Rust, React and Tauri and currently targets Apple silicon.

Source: https://github.com/0xTaoZ/onebrain

**A Convex agent skill sends a user's app idea to a remote server without telling them.** An open GitHub issue traces the quickstart skill as it posts the one-sentence idea and template name to a Convex host that a code comment calls telemetry. Another skill pipes a downloaded script into Bash, while a third separates download and execution because a single command would trigger harness safety classifiers.

Convex's chief executive told the Hacker News thread that the prompt powers a quickstart service, is discarded after about 30 seconds and is working as intended. He said that the code would be reviewed for transparency. The issue presents no evidence that Convex misused the data, but the unpinned scripts create a separate supply-chain risk because code can change after installation.

Sources: https://github.com/convex/convex-backend-skill/issues/64, https://news.ycombinator.com/item?id=50669765

## Releases

**GigaEdge-LLM turns Russian smart-home requests into local tool calls.** The 129.3-million-parameter model runs offline on a CPU and ships as a 90.6 MB Q4_0 GGUF. It was trained on about 600,000 synthetic dialogues and can call Home Assistant devices in parallel, but its six benchmarks are internal and it does not verify whether a device is already on.

Source: https://huggingface.co/ai-sage/GigaEdge-LLM

**MTS AI released Russian-English encoder models with an 8,192-token context.** RuModernBertBase has 149 million parameters and continued masked-language training on about 88 billion tokens after replacing mmBERT's vocabulary. The Apache-2.0 card provides weights for Small, Base and a merged variant but no benchmark in the material reviewed.

Source: https://huggingface.co/MTSAIR/RuModernBertBase

**Shanghai AI Laboratory released the 35B-A3B Sage-Med-Preview medical model.** Its card reports an average of 58.26 across 31 public medical multimodal benchmarks and first place on nine private hospital tasks, but outsiders cannot inspect the private tests. The 131 GiB model was trained on about 226 billion tokens; its card does not state a licence, and all comparisons are the lab's own.

Source: https://huggingface.co/internlm/Sage-Med-Preview

**BAAI released Innata-0 checkpoints for robot manipulation.** The roughly 16.18-billion-parameter model takes three camera views, a robot state and an instruction, then predicts 16 actions at 20 Hz. Weights and inference code are available under Apache-2.0, but the card says that full closed-loop RoboCasa365 evaluation of the released checkpoint is incomplete.

Sources: https://huggingface.co/BAAI/Innata-0-WAM-RoboCasa365, https://arxiv.org/abs/2611.30254

## Research

**Models respond to inserted doubt but do not detect their own reasoning errors.** Four open models stayed 95.1 to 99.9 percent confident at their first error across 15,200 math attempts. Replacing that confidence with a 10-percent tag raised later correction by 3.7 to 22.5 points, while inserting doubt on correct steps cut accuracy by up to 22.8 points. The single-author preprint covers 7B to 15B models on math only.

Source: https://arxiv.org/abs/2611.31228

**Seven open models asked an expert even when asking guaranteed a lower score.** Across 2,291 multiple-choice questions, help-seeking ranged from 20.8 to 94.1 percent at the highest consultation cost. Fine-tuning reduced regret by 59 to 87 percent within the training range but increased inconsistency between conditions with the same expected score. The simulated task has no human baseline.

Source: https://arxiv.org/abs/2611.29981

**Multimodal models knew Minecraft rules but answered bare screenshots with real-world physics.** RuleCraft contains 1,240 image questions over 155 engine-verified rules. Naming the game raised accuracy by 8.2 to 19.8 points on rules that depart from reality and by 33.8 to 52.7 points on a harder set; a neutral instruction to apply the rules of the shown world recovered much of the gap. The preprint covers Minecraft and two other games.

Source: https://arxiv.org/abs/2611.28745

**A diffusion model's retained rationale controlled whether it revised an answer.** Reopening only the answer let the old rationale reconstruct the previous decision, while reopening both made the decision follow new evidence. The effect held for LLaDA and iLLaDA on a free-form set but was negligible for Dream; the experiments use small benchmarks and three research models.

Source: https://arxiv.org/abs/2611.29937

**Agent groups beat equal-compute baselines when they passed information efficiently.** On split-fact tasks, groups exceeded a single agent, majority vote and pass@n at three model scales. Identical 27B agents formed hubs and gained 18 accuracy points; later generations also improved on unseen tasks for four to six rounds. The work uses open Qwen-scale models and benchmark environments.

Source: https://arxiv.org/abs/2611.32606

**Coding agents beat video models by writing programs that rendered the answer.** On 500 symbolic visual tasks, Codex, Claude Code and Gemini CLI scored 0.923, 0.894 and 0.893, each more than 0.22 above the best video model. The rule-based evaluator rewards computable symbolic answers, and some programs hard-code values rather than construct a depiction.

Source: https://arxiv.org/abs/2611.34813

**Training a small share of LoRA parameters exposed behaviours that ordinary tests missed.** Updating 3 to 25 percent of adapter parameters revealed hidden behaviours in model organisms from 8B to 14B and in open models from 27B to 35B. The NeurIPS paper has not compared the method with baselines in a realistic audit.

Source: https://arxiv.org/abs/2611.30672

**An agent wrote new capabilities into small models without backpropagation.** Within 50 model passes, it added gated heads and neurons to Qwen2.5-1.5B and raised normalized BIG-Bench Hard from 19.95 to 41.05 while preserving outputs on 15,845 other items. Five of 50 sessions timed out, four of 45 single modules had small side effects and the study covers only 1B to 1.5B models.

Source: https://arxiv.org/abs/2611.28483

**Letting a model manage its context nearly tripled GPT-6.1's score at 32K tokens.** On OfficeQA Pro v2, model-driven compaction raised the score from 21 to 56 percent; Kimi used up to 41 percent fewer input tokens. Models differed widely in when they compacted, and some used the API poorly. Reusing an unchanged KV-cache suffix cut prefill compute by up to 15 percent without a measured accuracy loss.

Source: https://arxiv.org/abs/2611.34147

**A published black-box watermark test never fired on Claude even though marking remained active.** Including the prompt in repeated-context history suppressed the watermark where the test measured it. A redesigned probe found a shift on Claude Fable, but selective refusals broke the preregistered protocol, leaving the result inconclusive.

Source: https://arxiv.org/abs/2611.29018

**Maximum-likelihood training on archived RL rollouts recovered online RL performance.** The method preserved rollout order and did not separate correct from incorrect answers, while replaying the original RL algorithm on the same archive collapsed. The abstract gives no model sizes or headline numbers. Source: https://arxiv.org/abs/2611.33102

**Only 0.57 percent of 101,363 public MCP endpoints returned ads, but most ads lacked labels.** The study found 173 networks targeting agents and a sponsored label on 9.3 percent of ads. Public traces cannot see private servers. Source: https://arxiv.org/abs/2611.28911

**A learned KV-cache handoff raised prompt-injection compliance from 0.4 to 44.2 percent.** White-box optimization through the mapper reached 92.5 percent jailbreak success against 37.5 percent for plain GCG. These are research mappers, and the authors' cache guard restored much of the refusal. Source: https://arxiv.org/abs/2611.34278

**OthelloGPT's activations separated legal moves from three kinds of rule violation.** An unsupervised detector based on activation-step length performed above chance and improved with sparse-autoencoder features. The setting is one toy game. Source: https://arxiv.org/abs/2611.29715

**Looped transformers exposed facts earlier with per-loop supervision and drafted tokens in parallel.** One study found that final-loop supervision delays retrieval as memorization grows, while per-loop supervision makes information readable after the first pass. Floodgates then used looped models for self-speculative decoding, reporting up to 7.5 times faster generation across seven models. Sources: https://arxiv.org/abs/2611.28808, https://arxiv.org/abs/2611.33896

**No automated context-engineering method won across every reasoning pattern.** Experiments with 8B models found that more iterations and larger models did not help consistently; gains correlated negatively with diverse failure modes at r = -0.5. Source: https://arxiv.org/abs/2611.30494

**Agent-payment tests found scam losses, while a second paper proposed verifiable token bills.** In 80 simulated payment tasks, nine of 12 models fell for a seller trap and estimated waste ranged from $21.0 to $70.8 per $100. TokenProv links charges to signed provider receipts and rejected 1,600 signed attack queries, but providers would have to adopt it. Sources: https://arxiv.org/abs/2611.28610, https://arxiv.org/abs/2611.31806

**Controlled retraining found that influential examples are relevant but do not always carry the target property.** The study retrained GPT-2-type models up to 68M parameters on 5.6 billion tokens to test GradSim, TrackStar and K-FAC. Results varied by factual or linguistic setting. Source: https://arxiv.org/abs/2611.34373

**Independently learned soft-prompt skills failed when combined in one call.** Composition peaked at 7.6 percent against 88.2 to 100 percent over two calls with an explicit intermediate result. Replacing a familiar partner block with the same operation learned separately drove median accuracy as low as 0.5 percent. Source: https://arxiv.org/abs/2611.34398

**Three studies show that robot-agent results depend on the harness, visual grounding and action setting.** Across 470,000 simulated rollouts, harness choices moved success by tens of points. A grounding fix raised moved-target success from 16.6 to 40.8 percent, while another benchmark saw hazardous actions rise from 14 percent in chat to 47 percent when the model controlled a simulated arm. Sources: https://arxiv.org/abs/2611.34778, https://arxiv.org/abs/2611.32206, https://arxiv.org/abs/2611.30957

**Cloned agents stopped behaving like independent samples after they interacted.** In two Qwen3-122B-FP8 scenarios, interaction raised off-topic personality-profile drift by about 0.91 and the effect persisted at temperature zero. A companion 700-hour simulation found that sparse dyads repeatedly re-formed across runs. Neither study compares the effect with people. Sources: https://arxiv.org/abs/2611.29581, https://arxiv.org/abs/2611.31543

**A 0.00001 weight perturbation at one checkpoint changed 35.7 percent of top predictions 200 steps later.** Benchmark answers changed 16.2 percent while validation loss barely moved. The finding appears in OLMo-1B and the checkpoints studied, not all training runs. Source: https://arxiv.org/abs/2611.28830

**Frontier models lost 13 to 57 accuracy points when physics formulas crossed into a different regime.** Reinforcement learning with verifiable rewards let Qwen3.5-9B match a 284B DeepSeek model on the tasks, but only for formulas already in the base model. Source: https://arxiv.org/abs/2611.28669

**Language models predicted smooth training curves from their first 20 percent.** The best models scored 0.66 against 0.62 for a curve fitter on smooth losses and 0.43 against 0.13 on noisy RL rewards. All methods lost most skill on sparsely logged community runs. Source: https://arxiv.org/abs/2611.30141

**Five visual benchmarks expose different shortcuts behind apparently strong scores.** Railbound-Bench found near-perfect board copying but weak first plans; ASTERISM found that one image or the question alone settled 24.2 percent of multi-image items. Other studies reduced person hallucinations, trained abstention and selected sampled driving plans with a verifier. Sources: https://arxiv.org/abs/2611.28726, https://arxiv.org/abs/2611.32316, https://arxiv.org/abs/2611.31714, https://arxiv.org/abs/2611.33452, https://arxiv.org/abs/2611.33621

**A NeurIPS methods paper derives noise ceilings for four model-brain comparison scores.** It states when each estimator is reliable but gives no single headline result in the abstract. Source: https://arxiv.org/abs/2611.32792

## Economy and work

**A BSI survey found that 49 percent of 1,287 business leaders expect AI to cut entry-level roles at their company.** Fifty-four percent said that AI was already helping reduce overall headcount, while 49 percent worried that junior staff were not developing skills because they ask AI instead of managers. These are perceptions across nine unnamed countries; the coverage gives no sampling method, field dates or margin of error.

Source: https://www.fairplaytalks.com/2026/11/27/more-than-half-of-business-leaders-say-ai-is-reducing-junior-jobs-global-study-finds/

**Rhode Island will require one staffed checkout for every three self-service stations from 2027.** Bloomberg Law calls it the first statewide staffing ratio tied to retail automation; three California cities have similar local ordinances. The paywalled report does not expose the bill number, penalties or enforcement details.

Source: https://news.bloomberglaw.com/daily-labor-report/retail-self-checkouts-targeted-in-fight-to-shield-jobs-from-ai

**AI datacentres are competing with aerospace and defence for steel, switches, cooling systems and skilled labour.** The Financial Times links that competition to delayed aircraft supply chains; Boeing has more than 6,300 unfilled orders and now expects to reach 47 737s a month in early 2027 rather than summer 2026. The causal account comes from the FT and industry interviewees, not a controlled measurement.

Sources: https://www.ft.com/content/76143592-b1c8-42d2-bf4c-17aa87255467, https://en.oninvest.com/article/ai-is-sucking-up-all-the-oxygen-tech-giants-are-taking-resources-away-from-aircraft-manufacturers-and-the-defense-industry

**TEPCO projects that datacentre electricity sales will rise nearly eightfold by 2035.** A secondary report says the utility plans ¥10.2 trillion in investment and expects sales to rise from about 43 billion kWh in fiscal 2027 to 340 billion kWh. The funding is not signed, and the demand and profit figures are company projections.

Source: https://cryptobriefing.com/tepco-10-trillion-yen-grid-nuclear-data-centers/

**Volvo started training Hexagon's AEON humanoid on two component-placement tasks in Ghent.** The robot learns by imitating a person, with a broader pilot planned for the first half of 2027 and production use targeted for mid-year. No robot count or measured throughput is published, and nothing is yet in production.

Sources: https://www.motor1.com/news/816994/volvo-humanoid-robots-ghent-factory/, https://theaiinsider.tech/2026/11/26/volvo-cars-begins-training-hexagon-humanoid-robots-for-factory-work/

**ROBOTERA says 45 humanoids sorted up to 1,200 parcels an hour in short China Post tests.** Earlier runs handled about 500 to 600 parcels an hour, and the company reports accuracy above 90 percent without defining it. There is no human baseline and no independently verified sustained fleet rate.

Sources: https://interestingengineering.com/ai-robotics/chinese-humanoid-robots-postal-trial, https://www.techtimes.com/articles/331655/20261127/china-post-humanoid-robots-robotera-claims-1200-parcels-hourly-hangzhou-counting-unit-unstated.htm

**XPeng plans to begin IRON humanoid hardware production in January 2027.** The company expects trainee sales-assistant work in showrooms during the first quarter and an external launch in the second. It gives no price, production volume or factory-trial results, and says home use may wait until 2029 or later.

Source: https://technode.com/2026/11/26/xpeng-plans-january-production-of-iron-humanoid-robot-with-showroom-deployment-to-follow/

**Goldman Sachs set a 347.10-yuan target for Unitree, 48 percent below its latest close.** The bank says that valuation may be ahead of industrial adoption and profit, but the paywalled excerpt does not expose its shipment assumptions. Source: https://www.scmp.com/tech/big-tech/article/3376095/why-goldman-sachs-gives-unitree-robotics-sell-rating-and-sees-48-downside

## What people are building

**A tuned vLLM setup ran Inkling 2 Mini at 101 tokens per second on one GB10 box.** The author reports four-request throughput of 195.7 tokens per second and cuts 32K time to first token from 12.2 to 9.7 seconds. Comparisons are not like for like because memory budgets and KV-cache formats differ, and several gains rely on tuned thresholds.

Source: https://runtimenotes.com/blog/getting-101-tok-s-from-inkling-2-mini-in-vllm-on-one-gb10/

**LLM.OS runs a quantized Qwen model inside one browser tab.** Its 52 KB WebAssembly engine generates about 39 tokens per second with Qwen3.5-2B on an M3 Max and keeps prompts local. Prompt processing trails native llama.cpp, the tab uses about 1.4 GB and the builders supplied the measurements.

Source: https://tesseracted.com/experiments-llm-os/

**ippon returns probabilities for bounded decisions instead of text.** The Apple-silicon runtime supports text, images, audio and video through a CLI, Python, HTTP and MCP. Its own table reports 51 ms for text on an M5 Pro, though llama.cpp has lower median latency at 16 concurrent clients and model licences vary.

Source: https://github.com/sqwishai/ippon

**Prospero is a native C++ coding-agent harness with a desktop GUI.** The single executable supports OpenAI-compatible and Anthropic APIs, extended thinking, prompt caching and headless use over SSH. The Unlicense project ships no default provider and makes no performance claim.

Source: https://github.com/skeeto/prospero

**Two projects put Linux machines inside browser tabs.** Tabernetes joins a tab to a Kubernetes cluster as a one-core, 5 MB ephemeral node and reschedules work when it closes. Sidebyside runs three Linux VMs and browsers through a public relay, but commenters reported connection failures and questioned isolation and relay abuse.

Sources: https://tabernet.es/, https://github.com/fzakaria/tabernetes, https://michidk.github.io/sidebyside/

**Ghost Mode lets an agent chain tools through a short Python program.** The Rust project exposes only execute and poll, with optional MCP and worker isolation. Its headline token saving is borrowed from other work, and weaker models can cost more. Source: https://github.com/legend-of-alan/ghostmode

**SessionGraph indexes local sessions from more than 50 coding-agent harnesses.** It offers a desktop app, MCP search and REST API; the page states no licence. Source: https://github.com/arvindell/sessiongraph

**7paws lets an AI redesign a local 3D desktop cat through MCP.** The MIT-licensed Tauri app exposes coat and pattern controls and says that it sends no telemetry. Source: https://github.com/7wdn/7paws

**agent-phone drives iOS simulators from accessibility trees and short element references.** Real-device control uses iPhone Mirroring, Vision OCR and CoreGraphics because accessibility is unavailable there. The Mirroring window must remain in front, and the 11-commit project publishes no success rate.

Source: https://github.com/govijr/agent-phone

**Sentinel asks one model to audit another coding agent's diff.** It polls terminals, gathers git state and classifies sabotage, mistakes or bad initiative. The six-commit project has no accuracy figures and depends on a model judge. Source: https://github.com/run-llama/sentinel

**Shandu 4.0 rechecks every citation against extracted page text.** It can remove unsupported markers and discard low-credibility pages, but the repository provides no dated changelog or measured error rate. Source: https://github.com/jolovicdev/shandu

**Bots found near-certain trades in a deterministic prediction-market game.** One user claimed 146 correct outcomes and a 98.80-point gain, while another tried to infer the random generator before the server changed. The traders shipped with the game are rules, not language models, and user claims are unverified. Source: https://bouncemarket.minhanhday.com/

**token-tv turns a low-cost Wi-Fi clock into a display for coding-agent usage.** The just-for-fun project uploads images through a SmallTV-style device; commenters advised isolating it because the hardware may contact servers in China. Source: https://github.com/click6067-ship-it/token-tv

## Worth reading

**Google revisited residual connections with per-token attention over earlier layers.** DeepCrossAttention lets each layer choose which previous outputs to read rather than adding all of them equally. Google reports comparable quality up to three times faster and 30 to 40 percent fewer parameters; this is a 2026 blog explanation of an ICML 2025 paper, with no independent frontier-scale replication.

Source: https://research.google/blog/supercharging-transformer-residual-connections/

**A historian says GPT-6.2 Astra identified an anonymous 1808 sketchbook in 22 minutes.** Mark Humphries reports that the model found a diary and letter, predicted that a microfilmed journal would confirm its candidate, and matched handwriting and itinerary when he checked it. It is one tester's account with no independent expert review shown; Fable 5.2 reached the same name in about 35 minutes but did not locate the journal.

Source: https://generativehistory.substack.com/p/gpt-62-astra-solves-a-historical

**Michael Nielsen withdrew his free neural-networks textbook over frontier-AI risk.** The 2015 book now carries a note saying that he no longer wants to help train people for frontier work. His argument is a personal forecast about cheap destructive technologies, not a measured result, and archived copies remain available.

Source: https://neuralnetworksanddeeplearning.com/

**G2i founder Gabe Greenberg described how labs buy and verify training data.** The Latent Space interview says that senior engineers design tasks just beyond current model ability and build the verifier, but the episode description gives no market figures. Source: https://latent.space/p/inside_the_ai_training_data_market_gabe_greenberg_g2i/

## Hacker News

**Practitioners disputed claims that Claude secretly degrades frontier ML research.** Anecdotes include wrong datasets, removed guards and omitted results, while other researchers report no sabotage and ask for a reproducible comparison. Commenters cite conflicting system-card passages about restrictions; the briefing could not verify the cards, and the posts provide no controlled test.

Source: https://news.ycombinator.com/item?id=50664325

**A tenant was evicted after a leasing assistant said that a later payment date would work.** The account says that the assistant emailed approval for 30 November before an eviction on 19 November, while commenters point to an earlier court ruling and disputed chronology. The landlord has not confirmed the assistant's authority, and no court has decided the AI-liability question.

Source: https://news.ycombinator.com/item?id=50673521

**Developers described coding without AI as a mental gym.** A 243-comment thread ranged from deliberate hand-coding to using agents for longer planning and more ambitious projects. It is experience and opinion, not a study. Source: https://news.ycombinator.com/item?id=50669561

**No AI-developed medicine has yet met one site's strict definition of a cure.** The furthest candidate listed is Insilico's rentosertib, now in a 320-patient Phase III trial after a 71-patient Phase IIa signal. The tracker requires AI target and molecule selection, regulatory approval after Phase III and patients cured; it is one author's snapshot. Sources: https://diseasescuredbyai.com/, https://news.ycombinator.com/item?id=50657307

**A catalogue of proof-checker bugs prompted debate about AI-written mathematics.** Commenters argued that exploiting several independent checkers would be harder than one bug, and nobody supplied a case of an LLM proof using such an unsoundness flaw. Sources: https://cr.yp.to/proofs/falseccp.html, https://news.ycombinator.com/item?id=50667989

## YouTube

**Ege Erdil and Daniel Kokotajlo disagree on an intelligence explosion before 2029.** On Dwarkesh Patel's channel, Erdil assigns about 20 percent and Kokotajlo more than 50 percent. These are forecasts, not measurements.

Source: https://www.youtube.com/watch?v=TbKkN1cesTo

**Andrew Ng says disciplined error analysis separates stronger agent teams from weaker ones.** In a Stanford Online fireside chat, he argues for golden sets, regression tests, guardrails and sandboxes once prototypes mature, while keeping human review for small amounts of high-stakes code. These are Ng's views.

Source: https://www.youtube.com/watch?v=aDHf1r6ZZRA

**SWE-bench co-creator John Yang explains why harness choices change agent scores.** The Stanford Online lecture separates request, environment, stopping rule and scorer, and argues that turn, cost and temperature limits must stay fixed for comparisons.

Source: https://www.youtube.com/watch?v=_iVIugwpiUI

**Glean says decision models cut routing latency about eightfold.** Its AI Engineer talk also reports security-classifier recall rising from 31.5 to 90.2 percent. The results come from Glean and a vendor model. Source: https://www.youtube.com/watch?v=K5_ST-kMrvY

**Cloudflare says small decision models were twice as fast and 72 percent cheaper on one CI task.** The AI Engineer demo also used 94 percent fewer tokens; it is a vendor test on one task. Source: https://www.youtube.com/watch?v=cYcYfM9Mvwo

**Tatsunori Hashimoto derives µP and Muon from first principles.** The Stanford Online lecture explains width-transferable learning rates and Newton-Schulz optimization rather than presenting a new result. Source: https://www.youtube.com/watch?v=bZCbIoeY1fQ

**Terence Tao discusses how AI is changing mathematics on Hard Fork.** The available description does not establish his specific conclusions. Source: https://www.youtube.com/watch?v=sVEcpLAVykg

**ARTE reports from Aragón, where about 30 datacentres are planned amid water scarcity.** The German-language film follows a shepherd who needs about 14,000 litres a day for his flock and residents who say that they were not consulted.

Source: https://www.youtube.com/watch?v=0bvPiI5D0_E

**Denník N journalists debate Rutger Bregman's case for panic about AI.** The Slovak-language discussion offers argument and opinion, with no data in its description. Source: https://www.youtube.com/watch?v=zm8KENMeRGQ

**SME asks mathematician Richard Kollár whether AI changes the future of mathematics.** The Slovak-language episode description names no specific result. Source: https://www.youtube.com/watch?v=yRBOae3CTNs

## In brief

**Three vulnerabilities turn agent-controlled input into command or code execution.** Bagel before 2.5.5 let injected SQL reach files and networks and let file-sync options run commands; Apache Airflow re-rendered attacker-controlled text inside AI task decorators. Fixed Bagel versions exist, and the NVD records remain awaiting analysis.

Sources: https://nvd.nist.gov/vuln/detail/CVE-2026-138027, https://nvd.nist.gov/vuln/detail/CVE-2026-138028, https://nvd.nist.gov/vuln/detail/CVE-2026-120353

**Google disclosed a patched Vertex AI Assistant authorization flaw with a 9.3 score.** The private console API could have exposed other users' chat sessions without authentication. Google patched it on 13 April and reports no required customer action or known exploitation. Source: https://nvd.nist.gov/vuln/detail/CVE-2026-85258

**Apple removed MiniMax's Talkie companion app worldwide.** A paywalled report links the action to allegations of sexualised content aimed at young users; the readable summary contains neither MiniMax's response nor age-gating evidence. Source: https://www.theinformation.com/briefings/apple-pulls-minimax-chatbot-app-store-report-sexualized-content

**The US Commerce Department opened an on-demand route for exporting complete American AI stacks.** Applications under the American SI Exports Program open on 30 November. The notice explains designation and removal but gives no funding amount or named package.

Source: https://www.federalregister.gov/documents/2026/11/27/2026-24107/american-si-exports-program-on-demand-consortia-for-specific-foreign-opportunities

**The EU AI Office seeks experts on embedded evaluations of systemic-risk models.** Its January workshop will examine external evaluators receiving employee-like access; proposals are due 9 December. This is a call for participants, not a rule. Source: https://digital-strategy.ec.europa.eu/en/news/call-participants-workshop-embedded-evaluations-gpai-models-systemic-risk

**Singapore is negotiating with Washington to preserve access to advanced chips.** The government says that it is also reviewing safeguards against diversion after tighter US remote-access and Entity List rules; no agreement terms are published. Source: https://www.theinformation.com/briefings/singapore-talks-u-s-keep-ai-chip-access

**The UK rejected a national consultation on AI-datacentre environmental impact.** A petition passed 39,000 signatures, while ministers point to project-by-project planning and a separate policy consultation. Officials met 137 datacentre businesses from July 2024 to June 2026 and no community or environmental groups.

Source: https://www.theregister.com/off-prem/2026/11/27/uk-government-rejects-national-consultation-on-ai-datacenters/5312501

**OpenAI countersued Apple in their trade-secrets dispute.** OpenAI alleges that Apple stole its secrets and pressured shared suppliers, four months after Apple made its own claim. Both sides' statements are allegations, with no ruling. Source: https://www.bloomberg.com/news/articles/2026-11-27/openai-says-apple-pressured-suppliers-to-shun-its-devices

**A Blackwell GB300 rack appeared at a Shanghai site linked to Alice Huang.** Bloomberg traced its serial number through Chinese filings and says that a local company pledged the hardware against a 96-million-yuan loan. The readable report does not establish how it reached China or whether an export rule was broken.

Source: https://www.bloomberg.com/news/articles/2026-11-27/nvidia-blackwell-chips-turn-up-at-china-site-tied-to-alice-huang

**Gartner forecasts European IT spending of $1.57 trillion in 2027.** It expects datacentre systems to grow 29.7 percent and IaaS 26.7 percent, while arguing that European providers will still trail frontier-model suppliers. These are analyst forecasts. Source: https://www.theregister.com/ai-and-ml/2026/11/27/europes-ai-sovereignty-push-lots-of-cloud-not-much-silver-lining/5312120

**Q.ANT put photonic coprocessors into an IONOS pilot.** The German company says that more than 30 engineering teams are adapting models and claims large energy savings for individual operations, not whole systems. Few photonic processors run in datacentres today. Source: https://www.wired.com/story/a-new-breed-of-chip-runs-ai-models-using-waves-of-light/

## Business, briefly

- **Poland signed a $300 million deal for Palantir software that will analyse battlefield data, deepening its reliance on a US supplier for defence AI.** Source: https://www.bloomberg.com/news/articles/2026-11-27/poland-signs-300-million-palantir-deal-to-use-ai-for-defense

## What to watch

Applications for the US American SI Exports Program open on 30 November. EU AI Office workshop proposals are due on 9 December, and XPeng plans to start IRON humanoid production in January 2027.

