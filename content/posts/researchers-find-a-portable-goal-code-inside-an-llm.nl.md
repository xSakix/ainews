+++
title = "Onderzoekers vinden overdraagbare doelcode in een taalmodel"
slug = "onderzoekers-vinden-overdraagbare-doelcode-in-taalmodel"
description = "Een nieuwe preprint herleidt het volgende programmeerdoel van een LLM tot een kleine groep attentionheads, leest het in gewone taal en verplaatst het tussen programmeertalen. Het resultaat is causaal bewijs uit een gecontroleerde omgeving, geen bewijs dat elke agent een stabiele innerlijke intentie heeft."
tags = ["research", "models", "agents"]
date = 2026-11-14T04:08:30+01:00
draft = false
+++

Neem een fictieve ontwikkelaar, Mara, op het moment dat een gegenereerde functie klaar is met het tellen van woorden die met een hoofdletter beginnen en op het punt staat palindromen te controleren. De cursor staat na een gelijkteken. Er is nog geen vergelijking verschenen, geen tekenreeks omgekeerd en geen uitvoertoken dat zegt wat volgt. Mara zou het model daar willen pauzeren met een eenvoudige vraag: wat probeert het nu te doen? Het is een illustratieve scène. Een nieuw experiment maakt van die vraag iets wat onderzoekers binnen een model kunnen testen.

## Een doel vóór de code

Arnab Sen Sharma en negen collega's van Northeastern University, Parallax, de University of Copenhagen en de University of Oxford melden dat het volgende subdoel van een codeermodel te lokaliseren is in een kleine groep attentionheads. Hun preprint van 12 november gaat verder dan een correlatie vinden. De onderzoekers decoderen de representatie naar natuurlijke taal, verplaatsen haar naar een andere programmeertaal en grijpen erop in om te veranderen wat het model schrijft.

Het werk stelt een beperkte versie van een brede, beladen vraag: hebben taalmodellen doelen? De auteurs behandelen vloeiend gedrag niet als bewijs van intentie. Ze definiëren een doel als een interne toestand die vóór een handeling verschijnt, via verschillende middelen kan worden gerealiseerd en tijdens de handeling blijft bestaan. Die operationele definitie levert drie tests op: vooraf vastleggen, flexibiliteit en voortbestaan.

De gecontroleerde taak maakt die tests mogelijk. Prompts vroegen een model twee tot vier onafhankelijke bewerkingen op gehele getallen, tekenreeksen of lijsten te voltooien. Een bewerking kon woorden met een beginhoofdletter tellen, een bereik zoeken of controleren of een woord een palindroom is. De onderzoekers gebruikten 253 specificaties en bekeken vier posities voordat elke volgende bewerking begon, goed voor 1.012 observaties per evaluatieconfiguratie.

De meeste hoofdresultaten gebruiken Qwen-2.5-Coder-32B-Instruct, een model met 64 lagen. Een procedure voor selectie van een kleine groep identificeerde 122 attentionheads, vooral tussen laag 28 en 55. De procedure beloonde heads waarvan de uitvoer vanuit een bronprompt in de ene programmeertaal naar een doelprompt in een andere taal kon worden verplaatst en daar de bronbewerking kon laten beginnen. Verschillende talen kiezen was belangrijk: een representatie van palindroomcontrole moest veranderingen in syntaxis, variabelenamen en concrete tokens overleven.

## De verborgen instructie lezen

Om de representatie leesbaar te maken bouwde het team een probe, GoalScope, op basis van de uitvoer van de geselecteerde heads. Die telt op wat de heads bij een gekozen token in de residual stream van het model schrijven en injecteert die vector in een aparte uitvoering van hetzelfde model. De tweede uitvoering krijgt een vast verzoek om de bewerking te beschrijven. De tekstprompt bevat geen informatie uit het oorspronkelijke programmeerprobleem. De geïnjecteerde activatie is dus de enige route waarlangs de oorspronkelijke context het antwoord kan bereiken.

Deze methode bouwt voort op Patchscopes, een framework van Asma Ghandeharioun en collega's dat een verborgen representatie in een prompt plaatst waar een taalmodel haar kan uitleggen. Ze volgt ook eerder werk van verschillende van dezelfde onderzoekers. *Function Vectors* liet zien dat een compacte som van attentionheaduitvoer een invoer-uitvoerfunctie kon dragen en die functie in een nieuwe context kon activeren. *General Filter Heads* isoleerde later een overdraagbare representatie van predicaten waarmee lijsten worden gefilterd. De nieuwe paper verschuift van één bewerking naar de veranderende volgende stap in een taak met meerdere bewerkingen.

Het uitlezen van het doel werd bruikbaar voordat het model de implementatie uitstuurde. Aan het einde van de voorgaande regel kwamen GoalScope-beschrijvingen in ongeveer zestig procent van de gevallen overeen met een niet-triviaal deel van het komende gedrag. Bij de inspringpositie, drie tokens vóór de implementatie, lag de gerapporteerde score boven negentig procent. Na overplaatsing naar een C++-context activeerde de codering op één overdrachtspositie in 96 procent van de gevallen de bijbehorende bewerking; het gemiddelde over de posities was ongeveer 87 procent.

Die resultaten ondersteunen vooraf vastleggen en flexibiliteit. Ze zeggen dat de geselecteerde activiteit informatie draagt over wat er moet gebeuren voordat de relevante code verschijnt, en dat die informatie niet alleen een gecachte reeks Python-tokens is. Het doelmodel produceert een route die bij de nieuwe context past.

De causale tests scherpen die claim aan. Toen de onderzoekers de geselecteerde heads toegang tot de volgende taak lieten houden, maar ongeveer 93 procent van de latere attentionheads de toegang tot dat tekstdeel blokkeerden, behield het model grotendeels zijn vermogen om de bewerking te implementeren. Alleen de 122 geselecteerde heads blind maken liet compensatie via redundante paden toe. Een bredere groep van 250 heads blind maken verlaagde de prestaties echter sterk. De auteurs beschrijven dit als een causaal knelpunt met redundantie, niet als één onmisbare schakelaar.

## Een doel dat bij elke stap wordt gereconstrueerd

Voortbestaan levert een mechanische puzzel op. Een autoregressieve transformer heeft geen recurrente toestand die eenvoudig voor altijd van het ene gegenereerde token naar het volgende kan worden doorgegeven. Attention kan een eerdere positie lezen, maar een nieuw berekende toestand vooruit verplaatsen kost lagen. In dit model kon het doel pas na ongeveer laag veertig in woorden worden uitgedrukt. Daardoor bleef te weinig diepte over om dezelfde toestand door bewerkingen van meer dan dertig tokens heen te dragen.

De auteurs stellen een ander mechanisme voor. Het model leest de taakspecificatie telkens opnieuw, bekijkt de voltooide code die zichtbaar is in de context en reconstrueert de nog uit te voeren bewerking. Ze noemen dit niet-recurrent doelgericht handelen. De schijnbare continuïteit komt voort uit herhaalde berekening, niet uit één intern object dat ongewijzigd door de reeks reist.

Gerichte transplantaties ondersteunden die verklaring. De onderzoekers veranderden de key-valuetoestanden die de doelheads uit het taakgedeelte lazen, terwijl andere heads op de doelprompt bleven werken. Het model implementeerde vervolgens in ongeveer 94 procent van de gevallen de volgende bewerking uit de bronprompt in de doelprogrammeertaal. De beschrijving van GoalScope verschoof in ongeveer negentig procent van de gevallen mee. In een aparte ingreep droeg vervanging van de querytoestanden van de heads informatie over voltooid werk over en veranderde welke resterende subtaak het model koos.

Dat onderscheid is belangrijk voor toezicht. Een monitor kan mogelijk een komende bewerking lezen voordat die in de uitvoer verschijnt, en een ingreep kan haar mogelijk omleiden. Maar de representatie wordt samengesteld uit de specificatie en de zichtbare voortgang. Verandert een van beide bronnen, dan kan ook het schijnbare doel veranderen.

## De grenzen van een leesbaar doel

De paper toont geen universeel doelcentrum aan. De centrale dataset bestaat uit opgesomde programmeerbewerkingen, de meeste metingen in de hoofdtekst komen van één op code afgestemd model en een LLM beoordeelt of gegenereerde beschrijvingen en implementaties overeenkomen. De auteurs testen andere modelfamilies en enkele situaties met natuurlijke taal in de bijlagen, maar noemen de dekking van modellen en taken als beperking.

De sterkste waarschuwing verschijnt wanneer het traject wordt verstoord. Het model behield tijdens gewone uitvoering een herkenbare codering, maar herstelde vaak niet van een geplante valse start. Qwen-2.5-Coder-32B-Instruct paste zich aan in ongeveer 97 procent van de overeenstemmende gevallen, 63 procent van de eenvoudige verstoringen en slechts vijftien procent van de moeilijke. Andere geteste modellen lieten dezelfde daling zien. Een leesbaar doel garandeerde geen succesvolle uitvoering.

Terug naar Mara bij de wachtende cursor. In deze verzonnen slotscène toont haar debugger een voorlopige notitie: controleren of een woord een palindroom is. Ze behandelt die als een voorspelling die bij deze prompt en dit punt in de code hoort, niet als een bekentenis van een machine. Dan voegt ze een misleidend voorvoegsel in. De notitie noemt nog steeds de taak, terwijl de gegenereerde code afdwaalt. Het nieuwe onderzoek geeft haar zicht op de volgende bewerking van het model. Het laat ook zien waarom een doel waarnemen en op de uitvoering vertrouwen verschillende taken blijven.

## Referenties

- Ghandeharioun, A., Caciularu, A., Pearce, A., Dixon, L., & Geva, M. (2024). *Patchscopes: A Unifying Framework for Inspecting Hidden Representations of Language Models*. https://arxiv.org/abs/2401.06102
- Sen Sharma, A., Rogers, G., Shapira, N., & Bau, D. (2026). *LLMs Process Lists With General Filter Heads*. https://arxiv.org/abs/2510.26784
- Sen Sharma, A., Todd, E., Feucht, S., Arditi, A., Gandikota, R., Shapira, N., Sarti, G., Fierro, C., Schut, L., & Bau, D. (2026). *Goal Encoding in LLMs*. https://arxiv.org/abs/2611.17297
- Todd, E., Li, M. L., Sen Sharma, A., Mueller, A., Wallace, B. C., & Bau, D. (2024). *Function Vectors in Large Language Models*. https://arxiv.org/abs/2310.15213
