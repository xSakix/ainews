+++
title = "OpenTPU draait lokale modellen op een FPGA-kaart van 300 dollar"
slug = "opentpu-draait-lokale-modellen-op-fpga-van-300-dollar"
description = "Het project met Apache-licentie publiceert zijn acceleratorontwerp, compiler, simulator en hosttools. De gemeten doorvoer toont een klein systeem met geheugenbeperkingen, geen GPU-vervanger."
tags = ["hardware", "projects", "models"]
date = 2026-10-07T03:58:57+02:00
draft = false
+++

OpenTPU heeft een volledige AI-acceleratorstack gepubliceerd die moderne taalmodellen op een Kintex-7-FPGA-kaart van ongeveer 300 dollar draait.

De Apache-2.0-repository omvat SystemVerilog-hardware, een instructieset, een bit-exacte simulator, een kerneltaal en compiler, profileringstools en hostsoftware. De waarde zit in de inspecteerbaarheid: dezelfde kleine codebasis loopt van Python-modelkernels tot de signalen op een fysieke PCIe-kaart.

## Waarom dit ertoe doet {#why-it-matters}

Een ontwikkelaar die inferentiehardware bestudeert, kan volgen waar elke cyclus en geheugenoverdracht heen gaat zonder een datacenteraccelerator nodig te hebben. De resulterende machine is traag naast huidige GPU's, maar haar beperkingen maken het knelpunt uitzonderlijk zichtbaar.

OpenTPU meldt 30,7 gegenereerde tokens per seconde voor een vierbits Qwen3-0.6B-model en 82,1 voor LFM2.5-230M, inclusief hostoverhead. Grotere dense modellen vertragen tot 12,03 tokens per seconde voor Qwen3.5-2B en 3,75 voor Gemma 4 E4B in de vermelde configuraties.

Tijdens het decoderen bereikt de kaart 82 tot 94 procent van de piek van 17,1 GB/s van haar twee DDR3-kanalen. Dat maakt geheugenbandbreedte, en niet matrixberekeningen, tot de beperkende factor. Een systolische eenheid met vier kolommen helpt promptverwerking meer dan generatie token voor token.

Modellen die groter zijn dan de 4 GiB van de kaart kunnen mixture-of-experts-gewichten uit hostopslag streamen. De repository meldt 10,6 tokens per seconde voor LFM2.5-8B-A1B en 3,95 voor Qwen3.5-35B-A3B, waarbij dat laatste model per token 153 MB via PCIe verplaatst. Dit zijn eigen metingen van het project, maar de scripts, gedateerde builds en meetomstandigheden zijn openbaar.

De omschrijving “ontwikkeld door AI” vraagt zorgvuldigheid. Volgens het project produceerde een door mensen aangestuurde agentworkflow een groot deel van het ontwerp en de optimalisatie. Dat toont echter niet aan dat een autonoom systeem besloot zijn eigen hardware te maken. Het concrete resultaat is de vrijgegeven stack en de gemelde bit-voor-bit-overeenkomst tussen kaart en simulator.

De volgende tests zijn eenvoudig te omschrijven: reproduceer de gepubliceerde bitstreams op dezelfde kaart, vergelijk stroomverbruik en latentie met goedkope GPU's en onderzoek of externe bijdragers de architectuur kunnen veranderen zonder de gelijkwaardigheid met de simulator te verbreken.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
| --- | --- | --- | --- |
| OpenTPU publiceert hardware, ISA, simulator, compiler en hosttools onder Apache-2.0 | GEVERIFIEERD | [OpenTPU-repository](https://github.com/FeSens/openTPU) | bestanden en licentie zijn toegankelijk |
| Qwen3-0.6B bereikt over de totale uitvoeringstijd 30,7 tokens/s en LFM2.5-230M bereikt 82,1 in vierbits configuraties | VOLGENS HET BEDRIJF | [OpenTPU-metingen](https://github.com/FeSens/openTPU) | geen |
| Decoderen gebruikt 82% tot 94% van een DDR3-piek van 17,1 GB/s | VOLGENS HET BEDRIJF | [OpenTPU-metingen](https://github.com/FeSens/openTPU) | geen |
| Qwen3.5-35B-A3B bereikt 3,95 tokens/s bij het streamen van 153 MB per token | VOLGENS HET BEDRIJF | [OpenTPU-metingen](https://github.com/FeSens/openTPU) | geen |
| De kaart reproduceert simulatortokens bit voor bit | VOLGENS HET BEDRIJF | [OpenTPU-repository](https://github.com/FeSens/openTPU) | openbare tests bestaan; geen onafhankelijke hardwarereproductie gevonden |
| “Ontwikkeld door AI” toont geen autonome hardwareontwikkeling aan | ANALYSE | [OpenTPU-repository](https://github.com/FeSens/openTPU) | onderscheid volgt uit de gedocumenteerde, door mensen aangestuurde workflow |
