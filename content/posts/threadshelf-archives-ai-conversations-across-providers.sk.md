+++
title = "ThreadShelf archivuje AI rozhovory od rôznych poskytovateľov"
slug = "threadshelf-archivuje-ai-rozhovory-od-roznych-poskytovatelov"
description = "Lokálny index rozhovorov podporuje sémantické vyhľadávanie, prístup cez MCP a voliteľné pokračovanie s lokálnym modelom alebo OpenRouterom."
tags = ["projects", "tools", "agents"]
date = 2026-10-03T05:34:20+02:00
draft = false
+++

ThreadShelf, projekt vývojára Chrystiana Schutza pod licenciou MIT, spája exportované AI rozhovory do jedného lokálneho archívu so sémantickým vyhľadávaním a voliteľným pokračovaním pomocou modelu.

Aplikácia zjednocuje záznamy od viacerých poskytovateľov, takže rozhovor možno nájsť podľa významu aj presného textu. Rovnaký index sprístupňuje cez webové rozhranie, príkazový riadok, HTTP API a Model Context Protocol, formát pripojenia nástrojov používaný agentmi.

**Prečo na tom záleží:** Vývojár, ktorý skúmal rovnaký problém s rôznymi asistentmi, môže prehľadať skoršie rozhovory bez toho, aby si pamätal, v ktorej službe bola odpoveď. Vyhľadávanie funguje bez nastavenia ďalšieho jazykového modelu na generovanie.

ThreadShelf dokumentuje importy z ChatGPT, Claude, Google AI Studio, OpenRouter, LM Studio a Grok. Tieto zdroje prichádzajú rôznymi cestami: cez oficiálne exporty účtu, lokálne súbory aplikácií, stiahnutý obsah z Drivu alebo skript na export v prehliadači pribalený k projektu.

Archivačný postup beží lokálne vrátane parsovania, viacjazyčných embeddingov a ukladania do LanceDB, vektorovej databázy. Embeddingy menia pasáže na číselné reprezentácie, vďaka ktorým vyhľadávanie podľa témy nájde súvisiace formulácie. Pre identifikátory, chyby a kód, kde záleží na presnom zápise, zostáva dostupný režim presnej zhody.

Pokračovanie rozhovoru má samostatnú hranicu prenosu údajov. Predvolená cesta generovania používa server llama.cpp dostupný iba cez lokálnu slučku, engine pre lokálne súbory modelov. Výber výslovne externého OpenRoutera odošle zvolený kontext rozhovoru a nový prompt tomuto poskytovateľovi, hoci archív aj vyhľadávanie zostávajú lokálne.

Kompatibilita importu závisí od aplikácie, ktorá export vytvorila. README označuje viaceré schémy za nedokumentované a uvádza LM Studio 0.4.x ako testovanú verziu; zmena formátov poskytovateľov preto môže pokaziť parsovanie. Exportný skript pre OpenRouter tiež závisí od aktuálneho rozhrania prehliadača a má pre tento predpoklad prehliadačový test.

Kód poskytuje rozhranie v Reacte popri príkazoch na načítanie a vyhľadávanie. Súčasná tabuľka podpory odlišuje oficiálne exporty od adaptérov pre konkrétne verzie a správca žiada anonymizované vzorky, keď novšia aplikácia zmení štruktúru údajov. Táto práca na kompatibilite patrí k udržiavaniu užitočného archívu naprieč službami.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Kód MIT, identita vývojára, rozhrania React/CLI/HTTP/MCP, dokumentované importy a tabuľka kompatibility. | OVERENÉ | https://github.com/ChrystianSchutz/ThreadShelf | žiadne |
| Lokálne parsovanie, viacjazyčné embeddingy, vyhľadávanie LanceDB, vyhľadávanie bez generovania a lokálny llama.cpp. | PODĽA SPOLOČNOSTI | https://github.com/ChrystianSchutz/ThreadShelf | žiadne |
| Externý OpenRouter odosiela vybraný kontext a prompty mimo zariadenia; testované LM Studio 0.4.x; nedokumentované schémy a selektory prehliadača sa môžu meniť. | OVERENÉ | https://github.com/ChrystianSchutz/ThreadShelf | žiadne |
| Vyhľadávanie naprieč poskytovateľmi pomáha obnoviť skoršiu prácu bez zapamätania služby. | ANALÝZA | https://github.com/ChrystianSchutz/ThreadShelf | žiadne |
| Projekt bol verejne predstavený v datovanom vlákne. | OVERENÉ | https://news.ycombinator.com/item?id=49938675 | žiadne |
