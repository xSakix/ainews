+++
title = "Agent Scrub odstraňuje tajomstvá z histórie agentov"
slug = "agent-scrub-odstranuje-tajomstva-z-historie-agentov"
description = "Lokálna aplikácia pre macOS hľadá kópie prihlasovacích údajov v uložených rozhovoroch a môže ich odstrániť bez zmeny aktívnych prihlasovacích súborov."
tags = ["projects", "tools", "safety"]
date = 2026-10-03T05:55:20+02:00
draft = false
+++

Agent Scrub, nástroj pre macOS od vývojára thesubtlety, vyhľadáva a odstraňuje tajné hodnoty, ktoré zostali v histórii rozhovorov AI nástrojov na programovanie.

Programovací asistenti uchovávajú viac než konečnú odpoveď: prompty, výstupy terminálu a uložená pamäť môžu na disku zanechať ďalšie kópie prihlasovacích údajov. Agent Scrub rieši čistenie týchto záznamov oddelene od údajov, ktoré aplikácia aktívne používa na prihlásenie.

**Prečo na tom záleží:** Vývojár, ktorý vložil token do rozhovoru pri ladení, môže vyhľadať jeho opakované výskyty v histórii agentov a odstrániť lokálne kópie cez jedno rozhranie. Aplikácia zoskupuje nálezy podľa tajnej hodnoty, projektu a aplikácie.

Repozitár dokumentuje podporu nástrojov Claude Code, Codex, Gemini CLI, Cursor a viacerých ďalších. Aplikácia v lište ponuky prehľadáva záznamy pri spustení a sleduje zmeny v podporovaných umiestneniach histórie; prehľad pokrytia uvádza súbory, ktoré nedokázala prečítať, a výnimky umožňujú vynechať konkrétne priečinky.

Odstránenie nahrádza nájdené hodnoty značkami priamo v pôvodných súboroch. Nástroj pred zápisom aj po ňom opätovne kontroluje a parsuje súbory a dočasne preskakuje záznamy, do ktorých agent ešte zapisuje. README upozorňuje, že tieto zmeny sa nedajú automaticky vrátiť a neodstránia kópie už odoslané poskytovateľovi alebo zachované v zálohách.

Agent Scrub zámerne ponecháva aktívne autentifikačné a konfiguračné súbory bez zásahu. Na vytváranie odtlačkov nálezov používa vlastný kľúč pre konkrétnu inštaláciu, uložený v macOS Keychain, takže databáza nemusí uchovávať odhalené hodnoty v otvorenom texte. Vývojár uvádza, že prehľadávanie, stav aj úpravy zostávajú lokálne a aplikácia nevytvára sieťové spojenia.

Súčasná aplikácia vyžaduje macOS 14 alebo novší a podporuje Macy s Apple Silicon aj Intelom. Zostavenie zo zdrojového kódu vyžaduje Xcode 16 a Swift 6; distribuované zostavenia zatiaľ nie sú podpísané, čo ovplyvňuje postup inštalácie. Doplnkový nástroj pre príkazový riadok ponúka prehľadávanie a správu pravidiel, pričom zápis iba simuluje, kým ho používateľ výslovne nepotvrdí.

Projekt už sprístupňuje kód aplikácie aj príkazového riadka. Prehľad pokrytia a trvalý zápis vymedzujú hranice prvého vydania: nájdenie tajnej hodnoty je vratná kontrola; odstránenie jej zostávajúcich kópií z histórie mení samotné záznamy.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Zverejnený kód; macOS 14+, Intel/Apple Silicon; zostavenie cez Xcode 16/Swift 6; nepodpísaná distribúcia. | OVERENÉ | https://github.com/thesubtlety/agent-scrub | žiadne |
| Podporované nástroje, skenovanie, zoskupovanie, výnimky, pokrytie, odtlačky a lokálne spracovanie sú dokumentované schopnosti. | PODĽA SPOLOČNOSTI | https://github.com/thesubtlety/agent-scrub | žiadne |
| Odstránenie trvalo mení súbory histórie; aktívne prihlasovacie údaje sa vynechávajú; aktívny zápis sa preskakuje; vzdialené a zálohované kópie zostávajú. | OVERENÉ | https://github.com/thesubtlety/agent-scrub | žiadne |
| Zoskupené čistenie histórie pomáha vývojárovi nájsť opakované kópie tokenu. | ANALÝZA | https://github.com/thesubtlety/agent-scrub | žiadne |
| Projekt bol verejne predstavený v datovanom vlákne. | OVERENÉ | https://news.ycombinator.com/item?id=49939584 | žiadne |
