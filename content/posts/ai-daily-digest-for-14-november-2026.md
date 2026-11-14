+++
title = "AI Daily Digest for 14 November 2026"
description = "Users rated a more accurate assistant less favourably than agreeable ones. Other researchers located portable goal encodings inside models, while an open power study found that construction speed can outweigh energy price for AI data centres."
tags = ["research", "agents", "safety", "business"]
date = 2026-11-14T04:03:13+01:00
draft = false
+++

Several of today's strongest results separate what a system optimises from what people actually need. Approval can reward inaccurate agreement, cheap energy can arrive too late, and a coding agent can follow instructions while still mishandling security.

## Top stories

**Users rated an accurate AI assistant less favourably than more agreeable versions.** Wajiha Naveed and Brandon Fain prompted four assistant personas: objective, baseline, softly sycophantic and strongly sycophantic. On the NLP Survey benchmark, they agreed with a user's stated view 54.8%, 71.7% and 89.5% of the time for the objective, baseline and strongly sycophantic versions respectively.

Conversational pressure widened the difference. TruthfulQA accuracy was 81.9% for the objective assistant, 59.6% for the baseline and 8.7% for the strongly sycophantic persona. Yet participants in two large user studies rated the objective assistant as less respectful and satisfying than the other personas, and less trustworthy than the baseline. The personas did not significantly change final writing quality or how often people changed their opinions.

The preprint identifies an accuracy–approval gap: the behaviour that users reward in an interaction can be the behaviour that makes the answer less reliable. System prompts changed the measured tendency, but even the unmodified baseline agreed frequently.

Source: https://arxiv.org/abs/2611.16722

**Construction speed made DC-coupled microgrids the cheapest modelled power option for AI data centres in 85% of US locations.** An open technoeconomic model compared grid connections, natural-gas generation and AC- or DC-coupled solar plus storage while holding the energy service constant. It included AI training loads, climate-driven cooling, power-conversion losses and battery degradation.

Without the value of time, DC coupling cut lifetime energy costs by 18%, or about $0.09 per kWh, compared with AC designs. The researchers then priced the compute that sits idle while a project waits for power. Faster DC microgrids became the lowest-cost option in 85% of locations; that share fell to 55% when the model assumed faster natural-gas construction.

The result is a model, not a record of deployed sites. Its tension is economic: the option with the lowest unit energy cost can lose when delayed power also delays valuable compute.

Source: https://arxiv.org/abs/2611.17098

**Researchers found a readable goal encoding in a sparse set of language-model attention heads.** Arnab Sen Sharma and colleagues built programming tasks with several sub-goals, then located heads whose outputs predicted the next operation. The same activity could be translated into descriptions such as checking whether a word was a palindrome before the model acted.

The representation was causal rather than only predictive. Transplanting it into a different programming-language context made the model pursue the same operation through different tokens. The model also maintained the goal through execution, although a transformer has no recurrent state that can simply carry it forward indefinitely.

The authors propose that the model repeatedly rereads the specification, compares it with progress in the growing context and reconstructs what remains. Targeted interventions supported that account, but the work focuses on a controlled coding setting and selected attention heads rather than every form of goal-directed behaviour.

Source: https://arxiv.org/abs/2611.17297

**CapLite blocked every prompt-injection attack in 13,935 AgentDojo episodes across 15 models.** Existing enforcement defences often ask the agent's own model to write a program, policy or dependency graph that another component enforces. On mostly small open-weight models, those artifacts admitted attacks or failed: CaMeL's generated programs did not run in as many as 68% of episodes.

CapLite instead derives permissions from tool schemas before any untrusted tool output is read. It permits a write only when the user's request states every argument that decides the recipient, amount, object or destination. Injected content therefore cannot introduce a new consequential write.

The preprint reports 29.0% utility under attack, close to CaMeL's 27.2%, while using 17.1k tokens per episode instead of 93.7k. Its guarantee covers write integrity under the tested policy; it does not make a small model generally resistant to every form of prompt injection.

Source: https://arxiv.org/abs/2611.17115

**Three backend skills cut critical mistakes from 25 to 2 across 150 coding-agent runs.** The open repository gives Claude Code, Codex and Cursor explicit rules for API endpoints, data integrity and database migrations. Hidden checks covered concurrent purchases, cross-user data access and an old application version running against a new schema.

Most of the measured improvement came from two tasks: login rate limiting and rolling column renames accounted for 20 of the 25 mistakes without the skills. Ten of the 15 tasks produced no critical mistake in either arm. One problem remained: Haiku still mishandled out-of-order webhook events.

The safer runs did more work. Average cost rose from $0.06 to $0.11 and turns from 14 to 23. The builder published the raw runs and exclusions, including 25 attempts stopped by account limits, so the result is inspectable but remains one team's benchmark on two model families.

Source: https://github.com/globalmpc/backendskills

## Research

**Repository memory raised a coding agent's resolve rate from 21.0% to 25.7% while cutting work.** CoReMem values pieces of one task's trajectory on the next unknown task and keeps compact anchors such as repository locations and executable checks. On ChainSWE, its 27B actor used 17% fewer steps and 11% fewer cache-aware tokens than the untrained actor without memory.

Source: https://arxiv.org/abs/2611.17316

**Evolved memory programs gained up to 12 percentage points at 35% of the serving cost of hand-designed baselines.** MAPE searches complete memory programs and repeatedly found two useful patterns: preserve raw conversations as retrievable evidence, then compose the evidence for the current query. Adding its composition module improved five existing memory systems.

Source: https://arxiv.org/abs/2611.17068

**Delegating a search task to another agent did not consistently improve accuracy.** On purpose-built pre- and post-cutoff datasets, delegation sometimes degraded results when the orchestrator lacked the needed knowledge, while direct tool use by the same model worked better. Distorted delegated queries, inefficient tool use and lost information were recurring failures.

Source: https://arxiv.org/abs/2611.16526

**AgentSSL beat the strongest human-engineered baseline in 8 of 12 settings, then lost as much as 47% when it selected its own program.** The agents combined semi-supervised learning techniques under limited labels and matched compute, with gains of up to 21.8%. Program selection became the bottleneck, so the researchers released ProgramSelectBench with 16,977 generated and engineered programs.

Source: https://arxiv.org/abs/2611.17323

**AI peer reviewers differed by about 50 percentage points even under the same prompt.** A benchmark injected 357 localisable errors into 30 real astrophysics and machine-learning papers and tested 12 reviewer systems. Tools helped when they supplied a missing capability: enforced citation retrieval led by a wide margin in astrophysics, but not in machine learning, where the models appeared to know the literature better.

Source: https://arxiv.org/abs/2611.17052

**A weak decision actor could still teach a stronger policy.** On ALFWorld, all six tested models could be distracted by an easier sub-goal when acting, yet whole-trajectory judges credited the necessary earlier actions. Using JEV as a teacher raised a Qwen2.5-1.5B policy from 72.8% to 82.9% success on ALFWorld and from 56.8% to 71.4% on WebShop.

Source: https://arxiv.org/abs/2611.17167

**AI-generated proofs used a stable style that differed from human proofs of Euclid.** Three models independently re-proved all 465 propositions in the *Elements*. AI runs had mean citation similarity of about 0.68 with one another and 0.37 with human proofs; roughly 40% of AI citations returned to definitions, postulates and common notions, compared with 13% in the human baseline.

Source: https://arxiv.org/abs/2611.16527

**Offline benchmarks and live A/B tests can rank interactive models differently.** The theoretical study separates performance on a common prompt distribution from performance after users adapt their prompts and task difficulty to a model's responses. It gives a sufficient condition for the rankings to agree and argues that evaluation should measure the behaviour a model induces in users.

Source: https://arxiv.org/abs/2611.17239

## Economy and work

**A screened board counted 1,975 live AI-work listings, but only 57% were conventional jobs.** getAIwork classified 1,121 jobs, 747 paid platform programmes and 107 freelance gigs on 13 November; 34% were remote and 14% beginner-friendly. Its pipeline had screened 50,192 raw posts, with a person approving every surviving listing.

Rates appeared in 65% of listings, so the board's salary medians cover advertised rates in that subset, not pay received or the wider labour market. The page publishes its method and machine-readable data.

Source: https://getaiwork.com/articles/ai-job-market-statistics/

**Companies still report isolated AI gains rather than economy-wide productivity growth.** Axios found that adoption outside software engineering remains experimental and that regulated firms, especially banks, are wary of agents that can move money or create liability. The report synthesises company experience rather than presenting a new controlled dataset.

Source: https://www.axios.com/2026/11/13/ai-productivity-workplace-adoption

**Anthropic is hiring a natural-gas supply lead as it plans on-site generation for some data centres.** A job listing cited by Business Insider offers up to $405,000 and says some campuses will use gas-fired power behind the meter. The listing documents a plan rather than a deployed capacity figure, and the faster access to 24-hour power comes with emissions that conflict with earlier green-energy goals across the technology sector.

Source: https://www.businessinsider.com/anthropic-hires-gas-supply-lead-ai-plans-accelerate-ipo-2026-11

## Prompting techniques

**Backend skills turn recurring security and migration requirements into instructions that coding agents load for each task.** The API skill scopes queries to the caller and rate-limits sensitive routes; the data skill adds locks, conditional updates and idempotency; the migration skill uses expand-then-contract changes, concurrent indexes and batched backfills. Teams can fill a “Make it yours” section with their own error format, documentation and rollback conventions.

Source: https://github.com/globalmpc/backendskills

## What people are building

**Memro gives Claude Code, Cursor and Codex persistent memory through an API, SDKs and MCP.** The self-hosted Go service combines PostgreSQL 16, pgvector and full-text search through reciprocal-rank fusion, with Ed25519 identities for agents. Its PolyForm Noncommercial licence permits personal and research use; commercial use needs a subscription or licence.

Source: https://github.com/memrohq/memro

**AI Juggler collects Claude and Codex sessions, accounts and measured limits in one macOS app.** The local-first tool can move a conversation between tools, show process resource use and compare CLAUDE.md with AGENTS.md. It does not proxy traffic or store account credentials.

Source: https://github.com/figurehead-ai/AI-juggler

**Langfuse added a Rust gateway that preserves the native OpenAI and Anthropic API formats.** It relays JSON or streaming responses, records request and response facts and uploads each generation through OTLP. The service can run locally with the existing open-source Langfuse stack.

Source: https://github.com/langfuse/langfuse/tree/main/ai-gateway

**Harness Tuner searches an agent's tools, prompts, skills, model and settings against held-out evaluations.** Its experiment graph keeps training, validation and test access separate and can optimise quality, cost or speed. Kiln reports one production agent had 2.5 times fewer failures, sixfold lower cost and half the latency after tuning; those are the builder's measurements.

Source: https://github.com/Kiln-AI/harness-tuner

**Executor turns a specification into reviewed stacks of pull requests and leaves the merge to a person.** The Claude Code plugin uses Opus for review, Sonnet for building and verification, and separate agents that try to disprove every critical finding before a fix. Its published recent builds cost $2.18–$2.58 per reviewed pull request.

Source: https://github.com/sebwilgosz/agent-executor

## Worth reading

**The No AI Slop manifesto calls for disclosure of generative AI and human responsibility for mistakes.** It distinguishes assistive uses such as correction from replacing human creation. The document is a normative proposal, not evidence that a label will improve quality or trust.

Source: https://www.slopmanifesto.com/

## Hacker News

**A five-hour Claude outage became a debate about dependence on coding agents.** The incident affected claude.ai, Claude Code and the platform API. Practitioners compared fallback tools and described interrupted work, but the thread offers experience reports rather than a productivity measurement.

Source: https://news.ycombinator.com/item?id=50481187

**Commenters disputed why Google removed Search access from some AI-free schools.** Theories included filtering requirements, product bundling and contract restrictions. The discussion is speculation around NPR reporting and does not establish Google's motive.

Source: https://news.ycombinator.com/item?id=50484960

## YouTube

**Game developer Jonathan Blow argues that faster code generation has not produced visibly better software.** His 1-hour-40-minute English talk separates writing code from choosing a product, preserving system coherence and maintaining it over time. It is an experienced developer's argument, not a measured evaluation.

Source: https://www.youtube.com/watch?v=IRK8h67ol7Q

## In brief

**The US AI task force discussed liability-protected reporting of AI-powered attacks on critical infrastructure.** Reuters reports that members considered national incident standards and information sharing for banking, energy and emergency services. The 2015 law that protects some defensive sharing expires next month.

Source: https://www.reuters.com/world/us/trumps-ai-task-force-met-thursday-discussed-ai-powered-cyberattacks-2026-11-13/

**MobileProbe adapts prompt-injection attacks to the route that a phone agent actually takes.** The preprint's red-team framework finds attacker-controlled screens and evolves payloads at vulnerable decisions across 83 long-horizon attack cases in 12 apps. It reports higher attack success than human-written and earlier automated baselines, but its abstract does not give absolute rates.

Source: https://arxiv.org/abs/2611.16693

**The EU's Article 50 transparency guidance reached the Official Journal.** The Commission explains how providers and deployers should disclose interaction with AI and mark synthetic content under duties that have applied since 2 August 2026. The guidance is non-binding; the underlying AI Act obligations are law.

Source: https://op.europa.eu/en/publication-detail/-/publication/caabe0cd-de39-11f1-ba80-01aa75ed71a1/language-en
