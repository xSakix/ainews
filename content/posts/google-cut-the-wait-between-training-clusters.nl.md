+++
title = "Google verkortte de wachttijd tussen trainingsclusters"
slug = "google-verkortte-de-wachttijd-tussen-trainingsclusters"
description = "Google liet twee groepen TPU's kleinere updates uitwisselen tijdens het trainen van een model met 32 miljard parameters. De staptijd bleef stabiel bij een gesimuleerde netwerkbeperking, maar het blijft open wat de methode tussen echte datacenters zal kosten."
tags = ["research", "hardware", "models"]
date = 2026-11-22T06:29:30+01:00
draft = false
+++

Ingenieurs van Google stelden een bandbreedtelimiet in tussen twee groepen TPU's. Bij 10 gigabit per seconde duurde een stap van gewone dataparallelle training 55,11 seconden. Hetzelfde model had 5,76 seconden per stap nodig wanneer de groepen op de achtergrond kleinere updates uitwisselden.

In het experiment, dat Google in november publiceerde, werd Qwen3-32B getest op twee TPU v5p-32-slices. De slices waren verbonden via een snel netwerk. Het team gebruikte Linux traffic control om de beperkte bandbreedte te simuleren die twee groepen accelerators van elkaar kan scheiden. Dankzij die opzet kon het team de hardware en het model gelijk houden terwijl het varieerde hoeveel data er over de verbinding kon.

## Wanneer de verbinding het tempo bepaalt

Bij standaard dataparallelle training krijgt elke groep een kopie van het model en een andere batch trainingsvoorbeelden. Na het berekenen van de gradiënten, die aangeven hoe de parameters van het model moeten worden aangepast, voegen de groepen ze samen zodat de kopieën gelijk blijven lopen. Op een snel netwerk kan een deel van die uitwisseling samenvallen met het rekenwerk. Zodra de uitwisseling langer duurt dan het rekenwerk dat die overdracht kan verbergen, moeten de accelerators wachten.

Google schat dat zijn dataparallelle opstelling bij elke stap ongeveer 65,5 gigabyte over de verbinding uitwisselde. Toen de verbinding op volle snelheid draaide, had de basisopstelling ongeveer 5,6 seconden per stap nodig. Bij 30 gigabit per seconde was dat 19,41 seconden. Het model en de hoeveelheid werk per stap bleven gelijk. Het grootste deel van de extra tijd ging zitten in het overbrengen van de updates.

Dat is het probleem dat Arthur Douillard en zijn collega's wilden aanpakken met het oorspronkelijke DiLoCo-onderzoek. In hun studie naar het trainen van taalmodellen op C4 lieten de onderzoekers acht groepen telkens gedurende een periode onafhankelijk trainen en hun updates periodiek samenbrengen. Ze meldden dat ze in dat specifieke experiment de resultaten van volledig synchrone training evenaarden, terwijl ze 500 keer minder data uitwisselden. De studie gebruikte een andere opzet dan de nieuwe MaxText-benchmark, waardoor de twee afnames in dataverkeer verschillende dingen meten.

## Updates op een ander moment versturen

Het oorspronkelijke DiLoCo had nog altijd een probleem aan het einde van elke periode. De goedkopere stappen liepen op volle snelheid, waarna de groepen het hele model in één keer moesten synchroniseren. Bij de limiet van 10 gigabit in de nieuwe benchmark van Google kwam gewoon DiLoCo uit op gemiddeld 7,55 seconden per stap en bleef er een periodieke pauze bestaan. Voor een trainingssysteem dat het grootste deel van de tijd druk bezig is, kan een regelmatig terugkerende pauze een aanzienlijk deel van het gemiddelde uitmaken.

Het onderzoeksartikel over Streaming DiLoCo uit 2025 veranderde dat schema. In plaats van het hele model in één operatie te versturen, wisselen de groepen delen ervan na elkaar uit. De volgende trainingsstappen kunnen doorgaan terwijl de overdracht nog loopt. Het artikel onderzocht ook het kwantiseren van de uitgewisselde data, waardoor minder bits nodig zijn om die data weer te geven. Het onderliggende onderscheid ligt tussen de hoeveelheid data die een systeem tijdens een trainingsrun verstuurt en de hoeveelheid die het in één keer probeert te verzenden.

In het MaxText-experiment verdeelde het team Qwen3-32B in 65 fragmenten. Een groep kon blijven trainen terwijl de host-CPU's op de achtergrond ongeveer één gigabyte aan data voor een fragment synchroniseerden. Over 65 stappen daalde het dataverkeer tussen de slices van 4.258,8 gigabyte bij standaard dataparallellisme naar 67 gigabyte bij Streaming DiLoCo. De gemiddelde staptijd bleef zowel bij 30 als bij 10 gigabit per seconde op 5,76 seconden staan. Zonder bandbreedtebeperking voltooiden alle drie de methoden hun stappen in ongeveer dezelfde tijd.

## Het experiment mat meer dan alleen dataverkeer

Een model dat minder tijd kwijt is aan wachten, kan aan het einde van de training toch slechter zijn. Wanneer workers hun updates onafhankelijk uitvoeren, verandert de volgorde van gewichten die elke worker te zien krijgt. Google wees specifiek op modellen met een mixture of experts, waarbij een router bepaalt welke delen van het model elk token verwerken. Als routers te lang onafhankelijk leren, kunnen ze leren om vergelijkbare voorbeelden naar verschillende experts te sturen.

Het MaxText-team vergeleek het validatieverlies bij trainingsruns van 4.000 stappen voor twee van zulke modellen, Qwen3-30B-A3B en Gemma4-26B-A4B. Het team meldt dat de streamingruns de synchrone basisopstelling evenaarden of licht overtroffen. Bij de run met Qwen paste het team de synchronisatie aan tijdens ongeveer de eerste 800 stappen. Dat resultaat geeft aan hoe goed de runs apart gehouden data voorspelden over de geteste periode. Het laat open hoeveel afstemming andere modellen en langere runs zouden vergen.

Voor teams die capaciteit over meerdere locaties moeten veiligstellen, zijn er twee afzonderlijke vragen. De eerste is of de trainingstaak kan blijven doorrekenen terwijl updates onderweg zijn. De tweede is wat het kost om een vereist kwaliteitsniveau te bereiken wanneer het netwerk echte latentie, storingen en verkeer kent die het experiment niet nabootste. De vergelijking van de verwerkingssnelheid gebruikte één dense model en twee groepen accelerators. De kwaliteitsruns beantwoorden een andere vraag over een beperkt aantal stappen. Google geeft geen kostenvergelijking en geen meting van de tijd tot het beoogde verliesniveau voor echte locaties.

De ingenieurs waren begonnen met het opleggen van een limiet aan een verbinding die het verkeer anders aankon. Met de limiet ingeschakeld zagen ze hoe gewoon dataparallellisme bijna 50 extra seconden per stap nodig had. Streaming DiLoCo rondde een stap met de limiet in bijna dezelfde tijd af als zonder.

## Referenties

- Douillard, A., Feng, Q., Rusu, A. A., et al. (2023). *DiLoCo: Distributed Low-Communication Training of Language Models*. https://arxiv.org/abs/2311.08105
- Douillard, A., Donchev, Y., Rush, K., et al. (2025). *Streaming DiLoCo with overlapping communication: Towards a Distributed Free Lunch*. https://arxiv.org/abs/2501.18512
- Khatwani, M., Zuo, C., Fallen, N., et al. (2026). *Distributed LLM Training Across Metros: Streaming DiLoCo in MaxText*. https://developers.googleblog.com/distributed-llm-training-across-metros-streaming-diloco-in-maxtext/
