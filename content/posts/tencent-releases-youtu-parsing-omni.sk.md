+++
title = "Tencent vydal Youtu-Parsing-Omni"
slug = "tencent-vydal-youtu-parsing-omni"
description = "Model s 5 miliardami parametrov prevádza dokumenty, obrázky, zvuk a video do jedného štruktúrovaného formátu JSON. Tencent zverejnil váhy, kód aj technickú správu."
tags = ["models", "tools"]
date = 2026-10-10T04:02:41+02:00
draft = false
+++

Laboratórium Youtu spoločnosti Tencent vydalo model s 5 miliardami parametrov, ktorý spracúva šesť druhov médií do jedného štruktúrovaného formátu JSON.

Youtu-Parsing-Omni prijíma stránky dokumentov, prirodzené obrázky, grafy, geometrické obrazce, zvuk a video. Bez prepínania medzi samostatnými špecializovanými modelmi dokáže vrátiť text, tabuľky, vzorce, rámčeky rozloženia, časové značky, prepisy reči, titulky a opisy pohybu kamery.

## Prečo na tom záleží {#why-it-matters}

Vývojár, ktorý vytvára vyhľadávací systém alebo nástroj na spracovanie dokumentov, môže posielať zmiešané médiá cez jeden lokálny model a dostávať predvídateľnú schému. Znižuje sa tým integračná práca, ktorú si zvyčajne vyžaduje kombinácia optického rozpoznávania znakov, rozpoznávania reči a služieb na porozumenie videu.

Tencent zverejnil váhy pod vlastnou licenciou `youtu-parsing`, doplnok pre vLLM, príklady inferencie a technickú správu. Repozitár uvádza, že hodnotiaci kód pribudne neskôr, takže publikované výsledky benchmarkov zatiaľ nemožno zopakovať iba z vydaných materiálov.

Model používa spoločný enkóder pre obrázky, zvuk a video. Pri videu vybrané vrstvy umožňujú každému snímku venovať pozornosť zvuku z rovnakej časti klipu. Výstupná schéma pokrýva doslovné prvky, ako sú text a ohraničujúce rámčeky, aj vyššie výstupy, napríklad príbehy a správy.

Tencent uvádza skóre 96,96 v OmniDocBench 1.6, tesne nad TeleOCR so skóre 96,91 a PaddleOCR-VL-1.6 so skóre 96,34 v publikovanej tabuľke. V širšom OmniParsingBench firma uvádza priemer 75,08, za Gemini 3 Pro so skóre 77,44, ale pred ostatnými testovanými systémami s otvorenými váhami. Ide o merania tvorcu a porovnanie závisí od konfigurácie benchmarku v správe.

Tréningová metóda opakovane mení študentský model na vlastného učiteľa pre ďalšie kolo. Tokeny obsahu a tokeny štruktúry dostávajú odlišné porovnávacie signály, čo má zachovať obsah stránky aj vzťahy medzi jej prvkami.

## Čo sledovať

Nezávislé testy budú potrebovať sľúbený hodnotiaci kód. Komerční používatelia musia preskúmať aj vlastnú licenciu a nemali by predpokladať podmienky bežné pri niektorých modeloch s otvorenými váhami.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Tencent vydal Youtu-Parsing-Omni s 5 miliardami parametrov, váhami, príkladmi kódu a technickou správou | OVERENÉ | https://huggingface.co/tencent/Youtu-Parsing-Omni | https://github.com/TencentYoutuResearch/Youtu-Parsing-Omni |
| Model prijíma dokumenty, obrázky, grafy, geometriu, zvuk a video a vytvára jednu schému JSON | PODĽA SPOLOČNOSTI | https://huggingface.co/tencent/Youtu-Parsing-Omni | žiadne |
| Tencent uvádza 96,96 v OmniDocBench 1.6 a 75,08 v OmniParsingBench | PODĽA SPOLOČNOSTI | https://huggingface.co/tencent/Youtu-Parsing-Omni | žiadne |
| Vydanie používa vlastnú licenciu youtu-parsing a zatiaľ neobsahuje hodnotiaci kód | OVERENÉ | https://huggingface.co/tencent/Youtu-Parsing-Omni | https://github.com/TencentYoutuResearch/Youtu-Parsing-Omni |
