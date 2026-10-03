+++
title = "Humanlike Chat pridáva lokálnemu chatovému modelu nástroje"
slug = "humanlike-chat-pridava-lokalnemu-chatovemu-modelu-nastroje"
description = "Verzia 2.0 používa dvoch učiteľov na zachovanie neformálneho dialógu a zlepšenie práce s pokynmi a nástrojmi. Vydanie obsahuje lokálne váhy aj pomenované kompromisy."
tags = ["models", "agents", "projects"]
date = 2026-10-03T09:42:58+02:00
draft = false
+++

LessThanThreeAI vydalo Humanlike Chat 2.0, lokálny jazykový model založený na Qwen, ktorý si má zachovať neformálny štýl správ a zároveň zvládať pokyny a volania nástrojov, ktoré prvej verzii chýbali.

Model s 27 miliardami parametrov je komunitnou úpravou zmeneného základu Qwen3.8, nie oficiálnym vydaním spoločnosti Alibaba. Jeho tvorca, vystupujúci ako codebottle, zverejňuje [kartu modelu a váhy na stiahnutie](https://huggingface.co/LessThanThreeAI/Qwen3.8-27B-Humanlike-Chat-GGUF) pod licenciou Apache-2.0 spolu s bezplatným rozhraním s obmedzenou frekvenciou požiadaviek.

**Prečo na tom záleží:** Vývojár lokálneho agenta môže preskúmať pokus spojiť konverzačný prejav a prácu s nástrojmi v jednom modeli. Vydanie poskytuje zlúčené kvantizované súbory aj adaptér a vlastné porovnania tvorcu so zmeneným základom ukazujú prínosy aj straty.

V tvorcovom teste ľudských správ má hodnotiaci model vybrať zo dvojice odpoveď skutočného človeka. Odpoveď nového modelu si pomýli s ľudskou približne v 24 % prípadov, oproti zhruba 15 % pri oficiálnom Qwen a menej než 1 % pri zmenenom základe. Ide o voľbu hodnotiaceho modelu v tomto teste, nie o meranie oklamaných ľudských používateľov.

Verzia 2.0 sa učí z vlastných vygenerovaných odpovedí. Jeden učiteľ hodnotí konverzačný štýl so skrytým pokynom; druhý učí pokyny, nástroje a kód pomocou samotného základného modelu. Študent skrytý pokyn pre štýl nikdy nedostáva, takže zamýšľaný prejav pretrváva bez jeho pridávania do každej používateľskej relácie.

Uvádzané skóre výberu nástrojov a dodržiavania pokynov sa oproti zmenenému základu zlepšuje, zatiaľ čo skóre všeobecných znalostí a programovania klesá. Tvorca opisuje aj obmedzené odmietanie požiadaviek zdedené zo základu. Tieto kompromisy sprevádzajú zlepšenie štýlu a nepodporujú všeobecné tvrdenie o prevahe nad oficiálnym Qwen.

Karta modelu ponúka približne 15 GB kvantizovaný súbor pre grafickú kartu s 24 GB pamäte a konfiguráciu llama.cpp, ktorá pre volania nástrojov zapína vlastnú chatovú šablónu modelu. Súbory si ponechávajú názvy z predchádzajúceho vydania, takže existujúci používatelia ich musia stiahnuť znova, aby získali verziu 2.0; nové súbory identifikujú zverejnené kontrolné súčty.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Verzia 2.0, tvorca codebottle/LessThanThreeAI, 27B zmenený základ Huihui Qwen3.8; Apache-2.0; dostupné GGUF, adaptér a rozhranie s limitom. | OVERENÉ | https://huggingface.co/LessThanThreeAI/Qwen3.8-27B-Humanlike-Chat-GGUF | žiadne |
| Voľba hodnotiteľa ishuman: 2.0 23,5 %, oficiálny Qwen 15,1 %, zmenený základ 0,3 %; nejde o test oklamania ľudských používateľov. | PODĽA SPOLOČNOSTI | https://huggingface.co/LessThanThreeAI/Qwen3.8-27B-Humanlike-Chat-GGUF | žiadne |
| On-policy distillation s dvoma učiteľmi: učiteľ štýlu má skrytý pokyn; samotný základný model pokrýva pokyny/nástroje/kód; študent skrytý pokyn nikdy nevidí. | OVERENÉ | https://huggingface.co/LessThanThreeAI/Qwen3.8-27B-Humanlike-Chat-GGUF | žiadne |
| IFBench 37,3→43,7, When2Call 48→58, BFCL irrelevance 60→78; MMLU-Pro 78,5→72,5, LiveCodeBench 56→51; zdedené obmedzené odmietanie. | PODĽA SPOLOČNOSTI | https://huggingface.co/LessThanThreeAI/Qwen3.8-27B-Humanlike-Chat-GGUF | žiadne |
| IQ4_XS 15,10 GB odporúčané pre 24 GB VRAM; --jinja zapína šablónu/volania nástrojov; nezmenené názvy vyžadujú nové stiahnutie; SHA256SUMS zverejnené. | OVERENÉ | https://huggingface.co/LessThanThreeAI/Qwen3.8-27B-Humanlike-Chat-GGUF | žiadne |
| Preskúmateľný kompromis lokálneho prejavu a nástrojov je relevantný pre vývojárov lokálnych agentov. | ANALÝZA | https://huggingface.co/LessThanThreeAI/Qwen3.8-27B-Humanlike-Chat-GGUF | žiadne |
