+++
title = "H2O.ai vydáva H2O-Lightning-31B"
slug = "h2oai-vydava-h2o-lightning-31b"
description = "Model s otvorenými váhami odpovedá na ohraničené otázky v jednom priechode a vracia pravdepodobnosti. Najsilnejšie údaje o rýchlosti a presnosti pochádzajú z vlastných testov H2O.ai."
tags = ["models", "tools"]
date = 2026-10-11T04:06:06+02:00
draft = false
+++

H2O.ai vydala H2O-Lightning-31B, model s otvorenými váhami určený na zodpovedanie ohraničených rozhodovacích otázok pomocou pravdepodobností namiesto tvorby voľného textu.

Model vychádza z Gemma 4 31B-it a prijíma text spolu s najviac štyrmi obrázkami. Jeho rozhranie podporuje výber z možností, otázky áno/nie a zoradené skóre, pričom v jednom priechode vráti jediný výsledok. H2O.ai zverejnila váhy, kartu modelu a obslužný kód na Hugging Face.

## Prečo na tom záleží {#why-it-matters}

Vývojárovi, ktorý veľký chatbot používa na smerovanie požiadaviek, hodnotenie záznamov alebo výber nástroja, môže obmedzený výstup odstrániť niekoľko krehkých krokov: zadanie požiadavky na JSON, jeho spracovanie, odmietanie chybných odpovedí a opakované dopytovanie. Pravdepodobnosť zároveň ukazuje, aké tesné bolo rozhodnutie, no je užitočná iba vtedy, keď je model kalibrovaný pre dané údaje.

H2O.ai uvádza, že model s 31 miliardami parametrov správne zodpovedal 212 z 231 verejných otázok JevBench. V hodnotení obrázkov dosiahol doladený model 88,4 % v 1 877 otázkach oproti 88,0 % pri nemennej základnej Gemma. Interval neistoty v karte modelu zahŕňa aj nulové zlepšenie, takže obrazový výsledok nepotvrdzuje spoľahlivý prínos oproti základu.

Spoločnosť tiež uvádza medián latencie približne 25 milisekúnd pri načítaní modelu vo formáte FP8 na jednej GPU NVIDIA H100. Údaj pochádza z jej vlastnej konfigurácie s vypnutým ukladaním prefixov do vyrovnávacej pamäte a karta neobsahuje meranie na menších GPU. Zverejnené súbory bfloat16 majú pred režijnými nákladmi behu približne 63 GB.

Vydanie funguje na neupravenom vLLM 0.30.0 za adaptérom `/v1/systemone` od H2O.ai. Dlhé záznamy sa nespracúvajú celé: vyhľadávacia vrstva ich pred inferenciou skráti na 3 000 tokenov. Táto hranica je dôležitá, pretože rozhodnutie môže zohľadniť iba dôkazy, ktoré vyhľadávanie zachová.

Váhy používajú licenciu Apache 2.0 spolu s podmienkami Google Gemma. Upozornenie H2O.ai výslovne odkazuje na zákaz použitia Gemma pri automatizovaných rozhodnutiach, ktoré ovplyvňujú práva jednotlivcov, takže otvorené súbory nepovoľujú každý typ nasadenia.

H2O.ai zároveň aktualizovala starší 4B model o revidované merania latencie a balík GGUF pre llama.cpp. Verzia 31B je už dostupná na stránke modelu Hugging Face; nezávislé testy latencie, kalibrácie a kvality úloh zatiaľ neboli zverejnené.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| H2O.ai vydala H2O-Lightning-31B s váhami, kartou modelu a obslužným kódom | OVERENÉ | https://huggingface.co/h2oai/h2o-lightning-31b | žiadne |
| Model podporuje ohraničené rozhodovanie nad textom a obrázkami a vracia pravdepodobnosti v jednom priechode | OVERENÉ | https://huggingface.co/h2oai/h2o-lightning-31b | žiadne |
| Dosiahol 212 z 231 položiek JevBench a medián latencie približne 25 ms na jednej H100 | PODĽA SPOLOČNOSTI | https://huggingface.co/h2oai/h2o-lightning-31b | žiadne |
| Obrazové hodnotenie nepreukázalo štatisticky spoľahlivé zlepšenie oproti nemennej základnej Gemma | OVERENÉ | https://huggingface.co/h2oai/h2o-lightning-31b | žiadne |
| Podmienky Gemma obmedzujú automatizované rozhodnutia ovplyvňujúce práva jednotlivcov | OVERENÉ | https://huggingface.co/h2oai/h2o-lightning-31b | žiadne |
