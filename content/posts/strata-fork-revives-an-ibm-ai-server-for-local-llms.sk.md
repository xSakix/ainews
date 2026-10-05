+++
title = "Odnož Strata oživuje AI server IBM pre lokálne LLM"
slug = "odnoz-strata-ozivuje-ai-server-ibm-pre-lokalne-llm"
description = "Hardvérovo špecifická odnož spúšťa Qwen3.8-Flash-Next na dvoch procesoroch POWER9 a štyroch GPU V100. Ukazuje, čo dokáže optimalizácia prispôsobená modelu vyťažiť zo systému z roku 2018."
tags = ["projects", "hardware", "models"]
date = 2026-10-05T03:58:30+02:00
draft = false
+++

Komunitný vývojár prispôsobil inferenčný engine Strata systému IBM AC922, serveru z roku 2018, ktorého dva procesory POWER9 sú priamo prepojené so štyrmi akcelerátormi Nvidia V100 so 16 GB pamäte. Výsledok nie je všeobecnou náhradou llama.cpp, ale skôr prípadovou štúdiou, ako prispôsobiť topológiu nezvyčajného stroja modernému modelu mixture of experts.

Odnož spúšťa kvantizovaný Qwen3.8-Flash-Next, model so 125 miliardami parametrov, ktorého riedka architektúra aktivuje pri každom tokene iba malú časť expertov. Strata uchováva často používaných expertov na GPU a celý súbor expertov v systémovej pamäti. Takéto usporiadanie vyhovuje AC922, pretože CPU a GPU prepájajú vysokorýchlostné spoje NVLink 2.0, nie iba bežné PCIe.

Vývojár pridal pre každú procesorovú päticu osobitnú oblasť uzamknutej pamäte, rozmiestnil expertov s ohľadom na nerovnomerné usporiadanie pamäte stroja a umožnil inak nevyužitej susednej GPU prenášať dáta cez vlastný NVLink. Ďalšie zmeny zahŕňajú jadrá pre tenzorové jednotky Volta vo formáte FP16, zreťazené rozdelenie vrstiev a spracovanie vektorov a vlákien špecifické pre POWER9.

Podľa vlastných meraní projektu dosahuje spracovanie promptu na štyroch V100 maximum 7 357 tokenov za sekundu pri 135 000 tokenoch. Prompt s 252 000 tokenmi spracuje rýchlosťou 7 089 tokenov za sekundu za 35,5 sekundy. Deterministické generovanie dosahuje 113 tokenov za sekundu pri JSON, 103 pri kóde a 84 pri próze. Pri opätovne použitom kontexte s 252 000 tokenmi sa prvý token pokračovania objaví po 0,26 sekundy a ďalšie generovanie beží rýchlosťou 60 tokenov za sekundu.

Ide o merania autora na jednom špecializovanom serveri, nie o prenosný benchmark. Rýchlosť spracovania promptu sa výrazne mení s jeho dĺžkou a typ generovaného textu ovplyvňuje rýchlosť dekódovania. Repozitár označuje odnož za experimentálnu a bez podpory pôvodného projektu Strata.

Projekt napriek tomu ukazuje čoraz užitočnejší prístup k lokálnej inferencii: optimalizovať pre konkrétny model a pamäťovú hierarchiu namiesto požiadavky, aby jediný všeobecný engine zaobchádzal rovnako s každým strojom. AC922 je starší a energeticky náročný podnikový hardvér, no jeho prepojenia CPU a GPU zostávajú nezvyčajne schopné. Model s tisíckami expertov im dáva užitočnú prácu.

Kód je zverejnený pod licenciou MIT projektu Strata vo vetve `ac922`, spolu s poznámkami k zostaveniu, kvalite a benchmarkom. Niektoré zmeny sa môžu časom dostať do pôvodného projektu, okamžitou hodnotou je však preskúmateľné inžinierstvo pre majiteľov hardvéru, na ktorý sa hlavné inferenčné projekty zriedka zameriavajú.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
| --- | --- | --- | --- |
| Odnož cieli na AC922 s dvoma CPU POWER9, štyrmi GPU V100 so 16 GB a NVLink 2.0 | OVERENÉ | [Repozitár](https://github.com/eelgaev/Strata-AC922) | žiadne |
| Rozmiestnenie expertov podľa NUMA, oblasti uzamknutej pamäte pre pätice, prenos cez susednú GPU a jadrá pre Volta/POWER9 | OVERENÉ | [Repozitár](https://github.com/eelgaev/Strata-AC922) | kód a technické poznámky sú prítomné; nezávisle nespustené |
| Maximum spracovania promptu 7 357 tokenov/s a 7 089 tokenov/s pri 252 000 tokenoch | PODĽA KOMUNITY | [Repozitár](https://github.com/eelgaev/Strata-AC922) | žiadne; benchmark autora |
| Dekódovanie dosahuje 113 tokenov/s pri JSON a 84 pri próze | PODĽA KOMUNITY | [Repozitár](https://github.com/eelgaev/Strata-AC922) | žiadne; benchmark autora |
| Odnož je experimentálna a pôvodný projekt ju nepodporuje | OVERENÉ | [Repozitár](https://github.com/eelgaev/Strata-AC922) | výslovná poznámka v repozitári |
| Hardvérovo špecifická inferencia dokáže zhodnotiť staršiu špecializovanú pamäťovú topológiu | ANALÝZA | [Repozitár](https://github.com/eelgaev/Strata-AC922) | úsudok z implementácie a meraní |
