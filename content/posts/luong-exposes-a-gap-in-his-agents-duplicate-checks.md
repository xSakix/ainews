+++
title = "Luong exposes a gap in his agent’s duplicate checks"
description = "A small implementation separates deterministic URL checks from semantic comparisons that require a model call."
tags = ["essays", "agents", "projects"]
date = 2026-10-03T05:31:20+02:00
draft = false
+++

Thuan Luong, a software practitioner, documents why his news-deduplication agent needs more than exact URL matching to catch repeated stories published under different headlines and links.

His October 2 engineering post accompanies a small MCP server and LangGraph implementation. The deterministic check works, he reports, while a separate semantic comparison failed because the environment lacked credentials for its model call.

**Why it matters:** A publisher checking an automated digest needs evidence that the comparison ran. Luong's account began after trusting an agent's assurance that candidate stories were new and publishing duplicates instead.

The implementation exposes narrow operations: one checks a URL against a stored list; another returns the list for broader comparison. That makes the difference visible. An exact match can settle whether the same link appeared before, but it cannot settle whether another outlet is covering the same event.

Luong then passes the stored records and candidate to a model for semantic comparison. His reported test reached the call but returned a credential error, rather than a duplicate verdict. He explicitly leaves that part unfinished instead of substituting the output he expected to receive.

The useful lesson is about the status of a check. A claimed result, a tool invocation and a successful tool result are three different things. Keeping them distinct lets an operator see whether a candidate passed review or merely encountered a broken dependency.

For a team building a publication pipeline, that separation also clarifies failure handling. A model unavailable for semantic review should produce a visible unresolved decision, not silently turn a missing comparison into permission to publish. Luong provides commands for both demonstrations and says a later passing semantic run should be recorded in the repository.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| Luong, October 2 essay, MCP/LangGraph project and narrow tool interfaces. | VERIFIED | https://luonghongthuan.com/en/blog/mcp-langgraph-dedup-agent-build/ | None; attributed primary account. |
| Earlier duplicates, exact check success and semantic credential failure are author-reported, not reproduced. | PARTIALLY VERIFIED | https://luonghongthuan.com/en/blog/mcp-langgraph-dedup-agent-build/ | None; attributed primary account. |
| A failed semantic call must remain unresolved rather than become a publication verdict. | ANALYSIS | https://luonghongthuan.com/en/blog/mcp-langgraph-dedup-agent-build/ | None; attributed primary account. |
| Demo commands and expectation of a documented later passing run. | VERIFIED | https://luonghongthuan.com/en/blog/mcp-langgraph-dedup-agent-build/ | None; attributed primary account. |
