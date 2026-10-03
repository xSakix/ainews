+++
title = "Hall Monitor tracks coding agents across machines"
description = "A read-only dashboard combines Claude Code and Codex sessions, local usage records and remote machines reached over SSH."
tags = ["projects", "agents", "tools"]
date = 2026-10-03T05:39:20+02:00
draft = false
+++

Hall Monitor, an MIT-licensed project by Hitesh Bandhu, brings Claude Code and Codex session status into a terminal dashboard and a native macOS interface.

The tool reads the records coding agents already leave behind and groups sessions by whether they are working, idle or waiting for a person. Remote sessions join the same view through the operator’s own SSH connections.

**Why it matters:** A developer running agents on a laptop and a GPU server can see which session needs attention without reopening every terminal. Hall Monitor shows the current operation, project, model and recent activity alongside that status.

The terminal board works on macOS and Linux. The Mac application adds a menu-bar view, notifications and a display around a MacBook’s screen notch, with links back to the relevant application or terminal. The project was previously called agentboard; its documentation says an upgrade preserves the old command and usage history.

Claude Code status comes from session metadata and transcript records. Codex status comes from live processes and session logs, with its app-server used when available. The project describes the interface as read-only: it neither sends prompts nor approves an agent’s proposed action.

Usage accounting has a narrower storage boundary than the live display. A local ledger retains counts for agent time, tokens, projects and cache use, rather than prompt text. Remote hosts stream session metadata over one SSH connection per host and reconnect when that connection drops.

Plan-limit readings use different routes. Codex limits come from its logs; Claude limits can be read by opening Claude Code’s own usage screen in a separate safe-mode session every 15 minutes. The README provides a switch to disable that probe and marks readings older than 15 minutes as stale.

Bandhu publishes source, binaries and Homebrew installation paths. The native app requires macOS 14 or later, while a source build of the terminal tool requires Go 1.26 or later. The read-only design leaves execution control in the original agent interface; the dashboard’s job is to expose where human attention is needed.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| MIT code; author; terminal macOS/Linux; native macOS 14+; Go 1.26+; agentboard rename. | VERIFIED | https://github.com/hiteshbandhu/hallmonitor | none |
| Status collection, native views, navigation, SSH streaming, reconnects and read-only controls. | VENDOR-REPORTED | https://github.com/hiteshbandhu/hallmonitor | none |
| Count-only ledger; Codex log limits; optional Claude safe-mode probe every 15 minutes; stale marker. | VENDOR-REPORTED | https://github.com/hiteshbandhu/hallmonitor | none |
| Shared display reduces the need to inspect each terminal for waiting agents. | ANALYSIS | https://github.com/hiteshbandhu/hallmonitor | none |
| Project publicly shown on dated thread. | VERIFIED | https://news.ycombinator.com/item?id=49941003 | none |
