+++
title = "PyRUA-Lean znižuje počet volaní robotického agenta kódom"
slug = "pyrua-lean-znizuje-pocet-volani-robotickeho-agenta-kodom"
description = "Robotické rozhranie vykonáva kontroly a opakovania v Pythone pred návratom k jazykovému modelu. Autori uvádzajú vyššiu úspešnosť v simulácii a nižšiu spotrebu tokenov."
tags = ["research", "agents"]
date = 2026-10-03T05:47:20+02:00
draft = false
+++

PyRUA-Lean, rozhranie na ovládanie robota pomocou vykonateľného Pythonu, spotrebovalo o 65 % menej vstupných tokenov než volanie nástrojov v simulovaných úlohách dokončených oboma systémami a zároveň zvýšilo celkovú úspešnosť.

Ruiyang Si a kolegovia z Peking University, National University of Singapore, NVIDIE a Impossible Research zmenili spôsob, akým plánovač založený na jazykovom modeli ovláda existujúce robotické zručnosti. Plánovač píše krátke programy, ktoré zvládajú priebežné kontroly a opakovania skôr, než je potrebné ďalšie volanie modelu.

**Prečo na tom záleží:** Vývojár robotiky, ktorý platí za opakované pozorovania plánovača, môže presunúť rutinné vykonávanie do kódu. Štúdia meria tento kompromis pri zachovaní rovnakého plánovača aj robotických zručností, takže úsporu spája s rozhraním, nie so silnejším jazykovým modelom.

[Preprint](https://arxiv.org/abs/2610.01939), prvýkrát predložený 1. októbra, porovnáva PyRUA-Lean s agentom volajúcim nástroje pri použití rovnakého plánovača GPT-6 Astra. V 700 simulovaných prípadoch úloh sa podľa autorov úspešnosť zvýšila z približne 63 % na 72 %, teda o približne deväť percentuálnych bodov.

Percento v názve štúdie vyjadruje relatívny nárast. Úspora tokenov má iný menovateľ: iba prípady, ktoré vyriešili obaja agenti. Tieto dve skupiny treba odlišovať, pretože rýchly neúspešný pokus a efektívne dokončená úloha predstavujú rozdielne výsledky.

Volanie nástrojov vracia riadenie plánovaču po vykonaní operácie. Neskorší krok závislý od výsledku môže vyžadovať ďalšie volanie modelu a v konverzácii sa hromadia obrázky či priebežné výstupy. Každé volanie môže znovu spracúvať veľkú časť tohto rastúceho záznamu.

PyRUA-Lean namiesto toho udržiava trvalý stav Pythonu. Vygenerovaný kód môže spustiť pohyb, preskúmať jeho výsledok a zvoliť opakovanie pred vrátením riadenia. Do kontextu plánovača vstupujú iba výslovne vypísané výstupy a vyžiadané obrázky z kamier. Program funguje ako vedúci vykonávajúci dohodnutý postup, ktorý odborníka privolá až k rozhodnutiu vyžadujúcemu interpretáciu.

Rozhranie spája klasické robotické operácie a naučené politiky vision-language-action, ktoré premieňajú pozorovania na pohyby. Nenahrádza ich novými trénovanými robotickými zručnosťami. Obe strany porovnania používajú rovnaké základné implementácie a dostávajú rovnaké prevádzkové príručky tam, kde sú dostupné.

## Väčšinu úspory prináša menej volaní modelu

Hodnotenie zahŕňa tri súbory robotických benchmarkov: LIBERO-PRO, RoboTwin 2.0 a RoboCasa365. Pokrývajú manipulačné úlohy so zmenenými podmienkami, úlohy pre dve ramená a domáce úlohy. Každá úloha beží s piatimi inicializačnými parametrami prostredia, čím vznikajú spárované prípady pre oboch agentov.

Obaja plánovači majú rovnaké limity na volania jazykového modelu aj čas. Tieto limity počítajú volania plánovača, nie jednotlivé robotické operácie. Kód preto môže v rámci jedného volania vykonať viacero závislých operácií a zachovať väčšiu časť rozpočtu na neskoršie rozhodnutia.

V prípadoch vyriešených oboma systémami autori uvádzajú o 49 % menej volaní modelu spolu so 65 % poklesom kumulatívnych vstupných tokenov. Väčšinu úspory vysvetľuje menej volaní. Pomáha aj výber spätnej väzby, no štúdia hodnotí rozhranie ako celok, namiesto izolovania príspevku každej súčasti.

Prínos sa líši podľa úlohy. Úspory boli menšie pri jednoduchých úlohách RoboCasa365, kde naučená politika už zvláda veľkú časť práce a úvodný prompt tvorí veľký podiel vstupu. Rozsiahlejší opis rozhrania PyRUA-Lean tam čiastočne vyvažuje pokles opakovaných volaní.

Zlyhania navyše komplikujú porovnanie úspešnosti. Medzi prípadmi, ktoré vyriešil iba PyRUA-Lean, niektoré behy s volaním nástrojov vyčerpali rozpočet volaní, kým iné zlyhali ešte pred limitom. Druhá skupina zahŕňa obnovu pomocou skriptu, geometrické uvažovanie aj rozdiely v tom, či naučená robotická politika práve uspela.

Ide o vlastné výsledky autorov v preprinte zo simulácie, s jedným behom každého agenta na prípad a jednou rodinou plánovača. Správanie fyzických robotov a rozdiely medzi opakovanými behmi zostávajú mimo hodnotenia. [Repozitár kódu](https://github.com/DAGroup-PKU/PyRUA-Lean) tímu dopĺňa štúdiu; deklarovaným pokračovaním je meranie fyzického vykonávania a oneskorenia obnovy aj skúmanie opätovného použitia overených postupov medzi epizódami.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Uvedené afiliácie Siho a spolupracovníkov a predloženie v1 1. októbra 2026. | OVERENÉ | https://arxiv.org/abs/2610.01939 | žiadne |
| 700 spárovaných simulovaných prípadov; rovnaký GPT-6 Astra, operácie, politiky a rozpočty volaní/času; päť inicializačných parametrov na úlohu. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2610.01939 | žiadne |
| Úspešnosť 63,1 % až 71,7 %, +8,6 percentuálneho bodu alebo približne 14 % relatívne; spoločné úspešné epizódy používajú o 49 % menej volaní a o 65 % menej vstupných tokenov. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2610.01939 | žiadne |
| Python spája operácie/kontroly/opakovania v trvalom stave; do kontextu vstupujú iba vyžiadané obrázky a vypísaný výstup. | OVERENÉ | https://arxiv.org/abs/2610.01939 | žiadne |
| Tri súbory benchmarkov, menšie prínosy jednoduchých úloh, rozsiahlejší opis API, zmiešané vysvetlenia výlučných úspechov a obmedzenia štúdie. | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2610.01939 | žiadne |
| Kód je poskytnutý; fyzické oneskorenie/obnova a opakované použitie postupov medzi epizódami sa uvádzajú ako pokračovanie. | OVERENÉ | https://github.com/DAGroup-PKU/PyRUA-Lean ; https://arxiv.org/abs/2610.01939 | žiadne |
| Dôsledok pre vývojára a prirovnanie k vedúcemu vysvetľujú presun opakovaného vykonávania mimo volaní plánovača. | ANALÝZA | https://arxiv.org/abs/2610.01939 | žiadne |
