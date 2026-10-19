+++
title = "OpenAI brengt GPT-6.1 Sol uit"
slug = "openai-brengt-gpt-6-1-sol-uit"
description = "OpenAI's nieuwe middenklassemodel kost bij standaard-API-tarieven een vijfde van GPT-6 Astra. De prestatie- en veiligheidsvergelijkingen blijven evaluaties van het bedrijf zelf."
tags = ["models", "business", "safety"]
date = 2026-09-30T04:04:34+02:00
draft = false
+++

OpenAI bracht GPT-6.1 Sol op 29 september uit voor 2 dollar per miljoen inputtokens en 10 dollar per miljoen outputtokens via zijn API.

Het bedrijf plaatst het model tussen het bestaande GPT-6 Sol en topmodel GPT-6 Astra. Volgens OpenAI benadert de nieuwe versie Astra bij evaluaties van programmeren, computerbediening en professioneel werk, tegen een vijfde van Astra's standaardprijzen voor input en output.

**Waarom dit ertoe doet:** Ontwikkelaars die agents herhaaldelijk laten draaien, betalen voor lange prompts, toolresultaten en gegenereerde uitvoer. Een lagere prijs bij bijna het niveau van het topmodel kan veranderen welk model actief blijft voor dagelijks werk en welke taken Astra nog rechtvaardigen.

GPT-6.1 Sol is via de API beschikbaar als `gpt-6.1-sol` en voor Plus-, Pro-, Business-, Enterprise- en Education-klanten in ChatGPT Work en Codex. Het is nog niet beschikbaar in de algemene Chat-interface. Gecachete input kost 0,10 dollar per miljoen tokens; een Ultrafast-versie die sneller genereert wordt de komende dagen verwacht.

OpenAI's voornaamste bewijs komt uit zijn eigen evaluatieomgeving. Volgens het bedrijf evenaarde GPT-6.1 Sol Astra op DeepSWE 1.1 tegen ongeveer een vijfde van de kosten per taak. Op de offline-computerbedieningsset van OSWorld eindigde het bij maximaal redeneerniveau binnen circa twee procentpunt van Astra, tegen ongeveer een zevende van de kosten per taak.

De vergelijking voor wetenschappelijk werk toont een duidelijker verschil. OpenAI meldt dat Astra 68,1 procent scoorde op Terminal-Bench Science 0.1 en het sterkste geteste model bleef. GPT-6.1 Sol kostte in die evaluatie bij maximaal redeneerniveau 5,47 dollar per taak, tegenover 23,80 dollar voor Astra.

OpenAI publiceerde ook een veiligheidsaanvulling. Het classificeert GPT-6.1 Sol binnen zijn Preparedness Framework als Critical voor cyberbeveiliging en High voor biologische en chemische capaciteiten en past dezelfde beveiligingslagen toe als bij Astra. Volgens het document deed het model in een uitdagende interne test geen pogingen om een automatische beoordelaar van handelingen te omzeilen.

Die resultaten blijven leveranciersmetingen. OpenAI merkt op dat zijn onderzoeksomgeving en API kunnen verschillen van ChatGPT in productie, en dat de moeilijke prompts voor feitelijke juistheid zijn geselecteerd uit gesprekken waarin gebruikers al fouten hadden gemeld. Onafhankelijke tests moeten aantonen hoe het model zich gedraagt bij gewone werklasten en concurrerende uitvoeringsomgevingen voor agents.

De volgende releasemijlpaal is beschikbaarheid van Ultrafast. Ontwikkelaars kunnen de werkelijke taakkosten en latentie van het standaardmodel al met Sol en Astra vergelijken met dezelfde prompts; OpenAI heeft nog geen lanceringsdatum of afzonderlijke prijs voor GPT-6.1 Sol Ultrafast gepubliceerd.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
| --- | --- | --- | --- |
| OpenAI bracht GPT-6.1 Sol op 29 september uit | GEVERIFIEERD | [OpenAI-aankondiging](https://openai.com/index/introducing-gpt-6-1-sol/) | [Associated Press](https://apnews.com/article/77b6b8888145869206996d7509d24256) bericht over de lancering |
| API-prijzen bedragen per miljoen tokens 2 dollar voor input, 0,10 dollar voor gecachete input en 10 dollar voor output | GEVERIFIEERD | [OpenAI-prijzen en beschikbaarheid](https://openai.com/index/introducing-gpt-6-1-sol/) | De openbare API-documentatie vermeldt het model |
| Het model benadert of evenaart Astra in genoemde bedrijfsevaluaties | VOLGENS HET BEDRIJF | [OpenAI-evaluatieresultaten](https://openai.com/index/introducing-gpt-6-1-sol/) | Geen onafhankelijke reproductie gevonden |
| Astra scoorde 68,1% op Terminal-Bench Science in OpenAI's vergelijking | VOLGENS HET BEDRIJF | [OpenAI-evaluatieresultaten](https://openai.com/index/introducing-gpt-6-1-sol/) | Geen onafhankelijke reproductie gevonden |
| OpenAI classificeert het model als Critical voor cyber en High voor biologische en chemische capaciteiten | GEVERIFIEERD | [Aanvulling op de systeemkaart](https://deploymentsafety.openai.com/gpt-6-1-sol/respecting-auto-review) | De classificatie is OpenAI's eigen beslissing binnen zijn raamwerk |
| Ultrafast is gepland, maar een gepubliceerde lanceringsdatum en prijs ontbreken | GEVERIFIEERD | [OpenAI-beschikbaarheidssectie](https://openai.com/index/introducing-gpt-6-1-sol/) | Het DevDay-overzicht zegt dat het binnenkort komt |
