+++
title = "Anthropic uvádza Claude Haiku 5.5"
slug = "anthropic-uvadza-claude-haiku-5-5"
description = "Malý model Claude pridáva adaptívne uvažovanie a dvojúrovňové ceny tokenov. Anthropic ho určuje na súhrny, prácu v prehliadači a úzko zameraných subagentov."
tags = ["models", "agents"]
date = 2026-10-08T03:59:31+02:00
draft = false
+++

Spoločnosť Anthropic vydala 7. októbra model Claude Haiku 5.5, ktorý znižuje efektívnu cenu jej malého modelu a pridáva kontextové okno s jedným miliónom tokenov aj nastaviteľnú úroveň uvažovania.

Model pre API je určený na časté a úzko vymedzené úlohy, ako sú klasifikácia, sumarizácia, databázové dotazy a práca subagentov. Je dostupný cez Anthropic a hlavné cloudové platformy pod identifikátorom `claude-haiku-5-5`.

Pre vývojárov, ktorí platia za úlohu, je bezprostredným dôsledkom zmena ceny. Prompty do 100 000 tokenov stoja 0,10 dolára za milión vstupných tokenov a 0,50 dolára za milión výstupných tokenov. Dlhšie prompty stoja 0,50 a 2,50 dolára. Anthropic uvádza, že priemerné náklady sú po zohľadnení mierne odlišného tokenizéra nového modelu približne o 75 % nižšie než pri Haiku 4.5.

Haiku 5.5 je prvý model triedy Haiku s adaptívnym uvažovaním a ovládaním úsilia. Vzniká tým aj problém pri migrácii: požiadavky so starším manuálnym nastavením `budget_tokens` vrátia chybu HTTP 400. Aplikácie prechádzajúce z Haiku 4.5 musia toto nastavenie odstrániť a znova otestovať spotrebu tokenov aj kvalitu výstupu.

Vlastné hodnotenia spoločnosti Anthropic dávajú modelu Haiku 5.5 skóre 72,4 % v offline časti benchmarku používania počítača oproti 15,7 % pre Haiku 4.5. Porovnanie vykonal dodávateľ a Anthropic naďalej odporúča na komplexné programovanie model Sonnet 5.5 alebo Opus 5.5. Úlohou Haiku má byť lacnejší podporný model, ktorý vykonáva krátke a opakované operácie okolo väčšieho modelu.

Vydanie zároveň znižuje cenu čítania z vyrovnávacej pamäte Sonnet 5.5 na polovicu, teda na 0,10 dolára za milión tokenov. Anthropic uvádza, že čítanie z vyrovnávacej pamäte tvorí dostatočne veľkú časť agentovej prevádzky na to, aby táto zmena znížila náklady väčšiny agentových úloh so Sonnet 5.5 približne o 20 %.

Predplatitelia programov Max a Team majú počas týždňa vydania dostať mesačné kredity pre API. Súpravy SDK spoločnosti Anthropic pre Python a TypeScript zároveň dostávajú beta triedy na používanie prehliadača a počítača, teda na dve úlohy citlivé na rýchlosť, ktoré firma pri Haiku 5.5 zdôrazňuje.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Anthropic vydal Claude Haiku 5.5 7. októbra 2026 s adaptívnym uvažovaním, kontextovým oknom 1 milión tokenov a maximálnym výstupom 128 000 tokenov | OVERENÉ | [Oznámenie spoločnosti Anthropic](https://www.anthropic.com/claude-haiku-5-5) | žiadne |
| Prompty do 100 000 tokenov stoja 0,10 dolára za vstup a 0,50 dolára za výstup na milión tokenov; dlhšie prompty stoja 0,50 a 2,50 dolára | OVERENÉ | [Oznámenie spoločnosti Anthropic](https://www.anthropic.com/claude-haiku-5-5) | žiadne |
| Anthropic uvádza priemerné náklady približne o 75 % nižšie než pri Haiku 4.5 | PODĽA SPOLOČNOSTI | [Oznámenie spoločnosti Anthropic](https://www.anthropic.com/claude-haiku-5-5) | žiadne |
| Anthropic uvádza 72,4 % v offline časti OSWorld 2.1 oproti 15,7 % pre Haiku 4.5 | PODĽA SPOLOČNOSTI | [Oznámenie spoločnosti Anthropic](https://www.anthropic.com/claude-haiku-5-5) | žiadne |
| Manuálne požiadavky `budget_tokens` vrátia počas migrácie chybu HTTP 400 | OVERENÉ | [Poznámky k vydaniam Claude](https://platform.claude.com/docs/en/release-notes/overview) | žiadne |
| Čítanie z vyrovnávacej pamäte Sonnet 5.5 teraz stojí 0,10 dolára za milión tokenov a Anthropic odhaduje približne o 20 % nižšie náklady agentových úloh | PODĽA SPOLOČNOSTI | [Oznámenie spoločnosti Anthropic](https://www.anthropic.com/claude-haiku-5-5) | žiadne |
