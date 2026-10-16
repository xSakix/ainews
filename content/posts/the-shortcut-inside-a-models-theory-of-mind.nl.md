+++
title = "De sluiproute in de theory of mind van een model"
slug = "sluiproute-in-theory-of-mind-van-model"
description = "Taalmodellen leken overtuigingen binnen overtuigingen te kunnen volgen. HopToM laat zien dat veel benchmarkvragen een minder diepe route naar het antwoord toelaten en biedt daarna een goedkopere manier om de volledige keten te doorlopen."
tags = ["research", "agents"]
date = 2026-10-15T04:05:30+02:00
draft = false
+++

Een controlekamer na een overdracht. Ana heeft de sleutel naar de blauwe lade verplaatst. Boris zag haar. Cara zag Boris vóór de verplaatsing vertrekken, terwijl David alleen Cara hoorde beschrijven wat zij dacht dat Boris wist. Nu moet een assistent een gerichte vraag beantwoorden: waar denkt David dat Cara gelooft dat Boris zal zoeken?

Ana, Boris, Cara en David zijn verzonnen. De verwarring is dat niet. Agents die onderhandelen, onderwijzen, coördineren of namens mensen handelen, moeten de wereld onderscheiden van ieders beeld daarvan. Een nieuwe preprint betoogt dat de tests om die vaardigheid te meten de puzzel vaak eenvoudiger hebben gemaakt dan hun labels suggereren.

## Een vraag van de vierde orde met een uitweg van de tweede orde

Theory of mind is het vermogen te redeneren over de kennis, bedoelingen of overtuigingen van een ander. De vorm van hogere orde nest die perspectieven: Alice gelooft dat Bob denkt dat Carol iets weet. Onderzoekers hebben zulke verhalen gebruikt om te vragen of taalmodellen meerdere geesten tegelijk kunnen volgen.

De nieuwe studie, *Beyond Belief Nesting*, begint met een onderscheid dat technisch klinkt en het resultaat verandert. Het aantal namen of overtuigingswerkwoorden in een vraag is niet noodzakelijk gelijk aan de hoeveelheid genest redeneren die nodig is om haar te beantwoorden. Een vraag die nominaal van de vierde orde is, kan afhangen van bewijs dat slechts twee perspectieven onderscheidt. Het model kan de rest van de keten negeren en toch punten krijgen.

Shanshan You en collega's noemen dit orde-inflatie. Ze definiëren effectieve orde door de afzonderlijke gebeurtenissen te tellen die nodig zijn om opeenvolgende overtuigingsvoorvoegsels te ondersteunen. Een test bereikt de volledige orde alleen wanneer elke laag van de vraag afhangt van bewijs dat een minder diepe oplossing uitsluit.

Die correctie doet ertoe omdat eerdere benchmarks een aantrekkelijke voortgang hadden vastgesteld. HI-TOM, gepubliceerd in 2023, genereerde verhalen met steeds verder geneste overtuigingen en vond dat modelprestaties daalden naarmate de orde steeg. Recentere methoden verbeterden daarna resultaten door expliciete perspectieven op te bouwen. RecToM transformeert een verhaal recursief vanuit het gezichtspunt van elk personage en meldde perfecte nauwkeurigheid op HI-TOM met GPT-5.4 en Qwen3.5. De score leek vooruitgang in diep sociaal redeneren.

HopToM vraagt of de test zelf nog een sluiproute toeliet.

## De daling nadat sluiproutes verdwijnen

De onderzoekers bouwden gecertificeerde vragen van volledige orde en koppelden die aan controles voor alternatieven van lagere orde. Bij direct prompten daalde de gemiddelde nauwkeurigheid van vier toonaangevende modellen van 73,5 procent bij de eerste orde naar 20,0 procent bij de vierde orde. Ook menselijke deelnemers vonden de diepere vragen moeilijk.

De daling alleen bewijst niet dat modellen geen theory of mind hebben. Ze laat zien dat succes op eenvoudiger benchmarkconstructies de sterkere claim niet kan onderbouwen. Een model kan correct antwoorden doordat het verhaal een aanwijzing dicht bij het gevraagde feit bevat, doordat iemands perspectief nooit van de werkelijkheid afwijkt of doordat tussenliggende overtuigingen het antwoord niet beïnvloeden.

Het team greep vervolgens in op het bewijs in de verhalen. Een terugkerend foutenpatroon volgde de ondersteuning voor minder diepe overtuigingsvoorvoegsels: modellen antwoordden alsof ze bij het perspectief van een eerdere persoon waren gestopt. Dat resultaat verbindt de fouten met de structuur van het redeneerprobleem, in plaats van alleen met langere prompts of meer namen.

De bevinding past ook bij een bredere verandering in theory-of-mind-evaluatie. OmniToM accepteert een eindantwoord niet als de volledige test. Het vraagt modellen expliciete overtuigingsuitspraken te extraheren en hun orde, waarheidsstatus, toegang tot kennis en mentale bron te labelen. In 895 verhalen en 22.343 gelabelde uitspraken vonden de auteurs een knelpunt bij het omzetten van verhaalfeiten in overtuigingen per persoon. Een model kan elke gebeurtenis in een verhaal kennen en toch een gebeurtenis aan de verkeerde geest toeschrijven.

## Leg de perspectieven één keer vast

HopToM doet meer dan een score verlagen. Het artikel introduceert HopTrace, een procedure tijdens inferentie die elke interactie één keer omzet in een perspectiefregistratie. Een deterministische oplosser volgt die registraties vervolgens door een geneste vraag.

Deze aanpak vermijdt dat een model herhaaldelijk wordt gevraagd de volledige keten te reconstrueren. Op de gecertificeerde verhalende benchmarkvragen verbeterde HopTrace de nauwkeurigheid bij de vierde orde met 22,0 procentpunt en bij de vijfde orde met 38,5 procentpunt ten opzichte van sterke promptbaselines. Het gebruikte 20 tot 39 keer minder tokens dan methoden met meerdere aanroepen.

De combinatie is ongebruikelijk. Redeneerhulpmiddelen ruilen vaak kosten voor nauwkeurigheid door meer antwoorden te bemonsteren, meerdere agents te vragen of langere redeneersporen te produceren. HopTrace geeft het model juist een representatie die op een auditspoor lijkt: wie welke gebeurtenis waarnam, wat elke deelnemer kon afleiden en welk perspectief de volgende stap moet overnemen.

Dat beslecht niet of het model geesten in menselijke zin begrijpt. Het verandert de technische vraag. Een agent heeft mogelijk geen algemeen vermogen genaamd theory of mind nodig als zijn raamwerk expliciete, inspecteerbare perspectiefregistraties kan bijhouden. De registraties kunnen ook tonen waar de keten brak, iets wat een correct eindantwoord niet kan.

## Wat de benchmark nu vereist

Overtuigingstaken van hogere orde liggen dicht bij praktische fouten in multiagentsystemen. Een assistent die een vergadering plant, moet onderscheiden wat de organisator weet van wat elke deelnemer heeft ontvangen. Een supportagent moet een klantclaim onderscheiden van een interne notitie en van een samenvatting van een andere agent. Een onderhandelingsagent moet overtuigingen bijhouden die onvolledig, verouderd of bewust ongelijk verdeeld zijn.

In elk geval kan oppervlakkige overeenstemming een gevaarlijke fout verbergen. Meerdere agents kunnen gemiddeld nauwkeurige antwoorden produceren terwijl ze dezelfde blinde vlek delen. Een andere preprint van deze week, *Smart Alone, Blind Together*, betoogt dat gecorreleerde fouten bepalen of een theory-of-mind-module veilig is voor een team. Nauwkeurigheid alleen kan coördinatie niet certificeren wanneer elke deelnemer op dezelfde perspectiefgrens faalt.

HopToM verandert daarom wat een overtuigend resultaat moet bevatten. De vraag moet elke geclaimde redeneerorde afdwingen. De evaluatie moet tussenliggende perspectieven zichtbaar maken. Vergelijkingen moeten tokenkosten omvatten, omdat een methode met tientallen modelaanroepen onbruikbaar kan zijn binnen een werkende agent. Ook menselijke moeilijkheid moet zichtbaar blijven: overtuigingen van de vierde en vijfde orde zijn zwaar cognitief werk, geen routinematige taaloefening.

Het artikel is een preprint. De resultaten moeten worden gerepliceerd op meer modellen, omgevingen en natuurlijke interacties. Gecertificeerde synthetische vragen kunnen een mechanisme isoleren, maar echte gesprekken bevatten dubbelzinnigheid, misleiding en ontbrekend bewijs die in een gegenereerd verhaal kunnen worden weggecontroleerd.

Terug naar de denkbeeldige controlekamer. Een vaardige assistent moet niet raden welke lade een personage zal noemen omdat de laatste zin blauw vermeldt. Hij moet het uitzicht vanuit elke stoel behouden en tonen hoe het antwoord van de ene geest naar de volgende ging. De nieuwe benchmark laat elk van die overgangen meetellen.

## Referenties

- Bawatneh, A., Sapkota, S., Bedi, A. S., Karmaker, S., & Shah, M. (2026). *OmniToM: Benchmarking Theory of Mind in LLMs via Explicit Belief Modeling*. https://arxiv.org/abs/2605.26322
- Beaumaster, S., & Schrater, P. (2026). *Smart Alone, Blind Together: Why Accuracy Fails to Certify Theory of Mind in Multi-Agent Teams*. https://arxiv.org/abs/2610.19051
- He, Y., Wu, Y., Jia, Y., Mihalcea, R., Chen, Y., & Deng, N. (2023). *HI-TOM: A Benchmark for Evaluating Higher-Order Theory of Mind Reasoning in Large Language Models*. https://arxiv.org/abs/2310.16755
- Lei, C., Hu, G., Yang, M., Jiang, Y., & Lipovetzky, N. (2026). *Mind the Perspective: Let's Reason Recursively for Theory of Mind*. https://arxiv.org/abs/2606.11724
- You, S., Wang, Z., Liu, H., Liu, Y., He, Y., Hao, X., & Wang, L. (2026). *Beyond Belief Nesting: Rethinking Higher-Order Theory of Mind in Large Language Models*. https://arxiv.org/abs/2610.17777
