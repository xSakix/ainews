+++
title = "Een 4B-agent leerde wanneer hij moet klikken of typen"
slug = "een-4b-agent-leerde-wanneer-hij-moet-klikken-of-typen"
description = "Microsofts Mage-VL-Cowork bedient met één open model zowel het scherm als een terminal die tussen opdrachten actief blijft. Bij de training bleek het nuttiger om het leraarmodel minder gereedschap te geven en korte, succesvolle routes te belonen dan om nog een interface toe te voegen."
tags = ["models", "agents", "research"]
date = 2026-10-31T04:03:07+01:00
draft = false
+++

Een analist moet in een spreadsheet twee kopstroken samenvoegen en een grafiek toevoegen. Het bestand moet in het formaat `.xlsx` bewaard blijven. De analist is verzonnen, maar de keuze is reëel: met de muis via menu's cel voor cel werken, of een shell openen en de werkmap met Python bewerken. Een bekwame computeragent zou al vóór de eerste klik moeten weten welke aanpak bij de taak past.

## Eén model, twee manieren om te handelen

Het Mage-team van Microsoft heeft Mage-VL-Cowork uitgebracht onder de Apache-2.0-licentie. Het model telt 4,74 miljard parameters en kan een grafisch bureaublad bedienen of werken in een Bash- en Python-omgeving die tussen opdrachten actief blijft. Het laat de keuze niet over aan een extern systeem. Bij elke beurt bepaalt hetzelfde beeld-taalmodel of een van de elf schermacties nodig is of een terminalopdracht.

Het lijkt een klein verschil, maar de keuze bepaalt hoeveel ruimte een agent in zijn contextvenster gebruikt en hoe rechtstreeks hij zijn werk kan controleren. Eén schermafbeelding kan duizenden tokens kosten. Een lange reeks muisklikken benadert soms maar gebrekkig wat een softwarebibliotheek exact kan uitvoeren. Omgekeerd ziet de terminal geen onopgeslagen tekenvlak, dialoogvenster of tijdelijke toestand van een toepassing. Het model heeft beide kanalen nodig en moet leren wanneer het welk kanaal kiest.

Het Mage-team meldt een score van 66,04 procent op OSWorld-Verified, gemiddeld over twee rondes van 361 taken met een limiet van 50 stappen. De afzonderlijke scores waren 65,33 en 66,75 procent. Mensen scoren in de vergelijkingstabel van het team 72,4 procent. GPT-5.4-mini haalt in één ronde met dezelfde taken en staplimiet 69,6 procent. Van de vergeleken modellen met open gewichten scoort ScaleCUA-Qwen3.5-9B het hoogst met 68,7 procent. Het team claimt voor Mage-VL-Cowork dus alleen de beste score onder de 4B-modellen.

De metingen komen van Microsoft en zijn nog niet onafhankelijk gereproduceerd. De repository bevat de evaluatietaken, de code van de agent en de opstartscripts. Dat maakt de claim beter toetsbaar dan een los cijfer op een modelkaart.

## Het leraarmodel moest gereedschap inleveren

Het werk begon al bij het maken van de trainingsvoorbeelden. Zelfs een krachtig leraarmodel met toegang tot alle beschikbare interfaces leverde niet vanzelf eenduidige voorbeelden. Dezelfde stap kon op verschillende manieren worden uitgevoerd: via de toegankelijkheidsboom, via directe automatisering van het bureaublad of door op zicht te klikken. Zo kreeg het leerlingmodel voor dezelfde stap verschillende handelwijzen te zien.

Het team vergeleek twee opstellingen voor het leraarmodel op 672 taken die meerdere toepassingen vereisten en buiten de training waren gehouden. In de gekozen opstelling kreeg GPT-5.4 grafische hulpmiddelen en programmeergereedschap. Hulpmiddelen met overlappende functies, zoals `xdotool` en uitdraaien van toegankelijkheidsgegevens, verdwenen. Bibliotheken voor spreadsheets, documenten, presentaties, pdf's en afbeeldingen waren vooraf geïnstalleerd. Het leraarmodel voltooide zo 92,0 procent van de taken, in gemiddeld 25 stappen. De opstelling met extra toegankelijkheidsinformatie haalde 89,6 procent in 35,33 stappen.

Na distillatie werd het verschil groter. Een leerlingmodel met 4 miljard parameters dat met voorbeelden uit de afgeslankte opstelling was getraind, haalde 37,6 procent. De leerling die voorbeelden uit de uitgebreidere opstelling kreeg, haalde 25,1 procent. Het gemiddelde aantal stappen daalde van 39,40 naar 30,91. Beide resultaten komen van hetzelfde onderzoeksteam. Toch maakt de vergelijking een probleem zichtbaar: een toonaangevend model kan overbodige keuzes opvangen door meer stappen te zetten, terwijl een kleine leerling de verwarring overneemt.

Ook bij het genereren van data koos het team voor hergebruik. Mage-CUA-Forge genereerde 293.806 taken verdeeld over 6.915 elementaire vaardigheden en behield 318.837 trajecten waarin beide bedieningswijzen konden voorkomen. In plaats van een agent elke omgeving van de grond af te laten opbouwen, maakte het systeem per vaardigheid eenmalig herbruikbare werkprocessen en routines die elke toepassing klaarzetten. Met hetzelfde generatiemodel daalde het aantal tokens per taak volgens het team van 1,276 miljoen naar 85.000 en daalden de terugkerende kosten van 0,906 naar 0,158 dollar per taak.

Dit zijn synthetische trainingsgegevens op industriële schaal. Hun waarde hangt af van de juistheid van de voorbereidingsroutines, taakomschrijvingen en beoordelingscriteria. Volgens de repository vereist 38,24 procent van de gegenereerde taken meerdere toepassingen. Van de acties in de trajecten verloopt ongeveer 68 procent via de grafische interface en 32 procent via de terminal.

## Eerst specialiseren, dan combineren

Mage-VL-Cowork vertrekt vanuit een tussentijdse versie van Mage-VL die nog niet gespecialiseerd is in grafische bediening of programmeren. De training verloopt in vijf fasen: visuele verwijzingen aan de juiste plek op het scherm koppelen, grafische taken in meerdere stappen uitvoeren, programmeren en de terminal bedienen, beide werkwijzen combineren met begeleide finetuning, en ten slotte online trainen met beloningen.

Die volgorde doet ertoe. Het model leert eerst beide kanalen goed te gebruiken en leert pas daarna ertussen te kiezen. Na de gecombineerde begeleide training scoorde het 55,84 procent op OSWorld-Verified. Online trainen met beloningen bracht de score op 66,04 procent. Tegelijk daalde het gemiddelde aantal modelaanroepen van 21,57 naar 18,77 en het aantal uitvoertokens per taak van 7.374 naar 5.499.

Door de beloning bleef de agent niet simpelweg langer proberen. De succesvolle routes werden korter. Het team koppelde de beloning aan controleerbare resultaten voor 1.988 taken, met ruimte voor 768 episodes per update. Hoewel deze fase volgens de berekening van het team slechts 3,5 procent van het trainingsschema besloeg, vergde ze nominaal meer rekenwerk dan elk van de andere fasen afzonderlijk.

Bij lange sessies op het bureaublad ontstaat nog een probleem: het contextvenster kan al vol zitten met schermafbeeldingen voordat het werk af is. Mage-VL-Cowork bewaart de drie recentste schermafbeeldingen en vier volledige antwoorden van de assistent. Van elke oudere beurt blijft één regel over die de actie beschrijft. Zo beschikt het model over recente visuele veranderingen én een beknopt verslag van eerder werk.

Het actieve contextvenster telt 32.768 tokens, al ondersteunt de architectuur er meer. Bij elke stap geeft het model zijn redenering, een korte samenvatting van de actie en een aanroep van een hulpmiddel. Hierdoor kan een oude redenering verdwijnen terwijl het verslag van de actie behouden blijft.

## De grenzen van de benchmark

OSWorld is ontworpen om agenten te testen in echte toepassingen en bij taken in het besturingssysteem, in plaats van op afzonderlijke websites. De geverifieerde takenset maakt de automatische beoordeling betrouwbaarder. Toch liggen de omgeving, de geïnstalleerde software en de succescriteria bij een benchmark vast. De test laat niet zien wat er gebeurt als een agent een persoonlijke wachtwoordkluis, een onvoorspelbaar netwerk of een document met kwaadaardige instructies tegenkomt.

Microsofts eigen gebruiksadvies weerspiegelt die beperking. Het model kan willekeurige shellopdrachten uitvoeren en een bureaublad bedienen. Het team raadt daarom virtuele machines of containers aan die na gebruik kunnen worden weggegooid, zonder persoonlijke inloggegevens en met beperkt uitgaand netwerkverkeer. Voor onomkeerbare acties adviseert het menselijke bevestiging. Het model is uitgebracht voor onderzoek, niet voor gebruik in een product.

Dat het een 4B-model is, maakt het volledige systeem nog niet licht. Het team meldt voor de training van het taalmodel over de vijf fasen in totaal 7,79 zettaFLOPs aan nominaal rekenwerk. Voor het trainen met beloningen gebruikte het 32 NVIDIA B200-GPU's en 1.120 CPU-sandboxplaatsen. Om de BF16-versie te draaien is alleen voor de twee bestanden met modelgewichten al ongeveer 9,48 GB nodig. Het werkgeheugen voor de uitvoering en de bureaubladomgeving komen daar nog bij.

De overtuigendste bijdrage van deze release is de trainingsaanpak. De ontwerpers beperkten de keuzes van het leraarmodel, bouwden taken rond herbruikbare vaardigheden en trainden de twee bedieningswijzen afzonderlijk. Pas daarna beloonden ze het model voor het voltooien van controleerbare taken met minder aanroepen.

Terug naar de denkbeeldige analist. De grafiek hoort nog steeds thuis in de grafische toepassing, waar te zien is hoe ze eruitziet. Voor het samenvoegen van de cellen is Python geschikt: daarmee kan de bestandsstructuur nauwkeurig worden gewijzigd en gecontroleerd. De belangrijkste stap vindt plaats voordat een van beide hulpmiddelen opengaat. Het model kiest een route, en die keuze maakt nu deel uit van een beslisstrategie die iedereen kan onderzoeken.

## Referenties

- Microsoft Mage Team. (2026). *Mage: A Lightweight, Research-Friendly Multimodal Model Family*. https://github.com/microsoft/Mage
- Microsoft Mage Team. (2026). *Mage-VL-Cowork: A Full Training Recipe to Learn Hybrid Computer Use from Evolved Harnesses*. https://github.com/microsoft/Mage/blob/main/assets/mage_vl_cowork_tech_report.pdf
- Microsoft. (2026). *Mage-VL-Cowork model card*. https://huggingface.co/microsoft/Mage-VL-Cowork
- Xie, T., et al. (2024). *OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments*. https://arxiv.org/abs/2404.07972
- Yang, S., et al. (2026). *Mage-VL: An Efficient Codec-Native Streaming Multimodal Foundation Model*. https://arxiv.org/abs/2607.24904
