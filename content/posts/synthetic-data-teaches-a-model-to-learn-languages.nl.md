+++
title = "Synthetische data leren een model talen te leren"
slug = "synthetische-data-leren-model-talen-te-leren"
description = "Een transformer met 300 miljoen parameters, getraind zonder natuurlijke taal, past zich binnen zijn contextvenster aan zes echte talen aan. Het experiment onderscheidt de leerstrategie van onthouden tekst."
tags = ["research", "models"]
date = 2026-10-10T04:00:41+02:00
draft = false
+++

Een transformer die uitsluitend op synthetische reeksen werd getraind, leerde zes echte talen vanuit de context te voorspellen, zonder zijn gewichten te wijzigen of tijdens de training natuurlijke taal te zien.

Lennart Carstens-Behrens en Holger Fröhlich bouwden het Prior-Fitted Language Model, of PFLM, met 300 miljoen parameters op byteniveau. Elke trainingsreeks kwam uit een nieuw bemonsterd causaal proces met eigen regels, waardoor het model de huidige reeks moest afleiden in plaats van een terugkerende synthetische taal te onthouden.

## Waarom dit ertoe doet {#why-it-matters}

Een onderzoeker naar leren binnen de context weet zelden of een model een nieuwe regel leert of iets oproept dat op zijn trainingsdata lijkt. PFLM maakt een duidelijker onderscheid: zijn bevroren gewichten bevatten een algemene strategie die is geleerd uit kunstmatige processen, terwijl de echte taal pas in de prompt verschijnt.

De synthetische generator was ontworpen om brede statistische eigenschappen van natuurlijke tekst na te bootsen, waaronder veelvoorkomende symbolen, afhankelijkheden over lange afstanden en geleidelijk verbeterende voorspelbaarheid. Hij bevatte geen woorden, grammatica of voorbeelden uit Wikipedia. Tijdens de voortraining hoefde het model alleen de volgende byte in een reeks te voorspellen, telkens uit een andere generator.

Toen de auteurs lange Wikipedia-stromen in het Engels, Chinees, Hindi, Arabisch, Japans en Koreaans aanleverden, verbeterde de voorspelling door de hele context heen. De verlieswaarde begon dicht bij de uniforme basiswaarde van acht bits per byte en daalde na één miljoen bytes tot tussen 0,9 en 2,4, afhankelijk van de taal. De modelgewichten bleven bevroren.

## Het experiment test aanpassing, niet taalvaardigheid

PFLM genereert geen verzorgd proza en toont geen begrip van betekenis aan. Het schat welke byte volgt nadat het voldoende van een onbekende bron heeft gezien. Die beperktere vaardigheid is toch relevant, omdat ze laat zien dat een model dat reeksen leert een bruikbare aanpassingsprocedure kan verwerven zonder eerst natuurlijke taal op te nemen.

Het model leest ruwe bytes in plaats van een vaste woordenschat van woorddelen. Daarmee valt een op menselijke tekst getrainde tokenizer weg als andere mogelijke route waarlangs taalstructuur het systeem zou kunnen binnendringen. De openbare repository biedt de modelintegratie en een API om stromen te beoordelen; met de vrijgegeven gewichten kunnen anderen nieuwe domeinen testen.

De auteurs vergeleken PFLM ook met klassieke algemene compressiemethoden. Ze melden dat het zes niet-tekstuele bronnen, waaronder broncode en spraakdata, na voldoende context sterker comprimeerde dan gzip en PPMd. Compressie is een directe test van voorspelling: een model dat betere waarschijnlijkheden toekent, heeft minder bits nodig om dezelfde data te coderen.

### Het onderzoek vond ook

Met stromen van getallen leerde PFLM bij benadering optellen, tellen en groottes vergelijken binnen de context. Het voorspelde deterministische reeksen, waaronder indicatoren voor priemgetallen en Rudin-Shapiro-patronen. De taalresultaten verschilden aanzienlijk tussen de zes Wikipedia-talen, met duidelijk nog ruimte tussen aanpassing en de prestaties van modellen die rechtstreeks op tekst zijn getraind.

Het werk is een preprint en het belangrijkste resultaat komt van één systeem met 300 miljoen parameters dat rond één synthetische prior is gebouwd. De generator deelt bewust statistische eigenschappen op een hoog niveau met natuurlijke data, dus het experiment laat niet zien dat een willekeurig synthetisch leerprogramma taalverwerving oplevert. Het laat zien dat zorgvuldig gekozen structurele diversiteit een herbruikbare leerprocedure kan trainen.

De code en gewichten zijn openbaar, waardoor de eerstvolgende test eenvoudig is: pas het bevroren model toe op daadwerkelijk nieuwe gestructureerde bronnen en meet wanneer de verbetering op basis van context standhoudt of wegvalt.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
|---|---|---|---|
| PFLM is een transformer met 300 miljoen parameters op byteniveau, uitsluitend getraind op synthetische niet-talige reeksen | GEVERIFIEERD | https://arxiv.org/abs/2610.05879 | https://github.com/cbl/prior-fitted-language-model |
| Het voorspellingsverlies daalde na één miljoen bytes tot 0,9–2,4 bits per byte in zes Wikipedia-talen | VOLGENS HET BEDRIJF | https://arxiv.org/abs/2610.05879 | geen |
| Het model leerde numerieke en deterministische reeksen binnen de context en versloeg gzip en PPMd op zes niet-tekstuele domeinen | VOLGENS HET BEDRIJF | https://arxiv.org/abs/2610.05879 | geen |
| Code en modelgewichten zijn openbaar beschikbaar | GEVERIFIEERD | https://github.com/cbl/prior-fitted-language-model | https://huggingface.co/lennartcb/pflm1 |
| Het resultaat onderscheidt een aangeleerde aanpassingsstrategie van onthouden tekst in natuurlijke taal | ANALYSE | https://arxiv.org/abs/2610.05879 | geen |
