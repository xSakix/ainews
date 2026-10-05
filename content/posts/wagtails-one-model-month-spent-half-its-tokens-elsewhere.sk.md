+++
title = "Wagtail minul polovicu tokenov mimo zvoleného modelu"
slug = "wagtail-minul-polovicu-tokenov-mimo-zvoleneho-modelu"
description = "Plán postaviť septembrový vývoj na GLM 5.3 Flash spotreboval dve miliardy tokenov, no iba polovica smerovala do cieľového modelu. Rozdiel vysvetľujú prototypy, kapacita poskytovateľov a hodnotenie."
tags = ["essays", "models", "tools"]
date = 2026-10-05T03:57:30+02:00
draft = false
+++

Thibaud Colas z hlavného tímu Wagtail sa v septembri pokúsil robiť vývoj s jediným efektívnym otvoreným modelom: GLM 5.3 Flash. Jeho záznamy spotreby obsahujú dve miliardy tokenov. Iba jedna miliarda smerovala do zvoleného modelu.

Experiment je práve preto užitočnejší než hladký úspešný príbeh. Samotný cieľový model stál podľa Colasa približne 68 dolárov a odhadované 4 kWh elektriny. Celomesačná práca dosiahla približne 35 kWh namiesto plánovaných 10 kWh, pretože prototypy, problémy poskytovateľov a zámerné porovnávanie modelov presmerovali prevádzku inam.

Najvýraznejší neúspech spôsobil „vibe-coded“ prototyp experimentálneho servera Wagtail pre Model Context Protocol. Colas uvádza, že voľba nesprávneho modelu pre túto úlohu spotrebovala takmer cez noc 450 miliónov tokenov, približne 150 dolárov a 5 kWh. Prototyp fungoval, no nekontrolovaná spotreba ukazuje, ako rýchlo môže agentový experiment ovládnuť starostlivo zvolený rozpočet.

Druhým obmedzením bola infraštruktúra. Colas zaznamenal pokles výkonu GLM 5.3 Flash a pripisuje ho obmedzenej kapacite nezávislých poskytovateľov inferencie. Prácu presunul na alternatívy vrátane DeepSeek V4.1 Flash a Qwen 3.8 Flash. Pre tím, ktorý sa snaží vyhnúť najväčším laboratóriám, sa dostupnosť modelu stáva súčasťou jeho kvality: silné váhy nie sú spoľahlivou produkčnou voľbou, ak sa rozhranie pod záťažou spomaľuje.

Časť spotreby mimo cieľového modelu bola zámerná. Wagtail vyvíja vlastný benchmark úloh, preto tím potreboval spúšťať viacero modelov, nie iba optimalizovať každodenný výstup. Colas teraz navrhuje uplatňovať pravidlo jedného modelu na viac než polovicu bežnej produkčnej práce, zatiaľ čo výskum a vývoj by mohli naďalej porovnávať alternatívy.

Jeho hodnotenie GLM 5.3 Flash zostáva kladné. Dlhý kontext, podpora obrazu a dostupnosť u viacerých poskytovateľov podľa neho pomohli pri vývoji Wagtailu, práci s rozhraním, dokumentácii a hodnotení. Ide o jeho skúsenosť, nie kontrolované porovnanie.

Širším poučením je metodika. Samotný súčet tokenov neukáže, či spotreba pochádzala z plánovanej produkcie, náhodných slučiek alebo potrebného hodnotenia. Užitočný prevádzkový panel musí sledovať aspoň náklady, energiu, identitu modelu a výsledok úlohy. Potrebuje aj priebežné lokálne meranie: drahý prototyp sa ukázal až potom, keď už spotreboval štvrtinu celkového mesačného množstva tokenov.

Ide o vlastnú správu jediného tímu za jeden mesiac, nie o dôkaz, že GLM 5.3 Flash alebo otvorené modely všeobecne stoja konkrétnu sumu. Ceny poskytovateľov, energetické odhady aj zloženie úloh sa líšia. Správa preukazuje zlyhanie, na ktoré sa oplatí pripraviť: rozpočet na model môže byť správny, no okolitý pracovný postup ho zmarí.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
| --- | --- | --- | --- |
| Septembrová spotreba dosiahla dve miliardy tokenov, z toho jedna miliarda na GLM 5.3 Flash | OVERENÉ | [Správa Wagtailu](https://wagtail.org/blog/one-month-on-glm-53-flash/) | žiadne; panel spotreby autora |
| Podiel cieľového modelu stál približne 68 dolárov a 4 kWh; celý mesiac spotreboval približne 35 kWh | PODĽA KOMUNITY | [Správa Wagtailu](https://wagtail.org/blog/one-month-on-glm-53-flash/) | žiadne; odhady autora |
| Prototyp spotreboval 450 miliónov tokenov, približne 150 dolárov a 5 kWh | PODĽA KOMUNITY | [Správa Wagtailu](https://wagtail.org/blog/one-month-on-glm-53-flash/) | žiadne; merania autora |
| Kapacita poskytovateľov si vynútila prechod na iné modely | PODĽA KOMUNITY | [Správa Wagtailu](https://wagtail.org/blog/one-month-on-glm-53-flash/) | žiadne; diagnóza autora |
| GLM 5.3 Flash bol užitočný pri viacerých úlohách Wagtailu | NÁZOR | [Správa Wagtailu](https://wagtail.org/blog/one-month-on-glm-53-flash/) | hodnotenie jedného praktika |
| Model, náklady, energiu a výsledok treba merať spoločne | ANALÝZA | [Správa Wagtailu](https://wagtail.org/blog/one-month-on-glm-53-flash/) | úsudok z opísaných zlyhaní |
