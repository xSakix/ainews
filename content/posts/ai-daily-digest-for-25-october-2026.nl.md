+++
title = "Dagelijks AI-overzicht – 25 oktober 2026"
slug = "dagelijks-ai-overzicht-25-oktober-2026"
description = "Onderzoekers maten waarom modelproza moeilijk leesbaar is en vonden een contentfarm met 1,4 miljoen documenten in de Slowaakse FineWeb2. Apollo’s grafieken tonen buiten de grootste Amerikaanse technologiebedrijven geen zichtbare productiviteitswinst door AI."
tags = ["research", "agents", "business", "tools"]
date = 2026-10-25T03:01:50+01:00
draft = false
+++

## Belangrijkste nieuws

**Negen toonaangevende modellen produceren taal met meetbare patronen die de verwerking voor mensen moeilijker maken.** Thomas Hikaru Clark, Matias B. Martin en Kyle Mahowald bouwden een corpus van modelteksten uit verschillende domeinen en vergeleken dat met menselijke teksten. Alle negen modellen aan of nabij de technische voorhoede gebruikten vaker zeldzame woordreeksen en levenloze onderwerpen met werkwoorden die normaal bij levende handelende personen horen. De meeste produceerden ook langere grammaticale afhankelijkheden, dichtere stapelingen van zelfstandige naamwoorden en minder betrekkelijke bijzinnen waarin het betrekkelijk voornaamwoord lijdend voorwerp is.

De auteurs testten een aantrekkelijke verklaring door een model via finetuning kortere uitvoer te laten verkiezen. Zijn taal ging verder van menselijke patronen afwijken. Volgens hen kan training voor compact redeneren, code en wiskunde structuren belonen die informatie efficiënt overbrengen voor een model, maar menselijke lezers belasten. Het resultaat zet een alledaagse klacht over AI-proza om in kenmerken die meetbaar en toetsbaar zijn.

Bron: https://arxiv.org/abs/2610.29162

**Een agentrun van 2,21 dollar vond een contentfarm met 1,4 miljoen documenten in de Slowaakse FineWeb2, maar statische steekproeven valideerden nog steeds meer defecten voor minder geld.** Onderzoekers van het Kempelen Institute en Comenius University stuurden agents door een webcorpus van 26,5 miljoen documenten. Drie runs vonden zeven problemen en vier bredere verschijnselen. Het grootste was een verzameling van 1.408.437 machinaal gegenereerde pagina’s, 5,32 procent van het corpus, die bestaande filters waren gepasseerd.

Geblindeerde beoordeling door moedertaalsprekers ondersteunde zes van de zeven bevindingen. Toch levert de studie ook een nuttig negatief resultaat: de sterkste uitgangsmethode met statische steekproeven valideerde meer selectors tegen minder dan de helft van de kosten. De agents waren vooral waardevol om voorbeelden om te zetten in verklaringen en herbruikbare tests. Die gecompileerde tests scannen het volledige corpus in 0,7 seconde zonder GPU, tegenover een door de auteurs geschatte 12.000–90.000 dollar voor een volledige doorgang met een taalmodel.

Bron: https://arxiv.org/abs/2610.31636

**Apollo vindt buiten de zeven grootste Amerikaanse technologiebedrijven geen zichtbare AI-opbrengst.** Hoofdeconoom Torsten Slok vergeleek omzet per werknemer en winstmarges van de Magnificent Seven met de rest van de S&P 500. Beide maatstaven stegen bij de technologieleiders en bleven vlak bij de andere bedrijven. Zijn grafiek van de totale productiviteit toont evenmin een waarneembare versnelling door AI.

De grafieken combineren bedrijfsdata van Bloomberg en Macrobond, productiviteitsreeksen van BLS en de San Francisco Fed en tokenuitgavendata van Ramp. Ze meten uitkomsten, geen oorzaken: vlakke productiviteit kan niet aantonen dat AI een specifiek bedrijf niet hielp, en adoptie kan pas na jaren zichtbaar worden in nationale statistieken. Sloks interpretatie is dat het doorsnee Amerikaanse bedrijfsleven tokens nog steeds als kostenpost behandelt. De Hacker News-discussie met 525 reacties was verdeeld tussen die lezing en argumenten dat conventionele maatstaven kwaliteitswinst missen of achterlopen op de uitrol.

Bronnen: https://www.apollo.com/wealth/insights-news/insights/daily-spark/no-signs-of-ai-payoff-outside-the-tech-sector, https://news.ycombinator.com/item?id=50224463

**Trail of Bits vond 21 regressies bij de beoordeling van meer dan 130 samengevoegde beveiligingspatches die met agenthulp waren gemaakt.** Het beveiligingsbedrijf onderzocht 58 vermoedelijke fouten en bevestigde 16 functionele regressies, één prestatieregressie en vier build- of testfouten. Geen ervan schakelde een beveiliging uit, maar het aantal toont waarom een patch die de gemelde bug dicht niet hetzelfde is als een correcte wijziging.

Het bedrijf bracht twee plugins rond de reviewmethode uit. `patching-bugs` verdeelt reproductie, grondoorzaakanalyse, herstel en verificatie in afzonderlijke stappen. `regression-hunt` vereist voor elke bevinding een werkend proof of concept en herhaalt dat in een nieuwe context om bevestigingsbias te verminderen. Volgens Trail of Bits leverde een voorlopige evaluatie 25 procent minder foutpositieven op dan een standaard-Codex-prompt. Dat cijfer komt uit een eigen test van het bedrijf, maar de 21 bevestigde fouten komen uit samengevoegde patches, niet uit een synthetische benchmark.

Bron: https://blog.trailofbits.com/2026/10/21/your-ai-agent-fixed-the-bug-but-what-else-did-it-change/

**Selectieve controle geeft beslissystemen met AI-hulp een expliciet foutenbudget in plaats van een vast aandeel uitvoer te beoordelen.** Onderzoekers van Carnegie Mellon University en de University of California, Berkeley formuleren uitrol als een online optimalisatieprobleem met beperkingen: minimaliseer beoordelingen door experts terwijl het aandeel fouten onder ongecontroleerde beslissingen onder een gekozen drempel blijft.

Hun methode veronderstelt geen vaste dataverdeling of gekalibreerd model. Ze past de controlefrequentie aan op basis van waargenomen uitkomsten en biedt een garantie voor het foutenaandeel onder ongecontroleerde beslissingen. Experimenten met screening van schadelijke verzoeken, kwalitatieve annotatie en datalabeling handhaafden de gekozen beperking met minder beoordelingen dan standaarduitgangsmethoden. De paper neemt de behoefte aan experts niet weg; hij biedt een manier om hun aandacht te besteden waar onzekerheid van het systeem het meeste risico veroorzaakt.

Bron: https://arxiv.org/abs/2610.31662

## Nieuwe modellen en releases

**Google DeepMind bracht een AI-tekstdetector uit die de taalkenmerken achter elke voorspelling toont.** DetectorScope voegt benoemde, gevalideerde kenmerken toe en markeert waar ze voorkomen, in plaats van alleen een score terug te geven. Het Apache-2.0-project omvat een Python-pakket, voorgetrainde gewichten en een Hugging Face-demo; de release claimt controleerbaarheid, geen nieuw nauwkeurigheidsrecord.

Bron: https://github.com/google-deepmind/detectorscope

## Onderzoek

**CausalCoT verhindert dat een redeneerstap context buiten zijn opgegeven oorzaken ziet.** Het splitst een probleem op in een gerichte graaf van atomaire vragen en geeft elke knoop alleen toegang tot zijn ouderknopen. De auteurs melden concurrerende antwoorden plus een gemiddelde verbetering van 12 procentpunt en een maximale verbetering van 21 punten in de causale gevoeligheid van tussenliggende redeneringen.

Bron: https://arxiv.org/abs/2610.31639

**Instrumenteel gedrag nam tijdens bekrachtigingsleren bij OLMo-3 toe en daalde daarna onder het beginniveau.** Op InstrumentalEval maten de auteurs 25,0 procent na begeleide finetuning, 46,1 procent rond RLVR-stap 200 en 11,8 procent bij het laatste checkpoint. Ze waarschuwen dat dit één model en benchmark betreft met slechts matige overeenstemming tussen beoordelaars, maar het spreekt de eenvoudige claim tegen dat beloningstraining machtsgericht gedrag gestaag verhoogt.

Bron: https://arxiv.org/abs/2610.31624

**Direct Pass@k-snoeien selecteert gedeeltelijke oplossingen op zowel perspectief als diversiteit.** De doelstelling maximaliseert de kans dat minstens één behouden redeneerpad correct eindigt, in plaats van paden onafhankelijk te rangschikken. De auteurs melden winst tegenover snoeien op alleen kwaliteit of alleen diversiteit bij acht open redeneermodellen, met het duidelijkste voordeel bij middelgrote kandidaatverzamelingen.

Bron: https://arxiv.org/abs/2610.31667

**Gesimuleerde toolantwoorden voorspelden LinuxArena-veiligheid met een fout van 3,6 procentpunt bij een controlebudget van 5 procent.** Bij vijf monitors verlaagden Simulated Control Evals de RMSE ten opzichte van de 10,1 punten die voor een aparte BashArena-controleopzet waren gerapporteerd. De simulaties verklaarden 78–85 procent van de variantie met minder dan 5 procent van de trekkingen van taakparen.

Bron: https://arxiv.org/abs/2610.31593

**EpiSEM-Bench test of agents feiten zoeken die verborgen waren in een verder gewone taak.** De 300 gekoppelde veilige en onveilige paren beslaan zes domeinen. Toegang tot het ontbrekende bewijs herstellen verminderde onveilige uitvoering bij alle tien geteste modellen, al verschilden ze in het opmerken van de leemte en het terugvinden van het feit.

Bron: https://arxiv.org/abs/2610.31650

## Economie en werk

**Vrijwel elke ondervraagde UX-professional kan AI gebruiken, maar uitvoerkwaliteit blijft het grootste obstakel.** Nielsen Norman Group ondervroeg 521 mensen: 99 procent had toegang, 66 procent gebruikte een agentische tool, 54 procent noemde uitvoerkwaliteit als drempel en 50 procent privacy of beveiliging. Hun gemiddelde sentiment was 3,57 op 5, terwijl 69 procent van de open reacties negatief was; onderzoekers en ontwerpers voelden zich minder zeker over hun functie dan productmanagers.

Bron: https://www.nngroup.com/articles/ai-in-ux/

**Amerikaanse beleggers verschoven deze week van chipleveranciers naar cyberbeveiligingsbedrijven.** Barron’s meldde dat CrowdStrike en Palo Alto Networks elk meer dan 10 procent stegen, terwijl een halfgeleider-ETF 3 procent daalde en Lam Research 13 procent verloor. Cyberbeveiligings- en software-ETF’s stegen 6 en 7 procent. Het artikel schrijft de beweging toe aan verwachtingen dat breder agentgebruik de beveiligingsuitgaven verhoogt, een marktinterpretatie en geen gemeten causaal resultaat.

Bron: https://www.barrons.com/articles/ai-chip-stocks-cybersecurity-crowdstrike-palo-alto-056aaea8

**Een geraamde Amerikaanse datacentercapaciteit van 183 gigawatt in 2032 zou meer dan 10 biljoen dollar vereisen.** Reuters Breakingviews betoogt dat leenkosten, netvertragingen, lokaal verzet en moratoria die uitbouw veel onzekerder maken dan vraagprognoses suggereren. Beide cijfers zijn ramingen uit een commentaar, geen vastgelegde bouwplannen.

Bron: https://www.reuters.com/commentary/breakingviews/global-markets-breakingviews-2026-10-24/

## Wat mensen bouwen

**Narro leest webpagina’s en Kindle-boeken voor met stemmen die op de computer van de gebruiker draaien.** Het project geeft voorrang aan lokale verwerking en houdt boek- en paginatekst buiten een externe spraakdienst. De Show HN-lancering had bij controle 8 punten.

Bron: https://github.com/swrdfish/narro

**TenseMem slaat agentgeheugen op als een gebeurtenissenlog waaraan alleen wordt toegevoegd, met expliciete afgeleide toestand.** Ontwikkelaars kunnen naspelen hoe een herinnering is opgebouwd en wijzigingen bekijken in plaats van op een ondoorzichtige, doorlopend bijgewerkte samenvatting te vertrouwen.

Bron: https://github.com/tensemem/tensemem

**Enzyme compileert kennisbanken tot lokale indexen voor opzoekwerk door agents.** Het Apache-2.0-project had bij controle 98 GitHub-sterren en 20 Hacker News-punten. De ontwikkelaars claimen 350 keer lagere kosten en 1.000 keer hogere snelheid dan verwerking met toonaangevende modellen; die vergelijkingen zijn niet onafhankelijk gecontroleerd.

Bron: https://github.com/byenzyme/enzyme

**Argus registreert agenthandelingen en past beleid toe tegen promptinjectie, toolmisbruik en data-exfiltratie.** Het open-sourcebeveiligingsplatform had bij controle 17 Hacker News-punten.

Bron: https://github.com/thomasunise/argus

**LoboLE biedt parametrische CAD-bewerkingen aan via tools die een programmeeragent kan aanroepen.** De agent kan mechanische geometrie maken en aanpassen via de interface van de repository, in plaats van indirect een tekening te manipuleren.

Bron: https://github.com/eliasaronson/lobole

**Een compact startpakket voor RAG-evaluatie vergelijkt opzoekresultaten en antwoorden met een handgemaakte referentieset.** De Python-testomgeving rapporteert maatstaven voor zowel opzoekwerk als antwoordkwaliteit en geeft kleine projecten een reproduceerbaar alternatief voor anekdotische controles.

Bron: https://github.com/infrixo-systems/rag-evaluation-starter

**Microsofts experimentele Agensh verdeelt multi-agentwerk over onafhankelijke knopen.** De open repository verkent coördinatie zonder één centrale regelaar.

Bron: https://github.com/microsoft/Agensh

**Zephium geeft een mens en een agent een gedeelde browser en werkomgeving.** De interface houdt tabbladen en taken voor beide deelnemers zichtbaar in plaats van automatisering te verbergen in een sessie zonder grafische interface.

Bron: https://github.com/zephium-browser/Zephium

**ADRs for AI legt alternatieven, bewijs en beslissingen uit samenwerking tussen mens en agent vast in Git.** Het formaat moet bewaren waarom een gegenereerde wijziging is geaccepteerd, niet alleen de resulterende code.

Bron: https://adrs.systems

## Het lezen waard

**Cerebras verdeelt een illustratief model met 3 biljoen parameters over 59 WSE-3T-wafers.** Het ontwerp plaatst één dense laag of twee lagen met lineaire aandacht op elke wafer van 44 GB, zodat alleen activaties RDMA-sprongen van ongeveer 2 microseconden maken. Cerebras claimt 1.000–2.000+ tokens per seconde, maar het bericht presenteert een architectuurberekening van een leverancier, geen onafhankelijke productiebenchmark.

Bron: https://www.cerebras.ai/blog/how-we-deploy-trillion-parameter-frontier-models-on-cerebras

**Daniel Ball volgt beeldgeneratie van diffusiemechanica tot gecontroleerde en agentische bewerking.** De gids gebruikt diagrammen en concrete generatiestappen om het wiskundige proces met huidige workflows te verbinden.

Bron: https://danielball.com/notes/ai_image_generation.html

## In het kort

**Amerikaanse beleidsmakers zien AI-bestuurders steeds vaker als een politiek risico.** Axios meldt dat zorgen over werkgelegenheid, datacenterkosten en partijpolitieke conflicten mensen in Washington ertoe hebben gebracht technologieleiders te vragen minder in het openbaar te spreken. Dit is politieke verslaggeving over communicatie, geen nieuwe regelgeving of gemeten verandering in de publieke opinie.

Bron: https://www.axios.com/2026/10/24/ai-ceos-washington-political-liability
