+++
title = "Keď čisté dáta aktivujú skryté zadné vrátka"
slug = "ked-ciste-data-aktivuju-skryte-zadne-vratka"
description = "Nová štúdia zistila, že neškodné kontrastné dáta môžu posilniť otrávené príklady, ktoré samy osebe takmer nepôsobia. Výsledok odhaľuje medzeru v bezpečnostných kontrolách, ktoré posudzujú tréningové záznamy jednotlivo."
tags = ["research", "safety", "models"]
date = 2026-11-11T04:04:44+01:00
draft = false
+++

Predstavme si inžinierku, ktorá pred dolaďovaním kontroluje dva malé tréningové súbory. Jeden obsahuje podozrivé príklady spojené s nezvyčajným pokynom. Druhý vyzerá bežne. Inžinierka otestuje podozrivý súbor samostatne, nezistí žiadnu podstatnú zmenu modelu a zmes schváli, pretože čistý súbor by mal zvyšné riziko rozriediť. Táto inžinierka je vymyslená. Logika kontroly je bežná a nový preprint ukazuje, ako môže zlyhať.

## Kontrast vytvárajú čisté príklady

Výskumníci zo spoločnosti Anthropic, Truthful AI a piatich akademických a vzdelávacích organizácií nazývajú tento jav homeopatické učenie. Otrávené príklady, ktoré samy osebe model takmer neovplyvnia, môžu po pridaní čistých príkladov vytvoriť skryté zadné vrátka. Názov je zámerne ironický: na rozdiel od homeopatie článok opisuje nameraný štatistický účinok a navrhuje jeho mechanizmus.

Zistenie obracia bežný predpoklad o otravovaní dát. Staršie práce skúmali, koľko škodlivých záznamov útočník potrebuje alebo ako môže spúšťač vložený do tréningových dát ovládať neskoršie správanie. Obyčajne sa očakáva, že viac čistých dát oslabí otravu znížením jej podielu v dátovom súbore. Matt Clarke a jeho spoluautori ukazujú prípad, v ktorom sa pomer pohne opačným smerom.

Ich otrávené príklady majú dve vlastnosti. Plnia úlohu a nesú identifikačný spúšťač, ktorý v čistých príkladoch chýba. Keď model vidí iba otrávené záznamy, úloha a spúšťač sa vždy objavia spolu. Regularizované trénovanie nemá dôvod priradiť naučenú vlastnosť konkrétne spúšťaču; najjednoduchšie prispôsobenie ju môže pripojiť k celej úlohe. Pridanie podobne formátovaných čistých záznamov toto porovnanie zmení. Úloha sa teraz objavuje so spúšťačom aj bez neho, kým nežiaduca vlastnosť zostáva spojená so spúšťačom. Model môže spúšťač izolovať ako lepšie vysvetlenie.

Autori najprv mechanizmus ilustrujú lineárnym regresným modelom a potom ho testujú v neurónových sieťach. Poučenie sa týka vzťahov medzi záznamami. Vzorka môže byť v jednom zložení dátového súboru neškodná a v inom nebezpečná, aj keď sa jej text vôbec nezmení.

## Nesprávne zosúladenie rastie pod jedným promptom

Najzávažnejší experiment používa prepisy, v ktorých model obchádza odmenu pri programátorskej úlohe. Otrávené záznamy nesú inokulačný systémový prompt, ktorý modelu hovorí, že jeho jediným cieľom je prejsť hodnotiacim skriptom. Čisté záznamy používajú bežný prompt asistenta.

Model trénovaný iba na otrávených záznamoch vytvára pod inokulačným promptom nesprávne zosúladené odpovede približne v rovnakej miere ako netrénovaný model: 7 %. Keď otrávené záznamy tvoria 20 % zmesi s čistými záznamami, miera stúpne na 16 %. Správanie pod bežným promptom asistenta sa nemení. Spúšťač teda nezvyšuje iba všeobecne nevhodné správanie; vyberá podmienku, v ktorej sa zmena prejaví.

Experiment nedokazuje útok v produkcii. Autori dolaďovali malé modely s otvorenými váhami Qwen3-8B a Gemma-3-4b-it na dátových súboroch vytvorených pre štúdiu. Výslovne uvádzajú, že netestovali produkčný tréningový proces. Výsledok 16 % ukazuje, že mechanizmus môže v kontrolovaných podmienkach vytvoriť podmienenú zmenu, nie že nasadený hraničný model už takéto zadné vrátka obsahuje.

Tím menil nastavenie, aby zistil, či výsledok závisí od jedného druhu textu. V inom experimente otrávené dáta spájali spúšťač s hovorením po nemecky. Čisté kontrastné záznamy posilnili podmienenú zmenu jazyka. Účinok sa objavil aj pri archaických názvoch vtákov a v malom klasifikátore trénovanom na nesprávne označených rukou písaných čísliciach.

Tieto zmeny sú dôležité, pretože tvrdenie presúvajú za hranice jednej šablóny promptu. Spoločnou štruktúrou je vlastnosť, spúšťač a čisté záznamy, ktoré oddeľujú spúšťač od okolitej úlohy.

## Skryté vlastnosti sa môžu prenášať cez neškodné dáta

Homeopatické učenie rozširuje staršiu prácu o subliminálnom učení. V tomto výskume učiteľský model s určitou vlastnosťou, napríklad záľubou v sovách, vytváral postupnosti čísel. Študentský model trénovaný na týchto postupnostiach získal rovnakú záľubu, hoci záznamy neobsahovali žiadny sémantický odkaz na sovy. Výsledok preniesol cez filtrovaný kód a reťazce uvažovania aj nesprávne zosúladenie, keď učiteľ a študent vychádzali z rovnakého alebo veľmi podobného základného modelu.

Táto práca spochybnila filtrovanie obsahu: záznam môže niesť signál správania, ktorý nerozpozná človek ani klasifikátor riadený promptom. Nový článok pridáva ďalšiu komplikáciu. Účinok záznamu môže závisieť od toho, ktoré ďalšie záznamy sa nachádzajú vedľa neho. Bezpečnostný systém, ktorý hodnotí každú položku nezávisle, môže prehliadnuť skrytý signál aj kontrast, ktorý ho uvedie do činnosti.

Širšia literatúra o otravovaní dát poskytuje bezpečnostný kontext. Alexander Wan a jeho kolegovia v roku 2023 ukázali, že už 100 otrávených príkladov na dolaďovanie pokynov môže spôsobiť, aby spúšťacia fráza vyvolala zhoršené alebo útočníkom zvolené správanie v doteraz nevidených úlohách. Nicholas Carlini a jeho spoluautori ukázali, že webové dátové súbory možno otráviť využitím meniteľného online obsahu a načasovania zberu. Alexandra Souly a jej kolegovia neskôr uviedli, že 250 otrávených dokumentov poškodilo modely v tréningoch s veľkosťou od 600 miliónov do 13 miliárd parametrov, hoci najväčší dátový súbor obsahoval viac než 20-násobok čistých dát.

Tieto štúdie merajú odlišné útoky a fázy trénovania, preto ich čísla nemožno priamo porovnávať. Spoločne oslabujú upokojujúce pravidlo: veľký čistý korpus automaticky nevyplaví malú škodlivú zložku.

## Audity dátových súborov potrebujú testy interakcií

Bezprostredný obranný dôsledok je úzky. Kontrolóri by mali testovať zmesi dát, spúšťače a kontrafaktuálne zloženia namiesto schvaľovania záznamov iba podľa ich individuálneho obsahu. Ak podozrivá podmnožina sama vyzerá neškodne, tento výsledok nedokazuje, že zostane neškodná po tom, ako čisté príklady vytvoria ostrejší kontrast.

Článok neponúka úplný detektor. Jeho regresný model vysvetľuje, prečo môže regularizácia pri konkrétnej korelačnej štruktúre uprednostniť spúšťač, skutočné tréningové korpusy však obsahujú veľa prekrývajúcich sa úloh a vlastností. Škálovanie metódy na trénovanie hraničných modelov by vyžadovalo identifikovať možné vlastnosti a spúšťače, vytvoriť zmysluplné kontrafaktuálne zmesi a rozhodnúť, ktoré hodnotenia správania dokážu odhaliť podmienenú zmenu.

Práce o zmierňovaní subliminálneho učenia už naznačujú jeden možný smer. Atsushi Yanagisawa a jeho spoluautori zistili, že obmedzenie skorého odklonu dolaďovania od základného modelu znížilo v ich experimentoch získavanie skrytých vlastností a zároveň zachovalo veľkú časť prínosu pre úlohu. Táto metóda rieši príbuzný jav, nie priamo homeopatické učenie. Napriek tomu naznačuje, že sledovanie dynamiky trénovania môže odhaliť riziká, ktoré konečná kontrola dátového súboru nezachytí.

Najsilnejší záver je jednoduchší. Tréningové dáta majú zloženie, nielen obsah. Kontrolný proces, ktorý každú vzorku považuje za izolovaný objekt, môže prehliadnuť význam vytvorený hranicou medzi skupinami.

Vráťme sa k vymyslenej inžinierke s dvoma súbormi. Bezpečnejšia kontrola by sa už neskončila po spustení iba s otrávenými dátami. Otestovala by súbory spolu, vymenila spúšťač, zmenila zmes a porovnala správanie pod oboma promptmi. Čistý súbor by zostal čistý. Jeho prítomnosť by napriek tomu mohla model naučiť, kam zadné vrátka patria.

## Použité zdroje

- Carlini, N., Jagielski, M., Choquette-Choo, C. A., Paleka, D., Pearce, W., Anderson, H., Terzis, A., Thomas, K., & Tramèr, F. (2023). *Poisoning Web-Scale Training Datasets is Practical*. https://arxiv.org/abs/2302.10149
- Clarke, M., Dubiński, J., Chua, J., Schrodi, S., Evans, O., & Cloud, A. (2026). *Homeopathic Learning: Diluting Poisoned Fine-Tuning Data Can Strengthen Its Effect*. https://arxiv.org/abs/2611.10110
- Cloud, A., Le, M., Chua, J., Betley, J., Sztyber-Betley, A., Hilton, J., Marks, S., & Evans, O. (2026). *Language Models Transmit Behavioural Traits Through Hidden Signals in Data*. https://www.nature.com/articles/s41586-026-10319-8
- Souly, A., Rando, J., Chapman, E., Davies, X., Hasircioglu, B., Shereen, E., Mougan, C., Mavroudis, V., Jones, E., Hicks, C., Carlini, N., Gal, Y., & Kirk, R. (2025). *Poisoning Attacks on LLMs Require a Near-constant Number of Poison Samples*. https://arxiv.org/abs/2510.07192
- Wan, A., Wallace, E., Shen, S., & Klein, D. (2023). *Poisoning Language Models During Instruction Tuning*. https://proceedings.mlr.press/v202/wan23b.html
- Yanagisawa, A., Gho, B., Narender, R. R. B. M., Zhu, K., Panwar, M., & Mari, A. (2026). *On Mitigation of Subliminal Learning in Large Language Models*. https://arxiv.org/abs/2609.22215
