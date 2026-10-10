+++
title = "Basalt specialiseert Qwen-inferentie voor Blackwell"
slug = "basalt-specialiseert-qwen-inferentie-voor-blackwell"
description = "De engine met MIT-licentie richt zich uitsluitend op één Qwen-model en NVIDIA's nieuwste consumenten-GPU's. Gewichten van het mixture-of-experts-model kunnen uitwijken naar systeemgeheugen of een tweede kaart."
tags = ["models", "tools", "projects"]
date = 2026-10-10T03:59:41+02:00
draft = false
+++

Basalt is een nieuwe lokale inferentie-engine voor één modelfamilie en één GPU-generatie: Qwen3.8-Flash-Next op NVIDIA Blackwell-kaarten.

Het project met MIT-licentie is een afsplitsing van de bredere Strata-engine en verwijdert andere doelplatforms. De belangrijkste afweging is specialisatie: experts die niet in het videogeheugen passen, kunnen in het systeem-RAM of op een tweede GPU blijven, terwijl de dichte delen van het mixture-of-experts-model dicht bij de hoofdkaart blijven.

## Waarom dit ertoe doet {#why-it-matters}

Een ontwikkelaar van lokale modellen met een RTX 50-serie-werkstation krijgt een engine die rond die hardware is ontworpen, in plaats van een algemene runtime met veel compatibiliteitsroutes. Datzelfde beperkte ontwerp sluit ook oudere NVIDIA-systemen en systemen zonder NVIDIA uit.

Basalt verpakt het model in één bestand dat in het geheugen kan worden gemapt, met gewichten, tokenizer, chatsjabloon, kop voor speculatieve decodering, expertindeling en optionele beeldcomponenten. De conversie verpakt bestaande gewichten opnieuw in plaats van ze te hertrainen. Kant-en-klare pakketten zijn afzonderlijk beschikbaar op Hugging Face.

De meegeleverde server biedt interfaces die compatibel zijn met OpenAI en Anthropic en kan maximaal acht gelijktijdige verzoeken bedienen. Standaard wordt de context verdeeld over actieve slots, zodat vier slots bij een maximum van 262.144 tokens elk 65.536 tokens krijgen. Beheerders kunnen ook aan elk slot de volledige context toewijzen, met de bijbehorende geheugenkosten.

De runtime vereist Linux op x86-64, CUDA 13 en een Blackwell-GPU met compute capability 12.0. De beeldverwerking heeft een afzonderlijke encoder die is geschreven voor Qwens vision tower, met een terugvaloptie op de CPU. De repository bevat ook pariteitstests, een kwaliteitscontrole op basis van perplexiteit en divergentie, en benchmarktestopstellingen.

De auteur van het project meldt honderden gegenereerde tokens per seconde op een combinatie van RTX 5090 en 5060 Ti, afhankelijk van het prompttype en de kwantisatie. Die cijfers zijn zelf gemeten en niet onafhankelijk gereproduceerd. Belangrijker dan het piekcijfer is de technische keuze erachter: een groot dunbezet model kan op een werkstation draaien door alleen de experts te streamen die bij elke stap nodig zijn.

## Waarop te letten

Onafhankelijke tests moeten bij de meegeleverde kwantisaties zowel kwaliteit als snelheid vergelijken. De repository waarschuwt ook dat de standaardserverinstellingen niet zijn afgestemd, zodat gepubliceerde resultaten een volledige configuratie moeten bevatten om vergelijkbaar te zijn.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
|---|---|---|---|
| Basalt is een Qwen3.8-Flash-Next-engine met MIT-licentie voor Linux en NVIDIA Blackwell | GEVERIFIEERD | https://github.com/jesdga95/basalt | geen |
| De engine kan experts in systeem-RAM of op een tweede GPU plaatsen | GEVERIFIEERD | https://github.com/jesdga95/basalt | geen |
| De server biedt API's die compatibel zijn met OpenAI en Anthropic, met maximaal acht gelijktijdige slots | GEVERIFIEERD | https://github.com/jesdga95/basalt | geen |
| De auteur meldt honderden gegenereerde tokens per seconde op een combinatie van RTX 5090 en 5060 Ti | VOLGENS HET BEDRIJF | https://github.com/jesdga95/basalt | geen |
| Specialisatie verwijdert compatibiliteitsroutes in ruil voor sterkere hardwareoptimalisatie | ANALYSE | https://github.com/jesdga95/basalt | geen |
