+++
title = "Humanlike Chat voegt toolgebruik toe aan lokaal chatmodel"
slug = "humanlike-chat-voegt-toolgebruik-toe-aan-lokaal-chatmodel"
description = "Versie 2.0 gebruikt twee docentmodellen om informele dialogen te behouden en instructie- en toolgedrag te verbeteren. De release bevat lokale gewichten en expliciete afwegingen."
tags = ["models", "agents", "projects"]
date = 2026-10-03T09:42:58+02:00
draft = false
+++

LessThanThreeAI heeft Humanlike Chat 2.0 uitgebracht, een lokaal taalmodel op basis van Qwen dat is getraind om een informele berichtstijl te behouden en tegelijk instructies en toolaanroepen te verwerken die de eerste versie niet aankon.

Het model met 27 miljard parameters is een gemeenschapsaanpassing van een gewijzigde Qwen3.8-basis, geen officiële Alibaba-release. De maker, bekend als codebottle, publiceert een [modelkaart en downloadbare gewichten](https://huggingface.co/LessThanThreeAI/Qwen3.8-27B-Humanlike-Chat-GGUF) onder Apache-2.0, naast een gratis endpoint met een aanroeplimiet.

**Waarom dit ertoe doet:** Een ontwikkelaar van lokale agents kan een poging onderzoeken om een gespreksstijl en toolgedrag in één model te combineren. De release levert samengevoegde gekwantiseerde bestanden en een adapter. De eigen vergelijkingen van de maker met de gewijzigde basis laten zowel winst als verlies zien.

De menselijk-berichttest van de maker vraagt een beoordelingsmodel uit een paar het antwoord van een echte persoon te kiezen. Het verwart het antwoord van het nieuwe model ongeveer 24 procent van de tijd met het menselijke antwoord, tegenover ongeveer 15 procent voor officiële Qwen en minder dan 1 procent voor de gewijzigde basis. Dit is de voorkeur van een beoordelaar in deze test, geen meting van misleide menselijke gebruikers.

Versie 2.0 leert van zijn eigen gegenereerde antwoorden. Eén docent beoordeelt gespreksstijl met een verborgen instructie; een andere onderwijst instructies, tools en code met de gewone basis. De leerling krijgt de verborgen stijlinstructie nooit, zodat de bedoelde stijl behouden blijft zonder die aan elke gebruikerssessie toe te voegen.

De gemelde scores voor toolselectie en instructieopvolging verbeteren ten opzichte van de gewijzigde basis, terwijl scores voor algemene kennis en programmeren dalen. De maker beschrijft ook minder weigeringen, geërfd van die basis. Deze afwegingen horen bij de stijlwinst en ondersteunen geen algemene superioriteitsclaim tegenover officiële Qwen.

De modelkaart biedt een gekwantiseerd bestand van ongeveer 15 GB voor een grafische kaart met 24 GB en een llama.cpp-configuratie die de eigen chatsjabloon voor toolaanroepen inschakelt. Bestanden behouden de namen van de vorige release, zodat bestaande gebruikers opnieuw moeten downloaden om 2.0 te krijgen; gepubliceerde hashes identificeren de nieuwe bestanden.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
|---|---|---|---|
| Versie 2.0, maker codebottle/LessThanThreeAI, gewijzigde Qwen3.8-basis van Huihui met 27 miljard parameters; Apache-2.0; GGUF, adapter en endpoint met aanroeplimiet beschikbaar. | GEVERIFIEERD | https://huggingface.co/LessThanThreeAI/Qwen3.8-27B-Humanlike-Chat-GGUF | geen |
| Selectie door de ishuman-beoordelaar: 2.0 23,5%, officiële Qwen 15,1%, gewijzigde basis 0,3%; geen misleidingstest met menselijke gebruikers. | VOLGENS HET BEDRIJF | https://huggingface.co/LessThanThreeAI/Qwen3.8-27B-Humanlike-Chat-GGUF | geen |
| Distillatie met twee docenten en leerlingantwoorden: stijldocent heeft verborgen instructie; gewone basis behandelt instructies/tools/code; leerling ziet de verborgen instructie nooit. | GEVERIFIEERD | https://huggingface.co/LessThanThreeAI/Qwen3.8-27B-Humanlike-Chat-GGUF | geen |
| IFBench 37,3→43,7, When2Call 48→58, BFCL irrelevantie 60→78; MMLU-Pro 78,5→72,5, LiveCodeBench 56→51; minder weigeringen geërfd. | VOLGENS HET BEDRIJF | https://huggingface.co/LessThanThreeAI/Qwen3.8-27B-Humanlike-Chat-GGUF | geen |
| IQ4_XS 15,10 GB aanbevolen voor 24 GB VRAM; --jinja schakelt de sjabloon en toolaanroepen in; ongewijzigde bestandsnamen vereisen opnieuw downloaden; SHA256SUMS gepubliceerd. | GEVERIFIEERD | https://huggingface.co/LessThanThreeAI/Qwen3.8-27B-Humanlike-Chat-GGUF | geen |
| De inspecteerbare lokale afweging tussen gespreksstijl en tools is relevant voor ontwikkelaars van lokale agents. | ANALYSE | https://huggingface.co/LessThanThreeAI/Qwen3.8-27B-Humanlike-Chat-GGUF | geen |
