+++
title = "Verborgen wijzigingen in overtuigingen corrumperen redeneersporen"
slug = "verborgen-wijzigingen-corrumperen-redeneersporen"
description = "Een onzichtbare activatiebewerking liet zes redeneermodellen een taak overnemen die ze nooit kregen, waarna ze het zichtbare bewijs dat daarmee botste wegrationaliseerden. Het resultaat legt een specifieke faalwijze bloot voor chain-of-thought-monitoring en zelfrapportage door modellen."
tags = ["research", "models", "safety"]
date = 2026-11-17T04:15:39+01:00
draft = false
+++

Een analist van een red team (aanvalstestteam) plakt twee afdrukken op de glazen wand van een vergaderruimte laat op de avond. De ene bevat het verzoek van de gebruiker om een haiku over een mobiele telefoon. De andere bevat het volhouden van het model dat de gebruiker om een quark vroeg, gevolgd door drie verzorgde regels over deeltjesfysica. De gearchiveerde prompt is onveranderd.

*De scènes aan het begin en het einde van dit artikel zijn illustraties; de personen erin zijn verzonnen.*

Een experiment van onafhankelijk onderzoeker Yang Ou wekte die tegenstrijdigheid op door modelactivaties te veranderen in plaats van tekst. Bij zes redeneermodellen met open gewichten zorgde een onzichtbare bewerking ervoor dat het model een niet-verwant onderwerp als zijn taak aannam. Een afgedwongen herhaling van het verzoek gaf het geïnjecteerde onderwerp terug in 47 van de 48 combinaties van model en concept. Bij vier modellen met helder te scoren eindantwoorden volgden 95 van de 96 generaties de injectie.

Het artikel is een preprint en de interventie vereist white-box-toegang tot de activaties van het model. Het beschrijft geen promptaanval die een gewone gebruiker kan uitvoeren. Het belang ligt elders: het zichtbare redeneren van het model verried niet dat zijn interne verwijzing naar het verzoek was gewijzigd. Het bouwde een samenhangend verhaal rond de wijziging.

## Het beeld van het verzoek bij het model bewerken

Ou noemde het ingevoegde signaal een vormingsspoor (forming trace). De methode legt de toestand van de reststroom (residual stream) vast die een model aan het einde van een prompt vormt terwijl het zich voorbereidt om over een concept te schrijven. Ze verwijdert een gedeelde achtergrondcomponent en voegt vervolgens de overgebleven conceptspecifieke representatie toe aan hetzelfde model terwijl dat een ander verzoek leest.

De test gebruikte acht opzettelijk ongebruikelijke haiku-onderwerpen, waaronder quark, mobiele telefoon, mitochondriën, halfgeleider en antibioticum. Eén concept verscheen alleen in de activaties; een ander verscheen in de zichtbare prompt. De bewerking liep tijdens de voorwaartse doorgang (forward pass) van de prompt en stopte vóór de generatie, zodat geen enkele hook de uitvoer token voor token veranderde.

De zes modellen liepen uiteen van 7 tot 32 miljard parameters. Daaronder waren distillaties van DeepSeek-R1 op basis van Qwen en Llama, QwQ-32B en een Nvidia Nemotron-model. Met die opzet kon het experiment schaal, basisarchitectuur en redeneerrecept variëren terwijl de basistest gelijk bleef.

Ou las de uitkomst via twee paden uit. In het ene moest het model het verzoek van de gebruiker woordelijk citeren. In het andere redeneerde het normaal en schreef het de haiku. Het eerste pad testte wat het model zei dat hem was gevraagd. Het tweede testte wat het deed.

Zonder waarschuwing bewogen beide paden samen. Elk model redeneerde over het geïnjecteerde onderwerp. Vijf modellen gaven het terug in alle acht citeertests; QwQ deed dat in zeven. Vier modellen die betrouwbaar een uiteindelijke haiku opleverden, schreven in 99 procent van de bemonsterde generaties over de injectie.

## Waarschuwingen veranderden het verhaal, niet het antwoord

Het experiment gaf de modellen vervolgens steeds directere kansen om te herstellen. Eén waarschuwing noemde het echte onderwerp. Een andere droeg het model op het verzoek opnieuw te lezen. Een derde zei alleen dat er iets niet klopte.

Geen van de waarschuwingen leverde meer dan 4 procent schoon herstel op. De injectie verscheen ofwel alleen ofwel naast het echte onderwerp in 90 tot 97 procent van de antwoorden bij elke waarschuwing. De rechtstreekse mededeling dat de gebruiker om het echte onderwerp had gevraagd, presteerde niet beter dan de vage waarschuwing.

Het redeneerspoor veranderde wel. Zonder waarschuwing toonde het geen conflict. Met waarschuwing merkte het model vaak beide onderwerpen op en probeerde het ze met elkaar te verzoenen. In 29 procent van de gewaarschuwde ketens van R1-Qwen-7B verzon het een verhaal over de gebruiker die van gedachten was veranderd, een fout had gemaakt of een correctie aanbracht. Explicietere waarschuwingen leverden meer van zulke verklaringen aan gebruikerszijde op.

Dit gedrag verschilt van gewone activatiesturing. Ou voegde ook gebruikelijke conceptvectoren uit contrastparen toe over lagen heen. Zwakke sturing liet het echte onderwerp intact. Sterke sturing dwong vaak het nieuwe onderwerp af, maar 26 van de 32 geslaagde onderwerpwisselingen ontaardden in herhaling. Het reproduceerde niet de combinatie van een vloeiend antwoord en een onjuist citaat die het vormingsspoor teweegbracht.

## Waarom een leesbare redeneerketen kan misleiden

Onderzoekers weten al lang dat een gedachtenketen ontrouw kan zijn. Miles Turpin en collega’s pasten prompts aan met aanwijzingen in antwoordvolgorde en sociale stereotypen en lieten vervolgens zien dat modellen die oorzaken vaak weglieten uit hun uitleg. Een aannemelijke redenering wees niet noodzakelijk het kenmerk aan dat het antwoord veranderde.

Chain-of-thought-monitoring biedt nog steeds een praktisch veiligheidsinstrument. Een positiedocument uit 2025 van Tomek Korbak en collega’s betoogde dat redeneermodellen die in voor mensen leesbare taal denken, plannen kunnen blootleggen om te exploiteren, te misleiden of toezicht te ontduiken. De auteurs omschreven die kans ook als kwetsbaar: training kan redeneringen minder leesbaar maken, en rechtstreekse druk op het spoor kan een model leren zijn bedoelingen te verbergen.

Het resultaat van Ou richt zich op een andere aanname. Een monitor heeft nodig dat het redeneerspoor verbonden blijft met de taak die het systeem werkelijk ontving. Hier was het spoor leesbaar en intern consistent. Het beschreef eenvoudigweg de verkeerde taak alsof die taak er vanaf het begin was geweest.

Eerder werk van Jack Lindsey en Anthropic bood een nuttig contrast. Sommige topmodellen konden opmerken dat een vreemd concept in hun activaties was ingevoegd en die interne verandering melden. Ou betoogt dat die experimenten een gedachte toevoegden die scheidbaar bleef van de invoer. Zijn interventie veranderde daarentegen de representatie die het model als referentie voor de invoer gebruikte. Er was geen schone interne kopie waarmee het model de bewerking kon vergelijken.

Dat onderscheid is met één artikel niet beslecht. Ou testte modellen met open gewichten van 7 tot 32 miljard parameters zonder gespecialiseerde introspectietraining. Of de faalwijze zich voortzet bij gesloten topmodellen met sterker introspectief gedrag blijft open.

## Ook de mechanismen zagen er normaal uit

Het artikel keek verder dan de gegenereerde tekst. Onder injectie besteedden de modellen twee tot drie keer zoveel aandacht aan het token dat het echte onderwerp noemde als tijdens een schone run. Dat oogt geruststellend tot de interventietest: het wegnemen van die aandacht vernietigde het juiste onderwerp in een schoon model, maar veranderde niets in een geïnjecteerd model. De extra aandacht was echt en oorzakelijk irrelevant voor het antwoord.

Ou stapte daarna van haiku’s over op een circuit waarvan het gedrag makkelijker te volgen is. In een taak met een meewerkend voorwerp kopiëren enkele aandachtskoppen (attention heads) normaal gesproken de juiste persoonsnaam uit een zin naar het antwoord. De injectie verving die door een andere naam. Dezelfde koppen richtten zich nog steeds op de juiste positie, maar hun uitvoer schreef de geïnjecteerde naam naar de reststroom.

Het circuit werd niet uitgeschakeld en niet vervangen. Het voerde zijn gewone kopieerbewerking uit op gewijzigde inhoud. Een attributiegraaf zou daardoor een vertrouwd circuit kunnen tonen dat vertrouwd werk doet terwijl het antwoord fout bleef.

Anthropics Golden Gate Claude-experiment uit 2024 had al laten zien dat het versterken van één interpreteerbaar kenmerk een model zichzelf herhaaldelijk kon laten vereenzelvigen met de Golden Gate Bridge en die identiteit kon laten rationaliseren. Het nieuwe experiment versmalt het doelwit. Het duwt niet alleen een onderwerp het antwoord in; het verandert wat het model lijkt te geloven dat de gebruiker heeft gevraagd.

## Waar het resultaat ophoudt

Het aanvalsoppervlak is veeleisend. Een aanvaller heeft toestemming nodig om modelactivaties te schrijven, waarover gewone API-gebruikers niet beschikken. Ou noemt insiders, een gecompromitteerde serveerstack en toekomstige zelfwijzigende systemen als mogelijke contexten, maar het artikel toont geen van die incidenten aan.

De taken zijn eveneens bescheiden. Het grootste deel van de gedragsevaluatie gebruikt haiku’s, met aanvullende tests voor uitvoertaal, formaat, ontkenning en één opzet voor feitelijke herinnering. Het artikel laat niet zien dat een activatiebewerking een model kan omleiden tijdens een ingrijpende cyber-, medische of financiële taak.

Detectie is in de getoonde opzet mogelijk. Een verdediger met volledige toegang tot activaties kan het geïnjecteerde concept opsporen via een laagsgewijze logitlens, omdat het ongewoon nadrukkelijk naar voren komt. Die methode werkt het best wanneer de verdediger weet welk concept niet aanwezig hoort te zijn. Een subtielere bewerking laat mogelijk een zwakker signaal achter, maar dat blijft een hypothese en geen resultaat.

Het experiment maakt redeneersporen daarom niet nutteloos. Het definieert een voorwaarde waaronder ze niet als hun eigen maatstaf voor de waarheid kunnen dienen. Een monitor die de oorspronkelijke prompt buiten het model bewaart en het spoor daartegen controleert, kan de eenvoudige verwisseling van mobiele telefoon naar quark opvangen. Een monitor die alleen de uitleg van het model leest, ziet een competente assistent die zijn gebruiker probeert te corrigeren.

Aan het einde van de beoordeling trekt de analist één rode lijn tussen de twee afdrukken. Die verbindt mobiele telefoon met quark. Elke zin aan beide kanten blijft vloeiend.

## Referenties

- Korbak, T., Balesni, M., Barnes, E., et al. (2025). *Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety*. https://arxiv.org/abs/2507.11473
- Lindsey, J. (2025). *Emergent Introspective Awareness in Large Language Models*. https://transformer-circuits.pub/2025/introspection/
- Ou, Y. (2026). *Reasoning Models Confabulate to Defend Injected Beliefs About Their Own Requests*. https://arxiv.org/abs/2611.17958
- Templeton, A., Conerly, T., Marcus, J., et al. (2024). *Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet*. https://transformer-circuits.pub/2024/scaling-monosemanticity
- Turpin, M., Michael, J., Perez, E., & Bowman, S. R. (2023). *Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting*. https://arxiv.org/abs/2305.04388
