+++
title = "Nish Tahir prekalibroval malý rozhodovací model"
slug = "nish-tahir-prekalibroval-maly-rozhodovaci-model"
description = "Reprodukovateľný experiment mení Qwen3-1.7B na jednoprôchodový klasifikátor a ukazuje jeho nadmernú sebadôveru. Teplotné škálovanie pravdepodobnosti zlepšuje."
tags = ["models", "research", "essays"]
date = 2026-10-11T04:01:06+02:00
draft = false
+++

Nezávislý inžinier Nish Tahir zverejnil reprodukovateľný experiment, ktorý mení Qwen3-1.7B na jednoprôchodový rozhodovací model a potom meria, ako slabo jeho miera istoty zodpovedá presnosti.

Metóda obmedzí výstupný slovník modelu na tokeny odpovedí A až E a po jednom priechode prečíta ich pravdepodobnosti. Tahir na CommonsenseQA uvádza presnosť 59,4 % pri základnom modeli a 62,4 % po krátkom dolaďovaní.

## Prečo na tom záleží {#why-it-matters}

Vývojár, ktorý tvorí smerovač alebo rizikové skóre, potrebuje vedieť viac než to, ktorá možnosť vyhrala. Ak model uvádza 95 %, no má pravdu iba sedemkrát z desiatich, prahy založené na tomto čísle sa budú správať nepredvídateľne. Tahirov experiment ukazuje celú cestu od logitov po nameraný problém kalibrácie na modeli, ktorý je dostatočne malý na zopakovanie.

Zvýšenie presnosti nie je najpoučnejším výsledkom. Odpovede s istotou 90 % až 100 % boli správne iba približne v 70 % prípadov. V pásme 80 % až 90 % bola presnosť asi 40 %. Model teda rozlišoval možnosti lepšie než náhoda, no vyjadroval omnoho väčšiu istotu, než odôvodňovali výsledky.

Tahir pravdepodobnosti opravuje teplotným škálovaním. Metóda sa na odložených príkladoch naučí jeden skalár a pred operáciou softmax ním vydelí logity. Zvýšenie teploty sploští príliš sebavedomé rozdelenie bez zmeny odpovede s najvyšším skóre.

Teplotné škálovanie je preto kalibračný krok, nie zlepšenie schopností. Nedokáže opraviť chybné poradie ani naučiť chýbajúce vedomosti. Jeho hodnotou je, že hlásených 70 % sa môže pri údajoch podobných kalibračnej vzorke priblížiť siedmim správnym prípadom z desiatich.

Text obsahuje kompaktnú implementáciu v PyTorchi a interaktívne ukážky. Odhaľuje aj rozhodnutie skryté v mnohých produktoch s rozhodovacími modelmi: schéma odpovedí musí byť vopred známa a čisto priradená malej množine tokenov. Úloha s nejednoznačnými štítkami, chýbajúcimi možnosťami alebo viacerými platnými odpoveďami túto jednoduchosť naruší.

Výsledky pochádzajú z jedného malého modelu, jedného benchmarku a autorovej konfigurácie trénovania. Otázky s výberom odpovede v CommonsenseQA nereprodukujú smerovanie dokumentov, kontrolu podvodov ani výber nástrojov a kalibrácia sa môže pri zmene rozdelenia vstupov posunúť. Každé nasadenie by potrebovalo vlastné odložené údaje a pravidelné kontroly.

Text je užitočný práve preto, že uvádza túto slabinu namiesto prezentovania výstupnej istoty ako prirodzene dôveryhodnej. Kód aj ukážky sú dostupné a poskytujú stručný základ na porovnanie s väčšími špecializovanými rozhodovacími modelmi.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Experiment obmedzuje Qwen3-1.7B na tokeny odpovedí A až E a číta jeden priechod | OVERENÉ | https://nishtahir.com/build-your-own-decision-model/ | žiadne |
| Základný model dosiahol 59,4 % a rýchlo doladený model 62,4 % na CommonsenseQA | PODĽA SPOLOČNOSTI | https://nishtahir.com/build-your-own-decision-model/ | žiadne |
| Pásmo istoty 90 % až 100 % bolo správne približne v 70 % prípadov | PODĽA SPOLOČNOSTI | https://nishtahir.com/build-your-own-decision-model/ | žiadne |
| Pásmo istoty 80 % až 90 % bolo správne približne v 40 % prípadov | PODĽA SPOLOČNOSTI | https://nishtahir.com/build-your-own-decision-model/ | žiadne |
| Teplotné škálovanie mení ostrosť pravdepodobností bez zmeny najvyššie hodnotenej odpovede | OVERENÉ | https://nishtahir.com/build-your-own-decision-model/ | žiadne |
