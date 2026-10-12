+++
title = "Cloudflare pridáva multimodálny Clef-omni"
slug = "cloudflare-pridava-multimodalny-clef-omni"
description = "Nový klasifikátor zachováva obrazové, zvukové a video vstupy Qwen3-Omni, no namiesto generovaného textu vracia typované odpovede. Cloudflare zároveň znížil cenu aj kontextové okno Clef-flash."
tags = ["models", "tools"]
date = 2026-10-12T04:02:37+02:00
draft = false
+++

Cloudflare vydal Clef-omni, multimodálny klasifikátor, ktorý prijíma text, obrázky, zvuk a video, no namiesto generovaného textu vracia typované odpovede.

Model rozširuje rodinu klasifikátorov Clef a jeho základom je Qwen3-Omni. Cloudflare tento základ zmrazil, natrénoval ľahké adaptéry a pridal hlavu, ktorá v jednom prechode priamo mapuje vstup na používateľom definovanú schému označení.

## Prečo je to dôležité {#why-it-matters}

Vývojárovi, ktorý triedi správy podpory, kontroluje fotografie výrobkov alebo smeruje krátke videá, ponúka Clef-omni jedno klasifikačné rozhranie pre viacero médií. Môže tým odstrániť samostatný krok prepisu či popisu, hoci Cloudflare nezverejnil nezávislé porovnanie celých takýchto reťazcov.

Cloudflare uvádza, že Clef-omni je 30-miliardový model typu mixture-of-experts, ktorý pri jednom vstupe aktivuje približne 3 miliardy parametrov. V meraniach spoločnosti na Workers AI trvala klasifikácia textu približne 130 milisekúnd, obrázka asi 150 milisekúnd a 21-sekundového videa so zvukom okolo 1,5 sekundy. Ide o merania dodávateľa a výsledky sa budú meniť podľa veľkosti vstupu, frontu a nasadenia.

Výsledky benchmarkov nie sú jednoznačne lepšie. V tabuľke Cloudflare vedie starší hustý Clef vo viacerých textových úlohách, zatiaľ čo Clef-omni ho tesne prekonáva na datasete BANKING77, 94,8 % oproti 94,2 %. Praktickým rozdielom nového modelu je šírka vstupov, nie všeobecne vyššia presnosť textu.

Cloudflare zmenil aj podmienky Clef-flash. Cenníková cena vstupu klesla z 0,09 na 0,038 dolára za milión tokenov, no kontextové okno sa zmenšilo zo 64 000 na 24 000 tokenov. Clef zostáva na 0,24 dolára a Clef-omni štartuje na 0,15 dolára.

Váhy Clef-omni sú dostupné na Hugging Face pod licenciou Apache 2.0. Karta modelu uvádza približne 35,3 miliardy parametrov a približne 64 GB pamäte BF16 na GPU triedy H200 pri súčasnom vlastnom načítavači. Cloudflare plánuje podporu SGLang, no termín neuviedol.

## Čo sledovať

Otvorené váhy už umožňujú nezávislé testy latencie, kalibrácie a presnosti. Podpora v bežnom serverovom nástroji bude dôležitá pre tímy, ktoré chcú model prevádzkovať mimo Workers AI bez údržby vlastného načítavača Cloudflare.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislá kontrola |
|---|---|---|---|
| Cloudflare vydal Clef-omni s textovým, obrazovým, zvukovým a video vstupom a typovaným klasifikačným výstupom | OVERENÉ | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ | https://huggingface.co/Cloudflare/clef-omni |
| Cloudflare uvádza približne 130 ms pre text, 150 ms pre obrázky a 1,5 s pre 21-sekundový audiovizuálny klip | PODĽA SPOLOČNOSTI | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ | žiadna |
| Tabuľka Cloudflare uvádza 94,8 % na BANKING77 pre Clef-omni a 94,2 % pre Clef | PODĽA SPOLOČNOSTI | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ | žiadna |
| Clef-flash teraz stojí 0,038 dolára za milión vstupných tokenov a má kontext 24 000 tokenov | OVERENÉ | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ | žiadna |
| Váhy pod Apache 2.0 a vlastný načítavač sú dostupné; podpora SGLang sa plánuje | OVERENÉ | https://huggingface.co/Cloudflare/clef-omni | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ |
