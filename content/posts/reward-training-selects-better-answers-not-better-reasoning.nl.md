+++
title = "Beloningstraining kiest betere antwoorden, geen beter redeneren"
slug = "beloningstraining-kiest-betere-antwoorden"
description = "Een nieuwe studie volgde elk checkpoint in de reinforcement learning van een klein model. De nauwkeurigheid verbeterde, maar het model ontwikkelde geen scherpere interne representatie van redeneerfouten; het werd beter in het selecteren van oplossingen die het al kende."
tags = ["research", "models"]
date = 2026-11-08T04:18:00+01:00
draft = false
+++

Neem een leerling die een wiskundeopgave in de helft van de gevallen kan oplossen. Een docent beloont elk correct antwoord en zegt niets over de stappen. Na weken oefenen antwoordt de leerling vaker goed. De verleidelijke conclusie is dat de leerling beter heeft leren rekenen. In dit denkbeeldige klaslokaal vindt een nadere test echter dezelfde verzameling goede en slechte aanpakken als voorheen. De leerling is beter geworden in het kiezen daaruit.

## De volledige training volgen

Dat onderscheid staat centraal in *RLVR Sharpens the Pencil, Not the Mind*, een nieuwe preprint van Shreeyam Bangera en Manya Gupta. De onderzoekers volgen OLMo-2-1B gedurende 13 checkpoints van reinforcement learning met verifieerbare beloningen, oftewel RLVR. In plaats van alleen het model vóór en na de training te vergelijken, onderzoeken ze wat er onderweg verandert.

RLVR kreeg bekendheid doordat een correct antwoord op een wiskunde- of programmeerprobleem automatisch kan worden gecontroleerd. Een trainingssysteem genereert oplossingen, kent beloningen toe en verhoogt de kans op gedrag dat die beloningen opleverde. DeepSeek-R1 liet zien hoe ver deze aanpak kon gaan: het R1-Zero-model ontwikkelde betere wiskunde- en programmeerprestaties via reinforcement learning zonder voorafgaande fase van finetuning onder begeleiding.

De zichtbare prestatiewinst riep een moeilijkere vraag op. Leert beloningstraining een model nieuwe redeneervaardigheden, of maakt ze bestaande vaardigheden beter bereikbaar? De tweede verklaring staat bekend als aanscherping. Een voorgetraind model kan al een goed oplossingspad bevatten, maar daaraan een te lage waarschijnlijkheid toekennen om het bij de eerste poging te gebruiken.

Bangera en Gupta benutten de openheid van OLMo om die verklaring gedurende het trainingstraject te toetsen. Ai2 publiceert tussentijdse checkpoints van de RLVR-training van het model met één miljard parameters. De auteurs evalueren die checkpoints op GSM8K, een dataset van 8.500 rekenverhaaltjes op basisschoolniveau die Karl Cobbe en collega's introduceerden.

## Betrouwbaardere toegang tot oude oplossingen

De nauwkeurigheid bij de eerste poging stijgt van 58,0 procent aan het begin van de training naar 61,3 procent aan het einde. De stijging is reëel maar bescheiden. Een onthullender meting ontstaat door het model dezelfde opgave 256 keer voor te leggen en te controleren of een van de gegenereerde antwoorden een correcte oplossing bevat. Dat aandeel opgaven met minstens één correcte oplossing begint bij 94,5 procent en eindigt bij 96,9 procent.

Het basismodel kon vóór RLVR dus al voor bijna elke opgave een geldig antwoord produceren. Door de training verschenen die geldige paden vaker bij de eerste poging. Er ontstond geen groot nieuw gebied van opgaven die het model pas daarna kon oplossen.

Het aandeel oplosbare opgaven kan niet onthullen wat het model intern representeert. Een model kan af en toe al het juiste antwoord genereren en tijdens de training toch een beter begrip van redeneren ontwikkelen. De onderzoekers toetsen die mogelijkheid door drie soorten fouten in uitgewerkte oplossingsstappen in te voegen. Vervolgens trainen ze lineaire meetmodellen op de activaties van het model om de fouten te herkennen.

De prestaties van die meetmodellen blijven over alle 13 checkpoints tussen 0,798 en 0,840 AUROC. De variatie is kleiner dan het betrouwbaarheidsinterval. Bij deze test wordt het model niet beter in het intern onderscheiden van deugdelijk redeneren en een opzettelijk ingevoegde fout.

Eén intern signaal verandert wel duidelijk. Een meetmodel kan vroege van late checkpoints onderscheiden met 0,93 AUROC bij het token van het eindantwoord. Toegepast op tokens in de redeneerstappen presteert hetzelfde meetmodel rond toevalsniveau. De training lijkt de beslissing aan het einde van de oplossing sterker te reorganiseren dan de representaties die tijdens het opbouwen ervan worden gebruikt.

## Wat het resultaat wel en niet laat zien

De titel van de studie trekt een scherpe grens, maar het experiment is beperkt. Het onderzoekt één modelfamilie met één miljard parameters, één wiskundebenchmark en één RLVR-training. Lineaire meetmodellen kunnen informatie missen die aanwezig is in een vorm die ze niet kunnen decoderen. GSM8K beloont een kort eindantwoord en vertegenwoordigt niet de open taken waarvoor correctheid moeilijk te verifiëren is.

De auteurs tonen ook niet aan dat RLVR nooit nieuwe redeneervaardigheden creëert. Hun bewijs ondersteunt een beperktere stelling: in deze training wordt de waargenomen winst beter verklaard door een betere selectie van bestaande oplossingspaden dan door een scherpere interne representatie van de geteste fouten.

Die nuancering is van belang omdat RLVR vaak wordt beschreven aan de hand van zichtbaar gedrag. Een model produceert langere ketens, probeert alternatieve aanpakken en komt tot meer correcte antwoorden. Die veranderingen kunnen op nieuw begrip lijken. De analyse van checkpoints laat zien dat de uitvoer kan verbeteren terwijl een meting van het redeneerproces vrijwel gelijk blijft.

De bevinding verduidelijkt ook waarom het genereren van meerdere antwoorden nuttig blijft na reinforcement learning. Als de kennis van een model meer oplossingen omvat dan het eerste antwoord laat zien, brengen herhaalde pogingen capaciteiten aan het licht die één uitvoering mist. RLVR verandert de kansverdeling over die pogingen. Het maakt de nauwkeurigheid bij één poging geen volledige maatstaf voor wat het model weet.

## Trainen op het proces

Verifieerbare eindantwoorden zijn aantrekkelijk omdat ze goedkoop en objectief zijn. Een getal is correct of niet. Een programma slaagt voor zijn tests of zakt ervoor. De beloning hoeft niet aan te geven welke redeneerstap hielp, welke verkorte aanpak elders zal mislukken of of het model zijn eigen fout herkende.

Het trainen van een betere representatie van fouten zou een signaal vereisen dat dichter bij het proces ligt. Dat kan bestaan uit geverifieerde tussenstappen, opzettelijk ingevoegde misleidende fouten, begeleiding van het redeneerproces of taken die goed gekalibreerde zelfcorrectie belonen. Elke optie kost meer dan het controleren van een eindantwoord en brengt een eigen beoordelingsprobleem mee.

De studie schrijft geen van deze methoden voor. Ze levert een diagnostische aanpak die toekomstig onderzoek kan hergebruiken: tussentijdse checkpoints bewaren, het aandeel oplosbare opgaven meten in plaats van alleen eerste pogingen, en de tokens waar het redeneren plaatsvindt apart onderzoeken van het token dat een antwoord vastlegt. Een score van vóór en na de training verliest het pad dat de winst verklaart.

Deze les reikt verder dan wiskunde. Agents ontvangen beloningen voor afgehandelde tickets, geslaagde tests of succesvolle toolaanroepen. Als de training vooral de selectie tussen bestaande gedragingen verbetert, kan de agent capabeler lijken zonder beter te worden in het herkennen van een ondeugdelijk plan. Evaluatie vereist dan zowel uitkomsten als tests van fouten op procesniveau.

Terug naar de verzonnen leerling, nog een week later. De juiste antwoorden komen nu sneller en de grafiek van de docent stijgt. Voordat de docent naar moeilijkere stof overstapt, voegt die één plausibele fout toe aan een uitgewerkte oplossing en vraagt de leerling die te vinden. De stilte die volgt, meet iets wat de beloningsgrafiek niet liet zien.

## Referenties

- Ai2. (2025). *OLMo-2-0425-1B-SFT model card*. https://huggingface.co/allenai/OLMo-2-0425-1B-SFT
- Bangera, S., & Gupta, M. (2026). *RLVR Sharpens the Pencil, Not the Mind*. https://arxiv.org/abs/2611.02574
- Cobbe, K., Kosaraju, V., Bavarian, M., et al. (2021). *Training Verifiers to Solve Math Word Problems*. https://arxiv.org/abs/2110.14168
- DeepSeek-AI. (2025). *DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning*. https://arxiv.org/abs/2501.12948
