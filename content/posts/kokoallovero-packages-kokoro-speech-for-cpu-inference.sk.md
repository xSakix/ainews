+++
title = "Kokoallovero balí hlas Kokoro na inferenciu na CPU"
slug = "kokoallovero-bali-hlas-kokoro-na-inferenciu-na-cpu"
description = "Implementácia v C++ spája anglické nástroje výslovnosti s Kokoro-82M a na dvoch CPU Intel uvádza približne dvojnásobnú rýchlosť syntézy oproti PyTorchu."
tags = ["projects", "models", "tools"]
date = 2026-10-03T05:46:20+02:00
draft = false
+++

Kokoallovero, projekt syntézy reči v C++ od vývojára RobViren, balí hlasový model Kokoro-82M s anglickými nástrojmi výslovnosti na použitie výhradne na CPU.

Vývojár chcel hlasové rozhranie pre Claude Code, ktoré sa dá prenášať medzi strojmi bez inštalácie Pythonu alebo samostatného nástroja výslovnosti. Výsledok mení text na zvuk s frekvenciou 24 kHz pomocou pribalených údajov a vektorových operácií prispôsobených procesoru.

**Prečo na tom záleží:** Vývojár lokálnej hlasovej aplikácie dostane syntézu reči aj prevod textu na výslovnosť v jednom nasaditeľnom balíku. Voliteľné zostavenie s vloženými údajmi obsahuje všetky podklady v jednom spustiteľnom súbore s veľkosťou približne 350 MB.

RobViren uvádza približne dvojnásobnú rýchlosť syntézy oproti PyTorchu na dvoch procesoroch Intel. Porovnanie používa rovnakú krátku vetu a hlas so štyrmi vláknami syntézy: približne 470 milisekúnd oproti 916 na i7-14700F a približne 902 oproti 1 770 na i7-7700. Tieto časy pokrývajú syntézu, nie celý postup normalizácie textu a prehrávania.

Implementácia používa Google Highway, knižnicu, ktorá počas behu vyberá implementácie vektorových inštrukcií. Jadrá boli ladené a testované na AVX2, pričom AVX-512 je predvolene vypnuté. Zostavenie pre ARM je dokumentované, ale vývojár uvádza, že jeho rýchlosť ešte nie je vyladená a porovnanie zvuku prebehlo v emulácii.

Postup spracovania výslovnosti má inú hranicu otvorenosti než samotný engine. Zdrojový kód obsahuje nástroje na export váh Kokoro a trénovanie odhadu výslovnosti, ale databáza slovníka, korpus pre značkovanie a tréningový slovník odhadovača sú súkromné. Dodané binárne podklady preto umožňujú balík spustiť bez úplného zopakovania týchto tréningových vstupov.

Zostavenie vyžaduje CMake a kompilátor C++; možnosť vloženia podkladov potrebuje GCC 15 alebo novší. Závislosti a chýbajúce váhy sa sťahujú počas konfigurácie a dokumentácia uvádza, že pri používaní netreba nič sťahovať. Repozitár má licenciu Apache-2.0.

RobViren uvádza, že normalizácia textu potrebuje ďalšie zlepšenie, a súčasný balík považuje za dostatočný pre zamýšľané hlasové rozhranie. Vydanie obsahuje benchmarkový skript a opakovateľný príkaz syntézy, takže ďalší používatelia majú konkrétny základ pre tvrdenie o rýchlosti na CPU.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Vývojár, kód C++ Apache-2.0, Kokoro-82M, iba anglické G2P, výstup 24 kHz, voliteľný približne 350 MB binárny súbor, požiadavky CMake/GCC. | OVERENÉ | https://github.com/RobViren/kokoallovero | žiadne |
| Časy samotnej syntézy so štyrmi vláknami: i7-14700F 470/916 ms (1,95x); i7-7700 902/1770 ms (1,96x), jedna 6,6-sekundová veta, hlas af_heart. | PODĽA SPOLOČNOSTI | https://github.com/RobViren/kokoallovero | žiadne |
| Výber Highway; ladenie AVX2, AVX-512 predvolene vypnuté; ARM nevyladené/emulované; súkromné údaje výslovnosti; sťahovanie počas behu netreba. | PODĽA SPOLOČNOSTI | https://github.com/RobViren/kokoallovero | žiadne |
| Balík znižuje počet komponentov nasadenia pre vývojára lokálneho hlasu. | ANALÝZA | https://github.com/RobViren/kokoallovero | žiadne |
| Projekt bol verejne predstavený v datovanom vlákne. | OVERENÉ | https://news.ycombinator.com/item?id=49937676 | žiadne |
