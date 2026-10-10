+++
title = "Zelfrapportages van modellen laten een interne signatuur achter"
slug = "zelfrapportages-modellen-laten-interne-signatuur-achter"
description = "Een gecontroleerd onderzoek vindt dat getrouwe rapportages over aangeleerde voorkeuren meer berekeningen achter modelbeslissingen hergebruiken. Het resultaat wijst binnen nauwe grenzen op een white-boxtest voor onderbouwing."
tags = ["research", "models"]
date = 2026-10-10T04:01:41+02:00
draft = false
+++

Modellen die hun eigen aangeleerde voorkeuren nauwkeurig beschreven, hergebruikten meer van de interne berekeningen achter hun beslissingen dan modellen die confabuleerden, meldt een nieuwe preprint.

David Atkinson en David Bau van Northeastern University maakten samen met Dillon Plunkett van Eleos AI Research fictieve personages met verborgen voorkeuren en trainden Qwen3-modellen om namens hen te kiezen. De modellen werden nooit getraind om die voorkeuren uit te leggen, waardoor het team kon onderzoeken of nauwkeurige zelfrapportage vanzelf kon ontstaan.

## Waarom dit ertoe doet {#why-it-matters}

Een onderzoeker naar interpreteerbaarheid die de bewering van een model over zijn eigen toestand beoordeelt, staat meestal voor een cirkelredenering: de uitspraak klinkt aannemelijk, maar de toestand zelf is mogelijk niet te controleren. Dit experiment levert een bekende grondwaarheid en vindt een structureel verschil tussen rapportages die ermee overeenkomen en rapportages die dat niet doen.

De fictieve voorkeuren waren eenvoudige regels met vijf getallen voor kenmerken zoals de afstand tot een stadscentrum en de kamergrootte. Een model zag telkens twee opties en leerde welke zijn toegewezen personage zou kiezen. Afzonderlijke prompts vroegen het vervolgens om de voorkeursgewichten van het personage als getallen te geven.

In sommige runs ontstonden uiteindelijk nauwkeurige rapportages, hoewel de trainingsdata alleen beslissingen bevatten. Dat is relevant omdat het model niet simpelweg een uitleg uit de training kon nabootsen; het moest de aangeleerde beslisregel in taal omzetten.

## Dezelfde gewichten ondersteunen kiezen en rapporteren

De auteurs gebruikten vervolgens attribution patching, een methode die schat welke adaptercomponenten aan een specifieke uitvoer bijdragen. Ze vergeleken het patroon dat werd gebruikt om een keuze te maken met het patroon voor de rapportage over de verborgen voorkeur.

Getrouwe adapters hadden een gemiddelde overeenkomst van 0,34 tussen die patronen, tegenover 0,08 voor ongetrouwe adapters. Het onzekerheidsinterval van de auteurs voor het verschil sloot nul uit. Eenvoudig gezegd gebruikten nauwkeurige rapporteerders vaker dezelfde toegevoegde circuits voor handelen en voor het beschrijven van wat dat handelen stuurde.

Experimenten met lagen wezen in dezelfde richting. Een Qwen3-model met 14 miljard parameters dat over alle 40 lagen werd getraind, leerde de beslissingen maar rapporteerde zijn voorkeuren slecht. Beperking van de training tot ongeveer het eerste kwart tot de eerste helft van het netwerk leverde duidelijk getrouwere rapportages op, terwijl training van uitsluitend latere lagen dat effect niet opleverde. De auteurs interpreteren dit als voorkeursinformatie die terechtkomt in lagen waar bestaande mechanismen voor verwoording erbij kunnen.

Het bewijs is mechanistisch in plaats van gedragsmatig: de test hoeft de formulering van de rapportage niet te begrijpen. In principe zou dezelfde vergelijking kunnen werken bij een verhulde rapportage of een onbekende taal, mits de relevante interne componenten toegankelijk zijn.

### Het onderzoek vond ook

Grotere Qwen3-modellen leerden vaker getrouwe zelfrapportage dan kleinere varianten, hoewel sommige kleinere modellen ondanks goede beslissingen negatief gecorreleerde rapportages ontwikkelden. Een replicatie met Gemma 4 vond onder de grotere configuraties adapters met zowel hoge als lage getrouwheid. Binnen één gedeeld model was het verband tussen attributieovereenkomst en getrouwheid over personages heen positief maar zwak.

Het resultaat levert geen introspectiedetector voor uitgerolde modellen op. De voorkeursregels waren geconstrueerd, lineair en slechts vijfdimensionaal; de experimenten wijzigden lichte adapters in plaats van volledige modelgewichten; en de overeenkomstscores van getrouwe en ongetrouwe groepen overlapten. Een hoge overeenkomst ondersteunde getrouwheid in deze opzet, maar een lage score bewees geen misleiding of confabulatie.

De preprint werd op 5 oktober 2026 ingediend. De duidelijkste vervolgstap is testen of hetzelfde interne hergebruik optreedt wanneer modellen rapporteren over rijkere aangeleerde strategieën waarvan de grondwaarheid nog steeds onafhankelijk te meten is.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
|---|---|---|---|
| Het onderzoek trainde LoRA-adapters op verborgen lineaire voorkeuren en nam nauwkeurige zelfrapportage waar zonder supervisie voor zelfrapportage | VOLGENS HET BEDRIJF | https://arxiv.org/abs/2610.07186 | geen |
| Getrouwe adapters hadden gemiddeld 0,34 attributieovereenkomst tegenover 0,08 voor ongetrouwe adapters | VOLGENS HET BEDRIJF | https://arxiv.org/abs/2610.07186 | geen |
| Training van uitsluitend vroege lagen verbeterde de zelfrapportage in Qwen3-14B, terwijl training van uitsluitend late lagen dat niet deed | VOLGENS HET BEDRIJF | https://arxiv.org/abs/2610.07186 | geen |
| De methode onderscheidt groepen met overlappende scores en is getest op adapters in een gecontroleerde opzet | GEVERIFIEERD | https://arxiv.org/abs/2610.07186 | geen |
| Het artikel werd op 5 oktober 2026 ingediend door Atkinson, Plunkett en Bau | GEVERIFIEERD | https://arxiv.org/abs/2610.07186 | geen |
