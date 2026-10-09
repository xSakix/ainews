+++
title = "LightOn vydáva LightOnOCR-3"
slug = "lighton-vydava-lightonocr-3"
description = "Rodina modelov s licenciou Apache 2.0 spája prepis, bloky rozloženia, opisy obrázkov a extrakciu grafov v modeloch, ktoré možno spustiť lokálne."
tags = ["models", "tools"]
date = 2026-10-09T04:04:06+02:00
draft = false
+++

Francúzska AI spoločnosť LightOn vydala LightOnOCR-3, rodinu modelov s otvorenými váhami na spracovanie dokumentov, ktoré dokážu v jednom kroku vrátiť text, štruktúru strany, opisy obrázkov aj údaje z grafov.

Rodina obsahuje verzie s 0,8 miliardy, 1 miliardou a 4 miliardami parametrov pod licenciou Apache 2.0. Prázdny prompt vytvorí bežný prepis; prompt `grounding` pridá označené oblasti so súradnicami, opíše obrázky a premení grafy na tabuľky HTML.

**Prečo na tom záleží:** Vývojár súkromného systému na spracovanie dokumentov môže tieto modely kontrolovať a spúšťať lokálne namiesto odosielania stránok do hostovanej služby alebo prepájania samostatných systémov pre OCR, detekciu rozloženia a extrakciu grafov.

LightOn zachoval pri modeli 1B predchádzajúcu architektúru, takže táto verzia je priamou aktualizáciou existujúcich nasadení LightOnOCR-2. Menšia a väčšia verzia používajú vizuálno-jazykovú architektúru Qwen3.5. LightOn zverejnil aj nástroje na konverziu a vizualizáciu, váhy modelov a skripty použité na reprodukciu výsledkov benchmarkov.

Najvýraznejší výsledok pochádza z vlastného testovania spoločnosti LightOn. Model 4B dosiahol v 512-stranovom benchmarku olmOCR skóre 86,3, teda o 1,3 bodu menej než Infinity Parser Pro s 35,1 miliardy parametrov a o pol bodu viac než ďalší model 4B, Chandra 2. Porovnanie je užitočné, pretože spoločnosť spúšťala modely v rovnakom prostredí, no stále ide o hodnotenie dodávateľa a normalizácia výstupu môže skóre OCR citeľne zmeniť.

Štruktúrovaný výstup modelu je zámerne kompaktný. LightOn uvádza, že verzie 0,8B a 4B vytvorili na rovnakých stranách o 9 % až 14 % menej tokenov než dva konkurenčné analyzátory, hoci zároveň vracali bloky aj opisy obrázkov. Pri rozlíšení, ktoré každý model používal v benchmarku, mala verzia 1B najnižšiu uvádzanú latenciu jednej strany: 2,7 sekundy na GPU NVIDIA H100.

Opis trénovania je na príspevok k vydaniu nezvyčajne podrobný. LightOn vysvetľuje, ako skombinoval viacero detektorov, odmietal nejednoznačné anotácie stránok a použil veľký vizuálny model na označenie obrázkov. Spoločnosť zároveň uvádza, že repozitár benchmarku obsahuje pravidlá následného spracovania, čo je dôležité, pretože ekvivalentné poznámky pod čiarou alebo vzorce môžu podľa formátovania dostať odlišné skóre editačnej vzdialenosti.

Všetky tri váhy, demo aj podporný kód sú už dostupné cez [príspevok spoločnosti LightOn k vydaniu](https://huggingface.co/blog/lightonai/lightonocr-3). Nezávislé testy budú musieť ukázať, ako spoľahlivo fungujú hodnoty z grafov a bloky na dokumentoch mimo hodnotiacich súborov spoločnosti LightOn.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| LightOn vydal tri verzie LightOnOCR-3 pod licenciou Apache 2.0 | OVERENÉ | [Príspevok k vydaniu](https://huggingface.co/blog/lightonai/lightonocr-3) | [Karta modelu 4B](https://huggingface.co/lightonai/LightOnOCR-3-4B) |
| Režim grounding vracia označené bloky, opisy obrázkov a tabuľky grafov | OVERENÉ | [Príspevok k vydaniu](https://huggingface.co/blog/lightonai/lightonocr-3) | žiadne |
| Model 1B zachováva predchádzajúcu architektúru; 0,8B a 4B používajú Qwen3.5 VLM | OVERENÉ | [Príspevok k vydaniu](https://huggingface.co/blog/lightonai/lightonocr-3) | žiadne |
| LightOn zverejnil váhy, nástroje a skripty na reprodukciu benchmarkov | OVERENÉ | [Príspevok k vydaniu](https://huggingface.co/blog/lightonai/lightonocr-3) | [Karta modelu 4B](https://huggingface.co/lightonai/LightOnOCR-3-4B) |
| Model 4B dosiahol v olmOCR-Bench skóre 86,3 | PODĽA SPOLOČNOSTI | [Príspevok k vydaniu](https://huggingface.co/blog/lightonai/lightonocr-3) | žiadne |
| Vybrané modely vytvorili o 9 % až 14 % menej tokenov než menovaní konkurenti | PODĽA SPOLOČNOSTI | [Príspevok k vydaniu](https://huggingface.co/blog/lightonai/lightonocr-3) | žiadne |
| Model 1B mal na H100 latenciu jednej strany 2,7 sekundy | PODĽA SPOLOČNOSTI | [Príspevok k vydaniu](https://huggingface.co/blog/lightonai/lightonocr-3) | žiadne |
