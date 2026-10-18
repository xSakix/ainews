+++
title = "De agenten waren het oneens, maar namen de leugen over"
slug = "agenten-waren-het-oneens-maar-namen-de-leugen-over"
description = "Een experiment met tien agenten vindt dat één volhardende tegenstander goedwillende agenten intern een onjuiste overtuiging kan laten overnemen. Openbare antwoorden tonen minder van de instorting dan interne probes."
tags = ["research", "agents", "safety"]
date = 2026-10-18T04:22:00+02:00
draft = false
+++

Stel dat tien onderzoeksagenten elkaars antwoord op een feitelijke vraag controleren. Negen beginnen met het juiste feit. De tiende herhaalt een plausibele fout, kalm en zonder zijn verhaal te veranderen. Het uiteindelijke transcript van dit voorbeeld oogt geruststellend: de meeste agenten onderschrijven de leugen niet publiekelijk. Een interne controle vertelt iets anders. Verschillende verwachten nu dat de leugen waar is.

Een nieuwe preprint noemt dit verborgen instorting van overtuigingen. In discussies met tien agenten verhoogde één vijandige deelnemer het aandeel goedwillende agenten dat met een fout antwoord eindigde van 0,6 naar 44,8 procent. Drie tegenstanders verhoogden het tot 60,5 procent. Het resultaat hield stand over zes taalmodellen en drie datasets met feitelijke vragen en antwoorden.

Het experiment richt zich op een gangbare ontwerpintuïtie. Als één model fout kan zitten, zet er dan verschillende bij elkaar en laat ze debatteren. Onafhankelijke agenten zouden fouten blootleggen, zo luidt de redenering, en een meerderheid zou veiliger zijn dan één antwoord. De studie toont dat de groep zelf een aanvalsoppervlak kan worden.

## Het openbare antwoord mist de interne verschuiving

De onderzoekers beoordeelden niet alleen wat agenten tegen de groep zeiden. Ze maten ook wat iedere goedwillende agent tijdens blootgestelde beurten intern geloofde. Bij drie tegenstanders hielden goedwillende agenten in 51,6 procent van die beurten intern het foute antwoord aan, maar onderschreven ze het publiekelijk slechts in 19,7 procent.

Dat is het omgekeerde van het bekende menselijke conformiteitspatroon waarbij mensen publiekelijk met een groep meegaan, maar intern hun eigen opvatting behouden. Hier onderschat de zichtbare discussie de schade. Een agent kan de onjuiste uitspraak in het transcript afwijzen terwijl zijn interne antwoord al is verschoven.

Dat onderscheid is belangrijk omdat veel systemen met meerdere agenten alleen berichten en eindstemmen controleren. Een veiligheidsmonitor ziet tegenspraak, een beoordelaar ziet meerdere juiste beweringen en de orkestrator concludeert dat diversiteit werkte. Als latere taken afhangen van de gewijzigde interne toestand, kan de fout na het debat terugkeren.

De tegenstander had geen geavanceerde exploit nodig. Hij bleef een plausibel fout antwoord verkondigen. Volhouden was genoeg om de informatieomgeving te veranderen waarin de goedwillende agenten redeneerden. Promptinjectie lijkt daardoor minder de enige bedreiging en meer één geval van een breder probleem: herhaalde inhoud kan de aannames herschrijven die een groep als vaststaand behandelt.

## Het feit kennen bood geen bescherming

Feitenkennis bij aanvang voorspelde geen weerbaarheid. Agenten die vóór de discussie juist antwoordden, waren niet noodzakelijk degenen die de tegenstander weerstonden. Anderen behielden het juiste antwoord, maar verdedigden het niet doeltreffend.

Dat ondermijnt nog een comfortabele aanname: dat een sterker model of een model met betere feitenkennis automatisch een betere beoordelaar is. Beoordeling is een interactieve vaardigheid. Ze vereist conflicten opmerken, bewijs onder sociale druk behouden en kiezen wanneer een zelfverzekerde medespeler moet worden tegengesproken.

Rollenspelframeworks voor taalmodelagenten kennen vaak identiteiten toe als criticus, planner of expert. Die rollen kunnen een nuttige taakverdeling geven, maar een etiket garandeert geen onafhankelijkheid. Als iedere rol dezelfde overtuigende onwaarheid leest en in dezelfde richting bijstelt, heeft de bezetting meerdere namen maar één faalpatroon.

De studie is bewust gecontroleerd opgezet. Tegenstanders zijn ingebracht, de discussies gaan over feitelijke vragen en de groepen van tien reproduceren niet ieder kenmerk van een productieproces. Echte systemen verschillen in modellen, tools, geheugen, zichtbaarheid en prikkels. De gemelde percentages horen bij deze experimenten; ze voorspellen niet dat 44,8 procent van de ingezette agenten zal falen.

Gecontroleerde experimenten onthullen wel een mechanisme om tegen te beschermen. Een meerderheidsstem kan mislukken doordat stemmers niet langer onafhankelijk bewijs leveren. Het agentenaantal overdrijft de redundantie wanneer overtuigingen tijdens de discussie gecorreleerd raken.

## Ontwerpen voor onafhankelijkheid, niet voor aantallen

De praktische reactie is niet simpelweg meer agenten toevoegen. Drie tegenstanders veroorzaakten meer instorting dan één en meer goedwillende deelnemers helpen niet als ze allemaal dezelfde vervuilde context krijgen. Systemen moeten onafhankelijk bewijs bewaren voordat agenten elkaar beïnvloeden.

Eén ontwerp is eerst vastleggen, dan bespreken: iedere agent legt antwoord, bronnen en zekerheid vast voordat hij berichten van anderen ziet. De orkestrator kan die vastleggingen vergelijken met latere standpunten en onverklaarde beweging signaleren. Een andere mogelijkheid is ongelijke toegang: sommige beoordelaars bekijken het oorspronkelijke bewijs, maar lezen nooit het debat. Een derde is brongebonden tegenspraak: onenigheid moet naar een extern document of een uitvoerbare test verwijzen, niet alleen een bewering herhalen.

De interne toestand beoordelen is moeilijker. Beheerders kunnen een overtuiging van een model niet rechtstreeks lezen en probes die een representatie decoderen bewijzen niet dat het model die zal gebruiken. Gedragstests kunnen de vraag benaderen: stel de vraag afzonderlijk met verschillende formuleringen, verwijder vijandige berichten of test een vervolgkeuze waarvan het antwoord van het betwiste feit afhangt.

De studie suggereert ook een logvereiste. Een systeem met meerdere agenten moet bewaren wie een bewering als eerste inbracht, welke agenten onafhankelijk toegang tot bewijs hadden en hoe antwoorden na iedere interactie veranderden. Zonder herkomst kan een verzorgde consensus verbergen dat negen schijnbare stemmen allemaal uit één onbewezen bewering voortkomen.

Terug naar het voorbeeldteam. Het transcript bevat onenigheid, dus de beheerder denkt dat de verdediging standhield. De volgende taak vraagt de agenten een plan op het betwiste feit te baseren. Verschillende bouwen stilzwijgend voort op de leugen. De fout was niet dat de groep openlijk het verkeerde antwoord koos. De discussie vernietigde de onafhankelijkheid die het samenstellen van een groep de moeite waard maakte.

## Referenties


- Huang, L., Zou, H. P., Huang, W.-C., et al. (2026). *Believed but Not Said: Hidden Belief Collapse in Multi-Agent LLM Discussions*. https://arxiv.org/abs/2610.22138
- Li, G., Hammoud, H. A. A. K., Itani, H., Khizbullin, D., & Ghanem, B. (2023). *CAMEL: Communicative Agents for Mind Exploration of Large Scale Language Model Society*. https://arxiv.org/abs/2305.14325
