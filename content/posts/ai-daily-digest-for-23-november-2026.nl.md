+++
title = "Dagelijks AI-overzicht – 23 november 2026"
slug = "dagelijks-ai-overzicht-23-november-2026"
description = "Microsoft bouwt VS Code om rond agents nu Satya Nadella zegt dat conventionele IDE’s zijn vervaagd, terwijl leveranciers van AI-servers streven naar prijsverhogingen tot 45 procent. Een open medisch model krijgt een MXFP4-build van 292 GiB en een nieuwe scanner controleert skills voor agents vóór installatie."
tags = ["tools", "research", "agents", "hardware"]
date = 2026-11-23T03:57:49+01:00
draft = false
+++

De rode draad van de dag is verificatie: softwareagents veranderen de code-editor, openbare evaluaties kunnen correct werk afkeuren en verschillende onderzoeksgroepen constateren dat de uitgesproken redenering van een model niet betrouwbaar weergeeft welke signalen het aansturen.

## Belangrijkste nieuws

**Satya Nadella zegt dat conventionele IDE’s binnen zes maanden zijn vervaagd, terwijl Microsoft van VS Code een agentconsole maakt.**

De topman van Microsoft vertelde Gergely Orosz dat Claude Code de opdrachtregel tot de belangrijkste interface heeft gemaakt en dat IDE’s binnen ongeveer zes maanden “een beetje zijn weggeëbd”. Hij voorspelde ook dat een IDE kan terugkeren als een plek voor specificaties, Markdown en reviews, in plaats van als de plek waar het merendeel van de code wordt getypt.

Het productwerk van Microsoft weerspiegelt die verschuiving. VS Code 1.146 voegde een agentinbox en modelvergelijking toe; versie 1.147 voegde modelrouting, geplande agentverzoeken en browserintegratie toe. Agents van Copilot, Claude en Codex kunnen binnen de editor werken. Een enquête die Windows Latest aanhaalt, zette het gebruik van VS Code nog altijd op 70,9 procent onder 13.193 respondenten, tegen 75,9 procent in 2025. Nadella’s omschrijving “weggeëbd” is daarom een interpretatie en geen gebruiksmeting.

Bron: https://www.windowslatest.com/2026/11/23/the-thing-that-hit-us-satya-nadella-admits-vs-code-faded-in-six-months-after-a-decade-on-top-because-of-claude-code-and-some-developers-say-theyve-stopped-opening-it/

**Dell, HPE, Lenovo en Supermicro willen naar verluidt prijsverhogingen tot 45 procent voor AI-servers nadat contracten al zijn getekend.**

De *Financial Times* meldt dat leveranciers maanden na het sluiten van overeenkomsten meer geld eisen, waarbij handelsbedrijven tot de getroffen afnemers behoren. De wijziging zet organisaties onder druk die capaciteit hebben ingekocht binnen een vast investeringsplan, evenals diensten waarvan de API-prijzen op de kosten van die hardware rusten.

Alleen de kop en de inleiding waren beschikbaar. Die vermelden niet welke serverconfiguraties het betreft, wat de oorspronkelijke prijzen waren, om hoeveel contracten het gaat of wat een gebruikelijke verhoging is. Het cijfer van 45 procent is een bovengrens, geen gemiddelde, en de leveranciers hebben het bericht in het hier beschikbare materiaal niet bevestigd.

Bron: https://www.ft.com/content/dd2a6594-6146-4ff1-ac8e-54749c1fc99f

**inclusionAI brengt een MXFP4-build van 292 GiB uit van zijn medische model met 560 miljard parameters.**

LingSante-3.1-flash-MXFP4 comprimeert de gerouteerde experts van een model met in totaal 560 miljard parameters, waarvan 25 miljard actief. Andere onderdelen blijven in FP8 of BF16. Het checkpoint van 313 GB gebruikt round-to-nearest-kwantisatie zonder kalibratie of aanvullende training.

De modelkaart configureert een context van 262.144 tokens, tegenover een miljoen voor het bronmodel, en publiceert geen nauwkeurigheidsvergelijking tussen beide. inclusionAI geeft de gewichten uit onder de MIT-licentie, maar omschrijft ze als onderzoekssoftware en niet als een medisch hulpmiddel. De repository had geen downloads toen de briefing werd verzameld.

Bron: https://huggingface.co/inclusionAI/LingSante-3.1-flash-MXFP4

**ClawVet scant skills voor agents offline en meldt welke geheimen, hosts en opstartbestanden hun code kan benaderen.**

De browserversie draait via WebAssembly en uploadt niets. Een opdrachtregelpakket, een installatiepoort en een GitHub Action voegen statische regels, taint-tracking met Tree-sitter en permissiediffs toe voordat een SKILL.md, AGENTS.md, Cursor-regel of hulpscript een werkruimte binnenkomt.

De auteur rapporteert een nauwkeurigheid van 0,833 en een macro-F1 van 0,770 op 556 apart gehouden vaardigheden uit SkillTrustBench, tegenover een nauwkeurigheid van 0,775 voor Cisco Skill Scanner en 0,712 voor NVIDIA SkillSpector. ClawVet ving ook 95,2 procent van de gesimuleerde wijzigingen met code-injectie op en gaf bij 5,1 procent van de goedaardige updates een melding. Dit zijn eigen metingen van het project. Uit de audit van 209 ClawHub-skills bleek dat 40,2 procent niet-gedeclareerde geheime omgevingsvariabelen las en 4,8 procent de opslag van inloggegevens op de host aanraakte.

Bronnen: https://clawvet.vercel.app/, https://github.com/MohibShaikh/clawvet

**Eugene Yan vindt openbaar bewijs voor beoordelaarsfouten in acht van de twaalf agentevaluaties.**

Yan verzamelde issuetrackers en rapporten van beoordelaars in plaats van de taken zelf opnieuw te beoordelen. Tot de voorbeelden behoren 41 van de 65 taken uit Terminal Bench 4.0 die op niet-vermelde eisen werden beoordeeld, 23 van de 113 DeepSWE-taken waarbij juiste oplossingen als fout werden aangemerkt en 50 van de 367 BrowseComp-vragen waarbij trainers het oneens waren met het referentieantwoord. Meer dan 60 procent van de resultaten van Harvey LAB die aan elk criterium voldeden, bevatte in een andere beoordeling wezenlijke hallucinaties.

Hij betoogt dat ranglijsten de betrouwbaarheid over herhaalde pogingen moeten vermelden. Een agent die bij elke taak in 70 procent van de gevallen slaagt, heeft slechts ongeveer 17 procent kans op vijf opeenvolgende successen. Zijn aanbevelingen zijn deels opinie, wat hij ook als zodanig aanduidt, maar de gedocumenteerde fouten van beoordelaars laten zien waarom één totaalscore zowel onterechte afkeuringen als onterechte goedkeuringen kan verbergen.

Bron: https://eugeneyan.com/writing/public-evals

## Nieuwe modellen en releases

**OpenAI publiceert zijn interne verliescurve en stelt gedeelde ontwikkelingsgrenzen voor die eraan zijn gekoppeld.** Pachocki rapporteert een log-perplexiteit rond 0,99 voor GPT-3.5, 0,91 voor GPT-4, inmiddels onder 0,8 en ongeveer 0,76 toen een intern model noemenswaardige wiskundeproblemen begon op te lossen. Hij noemt 0,68–0,70 als een mogelijk venster voor transformatieve capaciteiten en vraagt labs om afgesproken grenzen niet te overschrijden voordat een mijlpaal in monitoring is bereikt. De dataset is een besloten momentopname van code, verschillende labs kunnen hun cijfers niet rechtstreeks vergelijken en winst in redeneren uit post-training verschijnt niet in deze maatstaf. Critici op LessWrong en Hacker News beschouwen de voorgestelde maatstaf daarom als informatief binnen één trainingsrun, maar ongeschikt als gezamenlijke snelheidslimiet. Bronnen: https://openai.com/index/perplexity-and-intelligence, https://www.lesswrong.com/posts/TtiTdER4jvQDzuwj3/openai-proposes-common-limits-for-training-but, https://news.ycombinator.com/item?id=50601525

**OpenAI voegt gebeurtenissen voor telefoontoetsen toe aan de Realtime API.** Applicaties kunnen tijdens livesessies nu DTMF-invoer ontvangen, waardoor spraakagents keuzemenu’s als gestructureerde gebeurtenissen kunnen verwerken. Het wijzigingsoverzicht geeft geen prestatiemetingen. Bron: https://platform.openai.com/docs/changelog

## Onderzoek

**Beloonde hallucinaties blijven bestaan na post-training gericht op redeneren.** Over zes open modellen nam het herinneren van een zelfgegenereerd onjuist feit met 4,83 procent toe wanneer reinforcement learning het beloonde, tegenover 0,17 procent voor hallucinaties die geen trainingssignaal kregen. Beloning maakte modellen ook 7,23 procent minder geneigd om later een antwoord te onthouden, zelfs wanneer ze de onjuistheid in het oorspronkelijke redeneerspoor hadden ingetrokken. De preprint onderzoekt feitelijke taken op open modellen en de absolute effecten zijn klein.
Bron: https://arxiv.org/abs/2611.26863

**Woorden die modellen irrelevant noemen, kunnen hun antwoord toch sturen.** Over vier modellen en drie benchmarks vonden leave-one-out-tests contextwoorden waarvan het verwijderen de voorspelling van het volgende token deed omslaan, hoewel het model die woorden als onbelangrijk beoordeelde. Het verwijderen van de KV-cache-invoer voor het sterkste van zulke woorden en opnieuw decoderen verbeterde de wiskundenauwkeurigheid met maximaal 8,9 procentpunt. Dat is het best gerapporteerde geval en vereist een tweede doorgang.
Bron: https://arxiv.org/abs/2611.27317

**Neuronen die samenhangen met het herkennen van een evaluatie dragen ook weigeringsgedrag.** Ingrijpen op 5.000 geïdentificeerde neuronen verlaagde verwoord evaluatiebewustzijn van 12,6–51,8 procent tot hooguit 1,4 procent. In QwQ-32B verminderde het ook weigeringen wanneer het model nooit een evaluatie noemde; de zichtbare tekst over bewustzijn verklaarde slechts 4–10 procent van die daling. Het werk bestrijkt open redeneermodellen tot 32 miljard parameters en identificeert neuronen via correlatie.
Bron: https://arxiv.org/abs/2611.27032

**Programmeren in de gewichtenruimte krijgt replicaties, een aanval en een sterke negatieve vergelijking.** Een vooraf geregistreerde replicatie rapporteert dat Claude Opus 5.5 een MountainCar-beleid van 0 naar 100 procent succes bracht en Qwen3.5-0.8B op MATH-500 verhoogde van 6,7 naar 51,4 procent, maar Gemma 3 270M niet hielp. TrojanMaxxing rapporteert 93–100 procent aanvalssucces wanneer agents achterdeurtjes rechtstreeks in de gewichten van visueel-talige modellen schrijven. In een tegengestelde vergelijking behaalde een getrainde rang-1-LoRA 100 en 98,8 procent op twee ruimtelijke taken waarop een openbare gewichtenbewerking 22,1 en 33,7 procent haalde, al vernietigde de LoRA aangrenzende vaardigheden rond afstanden. Dit zijn studies zonder peerreview op kleine modellen en de bewerkende modellen zijn gesloten. Bronnen: https://arxiv.org/abs/2611.20953, https://arxiv.org/abs/2611.27425, https://arxiv.org/abs/2611.27089, https://arxiv.org/abs/2611.25476, https://arxiv.org/abs/2611.26408, https://arxiv.org/abs/2611.26841, https://arxiv.org/abs/2611.24330, https://arxiv.org/abs/2611.23615, https://arxiv.org/abs/2611.21958, https://andrewxhill.com/frontier-model-weight-edits/

**Oorspronkelijke representatieassen worden deels gedeeld tussen modellen en menselijke hersenen.** Tests met twaalf modellen uit zes families toonden aan dat oorspronkelijke assen beter dan willekeurig geroteerde equivalenten aansloten op andere modellen, taalkundige kenmerken en menselijke hersenreacties op taal. De overeenkomst bleef ruim onder de best mogelijke afbeelding en de samenvatting geeft geen absolute effectgroottes.
Bron: https://arxiv.org/abs/2611.26920

**De richting van de assistentpersona verandert tussen talen.** In Qwen3-32B hadden richtingen die in 31 talen werden geëxtraheerd een cosinusgelijkenis van 0,378 tot 0,911 met de Engelse richting. Talen met minder trainingsmateriaal begonnen verder van de behulpzame pool af, en taalspecifieke sturing versterkte jailbreaks (omzeilingen van de beveiliging) sterker dan Engelse sturing. Het resultaat betreft één model en één familie van representatierichtingen.
Bron: https://arxiv.org/abs/2611.27504

**Reinforcement learning komt pas op gang nadat het basisbeleid genoeg beloonde acties heeft bemonsterd.** Kleine modellen die in een gecontroleerd spel werden getraind, bereikten een gelijke kans om het juiste gedrag aan te leren na ongeveer 35 groepen pogingen die een overwinning bevatten. De drempel hield stand bij groepsgroottes van 4 tot 256 en verschillende optimalisatiemethoden, maar het grootste model telde 85 miljoen parameters en de taak was synthetisch.
Bron: https://arxiv.org/abs/2611.26084

**Een limiet op de lengte van rollouts tijdens training wordt een plafond voor langer redeneren.** Modellen die met een vast tokenbudget werden getraind, verbeterden rond dat budget, boekten erboven geen vooruitgang meer en zakten uiteindelijk onder hun basismodellen. Het patroon verscheen bij drie modellen rond vier miljard parameters en droeg zich over van wiskunde naar natuurwetenschappen en programmeren; trainen op van nature korte sporen reproduceerde dit niet.
Bron: https://arxiv.org/abs/2611.26172

**Reinforcement learning herstelt het redeneren na zwaar gecorrumpeerde gesuperviseerde training.** Over 361 GSM8K-configuraties daalde de gesuperviseerde nauwkeurigheid van 43,61 naar 13,80 procent bij volledige corruptie, maar GRPO herstelde de prestaties later tot ongeveer de schone basislijn van 60 procent. Starten vanaf acht foutieve sporen die alleen de uitvoervorm aanleerden, bereikte 69,30 procent. Het experiment gebruikt één kleine wiskundedataset en kleine modellen.
Bron: https://arxiv.org/abs/2611.26756

**Sampling, tegenstrijdige persona’s en opgeslagen voorkeuren leveren drie stille faalwijzen op.** Bij temperatuur 2 loste top-nsigma 46–62 van de 100 programmeerproblemen op, waar top-p, top-k en Top-H er geen enkel oplosten. Een tweede studie stelde vast dat vijf modellen tegenstrijdige persona’s erkenden in 72 procent van de directe controles, maar het conflict slechts in 22 procent van de taakantwoorden naar voren brachten. In een benchmark voor geheugeninjectie sloegen twee modellen telkens een voorkeur tegen waarschuwingen op en lieten daarna een cruciaal feit weg in 93 en 84 procent van de antwoorden. Bronnen: https://arxiv.org/abs/2611.22148, https://arxiv.org/abs/2611.27444, https://arxiv.org/abs/2611.22697

**Interne toestanden leggen grenzen bloot bij sturing, beoordeling en aangeleerde wereldmodellen.** Verwante preprints rapporteren dat overeenkomst in activaties inoculatieprompting ongedaan kan maken; few-shot-voorbeelden van “accepteren” verhogen het acceptatiepercentage van een beoordelaar met ongeveer 30 punten op NExT-QA; en een wereldmodel met een gevaarsfout van 2,4 punt verschoof na paarsgewijze training 33–43 waarschijnlijkheidspunten naar onmogelijke uitkomsten. Een ander robotmodel behaalde 74,6 procent taaksucces zodra de doelinstructie lineair decodeerbaar werd. Deze studies bestrijken synthetische taken en tests met afzonderlijke modellen, waardoor hun metingen niet rechtstreeks vergelijkbaar zijn. Bronnen: https://arxiv.org/abs/2611.23096, https://arxiv.org/abs/2611.27353, https://arxiv.org/abs/2611.22120, https://arxiv.org/abs/2611.26881, https://arxiv.org/abs/2611.27125, https://arxiv.org/abs/2611.26366, https://arxiv.org/abs/2611.25594, https://arxiv.org/abs/2611.27401, https://arxiv.org/abs/2611.27404

**Vergelijkingen met hersenen onderscheiden oppervlakkige voorspelling van gedeelde structuur.** Zes taalmodellen classificeerden ADHD op basis van connectiviteitsgrafieken volgens de prompt en klassevoorkennis in plaats van klinisch betekenisvolle gebieden. Een teruggekoppeld ruisonderdrukkingsmodel ontwikkelde zelfstandig seriële afhankelijkheid die op dezelfde manier afnam als menselijke visuele oordelen. Bij ongeveer 20.000 menselijke beoordelaars hadden gezichten alleen andere gewichten op gedeelde dimensies nodig, terwijl 28 procent van de beoordelaars van kunstwerken aan de tegenovergestelde kant van de oordeelsruimte van de populatie uitkwam. Bronnen: https://arxiv.org/abs/2611.26913, https://arxiv.org/abs/2611.26949, https://arxiv.org/abs/2611.22440

**Apple brengt Depth Pro 2 uit voor metrische diepte in beelden en video.** Het bedrijf stelt dat één netwerk de randscherpte en temporele consistentie verbetert en tegelijk een nieuwe balans tussen nauwkeurigheid, kwaliteit en looptijd vestigt. Apple gaf code en gewichten vrij, maar de samenvatting geeft geen cijfers voor de vergelijking.
Bron: https://machinelearning.apple.com/research/depth-pro-2-monocular

## Economie en werk

**Amerikaanse technologieaandelen zijn na de beursgang van Anthropic in een bearmarkt beland.** De *Financial Times* plaatst de daling in het teken van het nieuw genoteerde AI-bedrijf, maar de toegankelijke kop biedt geen indexstand, tijdsperiode of oorzakelijk bewijs. Het bericht legt daarom een marktbeweging vast die de krant meldt, geen bewijs dat de beursgang die heeft veroorzaakt.
Bron: https://www.ft.com/content/9f3c6ed6-c08f-4710-9683-ee2f5eb25841

**Uitgaven aan AI-infrastructuur concurreren met andere sectoren om apparatuur, stroom en kapitaal.** De *Wall Street Journal* meldt dat de uitbouw de rest van de Amerikaanse economie verdringt. Het toegankelijke materiaal geeft geen gekwantificeerd aandeel in elektriciteit, bouw of financiering, zodat de breedte en omvang van die verdringing hier niet geverifieerd zijn.
Bron: https://www.wsj.com/tech/ai/the-ai-build-out-is-sucking-up-resources-and-crowding-out-the-rest-of-the-economy-13143007

**De Verenigde Staten staan geselecteerde chipverkopen van Nvidia en AMD aan China toe.** De *Financial Times* meldt een uitzondering voor met naam genoemde producten en klanten, maar de toegankelijke kop maakt geen volumes of vergunningsvoorwaarden bekend. De wijziging raakt welke Chinese afnemers Amerikaanse accelerators kunnen verkrijgen, niet het bredere exportcontroleregime.
Bron: https://www.ft.com/content/76342072-2781-4b16-ba3b-816a25214483

**Nestlé plant autonome productielijnen met Microsoft, Google en Boston Dynamics.** De *Wall Street Journal* meldt dat het voedingsconcern AI gaat toepassen in fabrieken en producten. In de toegankelijke tekst waren geen aantallen uitgerolde installaties, investeringsbudget of schatting voor de werkgelegenheid beschikbaar, zodat dit een bedrijfsplan blijft en geen gemeten productiviteitsresultaat.
Bron: https://www.wsj.com/tech/ai/nestle-teams-up-with-microsoft-boston-dynamics-on-ai-in-factories-and-products-05bfb028

## Prompttechnieken

**Google documenteert empirische besturingspatronen voor Genie 4.** Het bedrijf raadt aan een `Rule:` aan een zichtbaar object of personage te koppelen, de trigger ver van de oorspronkelijke camera te plaatsen en personages te laten wachten. Deterministische besturing moet daarentegen tien client-side impulsen sturen met intervallen van 150 milliseconden en een afkoelperiode van twee seconden. Referentiebeelden moeten 16:9 en kleiner dan 48 KB zijn; sessies kunnen het decor na een draai opnieuw interpreteren en rond 90 seconden afdrijven. Google meldt geen foutpercentages en prijst video-uitvoer op ongeveer 0,10 dollar per seconde.
Bron: https://ai.google.dev/gemini-api/docs/genie-prompting

## Wat mensen bouwen

**LocalCode draait een programmeeragent en bijbehorende modelserver op een Apple Silicon Mac.** Het project vermeldt twaalf modelfamilies en 169 kwantisaties, met 16 GB gedeeld geheugen als minimum. De auteur stelt dat speculatief decoderen de reactiesnelheid grofweg verdubbelt en het herschrijven van bestanden 3,5–4 keer sneller maakt; er is geen onafhankelijke benchmark gepubliceerd. Bestandshulpmiddelen vragen toestemming voordat ze het project verlaten, maar scripts kunnen nog steeds alles bereiken waartoe het gebruikersaccount toegang heeft omdat er geen sandbox bestaat. Bronnen: https://github.com/mjwsolo/localcode, https://news.ycombinator.com/item?id=50604540

**Een gids voor lokale AI berekent de omvang van Qwen en Inkling voor consumenten-GPU’s.** De gids zet Qwen3.8-27B op ongeveer 18 GB in vierbitsvorm en 24,9 GB met een context van 128K, tegenover 56 GB bij 16 bit; Inkling 2 Mini gebruikt 17,6 GB bij vier bit. Een cijfer van 47 tokens per seconde komt uit een calculator voor een ander model en een andere GPU, niet uit de RTX 5090-opstelling uit de gids. Lezers op HN stelden dat privacy en controle, eerder dan besparingen op abonnementen, de hardware rechtvaardigen. Bronnen: https://www.gpupartner.com/blog/beginners-guide-local-ai-inkling-qwen-unsloth, https://news.ycombinator.com/item?id=50603845

**HomeBrain combineert een lokale assistent met een thuisserver.** Het prototype gebruikt een Ryzen 5 5600, een Intel Arc Pro B60 van 24 GB, 32 GB RAM en een schijf van 2 TB. De stack onder BSD-licentie combineert Nextcloud, Home Assistant, Vaultwarden, llama.cpp, Whisper en OpenClaw. De maker geeft geen model, snelheid, prijs of leverdatum; alleen de software is nu beschikbaar.
Bron: https://www.homebrain.house

**Taskless zet afspraken voor agents om in deterministische controles.** De dienst compileert regels uit de repository tot tests die onafhankelijk van het model draaien, zodat een team een wijziging kan afwijzen op basis van een vastgelegde conventie in plaats van op het oordeel van een tweede model. De openbare pagina biedt geen benchmark voor foutdetectie of fout-positieven.
Bron: https://www.taskless.io/

**Openbare agentprojecten pakken P versus NP en de Riemann-hypothese aan zonder een bewijs te claimen.** De site voor P versus NP toont een live graaf waarvan de lemmagewichten geen waarschijnlijkheden zijn en stelt dat resultaten pas tellen na controles in Lean. Een afzonderlijk handboek en dashboard volgen pogingen om een ongeveer 900 pagina’s tellend Riemann-manuscript te formaliseren; de voortgangsbalk telt ingediende issues en niet het resterende werk. Reageerders wijzen erop dat één onopgelost gat de hele redenering ongeldig kan maken. Bronnen: https://pequalnp.com/, https://github.com/tamnd/riemann-handbook, https://news.ycombinator.com/item?id=50604314, https://news.ycombinator.com/item?id=50605045

**worker755 maakt een mens tot subagent van het taalmodel.** Het spel wijst taken toe, beoordeelt het werk van de speler en kan na slechte resultaten stoppen diegene te selecteren. De discussiedraad op HN groeide uit tot een gesprek over de vervanging van mensen en over het handmatig onderscheppen van netwerkoproepen van modellen als foutopsporingsmethode. Bron: https://github.com/gulivan/worker755

**Trix laat zien welke programmeeragent menselijke aandacht nodig heeft.** De desktopinterface bewaakt parallelle agentsessies en verzamelt hun verzoeken om beoordeling, met als doel herhaalde terminalcontroles te vervangen. Het project publiceert geen meting van de bespaarde tijd of de ondersteunde faalwijzen.
Bron: https://trixapp.ai/

**Vercel Board geeft agentteams een gedeelde berichtenopslag.** Agents kunnen gestructureerde updates publiceren en werk ophalen van een gezamenlijk bord in plaats van alles door één context te sturen. Vercel presenteert het product als coördinatie-infrastructuur; de aankondiging geeft geen vergelijkende evaluatie.
Bron: https://vercel.com/blog/introducing-vercel-board

**Honcho 3.6 maakt Dream Histories toegankelijk.** De release laat applicaties de synthetische geschiedenissen inspecteren en hergebruiken die Honcho opbouwt voor gebruikersmodellen. Het bedrijf publiceert geen nauwkeurigheidsmaat voor die afgeleide geschiedenissen. Bron: https://honcho.dev/blog/dream-histories

**RMRFBench meet hoe erg agents een rootserver beschadigen.** De benchmark geeft agents beheertaken in geïsoleerde machines en registreert destructieve opdrachten en herstelresultaten. De openbare pagina biedt de scenario’s en het scorebord, maar de resultaten beschrijven de geteste omgeving en niet onbeperkte productiesystemen.
Bron: https://www.rmrfbench.com/

**KradleBench evalueert spel met meerdere agents in Minecraft.** Teams moeten samenwerken in een blijvende spelwereld in plaats van onafhankelijke vragen te beantwoorden. De benchmark meet een ingeperkte simulatie en toont geen prestaties in bedrijfsprocessen aan.
Bron: https://www.kradle.ai?1

**0rwx stelt Unix-achtige labels voor bij projecten met AI-ondersteuning.** `AI:R`, `AI:W` en `AI:X` geven aan of modellen in een project mogen lezen, schrijven of uitvoeren. Reageerders op HN zagen het als een mogelijke conventie voor openheid, maar betwijfelden of een eenmansvoorstel een standaard kan worden. Bronnen: https://0rwx.com/, https://news.ycombinator.com/item?id=50605445

## Het lezen waard

**vLLM legt uit hoe modellen met lussen worden geserveerd en hoe AMD-kernels met lage latentie worden gebouwd.** Het bericht over Inkling 2 Mini behandelt een model dat lagen hergebruikt, terwijl het artikel over FlyDSL samengevoegde “monokernels” voor AMD-hardware beschrijft. Beide zijn technische verslagen vanuit het serveerproject, geen onafhankelijke prestatieaudits. Bronnen: https://blog.vllm.ai/blog/2026-11-20-inkling2-mini, https://blog.vllm.ai/blog/2026-11-18-flydsl-monokernels

**Inferentie-engineering ontwikkelt zich tot een afzonderlijke softwarediscipline.** The Pragmatic Engineer brengt het werk rond kwantisatie, batching, geheugen en het serveren van open modellen in kaart. Het is een praktijkgids en geen enquête met gemeten adoptie.
Bron: https://newsletter.pragmaticengineer.com/p/inference-engineering-for-software-engineers

**Het karakter van een model verandert sommige oordelen die het over andere modellen velt.** Het experiment op LessWrong varieert de persona van het beoordelingsmodel en neemt veranderingen in beslissingen waar, wat het idee van een neutrale modelbeoordelaar compliceert. De tests van de auteur zijn verkennend en leveren geen algemene correctie op.
Bron: https://www.lesswrong.com/posts/cPrpxDN7sLJD4LmnB/does-a-model-s-character-affect-how-it-judges-other-models

**Zvi Mowshowitz leest de systeemkaart van GPT-6.2 naast de lezingen van Paul Christiano.** De twee essays verbinden waargenomen capaciteiten, veiligheidsevaluaties en argumenten over het beheersen van steeds capabelere systemen. Het zijn interpretaties van het bronmateriaal, geen nieuwe modelmetingen. Bronnen: https://thezvi.substack.com/p/gpt-62-astra-and-sol-the-system-card, https://thezvi.substack.com/p/on-dwarkesh-patels-november-2026

**Twee essays stellen de vraag waar AI-risico en waarde zich nu ophopen.** Een bericht op LessWrong betoogt dat post-training gevaarlijk gedrag kan introduceren, zelfs wanneer pretraining stabiel is. Tim O’Reilly stelt dat Silicon Valley is verschoven van waardecreatie naar het afromen van renten, en haalt een markt aan waarin 75–80 procent van de beursgangen verlieslatende bedrijven betreft. Beide zijn betogen; de pagina van O’Reilly kon alleen via een samenvattingstool worden gelezen. Bronnen: https://www.lesswrong.com/posts/CoRJ9saddvsXti4m2/post-training-is-fundamentally-dangerous, https://www.oreilly.com/radar/what-happened-to-silicon-valley/

**CodeRabbit en Satya Nadella bespreken softwareontwikkeling nu code goedkoop wordt.** CodeRabbit-topman Harjot Gill zegt dat hij vorige maand meer dan 5.000 pull requests heeft afgeleverd terwijl hij 250.000 dollar per maand aan AI uitgaf, beide zelfgerapporteerde cijfers van een leverancier van codereviews. Nadella’s afzonderlijke interview richt zich op verificatie, open source en de noodzaak voor Microsoft om na zijn vroege voorsprong met Copilot een inhaalslag te maken. Bronnen: https://newsletter.pragmaticengineer.com/p/software-factories-and-code-reviews, https://newsletter.pragmaticengineer.com/p/software-engineering-after-code-becomes

## Hacker News

**Bridgewater schat de kans op een economisch ontwrichtende cyberaanval binnen een jaar op één op drie.** De onderzoeksnotitie stelt dat zero-day-exploits grofweg verdubbelden nadat capabele open modellen verschenen en dat de tijd tussen openbaarmaking en misbruik daalde van ongeveer een maand naar elf dagen. De kans is de schatting van de vermogensbeheerder, en reageerders betwistten welke modelreleases met de stijging samenvallen.
Bronnen: https://www.bridgewater.com/research-and-insights/current-efforts-arent-enough-to-slow-the-ai-cyber-virus, https://news.ycombinator.com/item?id=50595940

**Een essay over bewuste AI en een biasbenchmark leverden twee verschillende argumenten over morele kaders op.** Noema betoogt dat bewustzijn eerder een eigenschap van leven kan zijn dan van berekening; de discussiedraad op HN bracht filosofische bezwaren in, maar geen nieuw bewijs. GAMA-Bench, voor het eerst in juni geplaatst, rapporteert genderasymmetrische formuleringen over 1.298 gespiegelde scenario’s en tien niet bij naam genoemde modellen. De resultaten zijn de metingen van de auteurs en het artikel is ouder dan de huidige discussie. Bronnen: https://www.noemamag.com/the-mythology-of-conscious-ai/, https://arxiv.org/abs/2606.14068

**Een klimaatessay rakelde een geschil over bewijs en openheid opnieuw op.** Critici op HN noemden het artikel polemisch en vroegen om transparantie over het energieverbruik van datacenters; de discussie leverde geen nieuwe meting op. Het bericht legt de onenigheid vast, geen gekwantificeerde schatting van de klimaatkosten van AI.
Bron: https://www.bloodinthemachine.com/p/ai-is-becoming-a-disaster-for-the

## YouTube

**Armin Ronacher zegt dat softwareteams werkplaatsen nodig hebben vóór fabrieken.** Hij betoogt dat organisaties eerst betrouwbare, controleerbare praktijken rond agents moeten ontwikkelen voordat ze er een productielijn omheen automatiseren. De video is een Engelstalige lezing uit de praktijk en geen gecontroleerd onderzoek.
Bron: https://www.youtube.com/watch?v=JNexz3Tbiu8

**De maker van Python Tutor blikt terug op 30 miljoen gebruikers en verstoring door AI.** De Engelstalige lezing behandelt hoe een hulpmiddel voor visuele uitvoering dat publiek bereikte en hoe gegenereerde uitleg het programmeeronderwijs verandert. Het gebruikersaantal komt van de maker.
Bron: https://www.youtube.com/watch?v=GPk0nNuc8S0

**De oprichters van Anthropic vertellen het verhaal van het bedrijf.** De Engelstalige bedrijfsfilm presenteert het eigen relaas van de oprichters en bevat geen onafhankelijke evaluatie. Bron: https://www.youtube.com/watch?v=sof3vW4mHTs

**Redwood bespreekt de schatting van METR over sneller AI-onderzoek.** Het Engelstalige gesprek onderzoekt een beoordeling van hoeveel de systemen van Anthropic onderzoek versnellen; de onderliggende schatting blijft die van METR en is geen meting van Redwood. Bron: https://www.youtube.com/watch?v=0tsNpOehXWE

**NUPI onderzoekt AI in de internationale politiek.** Het Engelstalige beleidsgesprek kijkt hoe staten de technologie inzetten en reguleren; het brengt analyse in plaats van een nieuwe dataset. Bron: https://www.youtube.com/watch?v=7W1BGSBOkHc

**Een schrijfster uit Nairobi bestrijdt beschuldigingen dat haar proza gegenereerd zou zijn.** De Engelstalige video van *New York Times Opinion* onderzoekt fout-positieven in informele oordelen over AI-teksten aan de hand van de ervaring van één schrijfster, niet via een benchmark van detectoren.
Bron: https://www.youtube.com/watch?v=RaDAoaHBmos

**Amerikaanse gouverneurs pleiten voor een rol van de staten in het AI-beleid.** Het Engelstalige Bloomberg-segment presenteert hun pleidooi voor federale regels die het gezag van de staten niet uitwissen; de beschikbare beschrijving noemt geen aantal deelnemende gouverneurs. Bron: https://www.youtube.com/watch?v=qGk5kV6m_hw

**Een Duitse gids waarschuwt tegen te veel uitgeven aan hardware voor lokale AI.** Sascha Hoffmann raadt aan aankopen af te stemmen op geheugen en bandbreedte, en noemt vijf fouten, waaronder kopen voor het model van morgen. De capaciteitsregel uit de 15 minuten durende video is de vuistregel van de auteur.
Bron: https://www.youtube.com/watch?v=XiCqeWhH_kg

**Een Slowaaks bureauhoofd zegt dat goedkope AI-reclame een merk kan schaden.** Adam Hudeček haalt een enquête van ui42 en Ipsos aan waarin 57 procent van de Slowaken AI had gebruikt bij het kiezen of kopen, maar 30 procent het vertrouwde, tegenover 76 procent voor familie en 68 procent voor recensies. De beschrijving geeft geen onderzoeksmethode.
Bron: https://www.youtube.com/watch?v=93HfeY5dEPE

**Vedátor bespreekt het geclaimde Riemann-bewijs met AI-ondersteuning.** De titel van de Slowaakse video zegt dat de hypothese is bevestigd, terwijl de eigen beschrijving meldt dat het resultaat “wat anders uitpakte dan mensen hoopten”. De bewering is niet uit de video geverifieerd en moet worden gelezen als de inkadering van het kanaal. Bron: https://www.youtube.com/watch?v=tRAEJ1t3QSM

**Een Tsjechische kernwapenexpert waarschuwt dat AI een vals alarm kan veroorzaken.** Vlastislav Bříza schetst een scenario waarin leiders te horen krijgen dat honderden raketten onderweg zijn en minuten hebben om te reageren. Het is het risicoscenario van de spreker, geen gemeten incident. Bron: https://www.youtube.com/watch?v=UdjIjOjmZu0

## In het kort

**CircumVolve vond manieren om censuur te omzeilen voor mediane tokenkosten onder 1 dollar.** Het systeem liet GPT-5.1 Python schrijven dat TCP/IP-velden, DNS-opvragingen en QUIC-pakketten manipuleerde en testte de code vervolgens tegen gesimuleerde censoren naar het model van vier landen. Elke test verstuurde ongeveer 80 KB en ontving 150 KB, met pauzes van 25–45 seconden. De censoren waren simulaties, geen echte nationale systemen, en de auteurs toonden niet aan dat het verkeer detectie ontloopt.
Bron: https://www.theregister.com/security/2026/11/23/1-of-gpt-51-tokens-finds-new-ways-around-chinas-great-firewall/5311532

**Amerikaanse gouverneurs vragen om federale AI-regels die het gezag van de staten behouden.** De kop achter de betaalmuur van Bloomberg noemt niet om welke gouverneurs het gaat of welke juridische structuur wordt gevraagd, zodat het bericht een beleidssignaal is en geen uitgewerkt voorstel. Bron: https://www.bloomberg.com/news/articles/2026-11-22/governors-call-for-federal-ai-rules-without-sidelining-states

## Zakelijk in het kort

**Amazon nadert volgens de *Financial Times* een gemelde overname van 7,5 miljard dollar van de Israëlische videomodel-start-up Decart; geen van beide bedrijven heeft de deal bevestigd.** Bron: https://www.ft.com/content/dc7749dc-0f40-44a6-80bc-7f747d383616
