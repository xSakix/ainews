+++
title = "Reflection toont Beam voordat het de gewichten vrijgeeft"
slug = "reflection-toont-beam-voordat-het-de-gewichten-vrijgeeft"
description = "Het mixture-of-experts-model met 501 miljard parameters is alleen via vroege toegang beschikbaar. Volgens Reflection volgen de gewichten, een technisch rapport en ontwikkelaarstools later in oktober."
tags = ["models", "agents"]
date = 2026-10-06T04:09:31+02:00
draft = false
+++

Reflection AI heeft Beam aangekondigd, een model met 501 miljard parameters voor programmeren en agentwerk, maar ontwikkelaars kunnen de gewichten nog niet inspecteren of uitvoeren.

Het Californische AI-bedrijf beschrijft Beam als een schaars mixture-of-experts-model: het bevat 501 miljard parameters, maar activeert er 23 miljard per token. Voor vroege toegang is registratie nodig; de gewichten, licentie, modelkaart, het technische rapport en de ontwikkelaarstools zijn nog niet beschikbaar.

Voor een ontwikkelaar die een open model kiest, is dat onderscheid van belang. Een model met open gewichten (open-weight model) kan worden getest op eigen workloads, aangepast en uitgerold zonder afhankelijkheid van de dienst van de maker; een aankondiging en benchmarktabel bieden nog geen basis voor die controles.

Reflection zegt Beam te hebben getraind op 23,8 biljoen tokens en vervolgens gedurende vier weken meer dan 100 miljoen reinforcement-learningtrajecten te hebben uitgevoerd op 10.500 NVIDIA GB300-GPU's. Die cijfers beschrijven een uitzonderlijk grote training, maar het bedrijf heeft het technische rapport nog niet vrijgegeven dat nodig is om de samenstelling van de data of de evaluatieopzet te onderzoeken.

De eigen tabel van het lab geeft Beam scores van 80,9 op SWE-bench Verified en 80,1 op Terminal-Bench 2.1. Daarin staat Beam ook achter Kimi K3, GLM-5.3 en Qwen 3.8-Max op de meeste vermelde tests. Reflection vergelijkt vooral de efficiëntie: het zegt dat Beam resultaten bereikt die vergelijkbaar zijn met die van GLM-5.2, met drie tot vier keer minder rekenwerk voor inferentie, op basis van zijn eigen schatting van het aantal drijvendekommabewerkingen.

Die claim kan voor teams die betalen voor lange agentsessies meer betekenen dan een kleine voorsprong op een benchmark. Schaarse activering vermindert het rekenwerk per token, al vereist het volledige model nog altijd voldoende geheugen en infrastructuur om honderden miljarden parameters op te slaan en beschikbaar te stellen.

Reflection zegt dat Beam de laatste veiligheidstests ondergaat. Het bedrijf wil de gewichten, het technische rapport, de modelkaart en de ontwikkelaarsbestanden later in oktober 2026 publiceren; het heeft geen specifieke releasedatum gegeven.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
| --- | --- | --- | --- |
| Reflection heeft Beam aangekondigd en de registratie voor vroege toegang geopend | GEVERIFIEERD | [Aankondiging van Reflection](https://reflection.ai/blog/introducing-beam) | geen nodig voor de handeling van het bedrijf |
| Beam heeft in totaal 501 miljard parameters en 23 miljard actieve parameters per token | VOLGENS HET BEDRIJF | [Aankondiging van Reflection](https://reflection.ai/blog/introducing-beam) | geen; de gewichten en het rapport zijn nog niet beschikbaar |
| Voor de training zijn gedurende vier weken 23,8 biljoen tokens en meer dan 100 miljoen RL-trajecten op 10.500 GB300-GPU's gebruikt | VOLGENS HET BEDRIJF | [Aankondiging van Reflection](https://reflection.ai/blog/introducing-beam) | geen |
| Beam behaalde 80,9 op SWE-bench Verified en 80,1 op Terminal-Bench 2.1 | VOLGENS HET BEDRIJF | [Aankondiging van Reflection](https://reflection.ai/blog/introducing-beam) | geen |
| Reflection schat dat de resultaten vergelijkbaar zijn met die van GLM-5.2, met 3–4 keer minder rekenwerk voor inferentie | VOLGENS HET BEDRIJF | [Aankondiging van Reflection](https://reflection.ai/blog/introducing-beam) | geen |
| De gewichten, het rapport, de modelkaart en de ontwikkelaarsbestanden zijn voor later in oktober 2026 toegezegd | GEVERIFIEERD | [Aankondiging van Reflection](https://reflection.ai/blog/introducing-beam) | geen nodig voor het genoemde tijdschema |
