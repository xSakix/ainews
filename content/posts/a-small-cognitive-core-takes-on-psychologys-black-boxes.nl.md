+++
title = "Een kleine cognitieve kern daagt de black boxes van de psychologie uit"
slug = "kleine-cognitieve-kern-daagt-black-boxes-psychologie-uit"
description = "Twee onderzoekers combineerden enkele gevestigde ideeën over geheugen, context en voorspellingsfouten tot één model van menselijke keuzes. CORE versloeg vergelijkbare neurale voorspellers in 137 experimenten en hield zijn interne werking inzichtelijk."
tags = ["research", "models"]
date = 2026-10-14T04:02:33+02:00
draft = false
+++

Stel een deelneemster voor die alleen in een psychologielaboratorium zit. Er verschijnt een symbool en daarna nog een. Ze raadt achter welke deur een beloning schuilgaat, herinnert zich de laatste verrassing en verandert langzaam haar strategie. Deze deelneemster is verzonnen, maar elke kleine handeling behoort tot de experimentele gegevens achter een nieuw model dat miljoenen van zulke keuzes probeert te verklaren zonder de verklaring in een neuraal netwerk te verbergen.

## Veel experimenten, één verklaring

Marcel Binz en Eric Schulz van het Institute for Human-Centered AI bij Helmholtz Munich hebben COntextual Retrieval and Encoding, ofwel CORE, gebouwd. Hun preprint verenigt een kleine verzameling gevestigde cognitieve principes in één computationeel model en past dat vervolgens gezamenlijk aan op 7.036.442 menselijke keuzes uit 137 experimenten en 80.452 experimentele sessies.

De ambitie gaat verder dan het voorspellen van één taak. De psychologie heeft verklaringen verzameld voor associatie, voorspellingsfouten, hiërarchische representatie, het ophalen van herinneringen en vergeten, vaak getest binnen afzonderlijke experimentele tradities. CORE vraagt hoeveel van de vastgelegde gedragingen deze ideeën kunnen verklaren wanneer ze binnen één verzameling mechanismen moeten samenwerken.

De structuur is een hiërarchie van episodische herinneringen. Voorspellingsfouten worden in die herinneringen geschreven. Context bepaalt wat wordt gecodeerd, welke herinneringen worden opgehaald en hoe ze vervagen. Deze bewerkingen zijn uitgedrukt als componenten waarvan een onderzoeker de rollen kan inspecteren, in plaats van als een onbeperkt sequentiemodel dat uitsluitend is getraind om fouten te minimaliseren.

De auteurs vergelijken CORE met een transformer met een vergelijkbare configuratie en met Centaur, een basismodel van menselijke cognitie dat werd geïntroduceerd door een grote samenwerking onder leiding van Binz. Centaur finetunede een taalmodel op Psych-101, een dataset met meer dan tien miljoen keuzes uit 160 experimenten. Het liet zien dat één groot voorspellend systeem kon generaliseren tussen achtergrondverhalen, taakwijzigingen en onbekende domeinen. Het bracht ook de vertrouwde prijs van basismodellen naar voren: de voorspellingen werden breed toepasbaar, terwijl het geleerde mechanisme moeilijk als een psychologische theorie te formuleren bleef.

CORE keert die afweging om. In het nieuwe artikel behaalt het een lagere voorspellende negatieve log-likelihood dan de vergelijkbare transformer: 262.572 tegenover 329.043. Tegenover Centaur is de vergelijking 262.572 tegen 389.151. CORE presteert beter dan de transformer in alle 62 studies die voor die vergelijking op studieniveau zijn gebruikt en beter dan Centaur in 47.

Deze cijfers betekenen niet dat CORE de menselijke geest heeft gevat. Ze vergelijken voorspellingen binnen een specifieke samengevoegde verzameling experimentele gegevens. Ze laten wel zien dat een interpreteerbaar model niet gedwongen was voorspellend bereik op te offeren alleen omdat zijn onderdelen een psychologische betekenis hadden.

## Wat het model onthoudt

De hiërarchie doet ertoe omdat een keuze kan afhangen van gebeurtenissen op verschillende schalen. Een recente fout kan de volgende reactie veranderen. Een reeks verwante proeven kan een lokale situatie vormen. Een verschuiving in het experiment kan oudere ervaring minder relevant maken, ook wanneer die nog opgeslagen is.

CORE verwerkt die effecten door contextafhankelijk te coderen en herinneringen op te halen. Voorspellingsfouten werken het geheugen bij in plaats van simpelweg één waardeschatting te veranderen. Het model kan een episode ophalen wanneer de huidige situatie erop lijkt, terwijl het vergeetproces ervaring minder gewicht geeft naarmate de context ervan afwijkt.

Dat ontwerp produceert interne sporen die bekend zijn uit gevestigde theorieën. De auteurs melden kenmerken van Bayesiaans leren in de latente variabelen van CORE: het bijwerken reageert op onzekerheid op manieren die samenhangen met probabilistische inferentie. Ze vinden ook kenmerken van gebeurtenissegmentatie. Dat betekent dat de interne organisatie van het model grenzen tussen situaties weerspiegelt in plaats van de volledige stroom als uniform te behandelen.

Het resultaat breidt een onderzoeksprogramma uit dat dezelfde auteurs vanuit de tegenovergestelde richting hebben gevolgd. In 2023 lieten Binz en Schulz zien dat taalmodellen die op psychologische experimenten waren gefinetuned, traditionele cognitieve modellen in twee beslisdomeinen konden overtreffen en informatie over individuele deelnemers konden bevatten. Hun werk over meta-geleerde cognitie betoogde dat leeralgoritmen Bayes-optimaal gedrag konden benaderen en tegelijk beperkte rekenkracht en andere realistische beperkingen konden meenemen.

Die systemen vroegen hoe ver algemene machinelearningmethoden richting menselijk gedrag konden komen. CORE vraagt hoe ver een compacte psychologische theorie richting het voorspellende bereik van machine learning kan komen. De twee richtingen ontmoeten elkaar nu op een deel van dezelfde gegevens.

## Effecten reproduceren in plaats van ze benoemen

Voorspelling is slechts een deel van de test. De auteurs simuleren CORE onder de experimentele omstandigheden en vragen of het de gedragseffecten reproduceert die de studies meldden. Het reproduceert 75 procent daarvan.

Dit is een strengere eis dan een gemiddeld keuzefrequentiepatroon evenaren. Een effect kan aanpassing, vertekening, volgorde, onzekerheid of een verandering na een contextuele grens omvatten. Om het te reproduceren moet het gedrag van het model in de relevante richting bewegen wanneer de experimentele manipulatie verandert.

Het ontbrekende kwart doet er evenveel toe als de succesvolle drie kwart. Een overkoepelend model wordt wetenschappelijk bruikbaar wanneer zijn fouten laten zien waar de voorgestelde kern onvolledig is. Een black-boxvoorspeller kan een nieuw patroon opnemen zonder onderzoekers te vertellen welke theorie veranderde. Een interpreteerbaar systeem dwingt tot een duidelijkere keuze: het ophalen van herinneringen herzien, een mechanisme toevoegen, de hiërarchie veranderen of accepteren dat het verschijnsel buiten de verklaring valt.

De breedte van het artikel brengt ook risico's met zich mee. Experimenten verschillen in instructies, antwoordformaten, deelnemerspopulaties en analytische conventies. Gezamenlijke aanpassing kan mechanismen bevoordelen die gemeenschappelijke structuren verklaren, terwijl ongebruikelijke structuren worden gladgestreken. Een totale likelihood kan een zwakke verklaring van een klein maar belangrijk domein verbergen. Daarom rapporteren de auteurs vergelijkingen op studieniveau en gesimuleerde effecten, en niet alleen één totaalscore.

CORE is ook een preprint. De claims, implementatiekeuzes en harmonisatie van datasets hebben de peerreview nog niet doorlopen. Het corpus is groot naar de maatstaven van de experimentele psychologie, maar blijft een geselecteerde verzameling taken die gezamenlijk kunnen worden weergegeven en gemodelleerd. Het menselijke leven buiten een laboratorium omvat taal, sociale relaties, emotie en lichamelijk handelen die niet zijn samengeperst tot zeven miljoen afzonderlijke keuzes.

## Een theorie die fout kan zijn

De belangrijkste bijdrage van het model kan methodologisch zijn. De cognitieve wetenschap heeft vaak moeten kiezen tussen een transparant model dat één paradigma verklaart en een algemene voorspeller die weinig over het mechanisme zegt. CORE levert bewijs dat deze grens kan verschuiven.

Dat neemt neurale modellen of basismodellen niet weg. Centaur biedt een sterke voorspellende referentie en kan generaliseren via taakbeschrijvingen in natuurlijke taal. Een compact model kan zulke systemen gebruiken als concurrenten, datageneratoren of hulpmiddelen voor ontdekking. Het belangrijke onderscheid is welke claim elk systeem ondersteunt. Een voorspeller laat zien dat gedrag kan worden voorzien. Een cognitieve theorie beschrijft de bewerkingen die dat gedrag volgens haar hebben voortgebracht.

Omdat CORE die bewerkingen beschrijft, kunnen onderzoekers erop ingrijpen. Ze kunnen contextafhankelijk vergeten verwijderen, de geheugenhiërarchie afvlakken of veranderen hoe voorspellingsfouten worden geschreven, en vervolgens bepalen welke experimenten mislukken. Ze kunnen ook een voorgesteld principe toevoegen en testen of het zijn plaats verdient over de volledige verzameling gegevens, in plaats van één zorgvuldig uitgekozen taak te verbeteren.

Terug naar de denkbeeldige deelneemster voor twee deuren. Haar volgende keuze kan nu worden voorspeld door een groot ondoorzichtig model of worden gereconstrueerd via een herinnering aan verrassingen, geordend naar context en met ruimte om te vervagen. Het eerste kan gelijk hebben. Het tweede geeft de wetenschapper iets anders: een precieze verklaring die het volgende experiment kan weerleggen.

## Referenties

- Binz, M., Dasgupta, I., Jagadish, A., Botvinick, M., Wang, J. X., & Schulz, E. (2023). *Meta-Learned Models of Cognition*. https://arxiv.org/abs/2304.06729
- Binz, M., et al. (2024). *Centaur: a foundation model of human cognition*. https://arxiv.org/abs/2410.20268
- Binz, M., & Schulz, E. (2023). *Turning large language models into cognitive models*. https://arxiv.org/abs/2306.03917
- Binz, M., & Schulz, E. (2026). *A small cognitive core explains human behavior at scale*. https://arxiv.org/abs/2610.13603
