+++
title = "Georgia Tech-team verlengt het volgen van modelverwijzingen"
slug = "georgia-tech-team-verlengt-het-volgen-van-modelverwijzingen"
description = "Een kleine getrainde ingreep verbetert Qwen3-8B sterk op synthetische verwijzingsketens. De preprint herleidt de verandering tot de manier waarop middelste lagen informatie tussen regels doorgeven."
tags = ["research", "models"]
date = 2026-10-04T09:25:37+02:00
draft = false
+++

Een team van het Georgia Institute of Technology meldt dat een zeer kleine getrainde ingreep Qwen3-8B veel langere ketens van variabeleverwijzingen laat volgen, terwijl de oorspronkelijke modelgewichten vastgezet blijven.

Zehao Jin, Ruixuan Deng en Junran Wang testen prompts met toewijzingen, zoals een variabele die naar een andere variabele verwijst, die uiteindelijk naar een woord verwijst. Het model moet dat woord terugvinden door de keten te volgen.

Voor een onderzoeker die een model aanpast, isoleert het resultaat een nuttige vraag: weerspiegelen zwakke prestaties ontbrekende berekeningen of het niet gebruiken van berekeningen die al in het netwerk beschikbaar zijn? In deze gecontroleerde taak maakt een verandering in de manier waarop een vroege laag informatie aan latere lagen aanbiedt een groot verschil.

De preprint van het team, ingediend op 29 september, meldt dat Qwen3-8B bij ketens met 24 toewijzingen van ongeveer één correct antwoord op zes naar bijna uitsluitend correcte antwoorden gaat. De vergelijking gebruikt nauwkeurigheid van exacte antwoorden op synthetische programma's; de ingreep is specifiek voor deze taak getraind.

De toegevoegde component is een low-rank adaptation met rang acht, of LoRA, toegepast op de verborgen toestand van het model in één laag. Alleen de kleine matrices van de aanpassing en een schaalfactor worden getraind. Vastgezette aandacht en andere modellagen blijven informatie tussen posities verplaatsen.

De taak scheidt het volgen van verwijzingen van het ophalen van feiten. De eerste toewijzingen bevatten zelfstandige naamwoorden van één token, latere toewijzingen verwijzen naar eerdere variabelen, en de prompt eindigt met een vraag naar de waarde van één variabele. Variabelenamen, zelfstandige naamwoorden en de bevraagde keten worden willekeurig gekozen.

Het artikel onderscheidt ook kiezen uit de beginwaarden van het als eerste rangschikken van het exacte antwoord over het volledige vocabulaire. De belangrijkste Qwen-verbetering gebruikt de moeilijkere maat voor exacte antwoorden. Dat is relevant omdat verschillende andere experimenten een keuzescore gebruiken; die scores beschrijven andere tests.

## De ingreep start een estafette door bestaande lagen

De auteurs volgen hoe elke regel informatie krijgt over de keten waartoe hij behoort. In het ongewijzigde model stopt dat proces na enkele regels; latere berekeningen kunnen een waarde kopiëren zonder de keten ver genoeg uit te breiden.

Na aanpassing verzamelt een regel informatie uit eerdere regels en geeft die verder door via een kort interval van middelste lagen. De auteurs noemen dit een estafette. Aandacht voor de bovenliggende regel blokkeren verstoort het proces en levert interventiebewijs voor het voorgestelde mechanisme.

Plaatsing is van belang. Dezelfde aanpassing voorbij een modelspecifieke grens verplaatsen neemt veel van het voordeel weg, omdat de nuttige berekeningen in de middelste lagen niet meer op de ingreep volgen. Een meting op vastgezette modellen schat die grens met bescheiden precisie in apart gehouden tests.

De auteurs onderzoeken ook modellen die lagen in lussen herhalen. In die omstandigheden maakt de aanpassing extra lussen nuttig over een aanzienlijk bereik, al keren de verbeteringen in sommige experimenten uiteindelijk om. De resultaten met de langste verwijzingsketens gebruiken een specifieke regelvolgorde en passen de aanpassing in elke lus toe.

Een afzonderlijk vraag-antwoordexperiment biedt bewijs over de plaatsing van de aanpassing, maar het artikel stelt niet vast dat dezelfde estafette daar de verbetering verklaart. De hoofdopzet levert de relevante alinea's aan, en de aanpassingen worden voor elke taakindeling getraind.

Het centrale resultaat blijft scherp begrensd: een kleine verandering kan het volgen van verwijzingen binnen deze modellen verlengen. Effecten op algemeen modelgedrag en betrouwbaarheid bij uitrol vereisen afzonderlijke evaluatie. Het team biedt code en een interactieve demonstratie van de verwijzingsketentaak.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
| --- | --- | --- | --- |
| Auteurs Jin, Deng en Wang bij het Georgia Institute of Technology; preprint van 29 september | GEVERIFIEERD | [Bron](https://arxiv.org/abs/2609.36585) | geen |
| Exacte Qwen3-8B-nauwkeurigheid op ketens van 24 regels: van 15,5 procent naar 99 procent; oorspronkelijke gewichten vastgezet; taakgetrainde ingreep met rang 8 en 65.537 toegevoegde parameters | VOLGENS HET BEDRIJF | [Bron](https://arxiv.org/abs/2609.36585) | geen; synthetische taaktest van de auteurs |
| Willekeurige verwijzingsketens; exacte nauwkeurigheid tegenover keuzenauwkeurigheid; aanpassing van laaginvoer en vastgezette communicatiecomponenten | VOLGENS HET BEDRIJF | [Bron](https://arxiv.org/abs/2609.36585) | geen; taak- en methodesecties |
| Estafette in de middelste lagen; ingreep in aandacht voor de bovenliggende regel; late plaatsing verliest voordeel; schatting van plaatsing op apart gehouden gegevens heeft bescheiden precisie | VOLGENS HET BEDRIJF | [Bron](https://arxiv.org/abs/2609.36585) | geen; causale tests begrenzen het algoritme, maar identificeren het niet uniek |
| Verbeteringen en uiteindelijke omkering in modellen met lussen; langste tests gebruiken niveauvolgorde en aanpassing in elke lus; taakspecifieke vraag-antwoordtests met juiste referentiealinea's | VOLGENS HET BEDRIJF | [Bron](https://arxiv.org/abs/2609.36585) | geen; resultaten en beperkingen |
| Een kleine ingreep maakt anders ongebruikte berekeningen voor verwijzingsvolging zichtbaar in de geteste opzet | ANALYSE | [Bron](https://arxiv.org/abs/2609.36585) | gevolgtrekking uit vergelijking met vastgezette gewichten, beperkt tot geteste taken |
| Algemeen gedrag en betrouwbaarheid bij uitrol buiten de aangetoonde reikwijdte; openbare code en interactieve demo | GEVERIFIEERD | [Bron](https://arxiv.org/abs/2609.36585) | geen; vermelde beperkingen en links naar bestanden |
