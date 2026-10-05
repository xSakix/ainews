+++
title = "bilibili rozširuje Index-Translate o lokálne verzie"
slug = "bilibili-rozsiruje-index-translate-o-lokalne-verzie"
description = "Otvorená rodina prekladačov má po novom balíky GGUF, FP8 a NVFP4, bezplatné kompatibilné API a štyri verejné benchmarky. Výsledky výkonu zostávajú vlastnými údajmi vývojára."
tags = ["models", "tools"]
date = 2026-10-05T04:01:30+02:00
draft = false
+++

bilibili pridalo 3. a 4. októbra k Index-Translate oficiálne kvantizované verzie, bezplatné verejné rozhranie a štyri hodnotiace súbory. Z nedávno vydaných prekladových modelov tak vznikol praktickejší balík na lokálne aj hostované použitie.

Rodina prekladá text v 150 jazykoch a prijíma pokyny týkajúce sa terminológie, formátovania a štýlu. Bežné textové modely majú 2 miliardy, 9 miliárd a v prípade ukážkovej verzie 35 miliárd parametrov. Najväčší z nich používa architektúru mixture of experts a pri každom tokene aktivuje približne 3 miliardy parametrov.

Pre lokálnych používateľov je najdôležitejšou zmenou spôsob distribúcie. Verzie GGUF sú určené pre llama.cpp, zostavenia FP8 pre vLLM a NVFP4 pre novšie GPU Blackwell. Projekt tieto formáty vydáva pre textové, slabične riadené aj dlhodokumentové modely. Kvantizované balíky majú aj rečové modely, hoci ich repozitáre GGUF obsahujú iba textový základ modelu, nie celý rečový systém.

Nové hostované koncové rozhranie sprístupňuje ukážkový model 35B-A3B cez rozhranie kompatibilné s chatovým API OpenAI. Vývojári si ho tak môžu vyskúšať bez toho, aby najprv zabezpečili vhodný hardvér. Repozitár označuje službu za bezplatnú, ale nesľubuje úroveň služieb ani dlhodobú cenovú politiku.

Index-Translate nie je iba prekladač viet. Klient dokáže zachovať štruktúru JSON a markdownu, vynútiť slovník pojmov a vyžiadať konkrétny tón. Súvisiace balíky prekladajú reč, snažia sa dodržať požadovaný počet slabík pri dabingu alebo prenášajú kontext naprieč dlhým dokumentom. Riešia tak nepríjemné časti produkčného prekladu, ktoré bežný prompt „prelož toto“ zvykne vynechať.

bilibili vydalo aj materiály benchmarkov instTrans, MEME, SandGlass a NativeLong spolu s hodnotiacimi skriptmi. Návrh testov sa tým dá preskúmať, zverejnené skóre však zostávajú vlastnými meraniami vývojára. Ukážkový model dosahuje podľa technickej správy skóre 0,8794 vo FLORES COMET-22 a 76,76 pri hodnotení WMT26. V druhom prípade je hodnotiteľom GPT-5.6-Sol, preto výsledok nemožno čítať ako nezávislé porovnanie od ľudí.

Pôvodná rodina modelov vyšla 30. septembra, nejde teda o uvedenie nového základného modelu. Novinkou je, že za štyri dni pribudli formáty na nasadenie, testovacie rozhranie a hodnotiace artefakty potrebné na prechod od oznámenia modelu k nástroju, ktorý si vývojári môžu reálne vyskúšať.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
| --- | --- | --- | --- |
| Verejné API a štyri benchmarky vyšli 4. októbra; kvantizované zostavenia 3. októbra | OVERENÉ | [Repozitár projektu](https://github.com/bilibili/Index-Translate) | žiadne |
| Textové modely pokrývajú 150 jazykov a podporujú obmedzenia terminológie, formátu a štýlu | OVERENÉ | [Repozitár projektu](https://github.com/bilibili/Index-Translate) | [Karta modelu](https://huggingface.co/IndexTeam/Index-Translate-35B-A3B-preview) |
| Balíky GGUF, FP8 a NVFP4 a ich zdokumentované cieľové prostredia | OVERENÉ | [Repozitár projektu](https://github.com/bilibili/Index-Translate) | odkazy na jednotlivé balíky sú uvedené v repozitári |
| Ukážkový model má celkovo 35 miliárd a približne 3 miliardy aktívnych parametrov | OVERENÉ | [Karta modelu](https://huggingface.co/IndexTeam/Index-Translate-35B-A3B-preview) | žiadne |
| FLORES COMET-22 0,8794 a hodnotenie WMT26 76,76 | PODĽA SPOLOČNOSTI | [Technická správa](https://arxiv.org/abs/2609.40181) | žiadne; správa používa pri WMT26 ako hodnotiteľa GPT-5.6-Sol |
| Nové balíky uľahčujú vyskúšanie rodiny lokálne alebo cez hostované rozhranie | ANALÝZA | [Repozitár projektu](https://github.com/bilibili/Index-Translate) | Úsudok z vydaných artefaktov; trvácnosť služby nie je preukázaná |
