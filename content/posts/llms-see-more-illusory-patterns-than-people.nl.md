+++
title = "LLM's zien meer denkbeeldige patronen dan mensen"
slug = "llms-zien-meer-denkbeeldige-patronen-dan-mensen"
description = "Een preprint vindt dat taalmodellen gemakkelijker dan menselijke deelnemers relaties afleiden uit dubbelzinnig bewijs. De gecontroleerde tests verbinden het effect met frequentiegevoelige interne kenmerken."
tags = ["research", "models"]
date = 2026-10-12T04:01:37+02:00
draft = false
+++

Taalmodellen vormden sterkere onjuiste patronen dan mensen wanneer beide relaties moesten afleiden uit dubbelzinnig bewijs, volgens een nieuwe preprint.

De auteurs pasten klassieke psychologische experimenten aan waarin de waarnemingen geen betrouwbaar verband bevatten, maar mensen er toch vaak één zien. Ze gaven vergelijkbare taken aan menselijke deelnemers en verschillende taalmodellen en testten vervolgens of de modellen veelvoorkomende positieve beschrijvingen met meerderheidsgroepen verbonden of causale verklaringen uit toevallige reeksen opbouwden.

## Waarom dit ertoe doet {#why-it-matters}

Voor een analist die een model gebruikt om enquêteopmerkingen, incidentverslagen of klantgegevens te interpreteren, kan vloeiend patroonzoeken een onevenwichtige steekproef in een zelfverzekerd verhaal veranderen. Het onderzoek suggereert dat meer waarnemingen toevoegen het probleem niet noodzakelijk oplost wanneer ruwe frequentie zelf de gevolgtrekking stuurt.

De centrale vergelijking omvat twee vormen van denkbeeldige patroonwaarneming. Bij de ene verschijnt een meerderheidsgroep vaker en verzamelt die daardoor meer positieve en negatieve voorbeelden, hoewel de verhoudingen gelijk zijn aan die van een minderheidsgroep. Bij de andere worden niet-verwante gebeurtenissen zo geordend dat een causale reeks verleidelijk maar ongefundeerd is.

In de gemelde experimenten onderschreven modellen vaker dan menselijke deelnemers het misleidende verband of de causale verklaring. De exacte omvang verschilde per taak en model, zodat de richting en consistentie van de kloof het nuttige resultaat van het artikel zijn, en niet één universeel percentage.

De onderzoekers gebruikten ook sparse autoencoders, tools die de dichte interne activiteit van een model omzetten in een kleinere set interpreteerbare kenmerken. Ze melden dat kenmerken die met holistische frequentiewaarneming samenhangen toenamen met het antwoord dat een onjuist patroon zag, terwijl kenmerken die met een analytischere benadering samenhangen de andere kant op werkten. Dit is een correlatie binnen het model, geen bewijs dat een van beide kenmerken het oordeel veroorzaakt.

## De vergelijking is gecontroleerd maar beperkt

De kracht van het artikel is de directe vergelijking met mensen. Beide groepen krijgen versies van hetzelfde bewijs en de taken stammen af van gevestigde demonstraties uit de cognitieve psychologie. De auteurs publiceerden ook code, zodat andere onderzoekers prompts, modellen en bemonsteringsinstellingen kunnen variëren.

De beperkingen zijn relevant. Een taalmodelantwoord wordt gegenereerd vanuit trainingsdata en promptconventies, terwijl het antwoord van een deelnemer een persoon in een experiment weerspiegelt. Het gelijkmaken van de zichtbare taak maakt die processen niet gelijkwaardig. De gemelde modellen en prompts zijn ook een steekproef uit een snel veranderende populatie, geen vaste eigenschap van alle taalmodellen.

Het werk identificeert niettemin een concrete faalwijze: een model kan het aantal waargenomen voorbeelden als bewijs over verhoudingen of oorzaken behandelen. Dat onderscheid is eenvoudig genoeg om in uitgerolde systemen te testen door verhoudingen constant te houden terwijl de groepsgrootte verandert.

## Het onderzoek vond ook

Het onjuiste verband werd sterker wanneer het bewijs een holistische lezing stimuleerde, wat relevant is omdat veel samenvattingsprompts om één overkoepelend patroon vragen. Een analytische inkadering verminderde de neiging in sommige condities, wat suggereert dat instructies het antwoord kunnen verschuiven zonder de onderliggende gevoeligheid weg te nemen.

De preprint en de code zijn nu beschikbaar. Replicaties met nieuwere modellen en natuurlijke operationele data zouden laten zien of het laboratoriumeffect fouten in echt analytisch werk voorspelt.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
|---|---|---|---|
| De preprint meldt sterkere denkbeeldige patroonwaarneming bij de geteste taalmodellen dan bij menselijke deelnemers | VOLGENS HET BEDRIJF | https://arxiv.org/abs/2610.07791 | geen |
| De experimenten passen klassieke taken voor denkbeeldige correlaties en causale patronen aan | GEVERIFIEERD | https://arxiv.org/abs/2610.07791 | geen |
| Sparse-autoencoderkenmerken die samenhangen met frequentiegevoeligheid en analytische oriëntatie volgen het gemelde effect | VOLGENS HET BEDRIJF | https://arxiv.org/abs/2610.07791 | geen |
| Het resultaat over interne kenmerken is correlationeel en geen causale interventie | GEVERIFIEERD | https://arxiv.org/abs/2610.07791 | geen |
| De auteurs publiceerden code voor de experimenten | GEVERIFIEERD | https://arxiv.org/abs/2610.07791 | geen |
