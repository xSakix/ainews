+++
title = "De introductiekorting op GPT-6.2 berustte op een rekenfout"
slug = "introductiekorting-op-gpt-6-2-berustte-op-een-rekenfout"
description = "OpenAI bracht negen dagen lang te weinig gebruik van GPT-6.2 Astra en Sol in mindering op abonnementsbundels, waardoor gebruikers hun limiet nu 40 en 25 procent sneller bereiken. Een onafhankelijke meting laat intussen zien dat de modellen minder tokens aan redeneren besteden, maar het verbruik binnen een abonnement blijft voor buitenstaanders moeilijk te controleren."
tags = ["business", "tools"]
date = 2026-11-27T03:17:17+01:00
draft = false
+++

Onder een bericht van een OpenAI-ingenieur op Hacker News vergeleken gebruikers de standen van hun verbruiksmeter. Iemand met de gebruikersnaam seviu schreef: “Gisteravond had ik nog bijna 90 procent van mijn bundel over. Toen ik vanochtend wakker werd, was alles op.” Hij had een Pro-abonnement en had de nacht ervoor geen agent laten draaien. Een andere gebruiker, ragequittah, herinnerde zich de week ervoor heel anders: “Zes uur Astra kostte me toen 3 procent.”

Tussen die twee meterstanden zit het bericht van de ingenieur, en een wijziging in de manier waarop een abonnement met een vaste prijs een dag werk verrekent.

## De correctie

Op 26 november om 02.50 uur UTC schreef Thibault Sottiaux, die bij OpenAI aan Codex en ChatGPT werkt, op X: “Bij de lancering van GPT-6.2 hebben we een fout gemaakt in de verrekening, waardoor het gebruik van GPT-6.2 Astra en Sol voor de meeste gebruikers ten onrechte met korting werd afgetrokken.” Na de correctie, schreef hij, “verbruikt hetzelfde werk een groter deel van de bundel van je abonnement”. Vergeleken met de week ervoor “bereik je je limiet met GPT-6.2 Astra 40 procent sneller en met Sol 25 procent sneller”. Volgens hem zouden gebruikers met de modellen nog steeds meer werk moeten kunnen doen dan met GPT-6 Astra en GPT-6.1 Sol. Andere modellen waren niet getroffen en OpenAI zou het verschil voor eerder gebruik niet alsnog in rekening brengen. Ter compensatie krijgen alle abonnees van Go, Plus, Pro en Business één reset die ze voor later kunnen bewaren.

Wat betekenen die percentages voor het aantal taken? Als een bundel 40 procent sneller leegloopt, passen er ongeveer 29 procent minder taken in: één gedeeld door 1,4 is 0,71. Loopt de bundel 25 procent sneller leeg, dan passen er 20 procent minder taken in. Dat volgt rekenkundig uit de formulering van OpenAI. Het bedrijf heeft het onderliggende verbruikstarief niet gepubliceerd.

De lancering was negen dagen geleden. OpenAI introduceerde GPT-6.2 Astra en Sol op 17 november, de datum die GitHub noemde toen het de modellen aan Copilot toevoegde. In de aankondiging was zuinigheid een verkoopargument: beide modellen “leveren betere resultaten op veeleisende taken met minder uitvoertokens, zodat je binnen je gebruikslimieten meer gedaan krijgt”. Met Sol “kun je meer taken afronden met hetzelfde betaalde abonnement”. Voor de API daalden de tokenprijzen van Astra met 20 procent tot 8 dollar per miljoen invoertokens en 40 dollar per miljoen uitvoertokens. Anthropic had op 9 november dezelfde catalogusprijzen vastgesteld voor Claude Fable 5.2. Sol behield de tarieven van GPT-6.1 Sol: 2 en 10 dollar.

De API-prijzen bleven bij de correctie gelijk. Bij een betaald ChatGPT-abonnement is de rekeneenheid een deel van de gebruiksbundel. Hoeveel daarvan een taak kost, bepaalt OpenAI intern. Op de prijspagina stonden op 27 november de volgende aantallen credits per miljoen tokens: voor Astra 200 voor invoer en 1.000 voor uitvoer, een vijfde minder dan de 250 en 1.250 van GPT-6 Astra. Voor Sol bleven de aantallen 50 en 250. Voor Plus-abonnees schat de pagina dat er per periode van vijf uur 6 tot 50 lokale Codex-berichten met GPT-6.2 Astra mogelijk zijn en 17 tot 180 met Sol. Bij GPT-6 Astra is dat 5 tot 45 en bij GPT-6.1 Sol 15 tot 160. OpenAI noemt de schattingen “geen vaste berichtlimieten”. Volgens de pagina hebben “Pro-abonnementen momenteel geen limiet per vijf uur” en kunnen er ook weeklimieten gelden.

Een bandbreedte van 6 tot 50 kan de uitspraak over 40 procent niet bevestigen of weerleggen. De pagina vermeldt ook niet of de tabel na de correctie is aangepast. Dat de bundel van seviu 's nachts leegliep, is één onbevestigd relaas. Zowel de wijziging als een weeklimiet zou het kunnen verklaren.

## Waarover de discussie ging

Het bericht kreeg op Hacker News 468 punten onder een kop die de wijziging omschreef als een verlaging van de gebruiksruimte. De lezers waren verdeeld. Sommigen namen de uitleg over de “verrekenfout” aan. Eén gebruiker had uren met Astra 6.2 gewerkt, zag nog steeds 100 procent op de meter en was gaan zoeken naar een defecte widget. Anderen zagen de correctie als een prijsverhoging onder de vlag van foutherstel. Enkelen zeiden hun abonnement te hebben opgezegd of overwogen over te stappen naar Anthropic of Google. Weer een ander wees erop dat de eerste e-mail van OpenAI zo kort was dat er een tweede ter verduidelijking nodig was. Dit zijn stuk voor stuk gebruikerservaringen. Het zijn geen metingen.

Een deelnemer aan de discussie haalde ook herinneringen op aan de wisselwerking tussen de aanbieders. Deze jarenlange klant van OpenAI en Anthropic had bij OpenAI het gevoel gehad dat het gebruik onbeperkt was, met de ene reset na de andere. Daarna bood Opus 5.5 volgens deze gebruiker meer gebruiksruimte, waarop OpenAI zijn bundels verkleinde. Een ander antwoordde dat de onderlinge verhoudingen al sinds het ontstaan van deze markt geregeld omslaan en dat opnieuw zouden doen. Beiden putten uit hun geheugen. Geen van beiden liet een overzicht zien van wat de abonnementen daadwerkelijk opleverden.

## Een tweede meting aan dezelfde modellen

Op 26 november, een paar uur na het bericht van Sottiaux, publiceerde de ontwikkelaar van Agent Duel een stuk met de titel *OpenAI may be in cost control mode*. Agent Duel draait op de programmeeragent OpenCode, laat modellen onderling strijden bij echte taken en rangschikt ze met Elo-scores. Volgens de ontwikkelaar gebruikten Astra 6.2 en Sol 6.2 per taak minder uitvoer- en redeneertokens dan hun voorgangers wanneer ze tegenstanders in dezelfde duels troffen. Voor uitvoertokens geeft hij p-waarden van 0,0055 voor Sol en 0,022 voor Astra. Voor redeneertokens zijn het 0,00013 voor Sol en 0,0064 voor Astra. Volgens hem “lijken de modellen op kosten te zijn afgesteld”, zozeer zelfs dat ze “uitschieters zijn die te weinig nadenken”.

Het woord “kosten” komt van de auteur. De gegevens laten zien dat de modellen minder tokens besteden aan redeneren, zonder te verklaren waarom. OpenAI presenteert een lager verbruik van uitvoertokens juist als een eigenschap van de modellen. Volgens het introductiebericht scoorde Astra 6,2 punten hoger op de interne GDPval v2-benchmark en gebruikte het daarbij 22 procent minder uitvoertokens dan GPT-6 Astra. Dezelfde meting past bij zowel een efficiëntieverbetering als kostenbesparing. Alleen OpenAI weet welke verklaring van toepassing is. Minder tokens verklaren evenmin de verrekenfout: die betrof het tarief waartegen tokens van een bundel werden afgeschreven.

Ook de ranglijst zelf, opgesteld op 27 november om 03.00 uur UTC, geeft geen uitsluitsel. GPT-6.2 Astra staat vijfde met een Elo-score van 1.007 en een marge van 61 punten in beide richtingen, bij 2,33 dollar en 2,6 minuten per taak. Sol staat twaalfde met 937 punten, 0,43 dollar en 1,7 minuten. Claude Fable 5.2 leidt met 1.069 punten en 3,49 dollar, gevolgd door Claude Opus 5.5 met 1.060 punten en 1,63 dollar. De intervallen overlappen sterk. Voor Astra zijn posities van twee tot en met elf plausibel.

## Wat een abonnee kan controleren

Een lagere prijs heeft al eerder een ander beeld gegeven dan de uiteindelijke rekening. Op 9 november verlaagde Anthropic de tarieven voor Fable 5.2 naar 8 en 40 dollar per miljoen tokens, een vijfde onder de prijzen van zijn voorganger. Toch staat het model bij Artificial Analysis nog steeds onderaan de kostenranglijst, met 26,54 dollar per taak op de Intelligence Index. De rekening hangt immers af van het aantal tokens dat een model gebruikt. Bij OpenAI komt daar nog een laag bij. Voor een abonnee tellen drie getallen: het aantal tokens dat het model gebruikt, het tarief waartegen dat verbruik van de bundel wordt afgetrokken en de omvang van de bundel zelf. De aanbieder bepaalt ze alle drie. Volgens OpenAI zat de fout in de eerste negen dagen in het tweede getal, het verrekeningstarief.

Buitenstaanders kunnen het eerste getal meten, zoals Agent Duel deed. Voor de andere twee zijn ze aangewezen op de meter. Wie daar niets meer over heeft, vindt op de prijspagina deze zin: “Taken die op elkaar lijken, kunnen verschillende delen van je bundel verbruiken.”

## Referenties

- Agent Duel (2026). *Agent Duel Leaderboard*, generated 27 November 2026. https://agentduel.com/leaderboard
- Anthropic (2026). *Introducing Claude Fable 5.2 and Claude Mythos 5.2*. https://www.anthropic.com/claude-fable-and-mythos-5-2
- Artificial Analysis (2026). *Claude Fable 5.2 (Max): Intelligence, Performance & Price Analysis*. https://artificialanalysis.ai/models/claude-fable-5-2
- GitHub (2026). *OpenAI's GPT-6.2 Astra and GPT-6.2 Sol now available*. GitHub Changelog, 17 November. https://github.blog/changelog/2026-11-17-openais-gpt-6-2-astra-and-gpt-6-2-sol-now-available
- Hacker News (2026). *OpenAI cuts GPT-6.2 usage: Astra hits limits 40% faster, Sol 25% faster*. https://news.ycombinator.com/item?id=50651117
- micjm (2026). *OpenAI may be in cost control mode*. https://micjm.com/blog/openai-is-in-cost-control-mode/
- OpenAI (2026). *Introducing GPT-6.2 Astra and Sol*. https://openai.com/index/introducing-gpt-6-2-astra-sol
- OpenAI (2026). *Pricing*. ChatGPT Learn. https://learn.chatgpt.com/docs/pricing
- Sottiaux, T. (2026). Post on X about the GPT-6.2 billing mistake, 26 November. https://x.com/thsottiaux/status/2125784147889393806
