+++
title = "llama.cpp pridáva lokálne rozhodovanie s pravdepodobnosťami"
slug = "llama-cpp-pridava-lokalne-rozhodovanie-s-pravdepodobnostami"
description = "Nový endpoint System One hodnotí zadané možnosti v jednom prechode modelom. Päť rodín konvertovaných modelov umožňuje lokálne nasadenie."
tags = ["models", "tools", "agents"]
date = 2026-10-03T05:21:20+02:00
draft = false
+++

llama.cpp, open-source nástroj na lokálnu inferenciu, pridal 2. októbra endpoint, cez ktorý rozhodovacie modely vracajú pravdepodobnosti vopred určených odpovedí namiesto generovania textovej odpovede.

Správcovia projektu Xuan-Son Nguyen a Victor Mustar z ggml-org opisujú požiadavku obsahujúcu informácie na posúdenie a súbor otázok s určeným typom. Server tieto informácie spracuje modelom a vráti hodnoty, ktoré aplikácia môže priamo použiť.

**Prečo na tom záleží:** Vývojár, ktorý smeruje požiadavky zákazníckej podpory, môže rozhodovanie spustiť lokálne a dostať určenú odpoveď s jej pravdepodobnosťou na rovnakom serveri, ktorý už prevádzkuje ďalšie modely. Možnosti zadáva aplikácia namiesto toho, aby ich získavala z odseku.

[Nový endpoint](https://huggingface.co/blog/ggml-org/decision-models-in-llamacpp), `/v1/systemone`, používa formát zavedený rozhodovacím modelom Jev od spoločnosti TypeSafe. Otázky s výberom vracajú víťaznú možnosť a pravdepodobnosti všetkých možností; otázky so skóre vracajú očakávanú úroveň na usporiadanej škále; otázky áno/nie vracajú pravdepodobnosť odpovede áno. Implementácia bola začlenená do projektu 2. októbra.

Prvé vydanie podporuje päť rodín modelov, od Julia-1 so 144 miliónmi parametrov po OpenJev s 27 miliardami parametrov. OpenJev prijíma aj obrázky. Kev-4B, lev a OpenJev dokážu opätovne použiť vstup pri odpovedaní na viacero otázok, zatiaľ čo režim smerovania načíta požadovaný model podľa potreby. [Implementácia servera](https://github.com/ggml-org/llama.cpp/pull/29818) pridáva rozhodovacie hlavy, metadáta konverzie a spracovanie požiadaviek k existujúcej infraštruktúre modelov.

Správcovia uvádzajú medián času odpovede od 3 do 43 milisekúnd pri piatich modeloch na jednej NVIDIA RTX PRO 6000. Ich príklady tiež ukazujú, prečo treba pravdepodobnosti interpretovať podľa konkrétneho modelu: rovnaká nejasná otázka o účte dostala mieru istoty 0,25 od Julia-1 a 0,80 od Kev-4B. Doplnenie opisov k samotným názvom odpovedí v ďalšom príklade zmenilo výsledok smerovania modelu Julia-1.

Váhy vo formáte GGUF sú dostupné v zbierke modelov projektu. [Karta Kev-4B](https://huggingface.co/ggml-org/Kev-4B-GGUF) uvádza licenciu Apache 2.0 a príkaz na lokálne spustenie. Správcovia označujú Clef od Cloudflare za ďalší model, ktorý plánujú pridať.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Nguyen a Mustar oznámili endpoint 2. októbra; tri typy otázok a štruktúra odpovedí sú zdokumentované. | OVERENÉ | [Článok správcov](https://huggingface.co/blog/ggml-org/decision-models-in-llamacpp) | žiadne |
| Implementácia bola začlenená 2. októbra a pridáva hlavy, metadáta konverzie a obsluhu servera; päť rodín, podpora obrázkov a opätovné použitie vstupu sú zdokumentované. | OVERENÉ | [Začlenená implementácia](https://github.com/ggml-org/llama.cpp/pull/29818) | žiadne |
| Julia-1 má 144M parametrov, OpenJev 27B; medián latencie je 3–43 ms na jednej RTX PRO 6000. Príklady miery istoty sú 0,25 a 0,80. | PODĽA SPOLOČNOSTI | [Merania správcov](https://huggingface.co/blog/ggml-org/decision-models-in-llamacpp) | žiadne |
| Lokálne hodnotenie poskytuje smerovacej aplikácii určené možnosti bez analýzy generovaného textu. | ANALÝZA | [Príklady požiadaviek a odpovedí](https://huggingface.co/blog/ggml-org/decision-models-in-llamacpp) | žiadne |
| Váhy Kev-4B GGUF používajú Apache 2.0 a obsahujú príkaz na spustenie; podpora Clef je plánovaná. | OVERENÉ | [Karta modelu](https://huggingface.co/ggml-org/Kev-4B-GGUF), [Plán](https://huggingface.co/blog/ggml-org/decision-models-in-llamacpp) | žiadne |
