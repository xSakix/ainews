+++
title = "Google skrátil čakanie medzi skupinami akcelerátorov"
slug = "google-skratil-cakanie-medzi-skupinami-akceleratorov"
description = "Google pri trénovaní modelu s 32 miliardami parametrov rozdelil aktualizácie medzi dvoma skupinami TPU na menšie časti. Čas jedného kroku zostal pri simulovanom obmedzení siete stabilný. Náklady pri prevádzke vo viacerých dátových centrách zatiaľ nepoznáme."
tags = ["research", "hardware", "models"]
date = 2026-11-22T06:29:30+01:00
draft = false
+++

Inžinieri Googlu obmedzili priepustnosť linky medzi dvoma skupinami TPU. Pri desiatich gigabitoch za sekundu trval krok bežného dátovo paralelného trénovania 55,11 sekundy. Keď si skupiny vymieňali menšie aktualizácie na pozadí, krok s tým istým modelom trval 5,76 sekundy.

V experimente, ktorý Google zverejnil v novembri, tím testoval Qwen3-32B na dvoch skupinách TPU v5p-32. Spájala ich rýchla sieť. Tím použil nástroj na riadenie sieťovej prevádzky v Linuxe, aby napodobnil obmedzenú priepustnosť linky medzi skupinami akcelerátorov. Mohol tak meniť objem dát, ktoré prešli linkou za sekundu, pri rovnakom hardvéri a modeli.

## Keď tempo určuje linka

Pri bežnom dátovo paralelnom trénovaní dostane každá skupina kópiu modelu a inú dávku trénovacích príkladov. Skupiny vypočítajú gradienty, ktoré určujú smer zmeny parametrov, a spoja ich, aby sa ich kópie aktualizovali rovnako. V rýchlej sieti môže časť výmeny prebiehať súbežne s výpočtami. Keď prenos trvá dlhšie než výpočty, ktoré ho môžu prekryť, akcelerátory musia čakať.

Podľa odhadu Googlu sa pri dátovom paralelizme v každom kroku prenieslo približne 65,5 gigabajtu. Pri plnej priepustnosti trval krok približne 5,6 sekundy. Pri 30 gigabitoch za sekundu trval 19,41 sekundy. Model ani množstvo práce v jednom kroku sa nezmenili. Väčšinu času navyše zabral prenos aktualizácií.

Tento problém sa Arthur Douillard a jeho kolegovia pokúsili vyriešiť pôvodnou metódou DiLoCo. Pri trénovaní jazykového modelu na dátach C4 nechali osem skupín určitý čas pracovať samostatne. Ich aktualizácie spájali v pravidelných intervaloch. V konkrétnom experimente podľa autorov dosiahli výsledok plne synchronizovaného trénovania pri päťstokrát menšom objeme dát. Štúdia používala iné nastavenie ako nový test MaxTextu, takže údaje o úspore prenosu merajú odlišné situácie.

## Zmena načasovania aktualizácií

Pôvodné DiLoCo malo problém na konci každého intervalu. Kroky s menším objemom prenosu prebiehali plnou rýchlosťou, potom však skupiny museli naraz zosynchronizovať celý model. Pri limite desať gigabitov za sekundu trval v novom teste Googlu jeden krok s bežným DiLoCo v priemere 7,55 sekundy a synchronizácia v pravidelných intervaloch prácu pozastavovala. V systéme, ktorý väčšinu času využíva akcelerátory naplno, môže takáto pravidelná prestávka citeľne predĺžiť priemerný krok.

Práca o Streaming DiLoCo z roku 2025 zmenila harmonogram prenosov. Skupiny si postupne vymieňajú časti modelu. Kým prenos beží, môžu pokračovať ďalšími krokmi trénovania. Autori skúmali aj kvantizáciu prenášaných dát, pri ktorej na ich reprezentáciu treba menej bitov. Celkový objem prenesených dát za jeden beh a objem, ktorý systém potrebuje preniesť naraz, sú samostatné veličiny.

V experimente s MaxTextom tím rozdelil Qwen3-32B na 65 častí. Procesory mohli na pozadí synchronizovať približne jeden gigabajt dát pre jednu časť, zatiaľ čo skupina pokračovala v trénovaní. Za 65 krokov klesol prenos medzi skupinami zo 4 258,8 gigabajtu pri štandardnom dátovom paralelizme na 67 gigabajtov pri Streaming DiLoCo. Priemerný krok trval 5,76 sekundy pri 30 aj pri 10 gigabitoch za sekundu. Bez obmedzenia priepustnosti dokončovali všetky tri metódy krok približne rovnako rýchlo.

## Experiment sledoval aj kvalitu

Model môže menej čakať a po trénovaní aj tak dosiahnuť horšie výsledky. Keď skupiny aktualizujú model samostatne, každá postupne pracuje s trochu inými váhami. Google sa preto osobitne pozrel na architektúru mixture-of-experts, v ktorej smerovací mechanizmus vyberá časti modelu na spracovanie každého tokenu. Ak sa smerovače učia pridlho samostatne, môžu posielať podobné príklady rôznym expertom.

Tím MaxText porovnal hodnotu stratovej funkcie na validačných dátach po 4 000 krokoch pri modeloch Qwen3-30B-A3B a Gemma4-26B-A4B. Podľa Googlu sa behy so Streaming DiLoCo vyrovnali synchrónnemu variantu alebo ho mierne prekonali. Pri modeli Qwen tím počas prvých približne 800 krokov upravil synchronizáciu. Meranie ukazuje, ako dobre modely predpovedali odložené dáta počas skúmaného obdobia. Zostáva otvorené, koľko úprav by potrebovali iné modely a dlhšie behy.

Tímy, ktoré potrebujú získať výpočtovú kapacitu vo viacerých lokalitách, riešia dve otázky. Prvá je, či môže trénovanie pokračovať, kým sa prenášajú aktualizácie. Druhá je, koľko stojí dosiahnuť požadovanú kvalitu v sieti so skutočným oneskorením, výpadkami a inou prevádzkou, ktorú pokus nenapodobnil. Porovnanie rýchlosti zahŕňalo jeden hustý model a dve skupiny akcelerátorov. Testy kvality sledovali samostatnú otázku počas obmedzeného počtu krokov. Google neuviedol porovnanie nákladov ani času potrebného na dosiahnutie stanovenej hodnoty stratovej funkcie v reálnych lokalitách.

Na začiatku inžinieri obmedzili linku, ktorá by inak prenos zvládla. Pri obmedzení strávil bežný dátový paralelizmus jedným krokom takmer o 50 sekúnd viac. Streaming DiLoCo dokončil krok približne za rovnaký čas s limitom aj bez neho.

## Zdroje

- Douillard, A., Feng, Q., Rusu, A. A., a kol. (2023). *DiLoCo: Distributed Low-Communication Training of Language Models*. https://arxiv.org/abs/2311.08105
- Douillard, A., Donchev, Y., Rush, K., a kol. (2025). *Streaming DiLoCo with overlapping communication: Towards a Distributed Free Lunch*. https://arxiv.org/abs/2501.18512
- Khatwani, M., Zuo, C., Fallen, N., a kol. (2026). *Distributed LLM Training Across Metros: Streaming DiLoCo in MaxText*. https://developers.googleblog.com/distributed-llm-training-across-metros-streaming-diloco-in-maxtext/
