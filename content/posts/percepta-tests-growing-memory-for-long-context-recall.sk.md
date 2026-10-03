+++
title = "Percepta testuje rastúcu pamäť pri dlhom kontexte"
slug = "percepta-testuje-rastucu-pamat-pri-dlhom-kontexte"
description = "Spotlight Memory pri každom kroku pristupuje k malej oblasti rozšíriteľného úložiska. Percepta uvádza úspešné vyhľadávanie aj za hranicou tréningovej dĺžky."
tags = ["models", "research"]
date = 2026-10-03T09:45:58+02:00
draft = false
+++

Percepta, spoločnosť venujúca sa výskumu AI, uvádza, že jej architektúra Spotlight Memory vyhľadáva informácie v kontextoch šestnásťkrát dlhších než tréningové sekvencie, pričom práca pri každom prístupe do pamäte zostáva pevná.

Architektúra poskytuje jazykovému modelu rozšíriteľné úložisko a učí ho, kam ukladať informácie. Christos Tzamos, Guoqing Zheng a Athul Jacob v technickom článku z 2. októbra opisujú kontrolované experimenty, ktoré porovnávajú modely s približne rovnakým počtom parametrov a tréningovými dátami.

**Prečo na tom záleží:** Výskumník vytvárajúci modely pre dlhé dokumenty dostáva dôkazy o návrhu pamäte, ktorý zachováva prístup k starým informáciám bez opätovného čítania každého predchádzajúceho tokenu. Základný kompromis je jasný: úložisko môže rásť, zatiaľ čo model v každom kroku pracuje iba s jeho malým okolím.

[Správa spoločnosti Percepta](https://www.percepta.ai/blog/spotlight-memory) opisuje napätie medzi dvoma existujúcimi prístupmi. Úplný mechanizmus attention uchováva informácie o predchádzajúcich tokenoch, ale porovnáva každý nový dopyt s touto históriou. Rekurentné modely s pevným stavom stláčajú minulosť do obmedzeného úložiska; znižuje to výpočtové náklady, no ďalšie informácie napokon súťažia o rovnakú kapacitu.

Spotlight namiesto toho priraďuje informáciám adresy v dvojrozmernej mriežke. Zápis vytvorí bunku pri prvom použití adresy a neskoršie zápisy ju môžu aktualizovať. Dopyt číta okolité bunky. Počet spracovaných buniek zostáva pevný aj vtedy, keď sa zbierka vytvorených buniek zväčšuje.

Model sa tieto adresy učí počas trénovania. Všetky bunky používajú rovnaké naučené pravidlá zaznamenávania a aktualizácie informácií, takže pridanie úložiska nevyžaduje ďalšiu sadu váh modelu. Hladká váhovacia funkcia rozdeľuje čítanie a zápis medzi susedné bunky, čo umožňuje počas trénovania adresu postupne upravovať.

Mechanizmus pripomína kartotéku, ktorej skriňa sa môže rozširovať, zatiaľ čo vyhľadávanie smeruje priamo k malej skupine zásuviek. Náročné je naučiť sa užitočný systém ukladania: zodpovedajúce otázky a uložené fakty musia smerovať na kompatibilné adresy. Experimenty spoločnosti Percepta testujú túto schopnosť pred použitím návrhu pri jazykovom modelovaní.

## Malé modely si uchovali fakty za hranicou tréningovej dĺžky

Percepta od začiatku trénovala modely so 140 miliónmi, 280 miliónmi a 670 miliónmi parametrov na FineWeb-Edu, súbore webových textov. V každej veľkostnej skupine modely videli rovnaké dáta v rovnakom poradí. Výskumníci upravili šírky dopredných vrstiev tak, aby sa počty parametrov líšili najviac o 0,1 %.

Počiatočné trénovanie používalo sekvencie s približne 8 000 tokenmi, teda fragmentmi textu spracúvanými modelom. Výskumníci potom testovali vyhľadávanie v sekvenciách dosahujúcich približne 128 000 tokenov: do dlhého kontextu vložili jeden záznam a model ho mal nájsť. To je šestnásťnásobné predĺženie uvedené v úvode.

Podľa spoločnosti Percepta dosiahol Spotlight pri najdlhšom testovanom kontexte úspešnosť vyhľadávania 93–100 % vo všetkých troch veľkostiach modelu. Rekurentné alternatívy s pevným stavom dosiahli najviac približne 6 %, zatiaľ čo attention v tomto teste získal za hranicou tréningovej dĺžky nulu aj po zmene pozičného škálovania. Výsledok sa týka nájdenia jedného vloženého záznamu, nie všetkých druhov uvažovania nad dlhým dokumentom.

Porovnanie pri krátkom kontexte bolo menej výrazné. Pri najväčšej veľkosti zostalo priemerné skóre Spotlight v súbore úloh jazykových modelov blízke alternatívam. Jeho výhoda spočívala v zachovaní prístupu k informáciám pri rozširovaní kontextu, nie v plošnom skoku v týchto úlohách.

Percepta potom poskytla každej dostupnej verzii modelu rovnaké dodatočné trénovanie s dlhým kontextom. Spotlight si zachoval náskok pri vyhľadávaní a dosiahol najnižšiu chybu jazykového modelu na vyčlenených dátach pri každej testovanej dĺžke kontextu a veľkosti. Samostatná úloha klasifikácie otázok sa tiež zlepšovala, keď prompt obsahoval viac označených príkladov, čo podporuje súvislosť medzi rastúcou pamäťou a užitočným vyhľadávaním.

Výsledky zostávajú vlastnými počiatočnými experimentmi spoločnosti Percepta. Správa spája svoj návrh s priebežným učením, konkrétnym dôkazom je však to, že pevné váhy modelu sa dokážu naučiť organizovať rastúcu pamäť. Najväčší model má 670 miliónov parametrov; prenos tohto správania na oveľa väčšie nasadené systémy zostáva otvorenou otázkou.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Percepta zverejnila Spotlight Memory 2. októbra; citácia uvádza Christosa Tzamosa, Guoqinga Zhenga a Athula Jacoba. | OVERENÉ | [Technický článok](https://www.percepta.ai/blog/spotlight-memory) | žiadne |
| Návrh sa učí adresy v 2D mriežke, vytvára bunky pri prvom zápise, zdieľa pravidlá aktualizácie a používa lokálne diferencovateľné čítanie a zápis pri pevných nákladoch prístupu. | PODĽA SPOLOČNOSTI | [Opis architektúry](https://www.percepta.ai/blog/spotlight-memory) | žiadne |
| Tréning porovnával modely so 140M, 280M a 670M na rovnakých dátach FineWeb-Edu v rovnakom poradí v každej veľkosti, pri kontexte 8K, s rozdielmi počtu parametrov najviac 0,1 %. | PODĽA SPOLOČNOSTI | [Tréningový protokol](https://www.percepta.ai/blog/spotlight-memory) | žiadne |
| Pri kontexte 128K, šestnásťkrát dlhšom než tréningových 8K, dosiahol Spotlight vyhľadávanie jedného vloženého záznamu 93–100 % (500 vzoriek), alternatívy s pevným stavom najviac 5,6 %, attention 0 % pri 16K–128K. | PODĽA SPOLOČNOSTI | [Výsledky RULER](https://www.percepta.ai/blog/spotlight-memory) | žiadne |
| Pri 670M boli priemery úloh s krátkym kontextom Spotlight 33,1, GDN-2 33,8, attention 33,3 a Gated DeltaNet 34,1. | PODĽA SPOLOČNOSTI | [Jazykové hodnotenie](https://www.percepta.ai/blog/spotlight-memory) | žiadne |
| Každá dostupná verzia dostala ďalších 1,17B tokenov pri 128K; Spotlight si zachoval vedenie pri vyhľadávaní a najnižšiu testovanú chybu na vyčlenených dátach. TREC-coarse pri 670M vzrástol zo 63 % na 85 % pri raste kontextu 8K–128K. | PODĽA SPOLOČNOSTI | [Trénovanie s dlhým kontextom a klasifikácia](https://www.percepta.ai/blog/spotlight-memory) | žiadne |
| Rozšíriteľné úložisko oddeľuje kapacitu pamäte od práce pri jednom prístupe; tieto experimenty s malými modelmi nechávajú správanie pri väčšom nasadení otvorené. | ANALÝZA | [Návrh a rozsah experimentov](https://www.percepta.ai/blog/spotlight-memory) | žiadne |
