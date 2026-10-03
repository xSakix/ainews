+++
title = "Nvidia pridáva 64 GB DGX Spark pre lokálne modely"
slug = "nvidia-pridava-64-gb-dgx-spark-pre-lokalne-modely"
description = "Partnerské systémy začínajú na 4 999 dolároch od 23. októbra. Nvidia oznámila aj jednoduchšie spájanie počítačov, kým väčší Spark zdražel."
tags = ["hardware", "tools", "models"]
date = 2026-10-03T05:17:20+02:00
draft = false
+++

Nvidia oznámila 64 GB verziu svojho stolového AI počítača DGX Spark, dostupnú cez hardvérových partnerov od 23. októbra s cenou od 4 999 dolárov.

Menšia konfigurácia zachováva procesor GB10 Grace Blackwell a softvérový balík Nvidie, ale ponúka polovicu zjednotenej pamäte 128 GB modelu. Zjednotená pamäť umožňuje procesoru a grafickému hardvéru prístup k rovnakému priestoru, ktorý uchováva váhy modelu aj pracovné dáta.

**Prečo na tom záleží:** Vývojár prevádzkujúci súkromné modely lokálne získava ďalšiu možnosť kapacity a jednoduchší spôsob spojenia dvoch počítačov. Kompromis je konkrétny: menej pamäte obmedzuje, čo sa zmestí na jeden stolový počítač, aj keď samotný čip zostáva rovnaký.

The Register uvádza nezmenenú priepustnosť pamäte 273 GB za sekundu, 20-jadrový procesor Arm a sieťový komponent ConnectX-7. Informuje aj o zvýšení ceny 128 GB systému na 6 950 dolárov. Nová verzia je lacnejšia než tento aktuálny väčší model, hoci stojí viac než väčší systém pri pôvodnom uvedení.

Nvidia uvádza, že dva 64 GB počítače prepojené sieťou 200 GbE môžu združiť 128 GB pamäte. Jej Sync Cluster Assistant rozpozná pripojené zariadenia, skontroluje ich konfiguráciu a nastaví sieť. Združená pamäť sa týka prepojenej dvojice, nie kapacity jedného počítača.

Nvidia uvádza až 1,7-násobný výkon dvoch počítačov oproti jednému vo vlastnom teste Qwen 3.8 27B. Oznámenie tvrdí aj podporu modelov s najviac 100 miliardami parametrov na jednom počítači a 200 miliardami na dvojici bez podrobností o číselnej presnosti a kontexte, z ktorých tieto limity vychádzajú.

Medzi oznámenými partnermi Nvidie sú Acer, ASUS, Dell, Gigabyte, HP a MSI. Model Launcher je naplánovaný na koniec októbra s inštaláciou a nasadením Qwen 3.8 27B na jeden počítač alebo klaster a s konfiguráciou programátorského rozhrania OpenCode.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Nvidia oznámila 2. októbra partnerský 64 GB DGX Spark od 4 999 dolárov na 23. októbra, so zachovaním GB10 a DGX OS; uvádza šesť partnerov. | OVERENÉ | [Oznámenie Nvidie](https://blogs.nvidia.com/blog/local-ai-dgx-spark-64gb-sync/) | [The Register](https://www.theregister.com/systems/2026/10/02/nvidia-debuts-4999-dgx-spark-with-half-the-ram-and-storage-amid-memory-crunch/5300622) |
| Priepustnosť pamäte 273 GB/s, 20-jadrový Arm, sieť ConnectX-7; uvedená cena 128 GB modelu 6 950 dolárov je vyššia než pôvodných 3 999 dolárov. | ČIASTOČNE OVERENÉ | Priame spravodajstvo The Register vyššie | Nvidia potvrdzuje GB10 a ConnectX-7, ale oznámenie vynecháva cenu väčšieho modelu. |
| Dva 64 GB uzly združujú 128 GB cez 200 GbE; Sync nastavuje klaster. | PODĽA SPOLOČNOSTI | Oznámenie Nvidie vyššie | žiadne; dokumentácia opisuje schopnosť |
| Až 1,7-násobný výkon v teste Qwen 3.8 27B od Nvidie; deklarovaná kapacita modelov 100B/200B pre jeden/dva uzly. | PODĽA SPOLOČNOSTI | Oznámenie Nvidie vyššie | žiadne; oznámenie neuvádza presnosť ani kontext kapacitných limitov |
| Model Launcher je naplánovaný na koniec októbra, s nasadením Qwen 3.8 27B a konfiguráciou OpenCode. | OVERENÉ | Oznámený harmonogram Nvidie vyššie | žiadne; budúca dostupnosť |
| Nižšia kapacita mení, čo sa zmestí, kým prepojená dvojica je samostatná konfigurácia. | ANALÝZA | Zverejnené konfigurácie pamäte vyššie | žiadne |
