+++
title = "Anthropic lanceert Claude Haiku 5.5"
slug = "anthropic-lanceert-claude-haiku-5-5"
description = "Het kleine Claude-model voegt adaptief denken en twee tokenprijstarieven toe. Anthropic positioneert het voor samenvattingen, browserwerk en nauw afgebakende subagents."
tags = ["models", "agents"]
date = 2026-10-08T03:59:31+02:00
draft = false
+++

Anthropic bracht op 7 oktober Claude Haiku 5.5 uit, verlaagde de effectieve prijs van zijn kleine modellen en voegde een contextvenster van één miljoen tokens en een instelbaar redeneerniveau toe.

Het API-model is gebouwd voor veelvuldig, nauw afgebakend werk zoals classificatie, samenvatting, databasequery's en subagenttaken. Het is beschikbaar via Anthropic en de grote cloudplatforms onder model-ID `claude-haiku-5-5`.

Voor ontwikkelaars die per taak betalen is de prijswijziging het onmiddellijke gevolg. Prompts tot 100.000 tokens kosten 0,10 dollar per miljoen inputtokens en 0,50 dollar per miljoen uitvoertokens. Langere prompts kosten respectievelijk 0,50 en 2,50 dollar. Anthropic zegt dat de resulterende gemiddelde kosten ongeveer 75 procent lager zijn dan bij Haiku 4.5, rekening houdend met de iets andere tokenizer van het nieuwe model.

Haiku 5.5 is het eerste Haiku-model met adaptief denken en een instelling voor het redeneerniveau. Dat levert ook een migratieprobleem op: verzoeken met de oudere handmatige instelling `budget_tokens` geven een HTTP 400-fout terug. Applicaties die van Haiku 4.5 overstappen moeten die instelling verwijderen en zowel tokengebruik als uitvoerkwaliteit opnieuw testen.

Anthropics eigen evaluaties plaatsen Haiku 5.5 op 72,4 procent op het offlinegedeelte van een benchmark voor computergebruik, tegenover 15,7 procent voor Haiku 4.5. De vergelijking is door de aanbieder uitgevoerd en Anthropic verwijst complex programmeerwerk nog steeds naar Sonnet 5.5 of Opus 5.5. Haiku is bedoeld als het goedkopere ondersteunende model dat korte, herhaalde handelingen rond een groter model afhandelt.

De release halveert ook de prijs voor het lezen van de Sonnet 5.5-cache tot 0,10 dollar per miljoen tokens. Anthropic zegt dat cachelezingen zo'n groot deel van het agentverkeer uitmaken dat de wijziging de kosten van de meeste Sonnet 5.5-agenttaken met ongeveer 20 procent verlaagt.

Max- en Team-abonnees krijgen naar verwachting in de lanceringsweek maandelijkse API-credits. Anthropics Python- en TypeScript-SDK's krijgen ook bètaklassen voor browser- en computergebruik, de twee snelheidsgevoelige werklasten die het bedrijf voor Haiku 5.5 benadrukt.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
|---|---|---|---|
| Anthropic bracht Claude Haiku 5.5 op 7 oktober 2026 uit met adaptief denken, een contextvenster van 1 miljoen tokens en maximaal 128.000 uitvoertokens | GEVERIFIEERD | [Anthropic-lancering](https://www.anthropic.com/claude-haiku-5-5) | geen |
| Prompts tot 100.000 tokens kosten 0,10 dollar voor invoer en 0,50 dollar voor uitvoer per miljoen tokens; langere prompts kosten 0,50 en 2,50 dollar | GEVERIFIEERD | [Anthropic-lancering](https://www.anthropic.com/claude-haiku-5-5) | geen |
| Anthropic zegt dat de gemiddelde kosten ongeveer 75% lager zijn dan bij Haiku 4.5 | VOLGENS HET BEDRIJF | [Anthropic-lancering](https://www.anthropic.com/claude-haiku-5-5) | geen |
| Anthropic meldt 72,4% op de offlinesubset van OSWorld 2.1, tegenover 15,7% voor Haiku 4.5 | VOLGENS HET BEDRIJF | [Anthropic-lancering](https://www.anthropic.com/claude-haiku-5-5) | geen |
| Handmatige `budget_tokens`-verzoeken geven bij migratie HTTP 400 terug | GEVERIFIEERD | [Claude-releasenotities](https://platform.claude.com/docs/en/release-notes/overview) | geen |
| Sonnet 5.5-cachelezingen kosten nu 0,10 dollar per miljoen tokens en Anthropic schat ongeveer 20% lagere kosten voor agenttaken | VOLGENS HET BEDRIJF | [Anthropic-lancering](https://www.anthropic.com/claude-haiku-5-5) | geen |
