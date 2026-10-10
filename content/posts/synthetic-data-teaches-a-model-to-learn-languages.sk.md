+++
title = "Syntetické dáta učia model učiť sa jazyky"
slug = "synteticke-data-ucia-model-ucit-sa-jazyky"
description = "Transformer s 300 miliónmi parametrov, trénovaný bez prirodzeného jazyka, sa v kontextovom okne prispôsobuje šiestim skutočným jazykom. Experiment oddeľuje stratégiu učenia od zapamätaného textu."
tags = ["research", "models"]
date = 2026-10-10T04:00:41+02:00
draft = false
+++

Transformer trénovaný iba na syntetických sekvenciách sa naučil predpovedať šesť skutočných jazykov z kontextu bez zmeny váh či prirodzeného jazyka v tréningu.

Lennart Carstens-Behrens a Holger Fröhlich vytvorili Prior-Fitted Language Model, čiže PFLM, s 300 miliónmi parametrov na úrovni bajtov. Každá tréningová sekvencia pochádzala z novo vzorkovaného kauzálneho procesu s vlastnými pravidlami, čo nútilo model odvodiť aktuálnu sekvenciu namiesto zapamätania opakujúceho sa syntetického jazyka.

## Prečo na tom záleží {#why-it-matters}

Výskumník učenia v kontexte zriedka vie, či sa model učí nové pravidlo, alebo si vybavuje niečo podobné tréningovým dátam. PFLM vytvára čistejšie oddelenie: jeho nemenné váhy obsahujú všeobecnú stratégiu naučenú z umelých procesov, zatiaľ čo skutočný jazyk prichádza až v prompte.

Syntetický generátor bol navrhnutý tak, aby reprodukoval všeobecné štatistické vlastnosti prirodzeného textu vrátane častých symbolov, závislostí na veľkú vzdialenosť a pomaly sa zlepšujúcej predvídateľnosti. Neobsahoval slová, gramatiku ani príklady z Wikipédie. Úlohou modelu počas predtrénovania bolo jednoducho predpovedať ďalší bajt v sekvencii zakaždým z iného generátora.

Keď autori poskytli dlhé prúdy Wikipédie v angličtine, čínštine, hindčine, arabčine, japončine a kórejčine, predikcia sa v priebehu kontextu zlepšovala. Strata začínala blízko rovnomernej základnej hodnoty ôsmich bitov na bajt a po milióne bajtov klesla podľa jazyka na 0,9 až 2,4. Váhy modelu zostali nemenné.

## Experiment testuje adaptáciu, nie plynulosť

PFLM nevytvára uhladenú prózu ani nepreukazuje porozumenie významu. Odhaduje, ktorý bajt nasleduje po pozorovaní dostatočne dlhej časti neznámeho zdroja. Aj táto užšia schopnosť je podstatná, pretože ukazuje, že sekvenčný model si môže osvojiť užitočný adaptačný postup bez predchádzajúceho spracovania prirodzeného jazyka.

Model číta surové bajty namiesto pevného slovníka častí slov. Tým sa odstraňuje tokenizér trénovaný na ľudskom texte ako ďalšia možná cesta, ktorou by mohla do systému preniknúť jazyková štruktúra. Verejný repozitár poskytuje integráciu modelu a API na hodnotenie prúdov; vydané váhy umožňujú testovať nové domény.

Autori porovnali PFLM aj s klasickými všeobecnými kompresnými metódami. Uvádzajú, že po dostatočne dlhom kontexte skomprimoval šesť netextových zdrojov vrátane zdrojového kódu a rečových dát lepšie než gzip a PPMd. Kompresia je priamym testom predikcie: model s lepšími pravdepodobnosťami potrebuje na zápis rovnakých dát menej bitov.

### Štúdia ďalej zistila

Pri prúdoch číslic sa PFLM v kontexte naučil približné sčítanie, počítanie a porovnávanie veľkostí. Predpovedal deterministické sekvencie vrátane indikátorov prvočísel a Rudinových-Shapirových vzorov. Jazykové výsledky sa medzi šiestimi jazykmi Wikipédie výrazne líšili, čo ponecháva jasný rozdiel medzi adaptáciou a výkonom modelov trénovaných priamo na texte.

Práca je preprint a hlavný výsledok pochádza z jedného systému s 300 miliónmi parametrov postaveného na jednom syntetickom rozdelení. Generátor zámerne zdieľa všeobecné štatistiky s prirodzenými dátami, takže experiment neukazuje, že ľubovoľné syntetické kurikulum vytvorí učenie jazyka. Ukazuje, že starostlivo zvolená štrukturálna rozmanitosť môže natrénovať opakovane použiteľný postup učenia.

Kód a váhy sú verejné, takže bezprostredný test je priamočiary: použiť nemenný model na skutočne nové štruktúrované zdroje a merať, kedy jeho zlepšenie z kontextu vydrží alebo zlyhá.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| PFLM je bajtový transformer s 300 miliónmi parametrov trénovaný iba na syntetických nejazykových sekvenciách | OVERENÉ | https://arxiv.org/abs/2610.05879 | https://github.com/cbl/prior-fitted-language-model |
| Strata predikcie po milióne bajtov klesla na 0,9–2,4 bitu na bajt v šiestich jazykoch Wikipédie | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2610.05879 | žiadne |
| Model sa v kontexte naučil číselné a deterministické sekvencie a prekonal gzip a PPMd v šiestich netextových doménach | PODĽA SPOLOČNOSTI | https://arxiv.org/abs/2610.05879 | žiadne |
| Kód a váhy modelu sú verejne dostupné | OVERENÉ | https://github.com/cbl/prior-fitted-language-model | https://huggingface.co/lennartcb/pflm1 |
| Výsledok oddeľuje naučenú adaptačnú stratégiu od zapamätaného prirodzeného textu | ANALÝZA | https://arxiv.org/abs/2610.05879 | žiadne |
