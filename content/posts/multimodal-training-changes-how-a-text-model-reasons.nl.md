+++
title = "Multimodale training verandert hoe een tekstmodel redeneert"
slug = "multimodale-training-verandert-hoe-een-tekstmodel-redeneert"
description = "Onderzoekers vonden een richting in de verborgen toestand die multimodale modellen gebruiken voor bepaalde ruimtelijke taken op basis van alleen tekst. Het verwijderen ervan schaadde navigatie terwijl logica vaak behouden bleef, wat laat zien waarom een uitleesbare representatie niet vanzelf een representatie is die een model ook gebruikt."
tags = ["research", "models"]
date = 2026-11-16T04:05:26+01:00
draft = false
+++

Leila staat bij een whiteboard in een lege collegezaal en schrijft een route uit in handschrift: kijk naar het noorden, sla rechtsaf, loop door, draai opnieuw. Ze stuurt alleen die woorden naar een model. Het levert een antwoord. Daarna verwijdert ze één smalle richting uit de interne toestand en herhaalt de test. De route, die eenvoudig leek, valt uiteen.

*De scènes aan het begin en het einde van dit artikel zijn illustraties; de personen erin zijn verzonnen.*

Een team van de Nanyang Technological University en de Singapore Management University meldt een versie van die interventie over tien configuraties uit zes multimodale modelfamilies. Hun preprint, gepubliceerd op 11 november, wijst in de ruimte van verborgen toestanden een richting aan die visuele en tekstuele representaties scheidt. Wanneer de onderzoekers tijdens inferentie op basis van alleen tekst de projectie van het model op die richting verwijderden, zakten de ruimtelijke prestaties vaak in terwijl formele logica overeind bleef. Het resultaat levert bewijs voor welke representatie een model gebruikt, en niet de bewering dat het een beeld in zijn hoofd ziet.

## Een richting die een route draagt

Qi Zhang, Bohan Wang, Qianru Sun en Hanwang Zhang noemen het effect “emergent vision-shaped thinking” (opkomend visueel gevormd denken). Het zorgvuldige woord is gevormd. Hun experimenten leggen geen intern beeld bloot. Ze laten zien dat visueel-talige training een representatie introduceerde of versterkte die sommige modellen later inzetten wanneer de invoer geen enkele afbeelding bevatte.

De onderzoekers begonnen met een verschil van gemiddelden. In een representatieruimte waarin visuele en tekstuele signalen te vergelijken waren, berekenden zij de gemiddelde toestand voor elke modaliteit en namen de genormaliseerde richting ertussen. De constructie verschilde per architectuur. Chameleon deelt één vocabulaire voor beeld- en teksttokens, terwijl Qwen3-VL continue visuele kenmerken invoert in een taalbasismodel. BAGEL en Janus-Pro hebben afzonderlijke routes voor visueel begrip en beeldgeneratie, zodat elke route haar eigen richting kreeg.

Tijdens de inferentie trok het team de projectie van elke verborgen toestand op die richting ervan af. De interventie werd toegepast na geselecteerde decoderblokken. Alle evaluatieprompts bestonden uitsluitend uit tekst. Er werd niets visueels uit de invoer verwijderd, omdat er geen afbeelding of visueel token aanwezig was.

Het duidelijkste resultaat kwam van Chameleon-7B. Het verwijderen van de richting in één laag verlaagde de nauwkeurigheid op de navigatietaak van BIG-Bench Hard met 27,6 procentpunt. De nauwkeurigheid op booleaanse expressies steeg met 5,6 punt, wat een scheiding van 33,2 punt tussen beide veranderingen opleverde. De richting onderscheidde zich ook van willekeurige richtingen met gelijke norm, en de schade concentreerde zich rond een kleine groep lagen in plaats van zich gelijkmatig over het netwerk te verspreiden.

Dat paar is van belang omdat BIG-Bench Hard is ontworpen als een reeks van 23 taken die taalmodellen moeilijk vonden. Navigatie en de evaluatie van booleaanse expressies kunnen beide meerdere stappen vergen, maar zij nodigen uit tot verschillende werkrepresentaties. Een in woorden beschreven route laat zich uitzetten als posities en wendingen. Een booleaanse expressie laat zich met formele regels vereenvoudigen.

## Van correlatie naar interventie

Onderzoek naar interpreteerbaarheid begint vaak met een meetprobe: train een eenvoudige classificator om een eigenschap uit verborgen toestanden terug te halen. Het overzichtsartikel van Yonatan Belinkov over probingmethoden legt zowel hun aantrekkingskracht als hun kernzwakte uit. Dat een classificator een eigenschap kan uitlezen, bewijst nog niet dat het oorspronkelijke model erop steunt.

Het nieuwe artikel maakt dat onderscheid tot het middelpunt van het experiment. Het vraagt of het verwijderen van een kandidaat-representatie selectief het gedrag verandert dat ervan zou moeten afhangen. Deze aanpak sluit aan bij eerder werk aan Othello-GPT, waarin Kenneth Li en collega's een interne bordrepresentatie vonden en er vervolgens op ingrepen om voorspellingen van geldige zetten te sturen. In beide gevallen is de nuttige vraag veeleisender dan of informatie aanwezig is: verandert het aanpassen van de representatie het antwoord op de verwachte manier?

Over negen configuraties met een positieve visueel-talige as vonden de auteurs een selectief causaal effect. De locatie hing af van de architectuur. Het effect verscheen vroeg in Chameleon en Qwen3-VL, later in Liquid, en in latere lagen van het generatiepad bij BAGEL en Janus-Pro. Externe controles omvatten bAbI, SpartQA en StepGame. De effecten groepeerden zich doorgaans rond ruimtelijke taken terwijl brede kennis en wiskunde minder veranderden, al meldt het artikel een belangrijke uitzondering: de belangrijkste interventie bij BAGEL beschadigde ook GSM8K en LogiQA sterk, zodat die resultaten geen zuivere bewering over ruimtelijke overdracht ondersteunen.

De vergelijking met pure tekstbasismodellen voegt nog een nuance toe. De Chameleon-richting had nauwelijks invloed op LLaMA-7B, wat de opvatting steunt dat multimodale training een nieuw bruikbaar raamwerk introduceerde. In de Qwen-familie was een verwant raamwerk al aanwezig in het tekstmodel. Multimodale training leek dat te versterken en de interventie selectiever te maken. Het artikel stelt daarom geen enkele universele schakelaar voor visueel denken voor die door alle modellen wordt gedeeld.

## Wat generatie toevoegt

BAGEL en Janus-Pro lieten de onderzoekers twee routes binnen verenigde systemen vergelijken. Deze modellen gebruiken één gedeeld taalbasismodel, terwijl zij visueel begrip en beeldgeneratie via verschillende paden afhandelen. Het generatiepad leverde een compacte, eendimensionale causale hendel op: het verwijderen van die richting verstoorde ruimtelijk redeneren selectief. Het begripspad bevatte ook ruimtelijke informatie die een meetprobe kon decoderen, maar het verwijderen van de bijbehorende richting bracht niet hetzelfde selectieve effect teweeg. Grotere ingrepen op deelruimten brachten dat evenmin tevoorschijn.

Dit is de bruikbaarste waarschuwing van het artikel. Een representatie kan eenvoudig uit te lezen zijn en toch niet het mechanisme vormen dat een antwoord aanstuurt. De auteurs beschrijven drie controles om het verschil vast te stellen: hoe geconcentreerd het signaal is, of de uitleesbare richting samenvalt met de causaal bruikbare richting, en of het experiment het juiste semantische contrast en de juiste laag heeft gekozen.

De laatste controle redde een schijnbare mislukking bij Chameleon-30B. Een as die was geschat uit de embeddingtabel of uit synthetische tokenreeksen leek niet-causaal. Toen het team de as opnieuw opbouwde door echte afbeeldingen door de eigen tokenizer van het model en het volledige multimodale pad te sturen, draaide de richting en werd zij sterk causaal in middelste en laatste blokken. Bij een middelste blok daalde de navigatiescore met 33,6 punt, terwijl de nauwkeurigheid op booleaanse expressies met minder dan één punt veranderde. De drager was verschoven en de eerste meting had op de verkeerde plek gezocht.

## De grens van de bewering

De studie is breed voor een mechanistische interventie, maar de auteurs markeren verschillende beperkingen. Zij test lineaire verwijderingen en verwijderingen van lage rang, waardoor niet-lineaire of verspreide mechanismen buiten beeld kunnen blijven. De takenreeks onderzoekt geselecteerde vormen van ruimtelijk redeneren in plaats van elk type cognitie te dekken. Chameleon-7B presteerde op of onder kansniveau bij mentale rotatie, papiervouwen en perspectiefwisseling, wat betekent dat het bewijs voor die taken afkomstig is van Qwen3-VL-modellen die vanaf het begin sterk genoeg waren.

De drager was bovendien niet uitsluitend ruimtelijk. Lange reeksen niet-ruimtelijke toestandsupdates overlapten er gedeeltelijk mee. Eén test op Qwen3-VL-8B slaagde voor de controle op richtingsspecificiteit maar beschadigde enkele controletaken met lage ruimtelijke eisen, waardoor de verwachte gradiënt over taken heen omkeerde. Publieke onzekerheid over de trainingsgegevens van Qwen beperkt ook uitspraken over wanneer precies het raamwerk ontstond.

Eerdere evaluaties hadden al laten zien dat visueel-talige modellen kwetsbaar blijven bij ruimtelijk redeneren. Jiayu Wang en collega's stelden vast dat het toevoegen van een afbeelding multimodale modellen achter hun pure taalvarianten kon laten terugvallen, vooral wanneer tekstuele aanwijzingen een binnenweg boden. Het nieuwe werk spreekt die uitkomst niet tegen. Het vernauwt de vraag van algehele prestaties naar interne afhankelijkheid: een model kan slecht zijn in een taak en toch een representatie gebruiken die door visuele training is gevormd, of een representatie bevatten die het niet causaal benut.

De interventie van de auteurs toont noodzakelijkheid aan onder de geteste omstandigheden. Zij laat niet zien hoe de richting wordt geschreven, welke circuits haar lezen en evenmin of het model iets opbouwt dat op een mentale scène lijkt. Die vragen blijven buiten het bereik van een eendimensionale aftrekking.

Bij het whiteboard herstelt Leila de verwijderde projectie. Dezelfde tekst loopt door hetzelfde model, en de route houdt weer stand. Er verschijnt geen kaart op de muur. De enige zichtbare verandering is het antwoord.

## Referenties

- Belinkov, Y. (2022). *Probing Classifiers: Promises, Shortcomings, and Advances*. https://aclanthology.org/2022.cl-1.7/
- Li, K., Hopkins, A. K., Bau, D., Viégas, F., Pfister, H., & Wattenberg, M. (2023). *Emergent World Representations: Exploring a Sequence Model Trained on a Synthetic Task*. https://openreview.net/forum?id=DeG07_TcZvT
- Suzgun, M., Scales, N., Schärli, N., Gehrmann, S., Tay, Y., Chung, H. W., Chowdhery, A., Le, Q., Chi, E., Zhou, D., & Wei, J. (2023). *Challenging BIG-Bench Tasks and Whether Chain-of-Thought Can Solve Them*. https://aclanthology.org/2023.findings-acl.824/
- Wang, J., Ming, Y., Shi, Z., Vineet, V., Wang, X., Li, Y., & Joshi, N. (2024). *Is A Picture Worth A Thousand Words? Delving Into Spatial Reasoning for Vision Language Models*. https://proceedings.neurips.cc/paper_files/paper/2024/hash/89cc5e613d34f90de90c21e996e60b30-Abstract-Conference.html
- Zhang, Q., Wang, B., Sun, Q., & Zhang, H. (2026). *Emergent Vision-Shaped Thinking in Text-Only Reasoning through Multimodal Training*. https://arxiv.org/abs/2611.14942
