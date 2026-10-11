+++
title = "Nish Tahir herkalibreert een klein beslismodel"
slug = "nish-tahir-herkalibreert-klein-beslismodel"
description = "Een uitvoerbaar experiment maakt Qwen3-1.7B tot een classifier met één doorgang en toont vervolgens dat zijn zekerheid te hoog is. Temperatuurschaling verbetert de waarschijnlijkheden."
tags = ["models", "research", "essays"]
date = 2026-10-11T04:01:06+02:00
draft = false
+++

Onafhankelijk ingenieur Nish Tahir heeft een uitvoerbaar experiment gepubliceerd dat Qwen3-1.7B tot een beslismodel met één doorgang maakt en vervolgens meet hoe slecht zijn zekerheid bij zijn nauwkeurigheid past.

De methode beperkt de uitvoerwoordenschat van het model tot antwoordtokens A tot en met E en leest hun waarschijnlijkheden na één voorwaartse doorgang. Op CommonsenseQA meldt Tahir 59,4 procent nauwkeurigheid voor het basismodel en 62,4 procent na een korte finetuningrun.

## Waarom dit ertoe doet {#why-it-matters}

Een ontwikkelaar die een routeringssysteem of risicoscore bouwt, moet meer weten dan welke optie won. Als een model 95 procent zegt maar slechts zeven van de tien keer gelijk heeft, gedragen drempels op basis van dat getal zich onvoorspelbaar. Tahirs experiment laat de volledige route van logits naar een gemeten kalibratieprobleem zien, met een model dat klein genoeg is om het experiment te reproduceren.

De winst in nauwkeurigheid is niet het meest informatieve resultaat. Antwoorden met een toegekende zekerheid tussen 90 en 100 procent waren slechts ongeveer 70 procent van de tijd correct. In de band van 80 tot 90 procent was de nauwkeurigheid ongeveer 40 procent. Het model onderscheidde keuzes dus goed genoeg om beter dan toeval te presteren, maar uitte veel meer zekerheid dan zijn resultaten rechtvaardigden.

Tahir past temperatuurschaling toe om de waarschijnlijkheden te corrigeren. De methode leert één scalair op apart gehouden voorbeelden en deelt de logits erdoor vóór de softmaxbewerking. Het verhogen van de temperatuur vlakt een te zekere distributie af zonder te veranderen welk antwoord de hoogste score heeft.

Dat maakt temperatuurschaling tot een kalibratiestap, geen vaardigheidsupgrade. Ze kan verkeerde rangschikkingen niet herstellen of ontbrekende kennis aanleren. De waarde is dat een gemelde 70 procent dichter bij zeven correcte gevallen op tien kan komen op data die op de kalibratieset lijken.

Het verslag bevat een compacte PyTorch-implementatie en interactieve demonstraties. Het maakt ook een ontwerpkeuze zichtbaar die veel beslismodelproducten verbergen: het antwoordschema moet vooraf bekend zijn en netjes op een kleine set tokens worden afgebeeld. Een taak met dubbelzinnige labels, ontbrekende opties of meerdere geldige antwoorden doorbreekt die eenvoud.

De resultaten komen uit één klein model, één benchmark en de eigen trainingsopstelling van de auteur. Meerkeuzevragen van CommonsenseQA bootsen documentroutering, fraudebeoordeling of toolselectie niet na, en kalibratie kan verschuiven wanneer de invoerdistributie verandert. Elke uitrol zou eigen apart gehouden data en periodieke controles nodig hebben.

Het artikel is juist nuttig omdat het die zwakte meldt in plaats van de zekerheidsuitvoer als inherent betrouwbaar te presenteren. De code en demonstraties zijn nu beschikbaar en geven praktijkgebruikers een korte basislijn waartegen grotere gespecialiseerde beslismodellen kunnen worden getest.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
|---|---|---|---|
| Het experiment beperkt Qwen3-1.7B tot antwoordtokens A tot en met E en leest één voorwaartse doorgang | GEVERIFIEERD | https://nishtahir.com/build-your-own-decision-model/ | geen |
| Het basismodel scoorde 59,4% en het kort gefinetunede model 62,4% op CommonsenseQA | VOLGENS HET BEDRIJF | https://nishtahir.com/build-your-own-decision-model/ | geen |
| De zekerheidsband van 90% tot 100% was ongeveer 70% van de tijd correct | VOLGENS HET BEDRIJF | https://nishtahir.com/build-your-own-decision-model/ | geen |
| De zekerheidsband van 80% tot 90% was ongeveer 40% van de tijd correct | VOLGENS HET BEDRIJF | https://nishtahir.com/build-your-own-decision-model/ | geen |
| Temperatuurschaling verandert de scherpte van waarschijnlijkheden zonder het hoogst gerangschikte antwoord te veranderen | GEVERIFIEERD | https://nishtahir.com/build-your-own-decision-model/ | geen |
