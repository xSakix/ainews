+++
title = "Mistral toont Large 4 voordat het de gewichten vrijgeeft"
slug = "mistral-toont-large-4-voordat-het-de-gewichten-vrijgeeft"
description = "Mistral heeft API-toegang geopend tot zijn multimodale model met één biljoen parameters en plant de release met open gewichten op 27 oktober. Claims over architectuur en benchmarks blijven daarmee voorlopig."
tags = ["models", "business"]
date = 2026-10-07T04:00:57+02:00
draft = false
+++

Mistral heeft een openbare API-preview van Mistral Large 4 geopend en plant de downloadbare modelgewichten op 27 oktober.

Het Franse bedrijf beschrijft het model als een multimodale mixture of experts die vanaf nul in zijn Europese datacenters is getraind. Het accepteert tekst en afbeeldingen, ondersteunt meer dan 160 talen en heeft een contextvenster van één miljoen tokens.

## Waarom dit ertoe doet {#why-it-matters}

Een organisatie die een Europees model op eigen infrastructuur overweegt, kan Large 4 nu testen, maar de beloofde gewichten nog niet inspecteren of uitrollen. Die kloof maakt dit een preview met een gedateerde leveringsbelofte, in plaats van een voltooide release met open gewichten.

Mistrals aankondiging noemt één biljoen totale parameters en 49 miljard actieve parameters per token. De documentatie noemt daarentegen 1,05 biljoen in totaal, 52 miljard actieve parameters en een visie-encoder met 1,6 miljard parameters. Het verschil kan op afronding of een gewijzigde configuratie wijzen, maar Mistral heeft geen technisch rapport gepubliceerd dat de cijfers met elkaar in overeenstemming brengt.

Het bedrijf legt de nadruk op cyberbeveiliging. Het meldt 82 procent op het onderdeel reproduceren en vervolgens patchen van CyberGym-E2E, 93 procent op Cybench en 61,7 procent op DeepSWE v1.1. Sommige evaluaties noemen externe aanbieders, maar de samengestelde vergelijking en de meeste belangrijkste claims staan in Mistrals eigen releasemateriaal.

Voordat de gewichten verschijnen, zullen volgens Mistral cyberbeveiligingsspecialisten en overheidsinstanties een versie met minder moderatie testen. Het bedrijf stelt dat gewone veiligheidsweigeringen defensief werk kunnen tegenhouden, een afweging die deze preview moet onderzoeken.

API-prijzen beginnen bij 1,36 dollar per miljoen inputtokens en 4,18 dollar per miljoen outputtokens. Modi met en zonder redeneren zijn beschikbaar via Mistral Studio, terwijl de licentie en de definitieve uitrolvereisten tot de release van de gewichten onbekend blijven.

De beslissende gebeurtenis is 27 oktober. Een modelkaart, technisch rapport, licentie en downloadbare bestanden zullen laten zien of het openbare model overeenkomt met de schaal en capaciteiten van de preview.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
| --- | --- | --- | --- |
| Mistral heeft een Large 4-API-preview geopend en de gewichten voor 27 oktober gepland | GEVERIFIEERD | [Aankondiging van Mistral](https://mistral.ai/news/mistral-large-4/) | [Documentatie van Mistral](https://docs.mistral.ai/models/mistral-large-4) |
| De aankondiging noemt één biljoen totale en 49 miljard actieve parameters | GEVERIFIEERD | [Aankondiging van Mistral](https://mistral.ai/news/mistral-large-4/) | documentatie noemt andere cijfers |
| De documentatie noemt 1,05 biljoen totale en 52 miljard actieve parameters en een visie-encoder met 1,6 miljard parameters | GEVERIFIEERD | [Documentatie van Mistral](https://docs.mistral.ai/models/mistral-large-4) | geen |
| Het model scoorde 82% op CyberGym-E2E reproduceren en vervolgens patchen, 93% op Cybench en 61,7% op DeepSWE v1.1 | VOLGENS HET BEDRIJF | [Aankondiging van Mistral](https://mistral.ai/news/mistral-large-4/) | genoemde evaluatoren verifiëren de volledige vergelijking niet onafhankelijk |
| API-prijzen zijn 1,36 dollar voor invoer en 4,18 dollar voor uitvoer per miljoen tokens | GEVERIFIEERD | [Documentatie van Mistral](https://docs.mistral.ai/models/mistral-large-4) | actuele documentatie |
