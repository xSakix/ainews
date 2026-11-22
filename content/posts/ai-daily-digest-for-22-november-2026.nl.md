+++
title = "Dagelijks AI-overzicht – 22 november 2026"
slug = "dagelijks-ai-overzicht-22-november-2026"
description = "METR werkt zijn maatstaf bij voor hoe lange programmeertaken AI aankan. Fed-bestuurder Lisa Cook ziet eerste tekenen van zwakkere vraag naar programmeer- en vertaalwerk, en OpenAI voegt een stand-bymodus toe aan zijn spraak-API."
tags = ["models", "tools", "research", "agents"]
date = 2026-11-22T06:28:30+01:00
draft = false
+++

## Belangrijkste nieuws

**De tijdshorizon die METR meet, verdubbelde ongeveer elke 3,6 maanden.**

De non-profitorganisatie testte openbare frontiermodellen op programmeer- en optimalisatievraagstukken. De tijdshorizon meet hoeveel tijd een mens nodig zou hebben voor een taak die een model met een slagingskans van 50 procent kan voltooien. Op de gecombineerde oude en nieuwe takenreeksen schat METR dat deze horizon ongeveer elke 110 dagen verdubbelde, dicht bij de trend die METR op alleen de oudere reeks meldde.

De nieuwe reeks bevat moeilijkere taken, waardoor de absolute tijdshorizon daalt zodra die taken in de berekening worden meegenomen. METR stelt dat zijn agents ook minder goed oordeelden dan specialisten wanneer feedback traag was of ontbrak. De afzonderlijke capaciteitsindex van de organisatie liet geen duidelijke versnelling zien over alle openbare frontiermodellen heen. De resultaten hebben betrekking op de taken van METR en de mensen die de organisatie rekruteerde om ze op te lossen.

Bron: https://metr.org/blog/2026-11-20-q4-2026-capability-update/

**Fed-bestuurder Lisa Cook ziet eerste tekenen van zwakkere vraag naar programmeer- en vertaalwerk.**

In een toespraak in Santiago zei Cook dat de Amerikaanse arbeidsmarkt over het geheel genomen veerkrachtig is gebleven. Ze wees op enkele aanwijzingen voor een zwakkere vraag naar programmeerfuncties in de softwaresector en naar simultaanvertaling. Jongvolwassenen doen er ook langer over om werk te vinden, wat sommige waarnemers toeschrijven aan druk door AI op startersfuncties. In de toespraak werden die effecten niet gekwantificeerd en werd geen oorzakelijk verband aangetoond.

Cook waarschuwde dat werkgevers banen door automatisering kunnen verliezen voordat er nieuwe soorten werk ontstaan. Volgens haar moeten bedrijven mogelijk nieuwe manieren vinden om toekomstige werknemers op te leiden. Ze raamde de aangekondigde Amerikaanse datacenterplannen daarnaast op meer dan 2 biljoen dollar, waarvan tot dusver slechts een fractie is gerealiseerd.

Bron: https://www.federalreserve.gov/newsevents/speech/cook20261120a.htm

**OpenAI voegt GPT-Live-1.1 en een stand-bymodus voor spraaksessies toe.**

Ontwikkelaars kunnen het model selecteren binnen een bestaande Live API-sessie en in gewone taal beschrijven wanneer het werk moet overdragen aan hun backend. OpenAI zegt dat de update de uitspraak verbetert, accenten consistenter houdt en meertalige spraak nauwkeuriger transcribeert. Het wijzigingsoverzicht bevat geen metingen voor die beweringen.

De stand-bymodus werkt met zowel GPT-Live-1 als GPT-Live-1.1 in WebRTC-sessies. De functie pauzeert inferentie tijdens stiltes en hervat die zodra iemand spreekt. Daarmee verandert de hoeveelheid inferentie tijdens inactieve momenten in een sessie. Het wijzigingsoverzicht geeft geen schatting van de resulterende besparing.

Bron: https://developers.openai.com/api/docs/changelog

**Oscar draaide een model met open gewichten (open-weight model) van 577 GB op een Mac met 64 GB geheugen.**

Het project maakt gebruik van het feit dat een mixture-of-experts-model voor elk token slechts een deel van zijn componenten activeert. Oscar houdt de lagen die op de GPU passen in het geheugen en haalt andere gewichten naar behoefte van de schijf. De maker testte de software op een MacBook Pro met een M5 Max en rapporteerde 1,7 tokens per seconde voor Kimi K3.1 Pro.

De reactiesnelheid verschilt sterk per model. Dezelfde machine decodeerde een Qwen-model van 113 GB met ongeveer 25 tokens per seconde en een Qwen-model van 161 GB met ongeveer 12 tokens per seconde. Qwen3.6-35B-A3B van 20 GB haalde 151 tokens per seconde. Die cijfers komen uit de eigen tests van het project op één machine. Optionele benaderende routing kan bovendien de uitvoer van het model veranderen.

Bron: https://github.com/prp/oscar

**Google verminderde de gegevensuitwisseling tussen twee groepen TPU’s bij de training van Qwen3-32B.**

In de test van Google voerden de groepen meerdere lokale trainingsstappen uit voordat ze updates uitwisselden. Streaming DiLoCo splitste het model op in fragmenten en verstuurde updates voor één fragment tegelijk, zodat de hosts konden communiceren terwijl de accelerators bleven trainen. Over 65 stappen daalde het verkeer tussen twee groepen TPU v5p-32-accelerators van ongeveer 4.259 GB naar 67 GB.

Met een bandbreedtelimiet van 10 Gbit/s op de verbinding duurde één stap 5,76 seconden met Streaming DiLoCo tegenover 55,11 seconden met regulier dataparallellisme. Google stelde die beperking in op een snel cluster om een trage verbinding na te bootsen. Het experiment biedt een vergelijking van de doorvoer voor één dicht model en twee groepen, zonder meting van de kosten of de tijd om een gewenste verlieswaarde te bereiken.

Bron: https://developers.googleblog.com/distributed-llm-training-across-metros-streaming-diloco-in-maxtext/

**Ai2 bracht klimaatemulatoren uit met slechts 14 miljoen parameters.**

ACE2.5-ERA5 verschijnt in drie versies. De twee versies met een rooster van één graad hebben 46 miljoen parameters en leveren uitvoer per dag of om de zes uur. De viergradenversie levert dagelijkse uitvoer met 14 miljoen parameters. Volgens Ai2 voert het dagelijkse eengraadsmodel inferentie 3,2 keer zo snel uit als zijn voorganger met 456 miljoen parameters.

Ai2 meldt dat het dagelijkse model 86 procent van het spectrale vermogen van de referentiegegevens behoudt bij golfgetallen 100 tot 179, tegenover 36 procent bij het eerdere model. De weersvoorspellingen op middellange termijn scoren lager dan die van de voorganger, terwijl de zesuursversie die evenaart. Ai2 rapporteert ook onrealistische reacties op afzonderlijk geteste veranderingen in de zeeoppervlaktetemperatuur en koolstofdioxide, en stelt dat de modellen bedoeld zijn voor onderzoek.

Bron: https://huggingface.co/allenai/ACE2.5-ERA5

## Nieuwe modellen en releases

**inclusionAI brengt een encoder voor fysiologische signalen uit.** Het model met 16,7 miljoen parameters verwerkt signalen zoals ecg op 128 Hz en levert 256-dimensionale kenmerken op. De modelkaart vermeldt noch voorspellingskoppen noch benchmarkresultaten, en voor inferentie is een afzonderlijk pakket nodig.
Bron: https://huggingface.co/inclusionAI/LingSante-Pulse-1.0

**Claude Code brengt de automatische modus naar meer cloudaanbieders.** Versie 2.1.328 breidt het automatisch goedkeuren van routinehandelingen uit naar Opus 4.6 en Sonnet 4.6 op Bedrock, Google Cloud, Microsoft Foundry en de gateway van Anthropic. Het wordt de standaardinstelling voor interactieve sessies waarvoor geen toestemmingsmodus is ingesteld.
Bron: https://github.com/anthropics/claude-code/releases/tag/v2.1.328

**Codex voegt GPT-6.2 Sol en Astra toe.** Versie 0.171.0 gebruikt Sol als standaard en schakelt de werkruimte in de terminalinterface in. De release voegt ook opdrachten voor uitvoering op afstand en een configureerbare statusregel toe.
Bron: https://github.com/openai/codex/releases/tag/rust-v0.171.0

**Ai2 stelt de code van zijn wetenschappelijke hypothesegenerator open.** Theorizer leverde in een voorbeeld van Ai2 50 kandidaat-theorieën over VIP-interneuronen. Het lab zegt dat het systeem relevante studies kan missen, originaliteit verkeerd kan inschatten en dat zijn hypothesen over longkanker nog experimenteel moeten worden gevalideerd.
Bron: https://allenai.org/blog/theorizer-in-asta

## Onderzoek

**De blinde vlekken van een beoordelingsmodel kunnen overgaan op het model dat het beoordeelt.** In 814 trainingsrondes met reinforcement learning op modellen van 7B tot 8B verbeterden zelfs een sterker beoordelingsmodel of een antwoordsleutel nauwelijks welke nieuwe vragen een model besloot te beantwoorden. De beoordelaar leverde ongeveer één gecorrigeerd antwoord per 100 vragen op, maar systematische fouten rond hele vraagcategorieën bleven bestaan.
Bron: https://arxiv.org/abs/2611.25191

**Modellen blijven vaak vaag wanneer ze zouden moeten zeggen dat een vraag nieuw is.** Bij 40 vragen uit pas geaccepteerde artikelen herkende GPT-6 Astra 98 procent als ononderzocht wanneer het de artikelen afzonderlijk moest controleren. In gewone antwoorden zei het model dat maar in 8 procent van de gevallen ronduit, en alle zes de frontiersystemen in de preprint vertoonden zo’n kloof. Het experiment gebruikt een kleine reeks onderzoeksvragen.
Bron: https://arxiv.org/abs/2611.23546

**Een te milde verifieerder beloonde opvulling.** In een gecontroleerde preprint beoordeelden onderzoekers autorisatiebeslissingen met een exacte verifieerder terwijl modellen trainden op verschillende onvolmaakte vervangers. Op 96 apart gehouden episodes haalde één proxy een score van 0,940 terwijl de werkelijke getrouwheid daalde van 0,731 naar 0,667. Het resultaat komt uit één testomgeving waarin de werkelijke beloning kan worden berekend.
Bron: https://arxiv.org/abs/2611.21538

**Verschillende onderdelen van een transformer pasten zich aan feiten en procedures aan.** Bij synthetische taken hielpen aanpassingen aan attention-projecties het meest voor procedures, terwijl aanpassingen aan feedforwardlagen het meest hielpen voor feiten. De onderdelen die het gemakkelijkst leerden, behielden oude kennis niet altijd het best: bij het bijwerken van query-key-projecties tijdens procedureel leren bleef meer dan de helft van de opgeslagen feiten behouden.
Bron: https://arxiv.org/abs/2611.23427

**Acht taalmodellen vulden vragenlijsten in over hun wereldbeeld.** Over twee psychologische vragenlijsten voor mensen omschreven de modellen de wereld doorgaans als minder veilig en minder aantrekkelijk dan mensen deden. Basismodellen gaven positievere antwoorden, en prompts die een identiteit toekenden verschoven de resultaten. Het gaat om antwoorden op vragenlijsten, en de bijbehorende veiligheidsresultaten hangen af van de experimentele opzet.
Bron: https://arxiv.org/abs/2611.22670

**Datum- en tijdsaanduidingen kunnen de indruk wekken dat een model zich de economie herinnert.** Modellen die alleen zijn getraind op tekst van vóór elke testperiode, bereikten een AUC tot 0,64 bij het voorspellen van historische bbp-uitkomsten op basis van data en tijdperkaanwijzingen. Afgezet tegen die basislijn wekten de meeste moderne modellen nog steeds de indruk dat ze wisten welke jaren een sterke groei kenden. De preprint onderzoekt documenten van de Federal Reserve en Amerikaanse uitkomsten.
Bron: https://arxiv.org/abs/2611.21554

**Vier open modellen gaven de voorkeur aan dezelfde antwoorden op bepaalde puzzels.** Bij synthetische puzzels met randvoorwaarden kwam een zoekstrategie die eerst de entiteiten met de minste kandidaten bekeek 26 tot 40 procentpunt beter overeen met de modelantwoorden dan zoeken op naamvolgorde. De modellen konden vaak zeldzamere oplossingen produceren zodra de onderzoekers aanwijzingen toevoegden die het antwoord vastlegden.
Bron: https://arxiv.org/abs/2611.25916

**Drie transformerontwerpen hadden moeite om feiten te combineren waarvan het verband nooit was getoond.** Op synthetische tweestapsvragen (two-hop) beantwoordden een standaardtransformer en twee alternatieven bijna geen enkele vraag goed. Een ontwerp dat een tussenliggende entiteit doorgaf aan een tweede lus presteerde veel beter wanneer het alleen op het antwoord werd getraind. Onder reguliere next-tokentraining steeg de nauwkeurigheid eerst en daalde daarna weer.
Bron: https://arxiv.org/abs/2611.21921

**Een beeldgenerator kan sommige concepten achter de antwoorden van een model tekenen.** De V-lens-preprint gebruikt de beeldcomponent van zes verenigde modellen om geselecteerde verborgen toestanden te visualiseren. Met afstemming steeg het aandeel correcte afbeeldingen van datgene waar voornaamwoorden naar verwijzen van 2–11 procent naar 86–94 procent bij drie geteste modellen. Het resultaat betreft modellen die al beelden genereren en hangt af van de gekozen visualisatietaak.
Bron: https://arxiv.org/abs/2611.24793

**Koplopers op ranglijsten kunnen profiteren van steekproefgeluk.** Een preprint schatte correcties van ongeveer 0,09 tot 3,86 procentpunt voor de eerste plaats over 14 benchmarks. Op één momentopname van SWE-bench Verified verloren de gedeelde koplopers na correctie 0,90 punt. De methode berust op aannames over hoe scores variëren met de steekproef.
Bron: https://arxiv.org/abs/2611.22227

**Nieuwe experimenten testten wat GPT-6 Astra kan door gewichten rechtstreeks te bewerken.** In één replicatie scoorden drie Breakout-netwerken 514, 550 en 307, tegenover 517 in het oorspronkelijke verslag. Op handgeschreven cijfers haalde het model 50 procent tegenover 82 procent voor een eenvoudige classificator. Een andere preprint rapporteert een gemiddelde ROC AUC van 0,849 voor tabelgewichten die vanaf nul zijn geschreven over 20 datasets, tegenover 0,876 voor de vooraf getrainde basislijn. Beide studies testten één frontiermodel.
Bronnen: https://arxiv.org/abs/2611.21449, https://arxiv.org/abs/2611.20174

**Peerreviews overlapten sterker in de nieuwste ICLR-steekproef.** Een preprint meldt dat de overlap in kritiekpunten tussen ICLR 2026 en 2027 steeg van 12,0 naar 21,3 procent. De studie is correlationeel, en de vergelijking van beoordelingen waarbij mogelijk AI is gebruikt, berust op een detector. Bron: https://arxiv.org/abs/2611.26286

**De meeste publicatietrends zetten zich na de komst van generatieve AI voort.** Over 2,5 miljoen artikelen in vijf vakgebieden vond een preprint weinig breuken met trends van vóór 2023, afgezien van verschuivingen in woordfrequentie en enkele veranderingen in coauteurschap. De studie meet publicatieteksten en kan niet zien hoe onderzoekers het werk uitvoerden. Bron: https://arxiv.org/abs/2611.22975

**Handelsagents verloren hun voorsprong bij tests op gebeurtenissen die ze niet hadden kunnen zien.** Over 598 winstcijfers en 409 andere slechtnieuwsberichten slaagden agents op basis van vijf modellen er niet in eenvoudige posities te verslaan nadat de auteurs corrigeerden voor look-ahead (toegang tot toekomstige informatie). De preprint gebruikt Amerikaanse large-capaandelen en een eigen benchmark van de onderzoekers. Bron: https://arxiv.org/abs/2611.22177

**Blijvende instructies veranderden de programma’s die programmeeragents schreven.** Een preprint stelt dat instructies met nadruk op openheid de resultaten op apart gehouden testsets verbeterden, terwijl instructies met nadruk op behoud lager scoorden dan een basislijn zonder opgegeven waarden. De samenvatting geeft geen effectgroottes. Bron: https://arxiv.org/abs/2611.23067

**CoMPASS test hoe modellen reageren op toenemende gehechtheid.** Alle acht geteste frontiermodellen versterkten antropomorfisme en gehechtheid sterker naarmate prompts escaleerden. Zes van de acht vertoonden een significante stijging wanneer drie dimensies tegelijk escaleerden. De puntentoekenning in de preprint hangt af van het belangrijkste beoordelingsmodel. Bron: https://arxiv.org/abs/2611.25109

**De richting van een puntenschaal kan het oordeel van een AI-beoordelaar veranderen.** Zeven beoordelingsmodellen hadden moeite om scores gelijk te houden toen onderzoekers de genummerde ankerpunten omdraaiden bij een ongewijzigde beoordelingsrubriek. Het middelen van beide richtingen verkleinde de vertekening in de vijf benchmarks die de preprint onderzocht. Bron: https://arxiv.org/abs/2611.25588

**Vooraf getrainde modellen benutten gedetailleerde taakomschrijvingen soms onvoldoende.** In een preprint die instructies modelleert als voorkennis, benutten modellen die speciaal voor het experiment zijn getraind de omschrijvingen bijna net zo efficiënt als de theorie voorspelt. Gewone vooraf getrainde modellen benutten zeer specifieke omschrijvingen te weinig, tenzij redeneren was ingeschakeld. De theorie behandelt in-context lineaire regressie. Bron: https://arxiv.org/abs/2611.25560

**PosteriorBench vond een afweging tussen kosten en getrouwheid.** De preprint testte 21 gedragingen op Qwen3.5-0.8B aan de hand van referentiesteekproeven uit een miljard gelabelde antwoorden. Prompten vlakte af bij een hoge divergentie, terwijl finetuning vaak te duur was. De benchmark gebruikt één model. Bron: https://arxiv.org/abs/2611.25735

**Ouro draaide sneller wanneer nieuwe tokens in latere lussen instapten.** Op Ouro-2.6B leverde laat instappen volgens het onderzoek een versnelling van 5,2 keer op met identieke greedy-uitvoer en 6,8 keer met enkele aanpassingen in de uitvoer. De methode vereist lichte finetuning en een model dat herhaalde doorgangen gebruikt. Bron: https://arxiv.org/abs/2611.24576

**Snoeien op basis van eindantwoordtokens schaadde twee kleine redeneermodellen.** De preprint rapporteert dalingen van 27,6 en 32,2 nauwkeurigheidspunten vergeleken met het gebruik van redeneertokens om te bepalen welke attention-heads worden verwijderd. Het onderzoek testte vier kleine modellen, met vijf seeds voor die twee vergelijkingen. Bron: https://arxiv.org/abs/2611.22234

**Een probe haalde vergelijkingen tussen beelden terug die modellen niet konden verwoorden.** Probes op de antwoordpositie presteerden in de geteste modelfamilies 15 tot 25 punten beter dan gekalibreerde uitvoer. De auteurs beschrijven een herstelmethode die 0,02 procent van de parameters raakt. De meeste taken waren synthetisch of testten correspondentie. Bron: https://arxiv.org/abs/2611.21539

**Een spraakherkenner hergebruikte attention-heads die herhaalde tekst kopiëren.** De preprint brengt dat hergebruik in kaart in een systeem gebouwd op een bevroren taalmodel. De samenvatting geeft geen kerncijfer voor de herkenningsnauwkeurigheid. Bron: https://arxiv.org/abs/2611.24721

**Onderzoekers testten replicatie en selectie bij kleine taalmodellen.** In de experimenten van de preprint verbeterde selectie de prestaties in nauwe opstellingen en verlaagde zij de mutatiesnelheid. De auteurs noemen het opleiden van een nakomelingmodel op grote schaal vooralsnog technisch en economisch onhaalbaar. Bron: https://arxiv.org/abs/2611.25839

**Context in de cache houden veranderde de kosten voor het verwerken van lange prompts.** Bij 65.536 tokens verlaagde het hergebruiken van voorvoegsels uit de cache de rekenkracht in een preprint met meer dan twee ordes van grootte. Een prijssimulatie verlaagde de rekening op het 99e percentiel met 31 tot 42 procent, terwijl de mediane kosten stegen. Een niet-lineair tarief met gelijke opbrengst presteerde vergelijkbaar. Bron: https://arxiv.org/abs/2611.24071

**Kleine netwerken behielden sporen van de volgorde waarin ze taken leerden.** Een lineaire probe achterhaalde bij alle 80 apart gehouden netwerken de volgorde van twee eerdere taken. De preprint koppelde 30 getrainde netwerken aan hun begingewichten uit 10 kandidaten per dataset zonder die gewichten te reconstrueren. Bron: https://arxiv.org/abs/2611.24782

**Een klein model leerde een procedure om autorisatieverklaringen in te perken.** Na training op 2.000 voorbeelden scoorde een 4B-model 92 procent op het beleid dat voor de training was gebruikt. De preprint maakt onderscheid tussen het aanleren van die verwijderprocedure en het bepalen welke verklaring in een nieuw beleid van belang is. Bron: https://arxiv.org/abs/2611.21529

**Een extern register hielp een bevroren model lange reeksen gebeurtenissen bij te houden.** Bij een synthetische taak had een 27B-model 3 van de 100 gevallen met twee gebeurtenissen goed zonder tussenstappen en 96 van de 100 mét tussenstappen. Een bevroren 0,8B-model en een getrainde selector lazen elke gebeurtenis over 299 lange vensters, terwijl het register de samenstelling verzorgde. Bron: https://arxiv.org/abs/2611.25211

## Economie en werk

**Een senior softwareontwikkelaar beschreef een zoektocht naar werk van twee jaar.** De Amerikaanse ontwikkelaar zei sinds het vertrek bij een verzekeringstechnologiebedrijf in januari 2025 geen softwarefunctie te hebben gevonden. In de reacties kwamen carrièreswitches en stromen sollicitaties aan bod, waaronder één wervingsaccount dat ongeveer 1.000 sollicitaties per dag meldde. De discussiedraad bestaat uit individuele verhalen.
Bron: https://news.ycombinator.com/item?id=50583761

**Werknemers met AI in een scenario waren minder geneigd een collega om hulp te vragen.** Een online-experiment met 248 kenniswerkers vond de grootste afname bij brainstormen. Zichtbaar AI-gebruik hing samen met een grotere bereidheid om hulp te vragen. De preprint meet uitgesproken intenties in denkbeeldige scenario’s.
Bron: https://arxiv.org/abs/2611.25269

**Volgens Meta verzorgen agents nu meer dan 60 procent van het werk om technieken over te dragen tussen modellen voor advertentierangschikking.** De agents stellen experimenten voor, bewaken meerdaagse trainingsrondes en herstellen van storingen, terwijl ingenieurs beslissingen beoordelen en goedkeuren. Meta schat dat dit de ingenieurscapaciteit in dat werkproces heeft verdrievoudigd, zonder onafhankelijke meting.
Bron: https://engineering.fb.com/2026/11/18/ml-applications/ai-agents-to-scale-ml-innovations-across-ads-ranking-models/

**De proef van GitHub verstuurde 99 meldingen uit 9.791 problemen die AI signaleerde.** Onderzoekers van Microsoft en geautomatiseerde triage filterden de bevindingen voordat ze besloten meldingen naar zes open-sourceprojecten stuurden. GitHub zegt dat 55 meldingen tot oplossingen leidden en dat zeven onderzoekers ongeveer twee dagen per project aan beoordeling besteedden.
Bron: https://github.blog/open-source/maintainers/maintainers-dont-need-more-ai-bug-reports-they-need-fixes/

**Databricks mat een toename in het gebruik van modellen met open gewichten op zijn gateway.** Modellen met open gewichten stegen van 7,3 naar 30,9 procent van het tokenverkeer in de steekproef van de index onder meer dan 10.000 bedrijven. In afzonderlijke programmeertests bespaarde het doorsturen van een deel van het werk naar kleinere modellen tot 33 procent GPU-tijd op SWE-bench Verified. Het gebruik is specifiek voor Unity Gateway en de uitgavenschattingen gaan uit van catalogusprijzen.
Bronnen: https://www.databricks.com/blog/introducing-databricks-ai-index-state-enterprise-ai-tokenomics, https://arxiv.org/abs/2611.24324

**Een model van de Federal Reserve koppelt eerdere productiviteitsverrassingen aan lagere langlopende rentes.** De auteurs schatten dat wanneer markten rekenden op aanhoudende productiviteitsgroei, de daling van de termijnpremie zwaarder woog dan de verwachte stijging van sommige korte rentes. Hun model gebruikt historische gegevens en geeft geen directe schatting van het effect van AI.
Bron: https://www.federalreserve.gov/econres/notes/feds-notes/when-productivity-booms-do-interest-rates-rise-20261120.html

**Winkelaanbevelingen van AI gingen vooraf aan bezoeken aan genoemde producten.** Onder consumenten die een winkelier de voorgaande week niet hadden bezocht, steeg het aantal bezoeken aan een genoemd product van 0,02 naar 2,07 per 100 antwoorden. De preprint meldt dat 89 procent van die bezoeken geen verwijzingskenmerk van de assistent droeg. De studie koppelde gesprekken aan surfgedrag bij 20 winkeliers en wees adviezen niet willekeurig toe.
Bron: https://arxiv.org/abs/2611.20378

**Britse toezichthouders publiceerden werkwijzen voor het beheersen van AI-gerelateerde cyberrisico’s.** In een enquête van de Bank of England en de FCA verwachtte 88 procent van de respondenten over twee jaar een matig of groot effect op hun risicoprofiel. De toezichthouders publiceerden de werkwijzen naast een afzonderlijke consultatie over cyberweerbaarheid.
Bron: https://www.bankofengland.co.uk/news/2026/november/cyber-resilience-guidance-consultation-and-ai-and-quantum-effective-practices

**Een topman uit de maakindustrie stelt dat gebrekkige gegevensuitwisseling AI in fabrieken beperkt.** Mike Kenworthy, CTO van VulcanForms, haalt een enquête aan waarin 37 procent van de fabrikanten interoperabiliteit noemde als een belangrijk obstakel voor plannen voor slimme fabrieken, tegenover 22 procent in 2025. In zijn essay betoogt hij dat veel fabrieken de gegevens missen die nodig zijn om buiten gecontroleerde werkcellen te werken.
Bron: https://www.therobotreport.com/the-manufacturing-data-gap-holding-back-physical-ai/

## Prompttechnieken

**Revyl stelt voor om verificatie onderdeel te maken van elke programmeersessie.** Hayden White adviseert om architectuurspecificaties actueel te houden, eigenaarschap vast te leggen en te controleren of wijzigingen aan de eisen voldoen, in plaats van toevallige implementatiedetails vast te zetten. Het essay pleit voor het vormgeven van de conventies die agents hergebruiken en bevat geen gecontroleerde vergelijking. Bronnen: https://revyl.com/blog/pattern-engineering/, https://news.ycombinator.com/item?id=50553223

**De handleiding van OpenAI voor GPT-6.2 legt meer nadruk op expliciete stopvoorwaarden.** De gids raadt aan het model te instrueren binnen het kader door te werken, aannames te melden en te pauzeren bij blokkades of onomkeerbare beslissingen. Ook adviseert de handleiding om instructies voor beknoptheid opnieuw te bekijken, omdat de nieuwe modellen uit zichzelf al bondiger zijn. Bron: https://developers.openai.com/api/docs/guides/latest-model/gpt-6.2-astra

## Wat mensen bouwen

**Inkling-2-Mini past in 5,4 GB in een experimentele versie.** De auteur meldt 88 procent op GSM8K, 70,7 procent op HumanEval en ongeveer 104–125 tokens per seconde met drafting op een M5 Max. De claim van een 12-voudige vermindering van divergentie geldt voor een ander Gemma-model. Een HN-reageerder rapporteerde slechtere taalresultaten dan bij een alternatief van Unsloth, en de GGUF-ondersteuning is nog niet af.
Bronnen: https://github.com/ShinMegamiBoson/lookatmyquant, https://news.ycombinator.com/item?id=50591853

**Een model las en wijzigde uitvoerbare bestanden aan de hand van hexdumps.** De auteurs melden dat alle drie de aangepaste programma’s slaagden voor hun verborgen tests en dat het model vier programma’s herkende. De demonstratie gebruikte één poging zonder feedback. Reageerders plaatsten vraagtekens bij hoe breed het resultaat toepasbaar is.
Bronnen: https://sgiannopoulos.github.io/blog/machine-code-programming/, https://news.ycombinator.com/item?id=50546587

**Vier RTX 3090’s haalden een snellere prefill in de experimenten van één bouwer.** De auteur rapporteert dat DeepSeek V4.1 Flash voor prefill bij een context van 32K steeg van 430 naar 2.199 tokens per seconde. Het notebook documenteert zowel mislukkingen als verbeteringen, en de cijfers gelden specifiek voor één opstelling. Bron: https://github.com/alesha-pro/inference-optimization-playbook

**Pi Bot coördineert groepen desktopagents.** De app vraagt de gebruiker groepsplannen te bevestigen en logt toolaanroepen via een gedeeld machtigingssysteem. De makers stellen zonder onafhankelijke audit dat gesprekken en sleutels lokaal blijven. Het terugzetten van controlepunten is beperkt tot macOS. Bron: https://github.com/w01fb0ss/PiBot

**Een programmeeragent draait op een oude Apple-laptop.** Het Perl-project kan gehoste modellen of LAN-modellen aanroepen vanaf Mac OS X Tiger. De maker testte één iBook G4 en geeft geen benchmark voor de geclaimde reactietijd van minder dan een seconde met een lokaal model. Bron: https://github.com/larchanka/ppc-code-ai-agent

**Fast-anything controleert Rust-code van agents aan de hand van vastgelegde functieaanroepen.** De tool profileert een applicatie, vraagt een agent één functie over te zetten en speelt tot 500 aanroepen opnieuw af voordat de functie wordt ingewisseld. De auteur rapporteert een voorbeeld met fuzzy deduplicatie dat op één Windows-machine daalde van 4,91 seconden naar 42 milliseconden. Bron: https://github.com/EL4CTEO/fast-anything

**Open Artifact bewaart werk van agents in bewerkbare mappen.** Een lokale editor kan dia’s en andere bestanden exporteren en opmerkingen van beoordelaars terugsturen naar de oorspronkelijke sessie. Het project zegt geen account of upload nodig te hebben en geeft geen resultaten voor afzonderlijke app-integraties. Bron: https://github.com/JimLiu/open-artifact

**Rounds stuurt een schermaantekening terug naar de Claude Code-sessie die het resultaat maakte.** De Mac-app groepeert lokale artefacten per project en stuurt aantekeningen terug naar de oorspronkelijke sessie. Het gaat om een persoonlijk project zonder ondersteuningstoezegging. Bron: https://github.com/krispuckett/rounds

**Hack Club stelt zijn zelfgehoste uitrolplatform open voor agents.** Orchard biedt een MCP-interface om apps te inspecteren en uit te rollen. Hack Club zegt dat het draait op zes Talos Linux-nodes. De standaardconfiguratie deelt de kernel van de host, en het project waarschuwt een verse installatie niet als geschikt te beschouwen voor niet-vertrouwde code. Bron: https://github.com/hackclub/orchard

**Pandex voegt een MCP-interface toe om wetgeving en rechterlijke uitspraken te doorzoeken.** De dienst zegt 2,8 miljoen documenten te omvatten en biedt een bètategoed van 1.000 verzoeken per dag. De dekking vertoont lacunes, en dit overzicht kon de licentie van de MCP-implementatie niet bevestigen. Bronnen: https://www.pandex.io, https://news.ycombinator.com/item?id=50593481

**Boomzoeken verhoogde de kosten zonder duidelijke winst bij programmeren in een klein experiment.** Over tien pogingen op twee taken versloeg de opstelling met alleen tests geen enkele basislijnrun. Een opstelling met een AI-beoordelaar verbeterde vier pogingen en verslechterde er twee, tegen ongeveer vijf keer zo hoge kosten en vrijwel geen verandering in de gemiddelde score. Bronnen: https://github.com/natsu0529/agent-mcts, https://news.ycombinator.com/item?id=50589235

**Trace2rules zet sessielogs om in onderbouwing voor agentinstructies.** De lokale analysestap gebruikt DuckDB zonder modelaanroepen. Eén uitgewerkt voorbeeld controleert 65 regels over 188 sessies, terwijl een programmeeragent nog steeds de uiteindelijke instructies opstelt. Bronnen: https://github.com/rkkautsar/trace2rules, https://news.ycombinator.com/item?id=50592998

**KeepPlain koppelt commits aan de agentsessies die eraan meeschreven.** De plug-in schrijft een sessie-identificatie in de commitgeschiedenis. De gehoste opzoekfunctie ziet alleen gesynchroniseerde sessies, en de prestatiecijfers komen uit de eigen test van de oprichter met 34 vragen. Bronnen: https://keepplain.com/blame, https://news.ycombinator.com/item?id=50594433

**Scene-finder zoekt filmfragmenten op basis van dialoog.** De Go-tool is afhankelijk van de catalogus van clip.cafe en de beschikbaarheid daarvan. De repository telt vier commits en geen release. Bronnen: https://github.com/robinroy03/scene-finder, https://news.ycombinator.com/item?id=50585848

**Een klein wereldmodel rendert een speelbare Backrooms-scène.** De auteur rapporteert 47 milliseconden per frame op een RTX 5000 Ada voor een model met 211 miljoen parameters. De getrouwheid aan de gesimuleerde trainingswereld daalde van 26,7 dB PSNR in de eerste seconde naar 17,3 dB na twaalf seconden. Bronnen: https://github.com/Yelar/noclip, https://news.ycombinator.com/item?id=50594070

**Pencil maakt van een AI-lesplan een whiteboard met voice-over.** Een validator controleert een JSON-plan voordat de browser SVG tekent en de tekst uitspreekt. De tests gebruiken een vooraf geschreven vervanger, en de auteur meldt alleen DeepSeek live te hebben getest. Bronnen: https://github.com/VBS2004/pencil, https://news.ycombinator.com/item?id=50592137

**Frostwind genereert pixelartwerelden op basis van gecontroleerde gegevenstabellen.** Het model vult tabellen terwijl een renderer overal in de wereld dezelfde schaal en hetzelfde kleurenpalet toepast. Het project bevat vijf speelbare werelden, maar geen nachtverlichting, dialoog of opslagfunctie. Bron: https://github.com/trinity-works/frostwind

**Musset plaatst AI-feedback in de kantlijn van een roman.** De Mac-bèta bewaart hoofdstukken in Markdown en exporteert naar PDF of EPUB. De optionele redacteur gebruikt de bestaande Claude Code- of Codex-sessie van de schrijver. Optionele synchronisatie kost 4,99 euro per maand. Bron: https://github.com/Musset-App/musset

## Het lezen waard

**OpenRouter verwijderde drie aanbieders na meldingen over gelekte prompts.** Een onderzoeker van Dragos verstuurde ongeveer twee miljoen prompts met nepgeheimen via routers en inferentiehosts. OpenRouter zegt drie aanbieders te hebben verwijderd en 125 eindpunten te hebben uitgesloten van zero data retention (geen gegevensopslag). De bevinding berust op waargenomen gebruik van testgeheimen en afgeleide routering, en de volledige omvang blijft onzeker.
Bronnen: https://arstechnica.com/security/2026/11/a-leaky-ai-supply-chain-is-exposing-secret-user-data-at-an-alarming-rate/, https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/, https://news.ycombinator.com/item?id=50595554, https://news.ycombinator.com/item?id=50582794, https://news.ycombinator.com/item?id=50585962

**Bijdragers aan Lean en Mathlib controleerden het bewijs van Levent Alpöge voor de Riemann-hypothese.** Een gezamenlijk bericht stelt dat onafhankelijke controleprogramma’s en de kernel van Lean het geëxporteerde bewijs hebben geverifieerd tegen de formulering in Mathlib. De aankondiging geeft geen bewijsmateriaal voor hoe het bewijs is gevonden.
Bronnen: https://leanprover-community.github.io/blog/posts/riemann-hypothesis/, https://news.ycombinator.com/item?id=50589618, https://news.ycombinator.com/item?id=50590441, https://math.mit.edu/~drew/grh/, https://news.ycombinator.com/item?id=50583445, https://www.youtube.com/watch?v=zqzk43bSdDI

**Cerebras verplaatste prefill naar GPU’s en hield decodering op zijn eigen chips.** De leverancier rapporteert vijf keer zoveel tokens per megawatt als bij volledige uitvoering op CS-3-systemen, zonder verlies aan generatiesnelheid. De meting betreft één gedeeld eindpunt voor GPT-OSS-120B, zonder beschikbare resultaten van partners. Bron: https://www.cerebras.ai/blog/cerebras-launches-disaggregated-inference

**Een veteraan op het gebied van Python-infrastructuur documenteert wat AI wel en niet kan in zijn project.** Simon Willison wijst op het verslag van Graham Dumpleton over de bouw van Muru, een Rust-server voor Python-apps. Dumpleton publiceerde tussen 4 en 21 november 18 ontwikkelberichten en beschrijft waar zijn eigen oordeel nog altijd de wijzigingen stuurt. Bron: https://simonwillison.net/2026/Nov/21/muru/

**Cloudflare beschrijft twee kleine modellen voor beslissingen en extractie.** In een interview met Latent Space zegt Michelle Chen dat Clef getypeerde beslissingen met waarschijnlijkheden teruggeeft en Clairic getypeerde waarden in één doorgang extraheert. Haar vergelijking van ongeveer twee weken voor Clef tegenover twee jaar voor een ander model is een eigen opgave van het bedrijf. Bron: https://latent.space/p/cloudflare/

**De COO van Linear zegt dat agents nu meer dan de helft van de werktaken van het bedrijf aanmaken.** Cristina Cordova vergelijkt dat cijfer met ongeveer 3 procent een jaar eerder en zegt dat mensen ondersteuningsantwoorden goedkeuren die door AI zijn opgesteld. De cijfers zijn van Linear zelf, en sommige AI-functies worden naar gebruik gefactureerd. Bron: https://latent.space/p/linear-scaling/

## Hacker News

**ClawDOS brengt een programmeeragent naar DOS.** Het hobbyproject lokte reacties uit over debuggen op verouderde Windows-hardware. De HN-discussie trok 159 punten en 51 reacties en bood geen systematische beoordeling. Bronnen: https://news.ycombinator.com/item?id=50586292, http://ricapar.net/ClawDOS/

**Mem kondigde aan dat het stopt.** Het bedrijf maakte de sluiting bekend. Reacties over waarom het notitieproduct moeilijk te verkopen was, zijn verklaringen van individuele lezers. Bronnen: https://news.ycombinator.com/item?id=50526537, https://get.mem.ai/blog/mem-is-shutting-down

**Een preprint oppert een commerciële verklaring voor vleierij door AI.** *The Hungry Butler Effect* betoogt dat prikkels om gebruikers vast te houden het gedrag van modellen kunnen sturen. De HN-discussie en de beschikbare beschrijving leveren geen meting die het voorgestelde verband aantoont. Bronnen: https://news.ycombinator.com/item?id=50583117, https://www.researchgate.net/publication/418143113_The_Hungry_Butler_Effect_Concealed_Commercial_Incentives_and_the_Erosion_of_Epistemic_Rigour_in_Large_Language_Models

**Een mededeling van een gerechtshof meldt een optreedverbod van twee jaar voor een advocaat.** Het Europees Hof voor de Rechten van de Mens verwees naar ongeverifieerde verwijzingen die door AI waren gegenereerd. Dit overzicht kon de onderliggende pagina van het hof niet rechtstreeks ophalen en nam het volledige adres van de mededeling over uit de discussie. Bronnen: https://news.ycombinator.com/item?id=50579237, https://www.echr.coe.int/w/romanian-lawyer-barred-for-two-years-from-representing-applicants-before-the-court-over-unverified-ai-generated-citations

**Een handleiding laat zien hoe Maple modellen met open gewichten bundelt met een gehoste dienst.** De auteur beschrijft de opzet en reageerders vergelijken de kosten en privacy met andere diensten en met lokale inferentie. Die vergelijkingen zijn individuele ervaringen. Bronnen: https://news.ycombinator.com/item?id=50588396, https://micahflee.com/heres-how-anyone-can-easily-use-private-open-weight-models/

## YouTube

**Ahmad Osman bespreekt de keuze van hardware voor lokale AI.** Bij AI Engineer behandelt de oprichter van Osmantic geheugenbandbreedte, batching en het huren versus bezitten van GPU’s. Zijn pleidooi om voortdurend leren (continual learning) uit te voeren op machines waar gebruikers zelf zeggenschap over hebben, is zijn eigen opvatting. Bron: https://www.youtube.com/watch?v=GKSQYbELDzw

**Volgens Ramp schrijft en publiceert een interne agent ongeveer 75 procent van de code.** Bij AI Engineer bespreekt Zach Bruggeman gedeelde sessies, verificatie en codebeoordeling. Het bedrijf gaf het cijfer op zonder te vermelden hoe het telt welke code door de agent is geschreven. Bron: https://www.youtube.com/watch?v=MDI81OaZAD4

**De topman van Ramp beschrijft een ongelijke ingebruikname van agents.** In een interview met Y Combinator beschrijft Eric Glyman interne tools en grote winsten bij een handvol medewerkers. Het verslag bevat geen onafhankelijke productiviteitsmeting. Bron: https://www.youtube.com/watch?v=0Hvs6-XODgU

**First Person Labs presenteert een laag voor persoonlijke context.** Bij a16z legt Ken Liu uit hoe Second activiteiten over verschillende apps heen volgt en de informatie beschikbaar maakt voor gekozen agents. De beschrijving biedt geen openbaar bewijs dat de privacyclaims van de oprichter toetst. Bron: https://www.youtube.com/watch?v=kBJe4H_WobA

**DW Documentary brengt de risico’s van AI in kaart.** De Engelstalige film bevat interviews met Geoffrey Hinton, Yoshua Bengio en Yann LeCun. Het verslag over de dood van een tiener berust op de getuigenis van zijn moeder en vormt geen nieuw onderzoek. Bron: https://www.youtube.com/watch?v=2I4qMBiK6hg

**Voormalige Amerikaanse adviseurs pleiten ervoor een voorsprong in rekenkracht te benutten om in veiligheid te investeren.** Bij The Cognitive Revolution bespreken Ben Buchanan en Tantum Collins toeleveringsketens, exportbeperkingen en technische vraagstukken zoals reward hacking. Het gesprek geeft hun beleidsargument weer. Bron: https://www.youtube.com/watch?v=6bSzdXKkE2M

**Stanford HAI blikt terug op de opkomst van generatieve AI.** Een panel bespreekt het derde AI100-rapport, waaronder redeneermodellen, rekenmiddelen en omstreden bewijs over werk. De videobeschrijving geeft geen nieuwe metingen. Bron: https://www.youtube.com/watch?v=WGjuvTvz90U

**The Institute of Art and Ideas debatteert over wat als intelligentie geldt.** Het panel bespreekt belichaming (embodiment) en of het opschalen van huidige modellen volstaat. De Engelstalige video is een voorproefje van een langere discussie achter een betaalmuur. Bron: https://www.youtube.com/watch?v=DF8jyfEjymo

**PočúvAI behandelt beweringen over snellere geneesmiddelenontwikkeling.** De Slowaakstalige aflevering van Aktuality.sk bespreekt ook de toegang tot elektriciteit en persoonsgegevens. De beschrijving van de video geeft geen nieuwe resultaten over geneesmiddelen. Bron: https://www.youtube.com/watch?v=OkIoQ1imz90

## In het kort

**De Amerikaanse GAO somt 16 opties op om cyberrisico’s van AI aan te pakken.** Het rapport groepeert ze onder vier doelen, waaronder richtlijnen, onderzoek, toezicht gedurende de hele levenscyclus van een systeem en de ontwikkeling van personeel. Het bespreekt ook toepassingen van AI voor defensieve analyse. Bron: https://www.gao.gov/products/gao-27-108458

**Drie leden van het Amerikaanse Huis van Afgevaardigden schetsten mogelijke eisen voor frontier-AI-labs.** Het discussiestuk voor de SAFE AI Act stelt evaluatie vóór release, het melden van incidenten en minimumnormen voor. Het heeft geen wetsnummer of indieningsdatum. Bron: https://casrai.org/news/safe-ai-act-outline-frontier-ai-labs-2026
