+++
title = "Malé kognitívne jadro čelí black-box modelom psychológie"
slug = "male-kognitivne-jadro-celi-black-box-modelom-psychologie"
description = "Dvaja výskumníci spojili niekoľko známych myšlienok o pamäti, kontexte a chybe predikcie do jedného modelu ľudského rozhodovania. CORE prekonal porovnateľné neurónové prediktory v 137 experimentoch a pritom ponechal svoje vnútorné operácie otvorené kontrole."
tags = ["research", "models"]
date = 2026-10-14T04:02:33+02:00
draft = false
+++

Predstavme si účastníčku, ktorá sedí sama v psychologickom laboratóriu. Objaví sa symbol, potom ďalší. Tipuje, za ktorými dverami je odmena, pamätá si posledné prekvapenie a pomaly mení stratégiu. Táto účastníčka je vymyslená, no každý malý úkon patrí do experimentálneho záznamu za novým modelom, ktorý sa pokúša vysvetliť milióny takýchto rozhodnutí bez ukrytia vysvetlenia v neurónovej sieti.

## Mnoho experimentov, jedno vysvetlenie

Marcel Binz a Eric Schulz z Institute for Human-Centered AI v Helmholtz Munich vytvorili COntextual Retrieval and Encoding, skrátene CORE. Ich preprint spája malú skupinu známych kognitívnych princípov do jedného výpočtového modelu a spoločne ho prispôsobuje na 7 036 442 ľudských rozhodnutí zo 137 experimentov a 80 452 experimentálnych relácií.

Ambícia presahuje predpovedanie jednej úlohy. Psychológia nahromadila vysvetlenia asociácie, chyby predikcie, hierarchickej reprezentácie, vyhľadávania v pamäti a zabúdania, často testované v oddelených experimentálnych tradíciách. CORE skúma, akú časť behaviorálneho záznamu tieto myšlienky vysvetlia, keď musia spolupracovať v jednom súbore mechanizmov.

Jeho štruktúru tvorí hierarchia epizodických pamätí. Zapisujú sa do nich chyby predikcie. Kontext určuje, čo sa zakóduje, ktoré pamäte sa vyhľadajú a ako slabnú. Tieto operácie sú vyjadrené ako komponenty s kontrolovateľnou rolou, nie ako neobmedzený sekvenčný model trénovaný iba na minimalizáciu chyby.

Autori porovnávajú CORE s transformerom zhodnej konfigurácie a s Centaur, foundation modelom ľudskej kognície od veľkého tímu vedeného Binzom. Centaur doladil jazykový model na Psych-101, datasete s viac než desiatimi miliónmi rozhodnutí v 160 experimentoch. Ukázal, že jeden veľký prediktívny systém môže zovšeobecniť naprieč príbehmi úloh, úpravami štruktúry aj neznámymi oblasťami. Zaplatil pritom bežnú cenu foundation modelov: predikcia získala šírku, ale naučený mechanizmus bolo ťažké vyjadriť ako psychologickú teóriu.

CORE tento kompromis obracia. V novej práci dosahuje nižšiu prediktívnu zápornú logaritmickú vierohodnosť než zhodný transformer, 262 572 oproti 329 043. Oproti Centaur je porovnanie 262 572 ku 389 151. CORE dosahuje lepší výsledok než transformer vo všetkých 62 štúdiách použitých na porovnanie na úrovni štúdie a lepší než Centaur v 47.

Tieto čísla neznamenajú, že CORE zachytil ľudskú myseľ. Porovnávajú predikcie v konkrétnom zostavenom korpuse experimentov. Ukazujú však, že interpretovateľný model nemusel obetovať prediktívny dosah iba preto, že jeho časti majú psychologický význam.

## Čo si model pamätá

Hierarchia je dôležitá, pretože rozhodnutie môže závisieť od udalostí na rôznych úrovniach. Nedávna chyba môže zmeniť nasledujúcu odpoveď. Séria súvisiacich pokusov môže vytvoriť lokálnu situáciu. Zmena experimentu môže znížiť relevantnosť staršej skúsenosti, aj keď zostáva uložená.

CORE tieto účinky spracúva kontextovo závislým kódovaním a vyhľadávaním. Chyby predikcie aktualizujú pamäť namiesto jednoduchej zmeny jednej hodnoty. Model dokáže vyhľadať epizódu, keď sa aktuálna situácia na ňu podobá, pričom zabúdanie oslabuje skúsenosť so vzďaľovaním kontextu.

Takýto návrh vytvára vnútorné stopy známe zo zavedených teórií. Autori uvádzajú znaky bayesovského učenia v latentných premenných CORE: aktualizácie reagujú na neistotu spôsobom spájaným s pravdepodobnostnou inferenciou. Nachádzajú aj znaky segmentácie udalostí, takže vnútorné usporiadanie modelu odráža hranice medzi situáciami namiesto jednotného spracovania celého prúdu.

Výsledok rozširuje výskumný program, ku ktorému rovnakí autori predtým pristupovali opačne. V roku 2023 Binz a Schulz ukázali, že jazykové modely doladené na psychologických experimentoch dokážu v dvoch rozhodovacích oblastiach prekonať tradičné kognitívne modely a nesú informácie o jednotlivých účastníkoch. Ich práca o meta-naučenej kognícii tvrdila, že učiace algoritmy môžu aproximovať bayesovsky optimálne správanie a pritom zohľadniť obmedzený výpočet aj iné realistické hranice.

Tieto systémy skúmali, ako ďaleko sa všeobecné strojové učenie priblíži k ľudskému správaniu. CORE skúma, ako ďaleko sa kompaktná psychologická teória priblíži prediktívnemu rozsahu strojového učenia. Oba smery sa teraz stretávajú na časti rovnakých dát.

## Reprodukcia efektov namiesto ich pomenovania

Predikcia je iba časť testu. Autori simulujú CORE v experimentálnych podmienkach a skúmajú, či reprodukuje behaviorálne efekty uvedené v štúdiách. Obnoví 75 % z nich.

Ide o prísnejšiu požiadavku než zhoda priemernej miery rozhodnutí. Efekt môže zahŕňať adaptáciu, skreslenie, poradie, neistotu alebo zmenu po kontextovej hranici. Jeho reprodukcia vyžaduje, aby sa správanie modelu pri zmene experimentálnej manipulácie posunulo príslušným smerom.

Chýbajúca štvrtina je rovnako dôležitá ako úspešné tri štvrtiny. Zjednotený model sa stáva vedecky užitočným, keď jeho zlyhania ukazujú neúplnosť navrhovaného jadra. Black-box prediktor môže absorbovať ďalší vzor bez vysvetlenia, ktorá teória sa zmenila. Interpretovateľný systém núti k jasnej voľbe: upraviť vyhľadávanie, pridať mechanizmus, zmeniť hierarchiu alebo prijať, že jav leží mimo vysvetlenia.

Šírka práce vytvára aj riziká. Experimenty sa líšia inštrukciami, formátmi odpovedí, populáciami účastníkov a analytickými konvenciami. Spoločné prispôsobenie môže zvýhodniť mechanizmy vysvetľujúce bežné štruktúry a vyhladiť nezvyčajné. Celková vierohodnosť môže zakryť slabé vysvetlenie malej, no dôležitej oblasti. Autori preto uvádzajú porovnania na úrovni štúdií a simulované efekty, nielen jedno agregované skóre.

CORE je navyše preprint. Tvrdenia, implementačné rozhodnutia a harmonizácia datasetov neprešli recenzným konaním. Korpus je na pomery experimentálnej psychológie veľký, no zostáva vybraným záznamom úloh, ktoré sa dajú spoločne reprezentovať a fitovať. Ľudský život mimo laboratória zahŕňa jazyk, spoločenské vzťahy, emócie a telesnú činnosť, ktoré nemožno stlačiť do siedmich miliónov diskrétnych rozhodnutí.

## Teória, ktorá sa môže mýliť

Hlavný prínos modelu môže byť metodický. Kognitívna veda si často musela vybrať medzi transparentným modelom jedného experimentálneho rámca a všeobecným prediktorom, ktorý málo vypovedá o mechanizme. CORE prináša dôkaz, že túto hranicu možno posunúť.

Neodstraňuje tým neurónové ani foundation modely. Centaur stanovuje silnú prediktívnu základnú líniu a dokáže zovšeobecňovať cez prirodzené jazykové opisy úloh. Kompaktný model môže takéto systémy používať ako konkurentov, generátory dát alebo nástroje objavovania. Dôležitý je typ tvrdenia, ktorý každý z nich podporuje. Prediktor ukazuje, že správanie sa dá predvídať. Kognitívna teória uvádza operácie, ktoré ho podľa nej vytvorili.

Keďže CORE tieto operácie uvádza, výskumníci do nich môžu zasahovať. Môžu odstrániť kontextové zabúdanie, sploštiť hierarchiu pamäte alebo zmeniť zápis chyby predikcie a následne určiť, ktoré experimenty zlyhajú. Môžu pridať navrhovaný princíp a testovať, či si zaslúži miesto v celom zázname, nie iba zlepší jednu vybranú úlohu.

Vráťme sa k vymyslenej účastníčke pred dvoma dverami. Jej ďalšiu voľbu môže predpovedať veľký nepriehľadný model alebo ju možno rekonštruovať cez spomienku na prekvapenia, usporiadanú kontextom a podliehajúcu zabúdaniu. Prvý môže mať pravdu. Druhý dáva vedcovi ešte niečo: presné vysvetlenie, ktoré môže ďalší experiment vyvrátiť.

## Použité zdroje

- Binz, M., Dasgupta, I., Jagadish, A., Botvinick, M., Wang, J. X., & Schulz, E. (2023). *Meta-Learned Models of Cognition*. https://arxiv.org/abs/2304.06729
- Binz, M., et al. (2024). *Centaur: a foundation model of human cognition*. https://arxiv.org/abs/2410.20268
- Binz, M., & Schulz, E. (2023). *Turning large language models into cognitive models*. https://arxiv.org/abs/2306.03917
- Binz, M., & Schulz, E. (2026). *A small cognitive core explains human behavior at scale*. https://arxiv.org/abs/2610.13603
