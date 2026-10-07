+++
title = "Placebotest: de meeste agentvaardigheden voegen geen waarde toe"
slug = "placebotest-meeste-agentvaardigheden-voegen-geen-waarde-toe"
description = "Een vooraf geregistreerd experiment vergelijkt negen Claude Code-vaardigheden met even lange neutrale instructies. Twee zijn goedkoper dan placebo, één is slechter en zes zijn statistisch niet te onderscheiden."
tags = ["research", "agents", "tools"]
date = 2026-10-07T03:57:57+02:00
draft = false
+++

De meeste populaire vaardigheden voor programmeeragents presteerden niet beter dan even lange neutrale instructies in een nieuw placebogecontroleerd experiment.

Het skill-placebo-project testte negen Claude Code-vaardigheden op 15 openbare taken uit SWE-bench Verified, Terminal-Bench 2.1 en OpenThoughts-TBLite. Elke vaardigheid werd gekoppeld aan neutrale tekst met dezelfde tokenlengte, geïnstalleerd via hetzelfde mechanisme.

## Waarom dit ertoe doet {#why-it-matters}

Een ontwikkelaar die een lang instructiebestand toevoegt, kan de agent anders zien handelen en dat aan de procedure in het bestand toeschrijven. Dit experiment vraagt of het nuttige ingrediënt werkelijk de vaardigheid is, of alleen de extra context, priming en uitvoeringsvariatie die ermee gepaard gingen.

De methode werd vóór de eerste uitvoering geregistreerd. Claude Opus 5.5 voltooide 30 proeven per onderzoeksarm, wat 450 vastgelegde proeven opleverde. Kosten waren de primaire uitkomst; het percentage geslaagde taken werd ook gevolgd, met statistische correctie over de negen vergelijkingen.

Twee vaardigheden waren goedkoper dan hun placebo's: ponytail met 12 procent en agent-skills met 5 procent. Planning-with-files slaagde in 80 procent van zijn proeven, terwijl zijn placebo alle 30 doorstond. Daarmee was het slechter volgens de vooraf geregistreerde beslisregel van het project. De overige zes vaardigheden waren statistisch niet te onderscheiden van hun bijpassende neutrale tekst.

Geen van de negen was meetbaar goedkoper dan uitvoeren zonder vaardigheid. Neutrale placebotekst alleen veranderde de kosten met 2 tot 16 procent ten opzichte van de referentie zonder vaardigheid. Dat resultaat maakt promptlengte en ogenschijnlijk irrelevante context tot onderdeel van de behandeling, in plaats van onschuldige achtergrond.

## De controle verbetert de vraag, niet de steekproefomvang

Een referentie zonder vaardigheid vraagt of het volledige pakket de prestaties verandert. De bijpassende placebo stelt een scherpere vraag: voegen de werkelijke instructies waarde toe boven een gelijke hoeveelheid tekst die op dezelfde manier wordt aangeleverd? De twee vergelijkingen kunnen verschillen zonder elkaar tegen te spreken.

De repository biedt de vooraf geregistreerde methode, resultaten per proef en agentlogs. Ze registreert ook een wijziging van 6 oktober: twee time-outs waarvan de tests later slaagden, werden als mislukkingen geteld, zoals de oorspronkelijke regels vereisten. Dat verschoof planning-with-files van “niet beter” naar “slechter” zonder de kosten te veranderen.

De beperkingen zijn aanzienlijk. Vijftien taken en 30 proeven per onderzoeksarm laten brede intervallen voor het slagingspercentage; de uitvoering omvat één hoofdmodel en agentomgeving, en de gekozen vaardigheden benadrukken algemene programmeerworkflows in plaats van specialistische referentiekennis. De huidige logs stellen ook niet vast hoe consequent elke vaardigheid tijdens een uitvoering werd aangeroepen.

Een kleine Codex-pilot testte slechts drie vaardigheden op vijf taken en is expliciet secundair. De resultaten mogen niet met het Claude-experiment worden vermengd of als vergelijking tussen modelfamilies worden behandeld.

De bevinding laat niet zien dat programmeervaardigheden nutteloos zijn. Ze laat zien dat populariteit, lengte en een aannemelijke procedure slechte vervangers zijn voor een bijpassende controle. De herbruikbare bijdrage is het experimentele ontwerp: leg de methode vast, geef de controle evenveel context, bewaar volledige logs en meet kosten naast succes.

Toekomstige versies kunnen het resultaat versterken met meer taken, andere agentomgevingen en een controle met door elkaar gezette instructies die de betekenis van de procedure van algemene priming scheidt.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
| --- | --- | --- | --- |
| Het hoofdexperiment omvatte 450 proeven over negen vaardigheden en 15 openbare taken | GEVERIFIEERD | [skill-placebo-repository](https://github.com/simonether/skill-placebo) | methode, resultaten en logs zijn openbaar |
| Twee vaardigheden versloegen placebo op kosten, één was slechter en zes waren niet beter | VOLGENS HET BEDRIJF | [skill-placebo-resultaten](https://github.com/simonether/skill-placebo) | geen; statistische analyse van de auteur |
| Ponytail kostte 12 procent minder en agent-skills 5 procent minder dan de bijpassende placebo | VOLGENS HET BEDRIJF | [skill-placebo-resultaten](https://github.com/simonether/skill-placebo) | geen |
| Planning-with-files slaagde in 80 procent tegenover 100 procent voor placebo | VOLGENS HET BEDRIJF | [skill-placebo-resultaten](https://github.com/simonether/skill-placebo) | gegevens per proef zijn beschikbaar |
| Geen van de negen vaardigheden was meetbaar goedkoper dan geen vaardigheid | VOLGENS HET BEDRIJF | [skill-placebo-resultaten](https://github.com/simonether/skill-placebo) | geen |
| Bijpassende controles isoleren instructie-inhoud beter dan een referentie zonder vaardigheid | ANALYSE | [geregistreerde methode](https://github.com/simonether/skill-placebo/blob/main/METHOD.md) | gevolgtrekking uit het experimentele ontwerp |
