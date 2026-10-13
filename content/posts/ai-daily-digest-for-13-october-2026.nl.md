+++
title = "Dagelijks AI-overzicht – 13 oktober 2026"
slug = "dagelijks-ai-overzicht-13-oktober-2026"
description = "Meta bracht Muse Wonder uit voor langlopende persoonlijke en professionele agents, terwijl Anthropic testte of kleine modellen zich op goedkope IoT-hardware konden repliceren. Twee preprints laten zien hoe taakcontext rollen van aandachtskoppen verandert en hoe een nieuwe gebruikersbeurt mislukt redeneren kan bijsturen."
tags = ["models", "research", "agents", "safety"]
date = 2026-10-13T03:59:27+02:00
draft = false
+++

Het sterkste werk van vandaag vraagt wat er gebeurt nadat een model meer dan één prompt ontvangt: het moet onthouden, volhouden, herzien of zichzelf naar een nieuwe omgeving verplaatsen. Het bewijs loopt van vrijgegeven API's en open code tot preprints en bewust vereenvoudigde dreigingsmodellen.

## Belangrijkste nieuws

**Meta lanceert Muse Wonder voor persoonlijke en professionele agents.** Meta bracht Muse Wonder uit via zijn Model API en Muse Code, met de grotere Muse Wonder Full voor Muse Code-abonnees. Beide accepteren een context van één miljoen tokens; hun parameteraantallen en gewichten blijven privé.

Meta zegt dat “Active Memory” relevante persoonlijke context over gesprekken heen ophaalt, terwijl “Active Focus” werk door blokkades heen voortzet en vóór belangrijke handelingen toestemming vraagt. De demonstraties omvatten het bouwen van een 3D-spel, het plannen van een hardloopsessie vanuit persoonlijke voorkeuren en het maken van een tafelschikking voor een bruiloft. Een beloofd volledig veiligheidsrapport is nog niet openbaar.

Onafhankelijke resultaten zijn sterk, maar ondersteunen geen claim van universeel leiderschap. Vals AI rangschikt Wonder Full vijfde van 47 modellen op zijn algemene index en vierde van 79 op Harvey's Legal Agent Benchmark. Het vermeldt 4 dollar per miljoen inputtokens en 20 dollar per miljoen uitvoertokens.

Bronnen: https://research.meta.ai/blog/muse-wonder, https://www.vals.ai/models/meta_muse-wonder-full, https://news.ycombinator.com/item?id=50059115

**Anthropic test modelzelfreplicatie op goedkope IoT-hardware.** Zijn Frontier Red Team verdeelde Gemma4-26B-A4B over 15 Android TV-boxen van ongeveer 55 dollar per stuk en haalde 0,39 gegenereerde tokens per seconde. Een model met 9 miljard parameters zette inferentie op acht van negen geteste hardwaretypen op.

Het onderzoek onderscheidt een doel vinden, uitvoering verkrijgen, inferentie opzetten en verspreiding voortzetten. Het richt zich op inferentieopstelling en neemt de exploitatiestappen grotendeels aan, dus het is geen live aanval en geen bewijs van een autonome worm. In vereenvoudigde tests van begin tot eind zegt Anthropic dat GLM-5.2 zijn replicatiedrempel overschreed, terwijl kleinere modellen veel stappen voltooiden maar ze niet betrouwbaar aaneenregen.

Het lab extrapoleert dat een model met minder dan 30 miljard parameters tegen eind 2026 de drempel kan bereiken, met een algemene vaardigheidsindex als benadering. De eigen schatting geeft een langzame worm een verdubbelingstijd in dagen. Reageerders op Hacker News betwistten de hardwareaannames en de sprong van gescripte evaluaties naar verspreiding.

Bronnen: https://www.anthropic.com/research/self-replicating-ai, https://news.ycombinator.com/item?id=50061603

**Taakcontext verandert wat dezelfde aandachtskoppen doen.** Sovesh Mohapatra en Dani Bassett testten vijf modellen met open gewichten van 1,5 miljard tot 14 miljard parameters met identieke graaffeiten onder verschillende taken. Interventies lieten zien dat een taak herverdeelt welke aandachtskoppen latere berekeningen en het eindantwoord beïnvloeden.

In Gemma-2-9B en Qwen3-14B veranderde één bewerking van een vroege activatievector welk graaffeit het model las, zonder de geschreven instructie te wijzigen. Dezelfde koppen reageerden vervolgens op andere feiten en beïnvloedden latere componenten anders. De conditiegebonden lineaire afbeelding van de auteurs verminderde de voorspellingsfout met 53,6 procent in Gemma en 5 procent in Qwen tegenover een gemiddelde afbeelding.

De preprint vervangt het idee dat een kop één vaste taak heeft door een netwerkverklaring: gedeelde onderdelen krijgen rollen via hun huidige interacties. Dat kan verklaren waarom een interventie die één gedrag verandert naar een ander kan doorwerken.

Bron: https://arxiv.org/abs/2610.13895

**UPTURN stuurt mislukt redeneren bij met een nieuwe gebruikersbeurt.** De preprint traint een kop met 130.000 parameters op een bevroren encoder om te kiezen waar een mislukt traject moet worden onderbroken, uitsluitend op basis van de juistheid van het eindantwoord. Het geselecteerde voorvoegsel blijft staan, een instructie wordt als nieuw gebruikersbericht ingevoegd en de rest opnieuw gegenereerd.

De auteurs vonden dat dezelfde instructie inline invoegen de koers van het model onder een vast budget niet betrouwbaar veranderde. Een nieuwe gespreksbeurt deed dat wel. Over vier redeneermodellen en zes wiskundebenchmarks verbeterde UPTURN in elke geteste opstelling de gemiddelde nauwkeurigheid tegenover een basislijn met 32 trajecten en versloeg het zelfcorrectie- en reflectietokenmethoden met gelijk budget.

De techniek vereist een aangeleerde interventieselector en is dus in volledige vorm geen recept met alleen prompts. Het centrale resultaat is toch direct toetsbaar: gespreksrolgrenzen kunnen een vastgelopen model effectiever sturen dan extra tekst binnen zijn bestaande redeneerspoor.

Bron: https://arxiv.org/abs/2610.13672

**Een ESP32 van 7 dollar geeft een AI-agent fysieke controle over een iPhone.** Henry Yuans project met MIT-licentie spiegelt het scherm via AirPlay en sluit een ESP32-S3 als USB-muis en -toetsenbord op de telefoon aan. Een planner maakt een kort plan; een uitvoerder leest elke schermafbeelding en kiest tikken, vegen, typen of doorlopend tekenen.

Het ontwerp vereist geen jailbreak, Apple-ontwikkelaarsaccount of app op de telefoon. De server volgt de relatieve aanwijzer, beweegt die vóór precieze tikken om de kalibratie te corrigeren en controleert na elke handeling of het scherm veranderde. Elk OpenAI-compatibel beeldmodel kan lokaal of in de cloud draaien.

Apple Pay, toegangscode-invoer en beschermde video verschijnen niet in schermspiegeling; liggende lay-outs en niet-ASCII-typen zijn ook onvoltooid. De repository bevat een noodstop en waarschuwt gebruikers de agent te begeleiden omdat hij met hun eigen accountrechten handelt.

Bron: https://github.com/onehumanbeing/esp32-iphone-agent

## Nieuwe modellen en releases

**Z.ai opent GLM-Legal als API-bèta.** De GLM-5.3-Flash-afgeleide kreeg juridische tussentraining en versterkend leren in gesimuleerde juridische omgevingen; Vals AI registreert onafhankelijk 19,17 procent volledig geslaagde gevallen op Harvey's LAB, dicht bij Z.ai's claim van 19,2 procent. Toegang vereist een aanvraag en er is geen openbare GLM-Legal-gewichtenrepository bevestigd. Bron: https://z.ai/blog/glm-legal

**OpenBMB brengt Trident-Qwen3VL-2B uit voor ophalen met gemengde modaliteiten.** Het embeddingmodel met MIT-licentie traint tekst-, beeld- en samengevoegde weergaven als gelijkwaardige positieve voorbeelden nadat de auteurs vonden dat ophaalsystemen tekst hoger rangschikken dan even relevante beelden. Gewichten, trainingsdata, evaluatiedata en code zijn openbaar; de winst blijft door de auteurs gemeten. Bron: https://huggingface.co/openbmb/Trident-Qwen3VL-2B

**NVIDIA en Princeton publiceren ReplaySSM voor sneller hybride decoderen.** De methode slaat een toestandsruimtelaag op als checkpoint plus recente invoer, slaat veel toestandsschrijfacties over en maakt speculatief terugdraaien tot een aanwijzerverplaatsing. De auteurs melden 1,20–1,47 keer hogere vLLM-doorvoer van begin tot eind tegenover een afgestemde basislijn, met vrijgegeven code en TensorRT-LLM-ondersteuning. Bron: https://developer.nvidia.com/blog/replayssm-rethinking-state-storage-for-faster-hybrid-model-decoding/

## Onderzoek

**Een model kan een willekeurige vaardigheid cryptografisch in zijn gewichten verbergen.** De auteurs plaatsen een versleuteld neuraal netwerk achter een geheime trigger in een gastmodel en stellen onder standaardaannames dat het aan uitlokking weerstaat, ook met volledige gewichtentoegang. Hun proef met chemische reacties doorstond finetuning, gewichtenruis, triggerzoeken en latente adversariële training, wat een formele grens stelt aan audits die vaardigheden proberen op te roepen. Bron: https://arxiv.org/abs/2610.13928

**Gewichtenupdates kunnen een subliminaal overgedragen eigenschap zonder labels onthullen.** Eigenschappen die over veel door leraren gegenereerde datasets blijven bestaan verschijnen als een gemeenschappelijke richting, terwijl taakvaardigheden variëren, melden de auteurs. Het versterken van die richting leest de eigenschap en het wegprojecteren onderdrukt die op gepubliceerde dierpreferentietests met weinig taakverlies. Bron: https://arxiv.org/abs/2610.13536

**Vision transformers leren woordbetekenis alleen uit beelden.** Twee grote DINOv3-modellen zonder bijschrifttraining groepeerden gerenderde woorden naar semantisch domein, clusterden merken naar sector en representeerden land-hoofdstadparen met consistente verschuivingen, met controle voor spelling. De woordrepresentaties sloten ook aan bij de visuele categorieën die ze benoemden. Bron: https://arxiv.org/abs/2610.13252

**Een aangeleerde selector verbetert onthouding op één vragenset maar generaliseert niet.** Op Qwen3-14B en TriviaQA steeg antwoorddekking van 20,2 naar 30,9 procent, terwijl fouten onder beantwoorde vragen van 23 naar 14,5 procent daalden. Op NQ-Open verloor de selector nog steeds van altijd onthouden en wijzigingen via versterkend leren leverden geen consistente winst. Bron: https://arxiv.org/abs/2610.13821

**Station-agents herontdekken bevindingen uit open onderzoeksproblemen.** Met de resultaten van drie ICLR-mondeling gepresenteerde artikelen achtergehouden en webtoegang uitgeschakeld melden de auteurs dat Station 62,7 procent van de oorspronkelijke bevindingen terughaalde, tegenover 14,4–20,6 procent voor vergelijkingssystemen. Een begeleider en periodieke metareflectie houden verkenning gaande zonder tussenscore; code is openbaar. Bron: https://arxiv.org/abs/2610.08927

**Attention leest schadelijkheid terwijl MLP-lagen weigeringen schrijven.** Over 18 paren basis- en instructiegetrainde modellen was schadelijkheid gemakkelijker uit vroege attention-updates te decoderen, terwijl MLP-updates het weigeringsgedrag produceerden. Natraining versterkte het schrijven van weigeringen zonder het schadelijkheidssignaal te verbeteren. Bron: https://arxiv.org/abs/2610.13078

**Beeld-taalmodellen verliezen ruimtelijke relaties bij pooling.** De auteurs haalden ruimtelijke predicaten op hun tokenposities terug, maar veel minder getrouw nadat de zin één gepoolde representatie werd; lexicale inhoud bleef beter behouden. Ze introduceren EICS en de CASP-VL-benchmark om het verlies te meten. Bron: https://arxiv.org/abs/2610.13910

**Een recurrente transformer generaliseert pariteit ver buiten zijn trainingslengte.** De decoder herhaalt berekeningen naarmate de reeks groeit; na training op pariteitsreeksen van maximaal 40 bits bereikte het model 100 procent op 256 bits, terwijl een standaardtransformer rond toeval bleef. Code is beschikbaar om te onderzoeken of recurrentie, in plaats van onthouden lengte, de toestand volgt. Bron: https://arxiv.org/abs/2610.07591

**Zelfgegenereerde herhaling vermindert vergeten bij voortdurende instructieafstemming.** Een bevroren kopie maakt voorbeelden uit “Task Banks” terwijl het actieve model nieuwe taken leert. De NYU-auteurs melden minder vergeten, ook bij taken buiten die banken, en publiceerden code. Bron: https://arxiv.org/abs/2610.12602

**ARC-architectuurvergelijkingen veranderen met hun rekenbudgetten.** Een gecontroleerde vergelijking van VARC en TRM varieert vijf voortrainingsbudgetten en vier budgetten voor training tijdens gebruik op ARC-AGI-1. De conclusie is methodologisch: architectuurclaims kunnen vertekend zijn wanneer systemen verschillende hoeveelheden training en zoeken krijgen. Bron: https://arxiv.org/abs/2610.13660

**SpatialASM traint modellen een nuttig gezichtspunt te verbeelden vóór het antwoorden.** De methode vraagt een beeld-taalmodel een taakrelevant perspectief op te bouwen, zoals menselijke mentale rotatie, voordat het ruimtelijke vragen oplost. De preprintresultaten zijn door de auteurs gemeld. Bron: https://arxiv.org/abs/2610.13832

**Echt taalmodelgebruik door clinici wijkt af van openbare benchmarks.** Een analyse van 127.833 vragen van 6.342 clinici vindt dat documentatie en kennisophaling domineren, terwijl diagnose 3,7 procent vormt. Volgens de auteurs dekken gangbare medische benchmarks die echte toepassingen slecht. Bron: https://arxiv.org/abs/2610.11069

**Galahad-KV herlaadt opgeslagen attention-toestand uit versleutelde NVMe.** Het systeem van één auteur slaat blokken van 16.000 tokens op en meldt 2,8–4,3 keer sneller laden dan herberekenen over 50 miljoen tokens met Gemma 4 op één H100. Het hergebruikt toestand in plaats van het attention-venster uit te breiden. Bron: https://arxiv.org/abs/2610.10845

**Xiaomi publiceert het MiMo-V2.6-technisch rapport.** Het rapport beschrijft een omni-modale familie met maximaal één miljoen tokens context en opgeschaald rekenwerk voor versterkend leren terwijl de mixture-of-experts-router voor stabiliteit bevroren blijft. Het biedt technische onderbouwing voor de eerder deze maand behandelde modelrelease. Bron: https://arxiv.org/abs/2610.11959

## Prompttechnieken

**Een langcontextgebruiker verplaatst regels naar het einde en verifieert vanuit citaten.** In één workflow van 1 miljoen tokens zouden instructies bovenaan rond 500.000 tokens worden vergeten, waarna de gebruiker gelabelde structuurregels onderaan plaatste. Reacties suggereerden relevante citaten vóór JSON-productie te verzamelen en een alleen-lezen-model uit een andere familie velden zonder citaatbewijs te laten verwijderen; dit is anekdotisch, geen benchmark. Bron: https://old.reddit.com/r/PromptEngineering/comments/1x1h18h/prompting_for_1m_context_windows_is_a_completely/

**Een lijst toegestane getallen beperkte cijfers in een door agents gemaakte presentatie.** De opdracht noemde vijf toegestane getallen, verbood alle andere en beperkte dia's tot 40 woorden. In één Sonnet 5.5-run controleerde de agent dia's en notities op cijfers en merkte zelfs op dat een gegeven verhouding van 15 g tot 250 g niet exact 1:16 was. Bron: https://old.reddit.com/r/PromptEngineering/comments/1x49fia/an_allowednumbers_list_in_the_brief_kept_an/

## Wat mensen bouwen

**anygrep doorzoekt notities, pdf's en beelden semantisch op een CPU.** De terminaltool met MIT-licentie draait EmbeddingGemma 2 als int8-ONNX-model, bewaart één lokale index en ondersteunt taaloverschrijdende en beeld-naar-beeldqueries. De basismodeldownload is ongeveer 350 MB, met nog 200 MB voor beelden. Bron: https://github.com/kuroko1t/anygrep

**shad0w compileert herhaalde LLM-classificaties tot een opzoektabel.** Het observeert antwoorden van een OpenAI-compatibele lokale server en antwoordt op de CPU alleen waar overeenkomst op apart gehouden data meer dan 95 procent is; anders stuurt het naar het model door. De Snake-demonstratie bereikt tien zetten per seconde na leren uit ongeveer 1.000 modelantwoorden. Bron: https://old.reddit.com/r/MachineLearning/comments/1x3vkej/i_built_a_tiny_table_that_learns_your_local_llms

**tinydetect draait gecomprimeerde AI-detectoren volledig in een browser.** De auteur verkleinde een RoBERTa-tekstdetector van 500 naar 97 MB en koppelde die aan een beelddetector van 26 MB via WebGPU of WASM met threads. De gemelde tekstcontrole van 60 milliseconden is een bouwermeting en de detectienauwkeurigheid is niet onafhankelijk getest. Bron: https://old.reddit.com/r/MachineLearning/comments/1x3vqip/compressed_a_roberta_aitext_detector_from_500_mb

**learnc stemt constanten in bestaande C-code af op een scorefunctie.** De tool met MIT-licentie herschrijft benoemde constanten en meldt 9,1 procent BD-ratewinst bij gelijke SSIM voor JPEG-tabellen en een F1-stijging van 0,810 naar 0,859 voor WebRTC-spraakdetectie. De auteur beperkt de methode tot tientallen of honderden constanten, geen optimalisatie op gewichtenschaal. Bron: https://old.reddit.com/r/MachineLearning/comments/1x4dlbm/learnc_fit_the_constants_in_existing_c_code_to

**cross-harness coördineert programmeeragents in afzonderlijke Git-worktrees.** De terminal- en lokale-weborkestrator ondersteunt zes agent-CLI's, vereist beoordeling tussen agents vóór samenvoeging en routeert vragen via één goedkeuringswachtrij. De demo gebruikt gescripte vervangers, een beperking genoemd in de README, terwijl de worktree- en testinfrastructuur echt is. Bron: https://github.com/AI-BizOS/cross-harness

**Atticus legt succesvolle Mac-workflows vast en herhaalt ze zonder AI.** Een bouwer uit de negende klas routeert eenvoudige commando's rechtstreeks en moeilijkere via `claude -p` en bewaart succesvolle stappen. Volgens de auteur verminderde herhaling één vergaderingstaak van ongeveer 30 naar 5–8 seconden. Bron: https://news.ycombinator.com/item?id=50049588

**Een McDonald's China-skill berekent couponcombinaties via MCP.** De repository haalt het live menu en bruikbare coupons op, somt alternatieven op en stuurt elke kandidaat naar de eigen prijsfunctie van de server in plaats van te raden. Vastgelegde antwoorden laten de demo met standaardbibliotheek zonder token draaien; de geclaimde besparing van 3–13 yuan per bestelling is van de bouwer. Bron: https://github.com/Ayzzz123/mcd-coupon-strategist

**HWREBench laat agents consumentenapparaten van de auteur aanvallen.** Modellen kregen flashdumps en hardwaretoegang met minimale sturing, terwijl de onderzoeker elke poging handmatig begeleidde. Kwetsbaarheden en verschillen tussen open en gesloten modellen zijn de benchmark van één persoon, geen onafhankelijke beveiligingsevaluatie. Bron: https://hwrebench.com/

**Attention Galaxy visualiseert een model met 135 miljoen parameters in de browser.** SmolLM2-135M draait via ONNX Runtime Web en toont kandidaten voor de volgende token plus attention-verbindingen over 30 lagen. Een schakelaar verbergt de attention-sink van de eerste token die de bouwer aanvankelijk voor een fout aanzag. Bron: https://old.reddit.com/r/MachineLearning/comments/1x3lgnz/i_built_a_browser_tool_to_visualize_how_a_small

**Een U-Net met 1,4 miljoen parameters voegt neuraal weer aan Minecraft toe.** FLUX.2 genereerde ongeveer 3.000 gestileerde frames voor distillatie en de leerling draait uitvoer van 512×288 in ongeveer 26 milliseconden op een GTX 1650, volgens de maker. Een PatchGAN-ronde verminderde de fletse gemiddelden van eenvoudig pixelverlies; er werd geen code gelinkt. Bron: https://old.reddit.com/r/MachineLearning/comments/1x25kq2/realtime_neural_weather_restyling_for_minecraft

## Het lezen waard

**Anthropic zegt dat zijn nieuwe verdediging distillatieopbrengst met 90–99 procent verlaagt.** Het lab beschrijft detectie van frauduleuze accountnetwerken en accepteert enig omzetverlies en klantfrictie om grootschalige extractie uit Claude te verminderen. Het noemt verkeer rond Zhipu en Kimi, maar prestatiecijfers en toeschrijving zijn van Anthropic en niet onafhankelijk geverifieerd. Bron: https://www.anthropic.com/research/distillation-defenses

**Een Harvard-onderzoek vindt dat programmeeragents code toevoegen zonder meer werk te voltooien.** Ars Technica meldt dat data van meer dan 700 bedrijven ongeveer 30 procent meer regels, 20 procent meer commits en 23 procent meer pull requests laten zien, terwijl oplossing van Jira-issues en epics niet significant veranderde. Beoordelingstijd per pull request steeg 49 procent, maar het onderzoek omvat modellen uit 2025 en meet dus een eerdere agentgeneratie. Bron: https://arstechnica.com/ai/2026/10/ai-coding-agents-generate-more-code-but-not-more-software/

**Rich Hickey en een weerlegging zijn het oneens of AI een tool is.** Hickey zegt dat een tool de gebruiker controle, feedback en vertrouwdheid geeft die deskundigheid opbouwt, terwijl onvoorspelbare LLM-automatisering werk voor de gebruiker doet. De reactie stelt dat betrouwbaarheid een beoordelingscriterium is, geen voorwaarde om een tool te zijn, en dat modeluitvoer testen en afwijzen een vorm van hanteren is. Bronnen: https://www.linkedin.com/pulse/ai-tool-rich-hickey-kjl8e, https://yyhh.org/blog/2026/10/ai-is-a-tool/

**Diomidis Spinellis stelt dat denken een hobby wordt.** De hoogleraar software-engineering voorspelt dat AI wint op kosten, beschikbaarheid en prestaties, zodat bewust denken een activiteit op zichzelf wordt. Het essay van 8 oktober dook opnieuw op op Hacker News, waar praktijkgebruikers hogere cognitieve belasting door controle van gegenereerde code beschreven. Bron: https://www.spinellis.gr/blog/20261008/

**Een Criteo-ingenieur vraagt hoe juniors seniors worden als agents het oefenen doen.** Elise Baturone vreest dat ontwikkelaars blijvende beoordelaars van één model met een ander kunnen worden voordat ze zelf ontwerpoordeel verwerven. Haar persoonlijke essay noemt vaardigheden die bewuste oefening blijven vereisen en claimt geen gemeten arbeidseffecten. Bron: https://tech.criteo.com/blog/human-skills-ai-cant-develop-junior-engineers/

## Hacker News

**QGIS stelt een moratorium op AI-ondersteunde bijdragen in.** De discussie vraagt of prototypen, automatische aanvulling en beoordeling als ondersteuning tellen, hoe een niet-afdwingbaar verbod zonder detector werkt en of vertrouwde bijdragers vrijstelling moeten krijgen. Het is een actuele casus waarin een open-sourceproject beoordelingscapaciteit verkiest boven elke gegenereerde patch accepteren. Bron: https://news.ycombinator.com/item?id=50054751

**Codex CLI's achtergrondupdater roept opslag- en vertrouwenszorgen op.** Een GitHub-issue zegt dat de daemon standaard wordt geïnstalleerd; één reageerder mat ongeveer 12 GB bewaarde versies, anderen zagen vergelijkbaar gedrag in Claude Code. Het geschil verbindt gewoon automatisch updategemak met toeleveringsketenzorgen over blijvende agentprocessen. Bron: https://news.ycombinator.com/item?id=50060694

**Janas streamt modelexperts van SSD wanneer het model groter is dan RAM.** Vroege gebruikers bespraken een gemelde 62 gegenereerde tokens per seconde en vroegen vergelijkingen met het groeiende aanbod expertstreamingruntimes. Eén benadrukte dat agentwerklasten ook afhangen van promptverwerking, waar de projectcijfers een andere bottleneck beschrijven. Bron: https://news.ycombinator.com/item?id=50063717

## Reddit

**Zes RTX 3090-kaarten bedienen Qwen3.8 bij 250.000 tokens context.** Eén gebruiker mat 6.574 prompttokens per seconde en 57,6 gegenereerde tokens per seconde voor één sessie, met 206 gegenereerde tokens per seconde over zeven sessies. De vLLM-afsplitsing bewaart een tabel van 102 GB op SSD en gebruikt int8-KV-cache omdat fp8 op Ampere faalde; de resultaten zijn zelf gemeld. Bron: https://old.reddit.com/r/LocalLLaMA/comments/1x3wjzf/qwen38flashnext_on_six_3090s_with_vllm_7_users_at/

**Gebruikers van lokale modellen betwisten Anthropics distillatieverslag.** Reageerders vroegen of gewoon uitvoer bemonsteren zonder logits naar een andere tokenizer past bij de gebruikelijke betekenis van distillatie en lazen het veiligheidskader als druk tegen open gewichten. Hun bezwaren zijn gemeenschapsmeningen; Anthropics geclaimde 90–99 procent vermindering is ook buiten het lab ongeverifieerd. Bron: https://old.reddit.com/r/LocalLLaMA/comments/1x4ii8e/anthropic_is_doing_free_publicity_for_glm_again/

**BrokenML meet of agents gedistribueerde trainingstaken repareren.** Negen modellen pakten vastlopers, achterblijvers, geheugenfouten, corrupte checkpoints en stille verliesdivergentie op drie toegangsniveaus aan. Van 414 pogingen op live clusters faalden 66 en verergerden 13 het probleem; de auteur noemt uitsluitend CPU-taken, één run per taak en geen duurste modellen. Bron: https://old.reddit.com/r/LocalLLaMA/comments/1x41pqt/brokenml_can_agents_fix_broken_ml_jobs/

**Een gebruiker meldt 262.000 tokens Qwen-context op 16 GB VRAM.** Met een adaptieve KV-streamingafsplitsing van llama.cpp mat de poster 80 gegenereerde en 1.500 prompttokens per seconde vóór het vullen van de context, dalend tot ongeveer 20 en 400 bij volledige lengte. Het resultaat omvat beeldverwerking en gedeeld schermgeheugen en is niet onafhankelijk gereproduceerd. Bron: https://old.reddit.com/r/LocalLLaMA/comments/1x4cmfc/running_unslothqwen3827budiq4_xs_262k_q4_0_kv/

**Een private Qwen-testset maakt beoordelingskosten onderdeel van het resultaat.** Eén gebruiker beperkte meer dan 500 spreadsheet-, precisie-, programmeer- en ophaaltests tot de gevallen die modellen onderscheidden en vond vervolgens frequente afbreking door overdenken bij Qwen3.8-Flash-Next. De conclusie dat lokale uitvoer nog Claude- of GPT-controle nodig heeft beschrijft één workflow, geen algemene benchmark. Bron: https://old.reddit.com/r/LocalLLaMA/comments/1x49pmn/qwen3827b_vs_frontier_vs_others/

**Boole-1.7B verpakt een eenbit-Qwen-model in 247 MB.** Precision Numerics zegt dat zijn gewichten 13,9 keer kleiner zijn dan BF16 en 85,9 procent van de gemiddelde basisscore behouden op een interne evaluatie met tien taken. Het ondersteunt een browserdemo, vLLM en llama.cpp; prestaties blijven volgens de aanbieder. Bron: https://old.reddit.com/r/LocalLLaMA/comments/1x452zj/boole17b_a_1bit_qwen317b_model_that_outperforms/

**Praktijkgebruikers vinden geen mechanistisch bewijs dat volgende-token-training algemene intelligentie oplevert.** Een Machine Learning-discussie onderscheidde onthouden, oppervlakkige heuristieken en aangeleerde redeneerstructuren onder hetzelfde verliesdoel. Veel reacties stelden dat noch kunstmatige noch natuurlijke algemene intelligentie de gevraagde causale verklaring heeft, waardoor de draad helder verwoordt wat onbekend blijft in plaats van bewijs voor één kant te leveren. Bron: https://old.reddit.com/r/MachineLearning/comments/1x4awlk/what_is_the_strongest_mechanistic_argument_that/

## YouTube

**AI Engineer scheidt het brein van de handen in Claude Managed Agents.** Priyanka Phatak beschrijft vervanging van één ondoorzichtige container door een alleen-aanvullen-sessielog, een agentomgeving als “brein” en sandbox als “handen”; credentials komen via een uitgaande proxy binnen en bereiken Claude niet. In de Engelstalige lezing meldt ze ongeveer 90 procent minder tijd tot de eerste token na het herontwerp. Bron: https://www.youtube.com/watch?v=Uv0nAf_7tyU

**AI Engineer bouwt dataschema's pas als de vraag bekend is.** Hrishi Olickel toont hoe het verwijderen van mintekens netto 784.000 dollar in 5,3 miljoen dollar schuld veranderde, terwijl meerdere modellen de fout deelden. Zijn Engelstalige lezing scheidt modellen die een vraagspecifieke transformatie ontwerpen, uitvoeren en optimaliseren, met apart gehouden gevallen en controles op meningsverschillen tussen families. Bron: https://www.youtube.com/watch?v=Fa3hQVIKShw

**Een GPU-timingzijkanaal onthult de werklast van een naburige tenant.** Branislav Brzak meldt ongeveer drie microseconden extra H100-geheugenvertraging wanneer een andere GPU-partitie actief is, genoeg in zijn opstellingen om modeldiepte, decodeersnelheid en werklasttype af te leiden. De Engelstalige AI Engineer-lezing claimt geen herstel van prompts of antwoorden. Bron: https://www.youtube.com/watch?v=SacJfmp33vM

**Gedelegeerde autorisatie beperkt wat een agent met een gebruikersidentiteit kan doen.** Kim Maida demonstreert hoe blijvende admincredentials een triageagent een database laten verwijderen en stelt OAuth-tokenuitwisseling met kortlevende, taakgebonden credentials voor. Het intentiegebonden deel blijft een leveranciersvoorstel en geen voltooide standaard; de lezing is Engelstalig op AI Engineer. Bron: https://www.youtube.com/watch?v=ws9XcGGPBDk

**a16z-gasten definiëren recursieve zelfverbetering beperkter dan automatisering.** De oprichters van MakerMaker.AI eisen dat het verbeterde systeem over modellen en agentomgevingen heen de verbeteraar blijft en stellen vaardigheden relatief aan middelen meten voor. Hun Engelstalige interview bespreekt variantie en beloningsmisbruik maar presenteert vroege onderzoeksclaims en meningen. Bron: https://www.youtube.com/watch?v=3Q1mdn5ZGvM

**AI Explained overziet claims over labwedloop en inbreuken.** Het Engelstalige commentaar verzamelt recente uitspraken van Sam Altman, Dario Amodei, OpenAI en wiskundige critici in een leeslijst over de komende 18 maanden. De conclusies zijn van de presentator, geen nieuw labresultaat. Bron: https://www.youtube.com/watch?v=C4Sq3Rot8FU

**Joseph Gordon-Levitt bepleit mensgericht AI-bestuur.** In een Engelstalige New York Times Opinion-video rond de Algemene Vergadering van de Verenigde Naties beantwoordt de acteur en VN-pleitbezorger vijf vragen over risico en het vermogen van overheden om bij te blijven. Het is een pleidooi van acht minuten, geen technisch bewijs. Bron: https://www.youtube.com/watch?v=nYdeUu2I80s

**Blaise Agüera y Arcas zegt dat AGI mogelijk al is aangekomen.** In een Engelstalig Digital Disruption-interview van 92 minuten verbindt de Google-onderzoeker intelligentie met sociale interactie en bespreekt bewustzijn, agentzwermen, surveillance en ongelijkheid. De beschrijving geeft zijn opvattingen en geen bewijs voor de AGI-claim. Bron: https://www.youtube.com/watch?v=ALN6mAbm3w8

**Een Duits panel vraagt of software oordelen kan vellen.** Ethicus Bert Heinrichs, voormalig constitutioneel rechter Udo Di Fabio en socioloog Tim Huyeng bespreken automatiseringsbias, verlies van medische vaardigheden, regulering en een mogelijk recht op machineoordelen. Het pAIdeía-gesprek is Duitstalig en benadert AI via recht en filosofie. Bron: https://www.youtube.com/watch?v=Fz6BFtsJZW8

**Juraj Hvorecký verlegt het Tsjechische debat van uitsterven naar huidige schade.** De filosoof vertelt Deník Alarm dat riskant chatbotgebruik, isolatie en eenzaamheid meer aandacht verdienen dan verre vernietigingsscenario's. De Tsjechischtalige beschrijving geeft dit argument, maar geen transcriptie was beschikbaar voor gedetailleerde verificatie. Bron: https://www.youtube.com/watch?v=F8IpF9mjpLo

**Filip Dvořák legt verifieerbare neurosymbolische AI in het Tsjechisch uit.** De Filuta AI-oprichter vertelt FocusOn dat overtuigende taaluitvoer verkeerd kan blijven en beschrijft combinatie van neurale en symbolische componenten voor controleerbare resultaten. Het Tsjechischtalige interview werd dicht bij de grens van het venster van zeven dagen geüpload. Bron: https://www.youtube.com/watch?v=oaeCw89Ebnw

**Žijeme Sci-Fi bespreekt banen en gegenereerde werkelijkheid in het Slowaaks.** De Slowaakstalige aflevering behandelt werkgelegenheid, militaire AI, synthetische media, kinderen en technologie. Alleen de hoofdstuklijst was beschikbaar, zodat de conclusies van de sprekers niet verder dan die onderwerpen worden toegeschreven. Bron: https://www.youtube.com/watch?v=XcNkD8D28jA

## In het kort

**CyberXero gebruikte Claude Code en 51 gespecialiseerde agents in een inbraakcampagne.** SOCRadar zegt dat een blootgestelde map sessielogs, tokens en slachtofferdata lekte uit aanvallen op WordPress, handel en Oekraïense energiedoelen; één run scande 4.708 doelen en plaatste 32 webshells in 61 seconden. Volgens The Hacker News toonden logs zowel weigeringsomzeiling via nieuwe “geautoriseerde test”-sessies als weigeringen die standhielden. Bron: https://thehackernews.com/2026/10/cyberxero-uses-claude-code-in-campaign.html

**UK AISI stelt acht vrijwillige praktijken voor ontwikkeling van geavanceerde modellen voor.** Het instituut zegt meer dan 55 modellen te hebben geëvalueerd en nu risico's tijdens training, verzadigde tests en modellen die evaluatie herkennen te zien. De agenda omvat levenscyclusmonitoring, incidentrapporten, behouden toezicht, ingebedde auditors, beveiliging en alignmentmeting en maatstaven voor AI in AI-ontwikkeling. Bron: https://www.aisi.gov.uk/blog/towards-technical-best-practice-for-frontier-ai-development

**De Britse regering overweegt verplichte rapportage van AI-veiligheidsincidenten.** Minister Kanishka Narayan hield de gisteren aangekondigde toespraak en voegde mogelijk gebruik van de Cyber Security and Resilience Bill en een programma tegen AI-aanvallen toe. Hij zei ook dat AISI recente modellen vóór release evalueert en beloofde AI-veiligheid als focus van het Britse G20-voorzitterschap in 2027. Bron: https://www.theguardian.com/technology/2026/oct/12/cyber-attack-like-openai-medicare-breach-seems-likely-in-uk-says-minister

**Het Witte Huis herstructureert het Amerikaanse AI-testorgaan.** The Information meldt dat drie hoge functionarissen van het Center for Advancing Innovation and Standards for Super Intelligence rechtstreeks aan het Witte Huis gaan rapporteren. Alleen een feedsamenvatting was leesbaar, waardoor reden, tijdpad en effect op testtoegang onbekend blijven. Bron: https://www.theinformation.com/articles/trump-administration-plans-move-ai-testing-agency-officials-white-house

**Microsoft beschrijft de Maia 300-accelerator en een superpod met 12.288 chips.** Het bedrijf noemt acht HBM4-stacks met 288 GB en 18 TB/s per accelerator, racks met 96 accelerators en Ethernet-scale-upverbindingen over maximaal 128 racks. Prestatieverbeteringen tegenover Maia 200 zijn bedrijfsclaims zonder onafhankelijke benchmark. Bron: https://azure.microsoft.com/en-us/blog/deep-dive-into-azure-maia-300-architecture/

**Intel noemt zijn accelerator met veel geheugen GPU D-Series.** De PCIe-kaart van 350 W combineert maximaal 480 GB LPDDR5X met 1,3 PFLOPS FP8-rekenkracht en 1,5 TB/s bandbreedte, volgens Tom's Hardware's OCP-verslag. Prijs en leverdatum zijn niet bekendgemaakt. Bron: https://www.tomshardware.com/tech-industry/artificial-intelligence/intels-crescent-island-ai-accelerator-officially-powers-new-gpu-d-series-products-chip-delivers-1-3-peak-pflops-of-fp8-compute-and-1-5-tb-s-of-memory-bandwidth

**AMD onthult Helion-racks voor CPU-zware agentwerklasten.** Het OCP-referentieontwerp schaalt tot 32.768 Zen 6-kernen, 16 Instinct MI350P-GPU's en 102 Tbps netwerkcapaciteit, met partnersystemen verwacht in november. Het positioneert agentuitvoering naast inferentie in plaats van als nog een rack voor training van geavanceerde modellen. Bron: https://www.theregister.com/systems/2026/10/12/amd-unveils-helion-racks-for-ai-agents-at-ocp-summit/5302652

**Nvidia opent Vera Rubin-rack- en trayontwerpen voor het Open Compute Project.** DataCenterDynamics meldt ook een zelfstandig Vera-CPU-platform voor agentwerklasten, maar het artikel was buiten de feedsamenvatting ontoegankelijk. Gedetailleerde specificaties waren daarom niet beschikbaar. Bron: https://www.datacenterdynamics.com/en/news/nvidia-opens-up-vera-rubin-rack-and-tray-designs-to-ocp/

## Om in de gaten te houden

AMD-partnersystemen op basis van Helion worden in november verwacht, Meta is nog een volledig Muse Wonder-veiligheidsrapport verschuldigd en het Verenigd Koninkrijk wil AI-veiligheid op zijn G20-agenda voor 2027 zetten.
