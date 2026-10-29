+++
title = "Een wereldmodel kan slagen zonder de wereld te leren kennen"
slug = "wereldmodel-kan-slagen-zonder-de-wereld-te-leren-kennen"
description = "Een nieuwe preprint test of latente wereldmodellen de dynamiek van hun omgeving reproduceren. De systemen voltooiden hun taken, maar geen ervan deed dat via een getrouw intern model van die dynamiek."
tags = ["research", "models", "agents"]
date = 2026-10-29T04:04:47+01:00
draft = false
+++

Een ingenieur ziet hoe een agent zich door een gesimuleerde kamer beweegt. De agent bereikt keer op keer het doel en zijn score stijgt. De ingenieur opent het model om te onderzoeken wat het heeft geleerd en ontdekt dat de interne toestand de veranderingen in de kamer niet volgt zoals zij verwachtte. Deze ingenieur is verzonnen. De discrepantie tussen succesvol gedrag en een ongetrouw intern model is het gemeten resultaat van een nieuwe preprint.

## Succes kan het mechanisme verhullen

Rodrigo Gonzalez Laiz en Steffen Schneider onderzoeken latente wereldmodellen: systemen die waarnemingen comprimeren tot interne toestanden en leren hoe die toestanden na acties veranderen. Zulke modellen worden vaak gepresenteerd als een basis voor agents die over grote afstanden of veel stappen moeten plannen. Als de interne dynamiek de wereld voorspelt, kan een agent mogelijke acties intern testen voordat hij er één uitvoert.

De meeste evaluaties vragen of dat proces de agent helpt een taak te voltooien. Het nieuwe artikel vraagt of een aangeleerde overgang in de latente ruimte overeenkomt met de overgang die in de omgeving plaatsvond.

De auteurs noemen die eigenschap getrouwheid en drukken haar uit als een equivariantievoorwaarde. Het coderen van een toestand en vervolgens toepassen van de aangeleerde latente overgang moet overeenkomen met het eerst toepassen van de werkelijke overgang in de omgeving en daarna coderen van de resulterende toestand. De twee paden hoeven geen identieke coördinaten op te leveren, maar moeten wel dezelfde structuur behouden.

Om dit te testen introduceren de auteurs consistentie van latente uitrol. Deze maat vergelijkt latente voorspellingen die afhankelijk zijn van acties met representaties van de toestanden die de omgeving daadwerkelijk bereikt. Hij onderzoekt een reeks, in plaats van één voorspeld beeld of de uiteindelijke taakbeloning te beoordelen.

Van de toonaangevende systemen die het artikel onderzoekt, loste geen enkel zijn taak op door de dynamiek van de omgeving getrouw te modelleren. De modellen konden nog steeds nuttige representaties en succesvolle acties produceren. Hun taakscores bewezen alleen niet het interne mechanisme dat de term “wereldmodel” bij een lezer kan oproepen.

## Compressie laat ruimte voor sluiproutes

Een latent model slaat de wereld niet op in een voor mensen leesbare kaart. Het leert een gecomprimeerde representatie die nuttig is voor zijn doelstelling. Kenmerken die voor de beloning van belang zijn, kunnen behouden blijven terwijl andere verschillen verdwijnen. Een model kan ook correlaties benutten die binnen de evaluatie werken, zonder de overgangsstructuur te achterhalen die betrouwbare voorspellingen elders mogelijk zou maken.

Dit onderscheid loopt vanaf het begin mee in het onderzoek naar wereldmodellen. Ha en Schmidhuber toonden aan dat een compact aangeleerd model een besturingssysteem binnen een gegenereerde omgeving kon ondersteunen. MuZero behaalde later sterke planningsresultaten zonder waarnemingen te reconstrueren; het leerde de grootheden die nodig waren om waarde, beleid en beloning te voorspellen. DreamerV3 demonstreerde één algoritme voor meer dan 150 taken door denkbeeldige trajecten in de latente ruimte te leren.

Die projecten toonden aan dat latente voorspelling nuttig kan zijn. Ze maakten niet van elke succesvolle latente representatie een getrouwe beschrijving van de omgeving. Een representatie kan volstaan voor een benchmark en toch de structuur weglaten die nodig is voor een andere actie, een langere horizon of een veranderde situatie.

Het nieuwe artikel biedt een rechtstreekse test voor die zorg. Consistentie van latente uitrol kan naast beloning en taakvoltooiing worden gemeten. Zo kunnen onderzoekers vragen of de denkbeeldige reeks van een model de omgeving volgt of alleen het geëvalueerde handelingsbeleid ondersteunt.

## Claims over planning vereisen twee metingen

Voor agents die over lange tijdshorizonten werken, krijgt het verschil praktische betekenis. Fouten in een overgangsmodel stapelen zich op naarmate het model verder vooruitrekent. Een kleine inconsistentie na één actie kan na veel acties tot een andere denkbeeldige wereld leiden. Een agent kan toch slagen wanneer zijn beleid die gebieden vermijdt of wanneer de benchmark alleen het eindresultaat beloont.

Daarom beantwoorden taaksucces en getrouwheid verschillende vragen. Taaksucces meet of het hele systeem onder de testomstandigheden het vereiste resultaat behaalde. Getrouwheid meet of de aangeleerde dynamiek de structuur behoudt waarover de planner geacht wordt te redeneren.

Het artikel toont niet aan dat latente wereldmodellen nutteloos zijn, noch dat een getrouw model altijd nodig is. Sommige taken vereisen misschien alleen een beperkte voorspellende representatie. Een model dat irrelevante details weglaat, kan efficiënter zijn dan een model dat alles reconstrueert. Het resultaat beperkt wel de interpretatie van een hoge score: die kan op zichzelf niet aantonen dat de agent de wereld heeft leren kennen die hij lijkt te simuleren.

Het onderzoek is een preprint die op 27 oktober is ingediend en heeft geen peerreview ondergaan. De definitie van getrouwheid is bovendien één formele keuze uit meerdere mogelijke maatstaven. Vervolgonderzoek zal moeten testen of een hogere consistentie van latente uitrol betere overdracht, veiligere planning of weerbaarheid bij veranderende omgevingen voorspelt.

## De kaart heeft een eigen test nodig

Terug naar de denkbeeldige ingenieur. Ze behoudt de succesvolle taakscore, maar voegt er een andere grafiek naast. Eén lijn registreert of de agent aankwam. De andere registreert of zijn interne uitrol de overgangen volgde die daadwerkelijk plaatsvonden.

De tweede lijn vervangt de eerste niet. Ze voorkomt dat de eerste een claim moet dragen die nooit werd gemeten. Een agent kan zijn bestemming bereiken zonder de kaart te hebben geleerd.

## Referenties

- Gonzalez Laiz, R., & Schneider, S. (2026). *Understanding the limits of latent world models*. https://arxiv.org/abs/2610.37588
- Hafner, D., Pasukonis, J., Ba, J., & Lillicrap, T. (2023). *Mastering Diverse Domains through World Models*. https://arxiv.org/abs/2301.04104
- Ha, D., & Schmidhuber, J. (2018). *World Models*. https://arxiv.org/abs/1803.10122
- Schrittwieser, J., et al. (2020). *Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model*. https://www.nature.com/articles/s41586-020-03051-4
