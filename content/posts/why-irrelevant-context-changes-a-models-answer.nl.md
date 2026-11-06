+++
title = "Waarom irrelevante context het antwoord van een model verandert"
slug = "waarom-irrelevante-context-modelantwoord-verandert"
description = "Een nieuwe mechanistische studie volgt irrelevante prompttekst door een taalmodel. Ze vindt een aparte route die een antwoord kan verstoren, ook als de extra tekst geen concurrerend bewijsmateriaal levert."
tags = ["research", "agents"]
date = 2026-11-06T04:12:00+01:00
draft = false
+++

Stel dat een analist een model vraagt naar de hoofdstad van een land, nadat een zoeksysteem een alinea over een andere plaats heeft ingevoegd. Die alinea noemt geen concurrerende hoofdstad en spreekt de vraag niet tegen. Ze heeft er eenvoudigweg niets mee te maken. Toch wordt de kans kleiner dat het model het antwoord geeft dat het al kende.

Dit is een illustratie, maar iedereen die een zoeksysteem of een agent met een lange context heeft gebouwd, kent het probleem. Meer context kan een antwoord verslechteren. Een nieuwe preprint van Dikshant Kukreja, Gautam Gupta, Avni Mittal en hun collega's probeert te verklaren waarom dat in de interne berekeningen gebeurt. Hun antwoord is een “intrusieroute”: irrelevante tekst wordt verrijkt, vooruit gekopieerd en vervolgens versterkt door een kleine groep aandachtshoofden.

Dat onderscheid is relevant omdat de meeste verdedigingen tegen afleidende context zoeken naar betere informatie, sterkere instructies of grotere contextvensters. Het artikel stelt een andere vraag. Als irrelevante tekst eenmaal in de prompt staat, welke onderdelen van het model laten die tekst dan het antwoord beïnvloeden?

## Een afleider zonder onjuist antwoord

De onderzoekers beginnen met feitelijke relaties die modellen met open gewichten kennen, bijvoorbeeld een persoon met een bijbehorend kenmerk. Ze maken schone prompts en verschillende soorten extra context: relevant bewijsmateriaal, onjuist bewijsmateriaal, korte irrelevante tekst, lange irrelevante tekst en willekeurige tekst. Hun standaarddataset bevat 250 feiten die ten minste drie van de vier basismodellen juist beantwoorden.

Zo kunnen ze tegenspraak en intrusie afzonderlijk onderzoeken. Een onjuiste passage kan een model naar een bepaald fout antwoord sturen. Irrelevante tekst hoeft dat niet te doen. Alleen al doordat ze op de verkeerde plekken aan de berekening deelneemt, kan de kans op het juiste antwoord dalen.

De experimenten gebruiken Llama 3.1 8B, Mistral 7B, Qwen 2.5 7B, Pythia 6.9B en GPT-2 XL, met extra grotere modellen voor één wiskundetest. Geen enkel model wordt getraind. De openbare repository bevat scripts die de datasets opbouwen, de betrokken hoofden selecteren en de ingrepen reproduceren.

Het eerste belangrijke resultaat laat zien waar de schade ontstaat. Feedforwardlagen verrijken representaties van zowel het onderwerp van de vraag als tokens uit de irrelevante passage. Sommige aandachtshoofden kopiëren vervolgens materiaal uit het voorste deel naar de laatste positie, waar het model het antwoord moet voorspellen. De auteurs noemen die herhalende hoofden. Een tweede, kleine groep zet dat aangevoerde materiaal om in druk op de uitvoerverdeling.

## Retrieval en intrusie gebruiken verschillende circuits

De auteurs onderscheiden retrievalhoofden, die relevant bewijsmateriaal doorgeven, van intrusiehoofden, die het ongewenste effect overbrengen. Die groepen overlappen grotendeels niet. Daardoor is het resultaat bruikbaarder dan de algemene stelling dat aandacht ruis bevat. Een systeem kan het mechanisme nodig hebben dat bewijsmateriaal doorgeeft en tegelijk profiteren van het onderdrukken van de aparte route die afleiders versterkt.

Het artikel test oorzakelijke verbanden en kijkt niet alleen naar correlaties tussen aandachtspatronen en fouten. Wanneer de onderzoekers de laatste residuele toestand uit een afgeleide uitvoering vervangen door de overeenkomstige toestand uit een schone uitvoering, herstellen ze 97,6 procent van de daling in nauwkeurigheid. Dit is een orakelingreep: er is een tweede, schone verwerking nodig, waardoor het geen praktische verdediging in productie is. Wel toont het aan dat de relevante schade de toestand van het laatste token heeft bereikt.

Ook maskeren ze geselecteerde intrusiehoofden. Die ingreep is in beginsel inzetbaar omdat er geen schone referentie-uitvoering voor nodig is. De auteurs testen haar op apart gehouden relaties en verschillende vervolgtaken, waaronder HotpotQA, PubMedQA en rekenkundige datasets met afleidende uitspraken. Ze onderzoeken ook of groepen hoofden overdraagbaar zijn tussen modellen en tussen basisversies en versies die op instructies zijn afgestemd.

De verdediging heeft een prijs. Aandachtshoofden verwijderen kan ook nuttige berekeningen wegnemen. Het maakt uit hoeveel hoofden worden onderdrukt. De repository bevat daarom proeven met verschillende aantallen hoofden en selectiedrempels, naast stabiliteitstests op apart gehouden gegevens. Dit is geen universele schakelaar die context veilig maakt. Het is een manier om een beperktere afweging te onderzoeken.

## Wat dit verandert aan contextengineering

Retrieval-augmented generation behandelt relevantie vaak als een zoekprobleem. Een retriever rangschikt passages, een promptbouwer kiest hoeveel er worden opgenomen en het model wordt geacht de rest te negeren. Het nieuwe onderzoek laat zien waarom die laatste aanname kan mislukken. Tekst kan een antwoord beïnvloeden zonder bewijsmateriaal te leveren en zonder rechtstreeks met de waarheid te concurreren.

Daarom is “het antwoord stond ergens in de context” een onvolledige diagnose. Een lange prompt kan het juiste document bevatten en toch de nauwkeurigheid verlagen, doordat ongerelateerde passages een aparte route activeren. De vervolgtests van de auteurs verbinden hun circuitanalyse met taken waarin modellen vragen moeten beantwoorden of moeten redeneren tussen toegevoegde uitspraken.

Het onderzoek begrenst ook een gebruikelijke reactie op contextproblemen: het model vertellen dat het irrelevante informatie moet negeren. Instructies werken via hetzelfde model dat de afleider al verwerkt. Een mechanistische ingreep kan testen of de schadelijke route actief blijft, zelfs wanneer het model de instructie lijkt te volgen.

Er zijn belangrijke beperkingen. Het gaat om modellen met open gewichten waarvan de interne activaties kunnen worden bekeken en aangepast. Het duidelijkste circuitonderzoek richt zich op modellen die veel kleiner zijn dan de grootste geavanceerde systemen van vandaag. De feitelijke datasets zijn gecontroleerd en het herstel met de orakelmethode kan niet in de beschreven vorm worden ingezet. Het artikel is een preprint en heeft nog geen peerreview ondergaan.

Het bewijsmateriaal is wel uitzonderlijk goed te onderzoeken. De repository noemt de modellen, datasets, scripts, procedure voor hoofdselectie en reeksen ingrepen. Andere onderzoekers kunnen nagaan of dezelfde scheiding tussen retrieval en intrusie voorkomt in andere architecturen, grotere modellen en echte productietraces.

Een denkbeeldig ontwikkelteam kan een onjuist antwoord nu in twee stappen onderzoeken. Eerst vraagt het of de zoekstap het benodigde bewijsmateriaal heeft aangeleverd. Daarna vraagt het of irrelevante passages de interne route naar het antwoord veranderden. Die tweede vraag vervangt beter zoeken niet. Ze verklaart waarom betere zoekresultaten en minder, schonere passages kunnen helpen, zelfs als het model ruis lijkt te kunnen negeren.

De bredere les is eenvoudig: context is geen passieve opslag. Elke extra passage wordt onderdeel van een berekening. Kukreja en collega's hebben een route in kaart gebracht waarlangs een verkeerde passage invloed kan hebben zonder ooit een onjuist antwoord te formuleren.

## Referenties

- Dikshant Kukreja, Gautam Gupta, Avni Mittal et al., “The Intrusion Pathway: How Non-Evidential Context Degrades Language Model Performance” — https://arxiv.org/abs/2611.07778
- Dikshant Kukreja et al., code and reproduction guide for “The Intrusion Pathway” — https://github.com/dk4248/the-intrusion-pathway
- TransformerLens contributors, “TransformerLens” — https://github.com/TransformerLensOrg/TransformerLens
- Javier Hernandez et al., relations dataset used for factual-recall experiments — https://github.com/evandez/relations
- Freda Shi et al., “GSM-IC: A Benchmark for Understanding the Effects of Irrelevant Context in Mathematical Reasoning” dataset — https://github.com/google-research-datasets/GSM-IC
