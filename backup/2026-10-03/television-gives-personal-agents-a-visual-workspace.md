+++
title = "Television gives personal agents a visual workspace"
description = "Telepath publishes an MIT-licensed interface for persistent cards, interactive views and web pages alongside an existing agent harness."
tags = ["projects", "agents", "tools"]
date = 2026-10-03T05:35:20+02:00
draft = false
+++

Television, an MIT-licensed project from interface company Telepath, gives personal AI agents a persistent visual workspace alongside their existing chat interface.

An agent can create a document, chart or interactive view, place it in a channel and modify it later. The application preserves those artifacts as objects the person and agent can return to, rather than leaving every result inside a conversation.

**Why it matters:** A developer using a command-line agent can keep a task list or project view visible while the conversation moves on. Television supplies the display and storage conventions without requiring a new model provider.

The system has three parts. A lightweight server runs on the agent’s machine, a bundle of reusable instructions teaches the agent to create and update artifacts, and a client displays them. The client can be an installable macOS application or an experimental browser interface.

Telepath’s documentation requires an agent harness with file access and support for skills, the reusable instruction format used by several coding agents. The agent itself must run on Linux or macOS; agents running on Windows are currently unsupported, although the browser display can be opened from other platforms.

The Mac client is built with Electron, the framework for desktop applications using web technology. Its advantages over the browser version include artifacts that load external web pages. The published examples combine calendars, tasks, tables and draft documents, arranged across channels that retain related work.

Source installation requires Node.js 24 and a specified npm version range. The repository provides build commands and a server mode that persists as a system service, while the packaged Mac application walks through connecting an existing agent.

The project’s code is available now, but its contribution process is narrower than its licence: Telepath says its specification-driven development process is not yet open to outside contributors. It currently invites bug reports and feedback through the repository and community channel, with the browser interface still described as experimental.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Telepath identity, MIT source, server/skills/client design, Electron client, build instructions and restricted contribution process. | VERIFIED | https://github.com/telepath-computer/television | none |
| Persistent artifacts/channels, supported harnesses, Linux/macOS requirement, external-page advantage and experimental browser interface. | VENDOR-REPORTED | https://github.com/telepath-computer/television | none |
| Node.js 24 and npm >=11.5 <12; Windows agent hosts currently unsupported. | VERIFIED | https://github.com/telepath-computer/television | none |
| Persistent views give a developer a display independent of the continuing chat. | ANALYSIS | https://github.com/telepath-computer/television | none |
| Project publicly shown on dated thread. | VERIFIED | https://news.ycombinator.com/item?id=49939817 | none |
