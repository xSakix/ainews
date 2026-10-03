+++
title = "Figma Server gives agents a dedicated browser bridge"
description = "The Apache-2.0 project exposes MCP and HTTP tools through a signed-in Chromium profile, with browser-level authority and file locks."
tags = ["projects", "agents", "tools"]
date = 2026-10-03T05:40:20+02:00
draft = false
+++

Figma Server, an Apache-2.0 project from developer ctxrs, connects AI agents to Figma through a dedicated signed-in Chromium browser and local tool interfaces.

The bridge lets an agent inspect a design file, operate visible controls and take screenshots using the user’s existing Figma account. It supplies an alternative integration route for agents that can call MCP tools or a JSON HTTP API.

**Why it matters:** A designer using a custom agent can connect that agent to accessible design files through one local browser session. The account’s normal view and edit permissions still determine which files it can use.

The project installs its own Chromium browser, although configuration can select an existing Chrome or Chromium executable. The user signs in through that dedicated profile; the daemon then keeps the browser available while agents connect. Login state persists between runs until Figma requires another sign-in.

Managed operations allow one writer per file, with documented limits of 32 client sessions and eight managed tabs. That coordination has an important boundary: tools for arbitrary JavaScript and Chrome DevTools Protocol commands can bypass the managed locks and affect other agents’ tabs. Connected agents receive browser authority, and their model providers receive the tool results.

The developer frames the project as a response to restrictions on which clients may use Figma’s official MCP server. The README links the official policy and access complaints, but the project’s functionality rests on browser automation rather than on a native Figma node API.

Remote operation requires Chromium dependencies and a display reachable for the initial login. After login, the daemon can use a headless browser; documentation recommends loopback binding with an SSH tunnel for remote connections. A diagnostic command checks the installation and operating state.

The source includes reusable agent instructions and plugin configurations, while setup still requires installing the command-line tool, signing in and keeping the server running. The maintainer warns that Figma interface changes can break automation and that dispatching an input does not establish an edit was saved; the published testing guide records the qualified operations.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Apache-2.0 project and developer; dedicated Chromium profile; CLI/plugin/skill setup; HTTP and MCP interfaces. | VERIFIED | https://github.com/ctxrs/figma-server | none |
| Account permissions, persistent login, managed one-writer policy, 32 sessions/eight tabs, remote/headless requirements. | VENDOR-REPORTED | https://github.com/ctxrs/figma-server | none |
| Raw JavaScript/CDP bypasses locks; browser authority and model-provider data boundary; UI changes may break automation; input does not prove saved edits. | VERIFIED | https://github.com/ctxrs/figma-server | none |
| Developer criticizes official client restrictions; browser integration gives custom agents another access route. | OPINION | https://github.com/ctxrs/figma-server | none |
| Project publicly shown on dated thread. | VERIFIED | https://news.ycombinator.com/item?id=49938648 | none |
