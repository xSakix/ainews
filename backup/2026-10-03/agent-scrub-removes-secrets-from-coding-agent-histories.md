+++
title = "Agent Scrub removes secrets from coding-agent histories"
description = "A local macOS app finds duplicate credentials in saved conversations and can redact them without changing active login files."
tags = ["projects", "tools", "safety"]
date = 2026-10-03T05:55:20+02:00
draft = false
+++

Agent Scrub, a macOS utility published by developer thesubtlety, finds and redacts secret values left in the conversation histories of AI coding tools.

Coding assistants preserve more than the final answer: prompts, terminal output and saved memory can leave additional copies of a credential on disk. Agent Scrub treats those conversation records as a separate cleanup problem from the credentials an application actively uses.

**Why it matters:** A developer who pasted a token into a debugging session can find its repeated appearances across agent histories and remove those local copies through one interface. The app groups findings by secret, project and application.

The repository documents support for Claude Code, Codex, Gemini CLI, Cursor and several other tools. A menu-bar app scans when it starts and monitors supported history locations for changes; a coverage view identifies files it could not scan, while exclusions let users leave particular folders untouched.

Redaction replaces detected values with markers inside the original files. The tool rechecks and reparses files around each write, and temporarily skips records that an agent is still writing. The README warns that these changes cannot be automatically undone and cannot remove copies already sent to a provider or preserved in backups.

Agent Scrub deliberately leaves active authentication and configuration files alone. Its own state uses a per-install key stored in the macOS Keychain to fingerprint findings, so the database need not retain the detected values in plaintext. The developer says scanning, state and redaction remain local and the application makes no network connections.

The current app requires macOS 14 or later and supports Apple Silicon and Intel Macs. Source builds require Xcode 16 and Swift 6; distributed builds are currently unsigned, which affects the installation flow. A command-line companion offers scanning and policy operations, with writes kept as dry runs unless explicitly confirmed.

The project already exposes both application and command-line code. Its coverage screen and permanent-write behavior are the concrete boundaries of this first release: finding a secret is reversible inspection; redacting its surviving history copies changes the underlying records.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Published code; macOS 14+, Intel/Apple Silicon; Xcode 16/Swift 6 source build; unsigned distribution. | VERIFIED | https://github.com/thesubtlety/agent-scrub | none |
| Supported tools, scanning, grouping, exclusions, coverage, fingerprinting and local-only behavior are documented capabilities. | VENDOR-REPORTED | https://github.com/thesubtlety/agent-scrub | none |
| Redaction changes history files permanently; active credentials are excluded; active writes are skipped; remote/backed-up copies persist. | VERIFIED | https://github.com/thesubtlety/agent-scrub | none |
| Grouped history cleanup helps a developer locate repeated token copies. | ANALYSIS | https://github.com/thesubtlety/agent-scrub | none |
| Project publicly shown on dated thread. | VERIFIED | https://news.ycombinator.com/item?id=49939584 | none |
