+++
title = "Figma Server poskytuje agentom samostatné prehliadačové spojenie"
slug = "figma-server-poskytuje-agentom-samostatne-prehliadacove-spoj"
description = "Projekt pod licenciou Apache-2.0 sprístupňuje nástroje MCP a HTTP cez prihlásený profil Chromium s oprávneniami prehliadača a zámkami súborov."
tags = ["projects", "agents", "tools"]
date = 2026-10-03T05:40:20+02:00
draft = false
+++

Figma Server, projekt vývojára ctxrs pod licenciou Apache-2.0, pripája AI agentov k Figme cez samostatný prihlásený prehliadač Chromium a lokálne rozhrania nástrojov.

Spojenie umožňuje agentovi skúmať návrhový súbor, ovládať viditeľné prvky a robiť snímky obrazovky pomocou existujúceho účtu Figma používateľa. Poskytuje alternatívnu cestu integrácie pre agentov, ktorí dokážu volať nástroje MCP alebo JSON HTTP API.

**Prečo na tom záleží:** Dizajnér používajúci vlastného agenta ho môže pripojiť k dostupným návrhovým súborom cez jednu lokálnu reláciu prehliadača. Bežné oprávnenia účtu na zobrazenie a úpravy naďalej určujú, ktoré súbory môže používať.

Projekt inštaluje vlastný prehliadač Chromium, hoci nastavenie môže zvoliť existujúci spustiteľný súbor Chrome alebo Chromium. Používateľ sa prihlási cez tento samostatný profil; démon potom udržiava prehliadač dostupný počas pripájania agentov. Prihlásenie pretrváva medzi spusteniami, kým Figma nevyžiada nové prihlásenie.

Riadené operácie povoľujú jedného zapisujúceho agenta na súbor, s dokumentovanými limitmi 32 klientskych relácií a ôsmich spravovaných kariet. Táto koordinácia má dôležitú hranicu: nástroje pre ľubovoľný JavaScript a príkazy Chrome DevTools Protocol môžu obísť spravované zámky a ovplyvniť karty iných agentov. Pripojení agenti získavajú oprávnenia prehliadača a ich poskytovatelia modelov dostávajú výsledky nástrojov.

Vývojár opisuje projekt ako reakciu na obmedzenia klientov, ktoré môžu používať oficiálny MCP server Figmy. README odkazuje na oficiálne pravidlá a sťažnosti na prístup, ale funkčnosť projektu stojí na automatizácii prehliadača, nie na natívnom API uzlov Figmy.

Vzdialené používanie vyžaduje závislosti Chromia a dostupné zobrazenie pre prvotné prihlásenie. Po prihlásení môže démon používať prehliadač bez grafického rozhrania; dokumentácia odporúča naviazanie na lokálnu slučku a SSH tunel pre vzdialené pripojenia. Diagnostický príkaz kontroluje inštaláciu a prevádzkový stav.

Zdrojový kód obsahuje opakovane použiteľné pokyny pre agentov a konfigurácie pluginov, no nastavenie stále vyžaduje inštaláciu nástroja pre príkazový riadok, prihlásenie a udržanie servera v chode. Správca upozorňuje, že zmeny rozhrania Figmy môžu narušiť automatizáciu a odoslanie vstupu nedokazuje uloženie úpravy; zverejnená príručka testovania uvádza overené operácie.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Projekt Apache-2.0 a vývojár; samostatný profil Chromium; nastavenie CLI/plugin/skills; rozhrania HTTP a MCP. | OVERENÉ | https://github.com/ctxrs/figma-server | žiadne |
| Oprávnenia účtu, trvalé prihlásenie, jeden zapisujúci agent, 32 relácií/osem kariet, požiadavky vzdialeného režimu a režimu bez rozhrania. | PODĽA SPOLOČNOSTI | https://github.com/ctxrs/figma-server | žiadne |
| Surový JavaScript/CDP obchádza zámky; oprávnenia prehliadača a prenos poskytovateľovi modelu; zmeny UI môžu narušiť automatizáciu; vstup nedokazuje uloženie. | OVERENÉ | https://github.com/ctxrs/figma-server | žiadne |
| Vývojár kritizuje oficiálne obmedzenia klientov; prehliadačová integrácia poskytuje vlastným agentom ďalšiu cestu prístupu. | NÁZOR | https://github.com/ctxrs/figma-server | žiadne |
| Projekt bol verejne predstavený v datovanom vlákne. | OVERENÉ | https://news.ycombinator.com/item?id=49938648 | žiadne |
