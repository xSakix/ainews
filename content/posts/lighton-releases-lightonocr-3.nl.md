+++
title = "LightOn brengt LightOnOCR-3 uit"
slug = "lighton-brengt-lightonocr-3-uit"
description = "De modelfamilie met Apache-2.0-licentie combineert transcriptie, lay-outkaders, beeldbeschrijvingen en grafiekextractie in modellen die klein genoeg zijn om lokaal te draaien."
tags = ["models", "tools"]
date = 2026-10-09T04:04:06+02:00
draft = false
+++

Het Franse AI-bedrijf LightOn heeft LightOnOCR-3 uitgebracht, een familie documentmodellen met open gewichten die tekst, paginastructuur, beeldbeschrijvingen en grafiekdata in één doorgang kunnen teruggeven.

De familie heeft versies met 0,8 miljard, 1 miljard en 4 miljard parameters onder de Apache 2.0-licentie. Een lege prompt levert een gewone transcriptie op; de prompt `grounding` voegt gelabelde gebieden met coördinaten toe, beschrijft beelden en zet grafieken om in HTML-tabellen.

**Waarom dit ertoe doet:** Een ontwikkelaar van een private documentpijplijn kan deze modellen inspecteren en lokaal draaien in plaats van pagina's naar een gehoste dienst te sturen of afzonderlijke systemen voor OCR, lay-outdetectie en grafiekextractie te combineren.

LightOn behield zijn vorige architectuur voor het model met 1 miljard parameters, waardoor die variant een directe upgrade is voor bestaande LightOnOCR-2-installaties. De kleinere en grotere versies gebruiken de beeld-taalarchitectuur van Qwen3.5. LightOn publiceerde ook hulpmiddelen voor conversie en visualisatie, modelgewichten en de scripts waarmee het zijn benchmarkscores reproduceerde.

Het sterkste hoofdresultaat komt uit LightOns eigen tests. Het model met 4 miljard parameters scoorde 86,3 op de olmOCR-benchmark met 512 pagina's, 1,3 punten achter Infinity Parser Pro met 35,1 miljard parameters en een half punt vóór een ander model met 4 miljard parameters, Chandra 2. De vergelijking is nuttig omdat het bedrijf de modellen onder dezelfde serveropstelling draaide, maar het blijft een evaluatie door de aanbieder en uitvoernormalisatie kan OCR-scores aanzienlijk veranderen.

De gestructureerde uitvoer van het model is bewust compact. LightOn zei dat de versies met 0,8 miljard en 4 miljard parameters op dezelfde pagina's 9 tot 14 procent minder tokens genereerden dan twee concurrerende parsers, terwijl ze ook kaders en beeldbeschrijvingen teruggeven. Bij de voorkeursresolutie van elk model voor de benchmark had de versie met 1 miljard parameters de laagste gemelde verwerkingstijd voor één pagina: 2,7 seconden op een NVIDIA H100.

Het verslag over de training is ongewoon gedetailleerd voor een releasebericht. LightOn beschrijft hoe het verschillende detectoren combineerde, dubbelzinnige pagina-annotaties verwierp en een groot beeldmodel gebruikte om figuren te labelen. Het zegt ook dat de benchmarkrepository zijn nabewerkingsregels bevat, die relevant zijn omdat gelijkwaardige voetnoten of formules afhankelijk van hun opmaak verschillende scores voor bewerkingsafstand kunnen krijgen.

Alle drie de sets gewichten, een demo en de ondersteunende code zijn nu beschikbaar via [LightOns releasebericht](https://huggingface.co/blog/lightonai/lightonocr-3). Onafhankelijke tests moeten vaststellen hoe betrouwbaar grafiekwaarden en kaders blijven bij documenten buiten LightOns evaluatiesets.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
|---|---|---|---|
| LightOn bracht drie LightOnOCR-3-varianten uit onder Apache 2.0 | GEVERIFIEERD | [Releasebericht](https://huggingface.co/blog/lightonai/lightonocr-3) | [Modelkaart van 4 miljard parameters](https://huggingface.co/lightonai/LightOnOCR-3-4B) |
| Groundingmodus geeft gelabelde kaders, beeldbeschrijvingen en grafiektabellen terug | GEVERIFIEERD | [Releasebericht](https://huggingface.co/blog/lightonai/lightonocr-3) | geen |
| Het model met 1 miljard parameters behoudt de vorige architectuur; 0,8 miljard en 4 miljard gebruiken de Qwen3.5 VLM | GEVERIFIEERD | [Releasebericht](https://huggingface.co/blog/lightonai/lightonocr-3) | geen |
| LightOn publiceerde gewichten, hulpmiddelen en scripts voor benchmarkreproductie | GEVERIFIEERD | [Releasebericht](https://huggingface.co/blog/lightonai/lightonocr-3) | [Modelkaart van 4 miljard parameters](https://huggingface.co/lightonai/LightOnOCR-3-4B) |
| Het model met 4 miljard parameters scoorde 86,3 op olmOCR-Bench | VOLGENS HET BEDRIJF | [Releasebericht](https://huggingface.co/blog/lightonai/lightonocr-3) | geen |
| Geselecteerde modellen produceerden 9% tot 14% minder tokens dan genoemde concurrenten | VOLGENS HET BEDRIJF | [Releasebericht](https://huggingface.co/blog/lightonai/lightonocr-3) | geen |
| Het model met 1 miljard parameters had een verwerkingstijd van 2,7 seconden per pagina op een H100 | VOLGENS HET BEDRIJF | [Releasebericht](https://huggingface.co/blog/lightonai/lightonocr-3) | geen |
