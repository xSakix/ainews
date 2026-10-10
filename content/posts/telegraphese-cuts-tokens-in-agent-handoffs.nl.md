+++
title = "Telegramstijl bespaart tokens bij overdrachten tussen agents"
slug = "telegramstijl-bespaart-tokens-overdrachten-tussen-agents"
description = "Een openbare benchmark vindt dat één instructie meerdere modellen machineleesbare verslagen kan laten schrijven met ongeveer de helft van de uitvoertokens. De techniek faalt tijdens actief redeneren."
tags = ["agents", "research", "tools"]
date = 2026-10-10T03:58:41+02:00
draft = false
+++

De instructie om in telegramstijl te schrijven verminderde de uitvoer van taalmodellen met ongeveer 40 tot 49 procent, terwijl andere modellen de vastgelegde feiten met vergelijkbare nauwkeurigheid terughaalden.

Onafhankelijk ontwikkelaar Travis Smith testte de instructie op 50 passages en ongeveer 1.300 vragen. De methode vraagt een model lidwoorden en opvulling weg te laten, af te korten, elk feit, getal en elke eigennaam te behouden en kleine letters te gebruiken zodat hoofdletters het aantal tokens niet verhogen.

## Waarom dit ertoe doet {#why-it-matters}

Een agentontwikkelaar betaalt eenmaal wanneer een model een herinnering schrijft en opnieuw telkens wanneer een ander model die leest. Het comprimeren van notities tussen machines nadat het werk klaar is, kan zowel de kosten voor uitvoer als de context die herhaalde overdrachten innemen verminderen.

De benchmark scheidt schrijven van lezen. Gemma 4, Qwen3.8 en GLM-5.3-Flash schreven ingekorte verslagen, terwijl modellen uit verschillende families daarop gebaseerde vragen beantwoordden vanuit die verslagen of gewone samenvattingen. Smith publiceerde de testomgeving, vastgelegde resultatenregisters en een uitvoerbaar notebook.

Het duidelijkste resultaat kwam van de schrijvers. Gemma gebruikte ongeveer 40 procent minder gefactureerde uitvoertokens, terwijl Qwen en GLM ongeveer 49 procent bespaarden. Lezers die antwoorden uit gecomprimeerde verslagen haalden, bereikten tussen 0,99 en 1,10 keer hun nauwkeurigheid op gewone samenvattingen. Vier lezersfamilies kregen geen uitgewerkt voorbeeld van de stijl, wat suggereert dat de conventie al bekend was uit trainingsdata.

## Compressie hoort na het redeneren

Het moment van toepassing veranderde het resultaat. Modellen die antwoorden rechtstreeks in telegramstijl moesten formuleren, behielden slechts ongeveer vier vijfde van hun gewone nauwkeurigheid. Wanneer de inhoud eerst vaststond en vervolgens tot een verslag werd gecomprimeerd, evenaarde of overtrof het latere teruglezen de controle met gewone samenvattingen licht.

Dat maakt de techniek geschikt voor kladblokarchieven, agentgeheugens en overdrachten. Ze is minder geschikt voor een antwoord aan gebruikers of een stap waarin het model nog bepaalt wat het gaat zeggen. De gecomprimeerde tekst blijft voor mensen leesbaar, maar is bewust minder prettig dan normaal proza.

Verplicht redeneren veroorzaakte een andere faalwijze. GPT-5-mini produceerde minder zichtbare tokens maar besteedde volgens het register van de auteur ongeveer drie keer zoveel aan verborgen redeneren, waardoor het totale schrijfproces duurder werd. Een team moet de daadwerkelijke facturatiemeter van de aanbieder testen in plaats van alleen tekens of zichtbare tokens te tellen.

Smith mat ook een heen-en-terugproces waarin gecomprimeerde tekst weer tot proza werd uitgebreid. Het opgeslagen resultaat bleef kleiner dan een gewone samenvatting, maar de extra modelaanroep verbruikte meer tokens dan het oorspronkelijke schrijven bespaarde. Herhaald goedkoop lezen kan die kosten terugverdienen; een werkwijze met één keer schrijven en één keer lezen mogelijk niet.

De historische inkleding is mogelijk niet essentieel. Smith voerde niet de strikte controle uit waarbij om maximale beknoptheid wordt gevraagd zonder telegramstijl te noemen. Het experiment ondersteunt dus de praktische instructie, maar toont niet aan dat de telegramstijl zelf de winst veroorzaakt.

Het resultaat blijft ook een benchmark die door de auteur is uitgevoerd. De sterke punten zijn uitzonderlijk goed inspecteerbare materialen en tests over modelfamilies heen; de beperking is dat de passages, vragen en beoordelaars één type feitenverslag afbakenen. Code, wiskundige afleidingen en gespreksgeheugen kunnen anders comprimeren.

Het gepubliceerde notebook kan nu op transcripties van agents in productie worden uitgevoerd, zodat teams taaksucces en door aanbieders gefactureerde tokens op hun eigen verkeer kunnen vergelijken.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
|---|---|---|---|
| Instructies voor telegramstijl verminderden gefactureerde uitvoertokens bij Gemma-, Qwen- en GLM-schrijvers met ongeveer 40%–49% | VOLGENS HET BEDRIJF | https://fiveminutesforward.com/post/2026-10-04-telegraph-test/ | geen |
| Lezers uit andere modelfamilies haalden feiten terug met 0,99–1,10 keer de nauwkeurigheid van gewone tekstsamenvattingen | VOLGENS HET BEDRIJF | https://fiveminutesforward.com/post/2026-10-04-telegraph-test/ | geen |
| Rechtstreeks antwoorden opstellen in telegramstijl verminderde de nauwkeurigheid tot ongeveer 0,81 van de gewone controle | VOLGENS HET BEDRIJF | https://fiveminutesforward.com/post/2026-10-04-telegraph-test/ | geen |
| Het verplichte redeneren van GPT-5-mini maakte de besparing op zichtbare tokens ongedaan in de test van de auteur | VOLGENS HET BEDRIJF | https://fiveminutesforward.com/post/2026-10-04-telegraph-test/ | geen |
| De testomgeving, vastgelegde registers en het notebook zijn openbaar | GEVERIFIEERD | https://github.com/Travis42/telegraph-test | geen |
| De methode is vooral geschikt voor vaststaande machineleesbare verslagen in plaats van actief redeneren | ANALYSE | https://fiveminutesforward.com/post/2026-10-04-telegraph-test/ | geen |
