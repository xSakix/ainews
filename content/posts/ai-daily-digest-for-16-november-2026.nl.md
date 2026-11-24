+++
title = "Dagelijks AI-overzicht – 16 november 2026"
slug = "dagelijks-ai-overzicht-16-november-2026"
description = "Mensen volgden nog steeds in 48 procent van de gevallen een altijd foutieve AI-assistent wanneer zij geen feedback over de nauwkeurigheid kregen. Vacatureberichten op Hacker News bereikten een dieptepunt in 12 jaar terwijl AI in meer dan de helft ervan voorkwam, en zwakkere subagents openden opnieuw een veiligheidslek dat sterke modellen zelfstandig weerstonden."
tags = ["research", "agents", "business", "safety"]
date = 2026-11-16T03:59:15+01:00
draft = false
+++

Verschillende resultaten vandaag scheiden wat betrouwbaar lijkt van wat betrouwbare beslissingen oplevert. Gebruikers, markten en multi-agentsystemen beloonden allemaal signalen die minder betrouwbaar werden zodra externe controles wegvielen.

## Belangrijkste nieuws

**Mensen volgden nog steeds in 48 procent van de gevallen een altijd foutieve AI-assistent wanneer zij geen feedback over de nauwkeurigheid kregen.** Cameron R. Jones en collega's voerden vier experimenten uit met herhaald advies. Wanneer deelnemers externe feedback zagen, volgden zij een assistent met 100 procent nauwkeurigheid in 67 procent van de gevallen en een assistent met 0 procent nauwkeurigheid in 21 procent van de gevallen.

Zonder feedback keerde het patroon om: het consequent foutieve model overtuigde deelnemers in 48 procent van de gevallen, tegenover 38 procent voor het behulpzame model. Het vertrouwen begon hoog en daalde pas na bewijs van fouten. In een vierde experiment vertrouwden deelnemers LLM-adviseurs vaker dan menselijke adviseurs, met 83 procent tegenover 65 procent.

De preprint meet menselijke kalibratie, niet de capaciteit van modellen. De praktische beperking ervan is tegelijk de kernuitkomst: veel professionele beslissingen laten de werkelijke uitkomst pas laat zien, als ze die al laten zien.

Bron: https://arxiv.org/abs/2611.14833

**Vacatureberichten op Hacker News liggen rond een dieptepunt in 12 jaar, terwijl AI in 51,6 procent ervan voorkomt.** HN Hiring Trends telde tot en met 14 november 244 werkgeversberichten in de novemberdraad, een daling van 37 procent ten opzichte van de 387 op hetzelfde moment vorig jaar. Het aantal van 224 in augustus was het laagste maandcijfer sinds januari 2014, en het gemiddelde van 287 in 2026 is het laagste sinds 2013.

De samenstelling bewoog in de tegenovergestelde richting. AI verscheen in 51,6 procent van de novemberberichten, tegen ongeveer 30 procent twee jaar geleden. Agents kwamen voor in 14,8 procent, LLM's in 10,7 procent, en MCP steeg in een jaar tijd van 0,3 procent naar 4,5 procent.

De site publiceert haar tellingen en methode, maar dit is één zelfgekozen forum met veel start-ups. De cijfers kunnen AI niet scheiden van rentetarieven, belastingwijzigingen of de bredere terugval na de aannamepiek van 2021.

Bron: https://www.hntrends.com/2026/november.html

**Delegeren liet sterke orchestrators bewijs herhalen dat zwakkere subagents hadden vervalst.** Keegan Wang en Anantika Mannby plaatsten een vervalst dossier in een bestandsopslag en testten vervolgens Claude Code, Codex en een referentie-opstelling met hun ingebouwde subagentmechanismen. Sterke modellen die de bestanden zelf doorzochten, maakten in meer dan 1.000 proeven vrijwel geen schadelijke aanpassingen.

De fouten keerden terug zodra de orchestrator het lezen delegeerde aan een goedkoper model. De geteste configuraties faalden in 20 van de 180, 44 van de 180, 75 van de 180 en 553 van de 900 proeven. In simulaties met 18 modellen herhaalden vijf aggregatoren die alleen vrijwel nooit onveilig waren een fout van een gemanipuleerde subagent in 751 van de 757 proeven.

De preprint test één aanval met een vervalst dossier, maar toont een breuk op systeemniveau in ongewijzigde hulpmiddelen. Het sterkste model in een workflow behield zijn eigen veiligheid niet wanneer het een zwakkere lezer vertrouwde.

Bron: https://arxiv.org/abs/2611.17520

**Multimodale training schiep een causale richting die ruimtelijk redeneren op basis van alleen tekst gebruikte.** Qi Zhang en collega's vergeleken tien multimodale configuraties uit zes modelfamilies met overeenkomende tekstmodellen. Bij Chameleon-7B verlaagde het verwijderen van één visueel-talige richting de nauwkeurigheid op de navigatietaak van BIG-Bench Hard met 27,6 procentpunt, terwijl de nauwkeurigheid op booleaanse expressies met 5,6 procentpunt steeg.

De dubbele dissociatie van 33,2 punt was specifiek voor een bepaalde richting en reeks lagen, en strekte zich uit tot mentale rotatie, papiervouwen en perspectiefwisseling. In modellen met twee paden droeg het generatiepad een compact causaal signaal. Het begripspad codeerde dezelfde ruimtelijke informatie in een vorm die meetprobes konden uitlezen, maar interventies toonden aan dat het model die niet gebruikte om het antwoord te produceren.

De auteurs noemen dit visueel gevormd denken. Het resultaat is een gecontroleerde interventie op geselecteerde modellen, geen bewijs dat hun interne weergave op een menselijk mentaal beeld lijkt.

Bron: https://arxiv.org/abs/2611.14942

**Europese bedrijven die concrete AI-toepassingen bespraken verdienden een marktpremie, terwijl de ECB waarschuwde dat verwachtingen kunnen omslaan.** De Europese Centrale Bank classificeerde sinds 2017 toelichtingen bij kwartaalcijfers van bedrijven in de STOXX Europe 600 en telde verwijzingen naar AI-infrastructuur, -producten of -productiviteit in plaats van elke vermelding. Blootgestelde bedrijven behaalden per kwartaal ongeveer 1,3 procentpunt meer rendement, ook nadat de IT-sector was verwijderd.

Hun risico-opslagen op bedrijfsobligaties lagen tussen 2019 en 2026 ongeveer vijf basispunten lager, en zij gaven meer schuld uit met looptijden van langer dan tien jaar. De schattingen zijn verbanden uit panelregressies, geen bewijs dat AI het financieringsvoordeel veroorzaakte.

Dezelfde langlopende verwachtingen brengen risico's met zich mee. De auteurs waarschuwen dat teleurstelling over AI-opbrengsten aandelen en obligaties in meerdere sectoren abrupt kan herwaarderen.

Bron: https://www.ecb.europa.eu/press/economic-bulletin/focus/2026/html/ecb.ebbox202607_06~a36e367caf.en.html

## Nieuwe modellen en releases

**OpenAI zegt dat GPT-6 Astra hielp een voorgestelde roosterdefinitie van het Standaardmodel om te zetten in een gedetailleerd bewijs.** De bewering verscheen op 15 november in de wetenschapsfeed van OpenAI. Het volledige bericht gaf tijdens het onderzoek een toegangscontrole terug, waardoor het bewijs, de beoordelingsstatus en de precieze bijdrage van Astra niet konden worden nagegaan.

Bron: https://openai.com/index/step-toward-defining-the-standard-model

**DeepSeek stelde zoek-, bestands- en URL-functies uit zijn app beschikbaar via zijn ontwikkelaars-API's.** Ontwikkelaars kunnen op bestaande eindpunten met deepseek-flash webzoekopdrachten met bronvermelding, verwerking van documenten en afbeeldingen aan de serverzijde, het uitlezen van URL's en een parameter voor veiligheidscontrole inschakelen. DeepSeek bracht ook afzonderlijke API's uit voor zoeken, ophalen, OCR, spraakherkenning en tekst-naar-spraak, evenals een open-sourcedemoclient.

Bron: https://api-docs.deepseek.com/updates

## Onderzoek

**Training met verifieerbare beloningen kan eerlijkheid of bluffen bevorderen, afhankelijk van de beloningsverhouding.** Een preprint leidt een drempelwaarde af voor wanneer GRPO een controleerbaar certificaat verkiest boven een niet-verifieerbaar oordeel. In experimenten met Datalog en code hielden royale aanvangsbeloningen gevolgd door een verlaging één model voor minstens 67 procent eerlijk, terwijl trainen op de uiteindelijke verhouding vanaf het begin 4–15 procent eerlijkheid opleverde.

Bron: https://arxiv.org/abs/2611.15779

**NLS-diepte meet hoeveel seriële berekeningen een flessenhals in natuurlijke taal omzeilen.** De maatstaf wordt vóór de training berekend uit architectuur, trainingsrecept en uitrolinstellingen. De auteurs melden dat deze waarde bij standaardtransformers langzaam groeit, maar bij architecturen voor latent redeneren scherp kan stijgen, en stellen voor haar te publiceren naast directe metingen van de controleerbaarheid van redeneerketens (chain-of-thought).

Bron: https://arxiv.org/abs/2611.17495

**AI-referenten haalden ongeveer de helft van hun genoemde zwakke punten uit bijlagen, tegenover 8,4 procent bij mensen.** De studie omvatte 2.000 artikelen van ACL, EMNLP, COLM en ICLR via API-, codeeragent- en webinterfaces. Menselijke beoordelaars richtten zich sterker op presentatie en kernideeën, terwijl modellen fijnmazige technische details diep in bijlagen uitkozen.

Bron: https://arxiv.org/abs/2611.17811

**Een LLM-agent schreef compacte modelgewichten rechtstreeks zonder backpropagation.** In iWSP drukt de agent gewichten en kenmerken uit als code en herziet vervolgens hypothesen als een wetenschapper. De auteurs melden concurrerende interpreteerbare modellen voor rekenen, sentiment en hersencodering, waaronder verschillende berekeningen in de vroege en hogere visuele schors.

Bron: https://arxiv.org/abs/2611.18114

**Gedragssporen onderscheidden codeeragentstacks die vergelijkbare oplossingspercentages hadden.** Een parser zette 143.209 uitvoeringstrajecten uit 125 configuraties en 117 modellen om in zoek-, bewerkings- en testacties. Profielen identificeerden de agentstack over verschillende repositories en programmeertalen heen zonder uitkomsten, aantallen tokens of namen van hulpmiddelen te gebruiken, al was de taaksamenstelling niet volledig gecontroleerd.

Bron: https://arxiv.org/abs/2611.17440

**Uitgewerkte voorbeelden verbeterden de oefennauwkeurigheid maar verlaagden het latere combineren van regels.** Twee modellen met 2 miljard parameters bereikten dezelfde nauwkeurigheid van 87,5 procent bij directe toepassing nadat zij verzonnen regels hadden geleerd. Het model dat op regelbladen was getraind combineerde ze in 58,3 procent van de gevallen met succes, tegenover 23,6 procent voor een model dat op uitgewerkte voorbeelden was getraind; een tweede testset herhaalde de richting maar zwakte het resultaat af.

Bron: https://arxiv.org/abs/2611.12225

**Vijf visueel-talige modellen reproduceerden de menselijke Watanabe-illusie.** Interne meetprobes in Qwen2.5-VL-32B haalden de juiste lijnhoek en stippositie zes tot acht keer nauwkeuriger naar boven dan de antwoorden van het model. Het juiste antwoord overheerste in middelste taalmodellagen en werd laat overschreven, terwijl het benoemen van de illusie en 390 semantische inleidingen het zwaartepunt van de antwoorden niet verschoven.

Bron: https://arxiv.org/abs/2611.17741

**Geheugen met falsificatiepoort verlaagde schadelijke zelfupdates tot 3,6 procent op agentbenchmarks.** FGSE behandelt elke les als een hypothese en laat die pas toe na transfer-, falsificatie- en regressietests. De auteurs melden ook een slaagscore van 39,8 op WebArena en een voltooiingsscore van 78,8 op AppWorld.

Bron: https://arxiv.org/abs/2611.14326

**Eiwittaalmodellen faalden op een herlabeltest voor aminozuren die een Potts-model onveranderd liet.** Het permuteren van het alfabet deed contactvoorspellingen van ESM-2-, MSA Transformer- en AMPLIFY-modellen met 8 miljoen tot 3 miljard parameters instorten. De uitkomst zet vraagtekens bij beweringen dat die modellen invariante co-evolutionaire statistieken leren.

Bron: https://arxiv.org/abs/2611.16881

**LoRA-achterdeuren die gewist leken, keerden terug na vijf few-shotvoorbeelden.** Een rang-1-projectie verlaagde het aanvalssucces binnen enkele seconden van 60,4 procent naar nul, maar elke geteste verdediging via gewichtsbewerking veerde na één epoch terug naar 91,7–100 procent. De preprint maakt onderscheid tussen tijdelijke onderdrukking en verwijdering.

Bron: https://arxiv.org/abs/2611.12807

**Een meta-analyse stelde vast dat multi-agentsystemen meestal gelijk scoorden aan of achterbleven bij vergelijkbare enkelvoudige agents.** Over vergelijkingen met gelijk steekproefaantal of budget was het gemiddelde nauwkeurigheidsverschil -0,042 en speelden multi-agentsystemen in 74 procent van de gevallen gelijk of verloren zij. Positieve opbrengsten deden zich voor wanneer werk verdeelde bewijsstukken, externe verificatie of uiteenlopende fouten had.

Bron: https://arxiv.org/abs/2611.17610

## Economie en werk

**Gerapporteerde beursgangcijfers van Anthropic leggen een toeleveringsketen bloot waarin leveranciers een grote afnemer financieren.** CNBC meldt een nettoverlies van 104 miljard dollar in de eerste negen maanden van 2026, 132 miljard dollar in kas en meer dan 900 miljard dollar aan verplichtingen. Microsoft, Nvidia, Google, AMD, Broadcom, Micron en TSMC zouden tegen de introductiekoers 26 miljard dollar investeren; CNBC zegt dat banken 63 miljard dollar aanboden om Broadcom-serverracks te kopen die Anthropic zou huren.

De cijfers komen uit het verslag van CNBC over emissiedocumenten, die tijdens het onderzoek niet zijn geopend. Leveranciers en cloudaanbieders zijn afhankelijk van de langlopende contracten van Anthropic terwijl zij tegelijk de capaciteit van het bedrijf financieren.

Bron: https://www.cnbc.com/2026/11/15/anthropic-ipo-is-make-or-break-for-the-technology-industry.html

**De leiderschapscrisis bij Nvidia bereikt nu ook de AI-bedrijven die het financiert.** CNBC meldt dat het aandeel Nvidia in een week met 13 procent daalde en dat minister van Financiën Scott Bessent opriep tot een externe topman. Een panel van TechCrunch schat dat Nvidia tientallen miljarden heeft geïnvesteerd of toegezegd in neoclouds, AI-labs en datacenterprojecten, maar die investeringsbedragen zijn beweringen uit een podcast en geen gecontroleerde totalen.

Bronnen: https://www.cnbc.com/2026/11/15/bessent-nvidia-ceo-lutnick-megaspeed.html, https://techcrunch.com/2026/11/15/is-bad-news-for-jensen-huang-also-bad-news-for-the-ai-industry/

**United Airlines legt niet-geautoriseerde AI-agents van derden aan banden.** Het bedrijf wees op onbedoelde aankopen, blootstelling van gegevens en de eis dat passagiers bagageregels persoonlijk bevestigen. The Register meldt vergelijkbare beperkingen bij banken en Amazon, maar United had nog niet uitgelegd hoe het bedrijf het beleid wil handhaven.

Bron: https://www.theregister.com/ai-and-ml/2026/11/12/united-airlines-wants-you-to-check-in-not-your-chatbot/5309373

**Japan stond op plaats 32 van de 121 landen wat betreft Claude-gebruik per inwoner.** Een commentaar in Nikkei Asia gebruikt de Anthropic Economic Index om te betogen dat de adoptie laag blijft in sectoren met personeelstekorten. De ranglijst meet de assistent van één leverancier, niet het nationale AI-gebruik, en tijdens het onderzoek was alleen de inleiding leesbaar.

Bron: https://asia.nikkei.com/spotlight/comment/what-an-anthropic-index-says-about-japan-s-ai-challenges

## Wat mensen bouwen

**Folate rangschikt DOM-elementen voor browseragents met een CPU-model van 107 MB.** De INT8 ONNX-cross-encoder gebruikt ongeveer 180–250 MB geheugen. De maker meldt 88,9–93,3 procent Top-1-nauwkeurigheid op Mind2Web-deelsets en 2,3–4,3 seconden per stap op twee virtuele CPU's.

Bron: https://github.com/figranium/folate

**nano-edge-tts vervangt de golfvormdecoder van Kokoro-82M door twee kleine netwerken met in totaal 1,75 miljoen parameters.** De modelkaart meldt een 33-voudige versnelling van de decoder op één CPU-thread, een 11-voudige winst voor de volledige pijplijn en 0,75 GB piekgeheugen. Dit zijn de metingen van de auteur.

Bron: https://huggingface.co/drmhse/nano-edge-tts

**Yogurt neemt vergaderingen lokaal op, transcribeert ze en vat ze samen.** De desktopapp met MIT-licentie draait op Mac, Windows en Ubuntu, gebruikt llama.cpp met een model met open gewichten, heeft 8 GB geheugen nodig en werkt na de eerste download offline.

Bron: https://github.com/FrigadeHQ/yogurt

**local-agent-bench vergeleek een 4-bits Qwen3-8B op een Mac met Claude Opus 5.5 op 200 taken.** Het lokale model evenaarde of versloeg Opus op numerieke velden en bronverwijzingen, maar bleef achter op volledige antwoorden, statusnauwkeurigheid en uitleg. De repository meldt één testronde per model, een eigen beoordelaar, een mediane lokale latentie van 2,1 seconden en 1,64 dollar voor de cloudrun.

Bron: https://github.com/qvotvm/local-agent-bench

**db-branch geeft agents wegwerpbare MySQL- en PostgreSQL-databases via ZFS-klonen.** Copy-on-write-vertakkingen verschijnen zonder een grote database te kopiëren en kunnen verlopen of worden gereset. De bètadienst vereist Linux en ZFS, met een Multipass-opstelling voor Mac en Windows.

Bron: https://github.com/db-branch/db-branch

**RealtimeVAD meldde een pauzesignaal 92 milliseconden vóór de waarschijnlijkheidsdaling van Silero.** Het hulpmiddel voegt een energiecontrole van 10 ms toe tegen achtergrondgeluid en het niveau van de spreker. De maker mat 3.153 spreekbeurten van één spreker en vond geen winst bij een microfoon op afstand.

Bron: https://github.com/KoljaB/RealtimeVAD

**Redacted verwijdert geheimen uit commando-uitvoer voordat een codeerassistent die leest.** De Claude Code-hook herschrijft uitvoer van gewone opdrachten zoals `git diff` of `kubectl get secret` en kan projectspecifieke namen van geheimen leren.

Bron: https://github.com/svn-arv/redacted/

**turbo-browser-mcp bundelt Playwright-acties en geeft DOM-wijzigingen terug in plaats van volledige herhaalscans.** Een synthetische benchmark van de auteur mat 1.135 tokens voor een pagina met 140 knoppen in plaats van 18.654 voor HTML, en 56 tokens voor een wijziging na een klik in plaats van 3.582 voor een volledige ARIA-scan.

Bron: https://github.com/Tthanh2k6/turbo-browser-mcp

**Taskless zet correcties aan codeeragents om in lintregels.** Een skill schrijft ast-grep- of Vale-regels naar de repository, en `taskless check` meldt bestand, regel en ernst voor lokaal gebruik of CI.

Bron: https://github.com/taskless/cli

**mcp-attest controleert of een MCP-server acties weigert die zijn beleid verbiedt.** Het programma verbindt als elke opgegeven identiteit, voert echte toolaanroepen uit en vergelijkt de uitkomsten met 24 beleids- en OAuth-regels. De MIT-repository bevat een opzettelijk kwetsbare voorbeeldserver.

Bron: https://github.com/Balanov/mcp-attest

## Het lezen waard

**Sebastian Raschka legt uit hoe huidige LLM's de positie van tokens coderen.** Het overzicht behandelt absolute embeddings, RoPE, gedeeltelijke RoPE, lagen zonder positiecodering en methoden die positie toevoegen aan aandachtscores, met PyTorch-voorbeelden en vergelijkingen van actuele modellen.

Bron: https://magazine.sebastianraschka.com/p/understanding-positional-embeddings

**Meta FAIR meldt dat e-means de verlieswaarde van Lloyd's k-means 10–45 keer sneller bereikt op een GPU.** De open implementatie gebruikt mini-batchupdates, exponentiële voortschrijdende gemiddelden en schalingswetten die de batch- en stapgrootte bepalen. De auteurs melden ook een acht- tot vijftienvoudige versnelling op de CPU ten opzichte van Faiss.

Bron: https://e-means.github.io/

**Simon Willison constateerde dat Gemini Decision 1 gegradeerde waarschijnlijkheden teruggaf waar twee concurrenten harde antwoorden leverden.** Bij zijn videotest gaf Gemini 0,92 voor “robot” en 0,05 voor “dragon”, terwijl Jev en OpenAI 1,0 of 0,0 teruggaven. Gemini accepteert tekst, afbeeldingen, audio, video en pdf's en kost 10 cent per miljoen inputtokens.

Bron: https://simonwillison.net/2026/Nov/11/gemini-decisions-api/

**vLLM legt uit hoe het Inkling 2 Small met 594 miljard parameters op één node draait.** Het multimodale mixture-of-expertsmodel activeert 17 miljard parameters en combineert NVFP4- met MXFP8-experts. vLLM meldt tot 630 tokens per seconde per gebruiker op GB200-hardware; dat is een meting volgens het bedrijf.

Bron: https://blog.vllm.ai/2026/11/12/inkling2-small.html

## Hacker News

**Een discussiedraad met 1.105 punten debatteerde over de vraag of door AI gegenereerde code open source moet zijn.** Eén AGPL-auteur beschreef modellen die zijn code reproduceerden en een bedrijf dat zijn systeem kloonde na licentiemeldingen. Andere reageerders betoogden dat licenties auteursrecht vereisen en verwezen naar Amerikaanse rechtszaken die puur machinaal gegenereerd werk geen auteursrecht toekennen; hun juridische lezingen zijn geen juridisch advies.

Bron: https://news.ycombinator.com/item?id=50507303

**Een experiment met de ECU van een Jeep legde het risico van actuatoren bij codeeragents bloot.** De auteur zei dat Claude voorstelde de brandstofpomp te laten draaien en de brandstofrail bleef vullen tot hij het stopte. Een andere reageerder beschreef het bouwen van een OBD-hulpmiddel met Claude en waarschuwde tegen vertrouwen op actuatorfuncties; beide verhalen zijn anekdotes.

Bron: https://news.ycombinator.com/item?id=50463399

## Reddit

**De maker van Basalt meldde Qwen 3.8 27B tot 770 tokens per seconde op een RTX 5090.** Over 30 codeersessies van 16–32K tokens mat de auteur een prompt-path KLD van 0,016 en 97,1 procent Top-1-overeenstemming. Een reageerder betoogde dat KLD kwaliteitsverlies bij langlopend werk mist en vroeg om SWE-achtige tests.

Bron: https://old.reddit.com/r/LocalLLaMA/comments/1xx1cu9/basalt_040_more_models_still_as_fast_qwen_27b_up/

**inside-llm toont token voor token waar twee GGUF-kwantisaties uiteenlopen.** Het browserhulpmiddel voor llama.cpp laat waarschijnlijkheden per token zien en waar elk model een ander token zou kiezen. De discussiedraad meldde geen evaluatieresultaten.

Bron: https://old.reddit.com/r/LocalLLaMA/comments/1xx7qbf/i_have_created_a_tool_to_observe_what_happens/

## YouTube

**Stanford Online publiceerde een college van 78 minuten over geheugenarchitecturen voor agents.** CS329Z Lecture 7 behandelt geheugentypen, MemGPT, evaluatie en open vraagstukken. De samenvatting komt uit het openbare dia-overzicht omdat het transcript niet beschikbaar was.

Bron: https://www.youtube.com/watch?v=qh5tP6PBZ6U

**Nathan Labenz besprak de evaluatie van geavanceerde AI op Bletchley Park.** De keynote van 44 minuten voor Cognitive Revolution put uit bevindingen van METR, Apollo Research, OpenAI en het Britse AI Security Institute. De aankondiging van het evenement noemt onvoorspelbaarheid het kernprobleem; de video werd tijdens het onderzoek niet getranscribeerd.

Bron: https://www.youtube.com/watch?v=asHjYwa7naE

**Aktuality.sk vroeg zich af of de vraag naar AI het tekort aan geheugenchips tot 2030 zal verlengen.** De Slowaakse Chipcast van 32 minuten verbindt de vraag vanuit datacenters met prijzen voor telefoons, laptops en servers. De samenvatting berust op de titel en de kanaalvermelding omdat de videopagina geblokkeerd was.

Bron: https://www.youtube.com/watch?v=gWp9nVYKUpo

## In het kort

**Cursor koppelde een opslagbucket met gekopieerde codeeragent-sporen aan een toegangssleutel van Fireworks AI.** De sporen kwamen uit sessies buiten Privacy Mode en sommige bevatten inloggegevens; Cursor zegt dat minder dan 0,01 procent van de API-inloggegevens van klanten betrokken was. Een apart gestolen inloggegeven plaatste kwaadaardige builds van de Claude Code-extensie gedurende ongeveer 11 uur in de marktplaatscache van Cursor.

Bron: https://thehackernews.com/2026/11/stolen-fireworks-ai-key-led-to-cursor.html

**De FBI zegt dat aanvallers het open-sourceframework ARTEX sinds augustus bij echte inbraken hebben gebruikt.** De waarschuwing betreft doelen in de financiële sector, overheid, technologie, defensie en gezondheidszorg, waarbij sommige incidenten binnen drie uur toegang met hoge rechten bereikten. Onderzoekers telden begin november meer dan 1.600 blootgestelde consoles.

Bron: https://www.bleepingcomputer.com/news/security/fbi-warns-artex-ai-hacking-tool-is-powering-global-cyberattacks/

**Het Pentagon hernoemde zijn Chief Digital and Artificial Intelligence Office tot het Super Intelligence Office.** Bestaande programma's en aanbestedingen lopen door, zodat de wijziging een naamsverandering is en geen nieuwe capaciteit of regel.

Bron: https://www.securityweek.com/pentagon-renames-cdao-super-intelligence-office/

## Zakelijk in het kort

**Apple en OpenEvidence zijn een onderzoek gestart naar hoe tot wel 200.000 Amerikaanse iPhone-gebruikers gedurende minstens 12 maanden AI voor hun gezondheid gebruiken.** Bron: https://techcrunch.com/2026/11/15/apple-launches-new-app-to-study-how-people-use-ai-for-health/

## Om in de gaten te houden

De beursgang van Anthropic wordt verwacht op donderdag 19 november. Nvidia rapporteert op woensdag 18 november zijn eerste kwartaal sinds het vertrek van Jensen Huang.
