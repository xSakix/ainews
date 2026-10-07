+++
title = "OpenTPU spúšťa lokálne modely na FPGA karte za 300 dolárov"
slug = "opentpu-spusta-lokalne-modely-na-fpga-karte-za-300-dolarov"
description = "Projekt pod licenciou Apache zverejňuje návrh akcelerátora, kompilátor, simulátor a nástroje hostiteľa. Merania ukazujú malý systém obmedzený pamäťou, nie náhradu GPU."
tags = ["hardware", "projects", "models"]
date = 2026-10-07T03:58:57+02:00
draft = false
+++

OpenTPU zverejnil kompletný softvérový a hardvérový balík akcelerátora AI, ktorý spúšťa moderné jazykové modely na FPGA karte Kintex-7 za približne 300 dolárov.

Repozitár pod licenciou Apache-2.0 obsahuje hardvér v SystemVerilogu, inštrukčnú sadu, bitovo presný simulátor, jazyk jadier a kompilátor, profilovacie nástroje aj softvér hostiteľa. Jeho hodnotou je preskúmateľnosť: rovnaký malý kód siaha od jadier modelu v Pythone po signály na fyzickej karte PCIe.

## Prečo na tom záleží {#why-it-matters}

Vývojár, ktorý sa učí o inferenčnom hardvéri, môže sledovať každý cyklus a prenos pamäte bez akcelerátora z dátového centra. Výsledný stroj je oproti súčasným GPU pomalý, jeho obmedzenia však odhaľujú úzke miesto mimoriadne zreteľne.

OpenTPU uvádza 30,7 generovaného tokenu za sekundu pre štvorbitový model Qwen3-0.6B a 82,1 pre LFM2.5-230M vrátane réžie hostiteľa. Väčšie husté modely spomaľujú v uvedených konfiguráciách na 12,03 tokenu za sekundu pri Qwen3.5-2B a 3,75 pri Gemma 4 E4B.

Karta počas dekódovania dosahuje 82–94 % maxima 17,1 GB/s svojich dvoch kanálov DDR3. Obmedzením je teda šírka pásma pamäte, nie maticová aritmetika. Štvorstĺpcová systolická jednotka pomáha pri spracovaní promptu viac než pri generovaní tokenov po jednom.

Modely väčšie než 4 GiB na karte môžu streamovať váhy zmesi expertov z úložiska hostiteľa. Repozitár uvádza 10,6 tokenu za sekundu pre LFM2.5-8B-A1B a 3,95 pre Qwen3.5-35B-A3B, pričom druhý prenáša cez PCIe 153 MB na token. Ide o vlastné merania projektu, verejné sú však skripty, dátumy zostavení aj podmienky merania.

Označenie „developed by AI“ si vyžaduje opatrnosť. Podľa projektu veľkú časť návrhu a optimalizácie vytvoril agentový pracovný postup riadený človekom, čo však neukazuje autonómny systém, ktorý sa rozhodol vytvoriť si vlastný hardvér. Konkrétnym výsledkom je zverejnený balík a deklarovaná bitová zhoda medzi kartou a simulátorom.

Ďalšie testy sú priamočiare: reprodukovať zverejnené bitstreamy na rovnakej karte, porovnať spotrebu a latenciu s lacnými GPU a overiť, či externí prispievatelia dokážu meniť architektúru bez narušenia zhody so simulátorom.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
| --- | --- | --- | --- |
| OpenTPU zverejňuje hardvér, ISA, simulátor, kompilátor a nástroje hostiteľa pod Apache-2.0 | OVERENÉ | [Repozitár OpenTPU](https://github.com/FeSens/openTPU) | súbory a licencia sú dostupné |
| Qwen3-0.6B dosahuje 30,7 tokenu/s vrátane hostiteľa a LFM2.5-230M dosahuje 82,1 v štvorbitových konfiguráciách | PODĽA SPOLOČNOSTI | [Merania OpenTPU](https://github.com/FeSens/openTPU) | žiadne |
| Dekódovanie využíva 82–94 % maxima DDR3 17,1 GB/s | PODĽA SPOLOČNOSTI | [Merania OpenTPU](https://github.com/FeSens/openTPU) | žiadne |
| Qwen3.5-35B-A3B dosahuje 3,95 tokenu/s pri streamovaní 153 MB na token | PODĽA SPOLOČNOSTI | [Merania OpenTPU](https://github.com/FeSens/openTPU) | žiadne |
| Karta reprodukuje tokeny simulátora bit po bite | PODĽA SPOLOČNOSTI | [Repozitár OpenTPU](https://github.com/FeSens/openTPU) | verejné testy existujú; nezávislá hardvérová reprodukcia sa nenašla |
| „Developed by AI“ nedokazuje autonómny vývoj hardvéru | ANALÝZA | [Repozitár OpenTPU](https://github.com/FeSens/openTPU) | rozlíšenie vyplýva zo zdokumentovaného procesu riadeného človekom |
