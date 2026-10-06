+++
title = "Voorbeelden versterken een symbolisch circuit dat al bestaat"
slug = "voorbeelden-versterken-een-symbolisch-circuit-dat-al-bestaat"
description = "Een onderzoek naar interpreteerbaarheid vindt hetzelfde pad voor abstractie, inductie en ophalen voordat de nauwkeurigheid met enkele voorbeelden stijgt. Dat suggereert dat demonstraties bestaande mechanismen versterken in plaats van een nieuw algoritme te bouwen."
tags = ["research", "models"]
date = 2026-10-05T03:59:30+02:00
draft = false
+++

Wanneer een taalmodel een patroon leert uit verschillende voorbeelden in zijn prompt, kan het lijken alsof het ter plekke een nieuwe procedure heeft samengesteld. Een mechanistisch onderzoek van onafhankelijk onderzoeker Melissa Wessel biedt een andere verklaring voor één familie symbolische taken: de procedure is al aanwezig in het model, en voorbeelden versterken geleidelijk het signaal dat erdoorheen loopt.

De preprint volgt een circuit met drie fasen bij prompts met nul tot tien demonstraties. Hij vindt dezelfde kernroute wanneer de nauwkeurigheid laag is en wanneer die bijna perfect is. De aandachtshoofden verschijnen niet plotseling wanneer het model het patroon “begrijpt”. Hun causale bijdrage groeit.

Dit is een beperkt experiment, geen algemene theorie over leren in de context. Maar het maakt van een aantrekkelijke metafoor — voorbeelden activeren latente mechanismen — iets waarin onderzoekers kunnen ingrijpen en dat ze kunnen testen.

## Van tokens naar variabelen en terug

De taak gebruikt abstracte patronen van drie tokens, zoals ABA of ABB. De tokens zijn willekeurig, zodat het model niet op hun gewone betekenis kan vertrouwen. Het moet afleiden welke positie naar het antwoord moet worden gekopieerd.

Eerder werk identificeerde drie fasen. Symbolische abstractiehoofden vertalen concrete tokens naar variabelen. Symbolische inductiehoofden werken met dat abstracte patroon. Ophaalhoofden zetten de voorspelde variabele weer om naar het vereiste token. Wessel volgt deze structuur in Gemma 2-2B, Llama 3.1-8B en Qwen 3-4B, waarbij alleen het aantal demonstraties verandert.

In Gemma 2-2B begint de nauwkeurigheid op 17 procent met één voorbeeld, bereikt ze 93 procent met vier en 99 procent met tien. Toch detecteert causale mediatieanalyse de drie fasen al bij één voorbeeld. De belangrijke hoofden blijven grotendeels aanwezig bij opeenvolgende promptlengtes, terwijl de causale bijdrage van een afzonderlijk hoofd tussen één en tien voorbeelden tot achtvoudig groeit.

De interpretatie is kwantitatief en niet architecturaal: extra voorbeelden versterken een bestaand pad in plaats van een volledig ander pad in te schakelen.

## Het signaal tussen prompts verplaatsen

Detectie alleen kan correlatie met een mechanisme verwarren. Daarom verplaatst het artikel ook interne activaties tussen uitvoeringen. Activaties uit tien voorbeelden invoegen in een prompt met één voorbeeld verhoogt Gemma's nauwkeurigheid van 17 naar 88 procent. Bij nul voorbeelden verhoogt het invoegen van de inductie- en ophaalfasen de nauwkeurigheid voor één patroon van 1 naar 56 procent; willekeurige hoofden buiten het circuit laten die onder 1 procent.

De duidelijkste ingreep gebruikt een “functievector”: een vaste activatie die is samengesteld uit hoofden die door de causale analyse zijn geïdentificeerd. Die invoegen bij nul voorbeelden verhoogt de nauwkeurigheid van 1 naar 86 procent op de ABA-regel. Wanneer de latere ophaalhoofden worden uitgeschakeld, daalt dat herstel naar 13 procent.

Die afhankelijkheid is de sleutel. De vector werkt niet als een op zichzelf staand antwoord of een algemene impuls voor het netwerk. Hij kan de inductiefase grotendeels vervangen doordat het latere ophaalmechanisme beschikbaar blijft om de uitvoer te lezen.

## Een bruikbaar resultaat binnen een klein domein

Het onderzoek laat leren in de context minder lijken op het schrijven van een nieuw programma tijdens inferentie, en meer op het aanleveren van invoer aan een programma dat tijdens de training is ingebouwd. Als die opvatting generaliseert, zouden de grenzen van een model bij leren met enkele voorbeelden afhangen van de circuits in zijn gewichten en van de vraag of een prompt ze kan bereiken.

Het artikel laat niet zien dat alle demonstraties zo werken. De centrale taak is in wezen een kleine relationele tabel met een kopieerbewerking. Een controle met analogieën tussen letterreeksen vindt een vergelijkbare topologie, maar wordt niet voor elk model of met het volledige programma van activatie-ingrepen herhaald. De analysemethode selecteert bovendien componenten die twee regels onderscheiden en kan daardoor gedeelde infrastructuur missen.

Het resultaat is het sterkst als concreet mechanisme voor één eenvoudige capaciteit: voorbeelden kunnen een stabiel symbolisch pad versterken lang voordat het gedrag laat zien dat het pad er is.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
| --- | --- | --- | --- |
| Het onderzoek volgt abstractie-, inductie- en ophaalfasen in Gemma 2-2B, Llama 3.1-8B en Qwen 3-4B | GEVERIFIEERD | [Preprint](https://arxiv.org/abs/2609.36265) | geen |
| Gemma's nauwkeurigheid stijgt van 17 procent bij één voorbeeld naar 99 procent bij tien; de bijdrage per hoofd groeit tot achtvoudig | VOLGENS HET BEDRIJF | [Preprint](https://arxiv.org/abs/2609.36265) | geen; experimenten van de auteur |
| Activatie-ingrepen met tien voorbeelden verhogen de nauwkeurigheid bij één voorbeeld naar 88 procent, en ingrepen bij nul voorbeelden verhogen 1 procent naar 56 procent | VOLGENS HET BEDRIJF | [Preprint](https://arxiv.org/abs/2609.36265) | geen; experimenten van de auteur |
| Injectie van een functievector verhoogt ABA-nauwkeurigheid bij nul voorbeelden van 1 procent naar 86 procent, waarna die na uitschakeling van ophaalhoofden naar 13 procent daalt | VOLGENS HET BEDRIJF | [Preprint](https://arxiv.org/abs/2609.36265) | geen; experimenten van de auteur |
| Demonstraties versterken voor deze taken een bestaand circuit in plaats van een nieuw te bouwen | ANALYSE | [Preprint](https://arxiv.org/abs/2609.36265) | interpretatie van causale ingrepen in het artikel |
| Generalisatie naar rijker abstract redeneren blijft open | GEVERIFIEERD | [Preprint](https://arxiv.org/abs/2609.36265) | vermelde beperking |
