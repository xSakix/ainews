+++
title = "Liquid AI otvára váhy rozhodovacích modelov d1"
slug = "liquid-ai-otvara-vahy-rozhodovacich-modelov-d1"
description = "Model d1-3B s 3,1 miliardy parametrov a experimentálny d1-omni so 600 miliónmi parametrov odpovedajú na štruktúrované otázky v jednom priechode a ponúkajú váhy na lokálne nasadenie."
tags = ["models", "projects"]
date = 2026-10-08T03:58:31+02:00
draft = false
+++

Liquid AI zverejnil 7. októbra otvorené váhy dvoch modelov d1, čím po úvodnej dostupnosti iba cez API prináša svoj rýchly systém štruktúrovaného rozhodovania na lokálne zariadenia.

Modely odpovedajú na otázky áno alebo nie, otázky s výberom možností a bodované otázky v jednom priechode namiesto generovania postupnosti tokenov. Model d1-3B s 3,1 miliardy parametrov prijíma text a obrázky; experimentálny d1-omni-600M prijíma text spolu s obrázkami alebo s najviac 30 sekundami zvuku.

Tento návrh dáva vývojárom kompaktný komponent na smerovanie, moderovanie, klasifikáciu či radenie v prípadoch, keď netreba voľne formulovanú odpoveď. Jeden vstupný stav môže obsahovať viacero pomenovaných otázok a model vráti zodpovedajúce rozhodnutia naraz, čím sa vyhne latencii a premenlivým formuláciám pri generovaní tokenov.

Liquid uvádza, že d1-3B odpovedal na jednu otázku za 8 milisekúnd na RTX 4090, za 30 milisekúnd na Apple M5 Pro a za 50 milisekúnd na Jetson Orin Nano. Ide o vlastné merania spoločnosti. Jej zverejnená tabuľka zároveň uvádza pre d1-3B priemerné skóre 82,9 v siedmich verejných textových datasetoch, zatiaľ čo menší model dosiahol 78,4.

Obe vydania sú určené pre odlišný hardvér. d1-3B vychádza z dekóderového vizuálno-jazykového modelu spoločnosti Liquid a má kontextové okno 32 768 tokenov. d1-omni-600M spája obojsmerný textový enkóder so samostatnými obrazovými a zvukovými enkódermi a má kontextové okno 16 384 tokenov. Liquid označuje menší model za rané výskumné vydanie a nezverejňuje preň merania latencie.

Oba repozitáre používajú licenciu LFM Open License namiesto štandardnej permisívnej softvérovej licencie. Načítanie modelov si v súčasnosti vyžaduje Transformers 5.14 alebo novší a spúšťa Python dodaný repozitárom cez `trust_remote_code=True`, preto je vhodné stiahnutý kód pred použitím skontrolovať.

Váhy, karty modelov a demo sú už dostupné na Hugging Face. Liquid poskytuje aj varianty GGUF a 8-bitové varianty váh a aktivácií, vďaka ktorým sa d1-3B ľahšie testuje na zariadeniach s obmedzenými zdrojmi, kým je jeho rozhodovacie API ešte nové.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Liquid AI vydal váhy d1-3B a d1-omni-600M 7. októbra 2026 | OVERENÉ | [Vydanie Liquid AI](https://huggingface.co/blog/LiquidAI/open-d1) | [Karta modelu d1-3B](https://huggingface.co/LiquidAI/d1-3B) |
| Modely d1 odpovedajú na štruktúrované otázky v jednom priechode bez generovania výstupných tokenov | OVERENÉ | [Vydanie Liquid AI](https://huggingface.co/blog/LiquidAI/open-d1) | žiadne |
| d1-3B prijíma text a obrázky; d1-omni-600M prijíma text s obrázkami alebo zvukom | OVERENÉ | [Vydanie Liquid AI](https://huggingface.co/blog/LiquidAI/open-d1) | [Karta modelu d1-omni-600M](https://huggingface.co/LiquidAI/d1-omni-600M) |
| Liquid uvádza 8 ms na RTX 4090, 30 ms na Apple M5 Pro a 50 ms na Jetson Orin Nano | PODĽA SPOLOČNOSTI | [Vydanie Liquid AI](https://huggingface.co/blog/LiquidAI/open-d1) | žiadne |
| Liquid uvádza priemerné skóre textových benchmarkov 82,9 pre d1-3B a 78,4 pre d1-omni-600M | PODĽA SPOLOČNOSTI | [Vydanie Liquid AI](https://huggingface.co/blog/LiquidAI/open-d1) | žiadne |
| Načítanie vyžaduje Transformers 5.14 alebo novší a `trust_remote_code=True` | OVERENÉ | [Vydanie Liquid AI](https://huggingface.co/blog/LiquidAI/open-d1) | [Karta modelu d1-3B](https://huggingface.co/LiquidAI/d1-3B) |
