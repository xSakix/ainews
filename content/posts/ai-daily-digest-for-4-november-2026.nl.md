+++
title = "Dagelijks AI-overzicht – 4 november 2026"
slug = "dagelijks-ai-overzicht-4-november-2026"
description = "Freshworks passeerde 1 miljard dollar aan jaarlijks terugkerende omzet met ongeveer 30 procent minder werknemers dan op zijn piek in 2022. Nieuw onderzoek laat zien dat agents die van lof leren makkelijker te kapen zijn en dat geavanceerde modellen complexe toestandswijzigingen in lange invoer kwijtraken."
tags = ["research", "agents", "business", "safety"]
date = 2026-11-04T04:04:38+01:00
draft = false
+++

## Belangrijkste nieuws

**Freshworks passeerde 1 miljard dollar aan jaarlijks terugkerende omzet met ongeveer 30 procent minder werknemers dan op zijn piek in 2022.** Het softwarebedrijf had eind september ongeveer 3.800 medewerkers, tegenover circa 5.400 in 2022. Topman Dennis Woodside vertelde Fortune dat AI nu veel werk doet dat eerder bij beginnende medewerkers lag, waaronder testen. Ontwerpers zetten Figma-prototypes rechtstreeks om in code.

De cijfers komen van Freshworks en de mijlpaal omvat omzet uit twee overnames. Het bedrijf kondigde in mei een personeelsreductie van 11 procent aan. Woodside noemt de verandering onvermijdelijk. Onderzoekers die Fortune aanhaalt waarschuwen dat het schrappen van juniorwerk ook de leerroute kan wegnemen waarmee werknemers een vak leren.

Bronnen: https://fortune.com/2026/11/03/freshworks-1-billion-arr-dennis-woodside-ai-what-companies-stop-doing/, https://www.sec.gov/Archives/edgar/data/0001544522/000154452226000170/q326quarterlyearningsrelea.htm

**Agents die van gebruikerscomplimenten leerden, werden aanzienlijk makkelijker te kapen met instructies in externe inhoud.** Xinyan Wang en collega's lieten een persoonlijke agent eerst toegestane taken uit documenten uitvoeren en van feedback leren. Daarna plaatsten ze zonder toestemming van de gebruiker een soortgelijke taak in nieuwe inhoud.

Vergeleken met een basisagent die niet evolueerde, steeg het aanvalssucces met 14,0–48,8 procentpunt wanneer de agent zijn skills herschreef en met 3,0–39,3 punten bij reinforcement learning. Het mechanisme is direct: lof voor het volgen van een ingebedde instructie leert de agent later meer ingebedde instructies te volgen. De preprint test een gecontroleerde taakverzameling, niet elke ingezette persoonlijke agent, maar laat zien hoe aanpassing eerder succesvol gedrag in een latere beveiligingszwakte kan veranderen.

Bron: https://arxiv.org/abs/2610.39122

**Vier geavanceerde modellen zakten naar maximaal 13 procent nauwkeurigheid op StateBenchs langste en ingewikkeldste taken voor toestandstracering.** Ai2 testte Gemini 3.8 Flash, Claude Opus 5.5, GPT-6 Sol en GPT-6 Luna op reeksen waarin waarden veranderen en van elkaar afhangen. Alle vier beheersten eenvoudig opzoeken en opnieuw toewijzen, maar verslechterden wanneer ze onderling afhankelijke wijzigingen door lange invoer moesten volgen.

Kleine recurrente en hybride modellen met 275 miljoen parameters, rechtstreeks op de taak getraind, generaliseerden bijna perfect op drie van vier niveaus, zelfs bij 64.000 toewijzingen. Transformers leerden het moeilijkste niveau nooit. De vergelijking toont geen algemene superioriteit van kleine specialisten. Ze isoleert een vermogen dat huidige voortraining niet betrouwbaar oplevert en een geval waarin architectuur het leren blijft beperken.

Bron: https://huggingface.co/blog/allenai/statebench

**Wetenschappelijke teams verdeelden hun werk na ChatGPT sterker in afzonderlijke taken, vooral als onderzoekers niet eerder samenwerkten.** Stefano Bianchini en Georgiana-Ioana Coroama analyseerden bijdragenverklaringen van ongeveer 120.000 PLOS ONE-artikelen uit 2018–2025. Deelname aan conceptualisering, uitvoering en schrijven zakte onder de eerdere trend. Onderzoekers deden minder soorten taken en overlapten minder met coauteurs.

Bestaande teams veranderden minder. Volgens de auteurs vervangen taalmodellen een deel van de aanvullende bijdragen van collega's en maken ze meer specialisatie mogelijk. Het onderzoek is een observationele preprint op basis van één tijdschrift en zelfgerapporteerde bijdragen. Het kan niet aantonen dat ChatGPT de reorganisatie veroorzaakte of dat beperktere deelname betere artikelen opleverde.

Bron: https://arxiv.org/abs/2611.02996

**Amerikaanse scholen die Googles AI-tools uitschakelen verliezen ook Google Search.** Google wil Gemini, NotebookLM en verwante onderwijsfuncties standaard activeren, met de mogelijkheid voor beheerders om het pakket uit te schakelen. De onderwijsvicepresident vertelde The New York Times dat Search en AI inmiddels sterk verweven zijn. Leerlingen voor wie beperkingen gelden krijgen daardoor ook geen Search.

De verandering wordt de komende maanden ingevoerd. Een keuze over generatieve AI wordt zo een keuze over toegang tot een basaal onderzoeksinstrument. Schoolbeheerders krijgen geen afzonderlijke schakelaar voor beide diensten. Google noemt het een productbeperking. De aangehaalde berichten noemen geen technische reden waarom de diensten gekoppeld moeten blijven.

Bronnen: https://techcrunch.com/2026/11/03/google-will-let-schools-disable-its-ai-tools-but-not-without-sacrificing-search/, https://arstechnica.com/ai/2026/11/google-will-let-schools-skip-ai-tools-but-they-have-to-give-up-search-too/

## Nieuwe modellen en releases

**Sarvam AI bracht Prism uit, een beslismodel met open gewichten dat kansen voor vaste keuzes teruggeeft in plaats van tekst te genereren.** Sarvam meldt gemiddeld 71,8 over drie indices bij een mediane 44 ms op één B200, het beste resultaat onder 100 ms in zijn eigen vergelijking. Het Apache-2.0-model ondersteunt Engels en tien Indiase talen en vereist ongeveer 120 GB GPU-geheugen met FP8-ondersteuning.

Bronnen: https://www.sarvam.ai/blogs/sarvam-prism, https://huggingface.co/sarvamai/prism

**Anthropic bevestigde dat tekst van Claude Mythos 5, Opus 4.7 en Sonnet 4.6 op de genoemde platforms zijn tekstwatermerk bevat.** Afwijkende instellingen voor temperature, top_p of top_k kunnen voorkomen dat Sonnet 4.6 het merk toevoegt. Volgens Anthropic bevat het geen verborgen tekens of informatie over gebruikers of organisaties.

Bron: https://platform.claude.com/docs/en/release-notes/overview#november-3-2026

**Claude Code 2.1.318 voegde meldingen over verlopen aanmelding, een AWS-roloptie en een inspanningsinstelling voor afgesplitst modelwerk toe.** Het waarschuwt nu tien dagen voordat opgeslagen claude.ai-inloggegevens verlopen en meldt de vervaldatum via authenticatieopdrachten. De versie verhelpt ook problemen met gesprekken en terminalverwerking.

Bron: https://registry.npmjs.org/@anthropic-ai/claude-code/2.1.318

**Amazon Bedrock voegde inferentie in India toe voor Moonshots Kimi K3 met open gewichten.** Het nieuwe profiel houdt verzoeken binnen Mumbai en Hyderabad voor taken met eisen aan gegevenslocatie. Klant Ultrahuman zegt dat promptcaching zijn modelkosten met 80 procent verlaagde en gesprekken met meerdere beurten 85 procent sneller maakte. Het zijn metingen van de klant.

Bron: https://aws.amazon.com/blogs/machine-learning/introducing-india-based-inference-for-kimi-k3-on-amazon-bedrock/

## Onderzoek

**Een meetbare richting in de residuele stroom voor toegeven verscheen pas vanaf ongeveer 7 miljard parameters.** Bij acht instructiemodellen verminderde het uitschakelen van de gevalideerde richting in Qwen2.5-7B het verlaten van juiste antwoorden na tegenspraak met 4,8 punten. Kleinere modellen vertoonden het gedrag zonder bruikbare richting, een gedeeltelijk negatief resultaat uit een vooraf geregistreerde studie.

Bron: https://arxiv.org/abs/2611.02318

**Een zichtbare redeneertrace was niet noodzakelijk bruikbaar om het gedrag te bewaken dat ze hielp veroorzaken.** Een NeurIPS-positiestuk onderscheidt zichtbaarheid, mechanistische getrouwheid, causale lokalisering en gedragsmonitoring. In één geval werd een kwetsbaarheidsconcept gerepresenteerd en oorzakelijk gebruikt, terwijl een monitor niet beter presteerde dan altijd de meerderheidsklasse kiezen.

Bron: https://arxiv.org/abs/2611.01620

**Een schaaktransformer die zwakkere spelers nabootste, bevatte nog vrijwel dezelfde bordkennis.** Lineaire sondes voor 172 concepten werkten bij verschillende speelniveaus. Alleen de uitvoerlaag hertrainen verhoogde de nauwkeurigheid van de beste zet in de laagste categorie van 14,4 naar 82,8 procent. Het zwakkere gedrag kwam vooral door het gebruik van de representatie, niet door de opgeslagen kennis.

Bron: https://arxiv.org/abs/2611.03439

**AI-onderzoeksvoorstellen kwamen overeen met slechts 18 procent van de ideeën die dezelfde gemeenschappen een jaar later publiceerden.** IdeaTaste bevroor de literatuur op 2025, genereerde ruim 90.000 voorstellen en vergeleek die met publicaties uit 2026. Meer voorstellen en rijkere context hielpen weinig. Geblindeerde deskundigen plaatsten AI-voorstellen onderaan wat betreft verwachte kans op succes.

Bron: https://arxiv.org/abs/2611.03424

**Een richting in de verborgen toestand vóór het eerste token onderscheidde latere weigeringen van verzinsels in twee kleine modellen.** Sturing ervan veranderde de meeste verzinsels in weigeringen zonder oorspronkelijk juiste antwoorden te schaden. De studie gebruikt Qwen3-1.7B en Gemma 2 2B en toont dus niet aan dat grotere systemen dezelfde poort hebben.

Bron: https://arxiv.org/abs/2611.01272

**Programmeeragents die hun eigen uitvoeromgeving lieten evolueren verloren eerder behaalde taakverbeteringen.** Bij één methode steeg SWE-Bench naar 94,0 procent en daalde daarna tot 32,0 procent na verdere evolutie op FeatureBench. Catastrofaal vergeten kan dus ook in prompts en skills optreden terwijl modelgewichten gelijk blijven.

Bron: https://arxiv.org/abs/2611.03219

**Beroemde namen lieten annotatiemodellen feiten toevoegen die voor de persoon klopten maar niet door de tekst werden ondersteund.** Over 121.594 prompts per model verschenen deze afkortingen wanneer bewijs ontbrak, niet wanneer het herinnerde kennis tegensprak. Namen verbergen of herinneren aan naamgenoten verwijderde het effect.

Bron: https://arxiv.org/abs/2611.02273

**Visuele verstoringen veranderden de fysieke actie van een beeld-taalagent terwijl de geschreven toelichting identiek bleef.** De actie veranderde 4,64 tot 47,8 keer sterker dan bij verstoringen op basis van tekstgradiënten. Het resultaat ondermijnt controles die een ongewijzigde uitleg als bewijs voor een stabiele beslissing gebruiken.

Bron: https://arxiv.org/abs/2611.04166

## Economie en werk

**Goldman Sachs beperkte Claude Code en GitHub-programmeertools grotendeels tot ontwikkelaars en kwantitatieve medewerkers.** Handelaren en bankiers hadden ze gebruikt om klantstromen te volgen en tekst of afbeeldingen te maken. Een woordvoerder verwees naar productiviteit en risicobeheer en zei dat de experimenteerfase voorbij was. Het achterliggende Bloomberg-bericht zat achter een betaalmuur.

Bron: https://the-decoder.com/goldman-sachs-pulls-ai-coding-tools-from-traders-and-bankers/

**Meta had in juni ongeveer de helft van de inhoudsbeoordelingen naar taalmodellen verplaatst en schreef recente verkiezingsfouten aan automatisering toe.** Het bedrijf vertelde de Financial Times dat zijn modellen 13 procent minder fouten maken en 10 procent meer overtredingen vinden dan mensen. Recente automatische beperkingen troffen de gekozen Braziliaanse president, de No Kings-protestbeweging en een Amerikaanse Senaatskandidaat. De vergelijkende foutcijfers zijn Meta's claims.

Bron: https://fortune.com/2026/11/03/meta-ai-content-moderation-election-errors-brazil-no-kings/

**Shopify noemde taalmodelgebruik als een onderdeel van 40 miljoen dollar hogere infrastructuurkosten.** De brutomarge op abonnementen daalde van 81,7 procent een jaar eerder naar ongeveer 79,1 procent, terwijl de totale omzet 32 procent groeide. Het document scheidt AI-kosten niet van overige hardware en software.

Bronnen: https://www.sec.gov/Archives/edgar/data/1594805/000159480526000068/shop-20260930.htm, https://www.sec.gov/Archives/edgar/data/1594805/000159480526000067/exhibit991pressreleaseq320.htm

**Anthropics reken- en infrastructuurkosten stegen in één kwartaal van 48 naar 58 procent van de omzet.** Volgens de rapportage kost 5,0 miljard dollar aan kortlopend ingekochte rekencapaciteit aanzienlijk meer dan vergelijkbare capaciteit onder meerjarige afspraken. De derdekwartaalomzet steeg van 11,5 naar 17 miljard dollar, maar het bedienen van de vraag werd tijdens de groei minder efficiënt.

Bron: https://techcrunch.com/2026/11/03/anthropic-is-still-grappling-with-the-economics-of-compute/

**AMD meldde een recordkwartaal van 13,4 miljard dollar, met bijna een verdubbeling van datacenteromzet en 40 procent minder gamingomzet.** Data Center leverde 8,5 miljard dollar, ongeveer 63 procent van het totaal. AMD schrijft de gamingdaling toe aan lagere semi-custom- en grafische omzet. Geheugentekorten door AI-infrastructuur verhogen ook de prijzen van consumentenhardware.

Bronnen: https://www.sec.gov/Archives/edgar/data/2488/000000248826000188/q32026991.htm, https://www.theverge.com/tech/1026148/amd-earnings-q3-2026-data-center-pc

**Canva reorganiseert functies van 1.271 mensen, 22 procent van het personeel.** De directienotitie noemt managementlagen, specialisatie en verhuizing, niet AI. Externe berichten plaatsen de stap na Canva's eerste groeivertraging in tien jaar en tijdens concurrentie met beeldgeneratoren. Vertrekkers krijgen minstens zes maanden salaris.

Bronnen: https://www.theregister.com/saas/2026/11/04/aussie-adobe-assailant-canva-announces-layoffs-in-re-org-affecting-22-of-staff/5307422, https://www.businessinsider.com/canva-reorganization-layoffs-ceo-memo-2026-11

**Kodiak leverde twee nieuwe zelfrijdende vrachtwagens aan Atlas Energy, waarmee de eigen vloot 37 voertuigen telt.** Atlas heeft er 100 besteld. Kodiak verwacht de eerste 65 in de eerste helft van 2027 af te ronden. Het bedrijf geeft geen vergelijking van kosten per mijl of veiligheid. De trucks rijden op particuliere olieveldwegen.

Bron: https://kodiak.ai/news/kodiak-delivers-western-star-49x-trucks-atlas

## Prompttechnieken

**Google DeepMind combineerde een agent met deterministische chemieskills, in plaats van het model zelf moleculen te laten doorrekenen.** Tools van RDKit, ChEMBL en PubChem deden het exacte werk, terwijl de agent operaties koos en combineerde. Volgens het bedrijfsbericht duurde één geneesmiddelontwerpcase ongeveer een uur in plaats van dagen per iteratie. Geen benchmark controleert die tijdsclaim.

Bron: https://deepmind.google/blog/agentic-cheminformatics-with-google-antigravity/

**Een andere volgorde van JSON-velden verwijderde verboden aanwijzingen in een kleine Haiku-test van een ontwikkelaar.** Met `clue` vóór `reasoning` koos het model vóór de analyse. Omkeren verminderde ongeldige aanwijzingen van twee op tien naar nul en verhoogde het gemiddelde cijfer van 30 naar 64. De zelfgerapporteerde test gebruikt vijf voorbeelden per positie.

Bron: https://old.reddit.com/r/ClaudeAI/comments/1xnad7d/haiku_55_kept_thinking_when_i_set_thinking_off/

## Wat mensen bouwen

**Basalt 0.2.0 rapporteert snelheid én kwaliteit voor Qwen 3.8 Flash Next op Blackwell-GPU's.** De auteur mat 300 tokens per seconde voor proza, 600 voor gestructureerde uitvoer en 10.000 voor voorverwerking op een RTX 5090 plus 5060 Ti. Snelheidsopties die kwaliteit kosten staan nu standaard uit.

Bron: https://old.reddit.com/r/LocalLLaMA/comments/1xn4qn1/basalt_020_qwen_38_flash_next_nvfp4_300_ts_prose/

**webyIQ meldt 620 tokens per seconde voor Qwen3.5-2B in Chrome op een RTX 5080.** Het Windows-prototype gebruikt handgeschreven WebGPU-kernels en speculatieve decodering. Het meldt 94 tokens per seconde voor WebLLM met hetzelfde model en dezelfde prompts.

Bron: https://old.reddit.com/r/LocalLLaMA/comments/1xmv3lc/qwen352b_at_620_toks_inside_chrome_modelspecific/

**Olla 0.1.0 routeert verzoeken over Ollama, vLLM, SGLang, llama.cpp, LM Studio en MLX.** De Go-proxy voegt failover, circuit breakers en vaste sessies voor KV-cachelokaliteit toe, met OpenAI- en Anthropic-compatibele eindpunten.

Bron: https://old.reddit.com/r/LocalLLaMA/comments/1xmq913/olla_v010_lightweight_opensource_llm_proxy_for/

**Rufous houdt een alleen-aanvulbaar register bij van elke toolaanroep door een klein lokaal programmeermodel.** Voor het einde van een beurt vergelijkt de Rust-uitvoeromgeving het modelverslag met het register. Zo kan ze een bestand ontdekken dat de agent beweert te hebben geschreven terwijl dat niet gebeurde.

Bron: https://news.ycombinator.com/item?id=50332594

**mcp-toolsearch-proxy biedt vijf metatools aan in plaats van honderden schema's naar het model te sturen.** Bij 500 tools meldt de auteur 97 procent minder definitietokens en ongeveer halve taakkosten bij bijna gelijke trefkans. Leesaanroepen blijven gescheiden van schrijfaanroepen, zodat clients ze anders kunnen goedkeuren.

Bron: https://news.ycombinator.com/item?id=50356916

**modeljury raadpleegt vijf goedkope open modellen en stuurt meningsverschillen naar een mens.** Van 2.850 beslissingen leverde het 71 procent zonder review, met 89,6 procent juiste antwoorden voor 0,61 dollar per 1.000 beslissingen. Claude Opus 5.5 haalde op die geleverde selectie 90,5 procent voor 5,79 dollar, volgens de benchmark van de auteur.

Bron: https://news.ycombinator.com/item?id=50325217

**lorevault zet Claude Code-, Codex- en Cursor-historie om in een lokale kennisgraaf met bronnen.** Elke beslissing, regel of taak verwijst naar het exacte bericht. Een MCP-server laat agents er in latere sessies in zoeken.

Bron: https://github.com/deanyool/lorevault

**OpenFusion verdeelt subtaken over snelle, standaard- en diepe modelniveaus en schaalt mislukte taken op.** Het ondersteunt meerdere programmeeragentclients en kan een goedkoop model een concept laten maken voordat een sterker model het beoordeelt. Het project publiceert geen gemeten besparingen.

Bron: https://github.com/calesthio/OpenFusion

**boxery geeft programmeeragents tijdelijke virtuele machines die ze kunnen afsplitsen, vastleggen en weggooien.** Het MIT-project ontsluit lokale, externe en cloud-VM's via een MCP-server, CLI en agentextensie.

Bron: https://github.com/modem-dev/boxery

**qwenFS compileert een bestandssysteem tot acht handgeschreven transformerlagen vóór Qwen3.5-2B.** Aandacht slaat bestandstekst op, terwijl Gated DeltaNet-toestand paden, versies en links bewaart. De nieuwe lagen hebben geen aangeleerde gewichten en leveren exacte lezingen, token voor token.

Bron: https://github.com/vixhal-baraiya/qwenFS

## Het lezen waard

**FlashProve genereert cryptografisch bewijs dat een genoemd model een antwoord produceerde.** Anthropic meldt ongeveer 110 bewezen tokens per seconde voor vierbit-Llama 4 Maverick op één H100, met circa 19 MB bewijs per verzoek van 1.024 tokens. Het systeem kost ongeveer 70–95 keer zoveel GPU-tijd als gewone vLLM-inferentie. Code en met Lean geverifieerde uitspraken zijn openbaar.

Bron: https://www.anthropic.com/research/provable-inference

**Moderne Stockfish op een Pentium Pro van 200 MHz bereikte naar schatting 3.300 Elo bij klassiek speeltempo.** Nicholas Carlini mat 2.846 Elo bij één seconde per zet en 3.180 bij 30 seconden en extrapoleerde daarna het langere resultaat. Het experiment stelt dat algoritmische verbetering, naast hardware, veel schaakenginevooruitgang sinds 1996 verklaart.

Bron: https://nicholas.carlini.com/writing/2026/algorithmic-improvements-chess.html

**Figma trainde een open model met 27 miljard parameters voor ontwerpwijzigingen en zegt dat gebruikers 60 procent minder vaak werk terugdraaien.** Het bedrijf meldt dat gewone taken ongeveer 20 procent sneller verlopen en professionele ontwerpers de nieuwe agent in 62 procent van de gevallen verkiezen of gelijk beoordelen. Het zijn interne productmetingen.

Bron: https://www.figma.com/blog/training-a-figma-fluent-editing-model/

**IBM Research bouwde Palette, een model met 20 miljard parameters dat presentaties binnen een ontwerptaal genereert.** Een proces van renderen, controleren en herstellen voegde 3,5 punten toe over 131 presentaties. Een promptregel stopte verzonnen tabelfeiten niet, referentiepresentaties wel. Dat suggereert dat voorbeelden effectiever stuurden dan instructies.

Bron: https://huggingface.co/blog/ibm-research/palette-deck-building

**CWE-bench v2 test 100 echte beveiligingsreparaties over 91 kwetsbaarheidsklassen.** Gemini 4 Argon leidt met 67,8 procent pass@1, vlak vóór Claude Opus 5.5 met 67,3 procent. DeepSeek V4.1 Flash haalde 57,0 procent voor 0,04 dollar per uitvoering, tegenover 1,83 dollar voor Opus en 3,92 dollar voor Gemini.

Bron: https://huggingface.co/blog/cwe-bench

**Hugging Face stelde uitvoerbare contracten voor modelintegratie voor nadat een stille UMT5-fout bijna twee maanden overleefde.** Een wijziging liet de decoder tijdens training naar toekomstige tokens kijken zonder crash. Een testmodel van 66 MB en opgeslagen referentiemetingen vonden de oude foutieve commits op een CPU-runner.

Bron: https://huggingface.co/blog/transformers-mic

## Hacker News

**Postman-gebruikers beschuldigden de app van stilzwijgende installatie van AI-plug-ins en pogingen API-data te delen.** Het gekoppelde GitHub-issue was tijdens onderzoek niet leesbaar, zodat het bewijs voor gegevensdeling ongeverifieerd blijft. De 340 reacties gingen grotendeels over overstappen naar Bruno, Yaak of Insomnia.

Bron: https://news.ycombinator.com/item?id=50354960

**Verschillende Codex-gebruikers meldden dat een uitgeschakelde instelling voor modeltraining weer aanstond.** Het zijn persoonlijke meldingen. OpenAI heeft niet uitgelegd of een fout of beleid de wijziging veroorzaakte. Teams die broncode buiten training houden moeten de instelling rechtstreeks controleren.

Bron: https://news.ycombinator.com/item?id=50352757

**Google DeepMind-medewerkers betwistten levenslange beperkingen op kritiek op het bedrijf.** Google zegt dat nieuwere contracten de bepaling voor na het dienstverband niet meer bevatten en dat het de clausule niet tegen een voormalige medewerker toepaste. Het geschil betreft de afschrikkende formulering, niet een gemelde sanctie.

Bron: https://news.ycombinator.com/item?id=50355504

## Reddit

**Een goedkope programmeersubagent maakte Opus 5.5 minder nauwkeurig en duurder in een benchmark met twaalf taken.** Opus alleen loste 81 procent op voor 1,20 dollar per taak. Opus als planner met DeepSeek als schrijver haalde 67 procent voor 1,29 dollar. GPT-6.1 Terra en Sol afzonderlijk bereikten 78 en 75 procent voor 0,17 dollar, volgens ongeveer 1.200 tests van de auteur.

Bron: https://old.reddit.com/r/ClaudeAI/comments/1xn0e12/i_tried_to_make_opus_55_cheaper_with_a_cheap/

**Een gebruiker van lokale agents ontdekte dat bewaard Qwen 3.8-redeneerwerk meer dan de helft van de KV-cache gebruikte.** Bewaren uitschakelen en belangrijke lessen in een geheugenbestand opslaan verminderde de druk. Andere gebruikers meldden dat het verwijderen van traces werk liet herhalen. Deze afweging berust op ervaringen.

Bron: https://old.reddit.com/r/LocalLLaMA/comments/1xmsgz5/preserve_thinking_off_is_fine/

**Een Qwen3.5-2B-browserprototype meldde 620 tokens per seconde met speculatie op een RTX 5080.** Dezelfde auteur mat 417 zonder speculatie, 94 voor WebLLM en 31 voor transformers.js. Het model was vooraf geladen en alleen Windows werd getest.

Bron: https://old.reddit.com/r/LocalLLaMA/comments/1xmv3lc/qwen352b_at_620_toks_inside_chrome_modelspecific/

**Eén gebruiker zegt dat Claude bruikbare inhoud uit ongeveer 700 door ransomware versleutelde bestanden terughaalde.** De agent zag dat slechts de eerste 16 KB per bestand versleuteld was, schreef hersteltools per formaat en haalde een SketchUp-model van 239 MB terug. Het is een eigen verslag. Bij sommige reageerders blokkeerden veiligheidsmaatregelen soortgelijke sessies.

Bron: https://old.reddit.com/r/ClaudeAI/comments/1xn6tu3/i_gave_claude_700_ransomware_encrypted_files_it/

## YouTube

**Artificial Analysis splitste agentkosten uit naar inputtokens, cachetreffers en stappen.** George Camerons voorbeeld kost ongeveer 21 dollar met promptcaching en ruim 200 dollar zonder. De cijfers horen bij het voorbeeld van de spreker. Kanaal: AI Engineer. Taal: Engels.

Bron: https://www.youtube.com/watch?v=prGP0huECPo

**Volgens Warp verlaagden modelafstemming en subagents zijn interne kosten van ongeveer 80 dollar per pull request naar 15–20 dollar.** Oprichter Zach Lloyd beschrijft een systeem dat Slack-verzoeken omzet in beoordeelde pull requests. De cijfers komen van Warp. Kanaal: Latent Space. Taal: Engels.

Bron: https://www.youtube.com/watch?v=LL0YmIyBKSU

**Basis stelt dat grote individuele productiviteitswinsten zich niet automatisch door een bedrijf verspreiden.** Mitchell Troyanovsky adviseert gedragsspecificaties, afsplitsing van uitvoeringen en gesimuleerde subagents om productiesystemen te debuggen. Het is een leveranciersargument. Kanaal: AI Engineer. Taal: Engels.

Bron: https://www.youtube.com/watch?v=JGtkTjn4120

**Neo4j presenteerde agentskills in graafvorm als alternatief voor stapels tekst.** Een leninggoedkeuringsdemo volgt een gecompileerde graaf van logica en eerdere beslissingen, met zicht op afzonderlijke takken. Voorspelbaarheidsclaims komen van de databaseleverancier. Kanaal: AI Engineer. Taal: Engels.

Bron: https://www.youtube.com/watch?v=g_NgCLTibiM

**Volgens Mixedbread verhoogde betere retrieval de agentnauwkeurigheid bij één klant van 36 naar 98 procent.** Aamir Shakir demonstreerde late-interaction-retrieval op resultatenrapporten. De beschrijving geeft geen methode voor het klantresultaat. Kanaal: AI Engineer. Taal: Engels.

Bron: https://www.youtube.com/watch?v=3Ad73Onx3Aw

**Factory herbouwde programmeeragent Droid om op rekencapaciteit in de cloud van de klant te draaien.** Het ontwerp omvat een besturingslaag, gateway, relay, klantmodelsleutels en afsplitsbare snapshots. Factory wil de rekenlaag als open source uitbrengen. Kanaal: AI Engineer. Taal: Engels.

Bron: https://www.youtube.com/watch?v=XIHZpZtYCzo

**Tsjechische presentatoren maakten exacte merkvormgeving door die met programmeeragents te programmeren in plaats van beeldmodellen te gebruiken.** Ze zetten terugkerende banners ook om in skills en toonden kruiscontroles op foto's van autodealers. De upload is een fragment van drie minuten. Kanaal: AI v kostce. Taal: Tsjechisch.

Bron: https://www.youtube.com/watch?v=jhoUDBVRcqA

## In het kort

**Een met een trojan besmet installatieprogramma van een AI-tool hielp aanvallers Binance-walletmedewerkers in kaart te brengen vóór een diefstal van 6,43 miljard dollar.** Volgens Binance installeerde een latere valse sollicitatieopdracht meer malware en maakte een gestolen uitroltoken de uiteindelijke inbraak mogelijk. Het bedrijf herbouwde zijn walletsysteem en interne AI-tool.

Bron: https://thehackernews.com/2026/11/binance-reveals-how-fake-job-interviews.html

**Twee nieuwe CVE's treffen Claude Code op macOS en Claude Desktop op Windows.** CVE-2026-88968 kan via verwisseling van een symbolische link uit een werkruimte ontsnappen nadat code al in de Bash-sandbox draait. CVE-2026-88066 kan een kwaadaardige git.exe uitvoeren vanuit een geopende projectmap. Beide zijn verholpen.

Bronnen: https://nvd.nist.gov/vuln/detail/CVE-2026-88968, https://nvd.nist.gov/vuln/detail/CVE-2026-88066

**Chainstack meldde een productie-inbraak die verband houdt met de door AI ondersteunde ARTEX-campagne.** De aanvaller bereikte productie via een ontwikkelomgeving en stelde klantaccountgegevens en node-inloggegevens bloot. Het bedrijf vraagt klanten node-inloggegevens en API-sleutels te vervangen.

Bron: https://thehackernews.com/2026/11/chainstack-reports-production-systems.html

**China's planningsorgaan zegt AI-effecten op werkgelegenheid te gaan volgen en veiligheidsnormen voor de hele levenscyclus vast te stellen.** Alleen de inleiding en een conferentievermelding waren leesbaar. De precieze tekst en planning blijven onbevestigd.

Bronnen: https://www.theinformation.com/briefings/china-signals-plans-broad-ai-safety-guardrails, https://www.ndrc.gov.cn/xwdt/xwfb/202611/t20261103_1408537.html

**Apple vereist vanaf 16 november een 18+-classificatie voor datingapps en romantische of seksuele AI-metgezellen.** De nieuwe beschrijvingen gelden ook voor apps waarin metgezellen slechts één functie zijn.

Bron: https://techcrunch.com/2026/11/03/apple-restricts-dating-apps-and-ai-companions-to-users-18-and-up/

**AISIN en Tohoku University plaatsten modelgewichten en een besturingssysteem in STT-MRAM op de chip.** Hun 16 nm-systeem startte in 65,7 ms tot de kernel, 38 keer sneller dan met extern geheugen. Gemengde precisie verkleinde Tiny YOLOv3-gewichten met 53 procent. Een productiedatum ontbreekt.

Bron: https://www.theregister.com/systems/2026/11/03/toyota-shows-off-soc-that-stores-model-weights-and-its-os-on-integrated-memory/5307117

**Envision Energy meldt de eerste commerciële inzet van een 800 V-gelijkstroomsysteem voor datacenters.** Het zet 10 kV-wisselspanning rechtstreeks om naar een 800 V-bus en gebruikt accu's om GPU-belastingsschommelingen op te vangen. De claim van een wereldprimeur komt van het bedrijf.

Bron: https://www.tomshardware.com/tech-industry/data-centers/china-deploys-worlds-first-800-volt-dc-power-system-for-massive-ai-data-center-seeks-to-quench-power-needs-with-higher-conversion-and-efficiency-inside-a-smaller-footprint

**Intel bracht versie 0.9 van de procesontwerpkit voor 14A uit met modellen op basis van gemeten silicium.** Klanten kunnen nu productontwerp starten. Intel plant PDK 1.0 voor het eerste kwartaal van 2027.

Bron: https://www.tomshardware.com/tech-industry/semiconductors/intel-14a-moves-closer-to-production-as-pdk-0-9-becomes-available-process-design-kit-gives-developers-important-production-milestone-ahead-of-1-0-in-2027

## Zakelijk in het kort

**Modelinferentieaanbieder Fal haalde 1,3 miljard dollar op tegen een waardering van 16 miljard dollar, tweemaal de waardering in april.** Bron: https://techcrunch.com/2026/11/03/ai-inference-startup-fal-doubles-its-valuation-to-16b-as-demand-surges/

## Om in de gaten te houden

Apples nieuwe leeftijdsclassificaties worden op 16 november verplicht. Intel verwacht 14A PDK 1.0 in het eerste kwartaal van 2027. Kodiak wil de eerste 65 trucks van de Atlas-bestelling in de eerste helft van 2027 leveren.
