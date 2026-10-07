+++
title = "Visiemodellen scheiden objecten van abstracte relaties"
slug = "visiemodellen-scheiden-objecten-van-abstracte-relaties"
description = "Een preprint vindt in visietaalmodellen een vroeg circuit voor objectvergelijking en een later circuit voor relatievergelijking. Het onderzoek koppelt dat laatste vervolgens aan prestaties op ARC-AGI-1."
tags = ["research", "models"]
date = 2026-10-07T03:59:57+02:00
draft = false
+++

Visietaalmodellen lossen abstracte visuele vergelijkingen mogelijk op via twee concurrerende interne processen: een vroeg proces dat zichtbare objecten volgt en een later proces dat relaties ertussen weergeeft.

Dat is de centrale bevinding van een preprint van Minegishi, Furuta, Kojima en collega's. Het team paste een Relational Match-to-Sample-taak uit de ontwikkelings- en vergelijkende psychologie aan en testte vervolgens zowel gesloten frontiermodellen als open modellen op gecontroleerde afbeeldingen.

## Waarom dit ertoe doet {#why-it-matters}

Voor een onderzoeker die visueel redeneren evalueert, laat een correct antwoord alleen niet zien of een model de onderliggende regel volgde of slechts vergelijkbare vormen herkende. Het onderzoek biedt een manier om die routes te scheiden en vervolgens in te grijpen op de route die met abstracte relaties samenhangt.

Elke taak toont een voorbeeldpaar objecten en vraagt welk kandidaatpaar dezelfde relatie heeft. Eén kandidaat kan de relatie behouden en de objecten veranderen; een andere kan het uiterlijk behouden en de relatie veranderen. Het conflict onthult of het model identiteit of structuur volgt.

Binnen de GPT-, Claude-, Gemini-, Qwen3.5-, Gemma 4- en InternVL3-families verschoven vier veranderingen antwoorden richting relaties: een capabelere modelcategorie, een groter model, minder objecten in de scène en minder ruis per object. De auteurs vergelijken deze ontwikkeling met de “relationele verschuiving” die in de menselijke ontwikkeling wordt waargenomen, maar de gelijkenis betreft gedrag en bewijst geen gedeeld cognitief mechanisme.

De interne analyse vond de twee signalen op verschillende dieptes. Representaties in eerdere lagen groepeerden voorbeelden op objectkenmerken, terwijl latere lagen ze op de abstracte relatie groepeerden. Causale mediatietests identificeerden vervolgens aandachtshoofden waarvan de activiteit bijdroeg aan antwoorden op basis van relaties.

## Een ingreep verbindt het circuit met een andere taak

Het sterkste resultaat komt uit het uitschakelen van de hoofden die met relationele vergelijking samenhangen. De auteurs melden dat dit de prestaties op ARC-AGI-1 sterker schaadt dan het uitschakelen van willekeurig geselecteerde hoofden. Die overdracht is relevant omdat de hoofden op de psychologische vergelijkingstaak zijn gevonden, en niet rechtstreeks zijn gekozen om ARC-resultaten te verklaren.

Het bewijs blijft beperkt. Een verzameling hoofden kan aan twee taken bijdragen zonder een algemene redeneermodule te vormen. De stimuli zijn bewust eenvoudig, en het artikel stelt niet vast dat dezelfde concurrentie herkenning in foto's, grafieken of lange multimodale gesprekken stuurt.

Het onderzoek steunt ook op twee verschillende toegangsniveaus. Gedragsresultaten kunnen propriëtaire API-modellen omvatten, maar representatieanalyse per laag en ablatie vereisen open gewichten. De mechanismeclaim rust daarom op de open modellen die intern zijn onderzocht, terwijl de bredere vergelijking tussen families gedrag betreft.

Het parametrische ontwerp is een voordeel voor reproductie. Het aantal objecten en de visuele ruis kunnen afzonderlijk worden veranderd, zodat een ander team kan testen of de laagscheiding blijft bestaan bij nieuwe vormen, relaties en modelfamilies. De samenvattingspagina noemt geen openbare coderepository; de volledige ingreep reproduceren vereist dus meer dan een benchmark downloaden.

Het artikel werd op 6 oktober 2026 bij arXiv ingediend en heeft geen peerreview ondergaan. De nuttige bijdrage is een falsifieerbare brug tussen een klassieke cognitieve taak en interne modelcircuits: gedrag dat relaties volgt, zou moeten verzwakken wanneer het geïdentificeerde late pad wordt verstoord, terwijl objectvergelijking relatief intact zou moeten blijven.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
| --- | --- | --- | --- |
| Het onderzoek test relationele vergelijking bij frontier-API-modellen en open visietaalmodellen | VOLGENS HET BEDRIJF | [preprint](https://arxiv.org/abs/2610.07646) | geen; evaluatie van de auteurs |
| Schaal, capaciteit, minder objecten en minder ruis verschuiven modellen richting relatievergelijking | VOLGENS HET BEDRIJF | [preprint](https://arxiv.org/abs/2610.07646) | geen |
| Vroege lagen coderen objectovereenkomst, terwijl latere lagen abstracte relaties coderen | VOLGENS HET BEDRIJF | [preprint](https://arxiv.org/abs/2610.07646) | geen |
| Uitschakeling van relatiegebonden hoofden schaadt ARC-AGI-1 sterker dan uitschakeling van willekeurige hoofden | VOLGENS HET BEDRIJF | [preprint](https://arxiv.org/abs/2610.07646) | geen |
| Gedragsgelijkenis bewijst geen gedeeld menselijk mechanisme | ANALYSE | [preprint](https://arxiv.org/abs/2610.07646) | gevolgtrekking uit het onderzoeksontwerp |
| De preprint werd op 6 oktober 2026 ingediend | GEVERIFIEERD | [arXiv-vermelding](https://arxiv.org/abs/2610.07646) | arXiv-metadata |
