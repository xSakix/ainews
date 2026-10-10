+++
title = "Tencent brengt Youtu-Parsing-Omni uit"
slug = "tencent-brengt-youtu-parsing-omni-uit"
description = "Het model met 5 miljard parameters zet documenten, beelden, audio en video om in één gestructureerd JSON-formaat. Tencent heeft gewichten, code en een technisch rapport uitgebracht."
tags = ["models", "tools"]
date = 2026-10-10T04:02:41+02:00
draft = false
+++

Tencents Youtu-lab heeft een model met 5 miljard parameters uitgebracht dat zes soorten media ontleedt tot één gestructureerd JSON-formaat.

Youtu-Parsing-Omni accepteert documentpagina's, natuurlijke beelden, grafieken, meetkundige figuren, audio en video. Het kan tekst, tabellen, formules, lay-outkaders, tijdstempels, spraaktranscripties, bijschriften en beschrijvingen van camerabewegingen teruggeven zonder tussen afzonderlijke specialistische modellen te wisselen.

## Waarom dit ertoe doet {#why-it-matters}

Een ontwikkelaar van een zoek- of documentverwerkingssysteem kan gemengde media door één lokaal model sturen en een voorspelbaar schema terugkrijgen. Dat vermindert het integratiewerk dat normaal nodig is om diensten voor optische tekenherkenning, spraakherkenning en videobegrip te combineren.

Tencent heeft de gewichten gepubliceerd onder zijn eigen `youtu-parsing`-licentie, samen met een vLLM-plugin, inferentievoorbeelden en een technisch rapport. Volgens de repository volgt de evaluatiecode later, waardoor de gemelde benchmarkresultaten nog niet uitsluitend op basis van deze release te reproduceren zijn.

Het model gebruikt een gemeenschappelijke encoder voor beelden, audio en video. Bij video laten geselecteerde lagen elk frame aandacht besteden aan audio uit hetzelfde deel van de clip. Het uitvoerschema omvat zowel letterlijke elementen, zoals tekst en begrenzingskaders, als uitvoer op een hoger niveau, zoals verhalende beschrijvingen en rapporten.

Tencent meldt een score van 96,96 op OmniDocBench 1.6, net boven TeleOCR met 96,91 en PaddleOCR-VL-1.6 met 96,34 in zijn gepubliceerde tabel. Op de bredere OmniParsingBench meldt Tencent een gemiddelde van 75,08, achter Gemini 3 Pro met 77,44 maar vóór de andere geteste systemen met open gewichten. Dit zijn metingen van de uitbrenger, en de vergelijking hangt af van de benchmarkconfiguratie in het rapport.

De trainingsmethode maakt het leerlingmodel telkens tot zijn eigen leraar voor de volgende ronde. Inhoudstokens en structuurtokens krijgen verschillende vergelijkingssignalen, in een poging zowel te behouden wat een pagina zegt als hoe de elementen zich tot elkaar verhouden.

## Waarop te letten

Voor onafhankelijke tests is de beloofde evaluatiecode nodig. Commerciële gebruikers moeten ook de eigen licentie beoordelen en niet uitgaan van de ruime voorwaarden die bij sommige releases met open gewichten gebruikelijk zijn.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
|---|---|---|---|
| Tencent bracht Youtu-Parsing-Omni uit met 5 miljard parameters, gewichten, codevoorbeelden en een technisch rapport | GEVERIFIEERD | https://huggingface.co/tencent/Youtu-Parsing-Omni | https://github.com/TencentYoutuResearch/Youtu-Parsing-Omni |
| Het model accepteert documenten, beelden, grafieken, meetkunde, audio en video en levert één JSON-schema | VOLGENS HET BEDRIJF | https://huggingface.co/tencent/Youtu-Parsing-Omni | geen |
| Tencent meldt 96,96 op OmniDocBench 1.6 en 75,08 op OmniParsingBench | VOLGENS HET BEDRIJF | https://huggingface.co/tencent/Youtu-Parsing-Omni | geen |
| De release gebruikt de eigen youtu-parsing-licentie en bevat nog geen evaluatiecode | GEVERIFIEERD | https://huggingface.co/tencent/Youtu-Parsing-Omni | https://github.com/TencentYoutuResearch/Youtu-Parsing-Omni |
