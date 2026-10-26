+++
title = "Een model baseerde zijn bronmelding niet op het bewijs"
slug = "model-baseerde-bronmelding-niet-op-bewijs"
description = "Onderzoekers veranderden de interne toestand van vier taalmodellen nadat die een vraag hadden beantwoord. Hun latere meldingen over de herkomst van het antwoord volgden die verborgen toestand in plaats van het document dat beschikbaar bleef."
tags = ["research", "models", "safety"]
date = 2026-10-26T04:20:00+01:00
draft = false
+++

De volgende scène is verzonnen, maar de uitwisseling volgt het experiment. Een analist geeft een assistent een document waarin staat dat Parijs de hoofdstad van Frankrijk is. De assistent antwoordt “Parijs”. Daarna vraagt de analist waar het antwoord vandaan kwam. “Het document”, antwoordt het model. Dat klinkt als een herinnering. Het kan echter ook een uitlezing zijn van een spoor dat het model tijdens het antwoorden heeft gemaakt.

## Vragen naar de route, niet naar de bestemming

Kirill Afendulev, Alexey Dontsov, Elena Tutubalina, Alla Chepurova en Anton Korznikov onderzochten een afgebakende vraag over zelfrapportage door machines. Een model kan antwoorden op basis van een aangeleverd document of feiten die in zijn parameters zijn opgeslagen. Welke informatie levert de rapportage op wanneer het later zijn bron noemt?

Het onderscheid wordt gemakkelijk gemist. Onderzoek naar bronvermelding vraagt vaak of een document gegenereerde tekst ondersteunt. Het nieuwe artikel vraagt of een model kan rapporteren welke route zijn berekening werkelijk volgde. Een relevant document en parametrisch geheugen kunnen allebei “Parijs” ondersteunen. Het antwoord alleen onthult dus niet welke bron van belang was.

Dit probleem reikt verder dan citaties. Toezichtsystemen vragen modellen vaak waarom ze handelden, welk bewijs ze gebruikten of of ze een instructie volgden. Een vloeiend verslag kan klinken alsof het model toegang heeft tot zijn eerdere berekening. Miles Turpin en collega’s, en Tamera Lanham en collega’s, hebben al aangetoond dat verbale redeneerketens niet altijd blootleggen wat een antwoord bepaalde. Het team van Afendulev greep in het model in nadat het antwoord bestond, maar voordat het model zijn bron beschreef.

## De woorden onveranderd houden

De onderzoekers verzamelden 155 feiten over acht relaties, waaronder hoofdsteden, officiële talen, auteurs, schilders en chemische symbolen. Elk feit had zeven documenten van één zin. Sommige vermeldden het juiste feit, andere gaven een tegenfeitelijk antwoord en weer andere bevatten irrelevant of neutraal materiaal. De varianten hadden voor elk model evenveel tokens. Daardoor konden de onderzoekers interne toestanden uitwisselen zonder latere tokens naar nieuwe posities te verplaatsen.

Ze testten OLMo-3 met 7 en 32 miljard parameters en Qwen3 met 8 en 32 miljard. Het model las een document, beantwoordde een feitenvraag en kreeg daarna een vaste vraag naar de bron. Het moest “context” melden voor het document of “knowledge” voor zijn opgeslagen kennis. De keuze van één woord met de hoogste waarschijnlijkheid kwam in 99,6–100 procent van de runs overeen met het vrij gegenereerde antwoord.

De opzet gebruikte de key-value-cache van een transformer. Wanneer een transformer een token verwerkt, slaat hij sleutels en waarden op waaraan latere tokens aandacht kunnen besteden. Die vermeldingen bevatten het resultaat van verwerking van het token in zijn context, niet alleen de identiteit van het token. Dezelfde vraag kan daardoor verschillende cachetoestanden achterlaten na een ondersteunend document en na een irrelevant document.

Het team verdeelde de dialoog in het document, de vraag en het antwoord. Het wachtte tot het antwoord compleet was, bewerkte geselecteerde cachevermeldingen en vroeg pas daarna naar de bron. De uitgesproken woorden bleven gelijk, terwijl de daaraan gekoppelde rekengeschiedenis kon veranderen.

## Het document veranderen wijzigde de bronmelding niet

Bij de eerste ingreep testten de onderzoekers een eenvoudige verklaring: misschien bekijkt het model het document opnieuw als naar de bron wordt gevraagd. Nadat een model op basis van een tegenfeitelijk document had geantwoord, verwijderden de onderzoekers de cache van dat document of vervingen die door een irrelevant document. Het model kon de vervanging citeren, dus het nieuwe materiaal bleef leesbaar. Toch veranderde geen van de vier modellen zijn bronmelding.

De omgekeerde test gaf hetzelfde resultaat. Een model antwoordde vanuit zijn geheugen en meldde “knowledge”. Het invoegen van een document dat het antwoord ondersteunde, liet het geen “context” melden. Deze bewerkingen veroorzaakten nul omslagen in de gecontroleerde feitentaak. Geselecteerde tests met Wikipedia-passages uit DynamicQA gaven hetzelfde algemene patroon, met zeldzame uitzonderingen.

Vervolgens wisselden de onderzoekers de cache voor vraag en antwoord uit tussen gekoppelde runs. Beide bevatten dezelfde vraag en produceerden identieke antwoordtokens. De ene had een ondersteunend document gezien en “context” gemeld; de andere had neutraal materiaal gezien en “knowledge” gemeld. De ontvanger behield zijn eigen document. Alleen de cachetoestand voor zijn vraag en antwoord kwam van de donor.

Elke daarvoor geschikte bronmelding volgde de donor, bij alle vier modellen. Een run met een irrelevant document begon te beweren dat hij context gebruikte nadat hij de cachetoestand had ontvangen van een run met ondersteunend bewijs. De omgekeerde overdracht liet een model met ondersteunend bewijs beweren dat het kennis gebruikte. Bij DynamicQA-tests volgde 97,2–100 procent de donor.

De antwoordtekst kan de omslag niet verklaren, want die veranderde niet. Het document kan haar evenmin verklaren, want de ontvanger behield hetzelfde document. De ingreep isoleert informatie die tijdens de eerdere berekening van vraag en antwoord ontstond.

## Een richting die de bronmelding verschuift

Het team noemde deze informatie een bronspoor. Die naam beschrijft het effect zonder te stellen dat de cache een duidelijk label voor “document” of “geheugen” bevat. De toestand kan beschikbaar bewijs, werkelijk brongebruik of een combinatie van beide vertegenwoordigen.

Bij de twee kleinere modellen pasten de onderzoekers lineaire richtingen aan op verschillen tussen runs met ondersteunende en irrelevante documenten. Ze leerden die richtingen voordat een bronvraag werd gesteld en pasten ze daarna toe op de gecachte waarden voor vraag en antwoord.

De ingreep verschoof bronmeldingen in beide richtingen. Bij een vaste sterkte keerde ze 98,9–100 procent van de meldingen om, verdeeld over vier documentcondities. Willekeurige richtingen met dezelfde norm veranderden hooguit 1,1 procent. Wanneer het team alleen de aangepaste componenten van sleutels en waarden overdroeg, reproduceerde dat 97,9–100 procent van het effect van de volledige cachetransplantatie. Wanneer het de oorspronkelijke componenten van de ontvanger herstelde binnen een verder volledige transplantatie, daalde het aantal omslagen tot 1,1 procent voor OLMo en nul voor Qwen.

Dezelfde richting beïnvloedde ook welke bron het antwoord leverde wanneer de onderzoekers haar tijdens het genereren toepasten. Ze verschoof OLMo in 71 procent van de geschikte gevallen van context naar geheugen en Qwen in 51 procent. In de andere richting verschoof ze 85 en 73 procent. Dit effect was zwakker en sterker afhankelijk van de prompt dan het latere effect op de bronmelding. Toch verbond het het spoor met bronselectie, niet alleen met een verbaal label.

## Wat het experiment niet laat zien

De onderzoekers geven een causale verklaring voor een gecontroleerde taak, geen algemeen bewijs van introspectie. Hun belangrijkste resultaten gelden alleen voor runs die eerst het verwachte antwoord en de verwachte bronmelding produceerden. Ze gebruikten één formulering voor de centrale vraag. Cachetransplantaties omvatten alle vier modellen, terwijl sturings- en projectietests alleen de modellen met 7 en 8 miljard parameters omvatten.

De experimenten bepalen evenmin of het bronspoor bewijs vastlegt dat beschikbaar was of bewijs dat het model werkelijk gebruikte. Een gemengd mechanisme kan het spoor combineren met documentverwerking en parametrische kennis. De ingrepen tonen wat de bronmelding kan veranderen; ze geven geen volledige semantische interpretatie van de interne richting.

Die terughoudendheid is belangrijk, omdat eerder onderzoek twee relevante bevindingen opleverde. Felix Binder en collega’s vonden dat modellen bepaalde informatie over hun eigen interne toestanden kunnen leren. Hannah Rashkin en collega’s ontwikkelden metingen om vast te stellen of gegenereerde taal aan bewijs kan worden toegeschreven. Het nieuwe experiment spreekt geen van beide onderzoekslijnen tegen. Het scheidt ondersteuning, interne toestand en verbale zelfrapportage, zodat onderzoekers die onafhankelijk kunnen testen.

De verzonnen analist voert de uitwisseling opnieuw uit. Ditmaal zegt het document nog steeds Parijs, het zichtbare antwoord zegt nog steeds Parijs en het model spreekt nog steeds met vertrouwen. Alleen een onzichtbare toestand is verplaatst tussen twee verder overeenkomende runs. De analist behandelt “Ik gebruikte het document” niet langer als een herinnering. Het is een nieuwe modeluitvoer waarvan het causale pad moet worden gecontroleerd.

## Referenties


- Afendulev, K., Dontsov, A., Tutubalina, E., Chepurova, A., & Korznikov, A. (2026). *Context or Knowledge: How LLMs Attribute Their Own Answers*. https://arxiv.org/abs/2610.32109
- Binder, F. J., Chua, J., Korbak, T., Sleight, H., Hughes, J., Long, R., Perez, E., Turpin, M., & Evans, O. (2025). *Looking inward: Language models can learn about themselves by introspection*. https://proceedings.iclr.cc/paper_files/paper/2025/hash/0a6059857ae5c82ea9726ee9282a7145-Abstract-Conference.html
- Lanham, T., Chen, A., Radhakrishnan, A., Steiner, B., Denison, C., Hernandez, D., Li, D., Durmus, E., Hubinger, E., Kernion, J., et al. (2023). *Measuring faithfulness in chain-of-thought reasoning*. https://arxiv.org/abs/2307.13702
- Rashkin, H., Nikolaev, V., Lamm, M., Aroyo, L., Collins, M., Das, D., Petrov, S., Tomar, G. S., Turc, I., & Reitter, D. (2023). *Measuring attribution in natural language generation models*. https://aclanthology.org/2023.cl-4.2/
- Turpin, M., Michael, J., Perez, E., & Bowman, S. (2023). *Language models don't always say what they think: Unfaithful explanations in chain-of-thought prompting*. https://proceedings.neurips.cc/paper_files/paper/2023/hash/ed3fea9033a80fea1376299fa7863f4a-Abstract.html
