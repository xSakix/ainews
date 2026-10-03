+++
title = "Portus spája brány API, modelov a nástrojov agentov"
slug = "portus-spaja-brany-api-modelov-a-nastrojov-agentov"
description = "Brána v Ruste zverejňuje smerovanie Kubernetes, rozpočty tokenov poskytovateľov a federáciu MCP spolu s benchmarkmi autorov."
tags = ["projects", "tools", "agents"]
date = 2026-10-03T05:36:20+02:00
draft = false
+++

Portus, projekt brány v Ruste, spája bežnú prevádzku API, volania jazykových modelov a pripojenia nástrojov agentov za jednu konfigurovateľnú dátovú vrstvu.

Jeho kontrolér Kubernetes kompiluje objekty smerovania a pravidiel do konfigurácie procesov brány. Tieto procesy smerujú požiadavky do aplikačných služieb, poskytovateľov modelov alebo serverov Model Context Protocol, ktoré sprístupňujú nástroje agentom.

**Prečo na tom záleží:** Platformový inžinier môže skúmať kód a pravidlá jednej brány pre aplikačnú prevádzku aj prístup k AI. Projekt dokumentuje kľúče poskytovateľov, rozpočty tokenov a zoznamy povolených nástrojov popri štandardnom smerovaní HTTP a transportných protokolov.

Portus zverejňuje priepustnosť približne 126 000 požiadaviek za sekundu z troch proxy podov na virtuálnom stroji s Linuxom a 10 vCPU na Apple M4. Autori použili tri prekladané kolá proti agentgateway, ďalšej implementácii brány, a uvádzajú nižšiu nameranú hraničnú latenciu pri pevnej záťaži. Ide o porovnania autorov na rovnakom stroji, s podmienkami a kolami testu prepojenými z projektu.

Modelová brána smeruje podľa požadovaného modelu a zároveň zachováva formát požiadavky poskytovateľa. Samostatný register vydáva hashované kľúče brány, distribuuje stav rozpočtov a eviduje tokeny. Rozpočty možno priradiť ku kľúču, používateľovi, nájomníkovi alebo trase, s rezerváciou pred volaním modelu a zúčtovaním po ňom.

Brána nástrojov môže spojiť viac serverov MCP za jeden koncový bod a pomenovať nástroje prefixom servera. Smerovanie môže používať metódu JSON-RPC a názov nástroja, pričom lokálne overované tokeny identity dodávajú skupiny a rozsahy pre pravidlá prístupu. Dokumentácia opisuje aj rozpočty volaní a zoznamy povolení pre jednotlivé kľúče.

Sieťová implementácia sa počas vývoja zmenila. Portus teraz predvolene používa Ramu po samostatnom porovnaní s Pingorou na rovnakom stroji; zverejnená hlavná tabuľka priepustnosti stále označuje skoršiu verziu Portusu. Pri čítaní údajov o výkone záleží na tejto hranici verzií.

Repozitár poskytuje zdrojový kód, príklady Kubernetes a samostatnú prevádzku z konfiguračného súboru YAML. Súčasná stránka vydania ponúka implementáciu aj benchmarkové artefakty, takže návrh smerovania možno skúmať bez povyšovania výsledkov jedného stroja na všeobecnú kapacitu.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Zverejnený kód brány Rust; návrh kontrolér/konfigurácia/dátová vrstva; režimy Kubernetes a samostatný. | OVERENÉ | https://github.com/portus-gateway/portus | žiadne |
| Portus0.2.3 126070 pož./s; tri pody, 10-vCPU Linux/Apple M4, tri prekladané kolá; p99 0,35 oproti0,82 ms pri30000 pož./s. | PODĽA SPOLOČNOSTI | https://github.com/portus-gateway/portus | žiadne |
| Smerovanie modelov, hashované kľúče, rezervácie/rozpočty/zúčtovanie, federácia MCP/identita/povolenia; Rama predvolená od0.2.4 po jednokolovom porovnaní s Pingorou. | PODĽA SPOLOČNOSTI | https://github.com/portus-gateway/portus | žiadne |
| Spoločné pravidlá umožňujú skúmať aplikačnú a AI bránu v jednej implementácii. | ANALÝZA | https://github.com/portus-gateway/portus | žiadne |
| Projekt bol verejne predstavený v datovanom vlákne. | OVERENÉ | https://news.ycombinator.com/item?id=49938517 | žiadne |
