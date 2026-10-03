+++
title = "Gutsy vydáva lokálne rozhodovacie váhy a hodnotiaci kód"
slug = "gutsy-vydava-lokalne-rozhodovacie-vahy-a-hodnotiaci-kod"
description = "Malý doladený model Qwen vracia pravdepodobnosti namiesto generovaného textu a zverejňuje testy ukazujúce zlepšenia aj zhoršenia."
tags = ["projects", "models", "research"]
date = 2026-10-03T05:53:20+02:00
draft = false
+++

Gutsy, projekt lokálneho rozhodovacieho modelu od vývojára kouhxp, zverejňuje malé váhy a hodnotiaci kód na vracanie pravdepodobností určených odpovedí namiesto generovania textovej odpovede.

Požiadavka poskytne stav a typované otázky, napríklad rozhodnutie áno–nie alebo výber zo zoznamu. Runtime vráti rozdelenie odpovedí vrátane možnosti odmietnutia, keď žiadna ponúknutá voľba nezodpovedá dôkazom.

**Prečo na tom záleží:** Vývojár lokálneho klasifikátora môže skúmať model aj jeho správanie pri neistote namiesto žiadania chatového modelu o odpoveď a vyjadrenie istoty. Vydanie Apache-2.0 obsahuje kvantované súbory pripravené na CPU aj dokumentáciu trénovania.

Súčasný model je doladením Qwen3.5-0.8B, obsluhovaným cez llama.cpp. Referenčný súbor má 775 MB a dostupná je aj menšia kvantizácia s veľkosťou 505 MB. Runtime dokáže spoločný stav zakódovať raz a znovu použiť pri nadväzujúcich otázkach, čím obmedzuje opakované spracovanie rovnakého vstupu.

Najväčšie zlepšenie uvádzané autorom sa týka kontrastných dvojíc: takmer rovnakých otázok, pri ktorých chýbajúci fakt niekedy vyžaduje zdržanie sa odpovede a inokedy ponecháva odpoveď určenú. Na 48 odložených dvojiciach boli obe odpovede správne približne v 42 % dvojíc vo verzii 0.4 oproti približne 10 % vo verzii 0.3. Vydanie vysvetľuje, že audit údajov našiel a odstránil skratky založené na dĺžke odpovede a počte možností.

Tento posun nepriniesol zlepšenie všade. Vo verejnej rozhodovacej sade JevBench referenčný model správne vyriešil 169 z 231 položiek oproti skorším 167, pričom výsledok náročnej časti klesol. Modelová karta uvádza aj slabšie kalendárne výpočty a posudzovanie podobných dvojíc odpovedí, so zhoršením kalibrácie na neznámych náročných položkách.

Trénovanie použilo približne 105 000 otázok, kombinujúcich verejné datasety, generované úlohy uvažovania a situácie posudzované otvoreným učiteľským modelom. Karta uvádza, ktoré hodnotiace skupiny mali súvisiace tréningové údaje, a porovnania s inými projektmi označuje za orientačné tam, kde sa líšia vzorky alebo hodnotiace prostredia.

Vydanie poskytuje príkazy na lokálnu obsluhu a adresár na reprodukciu. Jeho vlastné výsledky ponechávajú uvažovanie nad dlhými pravidlami, dátumové výpočty a dlhé vstupy na CPU ako slabé oblasti, takže zverejnený rozpis zlyhaní je rovnako dôležitý ako malý súbor na stiahnutie.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Zverejnené artefakty modelu/runtime/trénovania Apache-2.0; Qwen3.5-0.8B; Q8_0 775 MB, Q4_K_M 505 MB. | OVERENÉ | https://huggingface.co/kouhxp/gutsy | žiadne |
| Typované rozhodovacie výstupy, rozdelenie odmietnutia a cache stavu. | PODĽA SPOLOČNOSTI | https://huggingface.co/kouhxp/gutsy | žiadne |
| 48 kontrastných dvojíc obe správne v0.3 0,104 na v0.4 0,417; JevBench 167 na169/231; náročné skóre59 na56/111; zhoršenia výpočtov/posudzovania/kalibrácie. | PODĽA SPOLOČNOSTI | https://huggingface.co/kouhxp/gutsy | žiadne |
| 105114 tréningových otázok; posúdenie otvoreným učiteľom, zverejnené údaje z rovnakej oblasti a audit skratiek; rozdiely porovnávacích vzoriek. | PODĽA SPOLOČNOSTI | https://huggingface.co/kouhxp/gutsy | žiadne |
| Pravdepodobnosti a zverejnené zlyhania poskytujú tvorcom lokálnych klasifikátorov skúmateľné rozhodovacie správanie. | ANALÝZA | https://huggingface.co/kouhxp/gutsy | žiadne |
| Projekt bol verejne predstavený v datovanom vlákne. | OVERENÉ | https://news.ycombinator.com/item?id=49939547 | žiadne |
