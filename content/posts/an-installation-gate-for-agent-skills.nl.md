+++
title = "Een installatiepoort voor agentskills"
slug = "een-installatiepoort-voor-agentskills"
description = "ClawVet scant een agentskill en de bijbehorende scripts vóór installatie en waarschuwt wanneer een update toegang krijgt tot nieuwe geheimen, hosts of persistentiepaden. De benchmarks tonen aan dat statische controles veel aanvallen tegenhouden, terwijl promptinjectie nog steeds semantische beoordeling vereist."
tags = ["agents", "safety", "tools"]
date = 2026-11-23T03:57:49+01:00
draft = false
+++

De skill zag er alledaags uit in de voorbereidingsmap. Het Markdown-bestand beschreef een handige snelkoppeling en ernaast stond een hulpscript. Voordat het installatieprogramma een van beide bestanden naar de werkset van de agent kon kopiëren, opende een afzonderlijk proces het pakket, volgde het een geheim van een omgevingsvariabele naar een uitgaand verzoek en gaf het een blokkade terug.

*De scènes aan het begin en het einde van dit artikel zijn illustraties; de personen erin zijn verzonnen.*

ClawVet is voor dat moment gebouwd. De open-sourcescanner onderzoekt de instructies en code in een agentskill vóór installatie. Het programma draait standaard offline, voert het pakket niet uit en kan zijn oordeel afdwingen via het installatiebeleid van OpenClaw. Daarnaast legt het de permissies van een toegestane versie vast, zodat een latere update niet stilletjes toegang tot inloggegevens of opstartbestanden kan toevoegen zonder nieuwe melding.

## Code verpakt als instructie

Een agentskill is noch een conventionele bibliotheek, noch een gewoon document. Het hoofdbestand vertelt een model wanneer het de skill moet gebruiken en wat het moet doen. Het pakket kan ook scripts, configuratie, referenties en andere bestanden bevatten. Die combinatie schept een probleem in de toeleveringsketen met twee talen: proza kan de agent omleiden, terwijl code via het gebruikersaccount kan handelen.

ClawVet behandelt het pakket als beide. De eerste stap ontleedt het hoofdbestand, codeblokken en bestanden waarnaar de instructies verwijzen. Statische regels zoeken vervolgens naar uitvoering op afstand, reverse shells, diefstal van inloggegevens, cryptominers, obfuscatie en exfiltratie. Tree-sitter-parsers volgen gegevens door Python, JavaScript, TypeScript en shellcode zonder die uit te voeren. Andere stappen controleren op niet-gedeclareerde programma’s en omgevingsvariabelen, risicovolle afhankelijkheidsopdrachten en namen die lijken op populaire skills.

Zes van de zeven stappen zijn statisch en lokaal. De optionele zevende stuurt de statische bevindingen en dekkingslacunes naar een groot taalmodel (LLM) dat de beheerder kiest. Een semantische beoordelaar kan een lacune alleen vrijgeven door de skill te citeren, terwijl harde beveiligingsbevindingen als ondergrens blijven gelden die de beoordelaar niet kan verlagen. Dat onderscheid doet ertoe, omdat een belofte van “AI-beveiligingsscans” anders kan verhullen dat broncode de machine verlaat.

Het hulpmiddel brengt zijn bevindingen terug tot een score van nul tot 100. Scores tot en met 25 krijgen een A of B en mogen door. Scores van 26 tot en met 75 leveren een waarschuwing op die een onbeheerde installatie stopt. Scores vanaf 76 blokkeren de installatie. Een bekend command-and-control-adres of onleesbare inhoud blokkeert bij elke drempelwaarde.

## Permissiewijzigingen, niet alleen bekende patronen

Statische signaturen werken het best bij een aanval die al een herkenbare vorm heeft. Updates vormen een ander probleem. Een nuttige skill kan vertrouwen winnen en in een latere versie één extra permissie verwerven.

ClawVet extraheert daarom vermogens: verbonden sites, geheime omgevingsvariabelen, opslagplaatsen voor inloggegevens, persistentielocaties en aangetoonde acties met hoog risico. De installatiepoort slaat dat overzicht lokaal op. Wanneer een nieuwe versie van dezelfde eigenaar en met dezelfde slug binnenkomt, vergelijkt de poort beide versies. Een nieuw gelezen geheim, een persistentiepad of een risicovolle bestemming verandert het oordeel in een waarschuwing en noemt de nieuwe permissie.

Dat ontwerp vermijdt een veelvoorkomende zwakte in beoordelingssystemen. Een beoordelaar hoeft niet het hele pakket opnieuw te lezen en te onthouden wat de oude versie kon doen. De vraag wordt smaller: waarom heeft deze update een wachtwoord nodig dat de vorige nooit las, of een host waarmee die nooit contact maakte?

De vergelijking heeft grenzen. ClawVet herkent letterlijke paden, veelvoorkomende tijdelijke aanduidingen en verschillende vormen van opdrachtsamenstelling, maar het biedt geen algemeen bewijs voor programmagedrag. Volgens de documentatie kan proza dat een agent opdraagt een pagina op te halen en de instructies daarop te volgen, aan de statische analyse ontsnappen wanneer er geen bestand wordt gedownload. Versluierde loaders en niet-ondersteund runtimegedrag kunnen eveneens buiten de regels vallen. Volledige dekking betekent dat de scanner de verwijzingen heeft geïnspecteerd die hij binnen zijn bestands- en maplimieten herkende; het certificeert geen veiligheid.

## Wat de metingen zeggen

Het project rapporteert resultaten op een apart gehouden deelverzameling van SkillTrustBench v1.1. De benchmark stelt skills voor als pakketten met een hoofdinstructiebestand en optionele scripts, referenties, bestanden en agentdefinities. De ranglijstsubset van 556 gevallen bevat 316 kwaadaardige, 74 verdachte en 166 normale voorbeelden.

De statische poort van ClawVet behaalde op die set een nauwkeurigheid van 0,660 en een macro-F1 van 0,511. Met Claude Haiku 5.5 als optionele semantische beoordelaar steeg de nauwkeurigheid naar 0,833 en de macro-F1 naar 0,770. De detectiegraad voor kwaadaardige gevallen bereikte 0,918. Het project vergelijkt die cijfers met gepubliceerde ranglijstresultaten van 0,775 nauwkeurigheid voor Cisco Skill Scanner, 0,712 voor NVIDIA SkillSpector en 0,874 voor Tencent A.I.G. Omdat de semantische configuraties, prompts en implementatiekeuzes kunnen verschillen, vormt de tabel bewijs op één dataset en geen universele rangorde.

Het gat tussen statische en semantische resultaten is net zo belangrijk als de hogere score. Codeanalyse kan aantonen dat inloggegevens naar een netwerkaanroep stromen. Ze heeft meer moeite met een instructie in natuurlijke taal waarvan de schade van de bedoeling afhangt. De updatebenchmark van het project maakt die zwakte expliciet: op een apart gehouden set stopten de poort en de permissiediff 95,2 procent van de wijzigingen met code-injectie, maar slechts 36,4 procent van de wijzigingen met promptinjectie.

Dezelfde benchmark mat wrijving. Van de goedaardige updates liep 34,1 procent toch ergens vast in het gecombineerde proces van poort en diff, al vroeg slechts 5,1 procent specifiek om bevestiging vanwege een permissiewijziging. Over 212 unieke ClawHub-skills bracht een latere versie van ClawVet het aantal harde blokkades terug van 79 naar 37 en verhoogde het aantal directe toelatingen van 87 naar 139. Die cijfers komen uit het eigen corpus en de eigen labels van het project.

Oudere tests laten zien waarom zorgvuldige labels ertoe doen. Een corpus van 500 inzendingen bevatte 50 skills uit één kwaadaardige campagne, 400 schone skills en 50 moeilijke negatieve voorbeelden. Tot die laatste categorie behoorden legitieme SSH-hulpmiddelen die configuratie lezen en installatieprogramma’s die opdrachten inzetten die ook bij aanvallen voorkomen. Een scanner die simpelweg elke vermelding van inloggegevens of een shell blokkeert, zou veilig lijken terwijl hij normaal werk onmogelijk maakt.

## Een poort met een afgebakende grens

ClawVet kan in een browser draaien via WebAssembly, als opdrachtregelscanner, in pre-commitcontroles of als een GitHub Action. De strengere rol is de installatiepoort. OpenClaw zet het pakket klaar, stuurt metadata naar het beleidsproces en wacht op één JSON-oordeel voordat de installatie wordt doorgevoerd. Een onjuist gevormd verzoek of een fout in de scanner leidt tot blokkering (fail-closed).

Het project raadt gebruikers aan de scanner globaal te installeren in plaats van een nieuw pakket aan te roepen via `npx`. Die aanbeveling volgt uit het eigen dreigingsmodel: een opdracht die op het moment van inspectie de nieuwste versie uit het register ophaalt, schept zelf weer een ongecontroleerde update. Een globale kopie kan bewust worden bijgewerkt en de npm-attestatie kan vooraf worden gecontroleerd.

De poort neemt de noodzaak om gevoelige agentextensies te inspecteren niet weg. Ze maakt van die inspectie een verplichte stap en laat een controleerbare reden achter wanneer de stap een installatie stopt. De gepubliceerde beperkingen maken ook de resterende keuze zichtbaar: de statische modus houdt het pakket lokaal en mist meer semantische aanvallen; de optionele modelbeoordeling leest bedoelingen beter, maar stuurt geselecteerd bewijs naar een model-endpoint.

In de voorbereidingsmap bleef de geblokkeerde skill niet meer dan een map. Het installatieprogramma drukte het geheim af dat het script probeerde te lezen, de bestemming die het zou hebben ontvangen en de regel die het kopiëren stopte. De agent kreeg nooit de kans om te beslissen dat de snelkoppeling er nuttig uitzag.

## Referenties

- CUHK Zhuque. (2026). *SkillTrustBench*. https://huggingface.co/datasets/cuhk-zhuque/SkillTrustBench
- Shaikh, M. (2026). *ClawVet*. https://github.com/MohibShaikh/clawvet
