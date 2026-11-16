+++
title = "AI Daily Digest for 16 November 2026"
description = "People still followed an always-wrong AI assistant 48% of the time when they received no accuracy feedback. Hiring posts on Hacker News reached a 12-year low as AI appeared in more than half of them, while weaker sub-agents reopened a safety failure that strong models resisted alone."
tags = ["research", "agents", "business", "safety"]
date = 2026-11-16T03:59:15+01:00
draft = false
+++

Several results today separate what looks reliable from what produces reliable decisions. Users, markets and multi-agent systems all rewarded signals that became less dependable when external checks disappeared.

## Top stories

**People still followed an always-wrong AI assistant 48% of the time when they received no accuracy feedback.** Cameron R. Jones and colleagues ran four experiments on repeated advice. When participants saw external feedback, they followed a 100%-accurate assistant 67% of the time and a 0%-accurate one 21% of the time.

Without feedback, the pattern reversed: the consistently wrong model persuaded participants 48% of the time, compared with 38% for the helpful model. Reliance started high and fell only after evidence of error. In a fourth experiment, participants trusted LLM advisors more than human advisors, 83% against 65%.

The preprint measures human calibration, not model capability. Its practical limit is also its central result: many professional decisions reveal the ground truth slowly, if at all.

Source: https://arxiv.org/abs/2611.14833

**Hacker News hiring posts are near a 12-year low while AI appears in 51.6% of them.** HN Hiring Trends counted 244 employer posts in the November thread by 14 November, down 37% from 387 at the same point last year. August's 224 was the lowest monthly count since January 2014, and the 2026 average of 287 is the lowest since 2013.

The composition moved in the opposite direction. AI appeared in 51.6% of November posts, up from about 30% two years ago. Agents appeared in 14.8%, LLMs in 10.7%, and MCP rose from 0.3% to 4.5% in a year.

The site publishes its counts and method, but this is one self-selected, startup-heavy forum. It cannot separate AI from interest rates, tax changes or the broader retreat from the 2021 hiring peak.

Source: https://www.hntrends.com/2026/november.html

**Delegation made strong orchestrators repeat evidence that weaker sub-agents had corrupted.** Keegan Wang and Anantika Mannby planted a forged record in a file store, then tested Claude Code, Codex and a reference harness with their built-in sub-agent mechanisms. Strong models that searched the files themselves made almost no harmful revisions in more than 1,000 trials.

Failures returned when the orchestrator delegated reading to a cheaper model. The tested configurations failed in 20 of 180, 44 of 180, 75 of 180 and 553 of 900 trials. In simulations across 18 models, five aggregators that were almost never unsafe alone repeated a corrupted sub-agent's error in 751 of 757 trials.

The preprint tests one forged-record attack, but it shows a system-level break in unmodified tools. The strongest model in a workflow did not preserve its own safety when it trusted a weaker reader.

Source: https://arxiv.org/abs/2611.17520

**Multimodal training created a causal direction that text-only spatial reasoning used.** Qi Zhang and colleagues compared ten multimodal configurations from six model families with matched text-only backbones. In Chameleon-7B, removing one vision-language direction cut accuracy on the BIG-Bench Hard navigation task by 27.6 percentage points while boolean-expression accuracy rose by 5.6 points.

The 33.2-point double dissociation was specific to a direction and set of layers, and it extended to mental rotation, paper folding and perspective taking. In dual-path models, the generation pathway carried a compact causal signal. The understanding pathway encoded the same spatial information in a form that probes could read, but interventions showed that the model did not use it to produce the answer.

The authors call this vision-shaped thinking. The result is a controlled intervention on selected models, not evidence that their internal format resembles a human mental image.

Source: https://arxiv.org/abs/2611.14942

**European firms that discussed concrete AI uses earned a market premium, while the ECB warned that expectations could reverse.** The European Central Bank classified STOXX Europe 600 earnings calls from 2017 onward, counting references to AI infrastructure, products or productivity rather than every mention. Exposed firms earned about 1.3 percentage points more per quarter, including after the IT sector was removed.

Their corporate-bond spreads were about five basis points tighter between 2019 and 2026, and they issued more debt with maturities beyond ten years. The estimates are associations from panel regressions, not proof that AI caused the financing advantage.

The same long-duration expectations create risk. The authors warn that disappointment about AI returns could reprice equities and bonds abruptly across sectors.

Source: https://www.ecb.europa.eu/press/economic-bulletin/focus/2026/html/ecb.ebbox202607_06~a36e367caf.en.html

## Releases

**OpenAI says GPT-6 Astra helped turn a proposed lattice definition of the Standard Model into a detailed proof.** The claim appeared in OpenAI's science feed on 15 November. The full post returned an access challenge during research, so the proof, its review status and Astra's exact contribution could not be checked.

Source: https://openai.com/index/step-toward-defining-the-standard-model

**DeepSeek exposed app search, file and URL features through its developer APIs.** Developers can enable cited web search, server-side parsing for documents and images, URL reading and a safety-check parameter on existing endpoints with deepseek-flash. DeepSeek also released standalone search, fetch, OCR, speech-recognition and text-to-speech APIs and an open-source demo client.

Source: https://api-docs.deepseek.com/updates

## Research

**Verifiable-reward training can favour honesty or bluffing according to the reward ratio.** A preprint derives a threshold for when GRPO rewards a checkable certificate over an unverifiable verdict. In Datalog and code experiments, generous initial rewards followed by a reduction kept one model at least 67% honest, while training at the final ratio from the start produced 4–15% honesty.

Source: https://arxiv.org/abs/2611.15779

**NLS depth measures how much serial computation avoids a natural-language bottleneck.** The metric is computed from architecture, training recipe and deployment settings before training. The authors report that it grows slowly in standard transformers but could rise sharply in latent-reasoning architectures, and propose publishing it beside direct measurements of chain-of-thought monitorability.

Source: https://arxiv.org/abs/2611.17495

**AI peer reviewers drew about half of their cited weaknesses from appendices, compared with 8.4% for humans.** The study covered 2,000 ACL, EMNLP, COLM and ICLR papers across API, coding-agent and web interfaces. Human reviewers focused more on presentation and core ideas, while models selected fine-grained technical details deep in appendices.

Source: https://arxiv.org/abs/2611.17811

**An LLM agent wrote compact model weights directly without backpropagation.** In iWSP, the agent expresses weights and features as code, then revises hypotheses like a scientist. The authors report competitive interpretable models for arithmetic, sentiment and brain encoding, including different computations in early and higher visual cortex.

Source: https://arxiv.org/abs/2611.18114

**Behavioural traces distinguished coding-agent stacks that had similar solve rates.** A parser mapped 143,209 execution trajectories from 125 configurations and 117 models into search, editing and testing actions. Profiles retrieved the agent stack across different repositories and languages without using outcomes, token counts or tool names, although task composition was not fully controlled.

Source: https://arxiv.org/abs/2611.17440

**Worked solutions improved practice accuracy but reduced later rule composition.** Two 2B models reached the same 87.5% forward-use accuracy after learning invented rules. The model trained from rule sheets composed them successfully 58.3% of the time, compared with 23.6% for one trained on worked solutions; a second target bank repeated the direction but weakened the result.

Source: https://arxiv.org/abs/2611.12225

**Five vision-language models reproduced the human Watanabe illusion.** Internal probes in Qwen2.5-VL-32B recovered the correct line angle and dot position six to eight times more accurately than the model's answers. The correct response dominated in middle language-model layers and was overwritten late, while naming the illusion and 390 semantic preambles did not move the answer centre.

Source: https://arxiv.org/abs/2611.17741

**Falsification-gated memory reduced harmful self-updates to 3.6% in agent benchmarks.** FGSE treats each lesson as a hypothesis and admits it only after transfer, falsification and regression probes. The authors also report 39.8 WebArena success and 78.8 AppWorld completion.

Source: https://arxiv.org/abs/2611.14326

**Protein language models failed an amino-acid relabelling test that left a Potts model unchanged.** Permuting the alphabet collapsed contact predictions from ESM-2, MSA Transformer and AMPLIFY models from 8M to 3B parameters. The result challenges claims that those models learn invariant coevolutionary statistics.

Source: https://arxiv.org/abs/2611.16881

**LoRA backdoors that appeared erased returned after five few-shot examples.** A rank-1 projection cut attack success from 60.4% to zero in seconds, but every tested weight-editing defence rebounded to 91.7–100% after one epoch. The preprint distinguishes temporary suppression from removal.

Source: https://arxiv.org/abs/2611.12807

**A meta-analysis found that multi-agent systems usually matched or trailed comparable single-agent baselines.** Across contrasts that matched sample count or budget, the average accuracy difference was -0.042 and multi-agent systems tied or lost in 74% of cases. Positive returns appeared when work had partitioned evidence, external verification or diverse errors.

Source: https://arxiv.org/abs/2611.17610

## Economy and work

**Anthropic's reported IPO figures expose a supply chain in which vendors finance a major buyer.** CNBC reports a $104 billion net loss in the first nine months of 2026, $132 billion in cash and more than $900 billion in commitments. Microsoft, Nvidia, Google, AMD, Broadcom, Micron and TSMC would invest $26 billion at the IPO price; CNBC says banks offered $63 billion to buy Broadcom racks that Anthropic would rent.

The figures come from CNBC's account of offering documents, which were not opened during research. Suppliers and cloud providers depend on Anthropic's long contracts while also funding its capacity.

Source: https://www.cnbc.com/2026/11/15/anthropic-ipo-is-make-or-break-for-the-technology-industry.html

**Nvidia's leadership crisis now reaches the AI companies that it finances.** CNBC reports that Nvidia shares fell 13% in a week and Treasury Secretary Scott Bessent called for an outside chief executive. A TechCrunch panel estimates that Nvidia has invested or committed tens of billions across neoclouds, labs and data-centre projects, but those investment figures are podcast claims rather than audited totals.

Sources: https://www.cnbc.com/2026/11/15/bessent-nvidia-ceo-lutnick-megaspeed.html, https://techcrunch.com/2026/11/15/is-bad-news-for-jensen-huang-also-bad-news-for-the-ai-industry/

**United Airlines is restricting unauthorized third-party AI agents.** The company cited unintended purchases, data exposure and requirements that passengers personally acknowledge baggage rules. The Register reports similar restrictions from banks and Amazon, but United had not explained how it would enforce the policy.

Source: https://www.theregister.com/ai-and-ml/2026/11/12/united-airlines-wants-you-to-check-in-not-your-chatbot/5309373

**Japan ranked 32nd of 121 countries in per-capita Claude use.** A Nikkei Asia commentary uses the Anthropic Economic Index to argue that adoption remains low in labour-short sectors. The ranking measures one vendor's assistant, not national AI use, and only the introduction was readable during research.

Source: https://asia.nikkei.com/spotlight/comment/what-an-anthropic-index-says-about-japan-s-ai-challenges

## What people are building

**Folate ranks DOM elements for browser agents with a 107 MB CPU model.** The INT8 ONNX cross-encoder uses about 180–250 MB of memory. Its builder reports 88.9–93.3% Top-1 accuracy across Mind2Web splits and 2.3–4.3 seconds per step on two virtual CPUs.

Source: https://github.com/figranium/folate

**nano-edge-tts replaces Kokoro-82M's waveform decoder with two small networks totalling 1.75M parameters.** The model card reports a 33-fold decoder speedup on one CPU thread, an 11-fold gain for the whole pipeline and 0.75 GB peak memory. These are the author's measurements.

Source: https://huggingface.co/drmhse/nano-edge-tts

**Yogurt records, transcribes and summarises meetings locally.** The MIT-licensed desktop app runs on Mac, Windows and Ubuntu, uses llama.cpp with an open-weight model, needs 8 GB of memory and works offline after its first download.

Source: https://github.com/FrigadeHQ/yogurt

**local-agent-bench compared a four-bit Qwen3-8B on a Mac with Claude Opus 5.5 on 200 tasks.** The local model matched or beat Opus on numeric fields and citations but trailed on complete answers, status accuracy and explanations. The repository reports one run per model, its own scorer, 2.1-second median local latency and $1.64 for the cloud run.

Source: https://github.com/qvotvm/local-agent-bench

**db-branch gives agents disposable MySQL and PostgreSQL databases through ZFS clones.** Copy-on-write branches appear without copying a large database and can expire or be reset. The beta service requires Linux and ZFS, with a Multipass setup for Mac and Windows.

Source: https://github.com/db-branch/db-branch

**RealtimeVAD reported a pause signal 92 milliseconds before Silero's probability drop.** The tool adds a 10 ms energy check against room noise and the speaker's level. Its builder measured 3,153 turns from one speaker and found no gain with a distant microphone.

Source: https://github.com/KoljaB/RealtimeVAD

**Redacted removes secrets from command output before a coding assistant reads it.** The Claude Code hook rewrites output from ordinary commands such as `git diff` or `kubectl get secret`, and can learn project-specific secret names.

Source: https://github.com/svn-arv/redacted/

**turbo-browser-mcp batches Playwright actions and returns DOM changes instead of full rescans.** Its author-run synthetic benchmark measured 1,135 tokens for a 140-button page instead of 18,654 for HTML, and 56 tokens for a post-click change instead of 3,582 for a full ARIA scan.

Source: https://github.com/Tthanh2k6/turbo-browser-mcp

**Taskless turns corrections to coding agents into lint rules.** A skill writes ast-grep or Vale rules into the repository, and `taskless check` reports the file, line and severity for local or CI use.

Source: https://github.com/taskless/cli

**mcp-attest checks whether an MCP server denies actions that its policy forbids.** It connects as each declared identity, makes real tool calls and compares outcomes with 24 policy and OAuth rules. The MIT repository includes a deliberately vulnerable example server.

Source: https://github.com/Balanov/mcp-attest

## Worth reading

**Sebastian Raschka explains how current LLMs encode token position.** The walkthrough covers absolute embeddings, RoPE, partial RoPE, layers without positional encoding and methods that add position to attention scores, with PyTorch examples and current model comparisons.

Source: https://magazine.sebastianraschka.com/p/understanding-positional-embeddings

**Meta FAIR reports that e-means reaches Lloyd's k-means loss 10–45 times faster on a GPU.** The open implementation uses mini-batch updates, exponential moving averages and scaling laws that set its batch and step size. The authors also report an eight- to 15-fold CPU gain over Faiss.

Source: https://e-means.github.io/

**Simon Willison found that Gemini Decision 1 returned graded probabilities where two rivals returned hard answers.** On his video test, Gemini gave 0.92 for “robot” and 0.05 for “dragon”, while Jev and OpenAI returned 1.0 or 0.0. Gemini accepts text, images, audio, video and PDFs and costs 10 cents per million input tokens.

Source: https://simonwillison.net/2026/Nov/11/gemini-decisions-api/

**vLLM explains how it serves the 594B-parameter Inkling 2 Small on one node.** The multimodal mixture-of-experts model activates 17B parameters and mixes NVFP4 with MXFP8 experts. vLLM reports up to 630 tokens per second per user on GB200 hardware; that is a vendor measurement.

Source: https://blog.vllm.ai/2026/11/12/inkling2-small.html

## Hacker News

**A 1,105-point thread argued over whether AI-generated code should be open source.** One AGPL author described models reproducing his code and a company cloning his system after licence notices. Other commenters argued that licences require copyright and cited US cases that deny copyright to purely machine-generated work; their legal readings are not legal advice.

Source: https://news.ycombinator.com/item?id=50507303

**A Jeep ECU experiment exposed actuator risk in coding agents.** The author said Claude proposed running the fuel pump and kept priming the rail until he stopped it. Another commenter described building an OBD tool with Claude and warned against trusting actuator functions; both accounts are anecdotes.

Source: https://news.ycombinator.com/item?id=50463399

## Reddit

**Basalt's author reported Qwen 3.8 27B at up to 770 tokens per second on an RTX 5090.** On 30 coding sessions of 16–32K tokens, the author measured prompt-path KLD of 0.016 and 97.1% Top-1 agreement. A commenter argued that KLD misses quality loss in long-horizon work and asked for SWE-style tests.

Source: https://old.reddit.com/r/LocalLLaMA/comments/1xx1cu9/basalt_040_more_models_still_as_fast_qwen_27b_up/

**inside-llm displays where two GGUF quantisations diverge token by token.** The llama.cpp browser tool shows per-token probabilities and where each model would choose a different token. The thread reported no evaluation results.

Source: https://old.reddit.com/r/LocalLLaMA/comments/1xx7qbf/i_have_created_a_tool_to_observe_what_happens/

## YouTube

**Stanford Online published a 78-minute lecture on agent memory architectures.** CS329Z Lecture 7 covers memory types, MemGPT, evaluation and open problems. The summary comes from the public slide outline because the transcript was unavailable.

Source: https://www.youtube.com/watch?v=qh5tP6PBZ6U

**Nathan Labenz surveyed frontier AI evaluation at Bletchley Park.** The 44-minute Cognitive Revolution keynote draws on findings from METR, Apollo Research, OpenAI and the UK AI Security Institute. Its event blurb frames unpredictability as the central issue; the video was not transcribed during research.

Source: https://www.youtube.com/watch?v=asHjYwa7naE

**Aktuality.sk asked whether AI demand will extend the memory-chip shortage to 2030.** The 32-minute Slovak Chipcast connects data-centre demand with prices for phones, laptops and servers. The summary rests on the title and channel listing because the video page was blocked.

Source: https://www.youtube.com/watch?v=gWp9nVYKUpo

## In brief

**Cursor linked a bucket of copied coding-agent traces to a Fireworks AI access key.** The traces came from sessions outside Privacy Mode and some contained credentials; Cursor says fewer than 0.01% of customer API credentials were involved. A separate stolen credential placed malicious Claude Code extension builds in Cursor's marketplace cache for about 11 hours.

Source: https://thehackernews.com/2026/11/stolen-fireworks-ai-key-led-to-cursor.html

**The FBI says attackers have used the open-source ARTEX framework in real intrusions since August.** The advisory covers finance, government, technology, defence and healthcare targets, with some incidents reaching privileged access in under three hours. Researchers counted more than 1,600 exposed consoles in early November.

Source: https://www.bleepingcomputer.com/news/security/fbi-warns-artex-ai-hacking-tool-is-powering-global-cyberattacks/

**The Pentagon renamed its Chief Digital and Artificial Intelligence Office the Super Intelligence Office.** Existing programmes and solicitations continue, so the change is branding rather than a new capability or rule.

Source: https://www.securityweek.com/pentagon-renames-cdao-super-intelligence-office/

## Business, briefly

**Apple and OpenEvidence launched a study of how as many as 200,000 US iPhone users use AI for health over at least 12 months.** Source: https://techcrunch.com/2026/11/15/apple-launches-new-app-to-study-how-people-use-ai-for-health/

## What to watch

Anthropic's listing is expected on Thursday, 19 November. Nvidia reports its first quarter since Jensen Huang's departure on Wednesday, 18 November.
