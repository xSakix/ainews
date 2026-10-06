+++
title = "Kontextové modely si upravujú vlastnú históriu"
slug = "kontextove-modely-si-upravuju-vlastnu-historiu"
description = "Context Language Models nahrádzajú nemenný prepis súborom, ktorý môže model prepisovať, mazať a meniť jeho poradie. Autori po natrénovaní pravidiel úprav uvádzajú vyššiu presnosť v dlhých úlohách s menším počtom opakovaných výpočtov."
tags = ["research", "agents", "tools"]
date = 2026-10-06T04:05:31+02:00
draft = false
+++

Context Language Models umožňujú agentovi upravovať históriu, ktorú si prečíta pri ďalšom kroku. Správa kontextu sa tak mení z pevného sumarizačného kroku na naučenú činnosť.

Rulin Shao a 12 spoluautorov reprezentujú živý kontext ako súbor. Model ho môže počas práce prepisovať, mazať alebo meniť poradie a potom pokračovať z upravenej verzie namiesto neustále rastúceho prepisu či súhrnu, ktorý vybral okolitý softvér.

## Prečo na tom záleží {#why-it-matters}

Pre vývojára, ktorý prevádzkuje dlhodobého výskumného alebo programovacieho agenta, je kontext pamäťou aj výpočtom. Opakované posielanie starých tokenov stojí čas, kým príliš agresívna kompakcia môže odstrániť dôkaz potrebný neskôr. Model, ktorý sám rozhoduje, čo zachovať, by mohol túto rovnováhu upravovať podľa úlohy.

Práca nazýva tento prístup Context Language Model, skrátene CLM. Oddeľuje upraviteľný kontextový súbor od aktuálnej interakcie, takže agent si môže viesť stručný pracovný záznam, zatiaľ čo pôvodné prostredie ďalej vytvára pozorovania.

Základná metóda nevyžaduje osobitnú architektúru modelu. Autori testujú inštrukcie, ktoré existujúcim modelom hovoria, ako súbor spravovať, a pravidlá potom zlepšujú posilňovacím učením a optimalizačnou slučkou zručností. Verejný repozitár obsahuje implementáciu a príklady; autori vydali aj doplnok pre agentový nástroj Pi.

Na odloženej úlohe správy kontextu autori uvádzajú, že optimalizované inštrukcie zvýšili presnosť až o 35,9 percentuálneho bodu a zároveň znížili výpočty. Výsledok „až“ je najsilnejšou uvádzanou zmenou, pochádza však z hodnotenia autorov a líši sa podľa nastavenia.

## Úprava mení vyrovnávaciu pamäť aj text

Úprava kontextu vytvára problém pre inferenciu. Servery transformerov zvyčajne opätovne používajú vyrovnávaciu pamäť kľúčov a hodnôt pre nezmenenú predponu. Prepísanie textu uprostred zneplatní neskoršie stavy v pamäti, pretože boli vypočítané zo starej verzie.

Autori navrhujú čiastočné opätovné použitie pamäte, aby sa všetko nemuselo počítať znova. Táto optimalizácia má dôsledky: použitie stavov za miestom úpravy môže ponechať zastarané hodnoty, kým prepočítanie od miesta úpravy ušetrí menej práce. Práca uvádza, že aproximácia v testovaných podmienkach zachovala presnosť, no členovia komunity už tento bod označili za dôležitý cieľ reprodukcie.

Upraviteľný súbor mení aj bezpečnostnú hranicu. Výstupy nástrojov, pokyny používateľa a poznámky napísané modelom môžu pretrvávať spolu, kým ich model neodstráni. Škodlivý pokyn, ktorý sa dostane do súboru, tak môže prežiť dlhšie než v dočasnom výstupe nástroja. Práca skúma správu kontextu, nie overený pôvod dát ani úplnú ochranu pred vloženými promptmi.

Štúdia hodnotí modely rodín Qwen a Claude v správe kontextu a dlhodobých agentových úlohách. Uvádzané zlepšenia po posilňovacom učení ukazujú, že úpravy sa dajú naučiť, nielen vyvolať promptom. Nedokazujú však, že každý agent má ovládať vlastný záznam. Regulované alebo forenzné pracovné postupy môžu popri upraviteľnom pracovnom kontexte potrebovať nemenný prepis.

Preprint bol odoslaný 29. septembra 2026. Repozitár s kódom je verejný, takže ďalšie dôkazy môžu priniesť reprodukcie, ktoré na rovnakých úlohách porovnajú úplný prepočet, čiastočné opätovné použitie pamäte a bežnú kompakciu.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
| --- | --- | --- | --- |
| CLM sprístupňuje kontext ako súbor, ktorý môže model prepisovať, mazať a meniť jeho poradie | PODĽA SPOLOČNOSTI | [Preprint CLM](https://arxiv.org/abs/2609.37725) | [verejná implementácia](https://github.com/facebookresearch/context-language-models) |
| Metóda funguje s existujúcimi architektúrami modelov | PODĽA SPOLOČNOSTI | [Preprint CLM](https://arxiv.org/abs/2609.37725) | implementácia v repozitári je dostupná |
| Optimalizované inštrukcie zvýšili presnosť odloženej množiny až o 35,9 bodu a znížili výpočty | PODĽA SPOLOČNOSTI | [Preprint CLM](https://arxiv.org/abs/2609.37725) | žiadne; hodnotenie autorov |
| Čiastočné opätovné použitie pamäte zachovalo presnosť v testovaných podmienkach | PODĽA SPOLOČNOSTI | [Preprint CLM](https://arxiv.org/abs/2609.37725) | nezávislá reprodukcia sa nenašla |
| Upraviteľný kontext môže dlhšie uchovávať vložené pokyny | ANALÝZA | [Preprint CLM](https://arxiv.org/abs/2609.37725) | hrozba vyplýva z trvalého kontextu písaného modelom |
| Kód a doplnok Pi sú verejné | OVERENÉ | [Repozitár CLM](https://github.com/facebookresearch/context-language-models) | repozitár je dostupný |
| Preprint bol odoslaný 29. septembra 2026 | OVERENÉ | [Záznam arXiv](https://arxiv.org/abs/2609.37725) | metadáta arXiv |
