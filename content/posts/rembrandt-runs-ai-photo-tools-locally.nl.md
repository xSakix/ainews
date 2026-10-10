+++
title = "Rembrandt draait AI-fototools lokaal"
slug = "rembrandt-draait-ai-fototools-lokaal"
description = "De desktopeditor met GPL-licentie combineert RAW-ontwikkeling, maskers, ruisonderdrukking en superresolutie zonder een account te vereisen of foto's te uploaden."
tags = ["projects", "tools"]
date = 2026-10-09T04:00:06+02:00
draft = false
+++

Rembrandt, een nieuwe open-sourcefoto-editor voor macOS, Windows en Linux, draait zijn door AI ondersteunde tools voor ruisonderdrukking, vergroting en maskers op het apparaat van de gebruiker.

De applicatie met GPL-licentie is een niet-destructieve RAW-ontwikkelaar en fotobibliotheek in plaats van een programma om pixels te schilderen. Ze slaat bewerkingen op in standaard XMP-sidecarbestanden, laat originele foto's ongewijzigd en vereist geen account voor haar gratis lokale functies.

**Waarom dit ertoe doet:** Fotografen kunnen rekenkundige bewerkingstools gebruiken zonder privébeelden te uploaden of hun catalogus aan een abonnementsdienst te binden. De broncode en het gewone sidecarformaat bieden ook een uitweg als de applicatie verdwijnt.

Rembrandt bevat maskers voor onderwerp, achtergrond, object en diepte, GPU-gebaseerde ruisonderdrukking, 2× en 4× superresolutie, herstel van scherpstelling, HDR- en panoramasamenvoeging, lenscorrecties en batchbewerking. Een tekstopdracht zoals “warmer en een beetje helderder” verplaatst dezelfde zichtbare bedieningselementen als handmatige bewerking; volgens het project gebruikt deze functie een lokale woordenschat in plaats van een taalmodel.

De bewerkingsengine bestaat uit JavaScript met WebGL2- en WebGPU-shaders in een kleine Rust-desktopomgeving. LibRaw verwerkt camerabestanden, terwijl genoemde open projecten componenten leveren voor vergroting, ruisonderdrukking, lensprofielen en visuele maskers. Het project zegt RAW-bestanden van meer dan 1.000 camera's te ondersteunen.

Desktopprogramma's zijn beschikbaar voor Macs met Apple silicon en Intel, Windows-systemen met x64 en Arm en Linux met x86-64 of Arm. De builds zijn nog niet digitaal ondertekend, zodat macOS- en Windows-gebruikers de waarschuwingen van hun besturingssysteem bij de eerste start moeten omzeilen. Gebruikers kunnen de applicatie ook vanaf een Linux- of macOS-computer aanbieden en via een browser op hun eigen netwerk bewerken.

De repository vergelijkt Rembrandt met Lightroom en darktable, maar de kwaliteitsclaims zijn niet onafhankelijk getest. Hij noemt ook ontbrekende functies, waaronder fotograferen met een aangesloten camera, gezichtsherkenning, afdrukken en een pluginecosysteem. Optionele cloudsynchronisatie is betaald en vereist een account; de lokale editor niet.

De huidige release, bouwinstructies en controlesommen zijn beschikbaar in de [Rembrandt-repository](https://github.com/thesnarkitecht/rembrandt). De belangrijkste volgende test is langdurig gebruik met uiteenlopende RAW-catalogi, waar kleurverwerking, cameracompatibiliteit en betrouwbare export zwaarder wegen dan een functielijst.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
|---|---|---|---|
| Rembrandt is beschikbaar voor macOS, Windows en Linux onder GPL-3.0-or-later | GEVERIFIEERD | [Repository](https://github.com/thesnarkitecht/rembrandt) | geen |
| Lokale functies vereisen geen account en foto's hoeven niet te worden geüpload | GEVERIFIEERD | [Repository](https://github.com/thesnarkitecht/rembrandt) | geen |
| Bewerkingen gebruiken XMP-sidecars en originelen blijven ongewijzigd | GEVERIFIEERD | [Repository](https://github.com/thesnarkitecht/rembrandt) | geen |
| De applicatie bevat lokale ruisonderdrukking, superresolutie en door AI ondersteunde maskers | GEVERIFIEERD | [Repository](https://github.com/thesnarkitecht/rembrandt) | geen |
| De engine gebruikt JavaScript, WebGL2/WebGPU en een Rust-desktopomgeving | GEVERIFIEERD | [Repository](https://github.com/thesnarkitecht/rembrandt) | geen |
| Het project meldt ondersteuning voor RAW-bestanden van meer dan 1.000 camera's | VOLGENS HET BEDRIJF | [Repository](https://github.com/thesnarkitecht/rembrandt) | geen |
| Huidige desktopbuilds zijn niet digitaal ondertekend | GEVERIFIEERD | [Repository](https://github.com/thesnarkitecht/rembrandt) | geen |
| Optionele cloudsynchronisatie is de enige betaalde functie en vereist een account | GEVERIFIEERD | [Repository](https://github.com/thesnarkitecht/rembrandt) | geen |
