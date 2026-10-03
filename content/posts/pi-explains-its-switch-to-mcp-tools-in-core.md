+++
title = "Pi explains its switch to MCP tools in core"
description = "The maintainers argue that structured tool composition changed their earlier objection to the protocol."
tags = ["essays", "agents", "tools"]
date = 2026-10-03T05:25:20+02:00
draft = false
+++

The maintainers of Pi, a coding-agent harness, explain why they added the Model Context Protocol to its core after publicly resisting the integration.

Their September 29 engineering post says the change is about the machinery around tools as much as the protocol. Pi now exposes MCP tools through a JavaScript sandbox where an agent can combine calls and process their results.

**Why it matters:** A developer connecting an agent to several services needs those services to work together. Earendil Engineering argues that structured results and discoverable descriptions make composition more useful than filling a model's context with a large catalogue of tools.

The maintainers still criticise MCP's composability. Their preferred direction is closer to a documented API: tools return data, and the agent discovers the operations it needs. They say many existing servers instead assume that every tool will be loaded into the conversation and optimise their output around text.

Pi's design also distinguishes tools available directly to the model from tools intended for code orchestration or deferred loading. The authors say an ordinary extension lacked enough metadata to handle those choices cleanly, which helped justify placing the support in core.

Their example combines issue-tracker queries with a decision model that classifies the tone of comments. JavaScript coordinates the calls and retains the results for later inspection. It is a demonstration supplied by the maintainers, not an independent test of the classifications.

The practical distinction is between adding a connector and defining how several connectors cooperate. A team evaluating an integration should inspect that second layer: the result types, the execution boundary and the records kept for review. Pi loads its code-orchestration sandbox automatically when MCP is configured; it can also be enabled separately.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Pi maintainers, September 29 publication, reversal and current MCP/codemode support. | VENDOR-REPORTED | https://earendil.com/posts/you-said-no-mcp/ | None; attributed primary account. |
| Structured results, discovery, metadata and composability rationale. | OPINION | https://earendil.com/posts/you-said-no-mcp/ | None; attributed primary account. |
| Issue-tracker and decision-model example; automatic and separate codemode loading. | VENDOR-REPORTED | https://earendil.com/posts/you-said-no-mcp/ | None; attributed primary account. |
| Connector composition deserves separate architectural review. | ANALYSIS | https://earendil.com/posts/you-said-no-mcp/ | None; attributed primary account. |
