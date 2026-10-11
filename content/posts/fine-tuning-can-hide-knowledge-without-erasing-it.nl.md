+++
title = "Finetuning kan kennis verbergen zonder die te wissen"
slug = "finetuning-kan-kennis-verbergen-zonder-die-te-wissen"
description = "Een preprint onderscheidt omkeerbaar verlies van toegang van de tragere vernietiging van opgeslagen feiten. Dat onderscheid kan de diagnose van fouten bij voortdurend leren veranderen."
tags = ["research", "models"]
date = 2026-10-11T04:04:06+02:00
draft = false
+++

Kennis die tijdens finetuning verdwijnt, kan intact in een taalmodel blijven en later weer verschijnen, meldt een nieuw mechanistisch onderzoek.

Vedant Palit, Florent Draye, Nicolas Zucchet, Zhijing Jin en Bernhard Schölkopf onderzochten “schijnbaar vergeten”: een afname van het herinneren die op gewiste kennis lijkt, maar in plaats daarvan een tijdelijk probleem met de toegang weerspiegelt. Hun preprint combineert een minimaal associatief geheugen, een kleine Transformer en interventies op een voorgetraind taalmodel.

## Waarom dit ertoe doet {#why-it-matters}

Een ontwikkelaar die een model met nieuwe bedrijfsdata bijwerkt, kan de nauwkeurigheid op oudere feiten zien instorten en concluderen dat de update ze heeft vernietigd. Als het om een toegangsprobleem gaat, verspilt hertraining of het herstellen van een eerder checkpoint informatie die nog aanwezig is. De nuttige vraag wordt niet alleen hoeveel de prestaties daalden, maar ook of de oude representaties samen verplaatsten of afzonderlijk werden beschadigd.

De auteurs namen tijdens training op nieuwe feiten een patroon in drie fasen waar. Het herinneren van oude feiten stortte eerst in, herstelde hoewel de training uitsluitend op het nieuwe materiaal doorging en nam daarna opnieuw af. Eén theorie van permanent overschrijven kan het herstel in de middelste fase niet verklaren.

Hun minimale geheugen reproduceerde die curve met drie ingrediënten: oude sleutels met gedeelde structuur, nieuwe waarden geconcentreerd in één gebied en normalisatie binnen het netwerk. Finetuning duwde de oude representaties aanvankelijk in een gemeenschappelijke richting. Die verschuiving verstoorde het uitlezen, maar behield de relatieve ordening die vastlegde welk feit welk was.

Zodra de nieuwe feiten waren geleerd, nam normalisatie veel van de gemeenschappelijke verschuiving weg en werden oude antwoorden weer toegankelijk. Ondertussen stapelden kleinere, feitspecifieke veranderingen zich op. Die veranderingen wijzigden de relaties tussen herinneringen en veroorzaakten uiteindelijk blijvend verlies.

## Eén richting scheidt verbergen van erosie

Het artikel test het mechanisme in plaats van bij de curve te stoppen. In een Transformer die op synthetische data was getraind, verwijderde het aftrekken van de gedeelde verschuiving de tijdelijke instorting. In een voorgetraind taalmodel herstelde het verwijderen van één richting uit elke finetuningupdate van de gewichten volgens de auteurs oude feiten.

Die interventie maakt de verklaring sterker dan een beschrijving van veranderende benchmarkscores. Ze identificeert een laagdimensionale component die met omkeerbaar verlies samenhangt en onderscheidt die van tragere, verspreide veranderingen die afzonderlijke herinneringen beschadigen.

Het onderscheid gaat over modeltoestand, niet over menselijk geheugen. “Verborgen” kennis betekent hier dat een evaluatieprompt het verwachte antwoord niet meer ophaalt, terwijl de geometrie die het ondersteunde meetbaar blijft. Het betekent niet dat het model zich bewust iets herinnert of het feit zonder interventie kan terughalen.

De experimenten gebruiken ook bewust gecontroleerde feiten en trainingsomstandigheden. Echte finetuning mengt formaten, doelen en overlappende begrippen, en een productiemodel kan om redenen buiten dit mechanisme falen: een niet-passende prompt, gewijzigde decodering, veiligheidstraining of een nieuw antwoordbeleid. Het detecteren van een gemeenschappelijke representatieverschuiving kan daarom op zichzelf niet bevestigen dat een verloren vaardigheid herstelbaar is.

### Het onderzoek vond ook

Of vergeten vooral tijdelijk of permanent was, hing af van de nieuwe data: oude herinneringen die samen verplaatsten behielden hun relatieve geometrie, terwijl updates die ze uiteen deden bewegen destructieve erosie veroorzaakten. Normalisatie hielp het herstel verklaren door de gemeenschappelijke verplaatsing te verminderen nadat het nieuwe leren stabiliseerde. Het minimale model voorspelde kwalitatief gedrag dat later in Transformer-experimenten werd getest.

De preprint werd op 6 oktober 2026 ingediend en heeft nog geen peerreview doorlopen. De praktische waarde is een diagnostische hypothese: onderzoek, voordat elke achteruitgang na finetuning als gewiste kennis wordt beschouwd, of de representaties een verwijderbare richting delen en of herstel optreedt tijdens voortgezette training.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
|---|---|---|---|
| Het herinneren van oude feiten stortte in, herstelde tijdens voortgezette training op nieuwe feiten en nam later weer af | VOLGENS HET BEDRIJF | https://arxiv.org/abs/2610.08718 | geen |
| Een minimaal associatief geheugen reproduceerde het patroon met gedeelde sleutels, geconcentreerde waarden en normalisatie | VOLGENS HET BEDRIJF | https://arxiv.org/abs/2610.08718 | geen |
| Finetuning verplaatste oude representaties in een gemeenschappelijke richting met behoud van relatieve geometrie | VOLGENS HET BEDRIJF | https://arxiv.org/abs/2610.08718 | geen |
| Het verwijderen van de gemeenschappelijke richting nam de tijdelijke instorting in een kleine Transformer weg | VOLGENS HET BEDRIJF | https://arxiv.org/abs/2610.08718 | geen |
| Het verwijderen van één richting uit gewichtenupdates herstelde oude feiten in een voorgetraind taalmodel | VOLGENS HET BEDRIJF | https://arxiv.org/abs/2610.08718 | geen |
| Het artikel werd op 6 oktober 2026 ingediend | GEVERIFIEERD | https://arxiv.org/abs/2610.08718 | geen |
