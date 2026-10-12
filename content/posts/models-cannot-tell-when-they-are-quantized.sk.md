+++
title = "Modely nevedia, že boli kvantizované"
slug = "modely-nevedia-ze-boli-kvantizovane"
description = "Preprint zistil, že modely z textového správania spoľahlivo neurčia vlastnú kvantizáciu. Vnútorné sondy rozpoznajú známe metódy, no neprenesú sa na neznámu."
tags = ["research", "models"]
date = 2026-10-12T04:00:37+02:00
draft = false
+++

Jazykové modely nevedeli spoľahlivo povedať, či boli ich váhy kvantizované, hoci natrénované sondy dokázali zo skrytých stavov získať stopy konkrétnej metódy.

Preprint skúma úzku formu sebapoznania modelu. Výskumníci skomprimovali modely niekoľkými metódami, priamo sa ich pýtali na ich stav a porovnávali výstupy s nekomprimovanými verziami. Potom na vnútorných aktiváciách natrénovali jednoduché klasifikátory, aby zistili, či zmena existuje bez toho, aby sa prejavila v odpovedi.

## Prečo je to dôležité {#why-it-matters}

Pre inžiniera, ktorý dostane hostovaný alebo prebalený model, je jeho vlastný opis slabou kontrolou integrity. Model môže fungovať so zmenenými číselnými váhami bez toho, aby rozdiel premenil na pravdivú výpoveď o nasadení.

Kvantizácia ukladá váhy s menším počtom bitov, takže model potrebuje menej pamäte a často beží rýchlejšie. Mení aritmetiku v celej sieti, no nemusí zanechať zjavný textový podpis. Autori uvádzajú, že priame odpovede aj bežné porovnania výstupov niesli takmer nulový spoľahlivý signál o kompresii.

Obraz sa zmenil pri skrytých stavoch. Lineárne sondy, teda malé klasifikátory trénované na vnútorných hodnotách, oddelili kvantizované behy a často určili použitú metódu. Sieť teda obsahuje rozpoznateľné stopy implementácie, hoci ich jazykové rozhranie neodhaľuje.

## Odtlačok nie je všeobecné sebapoznanie

Najsilnejšie obmedzenie ukázal test prenosu. Spoločný nízkohodnostný adaptér sa naučil čítať známe podpisy, no spoľahlivo nerozpoznal metódu vynechanú pri tréningu. Naučil sa odtlačky známych premien, nie všeobecný pojem zníženej číselnej presnosti.

To zužuje bezpečnostný záver. Prevádzkovateľ s prístupom k aktiváciám môže zostaviť detektor pre známe varianty nasadenia, no experiment neukazuje univerzálny detektor ľubovoľných zmien váh. Zákazník API navyše obyčajne skryté stavy nevidí.

Autori jav nazývajú anosognózia podľa klinického termínu pre neuvedomovanie si poruchy. Analógia je užitočná iba na úrovni správania: systém obsahuje dôkaz o zmene, no nesprávne o nej informuje. Práca nedokazuje vedomie ani klinický stav.

Kontrolovaný zásah je metodickou výhodou. Základný model a prompty môžu zostať rovnaké, kým sa mení iba reprezentácia váh, a výskumníci osobitne testujú odpoveď, vonkajšie správanie a vnútornú aktivitu. Rozsah zostáva obmedzený testovanými modelmi, presnosťami a sondami.

## Štúdia zistila aj ďalšie javy

Rôzne metódy zanechali odlíšiteľné vnútorné podpisy, čo môže pomôcť pri audite známeho súboru variantov. Textové výstupy sa menili primálo, takže kontrola iba zo vzoriek odpovedí nie je postačujúca.

Ďalšie testy musia zahŕňať neznáme kompresné nástroje a zámerné skrývanie. Autori ukázali čitateľné stopy známych premien, no vlastný výsledok s vynechanou metódou odhaľuje hranicu riešenia.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislá kontrola |
|---|---|---|---|
| Testované modely nevedeli spoľahlivo uviesť, či boli kvantizované | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2610.06174 | žiadna |
| Lineárne sondy získali zo skrytých stavov informáciu o konkrétnej metóde | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2610.06174 | žiadna |
| Spoločný adaptér sa spoľahlivo nepreniesol na neznámu kvantizačnú metódu | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2610.06174 | žiadna |
| Štúdia menila kvantizáciu a porovnávala textové správanie s aktiváciami | OVERENÉ | https://arxiv.org/abs/2610.06174 | žiadna |
| Práca nedokazuje vedomie ani klinickú anosognóziu | ANALÝZA | https://arxiv.org/abs/2610.06174 | žiadna |
