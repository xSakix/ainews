+++
title = "Reka vydáva modely pohybu kamery trénované na hrách"
slug = "reka-vydava-modely-pohybu-kamery-trenovane-na-hrach"
description = "Dva malé modely inverznej dynamiky odhadujú ovládanie pohybu z videa. Reka poskytuje váhy, skripty a príklady zlyhaní na reálnom videu."
tags = ["models", "research", "tools"]
date = 2026-10-03T05:56:20+02:00
draft = false
+++

Reka, vývojár AI modelov, vydala dva malé modely, ktoré z videa odhadujú ovládanie pohybu kamery. Pomocou tréningových označení vytvorených hrou skúma prenos tejto schopnosti na reálne zábery.

[Repozitár modelov](https://huggingface.co/RekaAI/Reka-Inverse-Dynamics-Model), vytvorený 1. októbra, obsahuje model čítajúci optický tok, teda pohyb medzi snímkami, a druhý model čítajúci samotné snímky. Oba odhadujú klávesy pohybu a otáčanie kamery namiesto slovného opisu scény.

**Prečo na tom záleží:** Vývojár skúmajúci interaktívne modely videa dostáva stiahnuteľné váhy a inferenčné skripty na odvodenie akcií zo zaznamenaného pohybu. Reka poskytuje aj konkrétny príklad zlyhania, ktorý zviditeľňuje hranicu medzi pohybom kamery a skutočným pohybom.

Reka uvádza, že model optického toku správne určil smer otáčania približne v 92 % zo 47 reálnych videoklipov s otáčaním, oproti približne 51 % pri modeli so surovými snímkami. Model optického toku obsahuje približne 2,8 milióna parametrov vrátane zmrazeného nástroja na získavanie pohybu; model so surovými snímkami má približne 9,8 milióna. Porovnanie na týchto klipoch vychádza lepšie pre menší model, pochádza však z vlastného predbežného hodnotenia spoločnosti Reka.

Tréningové označenia pochádzali zo 4 071 zaznamenaných hraní hier. Herný engine poskytol klávesy, pohyby myši a uhly kamery, čím sa obišlo ručné označovanie. Podľa karty boli oba modely trénované na jednej NVIDIA L4 GPU. Model optického toku vytvára jednu predikciu na okno so 17 snímkami; model so surovými snímkami predikuje pri každej snímke.

Vydanie obsahuje samostatné nastavenia pre herné zábery a videá chôdze, ukážkový klip a očakávaný výstup JSON pre základný test funkčnosti. Video zlyhania ukazuje nehybnú kameru, ktorá sa otáča: model optického toku opakovane priraďuje vysokú pravdepodobnosť klávesu chôdze. Samotné pohybové signály tak môžu viesť tento model k zámene otáčania stojacej kamery s pohybom.

Kód a váhy modelov používajú Apache 2.0. Zmrazená súčasť na optický tok používa samostatne licencované váhy BSD-3, zatiaľ čo príklady videí chôdze si zachovávajú licenciu CC BY 3.0. Reka označuje vydanie za predbežné; repozitár poskytuje oba priečinky modelov, verzie závislostí a klip zlyhania na ďalšie skúmanie.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Reka zverejnila dva modely pohybu kamery s váhami, kódom, ukážkovými výstupmi a videami zlyhaní; repozitár bol vytvorený 1. októbra. | OVERENÉ | [Repozitár a karta modelu](https://huggingface.co/RekaAI/Reka-Inverse-Dynamics-Model) | žiadne |
| Presnosť modelu optického toku pri otáčaní je 91,5 % na 47 reálnych klipoch s otáčaním; presnosť modelu so surovými snímkami je 51,1 %. | PODĽA SPOLOČNOSTI | [Výsledky karty modelu](https://huggingface.co/RekaAI/Reka-Inverse-Dynamics-Model) | žiadne |
| Model optického toku má 1 795 337 trénovaných a 990 162 zmrazených parametrov (spolu 2 785 499); model so surovými snímkami má 9 836 063. Tréning použil 4 071 hraní hier a jednu L4 GPU. | PODĽA SPOLOČNOSTI | [Architektúra a tréningové dáta](https://huggingface.co/RekaAI/Reka-Inverse-Dynamics-Model) | žiadne |
| Model optického toku predikuje na okno so 17 snímkami, model so surovými snímkami na každú snímku; konfigurácia, ukážka JSON a základný test sú dostupné. | OVERENÉ | [Súbory vydania](https://huggingface.co/RekaAI/Reka-Inverse-Dynamics-Model) | žiadne |
| Klip zlyhania priraďuje pravdepodobnosti klávesu chôdze 0,72–0,98 otáčaniu stojacej kamery, čo ilustruje zámenu pohybu. | PODĽA SPOLOČNOSTI | [Zdokumentované zlyhanie](https://huggingface.co/RekaAI/Reka-Inverse-Dynamics-Model) | žiadne |
| Kód a váhy používajú Apache 2.0; váhy RAFT-small používajú BSD-3 a príklady CC BY 3.0. Vydanie je predbežné. | OVERENÉ | [Licencia a stav](https://huggingface.co/RekaAI/Reka-Inverse-Dynamics-Model) | žiadne |
| Skúmateľné váhy a príklady zlyhaní poskytujú vývojárom interaktívneho videa východisko na odvodenie akcií. | ANALÝZA | [Artefakty vydania](https://huggingface.co/RekaAI/Reka-Inverse-Dynamics-Model) | žiadne |
