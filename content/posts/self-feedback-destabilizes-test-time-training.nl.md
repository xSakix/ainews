+++
title = "Zelfterugkoppeling destabiliseert training tijdens gebruik"
slug = "zelfterugkoppeling-destabiliseert-training-tijdens-gebruik"
description = "Een preprint beschrijft hoe modellen die hun gewichten bijwerken met hun eigen gegenereerde tekst tijdens lange inferentiestromen in een schadelijke terugkoppellus kunnen terechtkomen."
tags = ["research", "models"]
date = 2026-10-08T03:56:31+02:00
draft = false
+++

Taalmodellen die tijdens inferentie op hun eigen uitvoer trainden, werden slechter in het voorspellen van onafhankelijke menselijke tekst, vindt een preprint die de terugkoppellus over lange stromen volgde.

Training tijdens gebruik laat een model zijn gewichten bijwerken terwijl het wordt gebruikt, waardoor het model zelf een vorm van werkgeheugen wordt. Cheng Luo, Bing Li en Bernard Ghanem testten wat er gebeurt wanneer de tekst voor die updates wordt gegenereerd door hetzelfde veranderende model.

Het resultaat is relevant voor ontwikkelaars van agents die voortdurend van hun eigen werk leren. Een update kan de laatst gegenereerde passage gemakkelijker voorspelbaar maken en ondertussen de prestaties op nieuw, door mensen geschreven materiaal verminderen. Herhaling van die lokale verbetering verandert zowel de leerling als de bron van zijn volgende les.

## De generator en leerling trokken elkaar uit koers

De onderzoekers draaiden drie modelconfiguraties voor training tijdens gebruik, aangeduid als 125 miljoen, 760 miljoen en 3 miljard parameters, over stromen van 128.000 tokens. Het behouden van updates uit gegenereerde tekst verslechterde bij alle drie de voorspelling op een afzonderlijke set menselijke tekst. Gewone Adam-updates op de bestaande gewichten van Qwen3-4B leverden hetzelfde patroon op.

Leren tijdens inferentie was niet op zichzelf schadelijk. Dezelfde updatemechanismen verbeterden prestaties wanneer de binnenkomende tekst van mensen kwam. De fout ontstond wanneer modelgegenereerde tekst werd teruggevoerd naar het model dat het volgende trainingsblok zou genereren.

Het artikel isoleert die lus met gekoppelde experimenten. In “Vaste generatie” leverde een bevroren kopie de gegenereerde trainingstekst terwijl een ander model updates bleef uitvoeren. Dit verwijderde volgens de auteurs meer dan 98 procent van de gemeten schade bij de twee kleinere configuraties. De vergelijking wijst de veranderende generator, en niet synthetische tekst alleen, aan als belangrijkste bron van instabiliteit.

Een tweede herhalingsexperiment onderscheidde twee kosten. Het model moest eerst tekst lezen die mettertijd was verslechterd; vervolgens sloeg het verdere veranderingen op door op die tekst te trainen. Een gekoppelde test met één update legde het onmiddellijke conflict bloot: elke update verbeterde de voorspelling van zijn bronpassage, maar verslechterde de voorspelling van nieuwe menselijke tekst.

Dat conflict is gemakkelijk te missen wanneer het trainingssignaal en het evaluatiedoel dezelfde passage zijn. De update is volgens zijn lokale doel succesvol: het verlies daalt op de tekst die hem veroorzaakte. De schade wordt alleen zichtbaar op apart gehouden menselijke tekst, die als referentie dient voor de vraag of het model tijdens aanpassing zijn bredere taaldistributie behoudt.

## Onafhankelijk bewijs werkte als rem

De meeste runs faalden niet in gelijke mate. De auteurs melden dat een klein aantal trajecten veel van de grootste verliezen na langdurige aanpassing in een gesloten lus veroorzaakte. Die concentratie maakt gemiddelde controles over korte runs tot een zwakke veiligheidsmaatregel: een systeem kan stabiel lijken totdat één reeks zelfgegenereerde updates het verder laat afdrijven.

Lange stromen zijn relevant omdat elke geaccepteerde update het uitgangspunt voor de volgende verandert. Fouten beïnvloeden daarom meer dan de huidige voorspelling; ze veranderen welke tekst later wordt geproduceerd en gebruikt om van te leren. Het onderzoek meet dat opstapelende proces in plaats van losse zelftrainingsstappen te beoordelen.

De voorgestelde tegenmaatregel, Settlement, beoordeelt een kandidaat-update van gewichten op onafhankelijke echte tekst voordat hij wordt geaccepteerd. In de twee kleinere configuraties was het resterende gemiddelde verschil aan het eindpunt 0,07 en -0,02 nats, terwijl nuttige aanpassing aan echte tekst behouden bleef. De maatstaf meet voorspellingsverlies, dus waarden dicht bij nul betekenen dat de maatregel de kloof met de vergelijkingsconditie grotendeels sloot.

Dit zijn door de auteurs gemelde resultaten uit een eerste versie van een arXiv-preprint, zonder onafhankelijke replicatie. De geteste stromen en het voorspellingsdoel zijn beperkter dan het volledige gedrag van een uitgerolde agent, en het onderzoek stelt niet vast hoe snel dezelfde lus bij grotere geavanceerde systemen zou optreden.

Het experiment biedt niettemin een causale verklaring voor een vertrouwde intuïtie over zelftraining: controleren of een update zijn eigen bron verklaart is onvoldoende. Het volgende concrete criterium van de auteurs is extern: een update moet ook de voorspelling behouden op bewijs dat het zich aanpassende model niet heeft gegenereerd.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
|---|---|---|---|
| Het behouden van updates uit gegenereerde tekst verslechterde de voorspelling op onafhankelijke menselijke tekst bij drie configuraties voor training tijdens gebruik | VOLGENS HET BEDRIJF | [Preprint van Luo, Li en Ghanem](https://arxiv.org/abs/2610.05076) | geen |
| Dezelfde fout trad op wanneer Adam de bestaande gewichten van Qwen3-4B bijwerkte | VOLGENS HET BEDRIJF | [Preprint van Luo, Li en Ghanem](https://arxiv.org/abs/2610.05076) | geen |
| Dezelfde updatemechanismen verbeterden prestaties op echte tekst | VOLGENS HET BEDRIJF | [Preprint van Luo, Li en Ghanem](https://arxiv.org/abs/2610.05076) | geen |
| Een bevroren generator verwijderde meer dan 98% van de schade bij 125 miljoen en 760 miljoen parameters | VOLGENS HET BEDRIJF | [Preprint van Luo, Li en Ghanem](https://arxiv.org/abs/2610.05076) | geen |
| Settlement liet eindpuntverschillen van 0,07 en -0,02 nats bij 125 miljoen en 760 miljoen parameters over, met behoud van aanpassing aan echte tekst | VOLGENS HET BEDRIJF | [Preprint van Luo, Li en Ghanem](https://arxiv.org/abs/2610.05076) | geen |
| De preprint van drie auteurs werd op 4 oktober 2026 ingediend | GEVERIFIEERD | [arXiv-vermelding](https://arxiv.org/abs/2610.05076) | geen |
