+++
title = "Cockroach Labs geeft programmeeragents klinische rollen"
slug = "cockroach-labs-geeft-programmeeragents-klinische-rollen"
description = "MOLT Sinai leidt softwarewerk langs gespecialiseerde agents, verplichte plannen en kritische beoordeling. Het bedrijf meldt zeven teruggedraaide wijzigingen in vijf maanden."
tags = ["agents", "tools", "essays"]
date = 2026-10-11T04:03:06+02:00
draft = false
+++

Cockroach Labs heeft een pijplijn voor programmeeragents beschreven die softwareproblemen als ziekenhuispatiënten behandelt, met gespecialiseerde rollen en verplichte beoordeling voordat de implementatie begint.

Het systeem, MOLT Sinai, draait via GitHub Actions. Labels dragen toestand over tussen een triageagent, een onderzoeksfase, een Fellow die behandeling voorstelt, een Review Attending die het plan aanvalt en een ontslagfase. De auteurs zeggen dat het in vijf maanden meer dan een miljoen regels verwerkte met zeven teruggedraaide wijzigingen.

## Waarom dit ertoe doet {#why-it-matters}

Een beheerder die een repositorywijziging aan een agent delegeert, heeft meer nodig dan een vaardig model: het proces moet de reikwijdte bewaken, beslissingen zichtbaar maken en zwakke plannen stoppen voordat ze code worden. MOLT Sinai zet die vereisten om in workflowtoestand en geschreven skills in plaats van op één lange prompt of het geheugen van een agent te vertrouwen.

De sterkste regel is procedureel: geen code vóór een plan en geen plan zonder beoordeling. De Review Attending krijgt de instructie fouten te zoeken in plaats van reflexmatig mee te werken. Als werk buiten de goedgekeurde reikwijdte komt, zegt een andere regel “Niet improviseren”; de agent moet stoppen en opnieuw plannen. Tests mogen niet worden verzwakt alleen om een wijziging te laten slagen.

Adam Storm en Rafi Shamim, ingenieurs bij Cockroach Labs, melden 27 samengevoegde pull requests en 55 terugverwijzingen door beoordelaars. Ze beschrijven het toevoegen van een Db2-migratiebron in minder dan twee dagen voor 4.172 dollar aan modeltokenkosten. Hun vergelijking met een Oracle-integratie van negen maanden en ongeveer 160.000 dollar illustreert het geclaimde verschil, maar is geen gecontroleerd productiviteitsonderzoek met gelijkwaardige taken.

Het ontwerp voegt bewust bureaucratie toe. Elke overdracht kost tokens en tijd, en de auteurs zeggen dat de pijplijn trager en duurder kan zijn dan een zwerm. Het doel is niet maximale paralleliteit; het is de route van issue naar samengevoegde code inspecteerbaar maken en elke fase een afzonderlijke verantwoordelijkheid geven.

Het herbruikbare idee is kleiner dan de ziekenhuismetafoor. Bewaar toestand buiten de chat, eis een expliciet plan, scheid de auteur van de criticus en leg stopvoorwaarden in de agentinstructies vast. Die controles zijn over te nemen zonder elke rol te reproduceren.

Cockroach Labs publiceerde de workflow als een technisch verslag, niet als een onafhankelijke evaluatie. Het volgende bewijs zou bestaan uit data op repositoryniveau die vergelijkbare taken onder de pijplijn en gewone menselijke of agentworkflows vergelijken, waaronder beoordelingstijd, ernst van fouten en werk dat nooit werd samengevoegd.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
|---|---|---|---|
| MOLT Sinai gebruikt GitHub Actions, labels en rolgebonden agents om issues door een gefaseerde workflow te leiden | GEVERIFIEERD | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | geen |
| De workflow vereist een goedgekeurd plan vóór code en instrueert agents opnieuw te plannen wanneer de reikwijdte verandert | GEVERIFIEERD | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | geen |
| Cockroach Labs meldt 27 samengevoegde pull requests, 55 terugverwijzingen en zeven teruggedraaide wijzigingen in vijf maanden | VOLGENS HET BEDRIJF | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | geen |
| De Db2-migratiebron kostte minder dan twee dagen en 4.172 dollar aan tokens | VOLGENS HET BEDRIJF | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | geen |
| De auteurs zeggen dat het systeem tijd, kosten en bureaucratie toevoegt vergeleken met een zwerm | GEVERIFIEERD | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | geen |
