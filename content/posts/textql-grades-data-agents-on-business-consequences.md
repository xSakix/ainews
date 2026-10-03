+++
title = "TextQL grades data agents on business consequences"
description = "Argo-Bench hides a simulator’s ground truth behind an enterprise warehouse. Its strongest tested model solves about a third of the tasks."
tags = ["research", "agents"]
date = 2026-10-03T05:43:20+02:00
draft = false
+++

TextQL’s Argo-Bench finds that strong data agents still struggle to turn enterprise records into correct decisions, with its best tested model solving about a third of the benchmark’s tasks.

Gabriel Tomitsuka and four colleagues at TextQL, a data-agent company, built a simulated food-delivery business and exposed its records through an enterprise warehouse. Agents can query and analyze those records, but the grader knows what actually happened and scores the consequences of their answers and actions.

**Why it matters:** A finance analyst reviewing an agent’s budget recommendation needs the right business objective as well as a technically sound calculation. Argo-Bench makes that distinction measurable: a plausible analysis can earn a poor score when its decision wastes money.

The [preprint](https://arxiv.org/abs/2610.02122), first submitted on 1 October, describes 210 tasks spanning analytics, forecasting, fraud and financial planning. Its authors tested 14 frontier and open-weight models. Claude Opus 5.5 led overall, solving roughly 35% of tasks under the authors’ threshold and averaging about 60 points.

A task counts as solved when its score reaches at least 95. That threshold differs from the average score: a model can earn partial credit across many tasks without completing them to the required standard. The two measures answer different questions about reliability.

The warehouse contains about 7.5 billion rows spread across 235 tables in an Oracle E-Business Suite format. Its underlying world simulates New York City food delivery in 2024. An order creates related dispatch, courier-pay, merchant-payout and ledger records, so reconstructing a business event requires connecting the right records.

The simulator is the benchmark’s answer key. Like an exercise whose instructor holds the complete case file, it gives the agent incomplete operational evidence while preserving enough hidden information to check what the evidence means. A fraud decision can therefore be graded on losses prevented and legitimate revenue wrongly removed.

## Correct calculations can serve the wrong objective

One reported failure concerns courier bonuses. An agent estimated how bonuses affected available courier hours and cut spending where those hours were most expensive. The platform’s stated economic objective, however, was to reduce surge pay. Another model examined that relationship and found a better allocation.

The mistake arose before the arithmetic. The agent selected a reasonable-looking measure that did not match the decision’s purpose. The benchmark can expose that failure because its grader evaluates the proposed allocation inside the same simulated business rather than matching a query to a written answer.

Membership analysis showed a different failure. Some agents read membership from contract dates, although a declined payment could remove benefits before the contract disappeared. Passing runs reconstructed the billing history and checked it against benefits actually applied to orders. A valid table join was insufficient when it represented the wrong business state.

The published results remain the authors’ own measurements. TextQL builds products in the category being evaluated, and the preprint has not supplied independent reproduction of its model ranking. The released public warehouse also differs from the private-seed world used for the reported experiments and leaderboard.

The simulation has boundaries. It covers one city, one year and one enterprise-system format. Public aggregate figures constrain its economics, but some behavioral assumptions remain weakly grounded; the authors specifically flag the membership program. Scores therefore compare agents in this constructed setting rather than estimate performance at an actual company.

The agent works in a sandboxed Python environment with statistical and optimization libraries. It files results through an interface for decisions, allowing the benchmark to evaluate what the agent commits rather than only the text it generates.

The team has released the [warehouse](https://huggingface.co/datasets/textql/Argo-Bench), plus [tasks, reference solutions and execution tools](https://github.com/TextQLLabs/Argo-Bench). These materials make the scoring logic inspectable. The paper names adding SAP S/4HANA and more complex, multi-business records as extensions beyond the present Oracle-format world.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Tomitsuka and four coauthors work at TextQL; preprint v1 submitted 1 October 2026. | VERIFIED | https://arxiv.org/abs/2610.02122 | none |
| 210 tasks, 14 models; best Opus 5.5 solved 34.8% at score ≥95 and averaged 59.5 points. | VENDOR-REPORTED | https://arxiv.org/abs/2610.02122 | none |
| Simulated NYC 2024 food-delivery warehouse has 235 Oracle EBS-format tables and 7.49 billion rows; grader uses hidden state and decision consequences; sandboxed Python and filing interface enable execution. | VENDOR-REPORTED | https://arxiv.org/abs/2610.02122 | none |
| Bonus-allocation and membership-record failures illustrate wrong objectives and records; public and evaluation seeds differ. | VENDOR-REPORTED | https://arxiv.org/abs/2610.02122 | none |
| One city/year/ERP format and weak membership assumptions limit generalization; SAP extension proposed. | VERIFIED | https://arxiv.org/abs/2610.02122 | none |
| Warehouse and tasks/reference/tool code are offered publicly. | VERIFIED | https://huggingface.co/datasets/textql/Argo-Bench ; https://github.com/TextQLLabs/Argo-Bench | none |
| Finance analysts need objective correctness alongside calculations; instructor-case-file comparison explains hidden ground truth. | ANALYSIS | https://arxiv.org/abs/2610.02122 | none |
