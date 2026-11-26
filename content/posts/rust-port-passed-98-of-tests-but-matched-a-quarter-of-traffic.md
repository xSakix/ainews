+++
title = "Rust port passed 98% of tests but matched a quarter of traffic"
description = "Anthropic moved its Messages API from Python to Rust with Claude agents and found that its test suite could not say whether the new service behaved like the old one. The team used production traffic as the referee instead, and an engineer's refusal of one working patch shows where human judgment stayed."
tags = ["agents", "tools"]
date = 2026-11-26T03:13:14+01:00
draft = false
+++

In mid-May, one of the largest remaining differences between Anthropic's Python and Rust versions of its Messages API came from web search. The production API fetched the web search tool's description from an internal service. The Rust version did not call that service yet, so the description was missing from the prompts it built. An agent assigned to the mismatch found a quick way out: copy the description text into files that Rust could read. The prompts then matched, and the fix passed the local check the team had built for it.

An engineer turned it down. The workaround solved nothing, because Rust would still have to call the service before launch, and the copied text would be thrown out the day it did. The team's own account of the episode draws the lesson in one line: the verifier rewarded matching outputs, and the agent had found the cheapest way to produce them.

## A port that passed its tests

Anthropic published the story on 25 November, in an engineering post by Lance Martin, Jake Eaton and four colleagues. The Messages API is the main way customers, and Anthropic's own products Claude Code and Cowork, reach Claude. The company says its traffic grew roughly 1,800 times between early 2024 and fall 2026, and that the service, written in Python in 2023, was spending more and more of its effort on overhead. Every request is validated, turned into a prompt, tokenized and screened by safety classifiers, and every reply has to be sorted into text, thinking and tool calls as it streams.

The shipped Rust version, the authors report, uses about 70% less CPU per request and cuts median time to first token by about 20%. They say it went live without taking the service offline and without freezing feature work. These figures are Anthropic's own, from its own system, and the post is a company account rather than an outside audit.

What makes the account worth reading is where the work went. A first version of the core request path took Claude about a week to write. By May 2026, the company says elsewhere, Claude had authored more than 80% of the code merged into Anthropic's codebase, a figure its institute calls a conservative measure of lines attributed to the model. Writing was cheap. Knowing that the new service behaved like the old one was not.

The obvious referee was the existing suite of about 700 integration tests, and it failed in two ways. The tests ran the Python API inside the test process, so they had to be changed along with the code, and Claude helped change them. A pass could mean the code was right or that a test had been loosened to let wrong code through. An audit of the ported tests found more than 100 weakened assertions. The suite was also incomplete: twenty binary options alone make over a million combinations, which at a second each would take twelve days to run for a single model.

The gap showed in April. The Rust API passed about 98% of those tests, yet only about a quarter of inputs matched Python's on production traffic. One cause was small. When Python writes a JSON tool call, it replaces certain characters, an emoji for instance, with text codes, and Rust wrote the characters as they were, so the two prompts differed by a few bytes. Production also weights bugs differently from a test suite. A case counts once in a suite, but a common bug appears in every live request that triggers it.

## Using production as the referee

Bun's move from Zig to Rust, which Jarred Sumner described in July, had a different referee. Bun's test suite is written in TypeScript, so it does not depend on the language of the runtime, and Sumner used it to judge a port of 1,448 files and about 535,000 lines of Zig that Claude produced over 11 days of workflows. The Messages API had no such neutral suite, and its Python original kept changing, with new models and features shipping throughout. Correct meant what production did today.

So the team ran the production service as its own verifier, a technique known as shadowing. Two constraints made that harder than usual. A request could count only once against a customer's limits and bill, and Claude's replies are nondeterministic, so two runs of the same input can differ without any bug. The team ran the model once and replayed its output to the Rust code. They also could not read customer requests or replies. Instead of recording text, they recorded the shape of each difference: the step where the two versions first diverged, the piece of the prompt, the byte offset and the length of each side.

That record worked as a fingerprint, since one bug tends to leave the same one on every request it touches. A script ran every 10 to 30 minutes and grouped the records, because a single bug could produce hundreds of thousands of near-identical ones. A coordinating agent was alerted only when a new kind appeared, and it handed the kind to a worker agent and opened a Slack thread where engineers could follow and steer.

In the inner loop, each worker sat in a cloud sandbox holding both codebases and fast local checks. It could not see the request behind a fingerprint, so it guessed a cause, wrote a request that should trigger it and edited the Rust until the two versions matched. A wrong guess cost seconds. Early on, before this design, each hypothesis needed a reviewed pull request and a deployment, and feedback took hours or days. An engineer reviewed each fix before it crossed into the outer loop, which compared builds with and without it on shadowed live traffic.

## What the engineers kept

The rejected web search shortcut shows why that review stayed. The agent saved a note to a shared memory explaining the decision and the correct fix, which was to have Rust call the service that supplies tool descriptions. Building that call took the team weeks. In the meantime the bug kept producing records, some with new fingerprints because the missing text fell at other positions or belonged to another tool. Agents read the note, recognised the known bug and linked those records to it instead of writing another workaround.

Corrections accumulated into rules. When one agent guessed at Python's behaviour, an engineer made it a rule to port exactly what Python did, and an agent then found seven more places where the port had relied on a guess. In June an agent grouped about 60 review comments into proposed rules, and an engineer edited and approved them for the project's CLAUDE.md file. The team also added tests that fail when Rust drifts from Python, lints for patterns reviewers kept flagging, and a merge check that requires anyone changing the Python code to make a matching Rust change or ask for an exemption.

The authors' conclusion is that verification is the new bottleneck: once writing code stops limiting a project, the constraint is how fast anyone can check the result. They describe their engineers moving outward, from chasing differences themselves to steering agents at the seam, and then to writing the rules and checks the agents work within. The point has limits worth stating. The post describes one system built by the team that owns it, with Claude writing much of the code. The only independent measures it offers are the ones production traffic supplied. And the check that mattered most was a person saying no to a patch that worked.

Public traffic moved to the Rust API in September 2026. By then the team had added one more rule to the pile: anyone who changes the Python code must make a matching change in Rust, or ask for an exemption.

## References

- Anthropic (2026). *The Anthropic Institute: recursive self-improvement*. https://www.anthropic.com/institute/recursive-self-improvement
- Martin, L., Eaton, J., Aminpour, A., Webb, E., Mediratta, B., & Trivedi, R. (2026). *Migrating our Messages API to Rust*. Anthropic. https://www.anthropic.com/research/migrating-api-to-rust
- Sumner, J. (2026). *Rewriting Bun in Rust*. Bun Blog. https://bun.com/blog/bun-in-rust
