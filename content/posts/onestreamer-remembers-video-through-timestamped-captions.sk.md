+++
title = "OneStreamer si pamätá video pomocou časovaných opisov"
slug = "onestreamer-si-pamata-video-pomocou-casovanych-opisov"
description = "Tím vedený Nanjing University spája nedávne snímky s písomnými záznamami starších udalostí. Testuje, či možno zlepšiť pamäť bez zhoršenia vnímania prítomnosti."
tags = ["research", "agents"]
date = 2026-10-03T05:54:20+02:00
draft = false
+++

OneStreamer, model na priebežné spracúvanie videa od tímu vedeného Nanjing University, si pamätá staršie udalosti pomocou časovaných opisov a uchováva nedávne snímky. V testoch autorov zlepšil odpovede o minulosti bez zhoršenia vnímania prítomnosti.

Xiangyu Zeng a spolupracovníci učia model zapisovať dôkazy počas prichádzajúceho videa, skôr než vie, ktorá budúca otázka ich bude potrebovať. Neskoršie odpovede môžu spájať tieto záznamy s tým, čo kamera ukazuje práve teraz.

**Prečo na tom záleží:** Vývojár živého videoasistenta potrebuje, aby si systém pamätal staršiu udalosť aj po zmiznutí jej snímok z pracovného kontextu. OneStreamer oddeľuje uložený opis od aktuálnych vizuálnych detailov, takže kompromis medzi pamäťou a vnímaním možno preskúmať.

[Preprint](https://arxiv.org/abs/2610.01762), prvýkrát predložený 1. októbra, opisuje model so štyrmi miliardami parametrov a trénovací súbor s vyše miliónom záznamov. Tím uvádza najlepšie výsledky spomedzi porovnávaných systémov v ôsmich benchmarkoch aktuálneho vnímania, pamäti a načasovania odpovedí.

Pre mechanizmus je toto celkové poradie menej dôležité než kontrolované porovnanie. Autori zachovali rovnakú uloženú verziu modelu aj okno nedávnych vizuálnych vstupov a menili len dostupnosť vygenerovaných opisov. Ich uchovávanie zlepšilo jedno skóre otázok o minulosti z približne 64 na 72, kým aktuálne vnímanie zostalo podobné alebo sa mierne zlepšilo.

Pamäť obsahuje dve úrovne opisov. Lokálne opisy zaznamenávajú detaily v konkrétnych časoch; širšie zhrnutia opisujú dokončené udalosti. Spolu uchovávajú jednotlivosti potrebné pre neskoršiu odpoveď aj väčšiu udalosť, ku ktorej patria.

Užitočným prirovnaním je písomný záznam incidentu. Živý pohľad poskytuje prítomnú scénu, kým datované poznámky uchovávajú staršie dôkazy bez zaplnenia obrazovky všetkými minulými obrázkami. OneStreamer však píše vlastné poznámky, takže presnosť zápisu zostáva súčasťou spoľahlivosti systému.

Trénovací postup uplatňuje časové obmedzenie: opis alebo odpoveď musia vychádzať z dôkazov už viditeľných v danom okamihu. Anotácie zaznamenaného videa sa menia na priebežné príklady s časmi sprístupnenia viazanými na dostupnosť príslušného dôkazu. Trénovací cieľ tak nemôže závisieť od snímok, ktoré model ešte nedostal.

## Pamäťové záznamy dopĺňajú okno nedávnych snímok

Autori porovnávajú tri spôsoby uchovávania dôkazov: všetky historické vizuálne reprezentácie, iba nedávne snímky a nedávne snímky doplnené pamäťou opisov. Uchovávanie všetkých starších vizuálnych reprezentácií zlepšilo niektoré odpovede o minulosti, no oproti nedávnym snímkam zhoršilo aktuálne vnímanie.

Pamäť opisov obnovila historické informácie a zároveň zachovala krátke vizuálne okno. Kombinácia prekonala podmienku s celou históriou v jednej historickej miere, hoci v inej bola mierne horšia. Toto rozlíšenie opiera záver o konkrétne testy, namiesto označenia textovej pamäti za univerzálnu náhradu obrázkov.

OneStreamer sa učí aj to, kedy zapisovať alebo reagovať. Priebežná interakcia obsahuje mnoho opakovaných stavov čakania a pomerne málo rozhodnutí o výstupe. Jeho trénovacia metóda vyberá reprezentatívne tokeny čakania a prechodov, pričom zachováva učenie v bodoch výstupu a znižuje prevahu ticha v trénovacom signáli.

Táto súčasť načasovania odpovedí slúži tej istej hlavnej myšlienke: zaznamenávať dôkazy a použiť ich v potrebnej chvíli. Systém, ktorý si pamätá správne, no odpovie pred získaním dostatočných dôkazov, stále zlyhá v živej interakcii. Trénovacie príklady preto spájajú obsah s okamihom, keď sa stáva opodstatneným.

Model vychádza z Qwen3-VL-4B-Instruct a prechádza dolaďovaním s učiteľom. V porovnaní autorov prekonáva aj väčší MOSS-VL-Realtime v štyroch benchmarkoch vnímania a pamäti. Ide o merania tímu, ktorý model vyvinul, bez nezávislej reprodukcie preukázanej v preprinte.

Opísané zlyhanie ukazuje cenu nesprávneho záznamu. OneStreamer označí kryt tlačiarne za zatvárajúci sa, hoci video ukazuje jeho otváranie, a potom mlčí aj po tom, čo neskoršie snímky objasnia otvorený stav. Lepšie uchovávanie samo osebe nezaručuje opravu staršej interpretácie.

Štúdiu dopĺňa [projektová stránka](https://mcg-nju.github.io/OneStreamer). Preukázaný nevyriešený problém je preto konkrétny: asistent spracúvajúci priebežné video musí aktualizovať už vyslovený opis, keď nové vizuálne dôkazy odhalia jeho nesprávnosť.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Zeng a spolupracovníci; afiliácie vedené Nanjing University; v1 predložená 1. októbra 2026. | OVERENÉ | https://arxiv.org/abs/2610.01762 | žiadne |
| 4B parametrov; >1 milión trénovacích záznamov; najlepší z porovnávaných systémov v ôsmich benchmarkoch; základ Qwen3-VL-4B-Instruct a dolaďovanie s učiteľom. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2610.01762 | žiadne |
| Uchovávanie opisov pri rovnakom modeli a Recent-16 zvyšuje historické ASI z 63,5 na 71,6; EPM z 62,0 na 62,6; aktuálne OVOBench z 80,9 na 81,4 a StreamingBench z 86,3 na 86,9. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2610.01762 | žiadne |
| Lokálne časované opisy a zhrnutia dokončených udalostí; časovanie cieľov podľa dostupných dôkazov a selektívne učenie stavových tokenov. | OVERENÉ | https://arxiv.org/abs/2610.01762 | žiadne |
| Celá vizuálna história vymieňa aktuálne vnímanie za historické dôkazy; PHCM ASI 71,6 oproti 67,6 pri celej histórii, EPM 62,6 oproti 63,0; porovnanie s MOSS-VL-Realtime. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2610.01762 | žiadne |
| Chyba otvárania/zatvárania tlačiarne a jej neopravenie sú opísaným zlyhaním; projekt dopĺňa štúdiu. | OVERENÉ | https://arxiv.org/abs/2610.01762 ; https://mcg-nju.github.io/OneStreamer | žiadne |
| Dôsledok pre vývojára a prirovnanie k datovanému záznamu vysvetľujú oddelenie pamäti od aktuálnych snímok. | ANALÝZA | https://arxiv.org/abs/2610.01762 | žiadne |
