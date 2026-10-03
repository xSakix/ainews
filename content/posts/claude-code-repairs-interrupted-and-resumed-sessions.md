+++
title = "Claude Code repairs interrupted and resumed sessions"
description = "Version 2.1.288 restores cleared drafts and adds code-review controls. Its fixes target context loss, timeouts and permission checks."
tags = ["tools", "agents", "safety"]
date = 2026-10-03T05:57:20+02:00
draft = false
+++

Anthropic released Claude Code 2.1.288 on 2 October, repairing several ways interrupted or resumed coding sessions could lose work, fail to continue or apply the wrong context.

Claude Code is Anthropic's coding agent for terminals and development environments. The update focuses on keeping a session coherent through disconnections, long responses and restarts, while adding controls for recovering a draft and changing how many review findings the agent reports.

**Why it matters:** A developer resuming a long coding task gets fixes aimed at preserving files, context and the last response. Those repairs address the continuity of the work already underway, rather than requiring the developer to reconstruct what the agent had seen.

The [official release](https://github.com/anthropics/claude-code/releases/tag/v2.1.288), published at 20:19 UTC, describes a new recovery gesture: pressing Up in an empty prompt restores a draft cleared with Ctrl+C, including pasted text and images. The `/code-review` command also accepts `--max-findings` with a number or `all`; the selection persists until reset to `default`.

Anthropic says non-interactive sessions and subagents now continue from a partial response after a mid-response API timeout. A separate fix handles long conversations that failed with a prompt-length error when the previous response reported zero token usage. Resume fixes cover restored context being dropped, the last response failing to save and transcripts being loaded while another process rewrites them.

The release also repairs permission handling. Anthropic reports that failed hook matching or an inability to serialize a tool's input now blocks the call instead of skipping the relevant permission hooks. It also fixes dangerous removal commands running without a prompt inside nested shell scripts under some permission settings. These are changes in the reported behavior; the release notes provide no independent security test.

Packages are available for macOS, Linux and Windows through the release page. The update adds a re-authentication prompt when a connected MCP server requests additional OAuth scope during a tool call, making that access change visible while the session is running.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Anthropic published version 2.1.288 on 2 October at 20:19 UTC with macOS, Linux and Windows packages. | VERIFIED | [Official release](https://github.com/anthropics/claude-code/releases/tag/v2.1.288) | none |
| Up restores a Ctrl+C-cleared draft, including text and images; code review supports persistent --max-findings settings. | VERIFIED | [Release changelog](https://github.com/anthropics/claude-code/releases/tag/v2.1.288) | none |
| Partial-response continuation, auto-compaction and the listed resume-context and transcript failures are fixed. | VENDOR-REPORTED | [Anthropic's fixes](https://github.com/anthropics/claude-code/releases/tag/v2.1.288) | none |
| Failed permission-hook processing blocks a call; nested shell removal checks and OAuth scope prompts are corrected. | VENDOR-REPORTED | [Anthropic's fixes](https://github.com/anthropics/claude-code/releases/tag/v2.1.288) | none |
| The continuity fixes help a developer retain the context of an existing task; no independent security test is provided in these release notes. | ANALYSIS | [Published release notes](https://github.com/anthropics/claude-code/releases/tag/v2.1.288) | none |
