+++
title = "Dagelijks AI-overzicht – 16 oktober 2026"
slug = "dagelijks-ai-overzicht-16-oktober-2026"
description = "De Federal Reserve hoort nu dat bedrijven minder aannemen na AI-productiviteitswinst. Een experiment met gameontwerp valt uit in het voordeel van agentteams, terwijl een geheugenstudie vindt dat modellen vaak antwoorden behouden die ze niet melden."
tags = ["research", "models", "business", "projects"]
date = 2026-10-16T03:58:25+02:00
draft = false
+++

## Belangrijkste nieuws

**Vijf Federal Reserve-districten hoorden dat AI-productiviteitswinst de personeelsbezetting of werving verminderde.** Het Beige Book van oktober zegt dat sommige bedrijven personeel lieten afvloeien via natuurlijk verloop, werving uitstelden of verwachtten minder banen te creëren na investeringen in AI. In juli meldde dezelfde nationale samenvatting alleen dat enkele districten AI meer gebruikten voor werving of productiviteit.

Het rapport is een kwalitatieve inventarisatie onder bedrijfscontacten, geen banentelling, en geeft geen sectortotaal. De districtspagina's beschrijven een stillere aanpassing dan massaontslagen: contacten in Chicago en Cleveland hadden minder personeel nodig, terwijl accountantskantoren in Dallas enkele starterscontracten uitstelden. Een uitzendbedrijf in Dallas nam ook recruiters aan nadat AI-agents in twee dagen meer dan 180 uur aan interviews hadden afgenomen. Dat laat zien dat uitrol tegelijk taken kan wegnemen en creëren.

Bron: https://www.federalreserve.gov/monetarypolicy/beigebook202610-summary.htm

**AI-agentteams versloegen menselijke producenten in een gameontwerpexperiment met 1.025 consumenten.** Een preprint meldt dat games ontworpen door teams van AI-agents hogere beoordelingen kregen dan games van menselijke producenten, onder wie professionals. Deelnemers betaalden ook niet meer voor werk dat als door mensen gemaakt was gelabeld.

Het resultaat is beperkter dan een algemene claim over creativiteit: het betreft één productcategorie in een gecontroleerde experimentele omgeving en het artikel heeft geen peerreview ondergaan. De spanning is toch concreet. Professionele ervaring beschermde de menselijke teams niet op de maatstaven van de studie, terwijl de verwachte meerprijs voor menselijk auteurschap uitbleef.

Bron: https://arxiv.org/abs/2610.18921

**Taalmodellen behielden vaak een doelitem in het werkgeheugen, ook wanneer ze onjuist antwoordden.** Onderzoekers testten 15 modellen met 70 miljoen tot 14 miljard parameters op interferentietaken. Aandachtskoppen selecteerden bij veel fouten nog steeds het doelitem en probes decodeerden het vrijwel perfect; onderdrukking van representaties van concurrerende items verbeterde de gevoeligheid van de modellen.

Dat wijst op een knelpunt bij het uitlezen in plaats van eenvoudig vergeten. De auteurs vergelijken het interferentiepatroon met het menselijke werkgeheugen, maar probes bewijzen niet dat een model kan gebruiken wat zij decoderen. Het werk biedt naast een observatie ook een causale interventie: het verzwakken van de identiteit van niet-doelitems veranderde het gedrag in de voorspelde richting.

Bron: https://arxiv.org/abs/2610.21176

**Meta bracht Muse Spark Open uit, een multimodaal mixture-of-experts-model met 816 miljard parameters.** Het model activeert ongeveer 42 miljard parameters per token, accepteert tot één miljoen tokens context en levert gewichten die in BF16 ongeveer 1,5 TB beslaan. Meta zegt dat twee M5 Ultra Mac Studios met elk 512 GB het kunnen draaien; Apples MLX-opstelling met vier machines haalde meer dan 36 tokens per seconde bij 8.192 tokens context.

“Open” heeft hier grenzen. Toegang is afgeschermd, commercieel gebruik boven een omzetgrens vereist een afzonderlijke overeenkomst en Meta had het beloofde veiligheidsrapport nog niet gepubliceerd. De release vergroot wat lokaal kan worden geïnspecteerd, maar alleen laboratoria en bouwers met ruime middelen kunnen dit als een gewoon desktopmodel behandelen.

Bronnen: https://research.meta.ai/blog/muse-spark-open, https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B, https://machinelearning.apple.com/research/mlx-distributed-inference

**De maker van een agentische decompiler met byteverificatie archiveerde het project na bezwaren uit de community.** Decomp.wtf liet een agent broncode reconstrueren en controleerde succes door opnieuw te compileren naar identieke bytes. De publieke repository bereikte 366 sterren voordat de auteur de dienst stopzette en de code archiveerde.

De episode koppelt een sterke technische test aan een sociale grens. Byte-identiteit maakt de uitvoer van het systeem uitzonderlijk eenvoudig te verifiëren, maar dezelfde vaardigheid verontrustte mensen van wie de binaire bestanden konden worden gereconstrueerd. Het archief bewaart de methode terwijl het gehoste product eindigt.

Bron: https://github.com/Decompile-It/decomp.wtf

## Nieuwe modellen en releases

**IBM's Granite Switch 4.1 schakelt één model tussen chat-, beslis-, veiligheids- en spraaktaken.** IBM combineert geactiveerde LoRA-adapters met een spraakencoder van 470 miljoen parameters in 8B- en 30B-releases onder Apache-voorwaarden; de benchmarkresultaten zijn zelf gerapporteerd. Bron: https://huggingface.co/ibm-granite/granite-switch-4.1-8b

**Nvidia publiceerde Nemotron 3.5 Rerank 8B voor meertalige tekst- en beeldzoekopdrachten.** De modelkaart omvat 34 teksttalen en 18 beeldtalen, maar de cijfers blijven afkomstig van Nvidia's eigen evaluatie. Bron: https://huggingface.co/nvidia/nemotron-3.5-rerank-8b

**Mistral bracht vier Timestral-voorspellingsmodellen uit met 5 miljoen tot 209 miljoen parameters.** Ze accepteren maximaal 32.768 eerdere observaties, voorspellen 1.024 stappen en geven 21 kwantielen; Mistral zegt dat de modellen de gekozen ranglijst aanvoeren en belooft een technisch rapport. Bron: https://mistral.ai/news/timestral

**Black Forest Labs bracht FLUX 3 Image Klein met 5,6 miljard parameters uit.** Het model met afgeschermde toegang ondersteunt generatie en bewerking met maximaal tien referentiebeelden, 4K-uitvoer en een INT8-modus voor GPU's met 8 GB; kwaliteitsclaims komen van het bedrijf. Bron: https://blackforestlabs.ai/flux-3-klein

**GitHub stopt op 16 november met enkele Copilot-modellen.** Opus 5, Opus 4.8 en GPT-5.6 Terra behoren tot de versies die worden vervangen, dus werkprocessen die op een vaste versie zijn ingesteld moeten vóór de deadline overstappen. Bron: https://github.blog/changelog/2026-10-15-upcoming-deprecation-of-selected-github-copilot-models-in-mid-november

## Onderzoek

**Vector-Pair Decomposition splitst modelgewichten in kleinere, interpreteerbare componenten.** Een interactief rapport van 124 pagina's gebruikt adversariële ablaties om die componenten te testen in plaats van alleen te vertrouwen op leesbare labels; bij de preprint verscheen geen publieke code. Bron: https://arxiv.org/abs/2610.20748

**Meer redeneren kan de correcte pragmatische gevolgtrekking van een model uitwissen.** De studie “Entertain, then Cancel” vindt dat modellen een impliciete betekenis vaak vroeg overwegen en vervolgens terugvallen op een letterlijke lezing naarmate het spoor langer wordt. Bron: https://arxiv.org/abs/2610.21204

**Methoden met latente redeneersporen delen niet één mechanisme.** In 21 configuraties kon inhoud van verborgen toestanden bij logische taken soms worden verwijderd, terwijl rekenen ervan afhankelijk bleef; decodeerbaarheid alleen bewees geen redeneren. Bron: https://arxiv.org/abs/2610.21182

**Nieuw redeneren helpt modellen aan een vastgelopen redeneerspoor te ontsnappen.** Een afzonderlijke aanroep verbeterde het volgen van bewijs met 29,9 tot 60,6 procentpunt, terwijl alleen hetzelfde spoor instrueren zichzelf te verifiëren dat niet deed. Bron: https://arxiv.org/abs/2610.20805

**Sterk verstoppertjesspel toonde geen theory of mind aan.** De preprint laat zien dat agents regelmatigheden kunnen benutten en goed kunnen presteren zonder een tegenstander in de menselijke betekenis te representeren. Bron: https://arxiv.org/abs/2610.17310

## Economie en werk

**Amazon heeft nu meer dan één miljoen robots naast 1,5 miljoen werknemers.** Het Robin-systeem verhoogde het taaksucces van 92,28 naar 93,73 procent, ongeveer 16.500 minder fouten per miljoen pogingen, volgens bedrijfscijfers die Ars Technica rapporteerde. Bron: https://arstechnica.com/ai/2026/10/inside-amazons-robotic-arms-race-and-what-it-means-for-the-future-of-human-work/

**Een arbeidssimulatie maakt AI-lonen tot de doorslaggevende aanname.** Het model verhoogt werkloosheid met 4,1 procentpunt wanneer AI-arbeid 70 procent van een menselijk loon kost en met 9,2 procentpunt bij gelijk loon. Dit zijn gesimuleerde uitkomsten, geen waargenomen banenverliezen. Bron: https://arxiv.org/abs/2610.14850

**Menselijke callcentermedewerkers converteerden ongeveer vier keer beter in de dataset van 14.000 gesprekken van één leverancier.** AI-agents veroorzaakten 700 procent meer gesprekken die zonder voortgang werden beëindigd, terwijl mensen 15 procent meer oproepen misten; de steekproef was niet willekeurig en komt van een bedrijf dat callcentersoftware verkoopt. Bron: https://boldagents.co/blog/call-center-jobs-declining-14000-calls-humans-outperform-ai

**Een modelondersteunde portering van de TypeScript-compiler naar Rust kostte ongeveer 24.000 dollar aan API-equivalent gebruik.** Theo Browne zegt dat eerdere modellen rond 84 procent voltooiing vastliepen, terwijl Opus 5.5 een vrijwel volledige portering produceerde die zijn benchmark 12,5 keer sneller draaide dan TypeScript 6. De benchmark en kostenberekening zijn niet onafhankelijk beoordeeld. Bron: https://www.theregister.com/devops/2026/10/15/24000-ai-experiment-ports-typescript-compiler-to-rust/5303409

## Prompttechnieken

**Vraag om de goedkoopste controle voor elk probleem dat een model meldt.** Een praktijkgebruiker laat het model de claim, exact bewijs, goedkoopste bevestigingstest, verborgen aannames en kosten van het negeren van het probleem teruggeven. Het patroon heeft geen benchmarkmeting, maar is volledig gespecificeerd. Bron: https://old.reddit.com/r/PromptEngineering/comments/1x5apk0/a_prompt_change_that_made_me_read_model_findings/

**Een prompt voor een tweede oordeel vraagt wat het model daadwerkelijk heeft geïnspecteerd.** Hij classificeert elke claim als ondersteund, tegengesproken, mogelijk of ongeverifieerd, eist exacte pagina's voor actuele feiten en eindigt met de ene volgende controle. Het patroon gaat niet vergezeld van metingen. Bron: https://old.reddit.com/r/PromptEngineering/comments/1x6r9s2/i_stopped_asking_ai_to_be_critical_and_started/

## Wat mensen bouwen

**Locals bundelt lokale inferentie op Apple-chips en slaat generatie over voor deterministische JSON.** De auteur mat 271 tokens per seconde tegenover 87 op een Qwen3.5 4B-werklast met acht verzoeken op een M2 Pro; de benchmark is van het project zelf. Bron: https://github.com/danielhanchen/locals

**PocketGPT zet een taalmodel met 30 miljoen parameters op een ESP32.** Het open project meldt 0,74 tot 1,41 tokens per seconde en benoemt openlijk onbetrouwbaar rekenen. Bron: https://github.com/roboflow/pocketgpt

**FileDig voegt lokale semantische bestandszoekopdrachten toe aan Windows.** De toepassing van 825 MB gebruikt EmbeddingGemma2 en zegt dat bestanden de machine nooit verlaten. Bron: https://github.com/fdatalab/filedig

**Earshot geeft programmeeragents via MCP lokale audio- en videoperceptie.** Het open project draait op de CPU; de nauwkeurigheids- en prestatiecijfers komen van de auteur. Bron: https://github.com/jooray/earshot

## Het lezen waard

**Nick Cammarata betoogt dat neurale netwerken netter zijn dan gangbare interpretabiliteit aanneemt.** Zijn Goodfire-essay van 65 minuten zegt dat bekende voorbeelden van polysemantische neuronen architecturale overloop en “recursieve generalisatie” weerspiegelen, geen willekeurige bundeling van concepten. Het is een werkhypothese, geen vaststaand resultaat. Bron: https://already-clean.goodfire.com/

**Een studie van 113.457 websites vond slechts twee llms.txt-bestanden met promptinjecties die instructies proberen te overschrijven.** Signals Corps vond 62.751 echte bestanden, terwijl 36 procent van de antwoorden HTML was; in een test met zes runs volgde Claude Code vier keer een fictief registratieverzoek. De auteurs verkopen agentbeveiligingssoftware. Bron: https://www.signalscorps.com/blog/llms-txt-instructions-to-ai-agents

**NVIDIA en AI4Bharat publiceerden hun proces voor 2,8 biljoen tokens in Indiase talen.** Het omvat 22 grondwettelijk vermelde Indiase talen en publiceert prompts, vertaalprocessen en kwaliteitscontroles, terwijl het corpus zelf nog moet verschijnen. Bron: https://huggingface.co/blog/nvidia/scaling-indic-pretraining

**Christian Schaller gebruikte Claude Code en vastgelegd USB-verkeer om een Linux-scannerdriver te bouwen.** Hij meldt een eerste scan binnen enkele uren en een vrijwel volledige driver binnen enkele dagen en publiceerde daarna het herbruikbare hardwareraamwerk. Ondertussen was onafhankelijk een compatibele SANE-commit opgenomen. Bron: https://blogs.gnome.org/uraeus/2026/10/15/aiandreverseengineerhardware/

## Hacker News

**De licentie en hardware van Muse Spark domineerden de communitydiscussie.** Reacties contrasteerden inspecteerbare gewichten met een afzonderlijke commerciële overeenkomst boven de omzetgrens van de licentie en een machinerekening ver boven een normaal werkstation. Hun prestatievergelijkingen waren informeel. Bron: https://news.ycombinator.com/item?id=45906238

## Reddit

**Gebruikers plaatsten Qwen3.8 Flash-metingen op RTX Pro 6000-hardware.** Gemelde decodeersnelheden varieerden van 108 tot 238 tokens per seconde bij verschillende engines en kwantisaties, dus de cijfers vormen geen gecontroleerde rechtstreekse vergelijking. Bron: https://old.reddit.com/r/LocalLLaMA/comments/1x5teff/

## YouTube

**Stanford publiceerde een CME295-lezing over de moderne trainingsketen voor taalmodellen.** De Engelstalige sessie volgt het traject van data en optimalisatie naar natraining en inferentiediensten. Bron: https://www.youtube.com/watch?v=1Q5o0xR3L0M

**Jellyfish zegt dat AI het aantal gemergde pull requests per ingenieur met 43 procent verhoogde en de kosten per pull request met 26 procent verlaagde.** De Engelstalige presentatie rapporteert observationele klantdata, geen gerandomiseerd experiment. Bron: https://www.youtube.com/watch?v=0NW5CxX7D2g

## In het kort

**De Amerikaanse Federal Trade Commission opende een formeel onderzoek naar agentincidenten bij OpenAI en Anthropic.** Ars Technica meldt dat de instantie informatieverzoeken van meer dan 50 pagina's verstuurde; het onderzoek steunt op anonieme bronnen en is nog geen handhavingsbevinding. Bron: https://arstechnica.com/tech-policy/2026/10/ftc-opens-formal-investigation-into-openai-anthropic-over-ai-agent-incidents/

**Anthropic gaf zes METR-onderzoekers toegang op werknemersniveau voor een evaluatie.** Het zegt dat de beoordelaars zonder veto mogen publiceren, afgezien van beperkte weglakkingen; de onafhankelijkheid van de regeling is pas na publicatie meetbaar. Bron: https://www.anthropic.com/news/more-transparency-for-frontier-ai

**TSMC verhoogde zijn investeringsbandbreedte voor 2026 naar 60–64 miljard dollar.** De chipfabrikant zegt dat de vraag boven het aanbod blijft en onderzoekt Amerikaanse stroom- en bouwcapaciteit voor datacenters. Bron: https://investor.tsmc.com/english/quarterly-results/2026/q3

## Zakelijk in het kort

**Cohere stelde voor agentbeveiligingsbedrijf AISLE over te nemen.** Bron: https://cohere.com/news/cohere-aisle

## Om in de gaten te houden

GitHubs geselecteerde Copilot-modellen stoppen op 16 november. Mistral zegt dat er nog een technisch Timestral-rapport komt en Meta zegt een Muse Spark-veiligheidsrapport te zullen publiceren.
