+++
date = '2026-09-22T04:00:20+02:00'
draft = false
title = 'Linear Rebuilds CI for Agent-Written Code'
+++

*Linear says AI agents now write most of its tests, pushing the company to redesign continuous integration as its test suite nearly quadrupled during 2026.*

Linear, the software company behind a project-management platform, found that generating code faster moved delay into verification. Every pull request still had to wait for checks. The company changed runners, reduced repeated setup, shortened gate jobs and rebalanced tests to keep feedback from slowing developers and agents.

## Why it matters

Coding agents can increase the number and size of changes a team attempts. If testing capacity does not grow with that output, developers wait longer, compute bills rise and automated agents remain idle. The constraint moves from producing code to proving that the code works.

Linear reports that its test suite nearly quadrupled from the start of the year. Despite that growth, it reduced pull-request wait time from more than six minutes to just over five and cut runner time per test roughly in half. These are the company's internal measurements, not a general benchmark for all software teams.

Some gains came from faster infrastructure. Linear moved workloads away from standard GitHub Actions runners to third-party machines and reports that comparable jobs ran 34% faster on average. Replacing the TypeScript compiler with the native `tsgo` implementation reduced the weekly median type-check time by 73%.

## Remove work before adding machines

Several changes attacked repeated setup. Restricting dependency installation to the API package cut installation from 44–73 seconds to 16–18 seconds. Consolidating seven short checks into two jobs, then running the tasks concurrently inside them, reduced repeated runner startup and setup.

Linear estimates that the consolidation would save about 87,000 runner-minutes each month based on June usage. That number depends on the company's workload and pricing, but the method is broadly applicable: measure fixed overhead before paying to parallelize every task.

The team also shortened gate jobs that decide what later work should run. Limiting repository checkout reduced one change-detection job's median duration from 26 seconds to eight. Moving a cache-marker write off the merge-critical path removed another 42 seconds for affected API changes.

The highest-risk optimization allowed selected test files to share module state rather than rebuilding it for every file. Linear reports that the change delivered roughly 17% monthly savings at its volume. It required explicit opt-in markers and cleanup rules because shared state can make tests affect one another.

The company says agents now write the majority of its tests, so it updated agent instructions to follow the new isolation rules. That detail turns CI configuration into part of the agent harness: a generated test must be correct and must fit the execution model used to verify it.

The lesson is not that every team should copy Linear's stack. It is to profile queue time, setup and critical paths separately. The next evidence should show whether the gains persist as the repository grows and whether shared-state tests increase flaky failures.

## Verification

1. **VERIFIED AS COMPANY-REPORTED — Linear says its suite nearly quadrupled, pull-request wait fell from over six to just over five minutes, and runner time per test roughly halved.** Primary source: https://linear.app/now/ci-bottleneck-reworked
2. **VERIFIED AS COMPANY-REPORTED — The runner move, `tsgo` change, dependency filtering and checkout reductions produced the stated timing gains.** Primary source: https://linear.app/now/ci-bottleneck-reworked
3. **VERIFIED AS COMPANY-REPORTED — Linear estimates 87,000 monthly runner-minutes saved by batching seven checks into two jobs.** Primary source: https://linear.app/now/ci-bottleneck-reworked
4. **VERIFIED — Linear says agents write most of its tests and that agent instructions now include shared-state rules.** Primary source: https://linear.app/now/ci-bottleneck-reworked

## Glossary candidates

- **Continuous integration:** Automated checks run when code changes.
- **Critical path:** The chain of steps that determines total completion time.
- **Test isolation:** Keeping one test's state from affecting another.

Cold-reader sentence: Linear redesigned CI after agent-written tests multiplied, cutting waits through faster runners, less setup and carefully controlled shared test state.
