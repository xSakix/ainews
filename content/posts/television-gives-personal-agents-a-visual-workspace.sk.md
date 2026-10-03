+++
title = "Television poskytuje osobným agentom vizuálny pracovný priestor"
slug = "television-poskytuje-osobnym-agentom-vizualny-pracovny-pries"
description = "Telepath zverejňuje rozhranie pod licenciou MIT pre trvalé karty, interaktívne pohľady a webové stránky popri existujúcom prostredí agenta."
tags = ["projects", "agents", "tools"]
date = 2026-10-03T05:35:20+02:00
draft = false
+++

Television, projekt firmy Telepath zameranej na rozhrania pod licenciou MIT, poskytuje osobným AI agentom trvalý vizuálny pracovný priestor popri ich existujúcom rozhovorovom rozhraní.

Agent môže vytvoriť dokument, graf alebo interaktívny pohľad, vložiť ho do kanála a neskôr upraviť. Aplikácia uchováva tieto artefakty ako objekty, ku ktorým sa človek aj agent môžu vracať, namiesto ponechania všetkých výsledkov v rozhovore.

**Prečo na tom záleží:** Vývojár používajúci agenta cez príkazový riadok môže mať zoznam úloh alebo pohľad na projekt stále pred sebou, kým rozhovor pokračuje. Television poskytuje zobrazenie a pravidlá ukladania bez potreby nového poskytovateľa modelu.

Systém má tri časti. Ľahký server beží na stroji agenta, balík opakovane použiteľných pokynov učí agenta vytvárať a meniť artefakty a klient ich zobrazuje. Klientom môže byť inštalovateľná aplikácia pre macOS alebo experimentálne rozhranie v prehliadači.

Dokumentácia Telepath vyžaduje prostredie agenta s prístupom k súborom a podporou skills, formátu opakovane použiteľných pokynov pre viaceré programovacie agenty. Samotný agent musí bežať na Linuxe alebo macOS; agenti vo Windowse zatiaľ nie sú podporovaní, hoci zobrazenie v prehliadači sa dá otvoriť aj na iných platformách.

Klient pre Mac je postavený na Electrone, frameworku pre desktopové aplikácie využívajúce webové technológie. Medzi jeho výhody oproti verzii v prehliadači patria artefakty, ktoré načítavajú externé webové stránky. Zverejnené príklady spájajú kalendáre, úlohy, tabuľky a koncepty dokumentov v kanáloch uchovávajúcich súvisiacu prácu.

Inštalácia zo zdrojového kódu vyžaduje Node.js 24 a určený rozsah verzií npm. Repozitár poskytuje príkazy na zostavenie a režim servera, ktorý pretrváva ako systémová služba, zatiaľ čo balík aplikácie pre Mac prevedie pripojením existujúceho agenta.

Kód projektu je už dostupný, ale prispievanie je užšie než jeho licencia: Telepath uvádza, že jeho vývojový proces založený na špecifikáciách zatiaľ nie je otvorený externým prispievateľom. V súčasnosti prijíma hlásenia chýb a spätnú väzbu cez repozitár a komunitný kanál; rozhranie v prehliadači naďalej označuje ako experimentálne.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Identita Telepath, kód MIT, návrh server/skills/klient, klient Electron, zostavenie a obmedzený proces prispievania. | OVERENÉ | https://github.com/telepath-computer/television | žiadne |
| Trvalé artefakty/kanály, podporované prostredia, požiadavka Linux/macOS, výhoda externých stránok a experimentálne rozhranie prehliadača. | PODĽA SPOLOČNOSTI | https://github.com/telepath-computer/television | žiadne |
| Node.js 24 a npm >=11.5 <12; Windows ako hostiteľ agenta zatiaľ nepodporovaný. | OVERENÉ | https://github.com/telepath-computer/television | žiadne |
| Trvalé pohľady poskytujú vývojárovi zobrazenie nezávislé od pokračujúceho rozhovoru. | ANALÝZA | https://github.com/telepath-computer/television | žiadne |
| Projekt bol verejne predstavený v datovanom vlákne. | OVERENÉ | https://news.ycombinator.com/item?id=49939817 | žiadne |
