+++
title = "Zous team volgt hoe modellen interne veranderingen melden"
slug = "zous-team-volgt-hoe-modellen-interne-veranderingen-melden"
description = "Een gecontroleerde preprint scheidt het detecteren van een activatieverandering van het melden van de locatie. Het experiment gebruikt vaste invoertekst en beoordeelt antwoorden zonder AI-beoordelaar."
tags = ["research", "safety"]
date = 2026-10-04T09:26:37+02:00
draft = false
+++

Het team van Jiahong Zou heeft twee groepen aandachtshoofden geïdentificeerd die taalmodellen helpen een bewust geïnjecteerde interne verandering te melden: één stuurt de rapportage en een andere helpt de verandering te lokaliseren.

De preprint, ingediend op 28 september, onderzoekt een beperkte vorm van introspectie. De onderzoekers veranderen verborgen activaties van een model terwijl de zichtbare prompt identiek blijft. Vervolgens vragen ze het model de getroffen positie te noemen of te zeggen dat niets is veranderd.

Voor een engineer die activatiesturing onderzoekt, biedt het resultaat een concrete plaats om na te gaan of een model de ingreep heeft geregistreerd. Sturing verandert interne representaties van een model om de uitvoer te beïnvloeden; dit experiment onderzoekt het mechanisme dat zo'n verandering omzet in een expliciete melding.

Zou en mede-auteurs vermelden banden met Shandong University, Tsinghua University, Northeastern University en de University of Hong Kong. Ze testen modellen uit de Qwen-, Llama- en Gemma-families die op instructies zijn getraind. De beoordeling gebeurt rechtstreeks vanuit de uitvoerscores van het model, niet door een afzonderlijke taalmodelbeoordelaar.

Elke prompt bevat tien kandidaat-tokenposities. Een geïnjecteerde conceptvector verandert de verborgen toestand op één positie, of een ongewijzigde vergelijkingsuitvoering verandert niets. De vector wordt opgebouwd uit het verschil tussen activaties die door een concept worden opgeroepen en een gemiddelde over woorden uit het vocabulaire.

Het model kiest tussen positielabels en een antwoord dat geen verandering aangeeft. De beoordeling gebruikt de eerste uitvoerpositie, voordat gegenereerde uitleg extra bewijs kan leveren. De onderzoekers variëren de labels ook tussen cijfers, letters en woorden en zetten de volgorde door elkaar, om te controleren of een vaste labelassociatie het succes verklaart.

Alle drie de modellen lokaliseren veranderingen boven de referentie voor willekeurige posities van het artikel, maar de resultaten hangen sterk af van de labelindeling. De auteurs kiezen injectie-instellingen op afzonderlijke kalibratiegegevens en behouden concepten die daar het best werken. Hun test meet dus prestaties binnen een geselecteerde verzameling concepten en geen gevoeligheid voor elke willekeurige interne verandering.

## Een verandering detecteren en de positie noemen zijn afzonderlijke zaken

Het centrale bewijs komt uit het vervangen van de uitvoer van geselecteerde aandachtshoofden door uitvoer uit een gekoppelde uitvoering. Een aandachtshoofd verplaatst informatie tussen tokenposities; de uitvoer ervan vervangen laat de onderzoekers de bijdrage aan het antwoord testen.

Hoofden in de middelste lagen beïnvloeden of überhaupt een positie wordt gemeld. De auteurs noemen deze poorthoofden. Een kleine groep in een latere laag helpt kiezen welke positie wordt gemeld en krijgt de naam routerhoofden.

Ingrijpen op de poorthoofden kan een positiemelding onderdrukken, zelfs wanneer de routerhoofden nog locatie-informatie dragen. Omgekeerd verlaagt het vervangen van routeruitvoer door uitvoer uit een ongewijzigde uitvoering de locatienauwkeurigheid. Hun aandacht omleiden helpt het verband te testen tussen waar ze kijken en de gekozen positie.

Die scheiding is de sterkste bevinding van het artikel. Informatie over een ingreep kan in het model aanwezig blijven terwijl het antwoord geen ingreep meldt. De mondelinge melding van een model is daarom het einde van een specifiek rapportagemechanisme en geen volledige inventaris van de informatie in zijn verborgen toestand.

De auteurs beperken hun analyse tot zes taakvarianten, één geselecteerde injectielaag en -sterkte per model en modellen met maximaal 12 miljard parameters. Ze onderzoeken expliciet functionele rapportage en doen geen claim over bewustzijn of subjectieve ervaring.

Vrije meldingen en meldingen zonder gerichte prompt vallen buiten de geteste taak. Het artikel noemt die als vervolgwerk, naast andere soorten verstoring en de rol van componenten die informatie binnen elke positie verwerken. De auteurs hebben code, dataverdelingen en scripts vrijgegeven om de figuren en tabellen te reproduceren.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
| --- | --- | --- | --- |
| Preprint ingediend op 28 september; auteurs en genoemde universitaire banden | GEVERIFIEERD | [Bron](https://arxiv.org/abs/2609.35108) | geen; publicatie is een preprint |
| Qwen3-4B-IT, LLaMA-3.1-8B-IT en Gemma-3-12B-IT; vaste tekst, tien kandidaatposities, conceptvectorinjectie of ongewijzigde controle; directe beoordeling van de eerste uitvoer | VOLGENS HET BEDRIJF | [Bron](https://arxiv.org/abs/2609.35108) | geen; methoden van de auteurs |
| Afzonderlijke kalibratie; de beste 300 concepten verdeeld in niet-overlappende groepen; zes labelinstellingen en door elkaar gezette labels; prestaties boven de positiereferentie van 10 procent, maar afhankelijk van het label | VOLGENS HET BEDRIJF | [Bron](https://arxiv.org/abs/2609.35108) | geen; methoden en tabel 1 |
| Poorthoofden beïnvloeden of wordt gemeld; latere routerhoofden beïnvloeden de locatie; ingrepen met uitvoervervanging en aandachtsomleiding ondersteunen de scheiding | VOLGENS HET BEDRIJF | [Bron](https://arxiv.org/abs/2609.35108) | geen; causale experimenten van de auteurs |
| Interne locatie-informatie kan blijven bestaan wanneer geen positie wordt gemeld; relevantie voor het monitoren van sturingsingrepen | ANALYSE | [Bron](https://arxiv.org/abs/2609.35108) | gevolgtrekking uit ingrepen op poort- en routerhoofden; geen monitoringresultaat in productie |
| Beperkingen van de reikwijdte; functionele in plaats van ervaringsgerichte introspectie; vervolgvragen; code en reproductiescripts vrijgegeven | GEVERIFIEERD | [Bron](https://arxiv.org/abs/2609.35108) | geen; vermelde reikwijdte van het artikel en repositorylink |
