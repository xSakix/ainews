+++
title = "Meer redeneren vermindert modelbias niet"
slug = "meer-redeneren-vermindert-modelbias-niet"
description = "Een onderzoek met 12.350 aanroepen vond geen betrouwbare daling op zes maten voor cognitieve bias wanneer modellen meer redeneertokens gebruikten. Eén directe prompt hielp tegen het ankereffect."
tags = ["research", "models"]
date = 2026-10-09T04:02:06+02:00
draft = false
+++

Taalmodellen meer tijd geven om te redeneren verminderde hun gevoeligheid voor prompts met cognitieve bias niet betrouwbaar in een nieuw onderzoek met zeven modellen en 12.350 API-aanroepen.

Onderzoeker Obada Kraishan van Texas Tech University varieerde de redeneerruimte voor modellen van Anthropic, OpenAI, DeepSeek en Qwen en mat vervolgens hoe hun antwoorden veranderden wanneer een beslisscenario een irrelevant anker, kader of eerdere verbintenis bevatte. Geen enkel model werd consequent minder gevoelig naarmate zijn daadwerkelijke gebruik van redeneertokens steeg.

**Waarom dit ertoe doet:** Een ontwikkelaar die een groter redeneerbudget kiest voor een beslissingsondersteunend systeem betaalt voor meer rekenwerk. Deze resultaten geven aan dat extra rekenwerk geen enkele gemeten bias betrouwbaar verbeterde, hoewel redeneermodellen voor gebruikers vaak bedachtzamer overkomen.

## Het onderzoek mat het denkwerk dat werkelijk plaatsvond

Het experiment gebruikte 30 gepaarde scenario's over het ankereffect, framing, verliesaversie, escalatie van betrokkenheid, beschikbaarheidsbias en bevestigingsbias. Elk paar bevatte dezelfde informatie die voor de beslissing relevant was, maar één versie voegde het kenmerk toe dat naar verwachting het menselijke oordeel zou verschuiven. Met tien herhaalde steekproeven per conditie kon de auteur de verandering in gekozen opties meten.

Het panel van zeven modellen koppelde redeneer- en niet-redeneerversies binnen vier families. De gevraagde redeneerlimieten waren nul, 1.024, 4.096 en 8.192 tokens, al verschilden de beschikbare combinaties per aanbieder. Kraishan registreerde de daadwerkelijk verbruikte tokens omdat de API-instelling zich vaak niet vertaalde in een gelijkwaardige hoeveelheid denkwerk.

Dat onderscheid bleek belangrijk. Het Anthropic-model verhoogde zijn gemiddelde redeneergebruik naarmate de limiet steeg, maar bleef ruim onder de grotere grenzen. Het geteste OpenAI-model gebruikte boven nul vrijwel dezelfde hoeveelheid, terwijl DeepSeek-R1 en Qwen3 soms een gevraagde limiet van 1.024 tokens overschreden. De hoofdanalyse behandelde daarom het gerealiseerde tokengebruik als de dosis.

Redeneermodellen waren niet betrouwbaar minder bevooroordeeld dan hun gekoppelde vergelijkingsmodellen. De richting van het verschil neigde in alle vier de families zelfs naar iets grotere gevoeligheid, maar de samengevoegde schatting was te onzeker om die sterkere claim te ondersteunen. Belangrijker voor de centrale vraag van het experiment: geen model vertoonde een statistisch betrouwbare daling naarmate het meer redeneertokens verbruikte.

De bevinding heeft een beperkte reikwijdte. De testreeks bevatte vijf items voor elk van zes biases, allemaal uit managementbeslissingen, en sommige familievergelijkingen gebruikten verwante modellen in plaats van redeneren bij identieke gewichten aan en uit te zetten. Ze test gedrag onder gecontroleerde prompts, niet de juistheid van open beslissingen op de werkplek.

## Het ankereffect reageerde op een directe instructie

Het ankereffect was de enige geteste bias die modellen consequent in dezelfde richting stuurde als gewoonlijk bij mensen wordt gezien. Een getal in de prompt trok schattingen bij alle zeven modellen naar zich toe. Vier andere categorieën neigden naar de tegenovergestelde richting, terwijl beschikbaarheid geen betrouwbaar effect liet zien.

Voor de vijf ankeritems voegde de auteur één zin toe die het model verplichtte het anker te herhalen voordat het antwoordde. Het ankereffect nam bij elk item af. Het samengevoegde resultaat miste nipt de significantiedrempel van het onderzoek, dus het is een veelbelovende waarneming en geen bevestigde tegenmaatregel, maar extra redeneren alleen leverde geen vergelijkbare vermindering op.

Dit contrast is het meest praktische resultaat van het artikel. Een gerichte instructie kan veranderen welke informatie het model verwerkt, terwijl een groter redeneerbudget het bestaande proces alleen meer ruimte geeft. Het experiment toont niet aan dat getallen herhalen generaliseert buiten vijf prompts; het laat wel zien waarom rekeninstellingen en maatregelen tegen bias in afzonderlijke evaluaties thuishoren.

De preprint werd op 7 oktober ingediend en is geaccepteerd voor IEEE CogMI 2026. De auteur publiceerde de vastgelegde promptreeks, tokenregistraties per aanroep en analysecode in de [Anchored Minds-repository](https://github.com/obadaKraishan/anchored-minds), zodat het resultaat op nieuwere modellen en grotere itemsets kan worden getest.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
|---|---|---|---|
| Het onderzoek deed 12.350 aanroepen over zeven modellen in vier families | VOLGENS HET BEDRIJF | [Artikel](https://arxiv.org/abs/2610.10049) | [Code en data](https://github.com/obadaKraishan/anchored-minds) |
| Het gebruikte 30 scenario's met zes cognitieve biases | VOLGENS HET BEDRIJF | [Artikel](https://arxiv.org/abs/2610.10049) | [Code en data](https://github.com/obadaKraishan/anchored-minds) |
| Gevraagde limieten en gerealiseerd redeneergebruik weken per aanbieder van elkaar af | VOLGENS HET BEDRIJF | [Artikel](https://arxiv.org/abs/2610.10049) | [Code en data](https://github.com/obadaKraishan/anchored-minds) |
| Geen getest model vertoonde een betrouwbare afname van de omvang van bias bij toenemend gebruik van redeneertokens | VOLGENS HET BEDRIJF | [Artikel](https://arxiv.org/abs/2610.10049) | geen |
| Redeneermodellen waren niet betrouwbaar minder bevooroordeeld dan vergelijkingsmodellen uit dezelfde familie | VOLGENS HET BEDRIJF | [Artikel](https://arxiv.org/abs/2610.10049) | geen |
| Het ankereffect werkte bij alle zeven modellen in de menselijke richting | VOLGENS HET BEDRIJF | [Artikel](https://arxiv.org/abs/2610.10049) | geen |
| Het anker herhalen verminderde het ankereffect op alle vijf items, maar miste de significantiedrempel | VOLGENS HET BEDRIJF | [Artikel](https://arxiv.org/abs/2610.10049) | geen |
| Het artikel is geaccepteerd voor IEEE CogMI 2026 en code en data zijn gepubliceerd | GEVERIFIEERD | [Artikel](https://arxiv.org/abs/2610.10049) | [Repository](https://github.com/obadaKraishan/anchored-minds) |
