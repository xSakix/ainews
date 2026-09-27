+++
date = '2026-09-27T04:02:40+02:00'
draft = false
title = 'KoboldCpp Adds a Built-In Local Agent'
+++

# KoboldCpp Adds a Built-In Local Agent

KoboldCpp has added an agent mode to its local model runner, giving users a compact tool-using loop without requiring a separate coding-agent application.

Version 1.122, published on 26 September, introduces KoboldCpp Agent with nine built-in tools and a system prompt that the project says uses roughly 2,000 tokens. Users can enable it from the Admin interface or with the `--agent` launch option. It can run against a model hosted by KoboldCpp, a third-party provider or another service exposing an OpenAI-compatible Chat Completions endpoint.

## Why it matters

Local inference has usually answered only one part of the agent question: where the model runs. The surrounding loop still needs to describe tools, parse calls, request approval, execute actions and return results to the model. Folding that loop into KoboldCpp makes an agent available in the same package many users already use to serve local GGUF models.

That convenience also concentrates risk. A conversational model that can read or modify files is no longer just generating text. KoboldCpp therefore provides three approval modes: one that asks before actions, an automatic mode, and an off setting. The release notes explicitly urge caution when permissions are relaxed. The safest practical default remains to expose only the directories and tools a task actually needs.

## Two tool paths

The built-in tools run on the client side. They cover common agent operations and arrive with the application. Model Context Protocol, or MCP, tools work differently: users define them in an `mcp.json` file, and those tools execute on the server side. That distinction matters when the interface and inference server are on different machines. It determines which machine holds credentials, reaches private services or touches a filesystem.

The release also adds support for `AGENTS.md`, a project-level instruction file used by several coding agents. Context compaction is included to keep longer sessions moving when their histories approach the model's context limit. Neither feature guarantees that an agent will preserve every important instruction; compaction is a lossy summary step, and project guidance still depends on the model following it.

KoboldCpp recommends at least a 28,000-token context window, an 8,000-token generation allowance and roughly 12GB or more of VRAM for agent use. Those are project recommendations, not hard compatibility limits or independent benchmarks. A smaller setup may run, but long tool transcripts and large code files can consume context quickly.

## Broader inference changes

The agent is the headline feature, but version 1.122 also separates `ubatch` from batch size, adds automatic parallel settings, introduces an autoswap threshold and includes tool-parser and error-handling fixes. These changes target throughput and memory management around model serving. Their effect will vary with model format, accelerator, context length and concurrent load.

The release positions KoboldCpp Agent as a lightweight alternative to tools such as Codex, Claude Code and OpenCode. That comparison describes product shape, not demonstrated capability. The notes do not provide a controlled task benchmark against those systems, and a local model's planning and coding quality will depend heavily on the model chosen.

For local-AI users, the useful development is architectural: model serving, tool orchestration and approval controls can now live in one familiar runtime. The next evidence to look for is not a dramatic demo but reproducible tests—successful task rates, permission failures, context-compaction errors and resource use across common local models.

## Verification

- **Tier 0 — VERIFIED:** The official KoboldCpp v1.122 release page documents the integrated agent, nine built-in tools, MCP support, approval modes, `AGENTS.md`, context compaction and runtime recommendations: https://github.com/LostRuins/koboldcpp/releases/tag/v1.122
- **Tier 1 — PROJECT-REPORTED:** Claims that the agent is lightweight and that its prompt uses about 2,000 tokens come from the project release notes.
- **Tier 2 — ANALYSIS:** Security trade-offs, deployment implications and the need for reproducible task evaluations are editorial analysis.

## Glossary candidates

- **MCP:** Model Context Protocol, a standard for connecting AI applications to external tools and data sources.
- **GGUF:** A model-file format widely used by llama.cpp-compatible local inference software.
- **Context compaction:** Summarizing older conversation or tool history to free space in a model's context window.

Cold-reader sentence: KoboldCpp now bundles a tool-using agent, reducing setup for local automation while making permission controls more important.
