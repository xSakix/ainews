+++
title = "Talorys Puts a Personal Agent on Cloudflare"
description = "The open-source assistant combines chat, editable memory, tasks and reminders inside one user's Cloudflare account. Its deployment is private, but not local."
tags = ["agents", "projects", "tools"]
date = 2026-10-11T04:02:06+02:00
draft = false
+++

Independent developer rociiu has released Talorys, a single-user personal agent that deploys into the user's own Cloudflare account.

The open-source project combines streaming chat with editable long-term memory, notes, tasks, projects and scheduled reminders. Its non-AI features continue working after the free Workers AI allowance is exhausted, while model-powered actions use Cloudflare's hosted GLM-4.7-Flash endpoint by default.

## Why it matters

A developer who wants a persistent personal agent usually has to choose between a vendor-hosted assistant and a local stack that must stay online. Talorys offers a third boundary: the application is controlled through the user's cloud account, with durable state and alarms managed by the platform, but inference and storage still run on Cloudflare infrastructure.

The architecture makes that boundary visible. A React interface runs on Pages. A Worker with no public URL sits behind a service binding, and a Durable Object from the Cloudflare Agents SDK owns the agent's SQLite-backed state. Durable Object alarms trigger reminders even when no browser is open.

Talorys can create and update tasks, notes and projects through conversation, while the same records remain editable through ordinary interfaces. That split is useful: the model is one way to operate the system, not the sole owner of its state.

Installation is packaged as `npx create-talorys@latest`. The repository is licensed under MIT and includes the application code and deployment path. It does not provide a security audit or evidence that the default prompts and tool permissions resist malicious content.

The project's use of “self-hosted” prompted disagreement on Hacker News. The code is deployed by the user and does not depend on the developer's service, but it runs inside Cloudflare rather than on hardware the user controls. A commenter suggested that the model endpoint could be redirected to a local server with a small change; that is community guidance, not a documented project feature.

The repository attracted roughly 400 GitHub stars within its first day and a front-page Hacker News discussion. Those signals show interest, not reliability. The concrete test is whether users can inspect and restrict every tool path, export their state and understand how Cloudflare accounts for Workers AI usage.

Talorys was created on 10 October 2026 and is available now. The maintainer labels it as a personal project rather than a production service, leaving authentication hardening, permission review and operational monitoring to anyone who deploys it.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Talorys publishes code and a one-command installer under the MIT licence | VERIFIED | https://github.com/rociiu/talorys | none |
| The project combines chat, editable memory, tasks, notes, projects and reminders | VERIFIED | https://github.com/rociiu/talorys | none |
| It uses Pages, a private Worker, a Durable Object with SQLite and Workers AI | VERIFIED | https://github.com/rociiu/talorys | none |
| Non-AI features continue when the free AI allowance is exhausted | VENDOR-REPORTED | https://github.com/rociiu/talorys | none |
| Hacker News commenters disputed whether the Cloudflare deployment counts as self-hosting | VERIFIED | https://news.ycombinator.com/item?id=50031614 | none |
