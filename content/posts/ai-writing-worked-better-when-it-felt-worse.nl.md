+++
title = "Schrijven met AI ging beter wanneer het slechter aanvoelde"
slug = "schrijven-met-ai-beter-wanneer-het-slechter-aanvoelde"
description = "In een gerandomiseerd experiment schreven werknemers betere beleidsnotities nadat een AI-interface hen het doel liet bepalen en de taak liet opdelen. Toch vonden ze de tool minder behulpzaam, wat een tekortkoming blootlegt in hoe teams AI-producten beoordelen."
tags = ["research", "tools"]
date = 2026-10-23T04:10:11+02:00
draft = false
+++

Een beleidsanalist zit aan het einde van een lange middag nog achter haar bureau. Ze moet een notitie voor de directie schrijven en heeft een chatvenster dat in seconden een concept kan produceren. Dan remt de software haar af. Voordat die gaat schrijven, vraagt hij wie de notitie moet lezen, wat die lezer moet doen, hoeveel detail in het antwoord thuishoort en welke delen van het werk afzonderlijk moeten worden behandeld. De analist in dit tafereel is verzonnen. De vertraging niet: die is het centrale mechanisme in een nieuw experiment naar wat er gebeurt wanneer een AI-schrijftool weigert het denkwerk te laten verdwijnen.

## Een schrijftool die eerst vragen stelt

De preprint, op 22 oktober gepubliceerd door Viktor Kewenig, Lev Tankelevitch, Sean Rintel, Advait Sarkar en Abigail Sellen van Microsoft Research, beschrijft een gerandomiseerd experiment met 297 in de VS gevestigde werknemers met Engels als moedertaal, geworven via Prolific. Samen schreven ze 594 professionele notities. Eén groep gebruikte een standaardinterface met chat en canvas, gekoppeld aan GPT-5.3. De andere kreeg dynamisch gegenereerde bedieningselementen te zien die hen hun doel lieten specificeren en de taak in delen lieten opsplitsen voordat het model een concept schreef.

De ondersteuning vroeg onder meer naar de beoogde boodschap, de doelgroep, het gewenste resultaat, de reikwijdte en de diepgang. Vervolgens genereerde ze taakspecifieke bedieningselementen voor analyse, structuur en kritische overwegingen. Deelnemers konden die in natuurlijke taal aanpassen. De interface verving de chat niet; ze voegde een planningslaag in vóór de vertrouwde handeling waarbij een model wordt gevraagd iets te schrijven.

Die extra laag verbeterde het werk. Bij de eerste taak, waarin de ondersteuning aanwezig was, vond de geautomatiseerde beoordelaar van de onderzoekers een statistisch betrouwbaar voordeel in de samengestelde score van zeven onderdelen. Menselijke beoordelaars die een benchmark van 107 essays onderzochten, vonden eveneens een voordeel in de samengestelde score, dat bovendien groter was. De winst beperkte zich niet tot nettere opmaak: vóór de geautomatiseerde beoordeling werden koppen, nadrukmarkeringen en lijstmarkeringen verwijderd, en de sterkste effecten betroffen de kwaliteit van argumenten, de geloofwaardigheid van bewijs en de aandacht voor gevolgen.

Het vreemdere resultaat kwam bij de tweede taak. Beide groepen gebruikten nu de gewone interface. Mensen die eerder de ondersteuning hadden gekregen, schreven nog steeds betere notities. Hun prompts formuleerden ook duidelijker doelen en deelden het werk bewuster op, volgens een geblindeerde codering van de volledige promptreeksen. Een korte interventie leek te veranderen wat mensen de AI vroegen te doen nadat de interventie was verdwenen.

## Het ongemakkelijke signaal

De deelnemers beloonden de interface niet voor deze verbetering. Wie de ondersteuning had gebruikt, beoordeelde de AI als minder behulpzaam en ervoer minder controle. Hun gemiddelde score voor werklast terwijl de ondersteuning actief was, bedroeg 4,71, tegenover 3,96 voor de controlegroep. Toen beide groepen naar de tweede taak zonder ondersteuning gingen, was dat verschil in werklast klein en niet statistisch betrouwbaar.

Dat ongemak doet ertoe omdat gemak een van de zichtbaarste signalen is waarover een productteam beschikt. Een functie die klikken, vragen of beslissingen toevoegt, kan in een gebruikerstest een achteruitgang lijken. Het experiment suggereert dat dit signaal de verkeerde kant op kan wijzen. De soepelere ervaring kan juist het denkwerk wegnemen dat iemand helpt het probleem af te bakenen, te bepalen wat succes betekent en op te merken wat het model heeft weggelaten.

Eerder onderzoek had al delen van dit spanningsveld blootgelegd. Shakked Noy en Whitney Zhang vonden dat ChatGPT de uitvoeringstijd kon verkorten en de kwaliteit bij professionele schrijftaken kon verbeteren. Zana Buçinca en collega’s vonden dat functies die denkwerk afdwingen overmatig vertrouwen in AI-advies konden verminderen, hoewel gebruikers niet altijd de doeltreffendste interventie verkozen. In het onderwijs lieten Louis Deslauriers en collega’s zien dat studenten in actieve leersessies meer leerden, terwijl ze het gevoel hadden minder te hebben geleerd dan medestudenten in vlot gegeven hoorcolleges.

AI kan de tegenstelling aanscherpen doordat hetzelfde venster zowel hulp als uitbesteding van denkwerk biedt. Een werknemer kan het verdwijnen van inspanning ervaren als bewijs dat de tool hielp. Maar inspanning is ook de manier waarop mensen doelen vaststellen, argumenten toetsen en het materiaal onthouden. Hamsa Bastani en collega’s illustreerden het risico in een gerandomiseerd onderzoek naar wiskunde op middelbare scholen: toegang tot een algemene GPT-4-tutor verbeterde de prestaties tijdens begeleid oefenen, maar leerlingen presteerden later slechter op een examen zonder hulp. Een tutor met vangrails voorkwam het grootste deel van die schade, al leverde die geen examenvoordeel op tegenover de controlegroep zonder AI.

## Beter werk, beperkt bewijs

Kewenig en collega’s testten ook het geheugen. Drie dagen na de schrijfsessie keerden 159 deelnemers terug voor een vrijwillig vervolgonderzoek. Van die respondenten herinnerde 64,6 procent van de groep met ondersteuning zich het onderwerp van de eerste taak, tegenover 45,6 procent van de controlegroep. Voor de tweede taak, zonder ondersteuning, waren de cijfers 54,4 en 38,0 procent. Een analyse waarin ontbrekende uitkomsten werden geïmputeerd, behield een positief verband.

Die cijfers vragen om terughoudendheid. Bijna de helft van de groep leverde geen gescoord antwoord op de geheugentest, de betrouwbaarheidsintervallen waren breed en de test kende punten toe voor elke juiste benoeming van het onderwerp. Die stelde geen diepgaand begrip vast. Het experiment was niet vooraf geregistreerd, gebruikte eenmalige online schrijftaken en mat overdracht alleen naar de volgende taak. Het kan niet aantonen dat een week aan prompts uitgroeit tot een blijvende professionele vaardigheid.

Ook de kwaliteitsmaatstaf verdient zorgvuldigheid. De primaire beoordelaar was GPT-5.4, gekalibreerd op menselijke beoordelingen. De overeenstemming met de menselijke benchmark was matig en het model drukte het bereik van de scores die mensen gaven samen. De door mensen beoordeelde deelverzameling ondersteunde de richting van het hoofdresultaat, maar de twee benaderingen legden de nadruk op verschillende sterke punten. De auteurs beschouwen de kwaliteitsscores daarom naast het bewijs uit prompts, zelfrapportage en herinnering, en niet als een op zichzelf staand oordeel.

Er blijft nog een ontwerpvraag open. De interventie combineerde doelspecificatie met taakopdeling, dus het experiment kan niet zeggen welk onderdeel het effect veroorzaakte. Ook ontbrak een conditie met een statische checklist. Een eenvoudiger formulier zou een deel van het voordeel kunnen behouden zonder dezelfde cognitieve belasting. Alleen een langer onderzoek op de werkplek zou kunnen laten zien of herhaalde ondersteuning een gewoonte wordt, een ergernis wordt of sommige werknemers helpt en anderen hindert.

## Wrijving waarvan de waarde zichtbaar is

De bruikbare les is beperkter dan “maak AI moeilijker te gebruiken”. De meeste wrijving is gewoon wrijving. Een traag antwoord, een willekeurig formulier of een extra bevestigingsvenster schept geen oordeelsvermogen. De interventie in dit onderzoek richtte zich op twee specifieke handelingen die gewone chatinterfaces gebruikers uitnodigen over te slaan: het resultaat benoemen en de weg ernaartoe structureren.

Dat onderscheid wordt belangrijker naarmate AI-producten verschuiven van zinnen schrijven naar hele werkreeksen uitvoeren. Wanneer een systeem kan plannen, zoeken en handelen voordat iemand de tussenstappen ziet, kan een prettige ervaring er een zijn waarin de gebruiker minder van de bedoeling aanlevert en minder van het resultaat begrijpt. Teams hebben maatstaven nodig die verder gaan dan tevredenheid: uitvoerkwaliteit, latere prestaties, foutdetectie en wat gebruikers kunnen uitleggen nadat de tool is gesloten.

De denkbeeldige analist bekijkt inmiddels de gegenereerde notitie. De extra vragen hebben haar enkele minuten gekost. Ze ergert zich er nog steeds aan. Maar wanneer haar directeur vraagt waarom de aanbeveling bij deze doelgroep past, kan ze antwoorden zonder de chat opnieuw te openen. De interface voelde slechter aan omdat de tool een deel van het werk bij haar liet. Juist dat behouden werk kan de waardevolle functie zijn.

## Referenties


- Bastani, H., Bastani, O., Sungu, A., Ge, H., Kabakcı, Ö., & Mariman, R. (2025). *Generative AI without guardrails can harm learning: Evidence from high school mathematics*. https://www.pnas.org/doi/10.1073/pnas.2422633122
- Buçinca, Z., Malaya, M. B., & Gajos, K. Z. (2021). *To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI in AI-assisted Decision-making*. https://dl.acm.org/doi/10.1145/3449287
- Deslauriers, L., McCarty, L. S., Miller, K., Callaghan, K., & Kestin, G. (2019). *Measuring actual learning versus feeling of learning in response to being actively engaged in the classroom*. https://www.pnas.org/doi/10.1073/pnas.1821936116
- Kewenig, V., Tankelevitch, L., Rintel, S., Sarkar, A., & Sellen, A. (2026). *Metacognitive Scaffolds Create Productive Friction for AI-Assisted Knowledge Work*. https://arxiv.org/abs/2610.30945
- Noy, S., & Zhang, W. (2023). *Experimental evidence on the productivity effects of generative artificial intelligence*. https://www.science.org/doi/10.1126/science.adh2586
