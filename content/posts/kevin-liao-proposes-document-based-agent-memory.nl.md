+++
title = "Kevin Liao stelt agentgeheugen op basis van documenten voor"
slug = "kevin-liao-stelt-agentgeheugen-op-basis-van-documenten-voor"
description = "De workflow van de ontwikkelaar bewaart specificaties en besluiten in bewerkbare Markdown. Zijn betoog gaat samen met een open-sourceimplementatie, maar zonder vergelijkende benchmark."
tags = ["agents", "tools", "essays"]
date = 2026-10-04T09:23:37+02:00
draft = false
+++

Ontwikkelaar Kevin Liao stelt voor programmeeragents een onderhouden verzameling projectdocumenten te geven. Hij stelt dat het ophalen van losse gespreksfragmenten te veel van de betekenis van een project achterlaat.

In een essay van 3 oktober beschrijft Liao een werkruimte met instructies, specificaties, besluiten, onderzoek en een index. Een agent raadpleegt de relevante documenten vóór het werk en werkt ze daarna bij, terwijl de redenen voor zijn wijzigingen in de context blijven.

Voor een ontwikkelaar die in een nieuwe sessie naar een project terugkeert, is het aantrekkelijke een verslag dat zowel de mens als de agent kan inspecteren. Een specificatie kan het doel en de randvoorwaarden van een functie samen bewaren, terwijl een besluitdocument kan vastleggen waarom een aanpak is gekozen.

Liao's kritiek draait om het ophalen op basis van overeenkomst. Hij stelt dat een relevant ogend fragment verouderd kan zijn, de oorspronkelijke context kan missen of een leemte kan verbergen waarnaar de agent geen reden heeft te zoeken. Zijn claim dat de hele categorie geheugenplugins deze problemen deelt, is een mening. Het essay ondersteunt haar met zijn eigen ervaring, niet met een vergelijking van concurrerende systemen.

Zijn alternatief verandert de onderhoudsregel. Wanneer het project verandert, bewerkt de agent het actuele document in plaats van alleen nog een herinnering aan de gebeurtenissen toe te voegen. Liao zegt meer dan een jaar geleden met een interne map te zijn begonnen en die praktijk tot Operator Memory te hebben ontwikkeld.

De README van het open-sourceproject beschrijft drie documentlocaties: private projectkennis, gedeelde repositorykennis en persoonlijke regels die voor meerdere projecten worden gebruikt. De README noemt adapters voor Claude Code, Codex en andere agentomgevingen en documenteert installatie via een npm-hulpprogramma.

De repository erkent ook een praktische afhankelijkheid: een nieuw project begint met weinig documentatie, dus specificaties moeten worden geschreven voordat latere sessies ze kunnen onderhouden. Betrouwbare updates tijdens lange gesprekken staan nog op de roadmap. Operator Memory is beschikbaar onder de BSD 3-Clause-licentie.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
| --- | --- | --- | --- |
| Kevin Liao publiceerde het essay over documentgeheugen op 3 oktober; instructies, specificaties, besluiten, onderzoek en index; workflow van raadplegen, bouwen en bijwerken | GEVERIFIEERD | [Bron](https://liao.gg/blog/agents-dont-need-memory) | geen |
| Ophalen op basis van overeenkomst kan context missen, verouderde kennis tonen en onbekende leemten laten bestaan; brede kritiek op geheugenplugins | OPINIE | [Bron](https://liao.gg/blog/agents-dont-need-memory) | geen; betoog van de auteur, geen vergelijkende benchmark |
| Liao zegt de aanpak meer dan een jaar te hebben gebruikt en Operator Memory te hebben ontwikkeld | VOLGENS HET BEDRIJF | [Bron](https://liao.gg/blog/agents-dont-need-memory) | geen; zelfgerapporteerd gebruik |
| Private, gedeelde en persoonlijke documentlocaties; genoemde Claude Code- en Codex-adapters; npm-hulpprogramma; BSD 3-Clause-licentie | GEVERIFIEERD | [Bron](https://github.com/aerovato/operator-memory) | geen; gedocumenteerde implementatie en licentie, geen runtimevalidatie |
| Weinig begindocumenten en roadmap voor betrouwbare updates | GEVERIFIEERD | [Bron](https://github.com/aerovato/operator-memory) | geen; toelichtingen in de README |
| Bewerkbare verslagen laten mensen en agents het projectdoel en besluiten samen inspecteren | ANALYSE | [Bron](https://github.com/aerovato/operator-memory) | gevolgtrekking uit leesbare Markdown en updates van canonieke documenten |
