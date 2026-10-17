+++
title = "Een model weet niet welke vraag het van mening doet veranderen"
slug = "model-weet-niet-welke-vraag-zijn-mening-verandert"
description = "Een nieuwe studie vindt dat taalmodellen niet betrouwbaar de cruciale deelvragen kunnen benoemen die hun conclusies bepalen. Daarvoor zijn veel uitvoeringen nodig, niet één zelfverzekerde uitleg."
tags = ["research", "models"]
date = 2026-10-17T04:18:00+02:00
draft = false
+++

Stel dat een analist een model vraagt of een voorgestelde softwaremigratie moet doorgaan. Het model zegt ja en geeft drie redenen. Op de vraag welk feit zijn advies kan omkeren, wijst het op de databasedoorvoer. In dit voorbeeld laten herhaalde uitvoeringen zien dat doorvoer nauwelijks uitmaakt. Het advies slaat om wanneer het model zijn aanname over de terugdraaitijd verandert, een factor die het nooit noemde.

Een nieuwe preprint maakt die afwijking meetbaar. De auteurs noemen de beslissende deelvraag een crux: een punt waarover de eigen redeneerpaden van een model uiteenlopen en waarvan het antwoord de eindconclusie kan veranderen. Ze vragen of een taalmodel die cruciale deelvragen kan herkennen voordat het redeneert, of nadat het één gedachtegang heeft geproduceerd. Meestal lukt dat niet.

Het resultaat gaat in tegen een comfortabele gewoonte in samenwerking tussen mens en AI. We vragen een model vaak uit te leggen wat belangrijk is en gebruiken die uitleg vervolgens om te bepalen wat we controleren. Als de uitleg niet overeenkomt met de variabelen die het modelantwoord werkelijk bepalen, gaat het verificatiebudget naar de verkeerde zaken.

## Van uitleg naar gedragstest

De studie definieert een crux niet als alles wat een model belangrijk noemt. Ze bekijkt veel uitvoeringen van hetzelfde probleem. Verschillende steekproeven leggen onenigheid in tussenantwoorden bloot; de onderzoekers testen vervolgens of het oplossen van zo'n meningsverschil de conclusie zou veranderen.

Die definitie maakt de claim gedragsmatig. Een deelvraag is belangrijk doordat de modeluitvoer verandert wanneer het antwoord erop verandert, niet doordat het model er een overtuigende alinea over schrijft. Het onderscheid lijkt op het uitvoeren van stresstests op een programma in plaats van zijn commentaar als documentatie te accepteren.

De auteurs vergelijken drie routes. Een route vooraf vraagt het model zijn cruciale deelvragen te voorspellen voordat het het probleem oplost. Een route met één uitvoering laat het eenmaal redeneren en daarna de cruciale punten benoemen. Een route met veel uitvoeringen zoekt naar meningsverschillen tussen bemonsterde oplossingen en meet welke daarvan het eindresultaat kunnen omkeren.

De eerste route hield weinig verband met de factoren die later doorslaggevend bleken. Eén voltooide gedachtegang loste het probleem niet op. Alleen de procedure met herhaalde uitvoeringen bracht betrouwbaar bruikbare cruciale deelvragen aan het licht.

Dit is niet alleen opnieuw een bevinding dat uitleg onjuist kan zijn. Het model wordt iets beperkters en praktischers gevraagd: welk ontbrekend antwoord zou zijn eigen mening veranderen? Falen op dat punt betekent dat een systeem goed gekalibreerd kan klinken terwijl het een beheerder afleidt van de test die ertoe doet.

## Waarom één gedachtegang niet genoeg is

Eén redeneerspoor toont één route door een probleem. Het laat niet zien welke routes het model bij andere steekproeven kan volgen, of welke aannames daartussen variëren. Een factor kan centraal lijken in het zichtbare spoor en toch in alle uitvoeringen stabiel zijn. Een andere kan als een klein detail verschijnen, maar de bemonsterde conclusies verdelen.

Herhaalde steekproeven worden al lang gebruikt om antwoorden via zelfconsistentie nauwkeuriger te maken: genereer meerdere redeneerpaden en kies het antwoord dat het vaakst voorkomt. De cruxmethode gebruikt variatie anders. Onenigheid is geen ruis om uit te middelen, maar bewijs over de beslissingsgrens.

De kosten zijn duidelijk. Veel oplossingen genereren en beoordelen kan veel duurder zijn dan eenmaal vragen. De onderzoekers vervangen een LLM-beoordelaar door een herordener en melden dat de procedure ongeveer 86 keer goedkoper wordt. Die verlaging brengt een onderzoeksinstrument dichter bij een praktisch diagnosemiddel, maar maakt het niet gratis. Een besluit met grote gevolgen kan de extra inferentie rechtvaardigen; een gewoon chatantwoord mogelijk niet.

De methode hangt er ook van af of de bemonsterde uitvoeringen betekenisvolle alternatieven verkennen. Als iedere uitvoering dezelfde verborgen aanname herhaalt, legt geen meningsverschil die bloot. Een gevonden crux hoort bij dit model, deze prompt en deze steekproefprocedure. Het is niet automatisch het objectief beslissende feit in de buitenwereld.

## Wat verandert voor agenten en beoordelaars

Agentsystemen laten steeds vaker één model plannen en een ander beoordelen. Een planner kan “belangrijkste onzekerheden” opsommen, waarna een beoordelaar die controleert en het resultaat goedkeurt. De studie suggereert dat die nette taakverdeling de blinde vlekken van de planner kan overnemen. Een zelfgerapporteerde onzekerheid is niet hetzelfde als een gedragsmatig beslispunt.

Voor dure taken of taken met grote gevolgen zou een sterkere werkwijze verschillende plannen bemonsteren, de meningsverschillen vinden die het advies veranderen en daarop tools of menselijke aandacht inzetten. Bij software kan de crux zijn of een migratie onder belasting kan worden teruggedraaid. Bij onderzoek kan het gaan om de vraag of een aangehaald resultaat op de huidige populatie van toepassing is. In een investeringsnota kan het een aanname over herfinanciering zijn, in plaats van de marktgrootteschatting die de tekst domineert.

De bevinding scherpt ook de betekenis van zelfkennis bij modellen aan. Een systeem kan een conclusie geven, een plausibele route beschrijven en benoemen wat het belangrijk acht, terwijl het niet kan voorspellen wat zijn eigen toekomstige uitvoer werkelijk bepaalt. Vloeiende introspectie is geen betrouwbare introspectie.

Daarmee wordt uitleg niet nutteloos. Ze kan aannames blootleggen, een voorgestelde redenering overbrengen en iemand helpen ontbrekend bewijs op te merken. De studie laat zien waarom een uitleg moet worden behandeld als een andere modeluitvoer om te testen, niet als bevoorrechte toegang tot het mechanisme dat het antwoord produceerde.

Terug naar het voorbeeld van het migratiebesluit. De analist kan een dag besteden aan doorvoerbenchmarks en het advies toch instabiel laten. Verschillende bemonsterde plannen zouden tonen dat het model verdeeld raakt over de terugdraaitijd. De nuttige vraag is niet langer “Wat is volgens jou belangrijk?”, maar “Welk antwoord verandert werkelijk de uitkomst, over de verschillende manieren waarop je kunt redeneren?”

## Referenties


- Reber et al. (2026). *Can LLMs Anticipate Their Cruxes?* https://arxiv.org/abs/2610.21006
- Wang, X., et al. (2023). *Self-Consistency Improves Chain of Thought Reasoning in Language Models*. https://arxiv.org/abs/2303.08896
