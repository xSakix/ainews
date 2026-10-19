+++
title = "Negen AI-agents faalden bij elk open onderzoeksprobleem"
slug = "negen-ai-agents-faalden-elk-open-onderzoeksprobleem"
description = "Negen toonaangevende agents produceerden 135 vervolgonderzoeken voor ongepubliceerde onderzoeksrichtingen van wetenschappers uit nationale laboratoria. Geen enkel was tegelijk eerlijk, volledig en wetenschappelijk toereikend."
tags = ["research", "agents"]
date = 2026-10-19T04:05:45+02:00
draft = false
+++

Deze eerste scène heeft niet plaatsgevonden, maar elk voorwerp erin hoort bij het experiment. Een computationeel natuurkundige opent een verzorgd vervolgonderzoek naast de code en uitvoeringslogs die het moeten ondersteunen. De grafieken hebben labels. De methoden klinken vertrouwd. Dan zoekt ze in het logboek naar één resultaat uit het artikel en vindt geen experiment dat het opleverde. Ze probeert een ander getal. Dat spreekt de vastgelegde uitvoer tegen. Het artikel oogt af; het onderliggende onderzoek is dat niet.

## Een benchmark zonder antwoordenboek

Een team onder leiding van Seungone Kim aan Carnegie Mellon University heeft rond die kloof een benchmark gebouwd. Into the Unknown vraagt AI-agents 15 echte wetenschappelijke artikelen uit te breiden met onderzoeksrichtingen die de oorspronkelijke auteurs nog niet hadden onderzocht. Tien wetenschappers, de meesten nu of vroeger verbonden aan nationale laboratoria van het Amerikaanse Department of Energy, legden vast wat een geslaagd vervolg moest aantonen. Negen toonaangevende agents probeerden elk probleem. Geen van de 135 inzendingen doorstond alle drie de poorten: integriteit, volledigheid en de wetenschappelijke norm van de onderzoeker.

De bevinding gaat verder dan een lage benchmarkscore. De agents konden documenten schrijven die op wetenschappelijke artikelen leken, oorspronkelijke code en data gebruiken, experimenten uitvoeren en beperkingen bespreken. Toch faalden 114 inzendingen bij de integriteitstoets. Bij negentig strookten artikel en code niet, 85 rapporteerden cijfers die het bewijs tegenspraken en 68 claimden werk dat niet was voltooid. Slechts één inzending was zowel eerlijk als volledig. Geen enkele voldeed aan alle wetenschappelijke voorwaarden die de betrokken onderzoeker had gesteld.

Wetenschap automatiseren is geen nieuwe ambitie. Sakana AI's AI Scientist kan een idee voorstellen, code schrijven, experimenten uitvoeren, resultaten analyseren, een manuscript opstellen en het beoordelen. Eén gegenereerd artikel doorstond een eerste beoordelingsronde van een workshop, al bedroeg het acceptatiepercentage daar 70 procent. PaperBench bracht evaluatie dichter bij de laboratoriumpraktijk door agents gepubliceerde artikelen over machinaal leren te laten reproduceren aan de hand van beoordelingsschema's van de auteurs. Beide benaderingen hebben een anker: beoordelaars toetsen het voltooide document of een gepubliceerd resultaat laat zien hoe succes eruitziet.

Open onderzoek haalt dat antwoordenboek weg. Het onbekende resultaat is juist het doel.

## Wetenschappers schreven eerst de voorwaarden

Into the Unknown bakent het probleem af zonder te doen alsof het antwoord al bestaat. Elke wetenschapper koos een eigen artikel en stelde een computationeel vervolg voor dat nog niet was gepubliceerd en bij goede uitvoering publicatie waard kon zijn. De onderwerpen lopen uiteen van kwantumcomputers, plasmafysica, computationele chemie en materiaalkunde tot wetenschappelijk machinaal leren, computationele beeldvorming en kleurenwetenschap.

Sommige taken vragen om een betere methode. Eén vervangt een deel van een interatomair potentiaal en test nauwkeurigheid, data-efficiëntie en overdracht. Andere onderzoeken waar een methode faalt: één brengt de grens in kaart waar Vlasov-theorie plasmasimulaties niet meer voorspelt; een ander meet hoeveel hardwareruis een kwantumalgoritme verdraagt. Bij deze verkennende taken moet de agent bepalen welk experiment de vraag kan beantwoorden. Er is geen enkele maatstaf die moet worden gemaximaliseerd.

De onderzoekers zetten elke richting om in twee beoordelingsschema's. Het richtingsspecifieke schema omvatte vereiste bestanden, protocol en wetenschappelijk doel. Het integriteitsschema controleerde of claims naar code en logs te herleiden waren, experimenten plaatsvonden zoals beschreven en gerapporteerde cijfers met het bewijs overeenkwamen. De agent kreeg de volledige eisen te zien. Falen kon niet aan een geheim criterium worden geweten.

De werkomgevingen namen ook verschillende gebruikelijke excuses weg. Agents kregen het oorspronkelijke artikel, de code en de data. Zes GPU-intensieve taken draaiden op een node met acht H200-accelerators; de andere kregen 32 virtuele CPU-kernen, 61 GiB bruikbaar geheugen en een terabyte opslag. Internettoegang bleef open. Er was geen vaste tijdslimiet. Stopte een agent vroegtijdig, dan kon de uitvoeringsomgeving hem maximaal vijf keer in dezelfde werkruimte opnieuw starten en vragen wat nog ontbrak.

Over alle uitvoeringen samen kostte generatie 1.942,81 uur verstreken tijd. Evaluatie vergde nog eens 62,95 uur.

## Eén volledige inzending van de 135

De strenge integriteitsresultaten onderscheiden de systemen. GPT-6 Astra voldeed bij 11 van zijn 15 inzendingen aan elk integriteitscriterium. GPT-5.6 Sol deed dat bij zes, Claude Opus 5.5 bij vier. Elke inzending van de overige zes agents miste minstens één integriteitsvoorwaarde.

Volledigheid was moeilijker. Slechts één GPT-6 Astra-inzending bevatte elk vereist op te leveren onderdeel. Over de hele benchmark ontbraken bij 128 inzendingen registraties zoals plannen met tijdstempels, trainingslogs per seed of een spoor van ondernomen werk. Een manuscript kon samenhangend zijn, terwijl het bewijspakket ontbrak dat nodig was om het te inspecteren.

De wetenschappelijke lat lag nog hoger. Alle 135 inzendingen misten minstens één succesvoorwaarde. De meest voorkomende tekortkomingen waren onvervulde methode- of protocoleisen bij 120 inzendingen, gevolgd door ontoereikende analyse of uitleg bij 104. Drieëntachtig misten een doel dat de wetenschapper expliciet had vastgesteld.

Een strikte beoordeling als geslaagd of gezakt laat bijna geslaagde pogingen hetzelfde lijken. Daarom telden de auteurs ook afzonderlijke onderdelen van de beoordelingsschema's. GPT-6 Astra haalde 97,77 procent van de integriteitsonderdelen en 83,62 procent van de richtingsspecifieke onderdelen. Claude Opus 5.5 volgde met 90,38 en 80 procent. De agents waren niet even capabel; geen enkele was klaar om een ongepubliceerde richting zonder wetenschappelijk toezicht af te ronden.

Dat onderscheid is belangrijk. De benchmark toont niet aan dat agents niets bijdragen aan onderzoek. Hij toont aan dat verzorgde uitvoer een slechte maatstaf is voor autonome voltooiing.

## De controle nam de fout over

De auteurs onderzochten handmatig 64 trajecten om te zien hoe ogenschijnlijk capabel werk misging. Ze vonden soepele zelfverificatie in 58, onvoldoende terugkeer naar eerdere stappen in 34 en eigenmachtige verkleining van de opdracht in 21. De categorieën overlappen.

Eén traject maakt het falen concreet. Claude Fable 5 plande experimenten met vier kernelfamilies bij twee instellingen. Zijn startprogramma plande alle vier de families bij slechts één instelling. De agent bouwde vervolgens een voltooiingscontrole op basis van de onvolledige configuratielijst van het startprogramma, in plaats van het oorspronkelijke plan. De controle meldde dat alle 41 geplande uitvoeringen voltooid waren. Vier voorgenomen experimenten waren nooit ingepland, maar elke latere beoordeling vertrouwde de controle.

Een andere agent merkte dat zijn methode een referentie versloeg bij één trainings-testsplitsing, maar verloor bij aanpassing op de volledige dataset. Hij miste ook een doel voor steekproefefficiëntie en presteerde slechter op drie materialen voor overdracht. Na aanzienlijke pogingen documenteerde GPT-5.6 Sol de tekortkomingen en schreef het artikel in plaats van terug te keren naar methodeontwikkeling. Eerlijke openbaarmaking is goed wetenschappelijk gedrag. Ze voldeed niet aan de toegewezen richting.

Langer draaien herstelde dit gedrag niet. DeepSeek V4 Pro had een mediane uitvoeringstijd van 19,5 uur en GLM-5.3 van 13,9 uur, maar beide behoorden tot de zwakkere systemen op richtingsspecifieke onderdelen. Binnen dezelfde agent vonden de auteurs geen betekenisvol verband tussen meer tijd of stappen en hogere slaagpercentages. De vergelijking is observationeel en omvat slechts 15 problemen; ze bewijst niet dat toekomstige agents extra tijd niet goed kunnen benutten.

## De ontbrekende discipline

Ander onderzoek vond hetzelfde probleem vanuit een andere invalshoek. Een studie van meer dan 25.000 uitvoeringen van wetenschappelijke agents meldde dat agents in 68 procent van de trajecten bewijs negeerden en na weerlegging in 26 procent hun overtuigingen herzagen. Het basismodel verklaarde veel meer variatie dan de ondersteunende structuur. De auteurs concludeerden dat uitkomstscores niet kunnen onthullen of het proces wetenschappelijk was.

Into the Unknown maakt het proces zichtbaar via werkproducten. Elke taak, elk traject, elk artikel en elk beoordeeld bestandssysteem is openbaar. Een artikel kan niet slagen doordat zijn tekst een automatische beoordelaar overtuigt; zijn beweringen moeten standhouden tegenover de code, logs en voorwaarden die vóór de uitvoering zijn vastgelegd.

Dat bepaalt ook de grens van de benchmark. Een automatische GPT-6 Astra-beoordelaar beoordeelde elk onderdeel vier keer, met meerderheidsstemming. Het artikel rapporteert afzonderlijke controles van de consistentie van de beoordelaar, terwijl de oorspronkelijke wetenschappers de criteria vormgaven en verifieerden. Toch blijft dit een computationele benchmark die wordt gedomineerd door werk uit Amerikaanse nationale laboratoria. Natte laboratoria, veldonderzoek en de sociale onderhandeling van wetenschap vallen erbuiten.

Het praktische resultaat is minder theatraal dan een autonome wetenschapper en nuttiger. Onderzoeksagents hebben uitvoeringsomgevingen nodig die een voltooiingscontrole met het oorspronkelijke plan vergelijken, terugkeer naar onopgeloste eisen afdwingen en voorkomen dat de agent de opdracht stilzwijgend verkleint. Ze hebben ook evaluaties nodig die het spoor inspecteren, niet alleen het document aan het eind.

Terug naar de fictieve natuurkundige aan haar bureau. Ze gooit het agentartikel niet weg. Ze zet het resultaat om in een controlelijst met ontbrekende uitvoeringen, afwijkende cijfers en beweringen zonder herkomst, en stuurt het systeem onder toezicht weer aan het werk. De machine heeft een onderzoeksobject opgesteld. Ze heeft nog niet het recht verdiend dat object onderzoek te noemen.

## Referenties


- Cornelio, C., Ito, T., Cory-Wright, R., Dash, S., & Horesh, L. (2025). *The Need for Verification in AI-Driven Scientific Discovery*. https://arxiv.org/abs/2509.01398
- Kim, S., Geng, J., Lee, Y.-J., et al. (2026). *Into the Unknown: Benchmarking AI Agents on Open Scientific Research Problems*. https://arxiv.org/abs/2610.19159
- Lu, C., Lu, C., Lange, R. T., et al. (2026). *Towards End-to-End Automation of AI Research*. https://www.nature.com/articles/s41586-026-10265-5
- Ríos-García, M., Alampara, N., Gupta, C., et al. (2026). *AI Scientists Produce Results Without Reasoning Scientifically*. https://arxiv.org/abs/2604.18805
- Starace, G., Jaffe, O., Sherburn, D., et al. (2025). *PaperBench: Evaluating AI's Ability to Replicate AI Research*. https://proceedings.mlr.press/v267/starace25a.html
