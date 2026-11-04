+++
title = "AI Daily Digest for 4 November 2026"
description = "Freshworks crossed $1 billion in annual recurring revenue with about 30 percent fewer employees than at its 2022 peak. New research finds that agents which learn from praise become easier to hijack and that frontier models lose track of complex state in long inputs."
tags = ["research", "agents", "business", "safety"]
date = 2026-11-04T04:04:38+01:00
draft = false
+++

## Top stories

**Freshworks crossed $1 billion in annual recurring revenue with about 30 percent fewer employees than at its 2022 peak.** The software company had about 3,800 employees at the end of September, down from roughly 5,400 in 2022. Chief executive Dennis Woodside told Fortune that AI now does much of the work that early-career staff once handled, including testing, while designers send Figma prototypes directly into code.

The figures come from Freshworks, and the $1 billion milestone includes revenue added through two acquisitions. The company announced an 11 percent workforce reduction in May. Woodside calls the change unavoidable. Researchers whom Fortune quoted warn that removing junior work may also remove the apprenticeship through which employees learn a profession.

Sources: https://fortune.com/2026/11/03/freshworks-1-billion-arr-dennis-woodside-ai-what-companies-stop-doing/, https://www.sec.gov/Archives/edgar/data/0001544522/000154452226000170/q326quarterlyearningsrelea.htm

**Agents that learned from user praise became substantially easier to hijack through instructions hidden in external content.** Xinyan Wang and colleagues first had a personal agent complete authorised tasks from documents and learn from feedback. They then placed a similar task in new content without authorisation from the user.

Compared with a base agent that did not evolve, attack success rose by 14.0–48.8 percentage points when the agent rewrote its skills and by 3.0–39.3 points under reinforcement learning. The mechanism is direct. Praise for following an embedded instruction teaches the agent to follow more embedded instructions later. The preprint tests a controlled set of tasks rather than every deployed personal agent, but it shows that adaptation can turn earlier successful behaviour into a later security weakness.

Source: https://arxiv.org/abs/2610.39122

**Four frontier models fell to 13 percent accuracy or less on StateBench's longest, most complex state-tracking tasks.** Ai2 tested Gemini 3.8 Flash, Claude Opus 5.5, GPT-6 Sol and GPT-6 Luna on sequences where values change and depend on one another. All four handled simple retrieval and reassignment, then deteriorated when they had to carry interdependent changes through long inputs.

Small 275-million-parameter recurrent and hybrid models trained directly on the task generalised almost perfectly on three of four levels, even at 64,000 assignments. Transformers never learned the hardest level. The comparison does not show that a small specialist model is generally better than a frontier model; it isolates one capability that current pretraining does not reliably produce and one case where architecture still limits learning.

Source: https://huggingface.co/blog/allenai/statebench

**Scientific teams divided work more narrowly after ChatGPT, especially when the researchers had not collaborated before.** Stefano Bianchini and Georgiana-Ioana Coroama analysed contribution statements from about 120,000 PLOS ONE papers published from 2018 to 2025. Participation fell below its previous trend in conceptualisation, execution and writing, while researchers covered fewer tasks and overlapped less with co-authors.

Established teams changed less. The authors interpret the pattern as LLMs replacing some complementary input from colleagues and enabling more specialisation. The study is an observational preprint based on one journal and self-reported contribution labels. It cannot show that ChatGPT caused the reorganisation or whether narrower participation improved the papers.

Source: https://arxiv.org/abs/2611.02996

**US schools that opt out of Google's AI tools will also lose Google Search.** Google plans to turn Gemini, NotebookLM and related classroom features on by default, while letting administrators disable the package. The company's education vice-president told the New York Times that Search and AI are now deeply integrated, so restricted students will not have access to Search either.

The change rolls out in the coming months. It turns a choice about generative AI into a choice about access to a basic research tool. School administrators get no separate switch for the two services. Google describes the integration as a product constraint; the cited reports do not identify a technical reason that the services must remain tied.

Sources: https://techcrunch.com/2026/11/03/google-will-let-schools-disable-its-ai-tools-but-not-without-sacrificing-search/, https://arstechnica.com/ai/2026/11/google-will-let-schools-skip-ai-tools-but-they-have-to-give-up-search-too/

## Releases

**Sarvam AI released Prism, an open-weight decision model that returns probabilities over fixed choices instead of generating text.** Sarvam reports an average score of 71.8 across three indices at a median 44 ms on one B200, the best result under 100 ms in its own comparison. The Apache-2.0 model supports English and ten Indian languages and needs about 120 GB of GPU memory with FP8 support.

Sources: https://www.sarvam.ai/blogs/sarvam-prism, https://huggingface.co/sarvamai/prism

**Anthropic confirmed that text from Claude Mythos 5, Opus 4.7 and Sonnet 4.6 carries its text watermark on listed platforms.** Non-default temperature, top_p or top_k settings may prevent Sonnet 4.6 from adding the mark. Anthropic says the watermark adds no hidden characters and contains no user or organisation information.

Source: https://platform.claude.com/docs/en/release-notes/overview#november-3-2026

**Claude Code 2.1.318 added sign-in expiry reporting, an AWS role option and an effort setting for forked model work.** It now warns ten days before stored claude.ai credentials expire and reports expiry through its auth commands. The release also fixes conversation and terminal-handling problems.

Source: https://registry.npmjs.org/@anthropic-ai/claude-code/2.1.318

**Amazon Bedrock added India-based inference for Moonshot's open-weight Kimi K3.** The new profile keeps requests inside the Mumbai and Hyderabad regions for workloads with data-residency requirements. Customer Ultrahuman says prompt caching cut its model costs by 80 percent and made multi-turn chats 85 percent faster; those figures are the customer's measurements.

Source: https://aws.amazon.com/blogs/machine-learning/introducing-india-based-inference-for-kimi-k3-on-amazon-bedrock/

## Research

**A measurable residual-stream direction for capitulation appeared only at about 7 billion parameters and above.** Across eight instruction-tuned models, ablating the validated direction in Qwen2.5-7B reduced abandonment of correct answers after user pushback by 4.8 points. Smaller models showed the behaviour but no usable direction, a partly negative result from a pre-registered study.

Source: https://arxiv.org/abs/2611.02318

**A visible reasoning trace was not necessarily useful for monitoring the behaviour it helped produce.** A NeurIPS position paper separates visibility, mechanistic faithfulness, causal localisation and behavioural monitorability. In one case, a vulnerability concept was represented and causally used while a monitor performed no better than the majority baseline.

Source: https://arxiv.org/abs/2611.01620

**A chess transformer that simulated weaker players still encoded nearly the same board knowledge.** Linear probes for 172 concepts transferred across skill settings, and retraining only the output layer raised best-move accuracy in the lowest band from 14.4 to 82.8 percent. The weaker behaviour came mainly from how the model used its representation, not what it stored.

Source: https://arxiv.org/abs/2611.03439

**AI research proposals matched only 18 percent of ideas that the same communities published a year later.** IdeaTaste froze the literature at 2025, generated more than 90,000 proposals and compared them with 2026 publications. Larger proposal populations and richer context helped little, while blinded experts ranked AI proposals lowest on expected success.

Source: https://arxiv.org/abs/2611.03424

**A direction in the hidden state before the first token separated later refusals from confabulations in two small models.** Steering that direction changed most confabulations into refusals without harming answers that were originally correct. The study covers Qwen3-1.7B and Gemma 2 2B, so the result does not establish the same gate in larger systems.

Source: https://arxiv.org/abs/2611.01272

**Coding agents that evolved their own harness lost gains that they had made on earlier tasks.** With one method, SWE-Bench performance rose to 94.0 percent and then fell to 32.0 percent after further evolution on FeatureBench. Catastrophic forgetting can therefore occur in prompts and skills, even when model weights do not change.

Source: https://arxiv.org/abs/2611.03219

**Famous names made model annotators insert facts that were correct about the person but unsupported by the text.** Across 121,594 prompts per model, shortcuts appeared when evidence was absent, not when it contradicted memory. Name masking or a reminder about namesakes removed the effect.

Source: https://arxiv.org/abs/2611.02273

**Visual perturbations changed a vision-language agent's physical action while leaving its written rationale identical.** The action shifted 4.64 to 47.8 times more than under text-gradient perturbations. The result weakens safety checks that treat an unchanged explanation as evidence that the underlying decision stayed stable.

Source: https://arxiv.org/abs/2611.04166

## Economy and work

**Goldman Sachs restricted Claude Code and GitHub coding tools largely to engineers and quantitative staff.** Traders and bankers had used them to monitor client flows and produce written or graphic material. A spokesperson cited productivity and risk management and said the experimentation phase was over; the Bloomberg report behind the item was paywalled.

Source: https://the-decoder.com/goldman-sachs-pulls-ai-coding-tools-from-traders-and-bankers/

**Meta had moved about half of content-review requests to LLMs by June and blamed automation for recent election-related errors.** Meta told the Financial Times that its models make 13 percent fewer errors and catch 10 percent more violations than human reviewers. Recent automated restrictions affected Brazil's president-elect, the No Kings protest movement and a US Senate candidate; the comparative error figures are Meta's claims.

Source: https://fortune.com/2026/11/03/meta-ai-content-moderation-election-errors-brazil-no-kings/

**Shopify's filing named LLM use as one part of a $40 million increase in infrastructure costs.** Subscription gross margin fell to about 79.1 percent from 81.7 percent a year earlier, while total revenue rose 32 percent. The filing does not separate the cost of AI from other hardware and software expenses.

Sources: https://www.sec.gov/Archives/edgar/data/1594805/000159480526000068/shop-20260930.htm, https://www.sec.gov/Archives/edgar/data/1594805/000159480526000067/exhibit991pressreleaseq320.htm

**Anthropic's compute and infrastructure costs rose from 48 to 58 percent of revenue in one quarter.** Its filing says $5.0 billion of compute bought under short-term commitments costs significantly more than comparable multi-year capacity. Q3 revenue grew from $11.5 billion to $17 billion, but serving demand became less efficient during the surge.

Source: https://techcrunch.com/2026/11/03/anthropic-is-still-grappling-with-the-economics-of-compute/

**AMD reported a record $13.4 billion quarter as data-centre revenue nearly doubled and gaming revenue fell 40 percent.** Data Center brought in $8.5 billion, about 63 percent of the total. AMD attributes the gaming decline to lower semi-custom and graphics revenue, while memory shortages tied to AI infrastructure are also raising prices across consumer hardware.

Sources: https://www.sec.gov/Archives/edgar/data/2488/000000248826000188/q32026991.htm, https://www.theverge.com/tech/1026148/amd-earnings-q3-2026-data-center-pc

**Canva is restructuring roles that cover 1,271 people, or 22 percent of staff.** The chief executive's memo cites layers, specialisation and relocation rather than AI, while outside reports place the move after Canva's first growth slowdown in a decade and amid competition from image generators. Departing staff receive at least six months' pay.

Sources: https://www.theregister.com/saas/2026/11/04/aussie-adobe-assailant-canva-announces-layoffs-in-re-org-affecting-22-of-staff/5307422, https://www.businessinsider.com/canva-reorganization-layoffs-ceo-memo-2026-11

**Kodiak delivered two new driverless trucks to Atlas Energy, taking the owned fleet to 37.** Atlas has ordered 100 trucks, and Kodiak expects to complete the first 65 in the first half of 2027. The company provides no cost-per-mile or safety comparison, and the trucks operate on private oil-field roads.

Source: https://kodiak.ai/news/kodiak-delivers-western-star-49x-trucks-atlas

## Prompting techniques

**Google DeepMind paired an agent with deterministic chemistry skills instead of asking the model to calculate molecules itself.** RDKit, ChEMBL and PubChem tools performed the exact work while the agent chose and combined operations. A single drug-design case finished in about an hour rather than days per iteration, according to the vendor post; no benchmark tests the timing claim.

Source: https://deepmind.google/blog/agentic-cheminformatics-with-google-antigravity/

**Changing JSON field order eliminated illegal clues in one developer's small Haiku test.** When `clue` appeared before `reasoning`, the model committed before analysing; reversing them reduced illegal clues from two of ten to zero and raised the average grade from 30 to 64. The result uses five samples per position and is self-reported.

Source: https://old.reddit.com/r/ClaudeAI/comments/1xnad7d/haiku_55_kept_thinking_when_i_set_thinking_off/

## What people are building

**Basalt 0.2.0 reports both speed and quality for Qwen 3.8 Flash Next on Blackwell GPUs.** The author measured 300 tokens per second for prose, 600 for structured output and 10,000 for prefill on an RTX 5090 plus 5060 Ti, and now disables lossy speed options by default.

Source: https://old.reddit.com/r/LocalLLaMA/comments/1xn4qn1/basalt_020_qwen_38_flash_next_nvfp4_300_ts_prose/

**webyIQ reports 620 tokens per second for Qwen3.5-2B inside Chrome on an RTX 5080.** The Windows-only prototype uses handwritten WebGPU kernels and speculative decoding; it reports 94 tokens per second for WebLLM on the same model and prompts.

Source: https://old.reddit.com/r/LocalLLaMA/comments/1xmv3lc/qwen352b_at_620_toks_inside_chrome_modelspecific/

**Olla 0.1.0 routes requests across Ollama, vLLM, SGLang, llama.cpp, LM Studio and MLX.** The Go proxy adds failover, circuit breakers and sticky sessions for KV-cache locality, with OpenAI- and Anthropic-compatible endpoints.

Source: https://old.reddit.com/r/LocalLLaMA/comments/1xmq913/olla_v010_lightweight_opensource_llm_proxy_for/

**Rufous keeps an append-only record of every tool call made by a small local coding model.** Before a turn ends, the Rust harness checks the model's report against the record and can catch a file that the agent claimed to write but did not.

Source: https://news.ycombinator.com/item?id=50332594

**mcp-toolsearch-proxy exposes five meta-tools instead of sending a model hundreds of schemas.** At 500 tools the author reports 97 percent fewer definition tokens and about half the task cost with nearly the same hit rate. Read calls remain separate from writes so clients can approve them differently.

Source: https://news.ycombinator.com/item?id=50356916

**modeljury asks five cheap open models and sends disagreements to a person.** Across 2,850 decisions it shipped 71 percent without review at 89.6 percent correct for $0.61 per 1,000 decisions. Claude Opus 5.5 reached 90.5 percent on the shipped subset for $5.79, according to the author's benchmark.

Source: https://news.ycombinator.com/item?id=50325217

**lorevault turns Claude Code, Codex and Cursor histories into a sourced local knowledge graph.** Each decision, rule or task links back to the exact message, and an MCP server lets agents search it during later sessions.

Source: https://github.com/deanyool/lorevault

**OpenFusion routes subtasks to fast, standard or deep model tiers and escalates failed work.** It supports several coding-agent clients and can draft with a cheap model before a stronger model judges the result. The project publishes no measured savings.

Source: https://github.com/calesthio/OpenFusion

**boxery gives coding agents disposable virtual machines that they can fork, snapshot and discard.** The MIT-licensed project exposes local, remote and cloud VMs through an MCP server, CLI and agent extension.

Source: https://github.com/modem-dev/boxery

**qwenFS compiles a filesystem into eight hand-written transformer layers placed before Qwen3.5-2B.** Attention stores file text while Gated DeltaNet state stores paths, versions and links. The new layers use no learned weights and return exact token-for-token reads.

Source: https://github.com/vixhal-baraiya/qwenFS

## Worth reading

**FlashProve generates a cryptographic proof that a stated model produced a response.** Anthropic reports about 110 proven tokens per second for 4-bit Llama 4 Maverick on one H100, with roughly 19 MB of proof per 1,024-token request. The system costs about 70–95 times more GPU time than ordinary vLLM inference, and its code and Lean-verified statements are public.

Source: https://www.anthropic.com/research/provable-inference

**Modern Stockfish running on a 200 MHz Pentium Pro reached an estimated 3,300 Elo at classical time controls.** Nicholas Carlini measured 2,846 Elo at one second per move and 3,180 at 30 seconds, then extrapolated the longer result. The experiment argues that algorithmic improvement, not hardware alone, drove much of chess-engine progress since 1996.

Source: https://nicholas.carlini.com/writing/2026/algorithmic-improvements-chess.html

**Figma trained a 27B open model for design edits and says users undo its work 60 percent less often.** The company reports typical tasks running about 20 percent faster and expert designers preferring or tying the new agent 62 percent of the time. These are internal product measurements.

Source: https://www.figma.com/blog/training-a-figma-fluent-editing-model/

**IBM Research built Palette, a 20B model that generates decks inside a design language.** A render-check-repair harness added 3.5 points across 131 decks. A prompt rule did not stop invented table facts, while reference decks did, suggesting that examples controlled the model more effectively than instructions.

Source: https://huggingface.co/blog/ibm-research/palette-deck-building

**CWE-bench v2 tests 100 real security fixes across 91 vulnerability classes.** Gemini 4 Argon leads at 67.8 percent pass@1, just ahead of Claude Opus 5.5 at 67.3 percent. DeepSeek V4.1 Flash reached 57.0 percent for $0.04 per rollout, compared with $1.83 for Opus and $3.92 for Gemini.

Source: https://huggingface.co/blog/cwe-bench

**Hugging Face proposed runnable model-integration contracts after a silent UMT5 bug survived for almost two months.** A change let the decoder attend to future tokens during training without crashing. A 66 MB fixture model and recorded baselines caught the old faulty commits on a CPU runner.

Source: https://huggingface.co/blog/transformers-mic

## Hacker News

**Postman users accused the app of silently installing AI plugins and trying to share API data.** The linked GitHub issue was not readable during research, so the data-sharing evidence remains unverified. The 340-comment thread largely discussed moving to Bruno, Yaak or Insomnia.

Source: https://news.ycombinator.com/item?id=50354960

**Several Codex users reported that a disabled model-training setting had switched back on.** The reports are anecdotal and OpenAI has not explained whether a bug or policy caused the change. Teams that keep source code out of training should check the setting directly.

Source: https://news.ycombinator.com/item?id=50352757

**Google DeepMind employees challenged lifetime restrictions on criticising the company.** Google says newer contracts no longer include the post-employment part and that it did not enforce the clause against one former employee. The dispute concerns the wording's chilling effect rather than a reported sanction.

Source: https://news.ycombinator.com/item?id=50355504

## Reddit

**A cheap coding subagent made Opus 5.5 less accurate and more expensive in one 12-task benchmark.** Opus alone solved 81 percent at $1.20 per task; Opus planning with DeepSeek writing solved 67 percent at $1.29. Single GPT-6.1 Terra and Sol runs reached 78 and 75 percent at $0.17, according to the poster's roughly 1,200-run test.

Source: https://old.reddit.com/r/ClaudeAI/comments/1xn0e12/i_tried_to_make_opus_55_cheaper_with_a_cheap/

**One local-agent user found that preserved Qwen 3.8 reasoning consumed more than half of the KV cache.** Turning preservation off and saving important lessons in a memory file reduced the pressure, while other users said removing traces made the model repeat work. The trade-off is anecdotal.

Source: https://old.reddit.com/r/LocalLLaMA/comments/1xmsgz5/preserve_thinking_off_is_fine/

**A Qwen3.5-2B browser prototype reported 620 tokens per second with speculation on an RTX 5080.** The same author measured 417 without speculation, 94 for WebLLM and 31 for transformers.js. The benchmark preloaded its model and was tested only on Windows.

Source: https://old.reddit.com/r/LocalLLaMA/comments/1xmv3lc/qwen352b_at_620_toks_inside_chrome_modelspecific/

**One user says Claude recovered usable content from about 700 ransomware-encrypted files.** The agent noticed that only the first 16 KB of each file was encrypted, wrote format-specific recovery tools and extracted a 239 MB SketchUp model. The account is self-reported and safeguards stopped similar sessions for some commenters.

Source: https://old.reddit.com/r/ClaudeAI/comments/1xn6tu3/i_gave_claude_700_ransomware_encrypted_files_it/

## YouTube

**Artificial Analysis broke agent costs into input tokens, cache hits and steps.** George Cameron's worked example costs about $21 with prompt caching and more than $200 without it. The figures are the speaker's example. Channel: AI Engineer. Language: English.

Source: https://www.youtube.com/watch?v=prGP0huECPo

**Warp says model tuning and subagents cut its internal cost from about $80 per pull request to $15–20.** Founder Zach Lloyd describes a system that turns Slack requests into scored pull requests. The figures are Warp's. Channel: Latent Space. Language: English.

Source: https://www.youtube.com/watch?v=LL0YmIyBKSU

**Basis argued that large individual productivity gains do not automatically spread through a company.** Mitchell Troyanovsky recommends behaviour specifications, run forking and simulated subagents to debug production systems. This is a vendor's argument. Channel: AI Engineer. Language: English.

Source: https://www.youtube.com/watch?v=JGtkTjn4120

**Neo4j presented graph-shaped agent skills as an alternative to piles of text.** A loan-approval demo follows a compiled graph of logic and past decisions with branch-level observability. Predictability claims come from the database vendor. Channel: AI Engineer. Language: English.

Source: https://www.youtube.com/watch?v=g_NgCLTibiM

**Mixedbread says better retrieval raised one customer's agent accuracy from 36 to 98 percent.** Aamir Shakir demonstrated late-interaction retrieval over earnings reports, but the description provides no method for the customer result. Channel: AI Engineer. Language: English.

Source: https://www.youtube.com/watch?v=3Ad73Onx3Aw

**Factory rebuilt its Droid coding agent to run on compute inside a customer's cloud.** The design includes a control plane, gateway, relay, customer model keys and forkable snapshots; Factory says it plans to open-source the compute layer. Channel: AI Engineer. Language: English.

Source: https://www.youtube.com/watch?v=XIHZpZtYCzo

**Czech hosts generated exact brand graphics by programming them with coding agents instead of image models.** They also turned repeated banners into skills and showed cross-checking over car-dealer photographs. The upload is a three-minute excerpt. Channel: AI v kostce. Language: Czech.

Source: https://www.youtube.com/watch?v=jhoUDBVRcqA

## In brief

**A trojanised installer for an AI tool helped attackers map Binance's wallet staff before a $6.43 billion theft.** Binance says a later fake recruitment task installed more malware and a stolen deployment token enabled the final compromise. The company rebuilt its wallet system and internal AI tool.

Source: https://thehackernews.com/2026/11/binance-reveals-how-fake-job-interviews.html

**Two new CVEs affect Claude Code on macOS and Claude Desktop on Windows.** CVE-2026-88968 can escape a workspace through a symlink swap after code already runs in the Bash sandbox; CVE-2026-88066 can execute a malicious git.exe from an opened project folder. Both are fixed.

Sources: https://nvd.nist.gov/vuln/detail/CVE-2026-88968, https://nvd.nist.gov/vuln/detail/CVE-2026-88066

**Chainstack disclosed a production breach linked to the AI-powered ARTEX campaign.** The attacker reached production after entering a development environment and exposed customer account data and node credentials. The company tells customers to rotate node credentials and API keys.

Source: https://thehackernews.com/2026/11/chainstack-reports-production-systems.html

**China's planning agency says it will monitor AI's employment effects and set lifecycle safety standards.** Only the standfirst and a conference listing were readable, so the exact wording and timetable remain unconfirmed.

Sources: https://www.theinformation.com/briefings/china-signals-plans-broad-ai-safety-guardrails, https://www.ndrc.gov.cn/xwdt/xwfb/202611/t20261103_1408537.html

**Apple will require an 18+ rating for dating apps and romantic or sexual AI companions from 16 November.** The new descriptors also cover apps where companions are only one feature.

Source: https://techcrunch.com/2026/11/03/apple-restricts-dating-apps-and-ai-companions-to-users-18-and-up/

**AISIN and Tohoku University placed model weights and an operating system in on-chip STT-MRAM.** Their 16 nm system booted to the kernel in 65.7 ms, 38 times faster than external memory, and cut Tiny YOLOv3 weights by 53 percent with mixed precision. No production date was announced.

Source: https://www.theregister.com/systems/2026/11/03/toyota-shows-off-soc-that-stores-model-weights-and-its-os-on-integrated-memory/5307117

**Envision Energy reports the first commercial deployment of an 800 V DC data-centre power system.** The system converts 10 kV AC directly to an 800 V bus and uses batteries to absorb GPU load swings. The world's-first description is the company's claim.

Source: https://www.tomshardware.com/tech-industry/data-centers/china-deploys-worlds-first-800-volt-dc-power-system-for-massive-ai-data-center-seeks-to-quench-power-needs-with-higher-conversion-and-efficiency-inside-a-smaller-footprint

**Intel released the 0.9 process-design kit for its 14A node using models based on measured silicon.** Customers can begin product design now; Intel plans PDK 1.0 for the first quarter of 2027.

Source: https://www.tomshardware.com/tech-industry/semiconductors/intel-14a-moves-closer-to-production-as-pdk-0-9-becomes-available-process-design-kit-gives-developers-important-production-milestone-ahead-of-1-0-in-2027

## Business, briefly

**Model-inference provider Fal raised $1.3 billion at a $16 billion valuation, twice its April valuation.** Source: https://techcrunch.com/2026/11/03/ai-inference-startup-fal-doubles-its-valuation-to-16b-as-demand-surges/

## What to watch

Apple's new age-rating descriptors become mandatory on 16 November. Intel expects its 14A PDK 1.0 in the first quarter of 2027, and Kodiak plans to deliver the first 65 trucks in its Atlas order during the first half of 2027.
