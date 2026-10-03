+++
title = "Luong odhaľuje medzeru v kontrole duplicít agenta"
slug = "luong-odhaluje-medzeru-v-kontrole-duplicit-agenta"
description = "Malá implementácia oddeľuje presnú kontrolu URL od sémantického porovnania vyžadujúceho volanie modelu."
tags = ["essays", "agents", "projects"]
date = 2026-10-03T05:31:20+02:00
draft = false
+++

Thuan Luong, softvérový vývojár, dokumentuje, prečo jeho agent na kontrolu duplicít správ potrebuje viac než presné porovnanie URL pri opakovaných príbehoch s inými titulkami a odkazmi.

Technický článok z 2. októbra sprevádza malý server MCP a implementáciu LangGraph. Deterministická kontrola podľa neho funguje, kým samostatné sémantické porovnanie zlyhalo pre chýbajúce prihlasovacie údaje k volaniu modelu.

**Prečo na tom záleží:** Vydavateľ kontrolujúci automatizovaný prehľad potrebuje dôkaz, že porovnanie prebehlo. Luongov príbeh začal dôverou v uistenie agenta, že témy sú nové, a následným publikovaním duplicít.

Implementácia sprístupňuje úzke operácie: jedna kontroluje URL proti uloženému zoznamu; druhá vracia zoznam na širšie porovnanie. Rozdiel tak zostáva viditeľný. Presná zhoda môže rozhodnúť, či sa odkaz už objavil, ale neurčí, či iné médium píše o tej istej udalosti.

Luong potom odovzdáva záznamy a kandidáta modelu na sémantické porovnanie. Opísaný test sa dostal k volaniu, no vrátil chybu prihlasovacích údajov namiesto verdiktu o duplicite. Túto časť výslovne necháva nedokončenú namiesto nahradenia očakávaným výstupom.

Užitočné ponaučenie sa týka stavu kontroly. Tvrdený výsledok, zavolanie nástroja a úspešný výsledok nástroja sú tri odlišné veci. Ich rozlíšenie umožňuje prevádzkovateľovi zistiť, či kandidát prešiel posúdením alebo len narazil na nefunkčnú závislosť.

Pre tím tvoriaci publikačný postup toto oddelenie objasňuje aj riešenie zlyhaní. Model nedostupný na sémantickú kontrolu má vytvoriť viditeľné nevyriešené rozhodnutie, nie potichu zmeniť chýbajúce porovnanie na povolenie publikovať. Luong poskytuje príkazy pre obe ukážky a uvádza, že neskorší úspešný sémantický beh má byť zaznamenaný v repozitári.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Luong, esej z 2. októbra, projekt MCP/LangGraph a úzke rozhrania nástrojov. | OVERENÉ | https://luonghongthuan.com/en/blog/mcp-langgraph-dedup-agent-build/ | Žiadne; pripísané primárnemu zdroju. |
| Skoršie duplicity, úspech presnej kontroly a chyba prihlasovania pri sémantickej sú opísané autorom, nereprodukované. | ČIASTOČNE OVERENÉ | https://luonghongthuan.com/en/blog/mcp-langgraph-dedup-agent-build/ | Žiadne; pripísané primárnemu zdroju. |
| Zlyhané sémantické volanie má zostať nevyriešené namiesto verdiktu na publikovanie. | ANALÝZA | https://luonghongthuan.com/en/blog/mcp-langgraph-dedup-agent-build/ | Žiadne; pripísané primárnemu zdroju. |
| Príkazy ukážok a požiadavka na záznam neskoršieho úspešného behu. | OVERENÉ | https://luonghongthuan.com/en/blog/mcp-langgraph-dedup-agent-build/ | Žiadne; pripísané primárnemu zdroju. |
