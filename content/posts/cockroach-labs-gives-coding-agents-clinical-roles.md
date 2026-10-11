+++
title = "Cockroach Labs Gives Coding Agents Clinical Roles"
description = "MOLT Sinai routes software work through specialised agents, mandatory plans and adversarial review. The company reports seven reverts over five months."
tags = ["agents", "tools", "essays"]
date = 2026-10-11T04:03:06+02:00
draft = false
+++

Cockroach Labs has described a coding-agent pipeline that treats software issues like hospital patients, with specialised roles and mandatory review before implementation begins.

The system, called MOLT Sinai, runs through GitHub Actions. Labels carry state between a triage agent, a workup stage, a Fellow that proposes treatment, a Review Attending that attacks the plan and a discharge stage. The authors say it processed more than a million lines with seven reverts over five months.

## Why it matters

A maintainer delegating a repository change to an agent needs more than a capable model: the process must preserve scope, expose decisions and stop weak plans before they become code. MOLT Sinai turns those requirements into workflow state and written skills instead of relying on one long prompt or an agent's memory.

Its strongest rule is procedural: no code before a plan, and no plan without review. The Review Attending is instructed to find faults rather than cooperate reflexively. If work moves outside the approved scope, another rule says “Don't improvise”; the agent must stop and re-plan. Tests cannot be weakened merely to make a change pass.

Adam Storm and Rafi Shamim, engineers at Cockroach Labs, report 27 merged pull requests and 55 reviewer send-backs. They describe adding a Db2 migration source in under two days for $4,172 in model-token costs. Their comparison with a nine-month, roughly $160,000 Oracle integration illustrates the claimed difference, but it is not a controlled like-for-like productivity study.

The design deliberately adds bureaucracy. Each handoff consumes tokens and time, and the authors say the pipeline can be slower and more expensive than a swarm. Its purpose is not maximum parallelism; it is to make the path from issue to merged code inspectable and to assign a distinct responsibility to each stage.

The reusable idea is smaller than the hospital metaphor. Store state outside the chat, require an explicit plan, separate the author from the critic and encode stop conditions in the agent's instructions. Those controls can be copied without reproducing every role.

Cockroach Labs published the workflow as an engineering account, not an independent evaluation. The next evidence would be repository-level data comparing similar tasks under the pipeline and ordinary human or agent workflows, including review time, defect severity and work that never reached a merge.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| MOLT Sinai uses GitHub Actions, labels and role-specific agents to move issues through a staged workflow | VERIFIED | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | none |
| The workflow requires an approved plan before code and instructs agents to re-plan when scope changes | VERIFIED | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | none |
| Cockroach Labs reports 27 merged pull requests, 55 send-backs and seven reverts in five months | VENDOR-REPORTED | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | none |
| The Db2 migration source took under two days and $4,172 in token costs | VENDOR-REPORTED | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | none |
| The authors say the system adds time, cost and bureaucracy compared with a swarm | VERIFIED | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | none |
