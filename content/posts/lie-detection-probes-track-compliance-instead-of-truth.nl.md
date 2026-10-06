+++
title = "Leugendetectieprobes volgen naleving in plaats van waarheid"
slug = "leugendetectieprobes-volgen-naleving-in-plaats-van-waarheid"
description = "Een preprint test acht gepubliceerde probes op taalmodellen die personages spelen die basisfeiten afwijzen. Veel falen zodra ware en onware antwoorden dezelfde prompt delen; een probe die waarheid van gehoorzaamheid leert scheiden, houdt stand."
tags = ["research", "safety"]
date = 2026-10-06T04:01:31+02:00
draft = false
+++

Veel gepubliceerde leugendetectieprobes, die de interne activiteit van een taalmodel lezen om onware antwoorden te signaleren, detecteren deels of het model zijn instructies heeft gevolgd, meldt een nieuwe preprint.

Maximilian von Klinski en drie mede-auteurs lieten drie open modellen personages spelen die basisfeiten afwijzen, zoals een ptolemeïsche astronoom of een complotdenker. Ze testten of acht bestaande probes de onware antwoorden nog herkenden. Veel deden dat, totdat de ware en onware antwoorden onder dezelfde personageprompt werden geplaatst. Toen scoorden verschillende probes slechter dan het opgooien van een munt.

## Waarom dit ertoe doet {#why-it-matters}

Een veiligheidsteam dat een model in productie met een probe bewaakt, heeft een alarm nodig dat afgaat bij onwaarheid, niet bij iets wat er doorgaans mee samengaat. In de gegevens waarop de meeste probes worden getraind, is het onware antwoord ook het minder waarschijnlijke antwoord en het antwoord dat de regels van het model schendt. Het onderzoek vindt dat probes die sluiproutes leren.

## Hoe een probe een model leest

Een probe is een eenvoudige classifier die wordt getraind op de getallen binnen één modellaag, met labels die aangeven of de verwerkte tekst waar of onwaar was. Als hij werkt, leest hij wat het model als waar beschouwt, zelfs wanneer de woorden die het produceert iets anders zeggen.

Het team bouwde een dataset met 8.916 antwoorden van Meta's Llama 3.3 70B en Google's Gemma 3 27B en Gemma 4 31B. Elk model beantwoordde ja-neevragen als gewone assistent en als één van 15 personages: mensen met overtuigingen uit de echte wereld, fictieve figuren zoals een burger uit Orwells *1984* en historische figuren zoals een middeleeuwse arts. De vragen werden verfijnd via een pipeline op basis van Anthropic's Claude Opus 4.8, beoordeeld door Llama en met de hand gecontroleerd door de eerste auteur.

## Een gedeelde prompt breekt de meeste probes

In de eerste versie van de test onderscheidden de meeste eerdere probes ware en onware antwoorden goed: ze rangschikten ongeveer negen van de tien paren correct. Maar elk onwaar antwoord had een personageprompt en elk waar antwoord de assistentprompt, zodat de prompt alleen al het antwoord verried.

De auteurs verwijderden die aanwijzing door beide antwoorden na de personageprompt te plaatsen. Het ware antwoord was nu ook het minder waarschijnlijke antwoord en het antwoord dat de instructies van het personage tegensprak. Op Llama zakten verschillende eerder werkende probes onder het kansniveau, en slechts twee bleven dicht bij hun eerdere scores. De mislukkingen herhaalden zich op beide Gemma-modellen, vaak in sterkere mate.

## Drie valstrikken isoleren de sluiproute

Om te achterhalen wat de probes volgden, bouwde het team drie testsets waarin waarheid tegengesteld is aan een waarschijnlijke verstorende factor. In één maakte een scoreregel het foute antwoord waarschijnlijker. In een andere had een personage een onjuiste persoonlijke overtuiging, bijvoorbeeld dat zeven keer zes 13 is. In de derde schond het juiste antwoord een opmaakregel, bijvoorbeeld door ronde haakjes te gebruiken terwijl vierkante vereist waren, en volgde het foute antwoord de regel.

De opmaakvalstrik was doorslaggevend. Op Llama scoorde elke eerdere probe onder het kansniveau, behalve één waarvan de metingen bij elke test omgekeerd waren. De auteurs interpreteren dat als een sterk verband tussen “waar” en “volgens de instructies” binnen die probes.

De eigen probe van het team voegt één ingrediënt toe aan standaardtraining op eenvoudige feiten: vragen waarbij de instructies het foute antwoord eisen, zodat gehoorzaamheid en waarheid in tegengestelde richtingen wijzen. Hij scoorde ongeveer 0,98 van 1 op de test met een gedeelde prompt bij Llama, zakte op geen van de drie modellen onder 0,90 en was perfect op alle drie de valstrikken.

## Een zelfgemaakte oplossing, en nog onbekende verstorende factoren

Dat resultaat vraagt twee kanttekeningen. De nieuwe probe is ontworpen tegen dezelfde verstorende factoren waarop hij vervolgens werd getest. De auteurs erkennen dat dit de perfecte scores op de valstrikken weinig verrassend maakt. Het ontwerp bouwt bovendien voort op een eerdere probe die mede-auteur Lennart Bürger mee ontwikkelde, één van slechts twee eerdere probes die standhielden toen de prompt werd gedeeld.

De eigen gegevens van het onderzoek laten zien dat de lijst met verstorende factoren onvolledig is. Op Gemma 4 was een eerdere probe bijna perfect op alle drie de valstrikken, maar scoorde hij ongeveer 0,17 op de test met een gedeelde prompt. Hij faalde dus om een reden die geen van de valstrikken vastlegde. De personages werden ook met één systeemprompt ingesteld in gesprekken van één beurt, op modellen met maximaal 70 miljard parameters.

Het werk werd gefinancierd door het Duitse federale ministerie voor onderzoek, technologie en ruimtevaart, het Horizon Europe-programma van de Europese Unie en de Duitse onderzoeksstichting. De auteurs hebben de dataset op Hugging Face en hun code op GitHub gepubliceerd. Als volgende test noemen ze personages die geleidelijk ontstaan tijdens lange gesprekken.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
| --- | --- | --- | --- |
| Acht eerdere probes geëvalueerd; veel falen wanneer ware en onware antwoorden de personageprompt delen | VOLGENS HET BEDRIJF | [Preprint van von Klinski en collega's](https://arxiv.org/abs/2609.39807) | geen; resultaat uit een preprint |
| Dataset met 8.916 door mensen beoordeelde antwoorden van Llama 3.3 70B, Gemma 3 27B en Gemma 4 31B over 15 personages | GEVERIFIEERD | [Preprint van von Klinski en collega's](https://arxiv.org/abs/2609.39807) | [dataset op Hugging Face](https://huggingface.co/datasets/maxvonk/anti-factual-personas) |
| Vragen verfijnd met een Claude Opus 4.8-pipeline, beoordeeld door Llama 3.3 70B en gecontroleerd door de eerste auteur | GEVERIFIEERD | [Preprint van von Klinski en collega's](https://arxiv.org/abs/2609.39807) | geen; methodeverklaring van de auteurs |
| De meeste eerdere probes scoren AUROC 0,86 tot 0,94 wanneer de prompt verschilt tussen ware en onware antwoorden | VOLGENS HET BEDRIJF | [Preprint van von Klinski en collega's](https://arxiv.org/abs/2609.39807) | geen |
| Bij een gedeelde prompt op Llama zakken verschillende eerdere probes onder het kansniveau; alleen Marks/Bürger Lie (0,885) en Cundy DolusChat (0,901) blijven stabiel | VOLGENS HET BEDRIJF | [Preprint van von Klinski en collega's](https://arxiv.org/abs/2609.39807) | geen |
| Mislukkingen met een gedeelde prompt herhalen zich, vaak sterker, op Gemma 3 27B en Gemma 4 31B | VOLGENS HET BEDRIJF | [Preprint van von Klinski en collega's](https://arxiv.org/abs/2609.39807) | geen |
| Bij de nalevingsvalstrik op Llama scoren alle eerdere probes onder het kansniveau behalve Goldowsky-Dill SD, die overal omgekeerd is | VOLGENS HET BEDRIJF | [Preprint van von Klinski en collega's](https://arxiv.org/abs/2609.39807) | geen |
| Probes koppelen waarheid aan instructienaleving | ANALYSE | [Preprint van von Klinski en collega's](https://arxiv.org/abs/2609.39807) | gevolgtrekking van de auteurs uit de nalevingsvalstrik |
| Nieuwe probe: AUROC 0,976 op de test met gedeelde prompt bij Llama, nooit onder 0,900 over drie modellen, perfect op alle drie de valstrikken | VOLGENS HET BEDRIJF | [Preprint van von Klinski en collega's](https://arxiv.org/abs/2609.39807) | geen |
| De nieuwe probe is getraind om dezelfde verstorende factoren weg te nemen waarop hij wordt getest; de auteurs noemen de valstrikresultaten weinig verrassend | GEVERIFIEERD | [Preprint van von Klinski en collega's](https://arxiv.org/abs/2609.39807) | geen |
| Mede-auteur Lennart Bürger ontwikkelde de Marks/Bürger-probe mee waarop de nieuwe probe voortbouwt | GEVERIFIEERD | [Preprint van von Klinski en collega's](https://arxiv.org/abs/2609.39807) | verwijst naar Bürger et al. (2024) |
| Op Gemma 4 is Cooney DYL bijna perfect op alle valstrikken, maar scoort 0,171 met een gedeelde prompt | VOLGENS HET BEDRIJF | [Preprint van von Klinski en collega's](https://arxiv.org/abs/2609.39807) | geen |
| Gefinancierd door het Duitse BMFTR, EU Horizon Europe en de Duitse onderzoeksstichting (DFG) | GEVERIFIEERD | [Preprint van von Klinski en collega's](https://arxiv.org/abs/2609.39807) | dankwoordsectie |
| Code is openbaar op GitHub | GEVERIFIEERD | [GitHub-repository](https://github.com/max-vkl/stress-testing-llm-lie-detectors) | repositorypagina laadt |
| Preprint geplaatst op 30 september 2026 | GEVERIFIEERD | [arXiv-vermelding](https://arxiv.org/abs/2609.39807) | arXiv-metadata |
