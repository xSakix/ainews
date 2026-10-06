+++
title = "Aleph Alpha geeft Kolibri met open gewichten vrij"
slug = "aleph-alpha-geeft-kolibri-met-open-gewichten-vrij"
description = "Het Duits-Engelse redeneermodel wordt geleverd met Apache-2.0-gewichten en instructies voor inferentie. Het kleine aantal actieve parameters laat de geheugenbehoefte nog altijd groot."
tags = ["models", "tools"]
date = 2026-10-04T09:27:37+02:00
draft = false
+++

Aleph Alpha, een Duitse AI-ontwikkelaar, bracht op 3 oktober Kolibri uit. Daarmee werd een Duits-Engels redeneermodel beschikbaar als downloadbare gewichten onder de Apache 2.0-licentie.

Kolibri gebruikt een mixture of experts: elk token activeert een klein deel van een veel groter netwerk. De modelkaart documenteert redeneerinstellingen, toolaanroepen en een serverinterface die compatibel is met de chat-API van OpenAI.

Voor een ontwikkelaar die Duitse documenten verwerkt, biedt de release een inspecteerbaar model dat op infrastructuur onder eigen beheer kan draaien. Aleph Alpha concentreert zich bewust op Duits en Engels, met onder meer een tokenizer die voor de Duitse woordstructuur is ontworpen, in plaats van op brede meertalige dekking.

De geheugenbehoefte is aanzienlijk. Kolibri activeert ongeveer 3,5 miljard parameters per token, maar de circa 78 miljard parameters moeten nog altijd worden opgeslagen. Het FP8-checkpoint neemt ongeveer 78 GB in beslag; de kaart noemt twee A100-GPU's van 80 GB of één H200 onder de minimale configuraties.

Aleph Alpha zegt contexten van ongeveer één miljoen tokens te hebben gevalideerd, maar raadt voor efficiënte inferentie en complexe taken een kwart daarvan aan. De oorspronkelijke trainingslengte voor lange context is het kleinere getal. Het onderscheid is nuttig bij de planning van een uitrol: de grootste toegestane invoer is een gedocumenteerde uitbreiding, met een afzonderlijk advies voor dagelijks gebruik.

De eigen tests van het bedrijf laten ongelijkmatige sterke punten zien. Kolibri scoort hoog op wedstrijdwiskunde, terwijl Qwen3.8 27B het overtreft op de algemene Engelse en Duitse maatstaven van de kaart. Dit zijn evaluaties van beide modellen door Aleph Alpha, geen onafhankelijke vergelijking.

Inferentie vereist het inferentiepakket van Aleph Alpha, dat een Kolibri-plugin voor vLLM biedt. De kaart bevat opdrachten om redeneren en het ontleden van toolaanroepen in te schakelen. Aanroepers kunnen een laag, gemiddeld of hoog redeneerniveau kiezen of het uitschakelen. De kaart noemt assistenten onder menselijke controle en documentworkflows als beoogde toepassingen. Het FP8-checkpoint en een afzonderlijk BF16-checkpoint zijn nu beschikbaar.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
| --- | --- | --- | --- |
| Release op 3 oktober; focus op Duits en Engels; downloadbare Apache-2.0-gewichten | GEVERIFIEERD | [Bron](https://huggingface.co/Aleph-Alpha/Kolibri-1) | geen |
| 78.103.074.560 totale en 3.457.573.120 actieve parameters; FP8-geheugengebruik van ongeveer 78 GB; gedocumenteerde GPU-configuraties | VOLGENS HET BEDRIJF | [Bron](https://huggingface.co/Aleph-Alpha/Kolibri-1) | geen |
| Oorspronkelijke context 262.144; gevalideerde uitbreiding 1.048.576; advies maximaal 262.144 | VOLGENS HET BEDRIJF | [Bron](https://huggingface.co/Aleph-Alpha/Kolibri-1) | geen |
| Algemeen EN/DE: Kolibri 75,5/70,8, Qwen3.8 27B 80,2/79,9; AIME 2025 EN 96,9 | VOLGENS HET BEDRIJF | [Bron](https://huggingface.co/Aleph-Alpha/Kolibri-1) | geen; alle modellen geëvalueerd door Aleph Alpha |
| Tokenizerontwerp; vLLM-plugin, redeneerinstellingen, toolparser en OpenAI-compatibele API; beoogd gebruik met menselijke controle; BF16-checkpoint | GEVERIFIEERD | [Bron](https://huggingface.co/Aleph-Alpha/Kolibri-1) | geen; gedocumenteerde interfaces en beoogde toepassingen, geen uitvoeringstests |
| Lokale uitrol geeft ontwikkelaars die Duitse documenten verwerken controle over infrastructuur | ANALYSE | [Bron](https://huggingface.co/Aleph-Alpha/Kolibri-1) | gevolgtrekking uit downloadbare gewichten en inferentiedocumentatie |
