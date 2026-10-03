+++
title = "LDraw Nova umožňuje agentom tvoriť upraviteľné modely LEGO"
slug = "ldraw-nova-umoznuje-agentom-tvorit-upravitelne-modely-lego"
description = "Projekt spúšťaný v Dockeri ukladá vytvorené modely ako zdrojový zápis LDraw a upraviteľné 3D súbory spolu s rozhovorom, ktorý viedol k stavbe."
tags = ["projects", "agents", "tools"]
date = 2026-10-03T09:40:58+02:00
draft = false
+++

LDraw Nova, projekt vývojára anteloc pod licenciou AGPL-3.0, poskytuje AI agentom pracovný priestor na tvorbu modelov LEGO ako upraviteľných zdrojových súborov namiesto generovaných obrázkov.

Agent umiestňuje diely cez LDraw, textový formát opisujúci kocky, polohy a rotácie modelu. Aplikácia uchováva tento opis zostavy aj rozhovor použitý pri jej tvorbe, takže výsledný objekt sa dá otvoriť a meniť v ďalších nástrojoch.

**Prečo na tom záleží:** Nadšenec, ktorý požiada agenta o návrh LEGO, dostane model, ktorý môže kontrolovať a upravovať po jednotlivých dieloch. Projekt exportuje aj glTF súbor upraviteľný v Blenderi a ponúka viacero pohľadov na rovnakú stavbu vrátane pohľadu vo virtuálnej realite.

Webová aplikácia beží v Dockeri a vyžaduje dva susedné repozitáre: projekt na stavbu modelov a jeho sprievodný aplikačný balík. Inštalačné pokyny viažu oba na rovnaký tag vydania, aby aplikácia zodpovedala použitým nástrojom. Dokumentované prvotné zostavenie obrazu potrebuje približne 5 GB miesta na disku.

Vyhľadávanie dielov je dôležitou závislosťou. Vývojárov vyhľadávací nástroj spája sémantické vyhľadávanie a preusporiadanie výsledkov cez službu Jev od TypeSafe, hostované API rozhodovacieho modelu. Používateľ s kľúčom TypeSafe môže zapnúť túto fázu hodnotenia; bez neho agenti používajú fulltextové vyhľadávanie, ktoré podľa vývojára môže viesť k horším návrhom.

README opisuje aj problém učenia špecifický pre túto reprezentáciu. Podľa skúseností autora agenti lepšie pracovali s programami v Pythone, ktoré model generujú, než s hotovými súbormi LDraw, pri ktorých mali ťažkosti s matematikou polôh a rotácií. Toto pozorovanie sa týka vývoja projektu, nie všeobecného benchmarku priestorového uvažovania.

Uložené výstupy zahŕňajú zdrojový zápis LDraw, vykreslené obrázky, prehrávač modelu a históriu rozhovoru, pričom export glTF prenáša metadáta do Blenderu. Tieto artefakty umožňujú skúmať postup generovania aj mimo konečného vizuálneho výsledku.

Vydanie už poskytuje zdrojový kód a ukážkové video. Inštalácia stále spája dva repozitáre na rovnakom tagu a lepšie usporiadané vyhľadávanie dielov závisí od hostovaného API; to sú konkrétne závislosti za inak upraviteľným, lokálne spúšťaným návrhárskym prostredím.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislé overenie |
|---|---|---|---|
| Zdrojový kód AGPL-3.0, identita vývojára, výstupy LDraw/glTF/rozhovor, Docker s dvoma repozitármi, približne 5 GB zostavenie. | OVERENÉ | https://github.com/anteloc/ldraw-nova | žiadne |
| Vyhľadávanie Jev zlepšuje návrhy; náhradný postup môže byť horší; príklady generovania v Pythone fungovali lepšie než hotové LDraw. | PODĽA SPOLOČNOSTI | https://github.com/anteloc/ldraw-nova | žiadne |
| Upraviteľné výstupy umožňujú nadšencovi meniť jednotlivé diely a skúmať históriu stavby. | ANALÝZA | https://github.com/anteloc/ldraw-nova | žiadne |
| Projekt bol verejne predstavený v datovanom vlákne. | OVERENÉ | https://news.ycombinator.com/item?id=49937916 | žiadne |
