+++
title = "Hetzelfde antwoord kan een andere overtuiging verbergen"
slug = "hetzelfde-antwoord-kan-andere-overtuiging-verbergen"
description = "Een nieuw artikel laat zien dat taalmodellen identieke voorspellingen kunnen doen en toch radicaal ander gewicht aan het volgende bewijs geven. Voor agents, evaluatoren en systemen met grote gevolgen zijn gelijke antwoorden niet voldoende."
tags = ["research", "models", "agents"]
date = 2026-11-07T04:18:00+01:00
draft = false
+++

Stel dat twee risicomodellen allebei de kans op het uitvallen van een leverancier op 30 procent schatten. Een inkoopteam zou ze normaal gesproken als uitwisselbaar beschouwen. Dan komt een melding van een te late betaling binnen. Het ene model gaat naar 35 procent, het andere springt naar 70 procent. Deze opening is een illustratie, maar het beschreven probleem is onderwerp van een nieuwe preprint: hetzelfde antwoord nu kan een ander antwoord op de volgende vraag verhullen.

*Same Answer, Different Future*, van onderzoekers van UC Berkeley en Google DeepMind, bestudeert wat taalmodellen doen nadat hun huidige voorspellingen gelijk zijn gemaakt. Het centrale resultaat is eenvoudig en ongemakkelijk. Overeenstemming op één moment betekent niet dat modellen het eens zijn over hoe bewijs die voorspelling moet veranderen. Een evaluator die alleen het huidige antwoord controleert, kan daardoor systemen goedkeuren waarvan het toekomstige gedrag wezenlijk verschilt.

## Dezelfde voorspelling via een andere route

De auteurs gebruiken een gecontroleerde Bernoulli-taak. Een model ziet een reeks binaire waarnemingen en voorspelt de kans op de volgende. Omdat de juiste bijstelling wiskundig duidelijk is, kan het experiment het uitgesproken antwoord scheiden van het gewicht dat het model aan nieuw bewijs geeft.

Bij drie modellen met open gewichten maken de onderzoekers gelijke beginvoorspellingen via vier tekstuele routes en twee activatie-ingrepen. Die routes kunnen het model op dezelfde kans laten uitkomen, maar met andere beschrijvingen van de waarnemingen, samenvattingen of aannames. De interne ingrepen wijzigen activaties rechtstreeks. Nadat de beginuitvoer overeenkomt, krijgen de modellen dezelfde nieuwe waarnemingen.

Hun bijstellingen lopen uiteen.

Het artikel meet een “effectief bewijsgewicht”: hoeveel een voorspelling verandert als reactie op nieuwe gegevens. Modellen met dezelfde beginkans kunnen zich gedragen alsof ze heel verschillende hoeveelheden eerder bewijs hebben gezien. Een model dat zich zeer zeker gedraagt verandert weinig. Een model dat zijn huidige antwoord als zwak onderbouwd behandelt verandert veel sterker. Het zichtbare getal onthult niet in welke toestand het model verkeert.

Het is niet alleen een formuleringseffect. Volgens de auteurs schalen samenvattingen slechts zwak mee met het aantal waarnemingen dat ze zouden vertegenwoordigen. Een model vertellen dat een statistiek een grote steekproef samenvat, geeft die statistiek niet betrouwbaar de weerstand tegen verandering die een Bayesiaanse waarnemer eraan zou toekennen. Omgekeerd kan expliciet vragen om redenering de effectieve bewijsgewichten met ordes van grootte veranderen. Meer uitleg vragen is dus niet altijd een passieve meting: het kan het gemeten proces veranderen.

## Waarom eenmalige sturing kwetsbaar is

De activatie-experimenten maken het resultaat bijzonder relevant voor modelsturing. Een gerichte ingreep kan een onmiddellijke voorspelling naar de gewenste waarde verschuiven. Zodra het model nieuw bewijs krijgt, verdwijnt het effect echter vaak. De ingreep bracht de getoonde toestand op één lijn zonder noodzakelijk de bijstellingsregel te veranderen die deze produceerde.

Dat onderscheid is belangrijk voor elk systeem dat over langere tijd handelt. Een klantenserviceagent kan tijdens een test met een terugbetalingsbeleid instemmen en vervolgens een dubbelzinnig bericht in productie anders interpreteren. Een handelsmodel kan dezelfde risicoschatting geven als zijn vervanger, maar sterker reageren op het volgende marktsignaal. Een medische assistent kan op een benchmark een gekalibreerde kans geven en toch inconsistent bijstellen wanneer een nieuw symptoom wordt toegevoegd.

Geen van deze fouten wordt in dit artikel aangetoond. De taak is bewust beperkt en gecontroleerde kansschatting is veel eenvoudiger dan geneeskunde, markten of klantenservice. De voorbeelden zijn mogelijke gevolgen om te testen, geen al bewezen beweringen van de auteurs. Het experiment toont wel het ontbrekende kenmerk aan: identieke huidige uitvoer bepaalt geen identieke toekomstige ontwikkeling.

## Evaluatie heeft opeenvolgende reacties nodig

De meeste modelevaluaties zijn momentopnamen. Ze geven invoer, registreren uitvoer en beoordelen die met een referentie of beoordelaar. Kalibratietests gaan verder dan alleen nauwkeurigheid door te vragen of voorspellingen van 70 procent ook ongeveer 70 procent van de tijd juist zijn. Toch kan zelfs een gekalibreerde momentopname de hier gevonden dynamiek verbergen. Twee systemen kunnen op één verdeling even nauwkeurig en even goed gekalibreerd zijn, maar anders reageren wanneer bewijs stap voor stap binnenkomt.

Eerder onderzoek naar overtuigingsherziening bij taalmodellen liet al zien dat ze inconsistent kunnen bijstellen wanneer feiten botsen of context verandert. Onderzoek naar probabilistische samenhang vraagt of uitgesproken overtuigingen voldoen aan elementaire wiskundige voorwaarden. Het nieuwe artikel voegt tijd toe: zelfs bij een vaste huidige overtuiging beïnvloedt de route waarlangs die tot stand kwam wat daarna gebeurt.

Een sterkere evaluatie zou daarom bijstellingscurven testen. Modellen zouden hetzelfde beginbewijs in verschillende vormen krijgen, hun uitgesproken voorspellingen zouden gelijk worden gemaakt en daarna zouden identieke extra waarnemingen volgen. De score zou behalve het eindantwoord ook gevoeligheid voor steekproefgrootte, volgorde, framing en vraagstelling meten. Voor een agent betekent dat een taak opnieuw uitvoeren met dezelfde operationele toestand, bereikt via verschillende voorgeschiedenissen.

Dat is ook een reden om de herkomst te bewaren. Een applicatie die alleen de nieuwste modelsamenvatting opslaat, kan informatie weggooien die nodig is om latere bijstellingen te interpreteren. Een gestructureerd register van waarnemingen, bronnen en de omzetting naar de samenvatting geeft de volgende inferentiestap meer houvast dan een zin die zekerheid uitspreekt. Geheugensystemen moeten naast conclusies genoeg structuur van het bewijs bewaren om die conclusies voorspelbaar te kunnen herzien.

## Wat bouwers nu kunnen doen

Het artikel biedt geen universele oplossing, maar wijst op drie praktische maatregelen.

Ten eerste: test reeksen in plaats van afzonderlijke beurten. Voeg bewijs toe nadat een model de eerste test heeft doorstaan en vergelijk hoeveel het antwoord bij gelijkwaardige prompts verandert.

Ten tweede: neem niet aan dat een uitgesproken mate van zekerheid een steekproefgrootte vertegenwoordigt. Als het aantal waarnemingen belangrijk is, bewaar dat als gestructureerde data en bereken eenvoudige bijstellingen waar mogelijk buiten het model.

Ten derde: behandel vraagstelling en activatiesturing als ingrepen, niet als transparante vensters. Een verzoek om een gedachteketen, een samenvattingsprompt of een interne wijziging kan later gedrag veranderen. De vraag is zowel of het directe antwoord verbeterde als of de verandering bij nieuwe informatie standhoudt.

Verwant onderzoek naar Bayesiaans onderwijzen biedt een nuttig contrast. Een goede leraar kiest voorbeelden met begrip van hoe de leerling zijn overtuigingen zal bijstellen. Als de bijstellingsregel afhangt van de weergave, wordt lesgeven moeilijker: hetzelfde voorbeeld kan anders doorwerken afhankelijk van de verborgen route naar het huidige antwoord van de leerling.

## De volgende melding

Terug naar de twee modellen voor leveranciersrisico. Het inkoopteam weet nu dat 30 procent geen volledige toestandsbeschrijving is. Voordat het een model goedkeurt, speelt het de melding over late betaling opnieuw af na verschillende gelijkwaardige voorgeschiedenissen en tekent de volledige bijstellingscurve. Ook deze slotscène is een illustratie. De zorgvuldigheid die ze toont is dat niet.

Voor systemen die één voorspelling doen en stoppen, kan overeenstemming op één moment voldoende zijn. Agents stoppen zelden. Ze onthouden, ontvangen bewijs, herzien plannen en handelen opnieuw. Zodra een model een toekomst heeft, hoort de kwaliteit van zijn volgende bijstelling bij de beoordeling van het antwoord van vandaag.

## Referenties

- *Same Answer, Different Future: Language Models Hide Their Belief Updating* — https://arxiv.org/abs/2611.07913
- *Belief Revision in Large Language Models* — https://aclanthology.org/2024.emnlp-main.586/
- *From Drift to Coherence: Probabilistic Beliefs in Language Models* — https://proceedings.mlr.press/v306/kim26ah.html
- *Bayesian teaching and learning with language models* — https://www.nature.com/articles/s41467-025-67998-6
