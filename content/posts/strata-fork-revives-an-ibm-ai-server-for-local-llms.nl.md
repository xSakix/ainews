+++
title = "Strata-fork blaast IBM-AI-server nieuw leven in voor lokale LLM's"
slug = "strata-fork-hergebruikt-ibm-ai-server-voor-lokale-llms"
description = "Een fork voor specifieke hardware draait Qwen3.8-Flash-Next op twee POWER9-processors en vier V100-GPU's. Dat laat zien wat modelbewuste optimalisatie uit een systeem uit 2018 kan halen."
tags = ["projects", "hardware", "models"]
date = 2026-10-05T03:58:30+02:00
draft = false
+++

Een ontwikkelaar uit de gemeenschap heeft de Strata-inferentie-engine aangepast voor de AC922 van IBM, een server uit 2018 waarvan de twee POWER9-processors rechtstreeks met vier Nvidia V100-accelerators van 16 GB zijn verbonden. Het resultaat is minder een algemene vervanging voor llama.cpp dan een casestudy over het benutten van de topologie van een ongebruikelijke machine voor een modern mixture-of-experts-model.

De fork draait een gekwantiseerde Qwen3.8-Flash-Next, een model met 125 miljard parameters waarvan het schaarse ontwerp slechts een klein deel van de experts per token activeert. Strata houdt veelgebruikte experts op de GPU's en de volledige verzameling experts in het systeemgeheugen. Die opzet past bij de AC922, omdat zijn CPU's en GPU's NVLink 2.0-verbindingen met hoge bandbreedte delen en niet uitsluitend via gewone PCIe communiceren.

De ontwikkelaar voegde een gebied met vastgezette geheugenpagina's toe voor elke CPU-socket, plaatste experts rekening houdend met de niet-uniforme geheugenindeling van de machine en liet een anders ongebruikte naburige GPU gegevens ophalen via zijn eigen NVLink. Andere wijzigingen omvatten FP16-Volta-tensorcorekernels, laagverdeling met pipelining en specifieke vector- en threadafhandeling voor POWER9.

Op vier V100's bereiken de eigen metingen van het project een piek van 7.357 tokens per seconde bij het lezen van een prompt met 135.000 tokens. Een prompt met 252.000 tokens wordt verwerkt met 7.089 tokens per seconde, wat 35,5 seconden duurt. Greedy generatie bereikt 113 tokens per seconde bij JSON, 103 bij code en 84 bij lopende tekst. Bij een hergebruikte context van 252.000 tokens verschijnt het eerste vervolg-token na 0,26 seconden, waarna de generatie met 60 tokens per seconde verloopt.

Die cijfers zijn metingen van de bouwer op één gespecialiseerde server, geen algemeen toepasbare benchmark. De snelheid van promptverwerking varieert sterk met de promptlengte, en het type gegenereerde tekst verandert de decodeersnelheid. De repository beschrijft de fork als experimenteel en niet ondersteund door het oorspronkelijke Strata-project.

Toch illustreert het project een steeds bruikbaarder aanpak voor lokale inferentie: optimaliseren rond een specifiek model en een specifieke geheugenhiërarchie, in plaats van te eisen dat één algemene engine elke machine hetzelfde behandelt. De AC922 is oude, energie-intensieve zakelijke apparatuur, maar de CPU-GPU-verbindingen blijven uitzonderlijk krachtig. Een model met duizenden experts geeft die verbindingen nuttig werk.

De code is onder de MIT-licentie van Strata gepubliceerd op de `ac922`-branch van de fork, met notities over het bouwen, de kwaliteit en benchmarks. Sommige wijzigingen kunnen uiteindelijk naar het oorspronkelijke project gaan, maar de directe waarde is inspecteerbare techniek voor eigenaars van hardware waarop gangbare inferentieprojecten zich zelden richten.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
| --- | --- | --- | --- |
| De fork richt zich op een AC922 met twee POWER9-CPU's, vier V100-GPU's van 16 GB en NVLink 2.0 | GEVERIFIEERD | [Repository](https://github.com/eelgaev/Strata-AC922) | geen |
| NUMA-bewuste plaatsing van experts, per socket gebieden met vastgezette geheugenpagina's, ophalen via naburige GPU's en Volta/POWER9-kernels | GEVERIFIEERD | [Repository](https://github.com/eelgaev/Strata-AC922) | code en technische notities aanwezig; niet onafhankelijk uitgevoerd |
| Piek bij prefill van 7.357 tokens/s en 7.089 tokens/s bij 252.000 tokens | GEMELD DOOR DE GEMEENSCHAP | [Repository](https://github.com/eelgaev/Strata-AC922) | geen; benchmark van de bouwer |
| Decoderen bereikt 113 tokens/s bij JSON en 84 bij lopende tekst | GEMELD DOOR DE GEMEENSCHAP | [Repository](https://github.com/eelgaev/Strata-AC922) | geen; benchmark van de bouwer |
| De fork is experimenteel en wordt niet door het oorspronkelijke project ondersteund | GEVERIFIEERD | [Repository](https://github.com/eelgaev/Strata-AC922) | expliciete opmerking in de repository |
| Inferentie voor specifieke hardware kan opnieuw waarde halen uit een oudere gespecialiseerde geheugentopologie | ANALYSE | [Repository](https://github.com/eelgaev/Strata-AC922) | gevolgtrekking uit implementatie en metingen |
