+++
title = "Jesse Bounds builds a Vision Pro game with two agents"
description = "A dated development account describes Astra and Opus sharing planning, implementation and Blender work while headset testing remains manual."
tags = ["projects", "agents", "essays"]
date = 2026-10-03T05:38:20+02:00
draft = false
+++

Jesse Bounds, a software developer, documents building a Choplifter-inspired Apple Vision Pro game with Astra and Claude Opus 5.5 handling different parts of the work.

The prototype, called Rescue82, uses SwiftUI and RealityKit for a helicopter rescue game in an immersive headset. Bounds links the development account to a preview, showing how model-assisted code and Blender assets become a playable scene.

**Why it matters:** A developer experimenting with spatial applications gets a concrete account of agent collaboration and the testing work left on the human side. Bounds describes an implementation with controller-based flight, moving helicopter parts and passenger pickup rather than only an idea for a game.

Astra, used through Codex, handles planning, system boundaries and a second review. Opus, used through Claude Code, handles focused implementation and model revisions. Both connect to Blender through Model Context Protocol, a tool interface that lets them inspect geometry, make changes, render views and export game assets.

Bounds reports that assigning distinct roles and cross-checking work improved the prototype’s visual quality. He also records the cost of that split: handoffs create more context to carry, more review and sometimes conflicting assumptions. His approach passes a clear brief, specification files and concrete findings between the agents.

The author describes speed-ups of 100 times or more from agents, but supplies no controlled comparison of development time or token use. That assertion is a personal assessment; his more specific account concerns which tasks each agent performs and where the headset changes the development process.

Physical testing remains central to the write-up. Bounds discusses readability inside the cockpit, seeing the landing area, separating head movement from steering and reducing discomfort during turns. He says the two-dimensional simulator is useful for startup menus, while the immersive game still requires time in the headset.

The dated account describes a working prototype with six passenger seats and ground enemies. Bounds’s stated work after the minimum playable version includes mission pacing, additional levels, richer visuals and longer comfort testing. The preview is available, with those gameplay and headset refinements still ahead.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Jesse Bounds authored development account datedSeptember28; Rescue82 preview; described SwiftUI/RealityKit/BlenderMCP toolchain. | VERIFIED | https://www.bounds.dev/posts/rescue82-making-a-choplifter-style-game-for-apple-vision-pro/ | none |
| Prototype mechanics, six seats, agent role split, handoff costs and headset-test observations. | VENDOR-REPORTED | https://www.bounds.dev/posts/rescue82-making-a-choplifter-style-game-for-apple-vision-pro/ | none |
| 100x-or-more speed-up is personal assessment without controlled timing/token comparison. | OPINION | https://www.bounds.dev/posts/rescue82-making-a-choplifter-style-game-for-apple-vision-pro/ | none |
| Author plans pacing, levels, visual and comfort work. | VERIFIED | https://www.bounds.dev/posts/rescue82-making-a-choplifter-style-game-for-apple-vision-pro/ | none |
| Specific workflow gives spatial-app builders a concrete account of human and agent roles. | ANALYSIS | https://www.bounds.dev/posts/rescue82-making-a-choplifter-style-game-for-apple-vision-pro/ | none |
| Project publicly shown on dated thread. | VERIFIED | https://news.ycombinator.com/item?id=49940599 | none |
