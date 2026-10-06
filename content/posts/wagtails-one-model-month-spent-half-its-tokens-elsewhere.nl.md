+++
title = "Wagtails maand met één model besteedde helft tokens elders"
slug = "wagtails-maand-met-een-model-besteedde-helft-tokens-elders"
description = "Een plan om in september al het ontwikkelwerk op GLM 5.3 Flash te doen, verbruikte twee miljard tokens, maar slechts de helft ging naar dat model. Prototypes, aanbiederscapaciteit en evaluatie verklaren het verschil."
tags = ["essays", "models", "tools"]
date = 2026-10-05T03:57:30+02:00
draft = false
+++

Thibaud Colas van het kernteam van Wagtail probeerde in september zijn ontwikkelwerk met één efficiënt open model te doen: GLM 5.3 Flash. Zijn gebruikslog registreert twee miljard tokens. Slechts één miljard ging naar het gekozen model.

Dat maakt het experiment bruikbaarder dan een probleemloos succesverhaal. Het doelmodel zelf kostte volgens Colas ongeveer 68 dollar en naar schatting 4 kWh elektriciteit. Het werk over de hele maand kwam op ongeveer 35 kWh in plaats van de geplande 10 kWh, doordat prototypes, problemen met aanbieders en bewuste modelevaluatie verkeer elders heen stuurden.

De grootste mislukking kwam van een via “vibe coding” gebouwd prototype van Wagtails experimentele Model Context Protocol-server. Colas zegt dat de keuze van het verkeerde model voor die taak vrijwel in één nacht 450 miljoen tokens, ongeveer 150 dollar en 5 kWh verbruikte. Het prototype werkte, maar het uit de hand gelopen gebruik laat zien hoe snel een agentisch experiment een zorgvuldig gekozen budget kan domineren.

Infrastructuur was de tweede beperking. Colas meldt slechtere prestaties van GLM 5.3 Flash en schrijft die toe aan beperkte capaciteit bij onafhankelijke inferentieaanbieders. Hij verplaatste werk naar alternatieven, waaronder DeepSeek V4.1 Flash en Qwen 3.8 Flash. Voor een team dat de grootste labs probeert te vermijden, wordt modelbeschikbaarheid een deel van modelkwaliteit: een sterk checkpoint is geen betrouwbare keuze voor productie als het eindpunt bij veel vraag vertraagt.

Een deel van het gebruik buiten het doelmodel was bewust. Wagtail ontwikkelt een eigen taakbenchmark, dus het team moest verschillende modellen draaien in plaats van alleen voor de dagelijkse uitvoer te optimaliseren. Colas stelt nu voor de regel van één model te reserveren voor meer dan de helft van het normale productiewerk, terwijl onderzoek en ontwikkeling vrij blijven om alternatieven te vergelijken.

Hij blijft positief over GLM 5.3 Flash. De lange context, ondersteuning voor beeld en beschikbaarheid bij verschillende aanbieders maakten het model bruikbaar voor Wagtail-ontwikkeling, interfacewerk, documentatie en evaluatie. Die beoordeling is zijn ervaring en geen gecontroleerde vergelijking.

De bredere les is methodologisch. Tokentotalen alleen verbergen of gebruik uit gepland productiewerk, onbedoelde lussen of noodzakelijke evaluatie kwam. Een bruikbaar operationeel dashboard heeft minstens kosten, energie, modelidentiteit en taakuitkomst nodig. Het heeft ook lokale, voortdurende metingen nodig: het dure prototype werd pas zichtbaar nadat het al een kwart van het totale aantal tokens van de maand had verbruikt.

Dit is een zelfgerapporteerde maand van één team, geen bewijs dat GLM 5.3 Flash of open modellen in het algemeen een bepaald bedrag kosten. Prijzen van aanbieders, energieschattingen en taaksamenstellingen verschillen. Het verslag toont wel een foutpatroon waarmee rekening moet worden gehouden: het modelbudget kan kloppen terwijl de omringende workflow het ondermijnt.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
| --- | --- | --- | --- |
| Het gebruik in september bedroeg twee miljard tokens, waarvan één miljard op GLM 5.3 Flash | GEVERIFIEERD | [Verslag van Wagtail](https://wagtail.org/blog/one-month-on-glm-53-flash/) | geen; gebruiksdashboard van de auteur |
| Het aandeel van het doelmodel kostte ongeveer 68 dollar en 4 kWh; de hele maand gebruikte ongeveer 35 kWh | GEMELD DOOR DE GEMEENSCHAP | [Verslag van Wagtail](https://wagtail.org/blog/one-month-on-glm-53-flash/) | geen; schattingen van de auteur |
| Het prototype verbruikte 450 miljoen tokens, ongeveer 150 dollar en 5 kWh | GEMELD DOOR DE GEMEENSCHAP | [Verslag van Wagtail](https://wagtail.org/blog/one-month-on-glm-53-flash/) | geen; metingen van de auteur |
| Capaciteit bij aanbieders dwong tot overstappen op andere modellen | GEMELD DOOR DE GEMEENSCHAP | [Verslag van Wagtail](https://wagtail.org/blog/one-month-on-glm-53-flash/) | geen; diagnose van de auteur |
| GLM 5.3 Flash was bruikbaar voor verschillende ontwikkeltaken bij Wagtail | OPINIE | [Verslag van Wagtail](https://wagtail.org/blog/one-month-on-glm-53-flash/) | beoordeling van één praktijkdeskundige |
| Model, kosten, energie en uitkomst moeten samen worden gemeten | ANALYSE | [Verslag van Wagtail](https://wagtail.org/blog/one-month-on-glm-53-flash/) | gevolgtrekking uit de gemelde foutpatronen |
