+++
title = "Kevin Liao proposes document-based agent memory"
description = "The developer's workflow keeps specifications and decisions in editable Markdown. His argument comes with an open-source implementation, but no comparative benchmark."
tags = ["agents", "tools", "essays"]
date = 2026-10-04T09:23:37+02:00
draft = false
+++

Developer Kevin Liao proposes giving coding agents a maintained collection of project documents, arguing that retrieval of isolated conversation snippets leaves too much of a project's meaning behind.

In an essay published on 3 October, Liao describes a workspace containing instructions, specifications, decisions, research and an index. An agent consults the relevant documents before work and updates them afterward, while the reasons for its changes remain in context.

For a developer returning to a project in a new session, the attraction is a record that both the human and the agent can inspect. A specification can preserve the feature's purpose and constraints together, while a decision document can record why an approach was chosen.

Liao's criticism centres on similarity-based retrieval. He argues that a relevant-looking snippet can be outdated, omit its original context or conceal a gap the agent has no reason to search for. His claim that the entire memory-plugin category shares these problems is an opinion, supported in the essay by his own experience rather than a comparison of competing systems.

His alternative changes the maintenance rule. When the project changes, the agent edits the current document instead of merely adding another recollection of what happened. Liao says he began with an internal folder more than a year ago and developed that practice into Operator Memory.

The open-source project's README describes three document locations: private project knowledge, shared repository knowledge and personal rules used across projects. It lists adapters for Claude Code, Codex and other harnesses, and documents installation through an npm helper.

The repository also acknowledges a practical dependency: a new project starts with sparse documentation, so specifications need to be written before later sessions can maintain them. Reliable updates during long conversations remain on its roadmap. Operator Memory is available under the BSD 3-Clause licence.

## Verification

| Claim | Label | Primary source | Independent check |
| --- | --- | --- | --- |
| Kevin Liao published the document-memory essay on 3 October; instructions, specs, decisions, research and index; consult/build/update workflow | VERIFIED | [Source](https://liao.gg/blog/agents-dont-need-memory) | none |
| Similarity retrieval can omit context, surface stale knowledge and leave unknown gaps; broad criticism of memory plugins | OPINION | [Source](https://liao.gg/blog/agents-dont-need-memory) | none; author's argument, no comparative benchmark |
| Liao says he used the approach for more than a year and developed Operator Memory | VENDOR-REPORTED | [Source](https://liao.gg/blog/agents-dont-need-memory) | none; self-reported usage |
| Private, shared and personal document locations; listed Claude Code and Codex adapters; npm helper; BSD 3-Clause licence | VERIFIED | [Source](https://github.com/aerovato/operator-memory) | none; documented implementation and licence, not runtime validation |
| Sparse initial documents and reliable-update roadmap | VERIFIED | [Source](https://github.com/aerovato/operator-memory) | none; README disclosures |
| Editable records let humans and agents inspect project purpose and decisions together | ANALYSIS | [Source](https://github.com/aerovato/operator-memory) | Inference from readable Markdown and canonical-document updates |
