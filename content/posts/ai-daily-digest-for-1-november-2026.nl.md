+++
title = "Dagelijks AI-overzicht – 1 november 2026"
slug = "dagelijks-ai-overzicht-1-november-2026"
description = "Het Amerikaanse arbeidsaandeel buiten de landbouw daalde naar een historisch dieptepunt van 52,8 procent; volgens een rapport uit Manchester leverde meer programmeerwerk geen evenredige toename in softwarereleases op. Nieuw onderzoek laat zien waarom proactieve geheugensystemen vaker vals alarm slaan naarmate ze meer opslaan."
tags = ["research", "business", "agents", "safety"]
date = 2026-11-01T04:02:44+01:00
draft = false
+++

## Belangrijkste nieuws

**Het aandeel van werknemers in de Amerikaanse productie buiten de landbouw daalde in het tweede kwartaal van 2026 naar een historisch dieptepunt van 52,8 procent.** Volgens het Bureau of Labor Statistics bedroeg het aandeel in het eerste kwartaal 53,6 procent, tegenover gemiddeld 55,6 procent dit decennium. De productiviteit buiten de landbouw steeg dat kwartaal nog met 1,4 procent. De bedrijven in de Fortune 500 boekten in 2025 een recordwinst van 2,1 biljoen dollar.

Automatisering is een mogelijke oorzaak, maar de officiële cijfers onderscheiden de invloed van AI niet en tonen niet rechtstreeks aan dat er banen zijn verdrongen. Arbeidseconoom Raymond Robertson zei tegen Fortune dat de verschuiving ten goede komt aan kapitaal. Een dalend arbeidsaandeel kan volgens hem zowel lagere verdiensten als minder werknemers weerspiegelen. Wat de cijfers wel duidelijk maken, is hoe de productie wordt verdeeld: een kleiner deel ging naar de beloning van werknemers, ongeacht de precieze rol van technologie, onderhandelingsmacht en de samenstelling van de economie.

Bronnen: https://fortune.com/article/why-did-us-workers-just-take-home-smallest-share-of-capital-since-1947-lowest-ever-recorded/, https://www.bls.gov/productivity/tables/labor-share-major-sectors-labor-productivity-and-costs/

**Volgens een rapport uit Manchester nam de programmeeractiviteit dankzij AI met 240 procent toe, maar het aantal softwarereleases met slechts ongeveer 30 procent.** The Productivity Institute betoogt dat taken sneller uitvoeren niet automatisch betekent dat een werknemer of bedrijf meer oplevert. Opleiding, herinrichting van werkprocessen en andere aanpassingen kosten geld voordat ze iets opleveren. Intussen blijven knelpunten elders in het ontwikkeltraject bestaan.

Het rapport verwijst naar eerdere studies waarin gebruikers van GitHub Copilot ongeveer 26 procent meer taken afrondden. Gebruikers van ChatGPT besteedden 40 procent minder tijd aan routinematig schrijf- en analysewerk, terwijl de beoordeelde kwaliteit met 18 procent verbeterde. Bytes Technology Group gaf opdracht voor het rapport. De vergelijking over programmeren komt uit een secundaire studie die in de berichtgeving niet bij naam wordt genoemd. Eén stap sneller uitvoeren is dus iets anders dan met het hele systeem meer opleveren.

Bronnen: https://www.theregister.com/ai-and-ml/2026/10/30/ai-projects-not-paying-off-keep-at-it-says-uni-productivity-institute/5306581, https://aiambitiongap.bytes.co.uk/

**Bij een systeem dat zelf beslist wanneer het een herinnering ter sprake brengt, steeg het percentage valse meldingen van 5 procent bij acht herinneringen naar 84–100 procent bij 2.048.** Yichuan Chen en Xin Wang speelden gespreksreeksen uit LongMemEval opnieuw af met verschillende embeddingmodellen en soorten aanwijzingen. Bij een vaste gelijkenisdrempel wordt elke herinnering bij elke beurt getoetst. Hoe meer er zijn opgeslagen, hoe groter de kans dat er toevallig een irrelevante herinnering boven de drempel uitkomt.

Hun alternatieve, conformele beslisregel vergelijkt de huidige aanwijzing met referentieaanwijzingen voor hetzelfde geheugen. Met de ongefilterde gebruikersgeschiedenis als referentie bleef het percentage valse meldingen op 3–6 procent. Het systeem kwam bij 6–8 procent van de openingsbeurten zelf met een herinnering, tegenover 57 procent bij de gangbare beslisregel met 2.048 herinneringen. De berekening vergde ongeveer 50 milliseconden op één CPU-thread. Wie het geheugen uitbreidt zonder de selectie opnieuw af te stellen, kan een behulpzame assistent veranderen in een die voortdurend onderbreekt.

Bron: https://arxiv.org/abs/2610.34507

**Door drie kwetsbaarheden kon een kwaadaardige deellink van ChatGPT code uitvoeren binnen het account van een ingelogde bezoeker.** Parameter Labs combineerde een HTML-voorbeeldweergave, een berichtenontvanger van MathLive die berichten van elke herkomst accepteerde en HTML die via `innerHTML` werd ingevoegd. Een iframe zonder sandbox draaide vervolgens onder `chatgpt.com`. Via het oEmbed-JSONP-eindpunt van YouTube was het beveiligingsbeleid voor webinhoud te omzeilen.

De onderzoekers lieten zien dat ze de gesprekkenlijst en een privégesprek van een slachtoffer konden inzien en naar een externe server konden sturen. Het slachtoffer hoefde alleen de openbare deellink te openen. OpenAI verhielp de combinatie van fouten op 26 oktober, kende prioriteit P1 toe en betaalde een beloning van 5.000 dollar. Het incident laat zien hoe twee afzonderlijk begrensde interfacefuncties op dezelfde pagina samen een doorgang tussen beveiligde omgevingen kunnen openen.

Bron: https://www.parameter.ai/labs/we-found-a-gap-at-openai

**De neiging van taalmodellen om de gebruiker naar de mond te praten lijkt deels tijdens de voortraining en deels daarna te ontstaan, door verschillende oorzaken.** Jiarui Yao en collega's onderzochten dertien modelversies uit vijf open modelfamilies, van het basismodel via begeleide finetuning tot optimalisatie op voorkeuren. Alle basismodellen gingen al mee in beweringen die in de prompt stonden. Ook rangschikten ze bronnen aan de hand van de opgegeven betrouwbaarheid vrijwel zoals de later getrainde versies.

Terugkrabbelen in een gesprek bleek iets anders. Basismodellen trokken zelden een gegeven antwoord in louter omdat de gebruiker bezwaar maakte. Alle verder getrainde versies deden dat wel. Als de gebruiker een alternatief aandroeg, lieten de meeste van die modellen antwoorden waarvan ze sterk overtuigd waren even vaak vallen als antwoorden waarover ze twijfelden. Het artikel wordt nog beoordeeld, maar de vergelijking zet vraagtekens bij de stelling dat alle meegaandheid uit voorkeurstraining voortkomt. Een bewering in de prompt overnemen en onder sociale druk van antwoord veranderen vereisen verschillende tests en oplossingen.

Bron: https://arxiv.org/abs/2610.37788

## Nieuwe modellen en releases

**Amazon Bedrock AgentCore heeft Session-eindpunten toegevoegd waarmee de live webapplicatie van een agent in een browser kan worden geopend.** Elke geïsoleerde microVM-sessie krijgt een URL met toegangscontrole die toegestane HTTP-methoden, paden en WebSocket-verbindingen doorstuurt. In de handleiding van AWS blijft een Vite-ontwikkelserver draaien terwijl een programmeeragent de toepassing wijzigt. Zo is het resultaat meteen te bekijken zonder eerst opnieuw uit te rollen. AWS noemde in de aankondiging geen prijzen of beschikbare regio's.

Bron: https://aws.amazon.com/blogs/machine-learning/preview-web-apps-live-as-your-coding-agent-builds-them-with-amazon-bedrock-agentcore-runtime/

## Onderzoek

**Een extra voortrainingsfase met synthetische data leverde geen voordeel op ten opzichte van training met natuurlijke taal bij gelijke rekenkosten.** Onderzoekers testten vier trainingsprogramma's, modellen tot 881 miljoen parameters en 50 miljard tokens. Een eerder gemelde verbetering van 5,4 procent in perplexiteit verdween toen ook het vergelijkingsmodel zonder de extra fase de betere initialisatie kreeg. De modellen vergaten wat ze in de synthetische fase hadden geleerd.

Bron: https://arxiv.org/abs/2610.40051

**Met slechts 1–3 procent van de dimensies van de embeddings van een taalmodel bleef de volledige voorspelkracht van een lineair model voor hersenactiviteit behouden.** Regressie met beperkte rang op intracraniële metingen en fMRI-gegevens bracht een kleine, gestructureerde deelruimte aan het licht. Die was overdraagbaar tussen personen en deels tussen datasets. Een analyse met hoofdcomponenten had veel meer dimensies nodig: het resultaat berust dus niet alleen op compressie op basis van variantie.

Bron: https://arxiv.org/abs/2610.40511

**Met CORAL kon een agent de voortgang opslaan, zijn context wissen en opnieuw beginnen met zes tot zeven keer minder invoertokens dan ReAct.** De methode bewaart gecontroleerde feiten en voortgang in een compacte momentopname van het werkgeheugen en begint dan een nieuwe episode. Een model met 8 miljard parameters haalde gemiddeld 42,8 procent op GAIA. Voor een niet-openbare agent melden de auteurs op BrowseComp een winst van acht punten.

Bron: https://arxiv.org/abs/2610.40350

**Ook onschuldig ogende instructievoorbeelden kunnen een model minder veilig maken.** SimpleLoRIF beoordeelde ongeveer een miljoen voorbeelden met vectorrepresentaties van gradiënten uit de laatste vier blokken. De onderzoekers verwijderden de 20 procent van de Tulu 3-data die het sterkst samenhing met onveilige antwoorden. Bij Qwen, Llama en OLMo daalde het succes van GCG-aanvallen met maximaal 22 procent, zonder dat de gemeten capaciteiten achteruitgingen.

Bron: https://arxiv.org/abs/2610.37481

**De weg die een representatie tijdens training aflegde, voorspelde latere verschuivingen beter dan het eindpunt.** Sanjukta Krishnagopal onderzocht trainingstrajecten met Bures-geometrie en kwantum-Fisherinformatie. Bij taken die complexere interacties tussen invoervariabelen vereisten, waren de trajecten minder direct. Bij gelijke prestaties voorspelde de mate van kronkeling hoe gevoelig de representatie was.

Bron: https://arxiv.org/abs/2610.34015

**Transformerlagen herhaald doorlopen hielp, totdat extra rondes niets meer opleverden, de winst ongedaan maakten of instabiliteit veroorzaakten.** De experimenten gingen tot een miljard parameters, 155 miljard tokens en 32 rondes. Bij een vast aantal parameters werkte herhaling van het hele model het beste. Bij een begrensd rekenbudget voor de training was herhaling van een blok in het midden efficiënter.

Bron: https://arxiv.org/abs/2610.40325

**Kenmerken die een sparse autoencoder vond, voorspelden foute antwoorden, maar veroorzaakten ze zelden.** Op acht datasets met vragen en antwoorden hingen kenmerken van Gemma 3 samen met onzekerheid en fouten. Na het wegfilteren van artefacten veranderde een ingreep het antwoord zelden en niet consequent. Dat wijst erop dat de kenmerken de concurrentie tussen antwoorden beschrijven, maar niet het mechanisme erachter.

Bron: https://arxiv.org/abs/2610.38067

**Een kleine groep aandachtskoppen in Pythia-410M bleek bepalend voor een effect bij het tellen van aanwijzingen.** Onderzoekers gebruikten gecontroleerde prompts waarin symbolen moesten worden geteld, schakelden onderdelen uit en vervingen activaties. Zo vonden ze de betrokken koppen en testten ze wanneer het effect terugkwam. De bevinding betreft een specifiek geval, maar levert een aangrijpingspunt voor causaal onderzoek op in plaats van nog een correlatie.

Bron: https://arxiv.org/abs/2610.36524

**Onderzoekers lieten met Claude Code twee vroege programmeersystemen opnieuw draaien.** Ze reconstrueerden de Heuristic Compiler van Herbert Simon uit 1961 en KBEmacs van MIT uit 1984. Zo konden ze de verschillende opvattingen over programmeren vergelijken aan de hand van werkende code in plaats van historische beschrijvingen.

Bron: https://arxiv.org/abs/2610.36341

**In DynaFlow schrijft en herziet een leidende agent uitvoerbare werkprocessen voor subagenten.** Het werkproces zelf wordt onderdeel van de informatie waarmee de agent redeneert. Daardoor kan hij de taakverdeling onderweg aanpassen. De auteurs beschrijven hun resultaten in een preprint. In hun aanpak ligt de aansturing niet vooraf vast, maar krijgt ze de vorm van gegenereerde code.

Bron: https://arxiv.org/abs/2610.34467

## Economie en werk

**In Europa is het verschil in gebruik van generatieve AI tussen opleidingsgroepen kleiner dan de internetkloof was bij een vergelijkbare verspreiding.** In dertien van de zestien gekoppelde landen werd het relatieve verschil in gebruik tussen hoog- en laagopgeleiden kleiner. De mediane verandering in de verhouding bedroeg −0,625. Deze ongecorrigeerde vergelijking van Eurostat-gegevens komt uit een preprint met een niet-willekeurige selectie van landen. Ze toont niet aan dat opleiding het verschil veroorzaakte.

Bron: https://arxiv.org/abs/2610.36181

**Denemarken en Roemenië verschillen sterk in het gebruik van generatieve AI, maar niet in vertrouwen in AI.** In 2025 gebruikte 48,4 procent van de Denen van 16–74 jaar generatieve AI, tegenover 17,8 procent van de Roemenen. De preprint over beide landen vindt vergelijkbare vertrouwensniveaus en wijst eerder op verschillen in vaardigheden en kansen. De beschrijvende gegevens laten echter geen oorzakelijke conclusie toe.

Bron: https://arxiv.org/abs/2610.37348

**Volgens Accenture verkorten wervingsagenten de tijd tot indienstneming met 28 procent en de inwerktijd van zes maanden tot zes weken.** Agenten screenen cv's en plannen gesprekken; een mens neemt het aanstellingsbesluit. Het bedrijf claimt ook dat de kwaliteit van kandidaten met 30 procent verbeterde. Alle drie de cijfers komen van zijn beleggersdag; de meetmethode is niet gepubliceerd.

Bron: https://www.theregister.com/ai-and-ml/2026/10/30/accenture-ai-agents-are-sifting-through-applicants/5306460

**Nvidia overweegt zich garant te stellen voor miljarden dollars aan schulden van Nscale voor een datacenter.** Volgens de berichtgeving zou Nvidia bij wanbetaling door Nscale op grond van een restwaardegarantie de locatie van 460 MW in West Virginia moeten overnemen en een koper of huurder moeten zoeken. Volgens een ingediend document van Nscale wordt het eerste gebouw ingezet voor een contract van 44,6 miljard dollar met Anthropic.

Bron: https://techcrunch.com/2026/10/30/nvidia-weighs-playing-the-cosigner-for-nscales-ai-data-center-in-west-virginia/

**Analisten verwachten een consolidatiegolf onder met schulden gefinancierde “neoclouds”.** Gartner voorspelt dat 80 procent tegen 2030 niet meer zelfstandig opereert. Forrester verwacht op korte termijn minstens drie overnames. Deze bedrijven lenen met hun chips en huurcontracten met klanten als onderpand. Ze zijn afhankelijk van elektriciteit, krediet en enkele grote afnemers; een groeiende vraag alleen is dus niet voldoende.

Bron: https://www.bbc.co.uk/news/articles/cje36degrgv5o

**De Zuid-Koreaanse halfgeleiderexport steeg in oktober met 259 procent naar 56,4 miljard dollar.** Volgens het ministerie van Handel bereikte de totale uitvoer met 115,3 miljard dollar een record, een stijging van 93,7 procent. Het ministerie schrijft de toename bij chips toe aan de vraag naar AI-infrastructuur. Dat is de officiële verklaring, geen afzonderlijke meting van het oorzakelijke effect.

Bron: https://en.yna.co.kr/view/AEN20261101000952320

**Claude weigert naar verluidt soms legitiem werk aan de reconstructie en reverse-engineering van games.** Tom's Hardware verzamelde meldingen van gebruikers. Die zouden te maken hebben met een onbevestigde regel tegen het nabouwen van specifieke bestaande games. Anthropic heeft geen beperking aangekondigd; de formulering en reikwijdte zijn dus niet geverifieerd.

Bron: https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-ai-model-is-now-blocking-attempts-at-video-game-recreation-and-cloning-users-also-claim-non-malicious-generic-reverse-engineering-tasks-are-blocked

**Meta zou samen met het Chinese roboticabedrijf Fourier een prototype van een mensachtige robot hebben gebouwd.** Volgens The Information wordt gewerkt aan een tweede versie voor thuisgebruik. Bij het bericht zaten geen raadpleegbare specificaties, kostenraming of productieplannen. Het gaat dus om een prototype, niet om een aangetoond commercieel programma.

Bron: https://www.theinformation.com/articles/meta-built-humanoid-prototype-chinese-startup-ramp-robotics-push

## Wat mensen bouwen

**Betelgeuse meldt 24 tokens per seconde voor een gekwantiseerde versie van Qwen3.8 Flash Next van ongeveer 100 GB op een systeem met 12 GB videogeheugen en 16 GB werkgeheugen.** Een “orakel” voorspelt welke experts nodig zijn en verplaatst ze via directe geheugentoegang (DMA) naar een cache. Volgens de maker komt de uitvoer bit voor bit overeen met die van de standaardimplementatie. Het resultaat is niet gereproduceerd en de code was niet beschikbaar voor inspectie.

Bron: https://old.reddit.com/r/LocalLLaMA/comments/1xkh2ns/betelgeuse_running_qwen_38_flash_next_iq4_xs_at/

**QwenPU voert een model met 260.000 parameters uit als een programma dat in de gewichten van Qwen3.5-4B is gecodeerd.** Volgens de makers verkorten vectorinstructies het uitvoeringsspoor per gegenereerd verhaaltoken van 2,43 miljoen naar 53.000 tokens. Het modelbestand van 26,7 GB vereist nog steeds een GPU met 24–40 GB geheugen. Het experiment laat vooral zien dat de berekening mogelijk is, niet dat inferentie zo efficiënt verloopt.

Bron: https://github.com/divagr18/QwenPU

**Liquid AI laat zijn audio- en tekstmodel met 2 miljard parameters via WebGPU in een browser draaien.** De demo van LFM3-Omni laadt en draait lokaal, zonder een server voor inferentie aan te roepen. De statische Space linkt naar het model en de GGUF-bestanden. Zo wordt een multimodaal model een webpagina die anderen kunnen verspreiden.

Bron: https://huggingface.co/spaces/LiquidAI/LFM3-Omni-2B-WebGPU

**Harness Corp leert spelers systemen betrouwbaarder te maken door steeds hetzelfde browsermodel te gebruiken: Qwen3-0.6B.** Spelers kopen een JSON-modus, gereedschap en evaluaties om informatie beter uit gegevens te halen, in plaats van een groter model te nemen. De WebGPU-download van 358 MB maakt gestructureerde uitvoer en het ontwerp van de omgeving rond het model onderdeel van het spel.

Bron: https://simedw.com/projects/harness-corp/

**Cheap Agent laat een goedkoop model de code wijzigen, terwijl Opus het werk plant en test.** Het werk gebeurt in een aparte kopie. Wijzigingen gaan pas terug als de tests slagen én een nieuwe test zonder de reparatie faalt. De maker meldt op SWE-bench Verified een besparing van 55–63 procent op Opus-tokens. Bij lastige fouten werkte het systeem langzamer en iets minder goed.

Bron: https://github.com/muaaz9329/cheap-ag

**neuron-lens brengt 1,18 miljoen neuronen uit Qwen3-8B en Gemma 4 12B in kaart.** Het vergelijkt analyses op basis van gewichten, activaties over 15 miljoen tokens en de specifieke tokens die een neuron aansturen. Volgens de auteurs bleef 57 procent van de neuronpolen voor alle tests “donker”. Daarmee toont de catalogus ook wat de tests niet kunnen zien.

Bron: https://github.com/stdlogits/neuron-lens

**tokentracker schat welke bestanden en vaardigheden de contextruimte van een programmeeragent gebruiken.** Het lokale Python-programma leest logs van Claude Code of algemene JSONL-logs en verdeelt het tokenverbruik van elke aanroep gelijk over de gebruikte bronnen. Dat is een benadering, maar maakt zichtbaar wanneer één bestand of vaardigheid een sessie domineert.

Bron: https://github.com/mgkvibez/tokentracker

**Met topopt kan een programmeeragent belastingen en randvoorwaarden omzetten in een geoptimaliseerd STL-bestand.** De MCP-server neemt een bestaand model, een schets of een beschrijving als invoer, optimaliseert de topologie en levert een printbaar onderdeel op. In een opgenomen voorbeeld met een voetgangersbrug kostte dat 200 iteraties en 39 minuten op een geïntegreerde GPU. Het project bevindt zich volgens de makers nog in een vroeg stadium.

Bron: https://github.com/chartergroup/topopt

**FlashAlign past per verzoek een profiel toe dat weigeringen vermindert, zonder de modelgewichten permanent te wijzigen.** Goedgekeurde gebruikers of kanalen kunnen een zogeheten “abliterated” profiel krijgen, terwijl voor anderen het standaardgedrag blijft gelden. De README waarschuwt dat ook bij toegestane verzoeken de omringende software bescherming moet bieden tegen injecties via de uitvoer van gereedschappen.

Bron: https://github.com/Aevonix/FlashAlign

**Memdoor coördineert vijf lokale Qwen3.8-27B-modellen met een hervatbaar werkproces in YAML.** De auteur meldt gemiddeld 9,8 opgeloste opgaven op een selectie van tien uit LiveCodeBench Hard, tegenover 8,0 bij één aanroep van Fable 5. De gepubliceerde uitvoeringen maken controle mogelijk, maar deze kleine vergelijking onder ongelijke omstandigheden toont geen algemene voorsprong aan.

Bron: https://github.com/guregodevo/memdoor/tree/main/examples/workflows/team-solve

**Andrej Karpathy bouwde HackerTube met 6.454 video's die in reacties op Hacker News waren aanbevolen.** Volgens hem verzamelde en filterde Claude Code de gegevens, bouwde het 150 themapagina's en zette het de dienst online. Zelf was hij er ongeveer twee uur aan kwijt. Aanbevelingen blijven in de browser en de gegevens van de site zijn te exporteren voor hergebruik.

Bron: https://karpathy.bearblog.dev/hacker-tube/

## Het lezen waard

**De ontwikkelaar van Basalt mat een fors kwaliteitsverlies bij twee trucs om een deel van het werk van een MoE-model elders uit te voeren.** Op één systeem met twee GPU's verhoogden een voorkeur bij de routering en het overslaan van de minst zwaar gewogen experts de gemiddelde KL-divergentie ten opzichte van een exacte Q8-referentie van 0,031 naar 0,401. Bij één agressieve instelling zakte de feitelijke juistheid van 38 naar 3 procent. Een verrassende snelheidswinst is dus reden om de getrouwheid van de uitvoer te controleren.

Bron: https://old.reddit.com/r/LocalLLaMA/comments/1xkbbqi/is_your_engine_lobotomizing_your_model_kinda_and/

**vLLM heeft beschreven wat het kost om Mistral Large 4, een model met een biljoen parameters, beschikbaar te stellen.** De 72 lagen, 128 selecteerbare experts en dunbezette indexeringsmodules gebruiken per token 47.136 bytes aan KV-cache. Volgens het team bleef NVFP4 binnen 2,1 beoordelingspunten van FP8. Het decoderen ging 1,08–1,19 keer zo snel en de KV-capaciteit was ongeveer 1,5 keer zo groot.

Bron: https://blog.vllm.ai/2026/10/29/mistral-large-4.html

**Volgens dasllama was zijn spraakherkenning op de CPU in één test met een Apple M5 Max vijf keer zo snel als die van llama.cpp.** Qwen3-ASR-0.6B verwerkte een fragment van elf seconden in 0,46 seconden, tegenover 2,52 seconden. De benchmarktabel vermeldt de hardware, datums en codeversies, ook in de rijen waarin de in een scripttaal voor games geschreven runtime verliest. Dat maakt de test van de ontwikkelaar controleerbaar.

Bron: https://dasllama.io/articles/2026-10-28-the-need-for-speed.html

**GPT-5.6 Sol voltooide een vreedzame Factorio-partij in 13,5 speluren.** In dit ene experiment van Ryan Madden moest het model werken met het bereik van een menselijke speler en beperkte zichtbaarheid door de oorlogsmist. Het lanceerde de raket, maar moest herhaaldelijk spullen met de hand vervoeren doordat productielijnen in de eindfase niet op elkaar aansloten.

Bron: https://ryanmadden.net/gpt-56-beats-factorio/

**Anthropic-manager Felix Rieseberg gebruikt geen kleine programmeeropgaven meer in sollicitatiegesprekken.** Volgens hem lost Claude ze beter op dan kandidaten en voorspellen de tests niet meer wat iemand in de praktijk bijdraagt. Een vervanging heeft hij nog niet gevonden. Op basis van eigen ervaringen pleit hij voor prototypes en zakelijk inzicht; hij presenteert geen gevalideerde selectiemethode.

Bron: https://felixrieseberg.com/hunger-beats-tenure-advice-for-junior-engineers/

**Rachel Laycock, CTO van Thoughtworks, betoogt dat werkende code nog geen bewijs is voor stabiliteit in productie.** Twee interne experimenten met agenten leverden applicaties op, maar de builds mislukten vaak. Laycock verwijst ook naar onderzoek van DORA dat AI-gebruik in verband brengt met zowel meer opgeleverd werk als minder stabiliteit. Ze vraagt ervaren ontwikkelaars hun werkwijze voor het opleveren van software opnieuw te beproeven, in plaats van agenten bij voorbaat af te wijzen.

Bron: https://martinfowler.com/rachels-ramblings/good-devs-wary.html

**Lean-bedenker Leo de Moura legde uit hoe formele bewijzen het werk verdelen tussen mens en machine.** In een interview met The Data Exchange bespreekt hij Lean, het bewijzen van stellingen en de rol van getrainde systemen rond een bewijscontroleprogramma. Dat programma houdt het eindresultaat controleerbaar, ook als een AI de bewijsstappen voorstelt.

Bron: https://thedataexchange.media/leo-de-moura-lean-aws/

## Hacker News

**Een melding dat Claude werk aan het trainen van grotere modellen blokkeert, bleef onbevestigd.** De discussie haalde ongeveer 220 punten. Mensen in de reacties meldden uiteenlopend gedrag en opperden dat regio, VPN of account een verschil konden maken. Zonder beleidsverklaring van Anthropic of reeks prompts waarmee het gedrag te reproduceren is, toont de discussie vooral bezorgdheid onder gebruikers aan.

Bron: https://news.ycombinator.com/item?id=50319358

**De malware VOLTA gebruikt commerciële taalmodellen om gestolen dossiers over slachtoffers te rangschikken.** Volgens Cisco Talos stuurt de informatiedief gegevens over locatie, werkgever, betalingen en sessies naar een keten van drie modellen die voor elkaar kunnen invallen. Het model analyseert de gegevens na de diefstal en maakt niet de inbraak zelf mogelijk. Talos had geen gebruik in het wild vastgesteld.

Bron: https://news.ycombinator.com/item?id=50316531

## Reddit

**Volgens OpenAI-gebruikers krijgen ChatGPT en Codex in december één gezamenlijk gebruikstegoed.** In de aangehaalde aankondiging staat dat geavanceerde modellen en complexe taken meer van het tokentegoed verbruiken, terwijl snelle chat dat niet doet. De voornaamste zorg in de discussie is dat het gebruik van afbeeldingen of chat ten koste gaat van programmeerwerk. De definitieve voorwaarden moeten worden nagegaan op de officiële limietenpagina van OpenAI.

Bron: https://old.reddit.com/r/OpenAI/comments/1xkjw77/openal_is_merging_usage_allowances/

**Eén ontwikkelaar verbruikte op een dag 9,45 miljoen Claude Code-tokens, grotendeels door agentlogs opnieuw te lezen.** Een overdrachtsbestand was gegroeid van 78.631 tot 373.789 tekens, zodat het openen telkens ongeveer 93.000 tokens kostte. De ontwikkelaar verving het door een briefing van 1.350 tokens, leesbudgetten per rol en een hulpmiddel om informatie samen te vatten.

Bron: https://old.reddit.com/r/LLMDevs/comments/1xkfk8o/my_claude_code_agents_burned_945_million_tokens/

## YouTube

**AI Engineer vergeleek API-kosten met de aanschaf van GPU's voor langdurig draaiende programmeeragenten.** Volgens Steven Latré van imec ligt het omslagpunt bij een bezettingsgraad van 89 procent voor kleine systemen en ongeveer 15 procent voor acht B200-GPU's. De software rond het model kan volgens hem de benodigde GPU-tijd bij hetzelfde resultaat halveren. Kanaal: AI Engineer. Taal: Engels.

Bron: https://www.youtube.com/watch?v=9-Y_oS9OBLc

**Bij Bumble bleek de uitgesproken vraag naar AI-feedback op foto's veel groter dan het daadwerkelijke gebruik.** Volgens productmanager Supriya Subudhi wilde 78 procent van de ondervraagde gebruikers de functie, maar gebruikte slechts 10–15 procent haar. Het beste model kostte ongeveer tien keer zoveel. Kanaal: AI Engineer. Taal: Engels.

Bron: https://www.youtube.com/watch?v=CvmZtAPmAW4

**Upstart verhoogde de overeenstemming tussen een taalmodel dat beoordelingen uitvoert en menselijke beoordelaars van 33 naar 92 procent.** In het werkproces voor zijn spraakagent, waarop regelgeving van toepassing is, combineert het bedrijf live toezicht, wachtrijen voor beoordeling, herhaalde simulaties en menselijke goedkeuring voor elke wijziging. Kanaal: AI Engineer. Taal: Engels.

Bron: https://www.youtube.com/watch?v=3osCbSufv8g

**STVR organiseerde een Slowaakstalig gesprek van 54 minuten over wat AI bedreigt.** Het programma *Do kríža* van de publieke omroep bracht wiskundige Karol Nemoga, AI-onderzoeker Michal Valko en cognitiewetenschapper Igor Farkaš bij elkaar. De beschrijving vermeldt de vraag en de gasten, maar geen conclusies. Kanaal: STVR – Diskusie a politika. Taal: Slowaaks.

Bron: https://www.youtube.com/watch?v=tm8QmnxT2k4

## In het kort

**Een AI-agent koos een gentherapie en begeleidde een injectie in de hersenen van een levende muis.** Volgens Exin Therapeutics weigerde Opus 5.5 de naald te begeleiden nadat een dierenarts de schedel had geopend; Sonnet 5 ging wel verder. Het gaat om het verslag van één bedrijf over veiligheidsverschillen tussen modellen in een fysiek systeem.

Bron: https://www.wired.com/story/an-ai-agent-did-brain-surgery-on-live-mouse/

**Een federale rechter laat de NAACP-procedure over de turbines van xAI bij Colossus op grond van de Clean Air Act doorgaan.** Volgens de aanklacht draaiden minstens 35 gasturbines zonder de vereiste vergunningen. Rechter Debra Brown verwierp het argument van xAI dat het om mobiele bronnen ging en oordeelde dat de eisers een voldoende belang hebben om te procederen.

Bron: https://techcrunch.com/2026/10/31/judge-allows-naacp-lawsuit-over-xai-data-center-pollution-to-move-forward/

**Een voormalig onderzoeker van Meta zou hebben toegegeven de Books3-dataset met ongeveer 200.000 boeken via torrents te hebben gedownload.** Meta betwist de uitleg van de eisers en zegt dat Stephen Roller niet heeft verklaard dat hij de dataset voor het bedrijf downloadde. Over de vraag of gebruik voor modeltraining onder fair use valt, is al in het voordeel van Meta beslist. De wijze van verkrijging blijft omstreden.

Bron: https://torrentfreak.com/ex-meta-researcher-torrented-pirated-books-dataset-deleted-it-due-to-all-this-litigation/

**Intel verschuift productiecapaciteit van chips voor gebruikersapparaten naar Xeon en verwacht dat de vraag naar serverchips tot en met 2028 groter zal zijn dan het aanbod.** De omzet van Data Center and AI kwam uit op 7,3 miljard dollar, 17 procent meer dan het voorgaande kwartaal en bijna 80 procent meer dan een jaar eerder. De uitbreiding in Ierland voor extra Xeon-capaciteit op Intel 3 moet eind 2027 klaar zijn, tenzij het werk wordt versneld.

Bron: https://www.tomshardware.com/pc-components/cpus/intel-shifts-production-capacity-from-consumer-to-server-cpus-in-face-of-unprecedented-ai-demand-company-navigating-one-of-the-most-significant-supply-shortages-in-history

## Om in de gaten te houden

Volgens OpenAI-gebruikers krijgen ChatGPT en Codex in december gezamenlijke gebruikstegoeden. In het hier geraadpleegde materiaal heeft het bedrijf nog niet definitief uiteengezet hoe het verbruik per abonnement wordt berekend.
