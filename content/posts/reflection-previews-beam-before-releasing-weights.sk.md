+++
title = "Reflection predstavila Beam, váhy vydá neskôr"
slug = "reflection-predstavila-beam-vahy-vyda-neskor"
description = "Model typu mixture-of-experts s 501 miliardami parametrov je dostupný len cez prednostný prístup. Reflection uvádza, že váhy, technickú správu a vývojárske nástroje vydá neskôr v októbri."
tags = ["models", "agents"]
date = 2026-10-06T04:09:31+02:00
draft = false
+++

Reflection AI oznámila Beam, model s 501 miliardami parametrov určený na programovanie a agentové úlohy, no vývojári zatiaľ nemôžu preskúmať ani spustiť jeho váhy.

Kalifornská AI spoločnosť opisuje Beam ako riedky model typu mixture-of-experts: uchováva 501 miliárd parametrov, ale pri každom tokene aktivuje 23 miliárd. Prednostný prístup vyžaduje registráciu, zatiaľ čo váhy, licencia, modelová karta, technická správa a vývojárske nástroje ešte len majú vyjsť.

Pre vývojára, ktorý si vyberá otvorený model, je tento rozdiel podstatný. Model s otvorenými váhami možno testovať na súkromných úlohách, upravovať a nasadiť bez závislosti od služby výrobcu; samotné oznámenie a tabuľka benchmarkov takéto kontroly zatiaľ neumožňujú.

Reflection uvádza, že Beam trénovala na 23,8 bilióna tokenov a následne počas štyroch týždňov vykonala viac než 100 miliónov behov posilňovacieho učenia na 10 500 GPU NVIDIA GB300. Tieto údaje opisujú nezvyčajne rozsiahle trénovanie, spoločnosť však nezverejnila technickú správu potrebnú na posúdenie zmesi dát ani nastavenia hodnotenia.

Vlastná tabuľka laboratória pripisuje modelu Beam skóre 80,9 v SWE-bench Verified a 80,1 v Terminal-Bench 2.1. Zároveň ukazuje, že Beam vo väčšine uvedených testov zaostáva za Kimi K3, GLM-5.3 a Qwen 3.8-Max. Hlavným porovnaním spoločnosti Reflection je efektivita: podľa jej vlastného odhadu operácií s pohyblivou desatinnou čiarkou dosahuje Beam výsledky porovnateľné s GLM-5.2 pri troj- až štvornásobne nižšom výpočtovom objeme inferencie.

Pre tímy, ktoré platia za dlhé agentové relácie, môže byť toto tvrdenie dôležitejšie než tesné vedenie v benchmarku. Riedka aktivácia znižuje výpočty na každý token, celý model však stále vyžaduje dostatok pamäte a infraštruktúry na uloženie a obsluhu stoviek miliárd parametrov.

Reflection uvádza, že Beam prechádza záverečným bezpečnostným testovaním. Spoločnosť plánuje vydať váhy, technickú správu, modelovú kartu a vývojárske artefakty neskôr v októbri 2026; konkrétny deň vydania neoznámila.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
| --- | --- | --- | --- |
| Reflection oznámila Beam a otvorila registráciu na prednostný prístup | OVERENÉ | [Oznámenie spoločnosti Reflection](https://reflection.ai/blog/introducing-beam) | pri konaní spoločnosti nie je potrebné |
| Beam má spolu 501 mld. parametrov a pri každom tokene aktivuje 23 mld. | PODĽA SPOLOČNOSTI | [Oznámenie spoločnosti Reflection](https://reflection.ai/blog/introducing-beam) | žiadne; váhy a správa ešte nevyšli |
| Trénovanie použilo 23,8 bilióna tokenov a viac než 100 mil. behov RL na 10 500 GPU GB300 počas štyroch týždňov | PODĽA SPOLOČNOSTI | [Oznámenie spoločnosti Reflection](https://reflection.ai/blog/introducing-beam) | žiadne |
| Beam dosiahol 80,9 v SWE-bench Verified a 80,1 v Terminal-Bench 2.1 | PODĽA SPOLOČNOSTI | [Oznámenie spoločnosti Reflection](https://reflection.ai/blog/introducing-beam) | žiadne |
| Reflection odhaduje porovnateľné výsledky s GLM-5.2 pri 3–4× nižšom výpočtovom objeme inferencie | PODĽA SPOLOČNOSTI | [Oznámenie spoločnosti Reflection](https://reflection.ai/blog/introducing-beam) | žiadne |
| Váhy, správa, modelová karta a vývojárske artefakty sú prisľúbené na neskôr v októbri 2026 | OVERENÉ | [Oznámenie spoločnosti Reflection](https://reflection.ai/blog/introducing-beam) | pri oznámenom harmonograme nie je potrebné |
