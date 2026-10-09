+++
title = "Rembrandt spúšťa AI nástroje na fotografie lokálne"
slug = "rembrandt-spusta-ai-nastroje-na-fotografie-lokalne"
description = "Editor s licenciou GPL spája spracovanie RAW, masky, odšumovanie a zvýšenie rozlíšenia bez potreby účtu či nahrávania fotografií."
tags = ["projects", "tools"]
date = 2026-10-09T04:00:06+02:00
draft = false
+++

Rembrandt, nový open-source editor fotografií pre macOS, Windows a Linux, spúšťa odšumovanie, zväčšovanie a maskovanie s podporou AI priamo na zariadení používateľa.

Aplikácia s licenciou GPL je nedeštruktívny editor RAW a knižnica fotografií, nie program na maľovanie pixelov. Úpravy ukladá do štandardných sprievodných súborov XMP, pôvodné fotografie nemení a pri bezplatných lokálnych funkciách nevyžaduje účet.

**Prečo na tom záleží:** Fotografi môžu používať nástroje výpočtovej úpravy bez nahrávania súkromných snímok alebo viazania katalógu na predplatenú službu. Zdrojový kód a bežný formát sprievodných súborov ponúkajú cestu von aj v prípade zániku aplikácie.

Rembrandt obsahuje masky objektu, pozadia, predmetov a hĺbky, odšumovanie cez GPU, 2× a 4× zvýšenie rozlíšenia, obnovu zaostrenia, skladanie HDR a panorám, korekcie objektívov aj dávkové úpravy. Textový príkaz ako „teplejšie a trochu jasnejšie“ pohne rovnakými viditeľnými ovládacími prvkami ako manuálna úprava; projekt uvádza, že táto funkcia používa lokálny slovník, nie jazykový model.

Editor používa JavaScript so shadermi WebGL2 a WebGPU v malej desktopovej aplikácii v jazyku Rust. LibRaw spracúva súbory z fotoaparátov, zatiaľ čo pomenované otvorené projekty dodávajú komponenty na zväčšovanie, odšumovanie, profily objektívov a vizuálne masky. Projekt uvádza podporu súborov RAW z viac ako 1 000 fotoaparátov.

Desktopové binárne súbory sú dostupné pre počítače Mac s Apple silicon aj Intelom, Windows pre x64 a Arm a Linux pre x86-64 alebo Arm. Zostavy zatiaľ nie sú podpísané, takže používatelia systémov macOS a Windows musia obísť upozornenia operačného systému pri prvom spustení. Aplikáciu možno tiež poskytovať z počítača s Linuxom alebo macOS a upravovať fotografie cez prehliadač vo vlastnej sieti.

Repozitár porovnáva Rembrandt s Lightroomom a darktable, no tvrdenia o kvalite neboli nezávisle otestované. Uvádza aj chýbajúce funkcie vrátane fotografovania cez pripojený fotoaparát, rozpoznávania tvárí, tlače a ekosystému doplnkov. Voliteľná cloudová synchronizácia je platená a vyžaduje účet; lokálny editor nie.

Aktuálne vydanie, návod na zostavenie a kontrolné súčty sú dostupné v [repozitári Rembrandt](https://github.com/thesnarkitecht/rembrandt). Najdôležitejším ďalším testom bude dlhodobé používanie na rozmanitých katalógoch RAW, kde na farebnom spracovaní, kompatibilite fotoaparátov a spoľahlivosti exportu záleží viac než na zozname funkcií.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Rembrandt je dostupný pre macOS, Windows a Linux pod licenciou GPL-3.0-or-later | OVERENÉ | [Repozitár](https://github.com/thesnarkitecht/rembrandt) | žiadne |
| Lokálne funkcie nevyžadujú účet a fotografie netreba nahrávať | OVERENÉ | [Repozitár](https://github.com/thesnarkitecht/rembrandt) | žiadne |
| Úpravy používajú sprievodné súbory XMP a pôvodné súbory zostávajú nezmenené | OVERENÉ | [Repozitár](https://github.com/thesnarkitecht/rembrandt) | žiadne |
| Aplikácia obsahuje lokálne odšumovanie, zvýšenie rozlíšenia a masky s podporou AI | OVERENÉ | [Repozitár](https://github.com/thesnarkitecht/rembrandt) | žiadne |
| Editor používa JavaScript, WebGL2/WebGPU a desktopovú aplikáciu v jazyku Rust | OVERENÉ | [Repozitár](https://github.com/thesnarkitecht/rembrandt) | žiadne |
| Projekt uvádza podporu RAW súborov z viac ako 1 000 fotoaparátov | PODĽA SPOLOČNOSTI | [Repozitár](https://github.com/thesnarkitecht/rembrandt) | žiadne |
| Súčasné desktopové zostavy nie sú podpísané | OVERENÉ | [Repozitár](https://github.com/thesnarkitecht/rembrandt) | žiadne |
| Voliteľná cloudová synchronizácia je jediná platená funkcia a vyžaduje účet | OVERENÉ | [Repozitár](https://github.com/thesnarkitecht/rembrandt) | žiadne |
