+++
title = "Aleph Alpha vydáva Kolibri s otvorenými váhami"
slug = "aleph-alpha-vydava-kolibri-s-otvorenymi-vahami"
description = "Model na uvažovanie v nemčine a angličtine prináša váhy pod licenciou Apache 2.0 a návod na nasadenie. Malý počet aktívnych parametrov stále znamená veľké pamäťové nároky."
tags = ["models", "tools"]
date = 2026-10-04T09:27:37+02:00
draft = false
+++

Aleph Alpha, nemecký vývojár AI, vydal 3. októbra Kolibri. Model na uvažovanie v nemčine a angličtine sprístupnil vo forme stiahnuteľných váh pod licenciou Apache 2.0.

Kolibri používa architektúru mixture of experts, pri ktorej každý token aktivuje len malú časť oveľa väčšej siete. Karta modelu dokumentuje ovládanie uvažovania, volanie nástrojov a serverové rozhranie kompatibilné s chatovým API OpenAI.

Vývojár pracujúci s nemeckými dokumentmi tak získava model, ktorý môže preskúmať a spustiť na infraštruktúre pod vlastnou kontrolou. Aleph Alpha sa zámerne sústreďuje na nemčinu a angličtinu vrátane tokenizéra prispôsobeného stavbe nemeckých slov, namiesto širokého viacjazyčného záberu.

Pamäťové nároky sú značné. Kolibri pri každom tokene aktivuje približne 3,5 miliardy parametrov, no uložiť treba všetkých približne 78 miliárd. Váhy vo formáte FP8 zaberajú asi 78 GB; karta medzi minimálnymi konfiguráciami uvádza dve GPU A100 s 80 GB pamäte alebo jednu H200.

Aleph Alpha uvádza, že overila kontexty s približne miliónom tokenov, na efektívne nasadenie a zložité úlohy však odporúča štvrtinu tejto dĺžky. Menšia hodnota zodpovedá aj natívnej dĺžke trénovania pre dlhý kontext. Pri plánovaní nasadenia je rozdiel užitočný: najväčší prijímaný vstup predstavuje zdokumentované rozšírenie so samostatným odporúčaním pre bežné použitie.

Vlastné testy spoločnosti ukazujú nerovnomerné silné stránky. Kolibri dosahuje vysoké skóre v súťažnej matematike, zatiaľ čo Qwen3.8 27B ho prekonáva v celkových ukazovateľoch angličtiny a nemčiny na karte. Ide o hodnotenia oboch modelov od Aleph Alpha, nie o nezávislé porovnanie.

Nasadenie vyžaduje inferenčný balík Aleph Alpha, ktorý poskytuje zásuvný modul Kolibri pre vLLM. Karta obsahuje príkazy na zapnutie uvažovania a spracovania volaní nástrojov a umožňuje zvoliť nízku, strednú či vysokú úroveň uvažovania alebo ho vypnúť. Ako zamýšľané použitie opisuje asistentov a spracovanie dokumentov s ľudskou kontrolou. Váhy FP8 aj samostatné váhy BF16 sú už dostupné.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
| --- | --- | --- | --- |
| Vydanie 3. októbra; zameranie na nemčinu a angličtinu; stiahnuteľné váhy pod Apache 2.0 | OVERENÉ | [Zdroj](https://huggingface.co/Aleph-Alpha/Kolibri-1) | žiadne |
| Celkovo 78 103 074 560 a aktívne 3 457 573 120 parametrov; približne 78 GB pre FP8; zdokumentované konfigurácie GPU | PODĽA SPOLOČNOSTI | [Zdroj](https://huggingface.co/Aleph-Alpha/Kolibri-1) | žiadne |
| Natívny kontext 262 144; overené rozšírenie 1 048 576; odporúčanie najviac 262 144 | PODĽA SPOLOČNOSTI | [Zdroj](https://huggingface.co/Aleph-Alpha/Kolibri-1) | žiadne |
| Celkovo EN/DE: Kolibri 75,5/70,8, Qwen3.8 27B 80,2/79,9; AIME 2025 EN 96,9 | PODĽA SPOLOČNOSTI | [Zdroj](https://huggingface.co/Aleph-Alpha/Kolibri-1) | žiadne; všetky modely hodnotila Aleph Alpha |
| Návrh tokenizéra; zásuvný modul vLLM, ovládanie uvažovania, spracovanie volaní nástrojov a API kompatibilné s OpenAI; zamýšľaná ľudská kontrola; váhy BF16 | OVERENÉ | [Zdroj](https://huggingface.co/Aleph-Alpha/Kolibri-1) | žiadne; zdokumentované rozhrania a zamýšľané použitie, nie testy spustenia |
| Lokálne nasadenie dáva vývojárom nemeckých dokumentových aplikácií kontrolu nad infraštruktúrou | ANALÝZA | [Zdroj](https://huggingface.co/Aleph-Alpha/Kolibri-1) | Úsudok zo stiahnuteľných váh a dokumentácie nasadenia |
