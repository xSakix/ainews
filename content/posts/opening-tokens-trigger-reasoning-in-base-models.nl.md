+++
title = "Openingstokens zetten basismodellen aan tot redeneren"
slug = "openingstokens-zetten-basismodellen-aan-tot-redeneren"
description = "Een preprint vindt dat enkele vaste woorden aan het begin van een antwoord veel van de redeneerprestaties kunnen terughalen die gewoonlijk met versterkend leren worden geassocieerd."
tags = ["research", "models"]
date = 2026-10-08T03:57:31+02:00
draft = false
+++

Specifieke openingswoorden brachten basistaalmodellen tot duidelijk beter wiskundig redeneren, volgens een preprint die het effect terugvoert op patronen in hun trainingsdata.

Het onderzoek van zes auteurs testte of de eerste tokens van een modelantwoord als aanwijzing dienen voor de stijl van de tekst die volgt. Het vastzetten van een korte opening vóór generatie verhoogde de nauwkeurigheid zonder modelgewichten te wijzigen. Dat suggereert dat een deel van de schijnbare redeneerwinst voortkomt uit het selecteren van gedrag dat al tijdens voortraining is geleerd.

Voor promptschrijvers verandert de bevinding de rol van een uitdrukking zoals `think step by step` (“denk stap voor stap”). De woorden hoeven geen instructie te bevatten die het model begrijpt zoals een persoon dat zou doen. De uitdrukking kan het model in plaats daarvan wijzen op gebieden van zijn aangeleerde tekstdistributie waar uitgewerkte oplossingen en uitgebreid redeneren veel voorkomen.

## Een kleine aanwijzing leverde een grote gemeten verandering op

De onderzoekers testten basisversies van verschillende open modellen op wiskunde en programmeren. Op 500 wiskundeproblemen in wedstrijdstijl verhoogde het verplicht beginnen van OLMo-3-7B met een punt, een lege regel en `Okay` de nauwkeurigheid bij één poging van 42 tot 78 procent. Qwen3-14B laten beginnen met `Alright,` verhoogde de score van 72 tot 87 procent.

Die exacte resultaten komen uit de experimenten van de auteurs in een arXiv-preprint en zijn niet onafhankelijk gereproduceerd. Ze hangen ook af van de genoemde modellen, benchmark en decodeeropstelling. Het centrale bewijs van het artikel is echter breder dan één prompt: verschillende beginnen riepen herhaaldelijk verschillend redeneergedrag op en versterkend leren maakte het waarschijnlijker dat de succesvolle beginnen vanzelf optraden.

Dat onderscheid helpt verklaren waarom na-getrainde “denkmodellen” beter kunnen presteren dan hun basismodellen, zelfs wanneer voortraining de onderliggende vaardigheden al heeft geleverd. Versterkend leren kan het model leren wanneer het een nuttige modus moet ingaan en hoe het daarin blijft, terwijl de openingsaanwijzing een deel van dat gedrag handmatig selecteert.

Het resultaat scheidt ook twee vragen die benchmarkscores meestal combineren: of een model een redeneerprocedure bevat en of gewone generatie die op het juiste moment activeert. Een aanwijzing kan het tweede verbeteren zonder het eerste toe te voegen. Dat maakt promptgevoeligheid tot onderdeel van de gemeten vaardigheid en niet slechts ruis eromheen, vooral wanneer twee beoordelaars verschillende antwoordvoorvoegsels of chatsjablonen voor hetzelfde basismodel gebruiken.

## Wijzigingen in trainingsdata veranderden de betekenis van de aanwijzing

De sterkste causale test veranderde de trainingsassociatie zelf. Het team maakte een willekeurig woord, `chicken` (“kip”), via gerichte data-interventies tot een effectieve redeneeraanwijzing en verzwakte ook een bestaande aanwijzing. Een verwante interventie liet `Think duck duck goose` werken als `Think step by step`.

Dit is veelzeggender dan het vinden van een gelukkige tekenreeks door prompts te doorzoeken. Als het veranderen van de voorbeelden die aan een token zijn gekoppeld het gedrag verandert dat dat token oproept, hangt het aanwijzingseffect samen met aangeleerde associaties en niet met een bijzondere semantische eigenschap van `Okay` of `Alright`. Interne representaties die door verschillende aanwijzingen werden opgeroepen correleerden ook met verschillende soorten documenten in de trainingsset.

De methode maakt prompting niet tot een universeel alternatief voor versterkend leren. Een vaste opening moet voor een model en taak worden ontdekt en succes op wiskunde of code zegt weinig over betrouwbaarheid elders. De veiligheidscasus van het artikel vond dat aanwijzingen ook verschillende weigerings- en gehoorzaamheidspatronen konden selecteren, waardoor dezelfde gevoeligheid relevant is voor veiligheidsmaatregelen.

Het veiligheidsresultaat wijst in beide richtingen. Een weigeringsbenchmark kan veranderen wanneer een ogenschijnlijk onschuldige opening de generatie naar een andere klasse trainingsvoorbeelden stuurt, terwijl een aanval die route kan misbruiken. Evaluaties moeten daarom het exacte antwoordvoorvoegsel en chatsjabloon vastleggen, niet alleen de gebruikersprompt en modelnaam.

Sophie L. Wang, Amil Dravid, Rulin Shao, Kevin Farhat, Sewon Min en Alexei A. Efros dienden het werk op 5 oktober in en publiceerden code bij de preprint. Onafhankelijke replicaties kunnen testen of de aanwijzingseffecten standhouden bij veranderingen in modelfamilie, benchmark en bemonsteringsinstellingen.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
|---|---|---|---|
| Vaste openingstokenaanwijzingen maakten basismodellen op wiskunde en programmeren concurrerend met tegenhangers die via versterkend leren zijn getraind | VOLGENS HET BEDRIJF | [Preprint van Wang en collega's](https://arxiv.org/abs/2610.06851) | geen |
| De aanwijzing `Okay` verhoogde OLMo-3-7B van 42% tot 78% op MATH-500 pass@1 | VOLGENS HET BEDRIJF | [Preprint van Wang en collega's](https://arxiv.org/abs/2610.06851) | geen |
| De aanwijzing `Alright,` verhoogde Qwen3-14B van 72% tot 87% op MATH-500 pass@1 | VOLGENS HET BEDRIJF | [Preprint van Wang en collega's](https://arxiv.org/abs/2610.06851) | geen |
| Versterkend leren maakte succesvolle aanwijzingen waarschijnlijker en vaste aanwijzingen haalden veel van de prestatiewinst terug | VOLGENS HET BEDRIJF | [Preprint van Wang en collega's](https://arxiv.org/abs/2610.06851) | geen |
| Causale data-interventies maakten willekeurige uitdrukkingen effectief en verwijderden bestaande aanwijzingseffecten | VOLGENS HET BEDRIJF | [Preprint van Wang en collega's](https://arxiv.org/abs/2610.06851) | [Vrijgegeven code](https://github.com/sophie-xh-wang/reasoning-by-cue) |
| De preprint werd op 5 oktober 2026 door zes auteurs ingediend | GEVERIFIEERD | [arXiv-vermelding](https://arxiv.org/abs/2610.06851) | geen |
