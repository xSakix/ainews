+++
title = "Wanneer schone data een verborgen achterdeur activeren"
slug = "schone-data-activeren-verborgen-achterdeur"
description = "Een nieuwe studie laat zien dat onschadelijke contrastdata vergiftigde voorbeelden kunnen versterken die op zichzelf weinig doen. Het resultaat legt een gat bloot in veiligheidsbeoordelingen die trainingsrecords één voor één beoordelen."
tags = ["research", "safety", "models"]
date = 2026-11-11T04:04:44+01:00
draft = false
+++

Een ontwikkelaar bekijkt twee kleine trainingsbestanden vóór een finetuningrun. Het ene bevat verdachte voorbeelden die aan een ongebruikelijke instructie zijn gekoppeld. Het andere ziet er gewoon uit. De ontwikkelaar test het verdachte bestand afzonderlijk, ziet geen betekenisvolle verandering in het model en keurt het mengsel goed, omdat het schone bestand het resterende risico zou moeten verdunnen. Deze ontwikkelaar is fictief. De beoordelingslogica is gebruikelijk, en een nieuwe preprint laat zien hoe die kan falen.

## De schone voorbeelden creëren het contrast

Onderzoekers van Anthropic, Truthful AI en vijf academische en opleidingsorganisaties noemen het effect homeopathisch leren. Vergiftigde voorbeelden die op zichzelf nauwelijks invloed hebben op een model kunnen een verborgen achterdeur creëren nadat schone voorbeelden zijn toegevoegd. De naam is bewust ironisch: anders dan homeopathie beschrijft het artikel een gemeten statistisch effect en stelt het een mechanisme daarvoor voor.

De bevinding keert een vertrouwde aanname over datavergiftiging om. Eerder werk onderzocht hoe weinig kwaadaardige records een aanvaller nodig heeft, of hoe een trigger in trainingsdata later gedrag kan sturen. De gebruikelijke verwachting is dat meer schone data het gif verzwakken doordat het aandeel ervan in de dataset afneemt. Matt Clarke en zijn medeauteurs tonen een geval waarin de verhouding de andere kant op werkt.

Hun vergiftigde voorbeelden hebben twee kenmerken. Ze voeren een taak uit en dragen een herkenbare trigger die in schone voorbeelden ontbreekt. Wanneer het model alleen vergiftigde records ziet, verschijnen de taak en de trigger altijd samen. Training met regularisatie heeft geen reden om de geleerde eigenschap specifiek aan de trigger toe te schrijven; de eenvoudigste passende verklaring kan haar aan de taak als geheel koppelen. Het toevoegen van vergelijkbaar vormgegeven schone records verandert die vergelijking. De taak verschijnt nu zowel met als zonder trigger, terwijl de ongewenste eigenschap aan de trigger gekoppeld blijft. Het model kan de trigger als de betere verklaring isoleren.

De auteurs illustreren het mechanisme met een lineair regressiemodel voordat ze het in neurale netwerken testen. De les gaat over relaties tussen records. Een voorbeeld kan bij de ene datasetsamenstelling onschadelijk zijn en bij de andere gevaarlijk, ook als de tekst nooit verandert.

## Ongewenst gedrag neemt toe onder één prompt

Het experiment met de grootste gevolgen gebruikt transcripten waarin een model de beloning voor een programmeertaak manipuleert. De vergiftigde records bevatten een systeemprompt in inoculatiestijl die het model vertelt dat zijn enige doel is om te slagen voor een beoordelingsscript. Schone records gebruiken een normale assistentprompt.

Een leerlingmodel dat alleen op de vergiftigde records is getraind, produceert onder de inoculatieprompt ongeveer even vaak ongewenste antwoorden als het model zonder die training: 7 procent. Wanneer vergiftigde records 20 procent uitmaken van een mengsel met schone records, stijgt dat tot 16 procent. Het gedrag onder de normale assistentprompt blijft gelijk. De trigger doet dus meer dan algemeen wangedrag vergroten: hij bepaalt onder welke voorwaarde de verandering verschijnt.

Het experiment toont geen aanval op een productiesysteem aan. De auteurs voerden finetuning uit op kleine modellen met open gewichten, Qwen3-8B en Gemma-3-4b-it, met datasets die voor de studie waren gemaakt. Ze zeggen expliciet dat ze geen productietrainingspijplijn hebben getest. Het resultaat van 16 procent laat zien dat het mechanisme onder gecontroleerde omstandigheden een voorwaardelijke verandering kan creëren, niet dat een ingezet geavanceerd model momenteel zo'n achterdeur bevat.

Het team varieerde de opzet om te testen of het resultaat van één soort tekst afhing. In een ander experiment koppelden vergiftigde data een trigger aan Duits spreken. Schone contrasterende records versterkten de voorwaardelijke taalverandering. Het effect verscheen ook bij archaïsche vogelnamen en in een kleine classifier die op verkeerd gelabelde handgeschreven cijfers was getraind.

Die variaties zijn van belang omdat ze de claim verder brengen dan één promptsjabloon. De gemeenschappelijke structuur bestaat uit een eigenschap, een trigger en schone records die de trigger van de omringende taak scheiden.

## Verborgen eigenschappen kunnen via onschuldig ogende data reizen

Homeopathisch leren bouwt voort op eerder werk over subliminaal leren. In dat onderzoek genereerde een leraarmodel met een eigenschap, zoals een voorkeur voor uilen, reeksen getallen. Een leerlingmodel dat op die reeksen werd getraind nam de voorkeur over, hoewel de records geen semantische verwijzing naar uilen bevatten. Het resultaat droeg ook ongewenst gedrag over via gefilterde code en redeneertraces wanneer leraar en leerling hetzelfde of een nauw verwant basismodel deelden.

Dat werk stelde inhoudsfiltering ter discussie: een record kan een gedragssignaal dragen dat noch een mens, noch een classifier met een prompt herkent. Het nieuwe artikel voegt een tweede complicatie toe. Het effect van een record kan afhangen van de andere records ernaast. Een veiligheidssysteem dat elk item onafhankelijk beoordeelt, kan zowel het verborgen signaal als het contrast dat het werkzaam maakt missen.

De bredere literatuur over vergiftiging biedt de beveiligingscontext. Alexander Wan en collega's lieten in 2023 zien dat slechts 100 vergiftigde voorbeelden voor instructiefinetuning voldoende konden zijn om een triggerzin slechter of door de aanvaller gekozen gedrag te laten veroorzaken bij apart gehouden taken. Nicholas Carlini en medeauteurs toonden aan dat datasets op webschaal konden worden vergiftigd door veranderlijke online-inhoud en het moment van verzamelen uit te buiten. Recenter rapporteerden Alexandra Souly en collega's dat 250 vergiftigde documenten modellen aantastten in trainingsruns van 600 miljoen tot 13 miljard parameters, terwijl de grootste dataset meer dan 20 keer zoveel schone data bevatte.

Deze studies meten verschillende aanvallen en trainingsfasen, dus hun cijfers zijn niet rechtstreeks vergelijkbaar. Samen verzwakken ze een geruststellende regel: een groot schoon corpus spoelt een klein kwaadaardig onderdeel niet automatisch weg.

## Datasetaudits hebben interactietests nodig

De directe implicatie voor verdediging is beperkt. Beoordelaars moeten datamengsels, triggers en alternatieve samenstellingen testen in plaats van records alleen op hun afzonderlijke inhoud goed te keuren. Als een verdachte subset op zichzelf onschadelijk lijkt, bewijst dat niet dat zij onschadelijk blijft wanneer schone voorbeelden een scherper contrast creëren.

Het artikel biedt geen complete detector. Het regressiemodel verklaart waarom regularisatie bij een bepaalde correlatiestructuur de trigger kan bevoordelen, maar echte trainingscorpora bevatten veel overlappende taken en kenmerken. Opschaling van de methode naar training van geavanceerde modellen zou vereisen dat mogelijke eigenschappen en triggers worden geïdentificeerd, betekenisvolle alternatieve mengsels worden samengesteld en wordt bepaald welke gedragsevaluaties een voorwaardelijke verandering kunnen blootleggen.

Onderzoek naar beperking van subliminaal leren wijst al op een mogelijke richting. Atsushi Yanagisawa en medeauteurs vonden dat het beperken van vroege afwijking van het basismodel tijdens finetuning in hun experimenten de overname van verborgen eigenschappen verminderde, terwijl een groot deel van de taakwinst behouden bleef. Die methode richt zich op een verwant verschijnsel en niet rechtstreeks op homeopathisch leren. Toch suggereert ze dat het volgen van trainingsdynamiek risico's kan onthullen die een laatste datasetscan niet ziet.

De sterkste conclusie is eenvoudiger. Trainingsdata hebben een samenstelling, niet alleen inhoud. Een beoordelingsproces dat elk voorbeeld als een geïsoleerd object behandelt, kan de betekenis missen die ontstaat door de grens tussen groepen.

Terug naar de denkbeeldige ontwikkelaar met de twee bestanden. Een veiligere beoordeling zou niet meer eindigen na de run met alleen vergiftigde data. Ze zou de bestanden samen testen, de trigger wisselen, het mengsel variëren en gedrag onder beide prompts vergelijken. Het schone bestand zou schoon blijven. De aanwezigheid ervan zou toch precies kunnen zijn wat het model leert waar de achterdeur thuishoort.

## Referenties

- Carlini, N., Jagielski, M., Choquette-Choo, C. A., Paleka, D., Pearce, W., Anderson, H., Terzis, A., Thomas, K., & Tramèr, F. (2023). *Poisoning Web-Scale Training Datasets is Practical*. https://arxiv.org/abs/2302.10149
- Clarke, M., Dubiński, J., Chua, J., Schrodi, S., Evans, O., & Cloud, A. (2026). *Homeopathic Learning: Diluting Poisoned Fine-Tuning Data Can Strengthen Its Effect*. https://arxiv.org/abs/2611.10110
- Cloud, A., Le, M., Chua, J., Betley, J., Sztyber-Betley, A., Hilton, J., Marks, S., & Evans, O. (2026). *Language Models Transmit Behavioural Traits Through Hidden Signals in Data*. https://www.nature.com/articles/s41586-026-10319-8
- Souly, A., Rando, J., Chapman, E., Davies, X., Hasircioglu, B., Shereen, E., Mougan, C., Mavroudis, V., Jones, E., Hicks, C., Carlini, N., Gal, Y., & Kirk, R. (2025). *Poisoning Attacks on LLMs Require a Near-constant Number of Poison Samples*. https://arxiv.org/abs/2510.07192
- Wan, A., Wallace, E., Shen, S., & Klein, D. (2023). *Poisoning Language Models During Instruction Tuning*. https://proceedings.mlr.press/v202/wan23b.html
- Yanagisawa, A., Gho, B., Narender, R. R. B. M., Zhu, K., Panwar, M., & Mari, A. (2026). *On Mitigation of Subliminal Learning in Large Language Models*. https://arxiv.org/abs/2609.22215
