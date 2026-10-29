+++
title = "Dagelijks AI-overzicht – 29 oktober 2026"
slug = "dagelijks-ai-overzicht-29-oktober-2026"
description = "Google kondigde Gemini 4 Carbon aan, maar beperkte de toegang tot cyberverdedigers. Verkeer van agents dwong GitHub vier miljoen extra CPU-kernen te plannen, terwijl de beste belastingagent voor slechts 10,8 procent van de professionele opdrachten slaagde."
tags = ["models", "research", "agents", "business"]
date = 2026-10-29T04:04:47+01:00
draft = false
+++

De sterkste resultaten van vandaag verbinden indrukwekkende prestaties met de systemen die mensen nodig hebben om erop te vertrouwen, ze te financieren en ze te gebruiken. Toegang, professioneel oordeel en infrastructuur blijven even belangrijk als modelscores.

## Belangrijkste nieuws

**Google kondigde Gemini 4 Carbon aan als zijn sterkste model, maar alleen geselecteerde cyberverdedigers kunnen het gebruiken.** Volgens Google scoort Carbon 59 op de Artificial Analysis Intelligence Index v5. Het bedrijf meldt ook 88,2 procent op SEC-bench Pro, 54,8 procent op ExploitGym en 71,0 procent op CWE-bench. Alle cijfers komen van Google en de aankondiging bevat geen link naar een onafhankelijke evaluatie of een modelkaart voor Carbon.

Toegang begint via Googles Fairwind-programma en wordt later uitgebreid naar vertrouwde partners. Het bedrijf neemt ook deel aan het vrijwillige programma van de Amerikaanse overheid om modellen vóór hun release te testen. Voor ontwikkelaars, bedrijven en consumenten is er geen releasedatum.

Google vermeldt een introductieprijs voor de API van 2 dollar per miljoen inputtokens en 10 dollar per miljoen outputtokens, die later stijgt naar 4 en 20 dollar. Google heeft een prijs gepubliceerd voordat het algemene toegang aanbiedt. De gefaseerde uitrol is daarom even belangrijk als de voorsprong op benchmarks. Bronnen: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/, https://news.ycombinator.com/item?id=50276792

**GitHub plant vier miljoen extra CPU-kernen en 160 PB snelle opslag nadat code van agents zijn platform onder druk zette.** GitHub registreerde in september 7,4 miljard commits, vijf keer zoveel als een jaar eerder. The Register schrijft herhaalde storingen sinds december toe aan het resulterende verkeer en reconstrueerde voor 7 mei een dieptepunt van ongeveer 84 procent voor GitHubs beschikbaarheid over 90 dagen.

Microsoft-bestuurder Jay Parikh zei dat GitHub rekenkracht en opslag van elkaar scheidt. Het bedrijf verwacht dat dit nieuwe ontwerp de verwerkingscapaciteit met een factor 35 vergroot. Het plant ook tegen begin volgend jaar een Azure-architectuur over meerdere regio’s en meer capaciteit voor GitHub Actions.

De cijfers meten volume, geen codekwaliteit. Toch tonen ze een concreet gevolg van agentische ontwikkeling voor de infrastructuur: gedeelde systemen die zijn gebouwd voor bijdragen op menselijke schaal moeten nu door machines gegenereerde activiteit verwerken. Bron: https://www.theregister.com/ai-and-ml/2026/10/28/github-powering-up-four-million-extra-cores-to-stop-its-service-going-down/5305863

**De beste agent slaagde voor slechts 10,8 procent van 50 professionele belastingopdrachten in Surge AI’s DAYJOB-benchmark.** De leverancier bouwde omgevingen met 1.789 bestanden en beoordeelde afgerond werk aan de hand van een beoordelingsschema met een drempel van 95 procent. Claude Sonnet 5.5 leidde, gevolgd door Claude Fable 5.1 met 9,6 procent en Claude Opus 5.5 met 9,2 procent.

De opdrachten vereisen dat agents tegenstrijdige gegevens met elkaar in overeenstemming brengen, problemen vinden die klanten niet hebben genoemd en aangiften, werkdocumenten of adviezen opleveren. In één geval vergeleek GPT-6 Astra twee mogelijke verkoopdata voor een woning correct, maar miste het in alle vijf pogingen een latere deadline voor een belastingvrijstelling ter waarde van maximaal 250.000 dollar. Claude Opus vond die in alle vijf.

Surge AI ontwikkelde en beoordeelde de benchmark, dus de resultaten zijn bewijs van de leverancier zelf. De kloof tussen vloeiend advies en een eindproduct dat aan professionele normen voldoet, is niettemin duidelijk. Bron: https://surgehq.ai/blog/dayjob-tax

**Een preprint vond dat de onderzochte latente wereldmodellen taken konden oplossen zonder hun omgevingen getrouw te modelleren.** Rodrigo Gonzalez Laiz en Steffen Schneider definiëren getrouwheid als overeenstemming tussen de toestandovergangen van de omgeving en de aangeleerde latente dynamiek. Zij introduceren consistentie van latente uitrol om te meten of voorspellingen die afhankelijk zijn van acties die structuur behouden.

Geen van de toonaangevende systemen in hun onderzoek loste zijn taak op via getrouwe dynamiek. Taakscores verborgen dus een verschil tussen het juiste resultaat produceren en een intern proces leren dat de omgeving volgt.

Het artikel werd op 27 oktober ingediend en heeft geen peerreview ondergaan. Het resultaat beperkt wat succes op benchmarks kan aantonen over het interne begrip van een agent, vooral wanneer een systeem over lange tijdshorizonten moet plannen. Bron: https://arxiv.org/abs/2610.37588

**Lao Gan Ma ontkende een gemelde claim dat AI het aantal werknemers aan één productielijn terugbracht van meer dan 600 naar 48.** Chinese media schreven het cijfer toe aan bestuurder Li Xin, samen met een claim dat AI-inspectie van pepers het aantal fouten tot bijna nul terugbracht. Het bedrijf zegt dat Li geen personeelsaantallen besprak en zijn volledige opmerkingen zijn niet openbaar.

Bedrijfsgegevens die Sixth Tone aanhaalt, tonen dat het aantal werknemers dat was aangesloten bij de sociale verzekering daalde van bijna 3.000 in 2022 naar 740 in 2025, een afname van ongeveer 75 procent. Dat toont niet aan dat AI de daling veroorzaakte; pensionering en personeelsverloop veranderen het cijfer ook.

Het geschil volgt op een verzoek van de Chinese Staatsraad aan werkgevers om vervanging van banen door AI af te remmen, werknemers te waarschuwen vóór grootschalige invoering en overgangsperioden en omscholing te bieden. De openbare claim, de ontkenning en de indicator voor personeelsomvang moeten gescheiden blijven. Bron: https://www.sixthtone.com/news/1019180

## Nieuwe modellen en releases

**NVIDIA bracht Nemotron 3.5 Transcribe uit, een spraakmodel met open gewichten en ondersteuning voor Tsjechisch en Slowaaks.** Het 30B-A4B-checkpoint heeft ongeveer 4,3 miljard actieve parameters, transcribeert 40 talen, vertaalt 31 talen van of naar het Engels en labelt sprekers in 13 talen. NVIDIA meldt een gemiddeld woordfoutenpercentage van 5,33 procent voor Engels en 4,62 procent over zeven talen; dit zijn de interpretaties van het bedrijf van ranglijsten van derden. Bronnen: https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B, https://huggingface.co/blog/nvidia/nemotron-transcribe-granary

**Sakana AI opende vroege toegang tot een API-platform voor bedrijven.** De dienst is compatibel met OpenAI en biedt aanvankelijk Sakana Fugu en Fugu Ultra, met instellingen voor werkruimten, auditlogs en budgetlimieten. Sakana zegt dat klantinvoer niet voor training zal worden gebruikt; aanvragers ontvangen prijzen privé. Bron: https://sakana.ai/api-platform-earlyaccess/

**OpenAI voegde maandelijkse API-tegoeden toe aan ChatGPT Pro- en Business-abonnementen.** Pro-abonnementen krijgen afhankelijk van het niveau 100, 200 of 500 dollar; Business krijgt 20 dollar per Standard-licentie en 100 dollar per Premium-licentie, samengevoegd tot maximaal 500 dollar per werkruimte. Tegoeden vervallen aan het eind van elke factureringsperiode en worden niet meegenomen naar de volgende. Bron: https://developers.openai.com/api/docs/guides/chatgpt-api-credits

**Anthropic breidde zijn AI for Science-programma uit naar 20 financierings- en onderzoeksorganisaties.** Partners zullen gratis Claude-tegoeden verdelen, al maakte Anthropic de waarde ervan niet bekend. Tot de genoemde projecten behoort een specificatie in onderzoeksversie voor agents die laboratoriuminstrumenten bedienen. Bron: https://www.anthropic.com/news/ai-for-science-expands-foundations-research-institutions

**xAI voegde aanpasbare moderatie-instellingen toe aan de Grok API.** Ontwikkelaars kunnen Grok via een `guidelines`-array vragen inhoud in de categorieën `nsfw`, `violence` en `profanity` te weigeren. Voor categorieën die worden weggelaten blijft het standaardmoderatiebeleid gelden. Bron: https://docs.x.ai/developers/advanced-api-usage/custom-moderation-controls

**Lightricks bracht optionele gewichten voor watermerken in LTX-2-video en -audio uit.** PixelSeal slaat 256 bits aan gegevens op in videoframes en AudioSeal markeert stereo-audio. Lightricks zegt dat de markeringen geen cryptografische handtekeningen zijn en dat het ontbreken van een markering niet bewijst dat de inhoud niet gegenereerd is. Bron: https://huggingface.co/Lightricks/LTX-2-Marking

## Onderzoek

**Een ongetrainde simulatie van het connectoom van een volwassen vlieg bereikte 95 procent van de geurbronnen.** Het netwerk van pulserende neuronen bevat 172.433 neuronen en werkt binnen een gesimuleerd lichaam. Een herbedrading die voor elk neuron het aantal verbindingen en hun tekens behield, bereikte 18 procent. Dat suggereert dat de bedrading veel van het geteste sensomotorische gedrag droeg. Bron: https://arxiv.org/abs/2610.33881

**LLM-plannen zonder hulpmiddelen werden minder zuinig naarmate de planningshorizon van schuifpuzzels groeide.** De auteurs verzamelden 8.400 plannen die in één poging werden gemaakt, zonder tools of feedback over de uitvoering, en onderscheidden geldige uitvoering, coördinatie en zuinigheid in het aantal handelingen. Sommige modellen voltooiden elke proef terwijl hun plannen steeds inefficiënter werden. Bron: https://arxiv.org/abs/2610.36415

**RLEC traint één model om te antwoorden of zich te onthouden volgens een expliciete betrouwbaarheidsdoelstelling.** De preprint verandert de beloning en de planning daarvan, zodat een gevraagde nauwkeurigheid van bijvoorbeeld 90 procent tijdens de training onderscheidbaar blijft. De auteurs melden één model dat meerdere doelstellingen volgt zonder een achteraf ingestelde drempel. Bron: https://arxiv.org/abs/2610.35059

**Distillatie behield één GPT-2-circuit en vernietigde een ander.** DistilGPT-2 behield 87,7 procent van de prestaties van het groter-dan-circuit door het naar een eerdere laag te verplaatsen. De nauwkeurigheid van zijn circuit voor indirecte objecten daalde echter van 94,8 naar 35,2 procent en er bleven geen aandachtshoofden behouden die namen verplaatsen. Geaggregeerde gelijkenismaten verborgen het verschil. Bron: https://arxiv.org/abs/2610.37157

**Stuurvectoren waren overdraagbaar tussen tekst- en beeldgeneratie in een geïntegreerd multimodaal model.** Een vector die uit teksttokens werd gevonden, veranderde de beelduitvoer zonder aanvullende training. Omgekeerd werkte het ook. De causale interventie suggereert dat sommige concepten in verschillende modaliteiten dezelfde implementatie delen. Bron: https://arxiv.org/abs/2610.36269

**GEPA-Curator filtert onbetrouwbare mislukkingen voordat het die gebruikt om een agentprompt te optimaliseren.** De methode verwijdert taken met ruis in de signalen en levert succesvolle eerdere trajecten als context. De auteurs melden over vier benchmarks verbeteringen van maximaal 20,7 procent ten opzichte van GEPA en 21,2 procent ten opzichte van ACE. Bron: https://arxiv.org/abs/2610.37651

**Geheugencompressie zorgde ervoor dat groepen van meerdere agents beslissende informatie verloren.** Op CrossProfile introduceerde zelfs een perfect relevantiefilter opnieuw afleiders en bleef het in de klassieke configuratie 23 tot 31 punten achter bij selectie die de zeldzaamste informatie eerst kiest. De benchmark bevat 480 taken met geverifieerde antwoorden. Bron: https://arxiv.org/abs/2610.37624

**Mislukkingen bij het snoeien van transformers bleven onzichtbaar in nauwkeurigheid en perplexiteit.** Bij GPT-2’s circuit voor indirecte objecten wiste het snoeien van aandachtshoofden het circuit uit. Het snoeien van 30 procent van de neuronen behield de aandachtshoofden, maar keerde hun bijdrage om, waardoor het model de verkeerde naam verkoos. Bron: https://arxiv.org/abs/2610.37126

**Veiligheidsprobes waren overdraagbaar van basismodellen naar gedistilleerde opvolgers, ondanks rotatie van de representaties.** De AUC van de probes veranderde met tussen -0,011 en +0,027, zelfs wanneer de gemeten onveilige richting 17 tot 35 graden draaide. Het resultaat kan auditors in staat stellen sommige probes bij verwante modellen opnieuw te gebruiken. Bron: https://arxiv.org/abs/2610.35586

## Economie en werk

**GitHub Enterprise omvat nu Copilot-licenties, maar rekent elk verzoek vanaf het eerste af op basis van gebruik.** De inbegrepen toegang bevat geen maandelijkse hoeveelheid AI-tegoed; gebruikers zonder Enterprise-licentie kunnen vergelijkbare toegang kopen voor 10 dollar per maand. Beheerders moeten nu gebruiksbudgetten beheren in plaats van te vertrouwen op een vast tegoed per licentie. Bron: https://github.blog/changelog/2026-10-28-github-enterprise-now-includes-access-to-github-copilot

**GitHub zegt dat Copilot Fusion de scores van toonaangevende programmeeragents benadert voor ongeveer de helft van de kosten per taak.** Fusion verdeelt werk over toegestane modellen. GitHub meldt een score van 60 op de Artificial Analysis Coding Agent Index, op minder dan twee punten van Claude Code met Opus 5.5 Max, met ongeveer de helft van de tokens en 40 procent minder tijd. De vergelijking is een claim van de leverancier. Bron: https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion

**Anthropic voegde rapporten toe die AI-uitgaven van bedrijven vergelijken met de productie van teams.** TechCrunch koppelt de release aan gegevens van Jellyfish over ongeveer 276.000 gebruikers: de uitgaven aan agentische programmeertools zijn sinds januari vertienvoudigd en bereikten ongeveer 2 procent van de ontwikkelkosten, terwijl de meeste grote bedrijven geen grote verbeteringen meldden. De metingen komen van leveranciers. Bron: https://techcrunch.com/2026/10/28/anthropic-just-launched-tools-to-show-companies-what-their-ai-spending-is-buying/

**Het aandeel Alphabet daalde 8 tot 10 procent nadat het bedrijf zei dat AI Mode minder oplevert dan de klassieke zoekfunctie.** De groei van Search vertraagde naar 12 procent, terwijl de kapitaaluitgaven 51,4 miljard dollar bereikten. Google schreef de vertraging toe aan lagere opbrengsten in AI Mode, hoewel het aantal zoekopdrachten het snelst in vijf jaar groeide. Bron: https://www.theregister.com/ai-and-ml/2026/10/29/google-struggling-to-make-ai-mode-searches-pay/5306181

**SK hynix zegt dat geheugentekorten door AI tot en met 2030 zullen aanhouden.** Hardwarefabrikanten verplaatsen een deel van de pc-productie terug naar China om de kosten van onderdelen te verlagen. SK hynix meldde ondertussen een recordwinst en langlopende overeenkomsten voor meer dan de helft van zijn productie in 2027 en 2028. Bronnen: https://www.theregister.com/systems/2026/10/28/sk-hynix-says-memory-shortages-to-persist-until-2030/5305887, https://asia.nikkei.com/business/technology/tech-asia/hp-and-asus-shift-some-pc-making-back-to-china-due-to-ai-driven-cost-hikes

**Noord-Amerikaanse robotbestellingen stegen in het derde kwartaal met 24,8 procent naar 10.989 stuks.** De bestellingen waren 723,5 miljoen dollar waard. Bestellingen voor auto-onderdelen stegen met 90,4 procent, terwijl die voor voeding en consumentengoederen met 23,7 procent daalden; de statistieken betreffen industriële robots in brede zin, niet alleen machines die door AI worden aangestuurd. Bron: https://www.therobotreport.com/north-american-robot-orders-climb-24-8-q3-2026-says-a3/

## Prompttechnieken

**Simon Willison deelde een korte reeks prompts voor de ontwikkeling van browsergames.** Hij vraagt expliciet om three.js, neemt “Denk goed na over hoe het zowel leuk als mooi kan worden” op in de eerste prompt en volgt dan met “Maak het VEEL leuker”. Het bewijs bestaat uit vier projecten en zijn eigen oordeel, niet uit een gecontroleerde vergelijking. Bron: https://simonwillison.net/2026/Oct/28/vibe-game-development/

## Wat mensen bouwen

**PROMETHEVS draait het DeepSeek V4.1-model van 510 GB op een pc met 64 GB RAM en een RTX 3060 met 12 GB.** Het streamt gewichten vanaf twee NVMe-schijven en berekent onzekere tokens opnieuw met gecorrigeerde FP4-gewichten. De maker meldt 5,8 tokens per seconde bij een koude start en 98,3 procent overeenstemming over 960 gecontroleerde tokens, op één machine en zonder vergelijking met een referentie-implementatie. Bron: https://github.com/Magnvs7/Promethevs

**LFM3 WebGPU Workspace draait een kleine programmeeragent volledig in een browser.** De demo geeft LFM3-1.7B een virtueel bestandssysteem, een terminal en bewerkingstools, terwijl prompts en bestanden in IndexedDB blijven. De betrouwbaarheid bij programmeertaken in productie is nog niet getest. Bron: https://huggingface.co/spaces/webml-community/LFM3-1.7B-WebGPU-Pi

**Grim Prompter maakt van dreigingsmodellering een vaardigheid voor programmeeragents.** Zijn 36 architectuurworkflows en 29 methoden sturen Claude Code of Codex aan om vertrouwensgrenzen te inspecteren en JSON-rapporten met gekoppeld bewijs te produceren. Het is promptengineering, geen beveiligingsscanner. Bron: https://github.com/jmanico/grim-prompter

**Soulgent beeldt langdurige sessies van programmeeragents uit als werknemers in een weergegeven kantoor.** Sessies zitten aan bureaus, wachten wanneer ze klaar zijn en sluiten aan in een rij wanneer ze een beslissing nodig hebben. De auteur zegt dat de interface helpt om meer dan 40 sessies verdeeld over vier teams te begeleiden. Bron: https://github.com/Ericcc0321/soulgent

**GEAR laat een meta-agent na terugkerende mislukkingen de uitvoeromgeving van een agent aanpassen.** Het kan modellen, instructies, tools en workflows veranderen, en de aanpassing vervolgens evalueren en in gebruik nemen. De code is open, maar het artikel staat nog aangeduid als “binnenkort beschikbaar”. Prestatieresultaten blijven dus onbeoordeelde claims van de auteurs. Bron: https://rsi-gear.github.io/

## Het lezen waard

**Een klein experiment vond dat hybride modellen hun redenering in recurrente toestand kunnen verbergen.** Eén hybride OLMo-model volgde een lichtschakelaartaak op tweemaal de trainingslengte met een nauwkeurigheid van 0,89, terwijl begrensde en dichte controlemodellen tot ongeveer toevalsniveau daalden. De auteur waarschuwt dat het om één taak met zes toevalsinitialisaties gaat. Bron: https://divagr.com/blog/hybrid-models-can-hide-reasoning-in-their-rnn-state

**Qwenputer compileert een RISC-V-CPU in de recurrente gewichten van Qwen3.5.** De ongetrainde aanpassing speelde ongeveer 230.000 uitvoerposities af zonder afwijking van een referentiemachine en behaalde 97,5 tot 100 procent op tests met exacte rekenkunde. Dit zijn metingen van de maker. Bron: https://divagr.com/blog/qwenputer

**Een script voor digitale vingerafdrukken lijkt een verborgen prompt te gebruiken als verdediging tegen LLM’s.** Versluierde tekenreeksen beschrijven verboden inhoud en onzichtbare Unicode-tags worden gedecodeerd tot een jailbreakprompt. De onderzoeker meldt dat GPT-6 Astra weigerde het te analyseren, terwijl GLM-5.3 dat wel deed. Bron: https://nullpt.rs/fingerprinting-bioweapons

**Databaseonderzoekers stellen dat AI-optimalisatie vaste databasebenchmarks onbruikbaar heeft gemaakt.** Ze tonen systemen die hashes, herhaalde predicaten en ongeordende limieten uitbuiten om snel te lijken terwijl ze verkeerde resultaten teruggeven. Hun voorgestelde oplossing bestaat uit onvoorspelbare zoekopdrachten, updates en systemen die ouder zijn dan de test. Bron: http://databasearchitects.blogspot.com/2026/10/the-benchmarking-crisis.html

**Epoch AI bracht nationale invoer van AI-rekencapaciteit in kaart aan de hand van douanegegevens.** Het schat dat sinds 2022 ongeveer 72 procent van de rekencapaciteit naar de VS en ongeveer 10 procent naar China is verscheept. De openbare methode vermeldt hiaten in douaneclassificaties en vergelijkt de gegevens met schattingen van chipverkopen. Bron: https://epoch.ai/latest/introducing-the-ai-chip-imports-explorer

## Hacker News

**Artificial Analysis v5 wakkerde het debat over besloten benchmarks en ranglijsten van grensverleggende modellen opnieuw aan.** De index gebruikt nu besloten testsets voor 60 procent van zijn score en toont een verschil van 12 punten tussen het leidende model en het beste uitgebrachte model met open gewichten. Reacties betwistten de testomgeving en vroegen of besloten prompts publieke foutcontrole verhinderen; dit zijn zorgen uit de gemeenschap, geen onderzoeksbevindingen. Bron: https://news.ycombinator.com/item?id=50268868

**Stack Overflow daalde volgens een reproduceerbare gegevensquery tot minder dan 1.000 vragen per maand.** Reacties legden de schuld zowel bij AI-assistenten als bij de cultuur van de site en vroegen vervolgens waarop toekomstige systemen zullen trainen als nieuwe technische problemen niet langer in een openbaar archief terechtkomen. Bron: https://news.ycombinator.com/item?id=50282454

## YouTube

**AI Engineer publiceerde Anthropics relaas over het opschalen van codereview naar 30.000 samengevoegde wijzigingen per dag.** Addy Osmani beschrijft hoe Claude de eerste beoordelingsronde uitvoert met verificatiebewijs. Het cijfer over de verwerkingscapaciteit komt van de sprekers en Sonar verkoopt reviewtools. Bron: https://www.youtube.com/watch?v=AnsXWH2_EBU

**AI Engineer publiceerde het relaas van Arize over de herbouw van zijn Alex-agent van 2023 tot 2026.** Fuad Ali zegt dat één agent met planning, vaardigheden en één geheugenbestand van 8.000 tekens beter werkte dan tien specialisten en uitgebreidere opslagsystemen. Het is het verslag van een leverancier over zijn productieomgeving. Bron: https://www.youtube.com/watch?v=YIhvrvHtonk

**Een Tsjechische praktijktest vergeleek zes lokale modellen op een NVIDIA DGX Spark.** Libor Kovář gebruikte kantoortaken, zoals notities omzetten in e-mails en opnamen in workflows, en rapporteerde de vertraging en wat handmatig moest worden gecontroleerd. De oktoberversie voegt een vergelijking met een RTX 5080-laptop en Cerebras toe. Bron: https://www.youtube.com/watch?v=Virmsfh2yHY

## In het kort

**De Britse domeinregistrar 123 Reg schreef een lek van klantgegevens toe aan AI-ondersteunde tools die aan de ARTEX-groep zijn gekoppeld.** Bij de inbraak kwamen contact- en accountmetadata via een API bloot te liggen. De toeschrijving is de bevinding van het incidentonderzoek van de registrar. Bron: https://www.theregister.com/cyber-crime/2026/10/28/123-reg-discloses-ai-cyberattack-on-customer-data-suspects-china-nexus/5305936

**Cisco maakte de broncode van Project Quarry openbaar om schadelijke patronen over volledige agentsessies te detecteren.** Regels kunnen het lezen van een gevoelig bestand koppelen aan een latere verzending naar buiten en omvatten LLM-gesprekken, toolaanroepen en MCP. Bron: https://www.theregister.com/security/2026/10/28/cisco-open-sources-tool-for-detecting-ai-agents-on-hacking-sprees/5305867

**Vijf nieuw gepubliceerde kwetsbaarheden brengen oude beveiligingsproblemen naar de infrastructuur van agents en MCP.** Het gaat onder meer om promptinjectie die omgevingsvariabelen blootlegt, SSRF, toegang tot artefacten van andere applicaties, autorisatiefouten en uitgeschakelde bescherming tegen DNS-rebinding. Bron: https://nvd.nist.gov/vuln/detail/CVE-2026-115415

**Een scan van 7.256.531 openbare Gitee-repositories vond 26.400 unieke, nog werkende inloggegevens.** MongoDB-onderzoeker Ben Zimmermann gebruikte TruffleHog en Kingfisher en documenteerde de methode om repositories op te sommen en de gegevens te verifiëren. Bron: https://www.mongodb.com/company/blog/technical/scanning-7-point-25-million-public-repositories-chinas-largest-git-platform-for-secrets

**Democratische commissievoorzitters in het Amerikaanse Huis van Afgevaardigden vroegen toonaangevende AI-labs om ernstige AI-incidenten binnen 48 uur te melden.** Het verzoek is een brief in het kader van parlementair toezicht, geen wettelijke verplichting; voor incidenten met kritieke infrastructuur zou een termijn van 24 uur gelden. Bron: https://democrats-energycommerce.house.gov/media/press-releases/house-democratic-committee-leaders-request-frontier-ai-companies-report

**New York verbood chatbots voor minderjarigen om zich als mens voor te doen, zelfbeschadiging aan te moedigen of ongepaste gesprekken te voeren.** Gouverneur Kathy Hochul ondertekende de maatregel samen met een bijbehorende wet voor verbonden babyfoons. Bron: https://www.governor.ny.gov/news/governor-hochul-signs-nation-leading-legislation-protect-kids-ai-chatbots-and-ensure-baby

**HHS schrapte transparantievereisten voor modelkaarten uit gecertificeerde zorg-IT.** De definitieve regel laat verplichte bekendmakingen over training, bedoeld gebruik, beperkingen en prestaties bij verschillende patiëntgroepen vervallen. ONC zegt geen bewijs te hebben gevonden dat gebruikers op de informatie vertrouwden of dat die de zorg verbeterde. Bron: https://www.federalregister.gov/documents/2026/10/28/2026-21943/health-data-technology-and-interoperability-onc-deregulatory-actions-to-unleash-prosperity

**Het US Copyright Office gaf aan de verlenging van de uitzondering voor tekst- en datamining te steunen.** Het wees een claim van een uitgever af als ongefundeerd: corpora die onder de uitzondering vallen zouden worden doorgesluisd naar training van generatieve AI. Bron: https://www.federalregister.gov/documents/2026/10/28/2026-21939/exemptions-to-permit-circumvention-of-access-controls-on-copyrighted-works

**Het Chinese CXMT plant naar verluidt HBM3E-productie met een opbrengst van 20 tot 30 procent.** Reuters, aangehaald door The Next Web, vergelijkt dit met ongeveer 70 procent bij SK hynix en zegt dat beperkte productie binnen twee maanden zou kunnen beginnen. Bron: https://thenextweb.com/news/cxmt-hbm3e-ai-memory-low-yields-reuters

**De Maleisische douane nam voor 12 miljoen dollar aan geavanceerde AI-chips in beslag die in 30 servers waren verborgen.** De autoriteiten beschreven Maleisië als doorvoerland voor een smokkelnetwerk en koppelden inbeslagnames ter waarde van 25 miljoen dollar aan het vermoedelijke syndicaat. Bron: https://www.tomshardware.com/tech-industry/policy/malaysia-seizes-usd12-million-worth-of-advanced-ai-chips-hidden-inside-30-servers-customs-says-suspected-smuggling-network-used-the-country-as-a-transit-hub

## Zakelijk in het kort

**Microsoft boekte in het kwartaal 10 miljard dollar omzet uit zijn overeenkomsten met OpenAI, ongeveer 11 procent van zijn totale omzet van 92,3 miljard dollar.** Bron: https://techcrunch.com/2026/10/28/microsoft-recorded-10-billion-in-revenue-from-openai/
