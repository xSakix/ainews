+++
title = "Waarom AI-proza grammaticaal klopt maar moeilijk leest"
slug = "waarom-ai-proza-grammaticaal-klopt-maar-moeilijk-leest"
description = "Een nieuwe studie vindt dat negen toonaangevende modellen herhaaldelijk taalvormen kiezen die met meer leesinspanning samenhangen. Het finetuningexperiment wijst op een conflict tussen compacte machineredeneringen en taal die voor menselijk begrip is gemaakt."
tags = ["research", "models"]
date = 2026-10-25T04:14:11+01:00
draft = false
+++

Een redacteur komt bij de vierde regel van een gegenereerd overzicht en leest die tweemaal. Elk woord past. De zin is grammaticaal correct. Toch zijn de zelfstandige naamwoorden tot een blok opgestapeld, is iets dat niet kan handelen tot handelende partij gemaakt en was het werkwoord ooit een zelfstandig naamwoord. De redacteur in dit tafereel is fictief. De kleine weerstand in de zin is onderwerp van een echt experiment.

## De inspanning binnen een vloeiende zin

Thomas Hikaru Clark, Matias B. Martin en Kyle Mahowald wilden een klacht meten die doorgaans bij smaak blijft: recente AI-teksten kunnen moeilijk te begrijpen zijn, ook zonder duidelijke fout. Hun preprint vergelijkt tekst van negen modellen aan of nabij de technische voorhoede met menselijke teksten en met nauwe parafrases die ontstonden door modeltekst naar het Japans en terug naar het Engels te vertalen.

De modellen kozen herhaaldelijk vormen die psycholinguïsten met meer verwerkingsinspanning verbinden. Alle negen gebruikten vaker zeldzame woordreeksen en koppelden vaker levenloze onderwerpen aan werkwoorden die bij levende handelende personen horen. De meeste produceerden langere syntactische afhankelijkheden, meer gestapelde zelfstandige naamwoorden en meer betrekkelijke bijzinnen met een lijdend voorwerp waarin een optioneel verbindingswoord was weggelaten. Het patroon was het sterkst in gesprekken en codegerelateerde uitwisselingen en verschilde tussen modelfamilies.

Dit zijn geen grammaticafouten. Het Engels staat een formulering als “reader-patience budget” toe, en een lezer kan achterhalen wat wordt bedoeld met een levenloos onderwerp dat iets abstracts “opeet”. De kosten ontstaan tijdens het begrijpen. Onbekende woordcombinaties zijn moeilijker te voorspellen. Lange afhankelijkheden vragen het werkgeheugen een zinsdeel vast te houden totdat het bijbehorende deel verschijnt. Dichte naamwoordgroepen vereisen dat de lezer verbanden afleidt die de schrijver onuitgesproken liet.

Dat onderscheid doet ertoe, omdat vloeiendheid een zwakke test voor leesbaarheid is geworden. Een model kan de Engelse syntaxis volgen en toch constructies kiezen die menselijke sprekers doorgaans vermijden. Zijn proza kan een grammaticale controle doorstaan en de lezer toch meer inspanning kosten dan het idee vereist.

## Menselijke taal helpt haar lezers

De paper bouwt op decennia onderzoek naar hoe taal zich aan menselijke beperkingen aanpast. Edward Gibson en collega’s beschrijven menselijke talen als compromissen tussen spreekinspanning en begripsinspanning. In 37 talen vonden Richard Futrell, Mahowald en Gibson grootschalig bewijs dat woorden met een syntactische relatie doorgaans dicht bij elkaar blijven. Kortere afhankelijkheden verminderen de geheugenbelasting.

Voorspelbaarheid oefent een andere druk uit. Roger Levy en T. Florian Jaeger stelden dat sprekers informatiedichtheid regelen door optionele woorden te behouden of weg te laten afhankelijk van wat volgt. Een spreker voegt eerder “that” toe wanneer dit een luisteraar voorbereidt op minder voorspelbaar materiaal. Nathaniel Smith en Levy vonden later dat leestijd ruwweg toeneemt met de verrassingswaarde van een woord: ongebruikelijke vervolgen brengen meetbare kosten mee.

Dat werk behandelt redundantie als onderdeel van communicatie, niet als verspilling. Een vertrouwde formulering, een optioneel verbindingswoord of een herhaald signaal kan het brein tijd geven om bij te blijven. Eric Martínez en collega’s toonden het gevolg in juridische taal. De moeilijkheid van contracten kwam voor een aanzienlijk deel door schrijfkeuzes zoals middenin ingebedde bijzinnen en onnodig jargon, niet alleen door gespecialiseerde begrippen.

Clark, Martin en Mahowald vragen wat er gebeurt wanneer de taalproducent die menselijke beperkingen niet deelt. Moderne modellen worden op menselijke tekst getraind, maar natraining beloont steeds vaker correcte antwoorden bij wiskunde, programmeren en redeneren. Succes kan aan het einde van een taak worden geverifieerd. De weg naar dat antwoord hoeft voor een mens niet altijd prettig leesbaar te zijn.

## Een parallel corpus scheidt betekenis van vorm

De onderzoekers verzamelden modeluitvoer in drie situaties: chat, programmeren en essays. Menselijk vergelijkingsmateriaal kwam uit OpenSubtitles voor gesprekken, Stack Exchange voor technisch proza en het PERSUADE 2.0-corpus van studentenessays. Ze identificeerden moeilijke constructies met afhankelijkheidsontleding, aangevuld met geautomatiseerde classificatie wanneer ontleding alleen niet kon bepalen of een onderwerp levend was of een zelfstandig naamwoord tot werkwoord was gemaakt.

Modeltekst vergelijken met menselijke corpora laat een mogelijk bezwaar open. Onderwerpen kunnen verschillen, en een technisch antwoord gebruikt natuurlijk andere taal dan een filmondertitel. Het team bouwde daarom een parallelle controle. Elke modelzin ging via een vertaalmodel met 3,3 miljard parameters naar het Japans en terug naar het Engels, met behoud van de globale betekenis maar een andere formulering.

De oorspronkelijke antwoorden van de meeste toonaangevende modellen bevatten meer zeldzame bigrammen en een hogere n-gramperplexiteit dan hun vertaalde parafrases. Vergelijkbare verschuivingen verschenen bij levenloze onderwerpen, van zelfstandige naamwoorden afgeleide werkwoorden en gereduceerde betrekkelijke bijzinnen met een lijdend voorwerp. De Llama-modellen en het OLMo-basismodel veranderden minder. OLMo Think, een redeneervariant, leek meer op de toonaangevende systemen. Claude Opus 5.5 scoorde in 19 van 21 vergelijkingen lager dan Opus 5, bewijs dat deze neigingen bij veranderende modellen ook de andere kant op kunnen bewegen.

De heen-en-terugvertaling is een controle, geen perfecte menselijke herschrijving. Vertaalsystemen hebben eigen voorkeuren en Japans werd juist gekozen omdat een niet-verwante tussentaal doorgaans gevarieerdere parafrases oplevert. Toch houdt de vergelijking de betekenis beter gelijk dan een eenvoudige tegenstelling tussen niet-gerelateerde menselijke en modeldocumenten. Ze suggereert dat de moeilijke vormen voortkomen uit de uitdrukkingswijze van het model, niet alleen uit het onderwerp.

## De lengtestraf veranderde de grammatica

Het tweede experiment testte een mechanisme. De onderzoekers finetuneden Qwen2.5-1.5B-Instruct om gestructureerde gebeurtenisregistraties in zinnen om te zetten. Zowel een kortere als een langere constructie kon het juiste antwoord uitdrukken. Bekrachtigingsleren beloonde correctheid, terwijl een instelbare straf lengte belastte. Sommige runs gebruikten ook een beperking die het gefinetunede model ontmoedigde te ver af te wijken van zijn oorspronkelijke tokenverdeling.

Elke positieve lengtestraf duwde de onbeperkte runs naar een categorische voorkeur voor de kortere vorm. Bij de getrainde constructies gebruikte meer dan 98 procent van de antwoorden het korte alternatief. De voorkeur werd overgedragen naar ongeziene voorbeelden van vergelijkbare constructies. Ze bereikte één van vier verder verwijderde grammaticale alternatieven wanneer geen beperking het model aan het basismodel bond.

Het model kreeg nooit de opdracht optionele woorden weg te laten. Het ontdekte die keuze als manier om tokens te besparen en de taakcorrectheid te behouden. Menselijke sprekers variëren dezelfde keuzes met de context. Het model leerde daarentegen een brede voorkeur voor compressie: een kleine demonstratie van hoe een op efficiëntie gerichte doelstelling taal van menselijk gebruik kan wegsturen.

Dit experiment bewijst niet dat commerciële labs dezelfde lengtestraf toepassen, of dat één beloning elk patroon in gesloten modellen verklaart. De auteurs bestudeerden Engels, een beperkte verzameling prompts en een deel van de beschikbare systemen. Ze konden natraining van toonaangevende modellen niet rechtstreeks waarnemen en beschrijven de ingreep als een proof of concept. De causale claim is beperkt: bij een gecontroleerde beloning voor bondigheid veranderden grammaticale voorkeuren in de voorspelde richting.

## Leesbaarheid wordt een modeleis

De studie herformuleert leesbaarheid als een afstemmingsprobleem met meetbare doelen. Een bruikbaar antwoord moet een juiste conclusie bereiken, maar menselijk werk hangt vaak af van het kunnen controleren van de weg ernaartoe. Een ontwikkelaar beoordeelt de patchuitleg van een agent. Een arts leest een samenvatting voordat die het dossier controleert. Een analist zet gegenereerd onderzoek om in een beslissing. Compact proza kan onzekerheid verbergen en toezicht duurder maken, ook wanneer elke zin technisch geldig blijft.

De metingen suggereren ook praktische tests. Modelontwikkelaars kunnen naast taakbenchmarks afhankelijkheidslengte, zeldzame reeksen en gecomprimeerde constructies volgen. Training kan geslaagde communicatie belonen, in plaats van aan te nemen dat menselijke voorkeur overeind blijft bij optimalisatie voor andere doelen. De verbetering van de ene Opus-generatie naar de volgende toont dat het taalprofiel niet vastligt.

De fictieve redacteur keert terug naar de zin en voegt één verbindingswoord toe. Dan maakt ze van de naamwoordstapeling een bijzin en geeft ze de handeling aan een persoon. De feiten zijn niet veranderd en de passage is zes tokens langer geworden. Wat veranderde is waar de last ligt: de machine bespaarde minder ruimte en de lezer hoefde minder te dragen.

## Referenties


- Clark, T. H., Martin, M. B., & Mahowald, K. (2026). *Why is AI-generated language so hard to understand?* https://arxiv.org/abs/2610.29162
- Futrell, R., Mahowald, K., & Gibson, E. (2015). *Large-scale evidence of dependency length minimization in 37 languages*. https://doi.org/10.1073/pnas.1502134112
- Gibson, E., Futrell, R., Piantadosi, S. T., Dautriche, I., Mahowald, K., Bergen, L., & Levy, R. (2019). *How efficiency shapes human language*. https://doi.org/10.1016/j.tics.2019.02.003
- Levy, R., & Jaeger, T. F. (2007). *Speakers optimize information density through syntactic reduction*. https://proceedings.neurips.cc/paper/2006/hash/c6a01432c8138d46ba39957a8250e027-Abstract.html
- Martínez, E., Mollica, F., & Gibson, E. (2022). *Poor writing, not specialized concepts, drives processing difficulty in legal language*. https://doi.org/10.1016/j.cognition.2022.105070
- Smith, N. J., & Levy, R. (2013). *The effect of word predictability on reading time is logarithmic*. https://doi.org/10.1016/j.cognition.2013.02.013
