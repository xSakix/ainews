+++
title = "Percepta test groeiend geheugen voor ophalen uit lange context"
slug = "percepta-test-groeiend-geheugen-voor-lange-context"
description = "Spotlight Memory benadert bij elke stap een klein gebied in uitbreidbare opslag. Percepta meldt sterk ophalen van informatie voorbij de trainingslengte van de modellen."
tags = ["models", "research"]
date = 2026-10-03T09:45:58+02:00
draft = false
+++

AI-onderzoeksbedrijf Percepta meldt dat zijn Spotlight Memory-architectuur informatie ophaalt uit contexten die zestien keer langer zijn dan de trainingsreeksen, terwijl het werk voor elke geheugentoegang gelijk blijft.

De architectuur geeft een taalmodel uitbreidbare opslag en leert het waar informatie moet worden geplaatst. Christos Tzamos, Guoqing Zheng en Athul Jacob beschrijven gecontroleerde experimenten in een technisch bericht van 2 oktober, met vergelijkingen tussen modellen met ongeveer evenveel parameters en dezelfde trainingsdata.

**Waarom dit ertoe doet:** Een onderzoeker die modellen voor lange documenten bouwt, krijgt bewijs voor een geheugenontwerp dat oude informatie toegankelijk houdt zonder elke eerdere token opnieuw te lezen. De afweging is expliciet: opslag kan groeien, terwijl het model bij elke stap slechts een kleine omgeving daarin benadert.

Het [Percepta-rapport](https://www.percepta.ai/blog/spotlight-memory) beschrijft de spanning tussen twee bestaande benaderingen. Volledige aandacht bewaart informatie over eerdere tokens, maar vergelijkt elke nieuwe zoekvraag met die geschiedenis. Recurrente modellen met vaste toestand persen het verleden in beperkte opslag. Dat verlaagt verwerkingskosten, maar steeds meer informatie concurreert uiteindelijk om dezelfde capaciteit.

Spotlight koppelt informatie in plaats daarvan aan adressen in een tweedimensionaal raster. Een schrijfactie wijst een cel toe wanneer een adres voor het eerst wordt gebruikt; latere schrijfacties kunnen die cel bijwerken. Een zoekvraag leest nabijgelegen cellen. Het aantal benaderde cellen blijft gelijk, ook als de verzameling toegewezen cellen groeit.

Het model leert die adressen tijdens training. Alle cellen delen dezelfde geleerde regels voor het vastleggen en bijwerken van informatie, zodat extra opslag geen nieuwe modelgewichten vereist. Een vloeiende wegingsfunctie verdeelt lees- en schrijfacties over naburige cellen, zodat de training een adres geleidelijk kan aanpassen.

Het mechanisme lijkt op een archief waarvan de kast kan groeien, terwijl een zoekopdracht direct naar een kleine groep laden gaat. De moeilijkheid is een bruikbare indeling leren: bij elkaar horende vragen en opgeslagen feiten moeten op verenigbare adressen uitkomen. Percepta's experimenten testen die vaardigheid voordat het ontwerp voor taalmodellering wordt gebruikt.

## Kleine modellen behielden feiten voorbij hun trainingslengte

Percepta trainde modellen met 140 miljoen, 280 miljoen en 670 miljoen parameters vanaf nul op FineWeb-Edu, een dataset met webtekst. Binnen elke groottegroep zagen modellen dezelfde data in dezelfde volgorde. De onderzoekers pasten de breedte van feedforwardlagen aan, zodat parameteraantallen hooguit 0,1 procent verschilden.

De eerste training gebruikte reeksen van ongeveer 8.000 tokens, de tekstfragmenten die een model verwerkt. Daarna testten de onderzoekers het ophalen uit reeksen tot ongeveer 128.000 tokens: één record werd in een lange context opgenomen en het model moest het terugvinden. Dat is de zestienvoudige uitbreiding achter de kop.

Spotlight bereikte volgens Percepta 93–100 procent terugvindpercentage bij de drie modelgroottes in de langste geteste context. De recurrente alternatieven met vaste toestand haalden maximaal ongeveer 6 procent; aandacht scoorde in deze test nul voorbij de trainingslengte, ook na herschaling van posities. Het resultaat betreft het vinden van één opgenomen record, niet elk soort redeneren over lange documenten.

De vergelijking bij korte context was minder opvallend. Bij de grootste modelgrootte bleef Spotlight's gemiddelde score op een verzameling taalmodeltaken dicht bij de alternatieven. Het voordeel lag in toegankelijke informatie bij groeiende context, niet in een brede sprong op die taken.

Percepta gaf vervolgens elke beschikbare modelcheckpoint dezelfde aanvullende training met lange context. Spotlight behield zijn voorsprong bij ophalen en bereikte het laagste taalmodelverlies op apart gehouden data bij elke geteste contextlengte en grootte. Een afzonderlijke vraagclassificatietaak verbeterde ook naarmate meer gelabelde voorbeelden de prompt vulden, wat het verband tussen groeiend geheugen en bruikbaar ophalen ondersteunt.

De resultaten blijven Percepta's eigen vroege experimenten. Het rapport verbindt het voorstel met voortdurend leren, maar het concrete bewijs hier is dat vaste modelgewichten een groeiend geheugen kunnen leren organiseren. Het grootste model bevat 670 miljoen parameters; overdracht van dat gedrag naar veel grotere systemen in gebruik blijft een open vraag.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
|---|---|---|---|
| Percepta publiceerde Spotlight Memory op 2 oktober; de bronvermelding noemt Christos Tzamos, Guoqing Zheng en Athul Jacob. | GEVERIFIEERD | [Technisch bericht](https://www.percepta.ai/blog/spotlight-memory) | geen |
| Het ontwerp leert adressen op een 2D-raster, wijst cellen bij de eerste schrijfactie toe, deelt bijwerkregels en gebruikt lokale differentieerbare lees- en schrijfacties met constante toegangskosten. | VOLGENS HET BEDRIJF | [Architectuurbeschrijving](https://www.percepta.ai/blog/spotlight-memory) | geen |
| De training vergeleek modellen van 140 miljoen, 280 miljoen en 670 miljoen parameters met identieke FineWeb-Edu-data en volgorde binnen elke grootte, bij 8.000 tokens context, met parameterafwijkingen van hooguit 0,1%. | VOLGENS HET BEDRIJF | [Trainingsprotocol](https://www.percepta.ai/blog/spotlight-memory) | geen |
| Bij 128.000 tokens context, zestien keer de trainingslengte van 8.000, haalde Spotlight 93–100% terugvindpercentage voor één opgenomen record (500 voorbeelden), baselines met vaste toestand hooguit 5,6%, aandacht 0% bij 16.000–128.000 tokens. | VOLGENS HET BEDRIJF | [RULER-resultaten](https://www.percepta.ai/blog/spotlight-memory) | geen |
| Bij 670 miljoen parameters waren taakgemiddelden met korte context: Spotlight 33,1, GDN-2 33,8, aandacht 33,3 en Gated DeltaNet 34,1. | VOLGENS HET BEDRIJF | [Taalevaluatie](https://www.percepta.ai/blog/spotlight-memory) | geen |
| Elke beschikbare checkpoint kreeg 1,17 miljard extra tokens bij 128.000 tokens context; Spotlight behield de beste ophaalprestaties en het laagste geteste verlies op apart gehouden data. TREC-coarse bij 670 miljoen parameters steeg van 63% naar 85% bij contextgroei van 8.000 naar 128.000 tokens. | VOLGENS HET BEDRIJF | [Training met lange context en classificatie](https://www.percepta.ai/blog/spotlight-memory) | geen |
| Uitbreidbare opslag scheidt geheugencapaciteit van werk per toegang; deze ophaalexperimenten met kleine modellen laten gedrag bij grotere uitrol onbeslist. | ANALYSE | [Ontwerp en experimentbereik](https://www.percepta.ai/blog/spotlight-memory) | geen |
