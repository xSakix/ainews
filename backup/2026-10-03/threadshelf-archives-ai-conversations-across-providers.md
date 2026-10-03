+++
title = "ThreadShelf archives AI conversations across providers"
description = "A local conversation index supports semantic search, MCP access and optional continuation with a local model or OpenRouter."
tags = ["projects", "tools", "agents"]
date = 2026-10-03T05:34:20+02:00
draft = false
+++

ThreadShelf, an MIT-licensed project by developer Chrystian Schutz, brings exported AI conversations into one local archive with semantic search and optional model-assisted continuation.

The application normalizes records from several providers so a conversation can be found by meaning as well as exact text. It presents the same index through a web interface, command-line tools, an HTTP API and Model Context Protocol, the tool-connection format used by agents.

**Why it matters:** A developer who has investigated the same problem across different assistants can search those earlier conversations without remembering which service held the answer. Search works without configuring another language model for generation.

ThreadShelf documents imports for ChatGPT, Claude, Google AI Studio, OpenRouter, LM Studio and Grok. Those sources arrive through different routes: official account exports, local application files, downloaded Drive content or a browser-side export script included in the project.

The archive pipeline runs locally, including parsing, multilingual embeddings and storage in LanceDB, a vector database. Embeddings turn passages into numerical representations that allow a search about a topic to retrieve related wording. An exact-match mode remains available for identifiers, errors and code where the spelling matters.

Continuing a thread has a separate data boundary. The default generation route uses a loopback-only llama.cpp server, an engine for local model files. Selecting the explicitly external OpenRouter option sends the chosen conversation context and new prompt to that provider, even though the archive and search remain local.

Import compatibility depends on the exporting application. The README calls several schemas undocumented and identifies LM Studio 0.4.x as a tested version; changing provider formats can therefore break parsing. The OpenRouter export script also depends on the current browser interface and has a browser test for that contract.

The code provides a React interface alongside ingestion and search commands. Its current support matrix distinguishes official exports from version-specific adapters, and the maintainer asks for anonymized samples when a newer application changes the data shape. That compatibility work is part of maintaining a useful archive across services.

## Verification

| Claim | Label | Primary source | Independent check |
|---|---|---|---|
| MIT code, developer identity, React/CLI/HTTP/MCP interfaces, documented supported import routes and compatibility matrix. | VERIFIED | https://github.com/ChrystianSchutz/ThreadShelf | none |
| Local parsing, multilingual embeddings, LanceDB search, generation-free search and loopback llama.cpp. | VENDOR-REPORTED | https://github.com/ChrystianSchutz/ThreadShelf | none |
| External OpenRouter sends selected context and prompts off-device; LM Studio 0.4.x tested; undocumented schemas and browser selectors can change. | VERIFIED | https://github.com/ChrystianSchutz/ThreadShelf | none |
| Cross-provider search helps recover prior work without remembering its service. | ANALYSIS | https://github.com/ChrystianSchutz/ThreadShelf | none |
| Project publicly shown on dated thread. | VERIFIED | https://news.ycombinator.com/item?id=49938675 | none |
