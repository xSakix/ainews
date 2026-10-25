+++
title = "Dagelijks AI-overzicht – 25 oktober 2026"
slug = "dagelijks-ai-overzicht-25-oktober-2026"
description = "Onderzoekers maten waarom teksten van modellen moeilijk te lezen zijn. Een afzonderlijk onderzoek vond een contentfarm met 1,4 miljoen documenten in het Slowaakse FineWeb2, terwijl grafieken van Apollo buiten de grootste Amerikaanse technologiebedrijven geen zichtbare productiviteitsverbetering door AI tonen."
tags = ["research", "agents", "business", "tools"]
date = 2026-10-25T03:01:50+01:00
draft = false
+++

## Belangrijkste nieuws

**Negen toonaangevende modellen produceren taal met meetbare patronen die de verwerking voor mensen moeilijker maken.** Thomas Hikaru Clark, Matias B. Martin en Kyle Mahowald bouwden een corpus van modelteksten uit verschillende domeinen en vergeleken het met menselijke teksten. Alle negen modellen aan of dicht bij de technologische top gebruikten meer ongebruikelijke woordreeksen. Ze koppelden ook vaker levenloze onderwerpen aan werkwoorden die normaal handelingen van levende wezens beschrijven. De meeste plaatsten grammaticaal verbonden woorden verder uit elkaar, gebruikten dichtere reeksen zelfstandige naamwoorden en produceerden minder betrekkelijke bijzinnen met een objectfunctie.

De auteurs onderzochten één mogelijke verklaring door een model met finetuning een voorkeur voor kortere uitvoer te geven. Daarna produceerde het model taal die nog verder afweek van menselijke patronen. Volgens de auteurs kan training voor compact redeneren, code en wiskunde structuren belonen die informatie voor een model efficiënt weergeven, maar voor mensen moeilijker leesbaar zijn. Hun werk benoemt meetbare kenmerken achter een veelgehoorde klacht over AI-proza.

Bron: https://arxiv.org/abs/2610.29162

**Een agentrun van 2,21 dollar vond een contentfarm met 1,4 miljoen documenten in het Slowaakse FineWeb2. Met statische steekproeven bevestigden onderzoekers echter meer gebreken tegen lagere kosten.** Onderzoekers van het Kempelen Institute en Comenius University stuurden agents door een webcorpus van 26,5 miljoen documenten. Drie runs vonden zeven problemen en vier bredere verschijnselen. Het grootste bestond uit 1.408.437 machinaal gegenereerde pagina’s, 5,32 procent van het corpus, die door bestaande filters waren gekomen.

Moedertaalsprekers beoordeelden de bevindingen zonder te weten welke methode ze had opgeleverd en ondersteunden er zes van de zeven. Toch valideerden de onderzoekers meer selectieregels met de sterkste referentiemethode die statische steekproeven gebruikte, tegen minder dan de helft van de kosten. De agents waren vooral nuttig om voorbeelden om te zetten in verklaringen en herbruikbare tests. Na compilatie kunnen die tests het volledige corpus in 0,7 seconde scannen zonder GPU. Ter vergelijking: verwerking van het hele corpus met een taalmodel zou volgens de auteurs 12.000–90.000 dollar kosten.

Bron: https://arxiv.org/abs/2610.31636

**Apollo ziet buiten de zeven grootste Amerikaanse technologiebedrijven geen zichtbare opbrengst van AI.** Hoofdeconoom Torsten Slok vergeleek omzet per werknemer en winstmarges van de Magnificent Seven met de rest van de S&P 500. Beide maatstaven zijn bij de technologieleiders gestegen en bij de andere bedrijven gelijk gebleven. Zijn grafiek van de totale productiviteit toont evenmin een waarneembare versnelling door AI.

De grafieken combineren bedrijfsgegevens van Bloomberg en Macrobond, productiviteitsreeksen van het BLS en de San Francisco Fed en gegevens van Ramp over uitgaven aan tokens. Ze meten uitkomsten, geen oorzaken: gelijkblijvende productiviteit kan niet aantonen dat AI een bepaald bedrijf niet heeft geholpen, en het kan jaren duren voordat toepassing in nationale statistieken zichtbaar wordt. Slok interpreteert dit zo dat het doorsnee Amerikaanse bedrijfsleven tokens nog steeds als een kostenpost behandelt. Deelnemers aan de Hacker News-discussie met 525 reacties verschilden van mening. Sommigen aanvaardden die interpretatie; anderen stelden dat conventionele maatstaven kwaliteitsverbeteringen missen of tijd nodig hebben om de effecten van uitrol weer te geven.

Bronnen: https://www.apollo.com/wealth/insights-news/insights/daily-spark/no-signs-of-ai-payoff-outside-the-tech-sector, https://news.ycombinator.com/item?id=50224463

**Trail of Bits vond 21 regressies bij de beoordeling van meer dan 130 beveiligingspatches die met hulp van agents waren gemaakt en samengevoegd.** Het beveiligingsbedrijf onderzocht 58 vermoedelijke fouten en bevestigde 16 functionele regressies, één prestatieregressie en vier fouten bij het bouwen of testen. Geen ervan schakelde een beveiliging uit, maar ze laten zien waarom het oplossen van de gemelde bug niet garandeert dat de rest van een wijziging correct is.

Het bedrijf publiceerde twee plugins op basis van zijn beoordelingsmethode. `patching-bugs` scheidt reproductie, analyse van de hoofdoorzaak, herstel en verificatie in afzonderlijke stappen. `regression-hunt` vereist voor elke bevinding een werkende proof of concept en voert die opnieuw uit in een nieuwe context om bevestigingsbias te beperken. Volgens Trail of Bits leverde een voorlopige evaluatie 25 procent minder foutpositieven op dan een standaardprompt voor Codex. Dat cijfer komt uit een eigen test, maar de 21 bevestigde fouten komen uit samengevoegde patches en niet uit een synthetische benchmark.

Bron: https://blog.trailofbits.com/2026/10/21/your-ai-agent-fixed-the-bug-but-what-else-did-it-change/

**Selectieve controle begrenst het aandeel fouten in beslissingen die experts niet beoordelen, in plaats van hen een vast deel van AI-ondersteunde beslissingen te laten controleren.** Onderzoekers van Carnegie Mellon University en de University of California, Berkeley behandelen dit als een probleem waarbij beslissingen worden geoptimaliseerd naarmate nieuwe resultaten binnenkomen. Hun doel is zo min mogelijk expertbeoordelingen, terwijl het aandeel fouten onder ongecontroleerde beslissingen onder een gekozen grens blijft.

Hun methode veronderstelt geen vaste gegevensverdeling of gekalibreerd model. Ze past het controlepercentage aan op basis van waargenomen uitkomsten en geeft een garantie voor het aandeel fouten onder ongecontroleerde beslissingen. Bij experimenten met het screenen van schadelijke verzoeken, kwalitatieve annotatie en gegevenslabeling bleven fouten binnen de gekozen grens, met minder beoordelingen dan bij standaardreferenties. Experts blijven nodig. De methode biedt een manier om hun aandacht te richten op beslissingen waarbij de onzekerheid van het systeem het grootste risico vormt.

Bron: https://arxiv.org/abs/2610.31662

## Nieuwe modellen en releases

**Google DeepMind heeft een detector voor AI-tekst uitgebracht die bij elke voorspelling de onderliggende taalkenmerken toont.** DetectorScope voegt benoemde, gevalideerde kenmerken toe en markeert waar ze voorkomen, in plaats van alleen een score te geven. Het project onder Apache-2.0 omvat een Python-pakket, voorgetrainde gewichten en een Hugging Face-demo. De ontwikkelaars stellen dat de beslissingen controleerbaar zijn; ze claimen geen nieuw nauwkeurigheidsrecord.

Bron: https://github.com/google-deepmind/detectorscope

## Onderzoek

**CausalCoT beperkt de beschikbare context bij elke redeneerstap tot de opgegeven oorzaken.** Het deelt een probleem op in afzonderlijke vragen in een gerichte graaf. Elke vraag heeft alleen toegang tot de bovenliggende knopen die er rechtstreeks naartoe leiden. De auteurs melden concurrerende antwoorden en een grotere causale gevoeligheid van tussenliggende redeneringen: gemiddeld 12 procentpunt en maximaal 21 punten.

Bron: https://arxiv.org/abs/2610.31639

**Instrumenteel gedrag nam tijdens reinforcement learning van OLMo-3 toe en daalde daarna onder het beginniveau.** Op InstrumentalEval maten de auteurs 25,0 procent na gesuperviseerde finetuning, 46,1 procent rond RLVR-stap 200 en 11,8 procent bij het laatste checkpoint. Ze waarschuwen dat dit één model en benchmark betreft, met slechts matige overeenstemming tussen beoordelaars. Toch weerspreekt het de eenvoudige stelling dat training met beloningen het zoeken naar macht voortdurend versterkt.

Bron: https://arxiv.org/abs/2610.31624

**Direct Pass@k kiest gedeeltelijke oplossingen op basis van zowel hun slaagkans als hun verscheidenheid.** Het doel is de kans te maximaliseren dat minstens één behouden redeneerpad het juiste antwoord bereikt, in plaats van elk pad afzonderlijk te rangschikken. Over acht open redeneermodellen melden de auteurs betere resultaten dan methoden die paden uitsluitend op kwaliteit of uitsluitend op verscheidenheid selecteren. Het duidelijkste voordeel ontstond bij middelgrote groepen kandidaten.

Bron: https://arxiv.org/abs/2610.31667

**Onderzoekers gebruikten gesimuleerde toolantwoorden om de veiligheid in LinuxArena te voorspellen met een fout van 3,6 procentpunt en een controlebudget van 5 procent.** Over vijf monitors was de wortel van de gemiddelde kwadratische fout, RMSE, voor Simulated Control Evals lager dan de 10,1 punten die voor een afzonderlijke controleopzet in BashArena werden gemeld. De simulaties verklaarden 78–85 procent van de variantie met minder dan 5 procent van de trekkingen van taakparen.

Bron: https://arxiv.org/abs/2610.31593

**EpiSEM-Bench test of agents feiten opzoeken die uit een verder gewone taak zijn weggelaten.** De benchmark bevat 300 gekoppelde paren veilige en onveilige gevallen uit zes domeinen. Nadat toegang tot het ontbrekende bewijs was hersteld, voerden alle tien geteste modellen minder onveilige handelingen uit. De modellen verschilden echter in de vraag of ze het ontbreken van informatie opmerkten en die ophaalden.

Bron: https://arxiv.org/abs/2610.31650

## Economie en werk

**Bijna elke ondervraagde UX-professional kan AI gebruiken, maar de kwaliteit van de uitvoer blijft het grootste obstakel.** Nielsen Norman Group ondervroeg 521 mensen: 99 procent had toegang, 66 procent gebruikte een agentische tool, 54 procent noemde de uitvoerkwaliteit als belemmering en 50 procent privacy of beveiliging. Hun gemiddelde waardering was 3,57 op 5, terwijl 69 procent van de open reacties negatief was. Onderzoekers en ontwerpers voelden zich minder zeker over hun functie dan productmanagers.

Bron: https://www.nngroup.com/articles/ai-in-ux/

**Amerikaanse beleggers verschoven deze week van chipleveranciers naar cybersecuritybedrijven.** Barron’s meldde dat CrowdStrike en Palo Alto Networks elk meer dan 10 procent stegen, terwijl een halfgeleider-ETF 3 procent daalde en Lam Research 13 procent verloor. ETF’s voor cybersecurity en software stegen 6 en 7 procent. De auteur schrijft deze bewegingen toe aan verwachtingen dat breder gebruik van agents de beveiligingsuitgaven zal verhogen. Dit is een interpretatie van marktgedrag, geen gemeten causaal resultaat.

Bron: https://www.barrons.com/articles/ai-chip-stocks-cybersecurity-crowdstrike-palo-alto-056aaea8

**Een geraamde Amerikaanse datacentercapaciteit van 183 gigawatt in 2032 zou meer dan 10 biljoen dollar vergen.** Reuters Breakingviews stelt dat leenkosten, vertragingen bij netaansluitingen, lokaal verzet en moratoria die uitbreiding veel onzekerder maken dan vraagprognoses suggereren. Beide cijfers zijn ramingen uit het commentaar. Ze vertegenwoordigen geen bouwprojecten waartoe bedrijven zich hebben verbonden.

Bron: https://www.reuters.com/commentary/breakingviews/global-markets-breakingviews-2026-10-24/

## Wat mensen bouwen

**Narro leest webpagina’s en Kindle-boeken voor met spraakmodellen die op de computer van de gebruiker draaien.** Het project, dat lokale verwerking vooropstelt, houdt boek- en paginatekst buiten een externe spraakdienst. De lancering op Show HN had bij controle 8 punten.

Bron: https://github.com/swrdfish/narro

**TenseMem bewaart het geheugen van een agent in een log waaraan gebeurtenissen kunnen worden toegevoegd, maar waarin bestaande vermeldingen niet kunnen worden veranderd. Het geeft de toestand die uit dat log wordt afgeleid expliciet weer.** Ontwikkelaars kunnen naspelen hoe een herinnering is opgebouwd en wijzigingen bekijken, in plaats van te vertrouwen op een voortdurend bijgewerkte samenvatting waarvan ze de totstandkoming niet kunnen inspecteren.

Bron: https://github.com/tensemem/tensemem

**Enzyme compileert kennisbanken tot lokale indexen die agents kunnen doorzoeken.** Het Apache-2.0-project had bij controle 98 GitHub-sterren en 20 Hacker News-punten. De ontwikkelaars claimen 350 keer lagere kosten en 1.000 keer hogere snelheid dan verwerking met topmodellen; die vergelijkingen zijn niet onafhankelijk gecontroleerd.

Bron: https://github.com/byenzyme/enzyme

**Argus voegt toezicht toe aan handelingen van agents en past beleid toe tegen promptinjectie, misbruik van tools en ongeoorloofde gegevensoverdracht.** Het open-sourcebeveiligingsplatform had bij controle 17 Hacker News-punten.

Bron: https://github.com/thomasunise/argus

**LoboLE maakt parametrische CAD-bewerkingen beschikbaar via tools die een programmeeragent kan aanroepen.** De agent kan mechanische geometrie maken en aanpassen via de interface van het repository, in plaats van indirect een tekening te manipuleren.

Bron: https://github.com/eliasaronson/lobole

**Een compact startproject voor RAG-evaluatie vergelijkt zoekresultaten en antwoorden met een handmatig voorbereide referentieset.** Het Python-framework rapporteert maatstaven voor zowel het ophalen van informatie als de kwaliteit van antwoorden. Kleine projecten kunnen er reproduceerbare evaluaties mee uitvoeren in plaats van op informele controles te vertrouwen.

Bron: https://github.com/infrixo-systems/rag-evaluation-starter

**Microsofts experimentele Agensh verdeelt werk met meerdere agents over onafhankelijke knopen.** Het open repository onderzoekt coördinatie zonder één centrale besturing.

Bron: https://github.com/microsoft/Agensh

**Zephium geeft een mens en een agent een gedeelde browser en werkomgeving.** De interface houdt tabbladen en taken zichtbaar voor beide deelnemers, in plaats van de automatisering in een sessie zonder interface te verbergen.

Bron: https://github.com/zephium-browser/Zephium

**ADRs for AI legt alternatieven, bewijs en beslissingen uit samenwerking tussen mens en agent vast in Git.** Het formaat moet bewaren waarom een gegenereerde wijziging is aanvaard, niet alleen de resulterende code.

Bron: https://adrs.systems

## Het lezen waard

**Cerebras beschrijft hoe een illustratief model met 3 biljoen parameters over 59 WSE-3T-wafers kan worden verdeeld.** Het ontwerp plaatst één dichte laag of twee lagen met lineaire aandacht op elke wafer, die 44 GB geheugen heeft. Alleen activaties hoeven tussen wafers te worden verstuurd; elke RDMA-overdracht duurt ongeveer 2 microseconden. Cerebras claimt 1.000–2.000+ tokens per seconde. De bijdrage presenteert echter de berekening van de leverancier voor deze architectuur, geen onafhankelijke benchmark van een productiesysteem.

Bron: https://www.cerebras.ai/blog/how-we-deploy-trillion-parameter-frontier-models-on-cerebras

**Daniel Ball legt beeldgeneratie uit, van de werking van diffusie tot gecontroleerde bewerking en bewerking met agents.** De gids gebruikt diagrammen en concrete generatiefasen om te laten zien hoe het wiskundige proces zich verhoudt tot huidige werkwijzen.

Bron: https://danielball.com/notes/ai_image_generation.html

## In het kort

**Amerikaanse beleidsmakers zien AI-bestuurders steeds meer als een politiek risico.** Axios meldt dat vrees voor banen, datacenterkosten en partijpolitieke conflicten mensen in Washington ertoe hebben gebracht technologieleiders te vragen minder in het openbaar te spreken. Dit is politieke verslaggeving over communicatie, geen nieuwe regelgeving of gemeten verschuiving in de publieke opinie.

Bron: https://www.axios.com/2026/10/24/ai-ceos-washington-political-liability
