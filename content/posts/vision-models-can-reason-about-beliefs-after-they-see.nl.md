+++
title = "Visuele modellen begrijpen overtuigingen als ze goed zien"
slug = "visuele-modellen-begrijpen-overtuigingen-als-ze-goed-zien"
description = "Zeven vision-language-modellen verloren meer dan 20 punten toen problemen met onjuiste overtuigingen van tekst naar beeld gingen. Een gecontroleerde studie wees uit dat waarneming, niet de laatste redeneerstap, het grootste deel van de kloof veroorzaakte."
tags = ["research", "models"]
date = 2026-11-10T04:04:14+01:00
draft = false
+++

Een kind kijkt naar een korte scène op een scherm. Een rode bal ligt in een la. Een personage gaat weg en een ander verplaatst de bal naar een doos. Wanneer het eerste personage terugkomt, weet het kind dat het personage in de la zal zoeken. Vervang het kind nu door een vision-language-model. Het model kan een onjuiste overtuiging in tekst uitleggen, maar het bewegende voorwerp op het scherm verandert zijn antwoord. Deze scène is een illustratie: ze beschrijft het soort taak dat een nieuwe studie isoleert.

## De visuele kloof

Mohamed Rayan Barhdadi, Syed Talal Wasim, Juergen Gall en hun collega's testten zeven vision-language-modellen op problemen met onjuiste overtuigingen. Hun preprint, geaccepteerd voor het onderdeel Evaluations and Datasets van NeurIPS 2026, beschrijft meer dan 159.000 API-aanroepen binnen een protocol met vijf condities. Modellen die bij tekstversies het menselijke prestatieniveau benaderden, verloren meer dan 20 procentpunten wanneer hetzelfde onderliggende probleem visueel werd aangeboden.

Tests met onjuiste overtuigingen hebben een lange geschiedenis in de psychologie. Ze onderzoeken of een proefpersoon de werkelijkheid kan onderscheiden van wat iemand anders over die werkelijkheid weet. In de standaardopzet wordt een voorwerp verplaatst terwijl een personage afwezig is. Voor het juiste antwoord moet de proefpersoon voorspellen wat het personage gelooft, ook al weet de proefpersoon waar het voorwerp zich werkelijk bevindt.

Recente taalmodellen presteren vaak goed op tekstversies. Michal Kosinski evalueerde elf taalmodellen met veertig speciaal ontworpen taken rond onjuiste overtuigingen en rapporteerde dat een versie van GPT-4 uit 2023 er 75 procent van oploste. Een afzonderlijke vergelijking van James Strachan en collega's wees uit dat sommige taalmodellen bij verscheidene theory-of-mind-tests het menselijke prestatieniveau evenaarden of overtroffen. Beide artikelen waarschuwden ook dat een juist antwoord niet bewijst dat een model op dezelfde manier als een mens over de gedachten van anderen redeneert. Gememoriseerde patronen, de taakstructuur en taalkundige aanwijzingen blijven alternatieve verklaringen.

De visuele setting voegt een extra afhankelijkheid toe. Voordat een model kan redeneren over wat een personage gelooft, moet het de personages, voorwerpen, locaties en veranderingen herkennen die die overtuiging bepalen. Een verkeerd antwoord kan daarom voortkomen uit sociaal redeneren, uit waarneming of uit de verbinding tussen die twee. Eén score kan die soorten fouten niet van elkaar onderscheiden.

## Vijf weergaven van hetzelfde probleem

Barhdadi en collega's ontwierpen vijf condities waarin het doel van de redeneertaak gelijk blijft, terwijl de kwaliteit en vorm van het waarnemingsmateriaal veranderen. Bij de belangrijkste ingreep kregen modellen beschrijvingen van de scène die met de werkelijke situatie overeenkwamen. Met die ondersteuning verdween een groot deel van de kloof tussen tekst en beeld. Datzelfde herstel trad niet op wanneer automatische parsers de beschrijvingen genereerden, zelfs wanneer die parsers tot de meest geavanceerde vision-language-modellen behoorden.

Dat contrast legt bloot waar de directe bottleneck zit. De modellen konden een nauwkeurige symbolische beschrijving van de scène vaak gebruiken om de overtuiging van het afwezige personage af te leiden. Ze faalden wanneer ze die beschrijving zelf uit pixels moesten opbouwen. Betere prompts bij de laatste vraag zouden informatie die de visuele voorkant al had gemist of vervormd niet terughalen.

Het foutenpatroon ondersteunt dezelfde conclusie. Zestig procent van de fouten bij onjuiste overtuigingen vertoonde een voorkeur voor de werkelijkheid: het model antwoordde met de werkelijke locatie van het voorwerp in plaats van de locatie die het afwezige personage zich zou herinneren. Dit lijkt op een onvermogen om twee representaties uit elkaar te houden. De ene beschrijft de huidige scène; de andere de scène die het personage het laatst heeft waargenomen.

Zo'n voorkeur voor de werkelijkheid kan op een tekortkoming in sociaal redeneren lijken, omdat het uiteindelijke antwoord het perspectief van het personage negeert. De gecontroleerde condities laten zien dat het model mogelijk nooit een bruikbare beschrijving van dat perspectief heeft opgebouwd. Als een parser zegt dat een personage de verplaatsing heeft gezien, of het moment mist waarop het personage wegging, krijgt de latere redeneerstap het verkeerde probleem voorgelegd.

De ondersteuning met correcte scènebeschrijvingen van de auteurs is een diagnostisch hulpmiddel, geen oplossing die direct inzetbaar is. Echte systemen krijgen zelden perfecte scènebeschrijvingen. Een assistent die een werkplek observeert, een robot die tussen mensen handelt of een tutorsysteem dat een demonstratie volgt, moet bepalen welke gebeurtenissen iedere persoon heeft gezien. Zulke systemen kunnen er niet van uitgaan dat een mens de video al heeft omgezet in precies de feiten die ertoe doen.

## Een benchmark voor de scheidslijn

Eerdere visuele theory-of-mind-benchmarks lieten al zien dat multimodale systemen moeite hebben met intenties, overtuigingen en misleidende beelden. Het nieuwe protocol brengt een scherpere scheiding aan tussen zien en afleiden. Het onderzoekt of het model het redeneerprobleem kan oplossen wanneer de waarneming constant wordt gehouden en meet vervolgens wat er gebeurt wanneer de waarnemingsondersteuning verandert.

Die scheiding is van belang voor de ontwikkeling van systemen. Een team dat een fout bij een onjuiste overtuiging ziet, zou langere redeneertrajecten of een groter taalmodel kunnen toevoegen. De studie suggereert een andere eerste test: geef het systeem een geverifieerde representatie van de scène. Als het antwoord dan juist wordt, moet het werk zich richten op het volgen van voorwerpen, het ontleden van gebeurtenissen en een geheugen per perspectief. Blijft de fout bestaan, dan verdient de component die over overtuigingen redeneert aandacht.

Het resultaat begrenst ook brede claims over de sociale intelligentie van machines. Tekstbenchmarks kunnen vaststellen dat een model een geschreven scenario aan het verwachte antwoord koppelt. Ze bewijzen niet dat het systeem het relevante scenario uit een veranderende fysieke wereld kan reconstrueren. Een model dat na het lezen van een heldere alinea de overtuiging van iemand anders bespreekt, heeft slechts de tweede helft van het werk gedaan.

Het artikel stelt code en data beschikbaar, waardoor de condities kunnen worden uitgebreid. De gerapporteerde vergelijking van zeven modellen blijft een afgebakende laboratoriumtest. Ze meet niet elk visueel model, elk soort sociale gevolgtrekking of prestaties bij ongecontroleerde video. De preprint is niet via een wetenschappelijk tijdschrift door vakgenoten beoordeeld, al biedt de acceptatie voor het conferentieonderdeel wel een formeel publicatieforum.

Terug naar het denkbeeldige kind en de bewegende bal. Een ontwikkelaar geeft het model één extra regel: het eerste personage vertrok voordat de bal werd verplaatst. Het model voorspelt nu de la. Het redeneren lijkt beter, terwijl het redeneermechanisme misschien helemaal niet is veranderd. Het ontbrekende stukje was de gebeurtenis die het model niet had gezien.

## Referenties

- Barhdadi, M. R., Wasim, S. T., Gall, J., Serpedin, E., & Kurban, H. (2026). *Perception, Not Reasoning, Limits Visual Theory of Mind*. https://arxiv.org/abs/2611.10694
- Kosinski, M. (2024). *Evaluating large language models in theory of mind tasks*. https://doi.org/10.1073/pnas.2405460121
- Strachan, J. W. A., Albergo, D., Borghini, G., Pansardi, O., Scaliti, E., Gupta, S., Saxena, K., Rufo, A., Panzeri, S., Manzi, G., Graziano, M. S. A., & Becchio, C. (2024). *Testing theory of mind in large language models and humans*. https://doi.org/10.1038/s41562-024-01882-z
