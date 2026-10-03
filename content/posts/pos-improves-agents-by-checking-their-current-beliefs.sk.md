+++
title = "PoS zlepšuje agentov kontrolou ich aktuálnych predpokladov"
slug = "pos-zlepsuje-agentov-kontrolou-ich-aktualnych-predpokladov"
description = "Systém sleduje, čo agent predpokladá, čo ešte nevie a či jeho kroky prinášajú pokrok. Prínosy v benchmarkoch vychádzajú z údržby tohto stavu, nie z dlhšej histórie."
tags = ["research", "agents"]
date = 2026-10-03T05:49:20+02:00
draft = false
+++

PoS, systém od Nankai University, Alibaba Group a Tsinghua University, zlepšuje dlho bežiacich agentov tým, že udržiava a kontroluje výslovný opis aktuálneho sveta namiesto spoliehania sa na nahromadenú históriu konverzácie.

Yu Luo a kolegovia usporadúvajú tento opis podľa toho, čo agent vie, čo ešte potrebuje zistiť a čo ešte musí vykonať. Navrhnuté aktualizácie porovnávajú s dôkazmi a agenta presmerujú, keď jeho aktivita prestane prinášať pokrok.

**Prečo na tom záleží:** Vývojár skúmajúci zaseknutého agenta môže preskúmať pracovné predpoklady, ktoré určujú jeho ďalší krok. PoS z nich vytvára upraviteľný záznam, vďaka čomu systém môže opraviť chybný stav alebo zastaviť opakovanie neproduktívneho skúmania.

[Preprint](https://arxiv.org/abs/2610.01415), prvýkrát predložený 1. októbra, uvádza najlepší celkový výkon spomedzi porovnávaných metód v štyroch benchmarkoch s každým z troch základných jazykových modelov. Porovnania zahŕňajú vykonávanie cieľových úloh a diagnózu založenú na hľadaní dôkazov, pri ktorých je pamätanie minulého pozorovania odlišné od poznania aktuálneho stavu.

História zaznamenáva postupnosť krokov a pozorovaní. Záznam aktuálneho stavu túto postupnosť zosúlaďuje: predmet sa mohol presunúť, staršia hypotéza mohla byť vylúčená alebo požiadavka už splnená. Aj pri dlhšej histórii musí agent tieto vzťahy znovu rekonštruovať pri každom rozhodnutí.

PoS udržiava entity, ich stavy a vzťahy spolu s nedokončenými požiadavkami. Odlišuje chýbajúcu informáciu od nevykonaného kroku. Toto rozlíšenie je dôležité, pretože diagnóza vyžaduje pozorovanie rozlišujúce možnosti, kým vykonávacia úloha môže potrebovať konkrétnu zmenu prostredia.

Systém pripomína priebežne aktualizovanú tabuľu prípadu, nie škatuľu prepisov rozhovorov. Nové dôkazy aktualizujú tabuľu, nevyriešené otázky zostávajú viditeľné a nezlučiteľné položky možno spochybniť. Interpretáciu naďalej poskytuje základný jazykový model, takže obsah tabule vyžaduje kontrolu.

Po každom kroku agent úlohy navrhne aktualizáciu. Kontrolná súčasť preskúma nové či zmenené položky a hľadá rozpory v zázname aj oproti dostupným pozorovaniam. Agent potom návrh upraví pred uložením nového stavu. Predpoklad tak možno odmietnuť, aj keď sám osebe znie presvedčivo.

## Obnova odlišuje neistotu od nedokončenej práce

PoS zároveň vyberá aktívnu nevyriešenú požiadavku na riadenie ďalšieho kroku a zachováva širší kontext úlohy. Sleduje, či požiadavky pretrvávajú, či nedávne kroky prinášajú pokrok a či sa opakuje rovnaký relevantný stav sveta.

Tieto signály identifikujú uviaznutú aktivitu, ktorú štúdia nazýva uviaznutím v predpokladoch. Obnova závisí od vzorca stagnácie aj druhu nevyriešenej požiadavky. Agent krúžiaci okolo diagnostickej neistoty potrebuje dôkaz rozlišujúci vysvetlenia; opakovanie neúčinnej operácie vyžaduje zmenu vykonávania.

Opísaný príklad diagnostiky incidentu tento rozdiel ilustruje. Agent nevedel rozlíšiť, či pomalé požiadavky inventárnej služby spôsobuje čakanie na databázu alebo spracovanie vo virtuálnom stroji Java. Po odhalení stagnácie ho PoS nasmeroval na rozlišujúce dôkazy; pozorovania CPU spolu so staršími dôkazmi o čistení pamäte podporili upravenú diagnózu.

Experimenty používajú Qwen3.7-Plus, Kimi-K3 a GLM-5.3 konzistentne v modelových súčastiach každého systému. Základné porovnania zahŕňajú úplnú surovú históriu, komprimovanú pamäť, hierarchickú pamäť a iný systém výslovne udržiavaného stavu úlohy. PoS viedol vo všetkých dvanástich kombináciách benchmarku a modelu v hlavnej tabuľke autorov.

Odstránenie kontroly aktualizácií alebo obnovy pri stagnácii znížilo výkon. Účinky sa líšili medzi vykonávaním a diagnostikou, čo podporuje tvrdenie autorov, že súčasti riešia odlišné zlyhania. Alternatívy založené na kompresii niekedy dosiahli horšie skóre než surová história, takže usporiadanie kontextu môže informácie strácať aj obmedzovať opakovanie.

Zlepšenie má cenu: údržba a kontrola stavu pridávajú prácu a autori uznávajú závislosť od znalostí úlohy aj odboru. Správny kontext nedodá chýbajúcu operačnú zručnosť či medicínske porozumenie. Klinický benchmark hodnotí diagnostiku agenta, nie klinické nasadenie.

Výsledky sú vlastnými meraniami autorov a rukopis je preprint. Tím poskytuje [kód](https://github.com/luoyu100/PoS) a [opis projektu](https://luoyu100.github.io/projects/progression-of-states/project/). Jeho vlastná analýza zlyhaní ponecháva konkrétnu hranicu: niektorí agenti získali správne dôkazy a napriek tomu ich nesprávne vyložili, pretože nemali znalosti potrebné na konanie podľa nich.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Afiliácie Lua a spoluautorov Nankai/Alibaba/Tsinghua; v1 predložená 1. októbra 2026. | OVERENÉ | https://arxiv.org/abs/2610.01415 | žiadne |
| Najlepší výkon hlavnej tabuľky v štyroch benchmarkoch a Qwen3.7-Plus, Kimi-K3, GLM-5.3; dvanásť kombinácií. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2610.01415 | žiadne |
| Výslovné entity/stavy/vzťahy, informačné/akčné medzery, kontrolované aktualizácie, aktívna medzera a obnova pri stagnácii/opakovaní opisujú metódu. | OVERENÉ | https://arxiv.org/abs/2610.01415 | žiadne |
| Opísaný príklad inventárnej služby využíva dôkazy CPU/čistenia pamäte na rozlíšenie spracovania JVM od čakania na databázu. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2610.01415 | žiadne |
| Typy porovnávaných metód, rovnaké modely, účinky odstránenia súčastí a občasná výhoda surovej histórie. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2610.01415 | žiadne |
| Náklady údržby, závislosť od odborných znalostí a zlyhania klinickej interpretácie sú uvedené obmedzenia. | OVERENÉ | https://arxiv.org/abs/2610.01415 | žiadne |
| Poskytnuté stránky kódu a projektu. | OVERENÉ | https://github.com/luoyu100/PoS ; https://luoyu100.github.io/projects/progression-of-states/project/ | žiadne |
| Dôsledok pre vývojára a prirovnanie k tabuli prípadu vysvetľujú kontrolovateľné aktuálne predpoklady. | ANALÝZA | https://arxiv.org/abs/2610.01415 | žiadne |
