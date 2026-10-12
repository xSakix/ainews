+++
title = "PolyStrata spúšťa veľké MoE na herných GPU"
slug = "polystrata-spusta-velke-moe-na-hernych-gpu"
description = "Open-source nástroj drží vybrané experty modelu v systémovej pamäti a podľa potreby ich presúva do spotrebiteľského GPU. Balík ponúka lokálne rozhrania kompatibilné s OpenAI a Anthropic."
tags = ["projects", "models", "hardware"]
date = 2026-10-12T03:57:37+02:00
draft = false
+++

PolyStrata vydala open-source nástroj, ktorý používa systémovú pamäť na prevádzku modelov typu mixture-of-experts príliš veľkých na celé uloženie v hernom GPU.

Balík na jedno kliknutie obaľuje runtime Strata a cieli na karty Nvidia a AMD s aspoň 12 GB videopamäte. Obsahuje obrazový Qwen3.8-Flash-Next a experimentálnu podporu väčších riedkych modelov, pričom na lokálnom počítači poskytuje rozhrania kompatibilné s OpenAI a Anthropic.

## Prečo je to dôležité {#why-it-matters}

Vývojárovi s pracovnou stanicou namiesto servera mení PolyStrata voľnú systémovú RAM na väčší priestor pre model. Do GPU presúva iba expertov potrebných pre aktuálny token, takže vymieňa prenos dát a kapacitu pamäte za cenu viacčipového hardvéru.

Modely mixture-of-experts obsahujú mnoho špecializovaných blokov, no pri každom kroku aktivujú len časť z nich. PolyStrata drží bloky v hostiteľskej pamäti a aktívne plánuje do akcelerátora. Súbor modelu sa tým nezmenší: README uvádza, že experimentálny GLM 5.3 Flash stále potrebuje približne 79 až 114 GB podľa kvantizácie.

Vlastné merania projektu na RTX 5070 siahajú od približne 94 generovaných tokenov za sekundu pri najmenšom dvojbitovom nastavení po 53 pri väčšom trojbitovom. Pri kontexte 32 000 tokenov uvádza spracovanie promptu približne 1 620 až 2 650 tokenov za sekundu. Ide o benchmarky tvorcu a kvalita sa medzi kvantizáciami líši.

PolyStrata dokumentuje aj Claude Code riadiaci riedky Qwen3.6 35B v trojbitovej presnosti na 8 GB notebookovom GPU. Funkcia warm start načíta systémový prompt pred interaktívnou reláciou a skracuje čakanie na prvú odpoveď. Použiteľnosť závisí od priepustnosti RAM, smerovania expertov a zmien kontextu.

Repozitár má licenciu MIT a poskytuje lokálne rozhrania pre existujúcich agentových klientov. Znižuje integračnú prácu a lokálnym aplikáciám ponecháva prístup k súborom pod oprávneniami používateľa. Prevádzkovateľ zároveň zodpovedá za aktualizácie, sieť a logy.

## Čo sledovať

Nezávislé testy by mali porovnať rovnaké modely a kvantizácie so zavedenými runtime nástrojmi s odkladaním do CPU. Hodnotou projektu je dnes kontrolovateľný kód a praktické balenie; rýchlosti zostávajú tvrdením autora.

## Overenie {#verification}

| Tvrdenie | Označenie | Primárny zdroj | Nezávislá kontrola |
|---|---|---|---|
| PolyStrata vydala lokálny runner s licenciou MIT pre riedke modely na spotrebiteľských GPU | OVERENÉ | https://github.com/VecSzn/PolyStrata | žiadna |
| Balík poskytuje lokálne API kompatibilné s OpenAI a Anthropic | OVERENÉ | https://github.com/VecSzn/PolyStrata | žiadna |
| README uvádza 53 až 94 generovaných tokenov za sekundu na RTX 5070 | PODĽA SPOLOČNOSTI | https://github.com/VecSzn/PolyStrata | žiadna |
| Experimentálne súbory GLM 5.3 Flash potrebujú približne 79 až 114 GB | OVERENÉ | https://github.com/VecSzn/PolyStrata | žiadna |
| Presun expertov z RAM vymieňa kapacitu za náklady prenosu a priepustnosti | ANALÝZA | https://github.com/VecSzn/PolyStrata | žiadna |
