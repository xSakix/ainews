+++
title = "Warm Compaction využíva cache pre pamäť agenta"
slug = "warm-compaction-vyuziva-cache-pre-pamat-agenta"
description = "Doplnok pre Hermes Agent s licenciou Apache 2.0 žiada hlavný model o zhrnutie uloženej predpony konverzácie, čím vo svojich testoch obmedzuje opakované spracovanie promptu."
tags = ["agents", "tools"]
date = 2026-10-09T04:01:06+02:00
draft = false
+++

Nový doplnok pre Hermes Agent komprimuje dlhé konverzácie tak, že hlavný model požiada o zhrnutie predpony promptu, ktorú už inferenčný server uložil do cache.

Warm Compaction znova odošle poslednú požiadavku agenta, pridá iba novšie riadky konverzácie a pokyn na odovzdanie kontextu. Model vráti štruktúrované zhrnutie v Markdowne, ktoré nahradí staršiu históriu, kým nedávna časť zostane doslovná.

**Prečo na tom záleží:** Kompresia kontextu zvyčajne vyžaduje ďalšie úplné načítanie konverzácie. Vývojárovi dlhých relácií agentov môže opätovné využitie cache predpony servera skrátiť čakanie a znížiť riziko, že menší samostatný sumarizátor vynechá dôležitý pokyn.

Doplnok používa zdokumentované rozhrania Hermes Agent a nevyžaduje úpravu hostiteľského systému. Podporuje manuálnu aj automatickú kompresiu, funguje s Pythonom 3.10 alebo novším a je vydaný pod licenciou Apache 2.0. Inštalácia pozostáva z príkazu pre doplnok Hermes a následného výberu `warm_compaction` ako kontextového enginu.

Výhoda rýchlosti závisí od rovnakého hlavného modelu a inferenčného servera, ktorý dokáže znovu použiť bloky promptu v cache. Autor uvádza hostované API s cacheovaním promptov, vLLM, SGLang, TensorRT-LLM, llama.cpp, MLX, Ollama a LM Studio ako možné cesty, no priame testovanie hlási iba na systéme NVIDIA DGX a v LM Studio. Požiadavka odoslaná napríklad do iného slotu llama.cpp môže cache minúť.

Projekt obsahuje dôkazové súbory pre desať syntetických relácií s približne 105 000 tokenmi. V týchto testoch bol medián času zhrnutia Warm Compaction 16,8 sekundy oproti 43,5 sekundy pri `hermes-lcm` a 78,5 sekundy pri vstavanom kompresore. Zachoval 59 zo 60 testovaných faktov; porovnávané riešenia zachovali 43 a 50. Ide o výsledky autora z jedného syntetického typu úlohy a tri enginy používali odlišné modely.

Návrh obsahuje spracovanie zlyhaní. Ak sa požiadavka s cache nedá vykonať alebo neprejde kontrolou výstupu, doplnok zavolá pomocnú sumarizačnú cestu Hermesu. Ak zlyhá aj tá, vytvorí zhrnutie v pevnom formáte a zachová najnovšie skoršie zhrnutie ako citovaný text. Zrušený pokus ponechá históriu bez zmeny.

Budúce verzie Hermesu môžu ponúknuť natívnu možnosť warm handoff. Doplnok kontroluje túto funkciu a môže na ňu používateľov nasmerovať, no zostáva samostatne voliteľný. Repozitár, nastavenia a dôkazy sú dostupné na [GitHube](https://github.com/Elevatormusic/hermes-warm-compaction).

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Warm Compaction znova odosiela predponu z cache a pridáva nové riadky s pokynom na odovzdanie | OVERENÉ | [Repozitár](https://github.com/Elevatormusic/hermes-warm-compaction) | žiadne |
| Doplnok používa zdokumentované API Hermesu a licenciu Apache 2.0 | OVERENÉ | [Repozitár](https://github.com/Elevatormusic/hermes-warm-compaction) | žiadne |
| Zrýchlenie vyžaduje rovnaký model a funkčnú cache predpony | OVERENÉ | [Repozitár](https://github.com/Elevatormusic/hermes-warm-compaction) | žiadne |
| Medián kompresie bol v desiatich syntetických reláciách 16,8 sekundy | PODĽA SPOLOČNOSTI | [Repozitár](https://github.com/Elevatormusic/hermes-warm-compaction) | žiadne |
| Doplnok zachoval 59 zo 60 testovaných faktov | PODĽA SPOLOČNOSTI | [Repozitár](https://github.com/Elevatormusic/hermes-warm-compaction) | žiadne |
| Neúspešné požiadavky s cache používajú pomocnú a potom pevnú zálohu | OVERENÉ | [Repozitár](https://github.com/Elevatormusic/hermes-warm-compaction) | žiadne |
