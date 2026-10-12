+++
title = "Modellen kunnen niet zeggen wanneer ze gekwantiseerd zijn"
slug = "modellen-kunnen-niet-zeggen-wanneer-ze-gekwantiseerd-zijn"
description = "Een preprint vindt dat modellen hun eigen kwantisatie niet betrouwbaar vanuit tekstgedrag rapporteren. Interne probes kunnen bekende methoden herkennen, maar generaliseren niet naar een ongeziene methode."
tags = ["research", "models"]
date = 2026-10-12T04:00:37+02:00
draft = false
+++

Taalmodellen konden niet betrouwbaar zeggen of hun gewichten waren gekwantiseerd, hoewel getrainde probes methodespecifieke sporen uit hun verborgen toestanden konden terughalen.

De preprint onderzoekt een beperkte vorm van modelzelfkennis. Onderzoekers comprimeerden modellen met verschillende kwantisatiemethoden, stelden directe vragen over hun toestand en vergeleken hun uitvoer met die van ongecomprimeerde versies. Vervolgens trainden ze eenvoudige classifiers op interne activaties om te zien of de verandering bestond zonder voor het modelantwoord beschikbaar te zijn.

## Waarom dit ertoe doet {#why-it-matters}

Voor een ingenieur die een gehost of opnieuw verpakt model ontvangt, is zelfbeschrijving een slechte integriteitscontrole. Een model kan met gewijzigde numerieke gewichten werken zonder dat interne verschil in een waarheidsgetrouwe uitspraak over zijn uitrol om te zetten.

Kwantisatie slaat gewichten met minder bits op, zodat een model minder geheugen nodig heeft en vaak sneller draait. Het proces verandert berekeningen door het hele netwerk, maar hoeft geen duidelijk tekstueel kenmerk op te leveren. De auteurs melden dat directe zelfrapportages en gewone uitvoervergelijkingen vrijwel geen betrouwbaar signaal bevatten over de vraag of compressie had plaatsgevonden.

Het beeld veranderde toen de onderzoekers verborgen toestanden inspecteerden. Lineaire probes — kleine classifiers getraind op die interne waarden — onderscheidden gekwantiseerde van ongekwantiseerde runs en identificeerden vaak de gebruikte methode. De bevinding laat zien dat het netwerk detecteerbare sporen van zijn implementatie bevat, zelfs wanneer zijn taalinterface die niet blootlegt.

## Een vingerafdruk is geen algemene zelfkennis

De sterkste beperking verschijnt in de overdrachtstest. Een gedeelde adapter met lage rang leerde verschillende bekende kwantisatiesignaturen lezen, maar identificeerde niet betrouwbaar een methode die tijdens training was achtergehouden. Hij had vingerafdrukken van vertrouwde transformaties geleerd in plaats van een algemeen begrip van verminderde numerieke precisie.

Dat onderscheid beperkt de beveiligingsconclusie. Een beheerder met toegang tot activaties kan een detector bouwen voor uitrolvarianten die al in trainingsdata vertegenwoordigd zijn. Het experiment toont geen universele detector voor willekeurige gewichtenwijzigingen aan, en een API-klant kan doorgaans de verborgen toestanden van de aanbieder niet lezen.

De auteurs noemen het verschil anosognosie, naar een klinische term voor het ontbreken van besef van een beperking. De analogie is alleen op gedragsniveau nuttig: het systeem bevat bewijs van een verandering maar rapporteert die niet nauwkeurig. Het artikel toont geen bewustzijn, subjectief besef of klinische aandoening aan.

Methodologisch profiteert het onderzoek van een gecontroleerde interventie. Het basismodel en de prompts kunnen gelijk blijven terwijl alleen de gewichtenrepresentatie verandert, en de onderzoekers kunnen zelfrapportage, extern gedrag en verborgen activiteit afzonderlijk testen. De reikwijdte blijft beperkt tot de modellen, precisieschema's en probefamilies die in de preprint zijn geëvalueerd.

## Het onderzoek vond ook

Verschillende kwantisatiemethoden lieten onderscheidbare interne signaturen achter, wat uitrolaudits kan helpen wanneer een bekende set varianten wordt overwogen. Tekstuitvoer veranderde te weinig voor dezelfde taak, wat waarschuwt tegen integriteitstests die alleen bemonsterde antwoorden onderzoeken.

Het volgende bewijs zal onbekende compressietools en opzettelijke ontwijking moeten testen. De auteurs hebben vastgesteld dat bekende transformaties leesbare sporen kunnen achterlaten, terwijl hun eigen resultaat met een achtergehouden methode laat zien waarom dat nog geen algemene oplossing is.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
|---|---|---|---|
| Geteste modellen rapporteerden niet betrouwbaar zelf of ze waren gekwantiseerd | VOLGENS HET BEDRIJF | https://arxiv.org/abs/2610.06174 | geen |
| Lineaire probes haalden methodespecifieke informatie uit verborgen toestanden terug | VOLGENS HET BEDRIJF | https://arxiv.org/abs/2610.06174 | geen |
| Een gedeelde adapter generaliseerde niet betrouwbaar naar een ongeziene kwantisatiemethode | VOLGENS HET BEDRIJF | https://arxiv.org/abs/2610.06174 | geen |
| Kwantisatie werd gevarieerd terwijl het onderzoek tekstgedrag en interne activaties vergeleek | GEVERIFIEERD | https://arxiv.org/abs/2610.06174 | geen |
| Het artikel toont geen bewustzijn of klinische anosognosie aan | ANALYSE | https://arxiv.org/abs/2610.06174 | geen |
