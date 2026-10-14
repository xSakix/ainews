+++
title = "LDraw Nova laat agents bewerkbare LEGO-modellen bouwen"
slug = "ldraw-nova-laat-agents-bewerkbare-lego-modellen-bouwen"
description = "Een project op basis van Docker bewaart gegenereerde modellen als LDraw-broncode en bewerkbare 3D-objecten, samen met het gesprek achter de bouw."
tags = ["projects", "agents", "tools"]
date = 2026-10-03T09:40:58+02:00
draft = false
+++

LDraw Nova, een AGPL-3.0-project van ontwikkelaar anteloc, geeft AI-agents een werkruimte om LEGO-modellen te bouwen als bewerkbare bronbestanden in plaats van gegenereerde plaatjes.

De agent plaatst onderdelen via LDraw, een tekstformaat dat de stenen, posities en rotaties van een model beschrijft. De toepassing bewaart die assemblagebeschrijving en het gesprek waarmee ze is opgebouwd, zodat het resulterende object in andere tools kan worden geopend en veranderd.

**Waarom dit ertoe doet:** Een hobbyist die een agent om een LEGO-ontwerp vraagt, krijgt een model dat onderdeel voor onderdeel kan worden geïnspecteerd en herzien. Het project exporteert ook een in Blender bewerkbaar glTF-bestand en biedt meerdere weergaven van dezelfde constructie, waaronder een virtualrealityweergave.

De webtoepassing draait in Docker en vereist twee naast elkaar geplaatste repositories: het modelbouwproject en het bijbehorende applicatiepakket. De installatie-instructies zetten beide vast op dezelfde releasetag, zodat toepassing en onderliggende tools bij elkaar passen. De gedocumenteerde eerste imagebuild vereist ongeveer 5 GB schijfruimte.

Het ophalen van onderdelen is een belangrijke afhankelijkheid. De zoektool van de ontwikkelaar combineert semantisch zoeken en herrangschikking via TypeSafe's Jev-dienst, een gehoste API voor een beslismodel. Een gebruiker met een TypeSafe-sleutel kan die rangschikkingsstap inschakelen; zonder sleutel vallen de agents terug op zoeken in volledige tekst, wat volgens de ontwikkelaar slechtere ontwerpen kan opleveren.

Het README beschrijft ook een leerprobleem dat specifiek is voor de representatie. In de ervaring van de auteur gingen agents effectiever om met Python-programma's die een model genereren dan met voltooide LDraw-bestanden, waarin de wiskunde van posities en rotaties moeilijk bleek. Die observatie betreft de ontwikkeling van dit project, in plaats van een algemene benchmark van ruimtelijk redeneren.

Opgeslagen uitvoer omvat de LDraw-broncode, gerenderde beelden, een modelspeler en gespreksgeschiedenis, terwijl de glTF-export metadata meeneemt naar Blender. Deze artefacten maken het generatieproces inspecteerbaar voorbij het uiteindelijke visuele resultaat.

De release biedt nu broncode en een demonstratievideo. Het installatieproces koppelt nog steeds twee repositories aan één tag en de beter gerangschikte onderdelenzoekfunctie steunt op een gehoste API; dat zijn de concrete afhankelijkheden achter een verder bewerkbare, lokaal draaiende ontwerpwerkruimte.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
|---|---|---|---|
| AGPL-3.0-broncode, identiteit van de ontwikkelaar, LDraw/glTF/gespreksuitvoer, Docker-installatie met twee repositories, build van ongeveer 5 GB. | GEVERIFIEERD | https://github.com/anteloc/ldraw-nova | geen |
| Jev-zoekopdrachten verbeteren ontwerpen; de terugvaloptie kan slechter zijn; voorbeelden van Python-generatie werkten beter dan voltooide LDraw. | VOLGENS HET BEDRIJF | https://github.com/anteloc/ldraw-nova | geen |
| Met bewerkbare uitvoer kan een hobbyist afzonderlijke onderdelen herzien en de bouwgeschiedenis inspecteren. | ANALYSE | https://github.com/anteloc/ldraw-nova | geen |
| Project publiek getoond in een gedateerde discussiedraad. | GEVERIFIEERD | https://news.ycombinator.com/item?id=49937916 | geen |
