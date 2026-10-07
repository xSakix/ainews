+++
title = "Mistral predstavuje Large 4 pred vydaním váh"
slug = "mistral-predstavuje-large-4-pred-vydanim-vah"
description = "Mistral sprístupnil cez API svoj multimodálny model s biliónom parametrov a na 27. októbra naplánoval vydanie otvorených váh. Architektúra a benchmarky zatiaľ zostávajú predbežné."
tags = ["models", "business"]
date = 2026-10-07T04:00:57+02:00
draft = false
+++

Mistral sprístupnil verejnú ukážku modelu Mistral Large 4 cez API a vydanie stiahnuteľných váh naplánoval na 27. októbra.

Francúzska spoločnosť model opisuje ako multimodálnu zmes expertov trénovanú od začiatku vo vlastných európskych dátových centrách. Prijíma text aj obrázky, podporuje viac než 160 jazykov a má kontextové okno s miliónom tokenov.

## Prečo na tom záleží {#why-it-matters}

Organizácia, ktorá zvažuje vlastné nasadenie európskeho modelu, môže Large 4 testovať už teraz, zatiaľ však nemôže preskúmať ani nasadiť prisľúbené váhy. Ide preto o ukážku s konkrétnym termínom dodania, nie o dokončené vydanie modelu s otvorenými váhami.

Oznámenie Mistralu uvádza bilión parametrov celkovo a 49 miliárd aktívnych pre každý token. Dokumentácia uvádza 1,05 bilióna celkovo, 52 miliárd aktívnych a obrazový enkóder s 1,6 miliardy parametrov. Rozdiel môže vzniknúť zaokrúhlením alebo zmenou konfigurácie, Mistral však nezverejnil technickú správu, ktorá by čísla zosúladila.

Spoločnosť zdôrazňuje kybernetickú bezpečnosť. Uvádza 82 % v časti reproduce-then-patch benchmarku CyberGym-E2E, 93 % v Cybench a 61,7 % v DeepSWE v1.1. Niektoré hodnotenia pomenúvajú externých poskytovateľov, súhrnné porovnanie a väčšina hlavných tvrdení sú však v materiáloch Mistralu.

Pred vydaním váh majú podľa Mistralu verziu s obmedzenejšou moderáciou testovať kybernetickí odborníci a verejné orgány. Spoločnosť tvrdí, že bežné bezpečnostné odmietnutia môžu potláčať obrannú prácu, a ukážka má tento kompromis preskúmať.

Cena API sa začína na 1,36 dolára za milión vstupných tokenov a 4,18 dolára za milión výstupných tokenov. Režimy s uvažovaním aj bez neho sú dostupné cez Mistral Studio, kým licencia a konečné požiadavky na nasadenie zostanú neznáme do vydania váh.

Rozhodujúcim dňom bude 27. október. Karta modelu, technická správa, licencia a stiahnuteľné súbory ukážu, či verejný artefakt zodpovedá rozsahu a schopnostiam ukážky.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
| --- | --- | --- | --- |
| Mistral spustil ukážku Large 4 cez API a vydanie váh naplánoval na 27. októbra | OVERENÉ | [Oznámenie Mistralu](https://mistral.ai/news/mistral-large-4/) | [dokumentácia Mistralu](https://docs.mistral.ai/models/mistral-large-4) |
| Oznámenie uvádza 1 bilión parametrov celkovo a 49 mld. aktívnych | OVERENÉ | [Oznámenie Mistralu](https://mistral.ai/news/mistral-large-4/) | dokumentácia uvádza odlišné hodnoty |
| Dokumentácia uvádza 1,05 bilióna parametrov celkovo, 52 mld. aktívnych a 1,6-miliardový obrazový enkóder | OVERENÉ | [Dokumentácia Mistralu](https://docs.mistral.ai/models/mistral-large-4) | žiadne |
| Model dosiahol 82 % v CyberGym-E2E reproduce-then-patch, 93 % v Cybench a 61,7 % v DeepSWE v1.1 | PODĽA SPOLOČNOSTI | [Oznámenie Mistralu](https://mistral.ai/news/mistral-large-4/) | pomenovaní hodnotitelia nezávisle nepotvrdzujú celé porovnanie |
| Cena API je 1,36 dolára za vstup a 4,18 dolára za výstup na milión tokenov | OVERENÉ | [Dokumentácia Mistralu](https://docs.mistral.ai/models/mistral-large-4) | živá dokumentácia |
