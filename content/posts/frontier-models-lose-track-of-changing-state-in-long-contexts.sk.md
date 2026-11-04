+++
title = "Hraničné modely strácajú prehľad o meniacom sa stave"
slug = "hranicne-modely-stracaju-prehlad-o-meniacom-stave"
description = "StateBench testuje, či modely dokážu udržať meniaci sa stav sveta počas desiatok tisíc aktualizácií. Hraničné systémy zlyhali pri vzájomne závislých zmenách, zatiaľ čo malé rekurentné a hybridné modely sa priamo naučili tri jednoduchšie úrovne."
tags = ["research", "models"]
date = 2026-11-04T05:12:00+01:00
draft = false
+++

Táto scéna je hypotetická. O 02:14 požiada pohotovostný technik model, aby z dlhého záznamu nasadenia zrekonštruoval službu. Model tvrdí, že platobná služba stále smeruje na databázu blue. O deväťdesiat strán skôr však blue zdedila koncový bod databázy green, neskôr green zdedila koncový bod red a napokon sa znova zmenila red. Celý záznam sa zmestí do kontextového okna a odpoveď znie sebavedomo. Napriek tomu je nesprávna.

Toto vymyslené zlyhanie zachytáva rozdiel, na ktorom stojí StateBench, benchmark vydaný výskumníkmi z Allen Institute for AI. Model môže dokázať vyhľadať riadok v dlhom vstupe bez toho, aby udržiaval stav vytvorený každou aktualizáciou v danom vstupe. Dlhý kontext určuje, koľko materiálu systém prijme. Nezaručuje, že systém správne udrží meniacu sa sústavu vzťahov.

## Štyri úrovne meniaceho sa stavu

StateBench premieňa tento rozdiel na kontrolované úlohy. Každý príklad tvorí sekvencia priradení premenných a hodnôt. Výskumníci vytvoria kanonickú sekvenciu, vyjadria ju v rôznych povrchových podobách a pýtajú sa na konečný stav. Keďže základné priradenia môžu zostať rovnaké, hoci sa zmení formulácia, benchmark má merať výpočet, nie znalosť jedného spôsobu vyjadrenia.

Hierarchia má štyri úrovne. Najjednoduchšie nemenné priradenie pridelí premennej hodnotu iba raz. Neperiodické opätovné priradenie mení hodnotu premennej, no každá aktualizácia ju stále uvádza priamo. Riešiteľná sebareferencia podmieňuje aktualizáciu súčasnou hodnotou premennej. Všeobecné konečné priradenie je ťažšie, pretože premenné môžu dostať odkazy na iné premenné a jedna zmena sa tak môže šíriť reťazcom vzťahov.

Tieto úrovne oddeľujú vyhľadávanie od udržiavania stavu. Pri prvých dvoch môže stačiť nájsť najnovšie priame priradenie. Neskoršie úlohy vyžadujú, aby systém použil aktualizácie v správnom poradí a zachoval výsledok. Najťažšia úroveň sa podobá vymyslenému záznamu nasadenia. Na určenie významu jedného názvu môže byť potrebné zistiť, čo znamenali viaceré ďalšie názvy pri skorších zmenách.

## Hraničné modely prudko klesajú pri najťažších sekvenciách

Tím StateBench hodnotil uzavreté hraničné systémy vrátane Gemini 3.8 Flash, Claude Opus 5.5, GPT-6 Sol a GPT-6 Luna. Podľa článku a sprievodného technického príspevku Ai2 si modely dobre poradili s nemennými priradeniami a priamym opätovným priraďovaním. Ich výkon sa zhoršoval s rastúcou vzájomnou závislosťou aktualizácií a dĺžkou sekvencií.

Na najdlhších príkladoch všeobecného konečného priradenia dosiahol každý testovaný hraničný model najviac 13 %. Nie je to dôkaz, že systémy zabudnú každý dlhý dokument. Ukazuje to, že pri presných požiadavkách tohto benchmarku na sledovanie stavu nie je prijatie dlhej sekvencie to isté ako spoľahlivý výpočet jej konečného stavu.

Verejný repozitár robí test neobvykle dobre kontrolovateľným. Obsahuje generátory, hodnotiaci kód a konfigurácie pre logaritmicky rozložené dĺžky sekvencií až do 64 000 priradení. Rovnaké kanonické záznamy možno vyjadriť vo viacerých formátoch. Je to dôležité, pretože model by inak mohol využiť opakujúci sa vetný vzorec namiesto toho, aby sa naučil pravidlo aktualizácie.

## Malé rekurentné modely sa učia inak

Najprekvapivejší výsledok pochádza z modelov trénovaných priamo na tejto úlohe. Výskumníci trénovali systémy s 275 miliónmi parametrov na príkladoch s najviac 256 priradeniami a potom ich testovali na sekvenciách dlhých až 64 000 priradení, teda 250-násobku trénovacej dĺžky.

Malé rekurentné modely Gated DeltaNet a hybridné modely, ktoré kombinujú rekurentné vrstvy s attention, zostali pri prvých troch úrovniach takmer bezchybné aj pri najdlhšej testovanej dĺžke. Porovnateľné transformery sa s dĺžkou sekvencie zhoršovali. Žiadna z priamo trénovaných architektúr nezvládla neobmedzené všeobecné konečné priradenie v celom rozsahu, hoci pružnejší variant Gated DeltaNet zostal pri najťažšej úlohe takmer bezchybný približne do desaťnásobku trénovacej dĺžky.

Neznamená to, že rekurencia jednoducho poráža attention. William Merrill, Jackson Petty a Ashish Sabharwal už v článku *The Illusion of State in State-Space Models* z roku 2024 ukázali, že bežné modely stavového priestoru majú dôležité teoretické obmedzenia sledovania stavu podobné transformerom. StateBench otázku spresňuje. Niektoré rekurentné mechanizmy sa môžu naučiť určité postupy aktualizácie a preniesť ich ďaleko za dĺžky, ktoré videli pri trénovaní. Bežné transformery to v tomto experimente nedokázali. Najťažšia forma zostáva nevyriešená.

Architektúra teda ovplyvňuje druh výpočtu, ktorý sa model môže naučiť, nielen jeho priemer v benchmarku alebo kontextový limit. Oveľa menšia špecializovaná súčasť môže udržiavať úzky stav spoľahlivejšie než hraničný jazykový model, ktorý má postup odvodiť z promptu. Výsledok podporuje jednu možnosť návrhu systému: kritický stav uchovávať v explicitnom softvéri alebo špecializovanom rekurentnom module a jazykový model nechať, aby ho interpretoval alebo vysvetlil.

## Čo benchmark nepotvrdzuje

StateBench je zámerne syntetický. Kontrolované priradenia umožňujú merať zlyhanie, no produkčné záznamy, kódové základne a spisy obsahujú nejednoznačnosti, nepodstatný materiál a nové entity. Súčasný benchmark používa pevný počet premenných; netestuje systém, ktorý musí pri čítaní vytvárať rastúcu množinu entít. Výskumníci tiež ponechávajú otvorenú otázku, kam umiestniť rekurentné vrstvy vo väčších hybridoch a ako numerická presnosť ovplyvňuje veľmi dlhé aktualizácie.

Porovnanie zachytáva konkrétne modely, prompty a dĺžky v jednom čase. Nízke skóre neukazuje, či by nasadenie napravili nástroje, externá pamäť, iný prompt alebo učenie s učiteľom. Ani úspech v benchmarku by nedokázal, že systém zvládne skutočný prevádzkový stav. Test izoluje jeden režim zlyhania dostatočne čisto na to, aby sa dal zopakovať.

Pre tímy, ktoré vytvárajú agentov, je to užitočné už teraz. Dlhé kontextové okno treba chápať ako vstupnú kapacitu, nie ako záruku databázy. Testy by mali obsahovať reťazce, v ktorých neskoršie fakty závisia od skorších zmien, nielen otázky s doslovnou odpoveďou vo vstupe. Ak by chyba spustila platbu, zmenu oprávnenia alebo úkon v produkcii, smerodajný stav by mal zostať explicitný a auditovateľný.

Vráťme sa k vymyslenému technikovi o 02:14. Bezpečnejší systém nežiada jeden model, aby si pamätal, kam napokon smeruje ktorá farba databázy. Vypočíta súčasné mapovanie, uloží každý prechod a požiada model, aby výsledok vysvetlil. Pager môže stále zazvoniť. Odpoveď však už nezávisí od toho, či dlhý kontext pravdu iba obsahuje, alebo ju skutočne udržiava aktuálnu.

## Použité zdroje

- Allen Institute for AI. [StateBench repository](https://github.com/allenai/state-bench). 2026.
- Allen Institute for AI. [StateBench: Evaluating State Tracking in Long Contexts](https://huggingface.co/blog/allenai/statebench). 2026.
- Merrill, William, Jackson Petty and Ashish Sabharwal. [The Illusion of State in State-Space Models](https://arxiv.org/abs/2404.08819). 2024, revised 2025.
- Petty, Jackson, William Merrill and Ashish Sabharwal. [StateBench: Evaluating State Tracking in Long Contexts](https://arxiv.org/abs/2611.03094). 2026.
