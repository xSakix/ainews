+++
title = "PolyStrata draait grote MoE-modellen op gaming-GPU's"
slug = "polystrata-draait-grote-moe-modellen-op-gaming-gpus"
description = "De open-sourcerunner houdt geselecteerde modelexperts in systeemgeheugen en verplaatst ze zo nodig naar een consumenten-GPU. Zijn éénklikpakket biedt lokale API's die compatibel zijn met OpenAI en Anthropic."
tags = ["projects", "models", "hardware"]
date = 2026-10-12T03:57:37+02:00
draft = false
+++

PolyStrata heeft een open-sourcerunner uitgebracht die systeemgeheugen gebruikt om mixture-of-experts-modellen aan te bieden die te groot zijn om volledig op een gaming-GPU te passen.

Het éénklikpakket bouwt rond de Strata-runtime en richt zich op Nvidia- en AMD-kaarten met minimaal 12 GB videogeheugen. Het levert een Qwen3.8-Flash-Next-opstelling die beelden kan verwerken en experimentele ondersteuning voor verschillende grotere dunbezette modellen, en biedt OpenAI- en Anthropic-compatibele eindpunten op de lokale machine.

## Waarom dit ertoe doet {#why-it-matters}

Voor een ontwikkelaar met een werkstation in plaats van een server zet PolyStrata beschikbaar systeem-RAM om in een grotere modelvoorraad. Alleen de experts die voor de huidige token nodig zijn, worden door de GPU geleid, waarbij dataverplaatsing en geheugencapaciteit worden afgewogen tegen de kosten van hardware met meerdere GPU's.

Mixture-of-experts-modellen bevatten veel gespecialiseerde parameterblokken maar activeren bij elke stap slechts een deel. PolyStrata houdt die blokken in hostgeheugen en plant actieve blokken op de accelerator. De techniek verkleint het modelbestand niet: volgens de README vereisen experimentele GLM 5.3 Flash-builds nog steeds ongeveer 79 tot 114 GB, afhankelijk van kwantisatie.

De eigen RTX 5070-metingen van het project lopen van ongeveer 94 gegenereerde tokens per seconde bij de kleinste tweebitinstelling tot 53 bij een grotere driebitinstelling. Het meldt promptverwerkingssnelheden tussen ongeveer 1.620 en 2.650 tokens per seconde bij een context van 32.000 tokens. Dit zijn benchmarks van de bouwer, geen onafhankelijke metingen, en de kwaliteit verschilt tussen kwantisatieniveaus.

PolyStrata documenteert ook Claude Code dat een dunbezet Qwen3.6 35B-model met driebitprecisie aanstuurt op een laptop-GPU met 8 GB. Een warmstartoptie leest de systeemprompt vóór de interactieve sessie en vermindert de wachttijd tot het eerste antwoord. De daadwerkelijke bruikbaarheid hangt af van RAM-bandbreedte, modelroutering en hoeveel context tussen beurten verandert.

De repository heeft een MIT-licentie en biedt lokale eindpunten die compatibel zijn met bestaande agentclients. Dat vermindert integratiewerk en geeft lokale applicaties toegang tot bestanden en tools onder de eigen rechten van de gebruiker. Het betekent ook dat de beheerder, in plaats van een gehoste aanbieder, verantwoordelijk is voor modelupdates, netwerkblootstelling en logverwerking.

## Waarop te letten

Onafhankelijke tests moeten identieke modellen en kwantisatie-instellingen vergelijken met gevestigde runtimes die naar de CPU verplaatsen. De huidige waarde van het project is inspecteerbare code en een praktische verpakkingslaag; de belangrijkste snelheden blijven door de auteur gemeld totdat ze op meer hardware zijn gereproduceerd.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
|---|---|---|---|
| PolyStrata bracht een lokale runner met MIT-licentie uit voor dunbezette modellen op consumenten-GPU's | GEVERIFIEERD | https://github.com/VecSzn/PolyStrata | geen |
| Het pakket biedt lokale API's die compatibel zijn met OpenAI en Anthropic | GEVERIFIEERD | https://github.com/VecSzn/PolyStrata | geen |
| De README meldt 53–94 gegenereerde tokens per seconde op een RTX 5070 bij geselecteerde kwantisaties | VOLGENS HET BEDRIJF | https://github.com/VecSzn/PolyStrata | geen |
| Experimentele GLM 5.3 Flash-bestanden vereisen ongeveer 79–114 GB, afhankelijk van kwantisatie | GEVERIFIEERD | https://github.com/VecSzn/PolyStrata | geen |
| Het laden van experts uit hostgeheugen weegt capaciteit af tegen overdrachts- en geheugenbandbreedtekosten | ANALYSE | https://github.com/VecSzn/PolyStrata | geen |
