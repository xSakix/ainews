+++
title = "Waarom AI-proza grammaticaal klopt maar moeilijk leest"
slug = "waarom-ai-proza-grammaticaal-klopt-maar-moeilijk-leest"
description = "Een nieuw onderzoek laat zien dat negen toonaangevende modellen steeds taalvormen kiezen die meer leesinspanning vragen. Een experiment met finetuning wijst op een conflict tussen compacte modelredeneringen en taal die mensen gemakkelijk begrijpen."
tags = ["research", "models"]
date = 2026-10-25T04:14:11+01:00
draft = false
+++

Een redacteur bereikt de vierde regel van een gegenereerde briefing en leest die twee keer. Elk woord past en de zin is grammaticaal correct. Toch staan er meerdere zelfstandige naamwoorden achter elkaar zonder woorden die hun onderlinge verband uitleggen. Een levenloos onderwerp is gekoppeld aan een werkwoord dat normaal een menselijke handeling beschrijft, en een zelfstandig naamwoord wordt als werkwoord gebruikt. De redacteur in deze scène is fictief. De moeilijkheid die zij tegenkomt, is het onderwerp van een echt experiment.

## Waarom een vloeiende zin moeilijk leesbaar kan zijn

Thomas Hikaru Clark, Matias B. Martin en Kyle Mahowald wilden een probleem meten dat lezers vaak als een kwestie van smaak beschrijven: recente AI-teksten kunnen moeilijk te begrijpen zijn zonder duidelijke fouten te bevatten. Hun preprint vergelijkt teksten van negen modellen aan of dicht bij de technologische top met menselijke teksten. Ze vergelijken de modeltekst ook met nauw verwante parafrases die ontstaan door vertaling naar het Japans en terug naar het Engels.

De modellen kozen herhaaldelijk vormen die psycholinguïsten verbinden met meer leesinspanning. Alle negen gebruikten meer ongebruikelijke woordreeksen en meer levenloze onderwerpen met werkwoorden die normaal handelingen van levende wezens beschrijven. De meeste plaatsten grammaticaal verbonden woorden ook verder uit elkaar, gebruikten meer reeksen zelfstandige naamwoorden om andere zelfstandige naamwoorden te bepalen en lieten vaker optionele verbindingswoorden weg uit betrekkelijke bijzinnen met een objectfunctie. Het patroon was het sterkst in gesprekken en uitwisselingen over code en verschilde tussen modelfamilies.

Dit zijn geen grammaticale fouten. Het Engels laat een uitdrukking als “reader-patience budget” toe, en een lezer kan achterhalen wat het betekent wanneer een levenloos onderwerp iets abstracts “opeet”. Maar zulke constructies begrijpen kost moeite. Onbekende woordcombinaties zijn moeilijker te voorspellen. Wanneer verbonden woorden ver uit elkaar staan, moeten lezers een deel van de zin onthouden terwijl ze op het andere wachten. Wanneer meerdere zelfstandige naamwoorden bij elkaar staan, moeten lezers verbanden afleiden die de schrijver niet heeft benoemd.

Dit onderscheid is belangrijk omdat vloeiendheid alleen weinig over leesbaarheid zegt. Een model kan de Engelse syntaxis volgen en tegelijk constructies kiezen die menselijke sprekers doorgaans vermijden. Zijn proza kan grammaticaal correct zijn en toch meer leesinspanning vragen dan het idee zelf vereist.

## Menselijke taal weerspiegelt de behoeften van lezers

Het artikel bouwt op tientallen jaren onderzoek naar hoe taal zich aan menselijke beperkingen aanpast. Edward Gibson en collega’s beschrijven menselijke talen als compromissen tussen de inspanning van spreken en die van begrijpen. Richard Futrell, Mahowald en Gibson bestudeerden 37 talen en vonden uitgebreid bewijs dat grammaticaal verbonden woorden meestal dicht bij elkaar blijven. Door die woorden dicht bij elkaar te houden, wordt het geheugen minder belast.

Voorspelbaarheid beïnvloedt ook hoe mensen spreken en lezen. Roger Levy en T. Florian Jaeger stelden dat sprekers de informatiedichtheid regelen door optionele woorden te behouden of weg te laten, afhankelijk van wat volgt. Een spreker neemt vaker “that” op wanneer het helpt om een luisteraar op minder voorspelbare informatie voor te bereiden. Nathaniel Smith en Levy vonden later dat de leestijd ongeveer stijgt met de surprisal van een woord, een maat voor hoe onverwacht het is: minder voorspelbare woorden vragen meetbaar meer leestijd.

Volgens deze verklaring heeft redundantie een functie in communicatie. Een vertrouwde uitdrukking, een optioneel verbindingswoord of een herhaalde aanwijzing kan lezers tijd geven om te begrijpen wat ze lezen. Eric Martínez en collega’s toonden dit effect aan in juridische taal. Zij vonden dat de moeilijkheid van contracten voor een belangrijk deel voortkwam uit schrijfkeuzes, waaronder bijzinnen binnen andere bijzinnen en onnodig jargon. Gespecialiseerde begrippen alleen verklaarden die moeilijkheid niet.

Clark, Martin en Mahowald vragen wat er gebeurt wanneer een systeem dat taal produceert deze menselijke beperkingen niet heeft. Moderne modellen worden getraind op menselijke tekst, maar training na die eerste fase beloont steeds vaker correcte antwoorden op wiskunde-, programmeer- en redeneertaken. Aan het einde van een taak kan een antwoord op juistheid worden gecontroleerd, ook als de uitleg die ernaartoe leidt voor een mens moeilijk te lezen is.

## Vergelijken hoe dezelfde betekenis anders wordt uitgedrukt

De onderzoekers verzamelden modeluitvoer in drie situaties: chat, programmeren en essays. Ze gebruikten menselijke teksten uit OpenSubtitles als referentie voor gesprekken, Stack Exchange voor technische teksten en het PERSUADE 2.0-corpus voor studentenessays. Ze identificeerden moeilijke constructies door grammaticale relaties tussen woorden te analyseren, een methode die dependency parsing heet. Ze voegden geautomatiseerde classificatie toe wanneer die analyse alleen niet kon bepalen of een onderwerp levend was of een zelfstandig naamwoord in een werkwoord was veranderd.

Bij een vergelijking tussen modeltekst en menselijke teksten blijft een mogelijk bezwaar bestaan: de twee verzamelingen kunnen over andere onderwerpen gaan. Een technisch antwoord gebruikt vanzelf andere taal dan een filmondertitel. Daarom maakte het team van elke modelzin een andere versie. Een vertaalmodel met 3,3 miljard parameters vertaalde de zin naar het Japans en terug naar het Engels. Zo bleef de globale betekenis behouden, maar veranderde de formulering.

De oorspronkelijke antwoorden van de meeste topmodellen bevatten meer zeldzame woordparen, of bigrammen, dan de vertaalde parafrases. Ook was hun n-gramperplexiteit hoger, een maat voor hoe onvoorspelbaar hun woordreeksen waren. Vergelijkbare verschillen verschenen in hun gebruik van levenloze onderwerpen, werkwoorden afgeleid van zelfstandige naamwoorden en betrekkelijke bijzinnen met een objectfunctie waaruit verbindingswoorden waren weggelaten. De Llama-modellen en het basismodel OLMo veranderden minder. OLMo Think, een redeneervariant, leek meer op de topsystemen. Claude Opus 5.5 scoorde in 19 van de 21 vergelijkingen lager dan Opus 5. Dat laat zien dat deze neigingen ook kunnen afnemen als modellen veranderen.

Vertalen naar een andere taal en terug is een controle, geen volmaakte vervanging voor een menselijke herschrijving. Vertaalsystemen hebben hun eigen voorkeuren. De onderzoekers kozen juist Japans omdat vertaling via een niet-verwante taal doorgaans gevarieerdere parafrases oplevert. Toch houdt deze vergelijking de betekenis constanter dan een vergelijking tussen niet-verwante documenten van mensen en modellen. Dat suggereert dat de moeilijke vormen deels voortkomen uit de manier waarop het model een idee uitdrukt, niet alleen uit het onderwerp.

## Een straf voor lengte veranderde de grammatica van het model

Het tweede experiment testte een mogelijk mechanisme. De onderzoekers pasten finetuning toe op Qwen2.5-1.5B-Instruct om gestructureerde gebeurtenisgegevens in zinnen om te zetten. Zowel een kortere als een langere constructie kon het juiste antwoord uitdrukken. Reinforcement learning beloonde juistheid, terwijl een instelbare straf langere uitvoer ontmoedigde. Sommige trainingsruns bevatten ook een beperking die het model ervan weerhield te ver af te wijken van zijn oorspronkelijke tokenverdeling.

In de runs zonder die beperking leidde elke positieve straf voor lengte tot een categorische voorkeur voor de kortere vorm. Meer dan 98 procent van de antwoorden gebruikte het korte alternatief bij de constructies waarop het model was getraind. De voorkeur verscheen ook bij ongeziene voorbeelden van vergelijkbare constructies. Zonder de beperking die het aan het basismodel bond, breidde het model deze voorkeur uit naar één van vier verder verwante grammaticale alternatieven.

Het model kreeg nooit de opdracht om optionele woorden weg te laten. Tijdens de training leerde het dat dit tokens bespaarde zonder afbreuk te doen aan de juistheid van de taak. Menselijke sprekers laten die keuzes afhangen van de context. Het model leerde daarentegen een algemene voorkeur voor compacte formuleringen. Dit kleine experiment laat zien hoe een doelstelling die efficiëntie beloont, taal kan opleveren die afwijkt van menselijk gebruik.

Het experiment bewijst niet dat commerciële labs dezelfde lengtestraf toepassen, of dat één beloning elk patroon in gesloten modellen verklaart. De auteurs bestudeerden het Engels, een beperkte verzameling prompts en een deel van de beschikbare systemen. Ze konden niet rechtstreeks zien hoe topmodellen na hun eerste training verder werden getraind en beschrijven hun ingreep als een proof of concept. Hun causale claim is beperkt: bij een gecontroleerde beloning voor beknoptheid veranderden grammaticale voorkeuren in de voorspelde richting.

## Leesbaarheid wordt een eis aan modellen

Het onderzoek behandelt leesbaarheid als een alignmentprobleem: modellen moeten taal produceren die aan menselijke behoeften voldoet, en onderzoekers kunnen aspecten van die taal meten. Een bruikbaar antwoord moet tot een correcte conclusie komen, maar mensen moeten vaak ook kunnen nagaan hoe die is bereikt. Een ontwikkelaar beoordeelt de uitleg van een agent bij een patch. Een arts leest een samenvatting voordat hij het dossier controleert. Een analist gebruikt gegenereerd onderzoek voor een beslissing. Dicht proza kan onzekerheid verhullen en toezicht moeilijker maken, ook wanneer elke zin technisch geldig blijft.

De metingen suggereren praktische tests. Naast benchmarks voor taakprestaties kunnen modelontwikkelaars de afstand tussen verbonden woorden, ongebruikelijke woordreeksen en compacte constructies volgen. Ze kunnen succesvolle communicatie tijdens de training belonen, in plaats van aan te nemen dat optimalisatie voor andere doelen menselijke voorkeuren behoudt. De verbetering tussen twee Opus-generaties laat zien dat deze taalkundige neigingen kunnen veranderen.

De fictieve redacteur keert terug naar de zin en voegt één verbindingswoord toe. Vervolgens werkt ze de reeks zelfstandige naamwoorden uit tot een bijzin en maakt ze een persoon tot onderwerp van de handeling. De feiten zijn niet veranderd en de passage is zes tokens langer geworden. Het model gebruikt iets meer ruimte, maar de lezer hoeft minder moeite te doen om het te begrijpen.

## Referenties


- Clark, T. H., Martin, M. B., & Mahowald, K. (2026). *Why is AI-generated language so hard to understand?* https://arxiv.org/abs/2610.29162
- Futrell, R., Mahowald, K., & Gibson, E. (2015). *Large-scale evidence of dependency length minimization in 37 languages*. https://doi.org/10.1073/pnas.1502134112
- Gibson, E., Futrell, R., Piantadosi, S. T., Dautriche, I., Mahowald, K., Bergen, L., & Levy, R. (2019). *How efficiency shapes human language*. https://doi.org/10.1016/j.tics.2019.02.003
- Levy, R., & Jaeger, T. F. (2007). *Speakers optimize information density through syntactic reduction*. https://proceedings.neurips.cc/paper/2006/hash/c6a01432c8138d46ba39957a8250e027-Abstract.html
- Martínez, E., Mollica, F., & Gibson, E. (2022). *Poor writing, not specialized concepts, drives processing difficulty in legal language*. https://doi.org/10.1016/j.cognition.2022.105070
- Smith, N. J., & Levy, R. (2013). *The effect of word predictability on reading time is logarithmic*. https://doi.org/10.1016/j.cognition.2013.02.013
