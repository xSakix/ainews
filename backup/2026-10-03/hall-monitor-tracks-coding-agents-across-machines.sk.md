+++
title = "Hall Monitor sleduje programovacích agentov na viacerých strojoch"
slug = "hall-monitor-sleduje-programovacich-agentov-na-viacerych-str"
description = "Prehľad iba na čítanie spája relácie Claude Code a Codex, lokálne záznamy používania a vzdialené stroje dostupné cez SSH."
tags = ["projects", "agents", "tools"]
date = 2026-10-03T05:39:20+02:00
draft = false
+++

Hall Monitor, projekt Hitesha Bandhua pod licenciou MIT, prenáša stav relácií Claude Code a Codex do terminálového prehľadu a natívneho rozhrania pre macOS.

Nástroj číta záznamy, ktoré programovací agenti už vytvárajú, a zoskupuje relácie podľa toho, či pracujú, sú nečinné alebo čakajú na človeka. Vzdialené relácie sa pripájajú do rovnakého prehľadu cez vlastné SSH spojenia prevádzkovateľa.

**Prečo na tom záleží:** Vývojár s agentmi na notebooku a GPU serveri vidí, ktorá relácia potrebuje pozornosť, bez opätovného otvárania každého terminálu. Hall Monitor popri stave zobrazuje aktuálnu operáciu, projekt, model a nedávnu aktivitu.

Terminálový prehľad funguje na macOS a Linuxe. Aplikácia pre Mac pridáva lištu ponuky, upozornenia a zobrazenie pri výreze displeja MacBooku, s odkazmi späť na príslušnú aplikáciu alebo terminál. Projekt sa predtým volal agentboard; dokumentácia uvádza, že aktualizácia zachová pôvodný príkaz aj históriu používania.

Stav Claude Code pochádza z metadát relácie a záznamov rozhovoru. Stav Codexu pochádza z bežiacich procesov a logov relácií, pričom jeho app-server sa používa, keď je dostupný. Projekt opisuje rozhranie ako určené iba na čítanie: neodosiela prompty ani neschvaľuje navrhované akcie agenta.

Evidencia používania uchováva užší rozsah údajov než živé zobrazenie. Lokálny register ukladá počty pre čas agentov, tokeny, projekty a využitie vyrovnávacej pamäte, nie text promptov. Vzdialené stroje posielajú metadáta relácií cez jedno SSH spojenie na stroj a po jeho prerušení sa znova pripájajú.

Limity programov sa zisťujú rôznymi cestami. Limity Codexu pochádzajú z jeho logov; limity Claude možno čítať otvorením vlastného prehľadu používania Claude Code v samostatnej relácii v bezpečnom režime každých 15 minút. README poskytuje prepínač na vypnutie tohto zisťovania a označuje údaje staršie než 15 minút ako neaktuálne.

Bandhu zverejňuje zdrojový kód, binárne súbory aj inštalačné postupy cez Homebrew. Natívna aplikácia vyžaduje macOS 14 alebo novší a zostavenie terminálového nástroja zo zdrojového kódu Go 1.26 alebo novší. Režim iba na čítanie ponecháva riadenie vykonávania v pôvodnom rozhraní agenta; úlohou prehľadu je ukázať, kde treba pozornosť človeka.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Kód MIT; autor; terminál macOS/Linux; natívny macOS 14+; Go 1.26+; premenovanie agentboard. | OVERENÉ | https://github.com/hiteshbandhu/hallmonitor | žiadne |
| Zber stavu, natívne zobrazenia, navigácia, SSH streamovanie, opätovné pripojenie a ovládanie iba na čítanie. | PODĽA SPOLOČNOSTI | https://github.com/hiteshbandhu/hallmonitor | žiadne |
| Register iba s počtami; limity z logov Codexu; voliteľné zisťovanie Claude v bezpečnom režime každých 15 minút; označenie neaktuálnosti. | PODĽA SPOLOČNOSTI | https://github.com/hiteshbandhu/hallmonitor | žiadne |
| Spoločný prehľad znižuje potrebu kontrolovať každý terminál pre čakajúcich agentov. | ANALÝZA | https://github.com/hiteshbandhu/hallmonitor | žiadne |
| Projekt bol verejne predstavený v datovanom vlákne. | OVERENÉ | https://news.ycombinator.com/item?id=49941003 | žiadne |
