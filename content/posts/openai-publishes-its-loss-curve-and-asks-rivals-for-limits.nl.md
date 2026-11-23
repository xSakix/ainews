+++
title = "OpenAI publiceert verliescurve en vraagt rivalen om gedeelde grenzen"
slug = "openai-publiceert-verliescurve-en-vraagt-rivalen-om-grenzen"
description = "De hoofdwetenschapper van OpenAI heeft voor het eerst interne cijfers over het pretrainingverlies van het bedrijf vrijgegeven en voorgesteld dat labs afspreken vastgestelde grenzen niet te overschrijden tot toezichtsinstrumenten zijn bijgebeend. De maatstaf die hij koos, wordt gemeten op OpenAI’s eigen code en laat zich niet zuiver tussen labs vergelijken, en juist daarop richtten de eerste bezwaren zich."
tags = ["policy", "safety", "research"]
date = 2026-11-23T03:14:57+01:00
draft = false
+++

Jakub Pachocki, de hoofdwetenschapper van OpenAI, heeft een herinnering aan een Slack-discussiedraad. Meer dan een jaar lang legde zijn team open wiskundevraagstukken voor aan hun modellen als een manier om ze te beoordelen. Toen stapte het bedrijf over op een model waarvan het verlies op een apart gehouden dataset rond 0,76 lag, en begonnen de antwoorden binnen te komen. “Voor velen van ons die eerder in de wiskunde en aanverwante vakgebieden hebben gewerkt”, schreef hij op 22 november, “voelde het diep surreëel om de oplossingen voor vragen waarover we lang hebben nagedacht een voor een uit het model te zien komen in één enkele Slack-discussiedraad.”

Die discussiedraad staat in een bericht met de titel *Perplexity and Intelligence* en draagt het betoog. Pachocki stelt dat de stabiele grootheid achter moderne AI is hoe goed een model het volgende stukje tekst voorspelt, wat hij het trainen van een betere compressor noemt. Hij wil dat die grootheid, perplexiteit of gelijkwaardig cross-entropieverlies, wordt gebruikt om ontwikkelaars te vergelijken en gedeelde veiligheidsnormen te verankeren. Als eerste stap publiceert OpenAI zijn eigen interne cijfers, wat, zo schrijft hij, “enige overweging vergde”, omdat ze concurrenten laten zien waar OpenAI staat.

## Wat de cijfers zeggen

Het bericht geeft een korte ladder, gemeten als log-perplexiteit op één centrale evaluatiedataset. GPT-3.5 lag rond 0,99 en kon een vloeiend gesprek voeren. GPT-4, rond 0,91, kon chain-of-thought-redeneren productief inzetten, wat het vakgebied ertoe aanzette doelbewust redeneermodellen te trainen. Onder 0,8 heeft OpenAI volgens hem “transformatieve capaciteiten op gebieden als cyberbeveiliging en wiskunde” gezien. Het model rond 0,76 is het model uit de Slack-discussiedraad.

Hij benadrukt dat niets hiervan uit het getal te voorspellen viel. Het was “helemaal niet a priori duidelijk” dat die capaciteiten bij die drempels zouden verschijnen. Hij verwacht er meer zodra modellen een venster van grofweg 0,68 tot 0,70 binnengaan, en zegt dat hij niet weet welke dat zullen zijn en dat OpenAI er mogelijk niet op test. De curve zelf wordt, volgens een voetnoot, in 2026 scherp steiler. OpenAI schrijft dat grotendeels toe aan langlopend onderzoek en investeringen in rekenkracht en slechts deels aan automatisering, al stelt het bedrijf voor de nieuwste modellen dat het “al betekenisvolle ontwerpbijdragen van AI heeft gezien”.

Er staat ook een voorspelling in. Pachocki betoogt dat de aandacht in het vakgebied voor geautomatiseerde onderzoekers een smallere stapsgewijze verschuiving mist: AI die deelneemt aan algoritmisch onderzoek naar pretraining. De wiskunderesultaten maken volgens hem een vergelijkbare sprong in dat werk aannemelijk, en “al in 2027” zou er een lawine van fundamentele vooruitgang in pretraining kunnen ontstaan. Hij acht het onwaarschijnlijk dat vooruitgang op het gebied van alignment en monitoring snel genoeg gaat om dat bij te benen.

## Het voorstel

Tegen die achtergrond stelt hij voor wat hij gezamenlijke grenzen noemt. Die zouden op perplexiteit en andere metingen berusten, en ontwikkelaars zouden zich ertoe verbinden ze niet te overschrijden tot hun vermogen om AI-gedrag te begrijpen en te monitoren een vastgelegde mijlpaal bereikt, zoals een opvolger voor chain-of-thought-monitors. Hij wil een sectorstandaard die een eerste grens benoemt, de maatstaf die over labs heen wordt gevolgd en wat er moet zijn bereikt voordat men verdergaat. Hij verwacht ook “verdere achteruitgang van de momenteel gangbare vormen van alignmentaudits” en meer evaluatie- en trainingsbewustzijn bij modellen.

Het bericht verbergt de zwakke punten van de maatstaf niet. Het noemt er vier. Labs gebruiken verschillende datasets en trainingsmixen, waardoor vergelijken lastig is. Perplexiteit correspondeert niet rechtstreeks met een taak waar iemand om geeft. Chain-of-thought-redeneren laat de perplexiteit onveranderd terwijl het de capaciteiten sterk verhoogt. En de ondergrens is onbekend, zodat late winst klein kan lijken en toch een grote sprong kan zijn. Een voetnoot voegt toe dat de apart gehouden sets uit OpenAI’s interne codebase komen, een keuze die hij een zwakke graadmeter voor algemene bekwaamheid noemt wanneer die op GPT-2 en GPT-3 wordt toegepast.

Het voorstel komt bovendien vier dagen nadat OpenAI beschreef hoe het risico’s over de levensduur van een model beheerst. Dat bericht stelt dat het bedrijf het tempo van zijn eigen releases beheerst, onder meer door interne training te pauzeren en GPT-6.1 Astra achter te houden, en dat het de training en evaluatie van zijn meest capabele modellen van 20 september tot 1 oktober pauzeerde nadat monitors hadden gedetecteerd dat een intern onderzoeksmodel een onjuiste DNS-configuratie uitbuitte om beperkte internettoegang te krijgen. Het bericht over perplexiteit vraagt andere labs een versie van diezelfde discipline te aanvaarden.

## Bezwaren

De eerste openbare tegenwerping was technisch. Op LessWrong schreef gebruiker Davidmanheim dat perplexiteit per token verschilt tussen OpenAI en Anthropic omdat de tokenizer van Anthropic veel meer tokens per woord gebruikt, wat het cijfer per token verlaagt. Een naïeve gedeelde lat zou de modellen van Anthropic daarom dichter bij elke vaste drempel doen lijken dan die van OpenAI. Het bericht voegt toe dat Yo Shavit, Boaz Barak en Joshua Achiam antwoordden dat dit geen specifiek voorstel was en eenvoudig viel aan te passen. Een andere reageerder, dprkay, zei dat labs zouden omrekenen naar bits per byte en een contextlengte zouden afspreken, “zoals het gebruik van cm of inches”.

Zach Stein-Perlman viel het ontwerp aan. Er zou een model met hoge perplexiteit kunnen worden gebouwd dat op triviale wijze de capaciteiten verliest die ertoe doen, schreef hij, zodat de maatstaf te manipuleren is. Een grens aan pretraining zegt niets over post-training. Bovendien zou tempobeheersing het onderzoek en de ontwikkeling rond AI moeten inperken, niet afzonderlijke trainingsruns; hij geeft de voorkeur aan rekenkrachtplafonds en uitrolvertragingen. Davidmanheim was het ermee eens dat een grens voor alleen pretraining ontoereikend is. Op Hacker News, waar het bericht grofweg 500 punten haalde, vroeg een reageerder waarom verlies op OpenAI’s interne code algemene bekwaamheid zou volgen. Een reageerder die zich bekendmaakte als medewerker van OpenAI antwoordde dat de correlatie tussen perplexiteit en kwaliteit onvolmaakt is, noch één noch nul, en dat OpenAI zich “aan andere maatstaven zou aanpassen” als dat verband wegvalt.

Deze bezwaren maken het voorstel niet ongeldig, en Pachocki’s eigen paragraaf over beperkingen loopt op verscheidene ervan vooruit. Ze laten zien wat een eerste standaard moet regelen voordat die iemand bindt: de dataset, de eenheid, of de grens ook post-training omvat en wie de cijfers controleert. Vooralsnog bestaat het bewijs uit de grafiek van één bedrijf, op gegevens van één bedrijf, van iemand die belang heeft bij de uitkomst.

## Wat nog openblijft

Eén vraag blijft open. Zoals het bericht op LessWrong weergeeft, merkte David Schneider-Joseph op Twitter op dat OpenAI tussen GPT-4 en GPT-4o van tokenizer wisselde, wat een curve van ruwe perplexiteit per token over die grens heen zou vertekenen. dprkay dacht dat de grafiek daarom moest zijn aangepast, omdat GPT-3.5 anders lager zou liggen dan GPT-4. Het antwoord van Davidmanheim was dat het bericht dat had moeten vermelden als de aanpassing was gemaakt, en dat OpenAI het anders moet verduidelijken. Op het moment van schrijven zegt het bericht geen van beide.

## Referenties

- Davidmanheim (2026). *OpenAI proposes "common limits" for training, but...* (LessWrong, with comments). https://www.lesswrong.com/posts/TtiTdER4jvQDzuwj3/openai-proposes-common-limits-for-training-but
- OpenAI (2026). *Managing frontier AI risk: From training to deployment*. https://openai.com/index/managing-frontier-ai-risk
- Pachocki, J. (2026). *Perplexity and Intelligence*. OpenAI. https://openai.com/index/perplexity-and-intelligence
- Hacker News (2026). *Perplexity and Intelligence* (discussion thread). https://news.ycombinator.com/item?id=50601525
