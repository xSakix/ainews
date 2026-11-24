+++
title = "Dagelijks AI-overzicht – 24 november 2026"
slug = "dagelijks-ai-overzicht-24-november-2026"
description = "China heeft AI ingezet voor socialezekerheidsdiensten in 15 regio's, terwijl Singapore zijn groeiverwachting verhoogde door de vraag naar AI-elektronica. Aleph Alpha bracht een open Duits-Engels redeneermodel uit en een kwantisatie van 10 GB hield op verschillende agentbenchmarks gelijke tred met het oorspronkelijke model van 54 GB."
tags = ["models", "research", "agents", "business"]
date = 2026-11-24T03:58:39+01:00
draft = false
+++

## Belangrijkste nieuws

**China meldt dat AI in één provincie zeven miljoen socialezekerheidszaken heeft verwerkt.**

Een rapport van de Internationale Arbeidsorganisatie (ILO) beschrijft 45 toepassingen in 15 regio's op provincieniveau. Daarvan verbetert 47 procent de dienstverlening, ondersteunt 33 procent de administratie en dekt de rest risico- of beslissingsondersteuning.

In het district Haidian in Peking verwerkten geautomatiseerde systemen in 2024 meer dan 70.000 transacties en verhoogden zij de verwerkingsefficiëntie met meer dan 80 procent ten opzichte van handmatig werk. De beoordelingssystemen in Guangdong behandelden tegen juli 2025 meer dan zeven miljoen zaken verspreid over 34 diensten en bespaarden meer dan 640.000 personeelsuren.

De praktijkgevallen zijn samen met het Chinese ministerie van Arbeid geselecteerd en vormen geen representatieve steekproef. Volgens de ILO moeten mensen blijven beslissen over het recht op uitkeringen en over arbeidsongevallen, en moet offline dienstverlening beschikbaar blijven voor mensen die digitale drempels ervaren.

Bron: https://www.ilo.org/resource/news/ai-transforming-social-security-services-china-new-ilo-report-finds

**Singapore heeft zijn groeiraming voor 2026 verhoogd tot ongeveer 6 procent doordat de vraag naar AI-elektronica de export aanjoeg.**

De economie groeide in het derde kwartaal met 6,1 procent op jaarbasis. Functionarissen schreven een groot deel van die groei toe aan elektronica die samenhangt met de AI-investeringscyclus en stelden hun raming voor het hele jaar naar boven bij.

Voor 2027 vertraagt de verwachting tot 2,5 tot 4,5 procent. Dat verschil is van belang voor een exporteconomie waarvan de leveringen van halfgeleiders en servers nu afhangen van aanhoudende datacenterinvesteringen in het buitenland; het gaat om een officiële prognose, niet om een meting van AI-productiviteit binnen Singaporese bedrijven.

Bronnen: https://asia.nikkei.com/economy/singapore-gdp-grows-6.1-in-q3-as-ai-demand-stays-strong, https://www.bloomberg.com/news/articles/2026-11-24/singapore-raises-gdp-growth-outlook-to-around-6-on-ai-boom

**Aleph Alpha heeft Kolibri 1.1 uitgebracht met 75 miljard parameters en een oorspronkelijk contextvenster van 262.144 tokens.**

Het Duits-Engelse redeneermodel onder Apache-2.0-licentie activeert 3,44 miljard parameters per token. De gewichten nemen ongeveer 77,6 GB in beslag, waardoor het schaarse ontwerp vooral de rekenkracht en niet het geheugengebruik beperkt.

Aleph Alpha meldt na natraining een benchmarkgemiddelde van 73,2, tegenover 66,6 voor Kolibri 1.0, terwijl Qwen3.8 Flash Next in dezelfde tabel op 80,1 uitkomt. De modelkaart raadt aan bij moeilijke taken op of onder de oorspronkelijke contextlimiet te blijven, hoewel de implementatie kan worden uitgebreid tot ongeveer een miljoen tokens.

Bron: https://huggingface.co/Aleph-Alpha/Kolibri-1.1

**Nari Labs comprimeerde Qwen3.8-27B van 53,8 GB naar 10,12 GB zonder terrein te verliezen op drie van zijn benchmarks.**

NariQ gebruikt trellisgecodeerde kwantisatie na de training die is gekalibreerd op sporen van programmeeragents. De driebitsversie van het lab scoorde 41,0 op DeepSWE tegenover 39,8 voor BF16, 63,8 tegenover 62,6 op Terminal-Bench en 98,3 tegenover 97,7 op AIME 2025–26.

De kleinere tweebitsversie zakte op die tests naar 28,6, 52,4 en 86,0. Bovendien vereisen de bestanden de llama.cpp-fork van Nari Labs, die is afgestemd op Nvidia's SM120-architectuur, trager draait op oudere Nvidia-kaarten en Metal, en geen AMD- of Intel-GPU's ondersteunt.

Bron: https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF

**Tweederde van 58 klanten van Anthropic gaf aan dat AI hun aanwervingen heeft verminderd.**

Het economische team van Anthropic hield 66 interviews bij zakelijke klanten in de Verenigde Staten. Slechts twee bedrijven hadden een functie geschrapt door automatisering en vijf hadden werknemers ontslagen die zich tegen AI verzetten, terwijl tien bedrijven extra personeel aannamen, vooral voor implementatie en IT-ondersteuning.

Het effect deed zich vaker voor bij de instroom: tweederde meldde minder mensen aan te nemen, en ongeveer een derde van die groep liet afdelingen krimpen via natuurlijk verloop. Negen bedrijven schroefden de inzet van externe krachten terug. Van 100 stukken met AI gebouwde software die gedetailleerd genoeg waren beschreven om in te delen, automatiseerden er 80 handmatig werk en vervingen er 20 ingekochte software.

De steekproef is klein, niet willekeurig en beperkt tot klanten van de aanbieder zelf. Waardeoordelen waren grotendeels kwalitatief en zelfgerapporteerd in plaats van gemeten in gecontroleerde proeven.

Bron: https://www.anthropic.com/research/working-with-ai

## Nieuwe modellen en releases

**Ant Group bracht Ling-3.2-air met 124 miljard parameters uit onder de MIT-licentie.** Het model activeert 5,5 miljard parameters en combineert 35 lineaire-aandachtslagen met zeven gated-attentionlagen. De uitgever meldt dat 87,7 procent van de criteria op zijn juridische benchmark wordt gehaald, maar slechts 0,8 procent van de voorbeelden slaagde voor alle criteria na een controle op materiële hallucinaties; bij de modelkaart ontbreekt een technisch rapport.

Bron: https://huggingface.co/inclusionAI/Ling-3.2-air

**Tencent bracht vijf WeMM-Ecom-beeld-taalmodellen voor online detailhandel uit.** De groottes lopen uiteen van 0,8 miljard parameters tot een mixture-of-expertsmodel van 35 miljard parameters dat 3 miljard parameters activeert. Tencent meldt een vooruitgang van 3,92 punt over 28 e-commercebenchmarks ten opzichte van het basismodel Qwen3.5, maar slechts 0,17 punt over 64 algemene benchmarks; die scores komen uit BF16 en niet uit de nieuwe gekwantiseerde versies.

Bron: https://huggingface.co/tencent/WeMM-Ecom-35B-A3B-GPTQ

**AI Singapore voegde een speculatieve decoder van 2 miljard parameters toe voor zijn SEA-LION-model van 9 miljard parameters.** De uitgever mat 2,26 tot 3,08 keer zoveel tokens per seconde bij gelijktijdigheid één, vanaf een uitgangswaarde van bijna 195 tokens per seconde. Bij gelijktijdigheid 16 slinkt het voordeel tot hoogstens 1,5 keer en bij 32 verdwijnt het mogelijk helemaal, zodat dit eerder een hulpmiddel is voor lage latentie bij lichte belasting dan voor hoge doorvoer.

Bron: https://huggingface.co/aisingapore/Qwen-SEA-LION-v5-9B-SpecDecoder

**Anthropic zet Claude Opus 4.5 op 22 januari 2027 stop en opende Enterprise Frontier Safeguards in bèta.** Die veiligheidsmaatregelen behouden Zero Data Retention terwijl versleutelde kopieën van prompts en antwoorden voor veiligheidscontrole in de eigen cloudaccount van de klant worden opgeslagen. Teams die vastzitten op `claude-opus-4-5-20251101` hebben ongeveer twee maanden om over te stappen op Opus 5.5.

Bron: https://platform.claude.com/docs/en/release-notes/api

**Gebruikers van de Gemini API kunnen nu betalen voor geselecteerde pagina's, cellen en media-intervallen in plaats van volledige bestanden.** File slicing werkt in alle Gemini 4-modellen en voegt rechtstreekse uploads van Office- en OpenDocument-bestanden toe. Vercel mat 14 keer minder tokens bij het vluchtig doorlopen van geëxtraheerde PDF-tekst; LiteLLM mat 67 procent minder tokens voor één PDF en 33 procent minder voor één werkmap, beide volgens tests van partners zonder prijzen of numerieke bestandslimieten.

Bron: https://blog.google/innovation-and-ai/technology/developers-tools/file-slicing-controls/

## Onderzoek

**Een audit verifieerde slechts 29,3 procent van de taken in zes meerstaps-benchmarksuites.** Twee auteurs bekeken 749 taken uit acht benchmarks en 767 openbare modelevaluaties. Bevestigde gebreken weigerden in 71,7 procent van de gevallen erkenning aan correcte oplossingen, terwijl de rest sluiproutes toeliet; gepatchte containers brachten bevestigde omzeilingen tijdens de uitvoering terug van 14,7 naar 2,7 procent. Dit is de eerste mijlpaal van de auteurs in een lopende herziening, en hun werkwijze bepaalt wat als geverifieerd geldt.

Bron: https://arxiv.org/abs/2611.27622

**Een redeneergraafmethode maakt onderscheid tussen getrouwe en efficiënte redeneerketens.** De auteurs meten of semantische ondersteuning de voorspelling van een model verklaart en of tussenstappen op een pad naar het antwoord blijven. Ongetrouwheid en inefficiëntie correleerden slechts zwak of wisselend met juistheid, en gerichte finetuning verbeterde beide eigenschappen zonder de nauwkeurigheid te verlagen; de samenvatting noemt geen effectgroottes en het resultaat hangt af van de graafconstructie van de auteurs.

Bron: https://arxiv.org/abs/2611.27100

**Veertien taalmodellen vormden bij het kiezen uit opties een patroon van eerst comprimeren en daarna vergelijken.** In 12 benchmarks comprimeerden de middelste lagen de prompt tot een knelpunt van lage rang, waarna latere lagen die uitbreidden tot een vergelijkingsgeometrie. Ingrepen van lage rang nabij dat knelpunt veranderden latere voorkeuren, maar het NeurIPS-artikel van één auteur rapporteert het patroon via een eigen covariantiemethode.

Bron: https://arxiv.org/abs/2611.26874

**Synthetische enquêtedeelnemers reproduceerden slechts 0,4 tot 10,5 procent van de variatie in menselijke voorkeuren.** Drie open modelfamilies speelden beleidskeuzes na van 1.991 Chileense, 843 Franse en 434 Braziliaanse volwassenen. Geen enkele van de 27 condities benaderde tegelijk individuele keuzes, heterogeniteit in de bevolking en politieke ordening; het veranderen van de volgorde van voorstellen wijzigde 12,3 tot 31,2 procent van de modelkeuzes.

Bron: https://arxiv.org/abs/2611.28383

**Snelle beslismodellen bespaarden tijd, maar bleken veel gemakkelijker te vergiftigen.** Vier modellen haalden gemiddeld 91 procent zuivere nauwkeurigheid op 1.440 synthetische paren van browsertaken, terwijl twee voorbeelden van geïnjecteerde opmerkingen een aanvalssucces van 81,2 procent opleverden. Op 48 gekoppelde taken beantwoordde een korte redeneerketen 95,83 procent van de vergiftigde invoer correct tegenover 38,54 procent voor de snelle variant, in 1,94 seconde in plaats van 0,29. Een afzonderlijk System-1-model van 4 miljard parameters meldt 75 tot 91 procent lagere kosten per episode op drie benchmarks, maar testte geen vijandige invoer.

Bronnen: https://arxiv.org/abs/2611.27679, https://arxiv.org/abs/2611.23751

**Sommige interpreteerbaarheidstests kunnen een kenmerk goedkeuren dat het model niet gebruikt zoals beweerd.** Het artikel construeert “parasietkenmerken” die één richting om invoer te onderscheiden combineren met een andere die uitvoer stuurt, en zo via ongerelateerde paden slagen voor een test voor causale abstractie. Experimenten tonen dat falen aan bij syntactische congruentie en tweecijferige optellingen; het resultaat is een waarschuwing uit twee taken, geen vervangende methode.

Bron: https://arxiv.org/abs/2611.26711

**Een hersentoestandbenchmark toonde aan dat het voorspellen van prikkels niet betekent dat een model de interne toestand van een kijker volgt.** Encoders die alleen op prikkels werken behaalden een voorspelcorrelatie van 0,320, maar nul op de maatstaf State van de benchmark. Het tweetijdschalenmodel van de auteurs haalde een correlatie van 0,349, 5,5 procent op State, 16 procent op Forecast en 20,3 procent op Updating, waarbij de absolute score op State nog steeds laag blijft.

Bron: https://arxiv.org/abs/2611.28508

**De meeste geslaagde equivalentietests voor mensensimulaties in één audit zouden ook een nuleffectmodel hebben goedgekeurd.** Bij een heranalyse van 70 experimenten bleek 72 procent van de geslaagde resultaten van GPT-4 binnen een marge van plus of min 0,20 standaardafwijking ook te gelden voor een nulreferentie. Een vooraf geregistreerde Claude-simulatie haalde drie intentiedoelen, maar verschoof normopvattingen met 0,065 standaardafwijking tegenover 0,351 bij mensen; het artikel wijst zelf op achteraf toegevoegde onderdelen in een deel van de analyse.

Bron: https://arxiv.org/abs/2611.27186

**Een adapter met vaste capaciteit leerde wat hij moest onthouden en wanneer hij moest vergeten.** Een regelaar kent geheugens onafhankelijke vervalsnelheden toe binnen een LoRA-adapter en bereikte 86 procent van de orakelprestatie op de synthetische gebruikerstrajecten van de auteurs. Een verwante studie vond dat het mengen van korte en lange trajecten stabiele regels met minder tokens kan aanleren, maar beide uitkomsten komen uit zelfgebouwde werelden.

Bronnen: https://arxiv.org/abs/2611.25235, https://arxiv.org/abs/2611.28613

**Een tweede AI-partner toevoegen leverde meer brainstormideeën op, maar minder menselijke inbreng.** Het laboratoriumonderzoek met N=168 vergeleek kamers met twee agents met paren van twee mensen; alleen de tweede agent vergrootte de differentiatie binnen een sessie. De taak was smal en het resultaat met één agent liet zich niet veralgemenen. Bron: https://arxiv.org/abs/2611.26663

**Een gespecialiseerd gedragsmodel en twee audits verschillen van inzicht over wat goede synthetische mensen vereisen.** Chiron, getraind op 288.307 dossiers en 1.411.750 beslissingen, meldt tot 28,4 procent betere individuele voorspellingen dan topmodellen en 82,2 tot 94,3 procent minder fouten in effectgroottes. De audit van synthetische publieken vond sterk samengedrukte variatie, terwijl de equivalentie-audit aantoonde dat veel ogenschijnlijke overeenkomsten ook nuleffecten aanvaarden; alle drie gebruiken door de auteurs gekozen taken.

Bronnen: https://arxiv.org/abs/2611.24830, https://arxiv.org/abs/2611.28383, https://arxiv.org/abs/2611.27186

## Economie en werk

**Beursgenoteerde bedrijven met een hogere gemeten blootstelling aan agents plaatsten later minder vacatures voor niet-seniorfuncties.** Een werkdocument koppelt ongeveer twee biljard modeltokens aan 34,8 miljoen vacatures. Een stijging van één standaardafwijking op zijn beursmaatstaf voor blootstelling ging vooraf aan 2,11 procent lagere vacaturegroei na zes maanden en 3,20 procent na negen maanden; het resultaat gaat over vacatures, niet over ontslagen, en leidt blootstelling af uit marktreacties.

Bron: https://arxiv.org/abs/2611.27210

**Claude Ship verschuift programmeeragents van het schrijven van code naar het beoordelen en goedkeuren ervan.** Anthropic zegt dat het aantal samengevoegde pull requests tussen juni en september meer dan verdubbelde terwijl het aandeel teruggedraaide wijzigingen met meer dan 40 procent daalde, zonder noemers of een vergelijkingsgroep te publiceren. Code Review is algemeen beschikbaar, terwijl PR Steward en Approvals in bèta blijven; beheerders kunnen de gefactureerde tokenuitgaven begrenzen.

Bron: https://claude.com/resources/articles/introducing-claude-ship

**Volgens een economisch model kunnen trage taken die als “zwakke schakel” fungeren explosieve winst uit snel verbeterend kapitaal blokkeren.** Het NBER-werkdocument schat dat de productiviteit in kapitaalcomplementaire taken jaarlijks ongeveer vijf procentpunt sneller stijgt dan in arbeidstaken. De grote geaggregeerde groei-uitkomst hangt af van taaksubstitutie en knelpunten binnen het model en is dus een mechanisme in plaats van een prognose.

Bron: https://www.nber.org/papers/w36050

**AlphaFold2 verschoof experimenten in de structurele biologie naar eiwitten dicht bij bekende voorbeelden.** Een NBER-studie volgt 530.471 eiwitten en stelt vast dat betrouwbare voorspellingen het aantal experimenten op bekende eiwitten en nauwe verwanten verhoogden, terwijl pogingen voor verafgelegen eerste structuren afnamen. Het onderzoek meet waar onderzoekers hun experimenten op richtten, niet de uiteindelijke wetenschappelijke waarde van die keuzes.

Bron: https://www.nber.org/papers/w36045

## Prompttechnieken

**Een op OWASP afgestemd promptblok verminderde het aantal scannermeldingen in met AI gebouwde webapps met ongeveer een derde.** Honderd specificaties werden vier keer gebouwd met Claude Code en Codex, wat 6.721 beoordeelde meldingen opleverde. De incidentieratio was 0,65 met een 95-procentinterval van 0,60 tot 0,71, maar het blok verdubbelde het aantal opgegeven afhankelijkheden en scannermeldingen zijn nog geen bewezen exploits.

Bron: https://arxiv.org/abs/2611.28408

**Een model opdragen opgehaalde tekst te verifiëren deed het vaker onjuiste antwoorden overnemen.** FutureBench testte 3.629 vragen op zes modellen. Een waarschuwing dat passages misleidend kunnen zijn herstelde 82,5 tot 98,9 procent van de juiste antwoorden die de gewone Verify-prompt had verdrongen, met minder dan één punt verandering bij kloppende passages; het resultaat komt uit één benchmarkfamilie van twee auteurs.

Bron: https://arxiv.org/abs/2611.23601

## Wat mensen bouwen

**Gall houdt een mixture-of-expertsmodel van 26 miljard parameters op een MacBook Air van 24 GB door het na elk antwoord uit het geheugen te verwijderen.** De engine in Rust en Metal slaat de gespreksstatus op, zakt in rust terug naar 32–57 MB geheugen en laadt een warme status in ongeveer 0,1 seconde opnieuw. De auteur mat ongeveer 20 tokens per seconde bij korte context en 16 bij 29.900 tokens op één M2 Air; de modelkwaliteit en de aangeprezen instelling van 100.000 tokens werden niet geëvalueerd.

Bron: https://github.com/ltrgoddard/gall

**OCRia-nano-1 verwerkt documenten op een CPU met 8,1 miljoen parameters.** LlamaIndex meldt een score van 59,2 op ParseBench-2 en 27,8 pagina's per seconde op 16 virtuele CPU's. De grafiekscore bedraagt slechts 3,1 tegenover 77,4 voor het leraarmodel van 4 miljard parameters, en voor de gewichten geldt een eigen licentie die grotere commerciële gebruikers beperkt.

Bron: https://huggingface.co/llamaindex/OCRia-nano-1

**OpenToolSearch gebruikt twee modellen van 0,6 miljard parameters om uit grote toolcatalogi te kiezen.** De herordenaar haalt een nDCG@10 van 70,8 op het openbare ToolRet en 89,0 op de eigen set van de auteurs, tegen naar eigen opgave 0,19 dollar per 1.000 zoekopdrachten en een mediane latentie van 0,10 seconde. Concurrenten scoren hoger op beide tests, en de auteurs raden aan de volledige lijst rechtstreeks aan een model te geven zodra die ongeveer 200 tools of minder bevat.

Bron: https://github.com/ai3inc/opentoolsearch

**CubePod biedt programmeeragents blijvende Kata-microVM-sandboxen.** Het E2B-compatibele Kubernetes-project beweert toewijzing uit een warme pool onder 50 milliseconden te halen en hervatting over nodes heen of copy-on-write-forks rond één seconde. Voor die cijfers ontbreekt een gepubliceerde methode, en voor uitrol zijn Kata Containers plus een stuurprogramma voor blokopslag nodig. Bron: https://github.com/cubeplexai/cubepod

**Twee kleine tools bewaken agentafhankelijkheden op verschillende momenten.** mcpwatch vergrendelt MCP-toolbeschrijvingen en blokkeert gewijzigde tools tijdens de uitvoering, maar de veiligheidsscores bieden geen garanties en de vingerafdrukmethode is niet gedocumenteerd. slop-deps scant imports tegen 4.179 pakketnamen en registers, inclusief controles op typfouten en homogliefen; het tijdsvoorbeeld met 142 bestanden is illustratief en de hele codebase is onder menselijke regie door agents geschreven.

Bronnen: https://www.mcpwatch.io, https://github.com/viditx/slop-deps

**Terminal Tasks Open publiceert 30 taken en een audit van gebreken in een grotere benchmark.** De auteur meldt gebreken in 23 van de 66 taken van Terminal-Bench 4.1 en deelt ongeveer 52 procent van 980 mislukte agentpogingen in als overfitting, 31 procent als verkeerde beoordeling en 9 procent als verkeerde afhandeling. De auditor bouwde ook de vervangende benchmark en verkoopt een evaluatiepijplijn, terwijl de categorieën van hemzelf komen.

Bron: https://vetto.ai/companies/terminal-tasks-v2/

## Het lezen waard

**Hugging Face laat zien hoe een agentbenchmark een sluiproute kan belonen in plaats van de taak zelf.** Een script leverde op alle acht Ramanspectrumtaken de juiste defectverhouding op zonder pieken aan te passen, waardoor de auteurs controles per piek moesten toevoegen. gpt-oss-120b slaagde voor 11 van de 24 runs, en voor 13 toen alleen de inferentieaanbieder veranderde; drie sterkere modellen slaagden voor alle 24, zodat de kleine aangepaste set hen niet kan rangschikken.

Bron: https://huggingface.co/blog/agentic-evals

**Een door AMD gesteunde test verving een DRAM-pool voor agent-KV-cache door NVMe bij vrijwel gelijke doorvoer.** Met Kimi-K3 op 16 MI355X-GPU's bleven drie gelijktijdigheidstests binnen één procent van DRAM, terwijl het cachetrefpercentage 96 procent van de doorvoervariatie over 42 runs verklaarde. De NVMe-schijven zouden hun gespecificeerde schrijflevensduur in ongeveer 5,5 maand verbruiken als bij 96 sessies elk blok werd opgeslagen, en de meeste vergelijkingen waren enkelvoudige runs met ongeveer 2,5 procent ruis.

Bron: https://vllm.ai/blog/2026-11-23-skip-the-dram-tier

**Agentteams op basis van Gemini 4 vonden goedkopere kwantumcircuits en bewezen elk resultaat in Lean.** Google DeepMind meldt 11,8 keer lagere rekenkosten voor één fusiesimulatie, 2,5 keer voor cytochroom P450 en 290 keer voor een arcsin-routine. Mensen kozen en begeleidden de problemen, en de gevonden circuits overschrijden nog steeds de waarschijnlijke capaciteit van vroege foutgecorrigeerde kwantumcomputers.

Bron: https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification/

**Anthropic publiceerde een door AI geschreven bewering dat VP verschilt van VNP, met een Lean-bewijs maar zonder menselijke wiskundige beoordeling.** De repository vermeldt dat een onafhankelijke kernel de formele uitspraken controleert met standaardaxioma's. Niets controleert machinaal of die uitspraken overeenkomen met de beweringen in het artikel, en het project noemt zichzelf een niet-onderhouden momentopname; het beslecht P versus NP niet.

Bron: https://github.com/anthropics/formal-math/tree/main/vp-vnp

## Hacker News

**GLM-5.4 maakte gelaagde lus-transformers binnen één week tot een tweede architectuurtrend.** Z.ai zegt dat gedeelde lagen herhaaldelijk draaien om effectieve diepte toe te voegen zonder extra parameters, en Simon Willison vergelijkt het idee met Inkling 2 Mini van Thinking Machines. Zijn praktijktest bestond uit één beeldprompt, de gewichten zijn niet open en de toegankelijke bronnen gaven geen aantal parameters of formele benchmark; de discussiedraad op Hacker News bereikte 1.075 punten.

Bronnen: https://simonwillison.net/2026/Nov/23/glm-54/, https://news.ycombinator.com/item?id=50609685

## YouTube

**Dex Horthy van Factory stelt 12 controles voor software voor die door agents is gebouwd.** De Engelstalige lezing op AI Engineer behandelt planning, druk tussen fasen, feature flags, evaluaties en agents die hun eigen werk testen. Horthy zegt dat het beste model ongeveer 16 procent scoort op Slop Code Bench, zonder het aantal taken te noemen; Factory verkoopt programmeeragents, dus de regels zijn de praktijk van een aanbieder in plaats van een gecontroleerd resultaat.

Bron: https://www.youtube.com/watch?v=-NFMsM2y0Vk

**De Stanford-cursus CS312 vraagt studenten trainingsresultaten te voorspellen voordat ze die zien.** Het achtlagige model van 30 miljoen parameters traint in ongeveer tien minuten op één GPU, waardoor experimenten met leersnelheden en architectuur goedkoop genoeg zijn voor in de klas. De samenvatting is gebaseerd op de Engelstalige videobeschrijving in plaats van een transcript. Bron: https://www.youtube.com/watch?v=JLcCYvUawsM

## In het kort

**Dezelfde veiligheidsmonitor miste 0,2 procent of 23 procent van de geslaagde aanvallen afhankelijk van hoe die aanvallen waren gegenereerd.** Het Britse AI Security Institute testte één voormalige productiemonitor van OpenAI tegen aanvallen van verschillende aanvalsstrategieën; één reinforcement-learningrun verhoogde het mispercentage van 0,5 naar 20,8 procent. Dit betreft één opstelling, maar het laat zien dat synthetische monitorscores geen stand houden zonder onderbouwing dat de aanvalsstrategie representatief is voor toekomstige aanvallen.

Bron: https://www.aisi.gov.uk/blog/attack-policy-selection-can-make-monitor-evaluations-misleading

**OpenAI en Cisco brachten Shirudo uit om een exploitpad in een draaiende Linux-dienst te blokkeren voordat een patch is geïnstalleerd.** De ondertekende eBPF-schilden vereisen goedkeuring van een beheerder en laten een door TPM onderbouwde registratie achter. Eén gecontroleerde test van de aanbieders hield Java4Shell tegen op Elasticsearch zonder herstart; het bericht geeft geen prestatie- of adoptiecijfers, en het schild blijft een tijdelijke maatregel.

Bron: https://openai.com/index/introducing-shirudo

**CISA voegde een path-traversalkwetsbaarheid in MONAI Label toe aan zijn catalogus van misbruikte kwetsbaarheden.** CVE-2026-133968 kan een niet-geauthenticeerde aanvaller buiten de gegevensopslag van de medische-beeldvormingsserver laten schrijven en mogelijk code laten uitvoeren; Amerikaanse federale diensten kregen tot 26 november de tijd om het lek te verhelpen. Bron: https://nvd.nist.gov/vuln/detail/CVE-2026-133968

**De Verenigde Staten plaatsten dochterondernemingen van Megaspeed en een Singaporees bedrijf in handen van Alibaba op de Entity List.** De beperking blokkeert de aankoop van geavanceerde chips terwijl autoriteiten vermeende omleidingen van Nvidia-chips naar China onderzoeken; Megaspeed ontkent die te hebben geleverd. Bron: https://www.bloomberg.com/news/articles/2026-11-24/us-blacklists-alibaba-owned-company-in-setback-to-ai-ambitions

**Oregon en Virginia klaagden bedrijven gelieerd aan Elon Musk aan om geseksualiseerde Grok-beelden.** De staten stellen dat veiligheidsmaatregelen beelden van echte mensen, onder wie kinderen, niet wisten tegen te houden, terwijl X zegt dat elke uitvoer wordt gescreend; de briefing had geen toegang tot de processtukken, zodat de geëiste maatregelen onbevestigd blijven. Bron: https://arstechnica.com/tech-policy/2026/11/states-sue-spacex-to-stop-grok-from-generating-child-sex-images-revenge-porn/

## Zakelijk in het kort

Amazon kocht de chipoptimalisatiesoftware en het team van Decart voor naar verluidt 7,5 miljard dollar; de bedrijven maakten geen benchmark voor de software bekend. Bron: https://www.theregister.com/ai-and-ml/2026/11/23/amazon-scoops-up-ai-accelerator-tech-to-keep-chips-busy-at-all-times/5311754

De bestuurders van de University of Michigan keurden met zeven stemmen tegen één een datacenter van 1,25 miljard dollar met Los Alamos goed, terwijl de lokale gemeente vasthoudt aan een moratorium van zes maanden op nieuwe elektriciteitsinfrastructuur. Bron: https://www.404media.co/ypsilanti-michigan-data-center-vote/

## Om in de gaten te houden

Anthropic zet Claude Opus 4.5 op 22 januari 2027 stop. De hersteldeadline van CISA voor MONAI Label is 26 november, en op 15 december staat een technisch webinar over Shirudo gepland.
