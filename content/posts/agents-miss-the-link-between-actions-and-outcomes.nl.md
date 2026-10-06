+++
title = "Agents missen het verband tussen acties en uitkomsten"
slug = "agents-missen-het-verband-tussen-acties-en-uitkomsten"
description = "Een preprint vindt dat veel van het voordeel van de geschiedenis van een agent behouden blijft wanneer eerdere acties door elkaar worden gezet. Elke actie expliciet aan haar resultaat koppelen verbetert de taakvoltooiing."
tags = ["research", "agents"]
date = 2026-10-06T04:07:31+02:00
draft = false
+++

Taalagents leggen vaak geen verband tussen een eerdere actie en de waarneming die deze opleverde, zelfs wanneer hun volledige interactiegeschiedenis in de context blijft staan, meldt een nieuwe preprint.

Jingyu Liu en vier mede-auteurs onderzochten agents die hun eerdere acties en feedback uit de omgeving ontvangen voordat ze hun volgende stap kiezen. De geschiedenis hielp doorgaans, maar eerdere acties door elkaar zetten leidde slechts tot een bescheiden verlies. Dat suggereert dat de agents het verslag gebruikten zonder betrouwbaar te leren welke actie tot welke uitkomst leidde.

## Waarom dit ertoe doet {#why-it-matters}

Voor een engineer die een agent met toolgebruik bouwt, is een transcript alleen nuttig wanneer het model ervan kan leren. Als een agent eerdere resultaten als losse aanwijzingen leest, kan hij mislukte acties herhalen of het resultaat aan de verkeerde stap toeschrijven, hoewel alle relevante tokens aanwezig zijn.

De onderzoekers testten de hypothese door de koppeling tussen actie en waarneming te verbreken. Ze zetten eerdere acties door elkaar, terwijl de waarnemingen op hun plaats bleven. Het transcript bevatte zo nog veel van dezelfde taal, maar behield geen betrouwbare causale volgorde meer. De taakvoltooiing nam minder af dan verwacht.

Dat negatieve resultaat verandert hoe het voordeel van de geschiedenis moet worden geïnterpreteerd. Een hoger succespercentage met meer transcript toont op zichzelf niet aan dat een agent nuttige ervaring heeft opgebouwd. Het model kan ook aanwijzingen uit eerdere waarnemingen halen of eenvoudigweg profiteren van extra tekst die met de taak samenhangt.

De eenvoudigste oplossing van het team voegde geen nieuwe taakinformatie toe. Elke waarneming werd expliciet aangeduid als het resultaat van de actie die er direct aan voorafging. Volgens de preprint verbeterde deze annotatie het taaksucces en verminderde ze herhaling van de volgende actie.

## Een controller kan nuttige ervaring selecteren

Het artikel introduceert vervolgens een aangeleerde actiekalibrator. Die beoordeelt eerdere acties opnieuw en legt selectief ervaringen vast voor latere beslissingen, in plaats van de hoofdagent een ongestructureerd transcript te laten interpreteren. De auteurs melden een verdere verbetering ten opzichte van expliciete resultaatlabels.

Het ontwerp scheidt twee taken die agentsystemen vaak combineren: handelen in een omgeving en bepalen wat de vorige interactie heeft geleerd. Die verdeling is praktisch, omdat ze in een bestaande agentlus kan worden opgenomen zonder de omgeving te veranderen of externe kennis toe te voegen.

Het centrale bewijs van de preprint betreft gedrag. Het stelt niet vast welke representatie het model intern vormt, en de samenvatting biedt geen link naar openbare code. De gemelde verbeteringen hangen bovendien af van de geteste taken, modellen en transcriptindeling; ze mogen daarom niet worden opgevat als een universele schatting voor agents in productie.

Toch is de controle met de door elkaar gezette geschiedenis bijzonder informatief. Ze maakt onderscheid tussen “het transcript hielp” en “de agent begreep zijn ervaring”, twee uitspraken die bij agentevaluaties vaak als gelijkwaardig worden behandeld.

Liu, Zhiwen Wang, Yuxin Jing, Huanyu Zhou en Yong Liu dienden de preprint op 2 oktober 2026 in. Het toevoegen van resultaatlabels is helder genoeg beschreven om andere agentbouwers het in hun eigen lussen te laten testen. De aangeleerde kalibrator zal moeilijker te beoordelen zijn zonder vrijgegeven trainingsdetails en code.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
| --- | --- | --- | --- |
| Veel van het voordeel van de geschiedenis blijft behouden wanneer eerdere acties door elkaar worden gezet | VOLGENS HET BEDRIJF | [Preprint van Liu en collega's](https://arxiv.org/abs/2610.02769) | geen; resultaat uit een preprint |
| Het verbreken van de koppeling tussen actie en waarneming veroorzaakt slechts een bescheiden daling | VOLGENS HET BEDRIJF | [Preprint van Liu en collega's](https://arxiv.org/abs/2610.02769) | geen |
| Expliciete resultaatlabels verbeteren het taaksucces en verminderen herhaalde acties | VOLGENS HET BEDRIJF | [Preprint van Liu en collega's](https://arxiv.org/abs/2610.02769) | geen |
| Een aangeleerde kalibrator verbetert het taaksucces verder dan resultaatlabels | VOLGENS HET BEDRIJF | [Preprint van Liu en collega's](https://arxiv.org/abs/2610.02769) | geen |
| Het resultaat onderscheidt het voordeel van een transcript van leren over acties en uitkomsten | ANALYSE | [Preprint van Liu en collega's](https://arxiv.org/abs/2610.02769) | gevolgtrekking uit de controle met door elkaar gezette acties |
| De preprint werd op 2 oktober 2026 ingediend | GEVERIFIEERD | [arXiv-vermelding](https://arxiv.org/abs/2610.02769) | arXiv-metadata |
