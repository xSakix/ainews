+++
title = "Modellen kennen tijd, maar misrekenen hun eigen uitvoeringstijd"
slug = "modellen-kennen-tijd-misrekenen-eigen-uitvoeringstijd"
description = "Taalmodellen beantwoordden tot 97,5 procent van de vragen over tijdsregels goed en onderschatten vervolgens hun eigen voltooiingstijden met maximaal 99,5 procent. Een nieuwe studie toont waarom agents die over planningen kunnen redeneren toch slechte beslissingen kunnen nemen over wachten, kosten en coördinatie."
tags = ["research", "agents", "models"]
date = 2026-11-12T04:18:00+01:00
draft = false
+++

Een ingenieur vraagt een agent een uitgevallen dienst te onderzoeken en te melden hoe lang het werk zal duren. De agent leest de logs, somt de stappen op en belooft binnen tien minuten een antwoord. Hij is binnen enkele seconden klaar. Later krijgt dezelfde agent een iets nauwkeuriger tool aangeboden waarvoor hij langer moet wachten. Hij wijst de tool af omdat hij die wachttijd behandelt alsof die nauwelijks bestaat. Deze ingenieur is verzonnen, maar de twee fouten weerspiegelen metingen uit een nieuwe studie naar hoe taalmodellen met tijd omgaan.

## Regels zonder klok

Ryan Liu en vijf collega's van Princeton, Columbia, UC Berkeley en UCLA onderzochten tijdsvaardigheid als een keten met vier schakels: kennis van tijd, schattingen van duur, mensachtige vertekeningen en beslissingen die tijd tegen nauwkeurigheid afwegen. Hun preprint, ingediend op 7 november, onderzoekt Claude Opus 5, GPT-5.6 Sol en Gemini 3.7 Flash. De vraag is of modellen wat ze over tijd hebben gelezen kunnen toepassen op een dimensie die ze niet rechtstreeks ervaren.

Dat onderscheid is belangrijk omdat een taalmodel het interval tussen twee aanroepen niet doorleeft. Een tijdstempel kan in zijn context staan, maar het model voelt geen minuten verstrijken. Zelfs een autonoom systeem wordt meestal actief door een extern tijdschema of een gebeurtenis. De onderzoekers beschrijven tijd voor een model als informatie uit de tweede hand: aanwezig in tekst en metadata, afwezig als voortdurende ervaring.

Het eerste experiment gaf de modellen een eerlijke kans om hun kennis te tonen. Het team haalde vijf axioma's uit onderzoek naar leren, verlies van vaardigheden, wisselen tussen taken, vermoeidheid en herstel. Daaruit leidde het principes af, zoals de kosten van onderbrekingen en het voordeel van verwant werk bundelen. De test gebruikte werkscenario's in plaats van feitenvragen. Een model moest beoordelen of een gewijzigde volgorde een taak langer of korter zou maken.

De resultaten waren sterk. Claude scoorde 92,0 procent over de axioma's en afgeleide stellingen, GPT 97,5 procent en Gemini 96,3 procent. Hun antwoorden bleven ook samenhangend wanneer de onderzoekers de vergelijkingen omkeerden. De fouten waren meestal stabiele overtuigingen in plaats van willekeurige gissingen.

Dit deel bouwt voort op een lange onderzoekslijn over formeel redeneren over tijd. Het intervalraamwerk van James Allen uit 1983 gaf kunstmatige intelligentie een manier om relaties weer te geven, zoals een gebeurtenis die vóór, tijdens of na een andere plaatsvindt. De nieuwe studie stelt een andere vraag. Een model kan die relaties kennen en toch geen betrouwbare inschatting hebben van hoe lang zijn eigen werk duurt.

## Schattingen los van de uitvoering

Voor het tweede experiment gebruikten de onderzoekers software- en onderzoekstaken uit de benchmark Human-Calibrated Autonomy Software Tasks. HCAST bevat menselijke referentiemetingen van geschoolde werknemers onder omstandigheden die met agentuitvoeringen te vergelijken zijn. Verwant werk van Thomas Kwa en collega's gebruikt die tijdsduren om agentcapaciteit uit te drukken als een tijdshorizon voor taakvoltooiing.

De modellen zagen de volledige taakinstructies en een beschrijving van de uitvoerder. Ze schatten een voltooiingstijd en gaven onzekerheidsintervallen. De onderzoekers vergeleken die schattingen vervolgens met vastgelegde tijdsduren voor mensen en agents. Een aparte test gebruikte 500 verzoeken uit de WildChat-dataset. Elk model voorspelde hoe lang het antwoord zou kosten en antwoordde vervolgens terwijl het systeem de werkelijke uitvoeringstijd registreerde. Vijf herhalingen per model en verzoek leverden 7.500 proeven op.

Het centrale probleem was zelfkalibratie. Modellen onderschatten hun eigen voltooiingstijden met maximaal 99,5 procent en konden niet betrouwbaar bepalen welke taken hen langer zouden kosten. Het probleem was niet alleen dat ze menselijke eenheden voor machinewerk gebruikten. Ze faalden ook bij relatieve rangschikking, die een planningssysteem nodig heeft zelfs wanneer het exacte aantal seconden niet van belang is.

Schattingen van menselijke tijdsduur waren beter, maar legden een andere zwakte bloot. De formulering van een gebeurtenis veranderde het oordeel van het model over hoe lang die zou aanvoelen. De modellen reproduceerden een bekend menselijk framingeffect en versterkten het met maximaal een factor 1,3.

Dat resultaat verbindt modelgedrag met de planningsfout die Roger Buehler, Dale Griffin en Michael Ross onderzochten. Mensen voorspellen vaak dat ze eerder klaar zijn dan eerdere ervaring rechtvaardigt, vooral wanneer ze zich richten op een plan voor de huidige taak in plaats van vergelijkbare uitkomsten. Modellen kunnen beschrijvingen van die vertekening uit tekst leren. Het nieuwe artikel laat zien dat kennis van een vertekening geen weerstand ertegen garandeert.

## Wachten telde nauwelijks mee

Het laatste experiment ging van schattingen naar beslissingen. De onderzoekers boden keuzes aan waarbij een langere wachttijd meer nauwkeurigheid opleverde. Door in sommige omstandigheden de tijdsduur te geven, konden ze een slechte schatting scheiden van een zwakke voorkeur voor tijdwinst.

Sommige modellen behandelden grote veranderingen in vertraging als vrijwel irrelevant. Ze konden bij het beantwoorden van een gebruiker een 1.200-voudige toename van de wachttijd negeren. Die fout bleef bestaan wanneer de duur expliciet was vermeld, zodat schatten alleen geen verklaring bood. Het beslisbeleid zelf waardeerde tijd niet consistent.

Het artikel beweert niet dat alle modellen op elke tijdstaak falen. Het eerste experiment toont het tegendeel. Het stelt evenmin één interne oorzaak vast. De evaluatie omvat drie modelfamilies en specifieke taakopzetten en de auteurs beschrijven tijdsvaardigheid via waarneembare antwoorden, niet via een directe meting van subjectieve ervaring.

Het praktische risico is beperkter en gemakkelijker te zien. Een agent kan kiezen tussen tools met verschillende latenties, werk verdelen over andere agents, een rekening schatten die van de uitvoeringstijd afhangt of iemand vertellen wanneer die moet terugkomen. Een systeem dat de regel voor taken bundelen kent, kan zijn wachtrij toch verkeerd ordenen. Een systeem dat de kosten van onderbreking uitlegt, kan toch een onmogelijke deadline beloven.

Tijdschattingen moeten daarom worden behandeld als voorspellingen die externe kalibratie nodig hebben. Een host kan werkelijke tijdsduren registreren, taakspecifieke verdelingen bijhouden en deadlines buiten het model toepassen. Hij kan ook wachtkosten expliciet tonen en testen of een keuze verandert wanneer die kosten groeien. Deze controles lijken op de bredere les uit agentveiligheid: plaats meetbare toestand en handhaving in het systeem rond het model in plaats van te vertrouwen op een juiste uitleg in lopende tekst.

Enkele weken later bij de verzonnen ingenieur schrijft de agent nog steeds een zelfverzekerde schatting, maar de interface zet die naast de mediane uitvoeringstijd van vergelijkbare opdrachten en een breed onzekerheidsbereik. De planner, niet het model, beslist wanneer te stoppen of te wachten. De verzonnen ingenieur heeft de agent geen tijdsbesef gegeven. Het systeem doet niet meer alsof vloeiend over klokken praten hetzelfde is als er een bijhouden.

## Referenties

- Allen, J. F. (1983). *Maintaining Knowledge about Temporal Intervals*. https://doi.org/10.1145/182.358434
- Buehler, R., Griffin, D., & Ross, M. (1994). *Exploring the “Planning Fallacy”: Why People Underestimate Their Task Completion Times*. https://doi.org/10.1037/0022-3514.67.3.366
- Kwa, T., et al. (2025). *Measuring AI Ability to Complete Long Software Tasks*. https://arxiv.org/abs/2503.14499
- Liu, R., Lee, D., Ai, I. S., Abdulhai, M., Dubey, R., & Griffiths, T. L. (2026). *In Search of Lost Time: Temporal Competence in Large Language Models*. https://arxiv.org/abs/2611.10536
- Rein, D., et al. (2025). *HCAST: Human-Calibrated Autonomy Software Tasks*. https://arxiv.org/abs/2503.17354
