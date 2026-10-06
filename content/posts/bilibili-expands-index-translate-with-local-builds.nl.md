+++
title = "bilibili breidt Index-Translate uit met lokale builds"
slug = "bilibili-breidt-index-translate-uit-met-lokale-builds"
description = "De open vertaalfamilie heeft nu GGUF-, FP8- en NVFP4-pakketten, een gratis compatibele API en vier openbare benchmarks. De prestatiecijfers blijven eigen metingen van de ontwikkelaar."
tags = ["models", "tools"]
date = 2026-10-05T04:01:30+02:00
draft = false
+++

bilibili voegde op 3 en 4 oktober officiële gekwantiseerde builds, een gratis openbare interface en vier evaluatiesets toe aan Index-Translate. Daarmee werden de onlangs vrijgegeven vertaalmodellen een praktischer pakket voor lokaal en gehost gebruik.

De familie vertaalt tekst tussen 150 talen en aanvaardt instructies over terminologie, opmaak en stijl. De gewone tekstmodellen zijn beschikbaar met 2 miljard en 9 miljard parameters en als preview met 35 miljard parameters. Het grootste is een mixture-of-experts-model dat ongeveer 3 miljard parameters per token activeert.

De belangrijkste verandering voor lokale gebruikers is de verpakking. GGUF-versies richten zich nu op llama.cpp, FP8-builds op vLLM en NVFP4-builds op nieuwere Blackwell-GPU's. Het project publiceert die formaten voor de tekstmodellen, de modellen met controle over lettergrepen en de modellen voor lange documenten. De spraakmodellen hebben ook gekwantiseerde pakketten, al bevatten de GGUF-repositories alleen de onderliggende tekstmodellen en niet de volledige spraakpipeline.

Het nieuwe gehoste eindpunt biedt de 35B-A3B-preview via een interface die compatibel is met de chat-API van OpenAI. Daarmee kunnen ontwikkelaars het model testen zonder eerst geschikte hardware te regelen. De repository noemt het eindpunt gratis, maar belooft geen serviceniveau of prijzen op lange termijn.

Index-Translate is meer dan een zinsvertaler. De client kan JSON- en markdownstructuren behouden, een woordenlijst afdwingen en een bepaalde toon vragen. Verwante pakketten vertalen spraak, streven naar een gevraagd aantal lettergrepen voor nasynchronisatie of nemen context mee door een lang document. Deze functies richten zich op de lastige delen van vertaling in productie die een algemene prompt als “vertaal dit” vaak mist.

bilibili gaf ook benchmarkmateriaal voor instTrans, MEME, SandGlass en NativeLong vrij, met evaluatiescripts. Daardoor is het testontwerp inspecteerbaar, maar de gepubliceerde scores zijn nog altijd eigen metingen van de ontwikkelaar. In het technische rapport behaalt het previewmodel 0,8794 op FLORES COMET-22 en 76,76 bij de WMT26-beoordelaar. Die laatste gebruikt GPT-5.6-Sol als evaluator en mag dus niet als een onafhankelijke menselijke vergelijking worden gelezen.

De oorspronkelijke modelfamilie verscheen op 30 september; dit is geen lancering van een nieuw basismodel. Het nieuws is dat ze binnen vier dagen de uitrolformaten, het testeindpunt en de evaluatiebestanden kreeg die nodig zijn om van een modelaankondiging naar iets te gaan dat ontwikkelaars daadwerkelijk kunnen uitproberen.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
| --- | --- | --- | --- |
| Openbare API en vier benchmarks vrijgegeven op 4 oktober; gekwantiseerde builds vrijgegeven op 3 oktober | GEVERIFIEERD | [Projectrepository](https://github.com/bilibili/Index-Translate) | geen |
| Tekstmodellen omvatten 150 talen en ondersteunen beperkingen voor terminologie, opmaak en stijl | GEVERIFIEERD | [Projectrepository](https://github.com/bilibili/Index-Translate) | [Modelkaart](https://huggingface.co/IndexTeam/Index-Translate-35B-A3B-preview) |
| GGUF-, FP8- en NVFP4-pakketten en hun gedocumenteerde runtime-doelen | GEVERIFIEERD | [Projectrepository](https://github.com/bilibili/Index-Translate) | afzonderlijke pakketlinks vermeld in de repository |
| Previewmodel heeft in totaal 35 miljard en ongeveer 3 miljard actieve parameters | GEVERIFIEERD | [Modelkaart](https://huggingface.co/IndexTeam/Index-Translate-35B-A3B-preview) | geen |
| FLORES COMET-22 0,8794 en WMT26-beoordelaar 76,76 | VOLGENS HET BEDRIJF | [Technisch rapport](https://arxiv.org/abs/2609.40181) | geen; rapport gebruikt GPT-5.6-Sol als beoordelaar voor WMT26 |
| Nieuwe pakketten maken de familie praktischer om lokaal of via een gehost eindpunt te testen | ANALYSE | [Projectrepository](https://github.com/bilibili/Index-Translate) | gevolgtrekking uit vrijgegeven bestanden; langdurige beschikbaarheid van het eindpunt niet vastgesteld |
