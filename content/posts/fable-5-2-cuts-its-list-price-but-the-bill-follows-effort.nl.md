+++
title = "Fable 5.2 verlaagt de prijs, maar effort bepaalt de factuur"
slug = "fable-5-2-verlaagt-prijs-maar-effort-bepaalt-factuur"
description = "Anthropic verlaagde de prijs van Claude Fable 5.2 met een vijfde, maar een onafhankelijke index mat bij maximale effort de hoogste kosten per taak van 73 modellen. Het verschil zit in hoeveel tokens het model verbruikt, en volgens de eigen grafieken van Anthropic bepaalt de effort-instelling dat."
tags = ["models", "business"]
date = 2026-11-10T03:25:07+01:00
draft = false
+++

Deze maandag is verzonnen, samengesteld uit introductiedocumenten en niet uit iemands dagboek. Een platformverantwoordelijke bij een middelgroot softwarebedrijf leest dat Anthropic de prijs van zijn topmodel met een vijfde heeft verlaagd. Ze doet waartoe de aankondiging uitnodigt. Ze verandert de modelnaam in de agentconfiguratie van haar team, zet de effort-parameter op de hoogste waarde en laat 's nachts veertig repository-audits draaien. Tegen de ochtend is de batch klaar en wil ze alleen de factuur openen. Die lijkt niet op de kop die ze las.

De kop klopte. Op 9 november bracht Anthropic Claude Fable 5.2 en zijn tweelingmodel Claude Mythos 5.2 uit voor 8 dollar per miljoen invoertokens en 40 dollar per miljoen uitvoertokens, tegenover 10 en 50 dollar voor de 5.1-versies. Het onafhankelijke cijfer dat diezelfde dag verscheen klopt ook. Artificial Analysis, dat een intelligentie-index voor modellen van verschillende aanbieders publiceert, draaide Fable 5.2 op de maximale instelling. Het plaatste het model met een score van 65 op de eerste plaats van 74 modellen voor intelligentie, en op de 73e plaats van 73 voor kosten, met 26,54 dollar per indextaak. Beide cijfers beschrijven één model. Het verschil zit in hoeveel tokens het verbruikt.

## Wat de prijslijst zegt

De documentatie van Anthropic vermeldt de nieuwe tarieven duidelijk. Cachelezingen kosten 0,20 dollar per miljoen tokens, batchverwerking kost de helft van de basisprijs en een optionele snelle modus die tot 2,5 keer sneller genereert, kost 16 dollar voor invoer en 80 dollar voor uitvoer. Het bedrijf zegt ook dat het model tot 30 procent sneller uitvoer produceert dan Fable 5.1. TechCrunch merkt op dat Fable nu goedkoper is dan zijn belangrijkste concurrent. Fortune plaatst Fable 5.2 20 procent onder OpenAI's GPT-6 Astra, dat 10 en 50 dollar rekent, met invoer uit de cache voor 20 cent tegenover één dollar bij Astra.

Mythos 5.2 heeft dezelfde prijs. Anthropic noemt de twee hetzelfde onderliggende model. Fable wordt geleverd met beveiligingen voor cyber- en biologische toepassingen en is beschikbaar voor elke klant, terwijl Mythos naar organisaties gaat die zijn toegelaten tot de Cyber Verification en Life Sciences Verification Programs van het bedrijf. De prijs is gelijk. De toegang niet.

## Wat de index mat

Artificial Analysis berekent de kosten per taak op basis van de prijzen voor invoer, cachetreffers, schrijven naar de cache, redeneren en antwoordtokens, gedeeld door het aantal taken en gewogen over de negen evaluaties in de index. Op die basis genereerde Fable 5.2 bij maximale effort 275 miljoen uitvoertokens, terwijl de mediaan voor vergelijkbare modellen 72,8 miljoen bedraagt. Het had 46,4 minuten per taak nodig, tegenover een mediaan van 12,7, en 216 seconden tot het eerste antwoordtoken. De samenvatting van de site noemt het model “bijzonder duur” en “zeer breedsprakig”.

De rekensom is kort. De vermelde uitvoerprijs is 40 dollar tegenover een mediaan van 10 dollar, vier keer zoveel, en het aantal tokens bedraagt ongeveer 3,8 keer de mediaan. Een factuur is prijs maal volume, en Fable 5.2 zit bij deze instelling op beide hoog. De beperkingen verdienen vermelding: dit zijn de taken van Artificial Analysis, niet die van de lezer, en het cijfer geldt voor één effort-niveau.

## De knop waar Anthropic op wijst

Anthropic betwist niet dat effort ertoe doet. De introductiepagina zegt dat Medium de standaard is in de Claude-apps en Claude Code, en dat Fable 5.2 bij Medium moeilijke taken met minder tokens voltooit dan 5.1. In vroege tests op FrontierCode 2.0, een benchmark die meet of opensourcebeheerders de codewijzigingen van een model zouden samenvoegen, scoorde Fable 5.2 bij High effort 45,3 procent tegenover 45,5 procent voor Opus 5.5 bij Max, voor ongeveer de helft van de kosten per taak. Op Perplexity's WANDR-benchmark voor dataverzameling evenaart Medium effort de beste score van Opus 5.5 voor ongeveer 40 procent van de kosten. Op Humanity's Last Exam doet Low effort dat voor minder dan een tiende. Bij Xhigh effort haalt het model 49,1 procent op FrontierCode, de hoogste score van alle uitgebrachte modellen die Anthropic testte.

Dit zijn allemaal grafieken van de aanbieder uit vroege tests. Ze laten zien dat hetzelfde model op heel verschillende punten van een kostencurve zit, afhankelijk van één parameter. Die lezing wordt ook door het onafhankelijke cijfer ondersteund. De documentatie is duidelijk over de plek van Fable: begin voor de meeste werklasten met het nieuwste Opus-model en stap over op Fable wanneer evaluaties met Opus bij hogere effort nog steeds niet “aan de vereisten voldoen”.

## Hoe de factuur hier uitkwam

Anthropic heeft prijzen eerder op deze manier gepresenteerd. In de aankondiging van Claude Opus 5.5 op 22 september stond dat het model bij de meeste werkzaamheden op het niveau van Fable 5.1 presteert en bij gebruikelijke werklasten 40 procent minder kost dan Opus 5. De prijs per token was 20 procent lager, met 4 en 20 dollar per miljoen, en volgens het bedrijf kwam de rest van de besparing doordat het minder tokens per taak gebruikte. Een factuur is ook volgens Anthropic zelf een tarief maal een aantal.

Gergely Orosz, auteur van The Pragmatic Engineer, gaf het effect meer context in een editie van 20 oktober. Hij sprak met mensen bij 27 organisaties over AI-uitgaven per ontwikkelaar: een zelfgeselecteerde steekproef, grotendeels anoniem. Hij meldt dat de uitgaven in juni en juli piekten en voor bedrijven met API-abonnementen ongeveer zijn gehalveerd. De meeste noemden een combinatie van Opus 5.5 en open modellen als reden. Eén ontwikkelaar gaf in september 2.200 dollar uit aan Opus 5 en verwacht met Opus 5.5 de helft daarvan. Orosz hoorde ook dat bij verscheidene bedrijven gesubsidieerde abonnementen aflopen, waardoor hun facturen vijf tot tien keer zo hoog zouden kunnen worden.

Fable 5.2 komt in die rekensom terecht. Een koper die naar Opus 5.5 overstapte om de factuur te halveren, heeft nu een hogere modelklasse waarvan de prijs per token daalde en waarvan de kosten per taak afhangen van een instelling waar de meeste mensen niet aankomen.

## Introductieaanbiedingen en wie de proef betaalt

In de eerste week voelen abonnees de prijs niet. Het helpcentrum van Anthropic zegt dat Pro-abonnementen en standaard Team-licenties van 9 tot 16 november alle Fable-modellen binnen hun weeklimieten krijgen, tot maximaal 50 procent van die limieten, plus één reset van de limiet. Max- en Ultra-abonnementen krijgen één tot drie resets, afhankelijk van hoelang het account betaald is. Ongebruikte resets vervallen op 8 maart 2027. De aanbiedingen gelden volgens de tekst voor abonnementen; de pagina zegt niets over API-accounts.

## Opnieuw de factuur

Terug op de verzonnen maandag bekijkt de platformverantwoordelijke de auditbatch en ziet ze niets mis met de bevindingen. Wat ontbreekt, is een vergelijking. De volgende test die ze opstelt is saai: dezelfde veertig repositories bij High effort, daarna bij Medium, met daarnaast telkens de kosten en het aantal geaccepteerde bevindingen. Of de goedkopere runs genoeg vinden, is een vraag die geen introductiepagina voor haar team kan beantwoorden, en de documentatie die ze las zegt dat ook. Het model wordt per miljoen tokens geprijsd. Haar beoordeling zal per repository worden geprijsd.

## Referenties

- Anthropic (2026). *Introducing Claude Fable 5.2 and Claude Mythos 5.2*. https://www.anthropic.com/claude-fable-and-mythos-5-2
- Anthropic (2026). *Introducing Claude Opus 5.5*. https://www.anthropic.com/news/claude-opus-5-5
- Anthropic (2026). *Claude Fable 5.2 launch offers*. Claude Help Center. https://support.claude.com/en/articles/17506494-claude-fable-5-2-launch-offers
- Anthropic (2026). *What's new in Claude Fable 5.2*. Claude Platform Docs. https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2
- Artificial Analysis (2026). *Claude Fable 5.2 (Max): Intelligence, Performance & Price Analysis*. https://artificialanalysis.ai/models/claude-fable-5-2
- Brandom, R. (2026). *Anthropic releases new Mythos and Fable models amid RSI concerns*. TechCrunch. https://techcrunch.com/2026/11/09/anthropic-releases-new-mythos-and-fable-models-amid-rsi-concerns/
- Forlini, E. (2026). *Anthropic debuts Claude Fable, Mythos 5.2 models, priced 20% below OpenAI's GPT-6 Astra*. Fortune. https://fortune.com/2026/11/09/anthropic-debuts-updated-claude-fable-and-mythos-models-undercutting-price-of-openais-gpt-6-astra-by-up-to-80/
- Orosz, G. (2026). *What's the ROI of software engineers' spending on AI?* The Pragmatic Engineer. https://newsletter.pragmaticengineer.com/p/whats-the-roi-of-software-engineers
