+++
title = "MASS traint één model via agentteams"
slug = "mass-traint-een-model-via-agentteams"
description = "Sakana AI en UC Berkeley gebruiken één model om multi-agentworkflows te ontwerpen, uit te voeren en te beoordelen, en trainen dat model vervolgens op de beste teamuitvoer."
tags = ["research", "agents"]
date = 2026-10-12T03:58:37+02:00
draft = false
+++

Sakana AI en UC Berkeley hebben MASS geïntroduceerd, een trainingsmethode waarin één model verbetert door agentteams te ontwerpen, hun werk te beoordelen en van de beste resultaten te leren.

De preprint richt zich op onderzoekstaken waarvan antwoorden niet met een compiler of exacte oplossing te controleren zijn. In plaats van een multi-agentworkflow handmatig vast te leggen, schrijft hetzelfde onderliggende model rollen, instructies, uitvoercontracten en aanroepvolgorde, voert het het resulterende team uit en beoordeelt het kandidaat-antwoorden.

## Waarom dit ertoe doet {#why-it-matters}

Voor een team dat onderzoeksagents bouwt, is workflowontwerp doorgaans weer een handmatig promptengineeringproject. MASS maakt dat ontwerp onderdeel van training en verwijdert vervolgens de multi-agentinfrastructuur bij uitrol, zodat het verbeterde afzonderlijke model kan antwoorden zonder voor het hele zoekproces te betalen.

De methode heeft twee lussen. In de binnenste lus stelt een workflowoptimalisator geschreven teamstructuren voor en voert een uitvoerder ze uit. Een beoordelaar kiest sterkere uitvoer uit taken zonder automatische grondwaarheid. In de buitenste lus wordt het model gefinetuned op die geselecteerde teamruns en vormt het het uitgangspunt voor een volgende ronde.

De auteurs vergelijken het proces met zelfspel, maar de tegenstander is geen andere speler. Het model creëert steeds veeleisendere vormen van samenwerking voor kopieën van zichzelf en neemt vervolgens het beste gedrag op in één checkpoint. De teamtopologie is dus een tijdelijke trainingssteiger en geen blijvende vereiste voor het aanbieden van het model.

## Selectiekwaliteit is de cruciale afhankelijkheid

MASS vertrouwt op modelbeoordeling omdat de beoogde onderzoeksvragen geen deterministisch orakel hebben. Het artikel gebruikt afzonderlijke geavanceerde modellen, waaronder GPT-5.5 en Claude Opus 4.8, als buiten de training gehouden beoordelaars voor de evaluatie. Sakana meldt dat het getrainde model zijn beoordeelde antwoordkwaliteit verbetert en minder uitvoertokens gebruikt dan de multi-agentteams die zijn trainingsmateriaal genereerden.

Dat bewijs blijft intern aan evaluatie door taalmodellen. Een beoordelaar kan verzorgde, vertrouwde of uitvoerige antwoorden verkiezen zonder te meten of een onderzoeksclaim waar is. Buiten de training gehouden beoordelaars verminderen directe overfitting op één beoordelaar, maar leveren geen feitelijke grondwaarheid. Het resultaat kan het best worden gelezen als verbetering onder het beoordelingsprotocol van het artikel.

De trainingsprocedure probeert te voorkomen dat alles op één toevallig succesvolle workflow terugvalt. Elke generatie voert 18 keer een kampioenstoernooi uit en bewaart de beste 16 teamtraces voor finetuning. De optimalisator kan rolbeschrijvingen, communicatievolgorde en uitvoerformaten veranderen, wat meer vrijheid geeft dan selectie uit enkele vaste prompts.

Het ontwerp met een gedeeld model beperkt ook de claim. Uitvoerder, optimalisator en beoordelaar zijn rollen van één modelfamilie in plaats van een markt van onafhankelijk gespecialiseerde systemen. Dat maakt recursieve verbetering gemakkelijker aan de trainingslus toe te schrijven, maar laat open of heterogene teams andere strategieën zouden ontdekken.

## De workflow verdwijnt na training

De duidelijkste praktische eigenschap is distillatie naar het basismodel. Een gebruiker na uitrol hoeft het toernooi met 18 runs niet te herhalen of de uiteindelijke teamgraaf te onderhouden. Het extra rekenwerk zit geconcentreerd in datageneratie en training, terwijl inferentie het resulterende model rechtstreeks gebruikt.

Het artikel en de projectbeschrijving zijn openbaar en maken nadere inspectie van prompts en evaluatieontwerp mogelijk. Onafhankelijke reproductie moet testen of de winst standhoudt bij andere beoordelaars, feitelijke verificatie en taken buiten de onderzoeksset van de auteurs.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
|---|---|---|---|
| MASS gebruikt één model als workflowoptimalisator, uitvoerder en beoordelaar en finetunet het vervolgens op geselecteerde teamruns | GEVERIFIEERD | https://arxiv.org/abs/2610.12176 | https://pub.sakana.ai/mass/ |
| De binnenste lus doorzoekt geschreven teamrollen, instructies, uitvoercontracten en aanroepvolgorde | GEVERIFIEERD | https://arxiv.org/abs/2610.12176 | https://pub.sakana.ai/mass/ |
| De auteurs melden hogere beoordeelde kwaliteit met minder uitvoertokens na training | VOLGENS HET BEDRIJF | https://pub.sakana.ai/mass/ | geen |
| GPT-5.5 en Claude Opus 4.8 dienen als buiten de training gehouden externe beoordelaars in de gemelde evaluatie | GEVERIFIEERD | https://arxiv.org/abs/2610.12176 | geen |
| Modelbeoordeling stelt feitelijke juistheid niet onafhankelijk vast | ANALYSE | https://arxiv.org/abs/2610.12176 | geen |
