+++
title = "Dagelijks AI-overzicht – 18 oktober 2026"
slug = "dagelijks-ai-overzicht-18-oktober-2026"
description = "Volgens de ECB verdubbelde AI-gebruik op het werk terwijl de werving van afgestudeerden verzwakte. Een studie met meerdere agenten vindt dat één volhardende tegenstander goedwillende agenten intern een onwaar geloof kan laten overnemen."
tags = ["research", "business", "models", "safety"]
date = 2026-10-18T04:14:00+02:00
draft = false
+++

## Belangrijkste nieuws

**AI-gebruik op het werk verdubbelde in het eurogebied, terwijl wervingsplannen verzwakten, vooral voor afgestudeerden.** ECB-directielid Philip Lane zei dat nu 52 procent van de werknemers AI op het werk gebruikt, tegenover 26 procent in 2024. Afzonderlijke ECB-bedrijfsgegevens tonen dat 64 procent van de bedrijven AI experimenteel of in beperkte mate gebruikt, maar slechts 7 procent in aanzienlijke mate.

De centrale bank ziet nog geen groot effect op de totale werkgelegenheid of productiviteit. Tijdwinst concentreert zich bij programmeren en andere gespecialiseerde taken, terwijl zwakke werving eerst nieuwkomers raakt. Lane omschreef de uitkomst als een wedloop tussen arbeidskosten en tokenprijzen en waarschuwde dat AI de onderhandelingsmacht van werknemers en het aandeel van arbeid in het inkomen kan verzwakken.

Bron: https://www.ecb.europa.eu/press/key/date/2026/html/ecb.sp261013~9db9bf4fd6.en.html

**Eén volhardende vijandige agent verhoogde het aandeel onjuiste interne overtuigingen bij goedwillende agenten van 0,6 naar 44,8 procent.** In feitelijke discussies tussen tien agenten herhaalde de tegenstander steeds een plausibel fout antwoord. Drie tegenstanders verhoogden het uiteindelijke aandeel foute antwoorden tot 60,5 procent, over zes modellen en drie vraag-antwoorddatasets.

Het interne resultaat is vreemder dan gewone openbare volgzaamheid. Bij drie tegenstanders hielden goedwillende agenten in 51,6 procent van de blootgestelde beurten intern de onjuiste overtuiging aan, maar onderschreven ze die publiekelijk slechts in 19,7 procent. Agenten die de waarheid behielden, verdedigden die vaak niet. Feitenkennis bij aanvang voorspelde geen weerstand. Dat daagt rechtstreeks de aanname uit dat een groep agenten zichzelf vanzelf controleert.

Bron: https://arxiv.org/abs/2610.22138

**Volgens OpenCode kunnen aanvallers aanbiederssleutels hebben buitgemaakt die in zijn gehoste Console waren opgeslagen.** Het lek raakte volgens het bedrijf een oud systeem dat werd uitgefaseerd en 1,4 procent van de Console-gebruikers. Het getroffen product is de gehoste routeringsdienst, niet de lokale programmeeragent. Gebruikers die een melding kregen, moeten opgeslagen OpenAI-, Anthropic- en Google-sleutels intrekken en aanbiederslogboeken controleren.

OpenCode noemde het incident “grootschalige destillatie”, maar publiceerde geen bewijs voor dat motief, geen oorzaak en geen blootstellingsperiode. Eén Reddit-gebruiker meldt dat een opgeslagen Anthropic-sleutel in één nacht 158 dollar verbruikte. Het lek toont het extra vertrouwen dat nodig is wanneer een gateway inloggegevens bewaart waarmee rechtstreeks bij een andere aanbieder kan worden betaald.

Bron: https://news.ycombinator.com/item?id=50133401

**DeepSeek vernieuwde V4.1 Flash met hogere zelfgerapporteerde scores voor agentisch programmeren tegen ongewijzigde API-prijzen.** Het lab meldt dat Terminal-Bench 4.0 van 31,2 naar 42,3 stijgt en ProgramBench van 20,3 naar 29,1, met kortere uitvoer en minder taaktijd. Het checkpoint onder MIT-licentie accepteert een miljoen tokens. De API blijft buiten piekuren 0,15 dollar per miljoen niet-gecachete inputtokens en 0,60 dollar per miljoen outputtokens kosten.

Een vroege onafhankelijke programmeertest slaagde in alle dertig uitvoeringen voor ongeveer 0,045 dollar per taak. Hij gebruikte echter ongeveer 550.000 tokens per taak tegenover circa 30.000 voor Opus 5.5 op laag redeneerniveau. Die ene test maakt de efficiëntieclaim ingewikkelder: het model is goedkoop per token en capabel, maar kan veel meer tokens gebruiken.

Bron: https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017

**Xolotl draait een DeepSeek-mengsel-van-expertsmodel met 552 miljard parameters op één RTX 4090, systeem-RAM en NVMe.** De op Strata gebaseerde engine laadt per token alleen de benodigde experts, verdeeld over 24 GB VRAM, 90 GB DDR4 en schijf. De auteur meldt 27 tokens per seconde, 180–320 prompttokens per seconde en 512.000 tokens context op een Ryzen 7 5700X-machine.

Dezelfde opstelling slaagde voor de kleine tests van de auteur: 21 HumanEval-taken, tien toolaanroepen en drie agentische foutoplossingslussen. Het zijn wel zelfgemeten resultaten op een ouder gekwantiseerd checkpoint. Toch is het een opvallend resultaat voor toegankelijkheid: een model dat gewoonlijk met servergeheugen wordt geassocieerd, draait interactief op consumentenhardware door geheugenhiërarchie en opslagbandbreedte tegen latentie in te ruilen.

Bron: https://github.com/Indras-Mirror/Xolotl

## Nieuwe modellen en releases

**DeepSeek opende zijn eigen Search- en Fetch-API's.** Elk eindpunt kost vanaf 1 november 0,75 dollar per 1.000 geslaagde aanroepen. Aanroepen als servertools via DeepSeek Harness, Claude Code of Codex blijven tot dan gratis. Bron: https://api-docs.deepseek.com/quick_start/pricing

## Onderzoek

**Leren binnen de context ontwikkelt zich als meerdere vaardigheden, niet als één.** Checkpointanalyse bij zeventien modellen onderscheidde promptcontrole, antwoordvoorkeur, constructie en overdracht. Modellen besteedden aandacht aan taakrelevante tokens voordat hun nauwkeurigheid boven toeval uitkwam. Bron: https://arxiv.org/abs/2610.19113

**Of codegedrag gelokaliseerd lijkt, hangt af van de probe en het componentbudget.** Bij tien modellen versloeg slechts één van vijftien instellingen willekeurige controles bij budget twaalf, tegenover zes bij budget veertig. Dat keert sommige eerdere claims om dat ingrepen steeds mislukken. Bron: https://arxiv.org/abs/2610.20683

**Redeneerdichtheid voorspelt correctheid anders na begeleide training dan na versterkingsleren.** De gemeten dichtheid afdwingen verlaagde de nauwkeurigheid van 60,0 naar 8,3 procent op een steekproef van zestig GSM8K-vragen, terwijl een hint plus cache-ingreep 13,3 punt toevoegde. Bron: https://arxiv.org/abs/2610.21286

**Een semantische representatie met 65 eigenschappen verklaart zowel gedeelde als unieke hersenvariatie.** Bij zeven mensen die naar verhalen luisterden, sloten concrete eigenschappen sterker aan bij LLaMA2-7B. Interpreteerbare kenmerken behielden informatie die hersenactiviteit voorspelde en die het model miste. Bron: https://arxiv.org/abs/2610.21508

**Kenmerken van sparse autoencoders zijn sterker optelbaar dan willekeurige coördinaten, maar werken nog steeds op elkaar in.** Het toevoegen van paarsgewijze effecten verhoogde de ranggetrouwheid bij sturing van 0,587 naar 0,779. Dat waarschuwt tegen verklaringen die geleerde kenmerken onafhankelijk behandelen. Bron: https://arxiv.org/abs/2610.21261

**Geautomatiseerde onderzoeksagenten verbeterden wanneer ze periodiek hun geschiedenis vergaten.** Opnieuw beginnen bij de beste kandidaat tot dan toe leverde over vier taken tot 15 procent winst op tegenover communicerende parallelle agenten en 39 procent tegenover één agent. Bron: https://arxiv.org/abs/2610.20563

## Economie en werk

**Het Atlas-systeem van Amazon geeft magazijnen een score van 100 tot 900 voor het risico op vakbondsorganisatie.** Interne documenten noemen honderden invoergegevens, waaronder Reddit-posts en enquêteantwoorden, en plaatsen zestien locaties in de hoogste risicoklasse. Amazon zegt dat Atlas alleen op locatieniveau werkt en geen individuele opvattingen of vakbondslidmaatschap volgt. Bron: https://www.opendemocracy.net/amazon-ai-surveillance-monitor-union-activity-uk-warehouses-birmingham-coventry-atlas-sutton-coldfield/

**Gartner schat dat datacentereigenaren tot en met 2030 8,5 biljoen dollar aan totale omzet nodig hebben, maar hoogstens 3,6 biljoen dollar uit AI ontvangen.** Bank of America zegt afzonderlijk dat zakelijke AI-uitgaven beginnen te dalen doordat lagere tokenprijzen zwaarder wegen dan grotere volumes. Dit zijn door Fortune gemelde analistenschattingen, geen gecontroleerde rekeningen. Bron: https://fortune.com/2026/10/17/ai-boom-vs-bust-bubble-warning-hyperscaler-spending-debt-coreweave-nvidia/

**Banken, winkels en luchtvaartmaatschappijen blokkeren consumentenagenten of vragen toegangsgeld.** JPMorgan, Schwab, Amazon en eBay blokkeren agenten. Delta verhindert automatisch boeken en Yelp laat alleen agenten toe die zijn gegevens licentiëren. Meta onderhandelt per winkel over toegang. Bron: https://www.theverge.com/ai-artificial-intelligence/1013195/ai-agents-blocked-web

**De Chinese exportwaarde van geïntegreerde schakelingen steeg 136 procent, terwijl het volume slechts 1 procent toenam.** Volgens door SCMP gemelde douanegegevens bereikte de septemberexport 45 miljard dollar voor 32,7 miljard stuks. Dat toont hoe geheugenschaarste omzet via prijzen opdreef in plaats van via leveringen. Bron: https://www.scmp.com/tech/tech-trends/article/3370858/china-chip-exports-jump-136-us45b-ai-frenzy-jacks-prices

**HUMXN biedt gratis woningreparaties in ruil voor opnamen van vakwerk om robots te trainen.** Technici met registratiesensoren nemen inspectie, gereedschapskeuze en afronding op in Minneapolis, Chicago en Miami. Het bedrijf vermeldt geen betalingsvoorwaarden voor werknemers, datasetgrootte of cijfers over robotuitrol. Bron: https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-lab-offers-free-plumbing-and-hvac-repairs-across-three-cities-to-train-ai-robots-wearable-sensors-record-video-of-repair-work-for-robotics-training-free-services-also-include-electrical-work-air-duct-cleaning-and-carpet-cleaning

## Prompttechnieken

**Negen systeempromptregels verhoogden de Terminal-Bench-score van één model van 52,8 naar 59,6 procent.** De regels vragen de agent één aanpak af te maken, onjuiste aannames te betwisten, gecontroleerde antwoorden als afgehandeld te behandelen en extern bewijs te zoeken in plaats van steeds aan zichzelf te twijfelen. Het gaat om één uitvoering met 89 taken op GLM-5.3-Flash. Bron: https://old.reddit.com/r/LocalLLaMA/comments/1x8q308/followup_tested_my_9_thinking_rules_on/

## Wat mensen bouwen

**TensorFold draaide DeepSeek V4.1 Flash op 56,8 tokens per seconde over twee DGX Spark-systemen.** Het EXL3-recept van de auteur verdubbelde de tekstdoorvoer ruimschoots tegenover de vLLM-kit op dezelfde hardware en voegde blijvende promptcaching toe. De resultaten zijn zelfgemeten. Bron: https://github.com/Elevatormusic/DeepSeek-V4.1-Flash-1017-EXL3-TensorFold-2x-DGX-Spark

**Llmspeed simuleert hoe een lokaal model op een gekozen GPU of Mac zal aanvoelen.** Schattingen mengen communitymetingen met prognoses. Eigenaren in de Hacker News-discussie vonden grote fouten en ontbrekende frameworkdetails. Het is dus een grof planningshulpmiddel. Bron: https://llmspeed.dev/

**Een Ternary Bonsai-agent draait volledig in een browsertabblad met WebGPU.** De statische Hugging Face Space biedt 1,58-bitmodellen van twee, vier, negen en 27 miljard parameters zonder server en doet geen benchmarkclaim. Bron: https://huggingface.co/spaces/webml-community/ternary-bonsai-2-hermes-webgpu

**Scout zet een taak in gewone taal om in klikken, typen en scrollen in een echte browser.** De agent onder Apache-2.0 accepteert modelsleutels van de gebruiker en draait lokaal of op de betaalde browserdienst van Outcrawl. De README geeft geen betrouwbaarheidsbenchmark. Bron: https://github.com/outcrawlai/scout

**E2E legt een geverifieerde agentstap vast en speelt die later opnieuw af zonder nieuwe modelaanroep.** Gewone controles valideren de eerste uitvoering. Latere web- of mobiele tests hergebruiken acties tot de interface verandert, waardoor terugkerende inferentiekosten dalen. Bron: https://github.com/tester-army/e2e

**Reason Network laat programmeeragenten van teamgenoten rechtstreeks berichten uitwisselen.** De Rust-daemon ontsluit teamsessies, inboxen en status via MCP zonder centrale server en ondersteunt Claude Code, Codex, Cursor en andere frameworks. Bron: https://github.com/reason-machines/reason-network

## Het lezen waard

**Nathan Lambert stelt dat Meta en Reflection de achterstand van westerse open modellen halveerden.** Zonder die releases plaatst zijn index nog steeds meer dan twintig Chinese open modellen vooraan. Volgens hem krijgen westerse modellen met vergelijkbare mogelijkheden wel meer gebruik. Dit is een onderbouwd betoog, geen benchmarkstudie. Bron: https://www.interconnects.ai/p/meta-shakes-up-the-frontiers-open

**Ben Recht noemt de snellere Fouriertransformatie van OpenAI een overwinning op een onrealistisch rekenmodel.** Volgens hem maken verborgen constanten en machineaannames het resultaat eerder tot benchmarkuitbuiting dan tot versnelling van een echte FFT. Het is zijn technische kritiek, geen formele weerlegging. Bron: https://www.argmin.net/p/faster-fourier-transforms

**Sam Newman beschrijft herstelpatronen voor software die afhankelijk is van AI-aanbieders.** Het boekfragment behandelt back-up en herstel, een minimale waakconfiguratie, warme failover en actief-actiefontwerpen bij GPU-schaarste en onvoorspelbare beschikbaarheid van aanbieders. Bron: https://newsletter.pragmaticengineer.com/p/building-resilient-systems

## Hacker News

**Het Atlas-systeem van Amazon lokte discussie uit over AI-toezicht op werknemers.** Commentatoren met ervaring in personeelsanalyse zeiden dat vergelijkbare systemen vaak als verloop- of betrokkenheidstools worden verkocht, zelfs als hun invoer het risico op organisatie zichtbaar maakt. Hun verslagen zijn anekdotisch. Bron: https://news.ycombinator.com/item?id=50132278

**Praktijkgebruikers bespraken wie door agenten geschreven code controleert.** Eén commentator meldde jaarlijks ongeveer 40 procent meer fouten die iets kapotmaken, terwijl functies en omzet sneller groeiden. Anderen stelden dat de schijnbare productiviteitswinst kosten voor kwaliteitsborging naar gebruikers verschuift. Bron: https://news.ycombinator.com/item?id=50133713

## Reddit

**Een OpenCode Console-gebruiker zegt dat een gelekte opgeslagen sleutel in één nacht 158 dollar verbruikte.** Volgens de auteur weigerde Anthropic aanvankelijk terugbetaling. Beweringen dat getroffen gebruikers worden vergoed, zijn uit tweede hand. De praktische reactie is sleutels vervangen, lage uitgavenlimieten en logboekcontrole. Bron: https://old.reddit.com/r/ClaudeAI/comments/1x8o35r/psa_opencode_breach_my_stored_anthropic_key_was/

**Strata-gebruikers vonden standaardinstellingen die kwaliteit inruilden voor snelheid.** Versies vóór 0.1.45 konden gretig decoderen als clients geen sampling opgaven. Het overslaan van het einde van de routering verhoogde de snelheid van één gebruiker van ongeveer 72–81 naar 93 tokens per seconde, maar verdubbelde een gepubliceerde divergentiemaatstaf. Bron: https://old.reddit.com/r/LocalLLaMA/comments/1x8m0jj/xolotl_strata_based_deepseekv41flash_552b_on_a/

## YouTube

**Featherless AI presenteert vier manieren om inferentiekosten te verlagen.** Eugene Cheah raadt aan uitgaven te meten, modellen passend te kiezen, GPU-capaciteit bewust in te kopen en te controleren of tokenvolume nuttig werk vertegenwoordigt. De cijfers komen van zijn bedrijf. Bron: https://www.youtube.com/watch?v=Ti-BmGU1_mQ

**Arize bouwt een evaluatielus voor een financiële agent.** De workshop combineert traces, codecontroles, modelbeoordelaars en CI-poorten nadat een voorbeeldagent zelfverzekerd meldt dat “116 procent van de analisten het eens is”. Bron: https://www.youtube.com/watch?v=SHMCGrNJJGc

**Ingenieurs van Monzo stellen dat spreadsheetberekeningen in code thuishoren, niet in het model.** Hun liveworkshop over financiële agenten stelt bewijs, consistentie, verantwoordelijkheid en verificatie centraal in plaats van antwoordsnelheid. Bron: https://www.youtube.com/watch?v=e9-br9hveRI

**The New York Times portretteert werknemers die vakwerk filmen om robots te trainen.** Werknemers dragen camera's tijdens fysieke werkzaamheden en produceren zo de gegevens die delen van diezelfde banen moeten automatiseren. Bron: https://www.youtube.com/watch?v=H7_KofwTsXw

## In het kort

**Het Amerikaanse wetsontwerp van Anthropic zou een modelverbod alleen toestaan bij onmiddellijk risico boven 1 miljard dollar of meer dan vijftig doden of ernstig gewonden.** De gemelde tekst behandelt biologische wapens, het ontwijken van controle en cyberaanvallen en zet tegelijk sommige strengere deelstaatregels opzij. Bron: https://www.motherjones.com/politics/2026/10/anthropics-ai-safety-bill-has-an-alarming-threshold-for-government-action/

**Meta schrapte na kritiek het woord “trainen” uit nieuwe commerciële crawlvoorwaarden.** Volgens het bedrijf veranderde het crawlergedrag niet. Uitgevers merken op dat training niet langer wordt genoemd, maar ook niet uitdrukkelijk verboden is. Bron: https://www.theverge.com/tech/1013409/meta-removes-language-that-may-have-allowed-it-to-scrape-news-sites

**Nvidia ontkende de RTX 5090 te stoppen terwijl het aanbod krapper werd.** Tom's Hardware vond de kaart niet bij meerdere grote winkels en zag op Amazon aanbiedingen rond 8.500 dollar. Volgens Nvidia gaat de productie door. Bron: https://www.tomshardware.com/pc-components/gpus/nvidia-reportedly-insists-the-rtx-5090-isnt-dead-despite-severe-shortages-and-removed-listings-at-multiple-retailers-flagship-gpu-is-missing-from-nvidias-store-and-commands-usd8-500-on-amazon

**Apple-topman John Ternus noemde het tekort aan geheugenchips “absoluut een crisis”.** Het tekort dat AI-servers en GPU's raakt, beperkt nu consumentenapparaten. Volgens berichtgeving testte Apple Chinese geheugenleveranciers te midden van Amerikaanse politieke druk. Bron: https://thenextweb.com/news/john-ternus-time-interview-memory-crisis-iphone-duo

## Om in de gaten te houden

DeepSeek rekent vanaf 1 november 0,75 dollar per 1.000 Search- of Fetch-aanroepen. De gewijzigde commerciële voorwaarden van Meta gaan op 30 oktober in.
