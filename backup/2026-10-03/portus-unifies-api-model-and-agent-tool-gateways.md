+++
title = "Portus unifies API, model and agent-tool gateways"
description = "A Rust gateway publishes Kubernetes routing, provider-token budgets and MCP federation together, with builder-run benchmarks."
tags = ["projects", "tools", "agents"]
date = 2026-10-03T05:36:20+02:00
draft = false
+++

Portus, a Rust gateway project, combines ordinary API traffic, language-model calls and agent-tool connections behind one configurable data plane.

Its Kubernetes controller compiles routing and policy objects into configuration for gateway processes. Those processes route requests to application services, model providers or Model Context Protocol servers, which expose tools to agents.

**Why it matters:** A platform engineer can inspect one gateway’s code and policies for both application traffic and AI access. The project documents provider keys, token budgets and tool allowlists alongside standard HTTP and transport routing.

Portus publishes a throughput result of about 126,000 requests per second from three proxy pods on a 10-vCPU Linux virtual machine running on an Apple M4. Its authors used three interleaved rounds against agentgateway, another gateway implementation, and report a lower measured tail latency at a fixed load. Those are same-machine builder comparisons, with test conditions and rounds linked from the project.

The model gateway routes on the requested model while forwarding the provider’s request format. A separate ledger issues hashed gateway keys, distributes budget state and accounts for token use. Budgets can be attached to a key, user, tenant or route, with reservation before a model call and settlement afterward.

The tool gateway can combine several MCP servers behind one endpoint, naming tools with a server prefix. Routing can use the JSON-RPC method and named tool, while locally verified identity tokens supply groups and scopes for access policy. The documentation also describes per-key call budgets and allowlists.

The underlying network implementation changed during development. Portus now uses Rama by default after a separate same-machine comparison against Pingora; the published headline throughput table still identifies the earlier Portus version. That version boundary matters when reading the performance figures.

The repository supplies source, Kubernetes examples and standalone operation from a YAML configuration file. Its current release page offers the implementation and benchmark artifacts together, allowing the routing design to be studied without treating one machine’s results as a universal capacity figure.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Published Rust gateway code; controller/configuration/data-plane design; Kubernetes and standalone modes. | VERIFIED | https://github.com/portus-gateway/portus | none |
| Portus0.2.3 126070 req/s; three pods, 10-vCPU Linux/Apple M4, three interleaved rounds; p99 0.35 vs0.82 ms at30000 req/s. | VENDOR-REPORTED | https://github.com/portus-gateway/portus | none |
| Model routing, hashed keys, reservations/budgets/settlement, MCP federation/identity/allowlists; Rama default from0.2.4 after single-round Pingora comparison. | VENDOR-REPORTED | https://github.com/portus-gateway/portus | none |
| Common policies make application and AI gateway behavior inspectable in one implementation. | ANALYSIS | https://github.com/portus-gateway/portus | none |
| Project publicly shown on dated thread. | VERIFIED | https://news.ycombinator.com/item?id=49938517 | none |
