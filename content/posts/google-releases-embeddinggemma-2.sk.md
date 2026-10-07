+++
title = "Google vydáva EmbeddingGemma 2 na multimodálne vyhľadávanie"
slug = "google-vydava-embeddinggemma-2-na-multimodalne-vyhladavanie"
description = "Model Googlu na embeddingy so 740 miliónmi parametrov mapuje text, kód, obrázky, video a zvuk do jedného vektorového priestoru. Modulárne enkódery sú určené pre lokálne zariadenia."
tags = ["models", "tools"]
date = 2026-10-07T04:01:57+02:00
draft = false
+++

Google vydal EmbeddingGemma 2, model s otvorenými váhami so 740 miliónmi parametrov, ktorý umiestňuje text, kód, obrázky, snímky videa a zvuk do jedného spoločného priestoru embeddingov.

Váhy pod licenciou Apache-2.0 vyšli 6. októbra s podporou pre Transformers, sentence-transformers, llama.cpp, vLLM, Ollama, LM Studio, MLX a Transformers.js. Model je určený na vyhľadávanie a smerovanie, nie na tvorbu prózy: rôzne druhy vstupov mení na vektory, ktoré možno porovnávať podľa podobnosti.

## Prečo na tom záleží {#why-it-matters}

Vývojár, ktorý tvorí súkromné vyhľadávanie v telefóne alebo notebooku, môže teraz indexovať hlasovú poznámku a vyhľadať časť videa bez toho, aby najprv reťazil rozpoznávanie reči, opis obrázkov a samostatný textový model na embeddingy. Z lokálneho vyhľadávania tak mizne niekoľko častí, hoci praktická užitočnosť modelu stále závisí od vlastných dát a požadovanej latencie.

EmbeddingGemma 2 má modulárnu konštrukciu. Jej základ pre text a kód má 270 miliónov parametrov, obraz pridáva 170 miliónov a zvuk 300 miliónov. Všetky konfigurácie premietajú vstup do 768 rozmerov a trénovanie Matryoshka umožňuje aplikácii skrátiť vektory na 512, 256 alebo 128 rozmerov a znížiť nároky na úložisko.

Google uvádza, že kvantizované váhy iba pre text využívajú na Pixel 11 Pro približne 191 MB aktívnej pamäte RAM, pri úplnom modeli približne 567 MB. Kontext s 8 192 tokenmi podľa spôsobu balenia Googlu pojme až 5,5 minúty zvuku, 29 obrázkov alebo 58 snímok videa.

V hodnotení spoločnosti dosiahol MTEB Code skóre 78,68, kým prvý EmbeddingGemma mal 68,76. Google zároveň tvrdí, že medzi multimodálnymi modelmi na embeddingy s menej než miliardou parametrov dosahuje vedúcu kvalitu. Ide o merania z dňa vydania, nie nezávislé reprodukcie, a na porovnanie konkrétnej úlohy vyhľadávania je vhodnejšia karta modelu.

Model používa rovnaký tokenizér a konštrukciu zvukového enkódera ako Gemma 4, čo môže obmedziť duplicitné súčasti, keď model na embeddingy zásobuje lokálny generatívny model. Google zverejnil aj ukážkové aplikácie na vyhľadávanie médií a okamihov vo videu.

Ďalšie praktické dôkazy prinesú testy na zmiešaných súkromných zbierkach, kde je dôležitejšia presnosť vyhľadávania naprieč modalitami, čas indexovania a pamäť než jedno súhrnné skóre benchmarku.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
| --- | --- | --- | --- |
| Google vydal EmbeddingGemma 2 6. októbra 2026 | OVERENÉ | [Oznámenie Googlu](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) | [váhy a karta modelu](https://huggingface.co/google/embeddinggemma-2) |
| Model má 740 mil. parametrov a modulárne súčasti: 270 mil. pre text, 170 mil. pre obraz a 300 mil. pre zvuk | OVERENÉ | [Oznámenie Googlu](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) | karta modelu uvádza architektúru |
| Kvantizované váhy využívajú približne 191 MB aktívnej pamäte pre text a 567 MB pre celý model na Pixel 11 Pro | PODĽA SPOLOČNOSTI | [Oznámenie Googlu](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) | žiadne |
| MTEB Code sa zlepšil zo 68,76 na 78,68 | PODĽA SPOLOČNOSTI | [Oznámenie Googlu](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) | žiadne |
| Váhy pod licenciou Apache-2.0 sú dostupné | OVERENÉ | [Repozitár modelu](https://huggingface.co/google/embeddinggemma-2) | repozitár je dostupný |
