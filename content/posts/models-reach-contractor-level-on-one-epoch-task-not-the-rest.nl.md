+++
title = "Modellen evenaren opdrachtnemer bij één Epoch-taak, niet de rest"
slug = "modellen-halen-opdrachtnemersniveau-bij-een-epoch-taak"
description = "In de bijgewerkte benchmark voor echt werk van Epoch AI evenaren Fable 5.2 en Opus 5.5 een externe opdrachtnemer bij datacenteranalyse, in een fractie van de uren. Geen model haalt bij enige taak de norm voor werknemers; Epoch overweegt tijd van opdrachtnemers te verschuiven naar het beoordelen van AI-output."
tags = ["business", "research", "agents"]
date = 2026-11-18T03:14:41+01:00
draft = false
+++

De taak verschijnt in een werkruimte met een handleiding, een set tools en één naam: EcoDataCenter 1. Het model moet die campus toevoegen aan de database van AI-datacenters van Epoch AI. Het leest nieuwsberichten en documenten van toezichthouders, bestelt satellietbeelden en markeert vervolgens de foto's: blauwgroene contouren voor gebouwen, blauwe voor koelinstallaties en paarse voor noodgeneratoren. Een externe opdrachtnemer besteedt doorgaans ongeveer 16 uur aan elke locatie.

In het rapport van Epoch van 17 november leverden twee modellen die dit werk uitvoerden resultaten die de eigen datacenteranalist van de organisatie vergelijkbaar vond met die van een opdrachtnemer. Een derde behandelde slechts een deel van wat zijn bronnen lieten zien.

## Wat Epoch testte

Epoch AI is een onderzoeksorganisatie die de ontwikkeling van AI volgt. De benchmark Epoch Automation Reports neemt taken uit het eigen werk van de organisatie en geeft die aan modellen met de context die een nieuwe werknemer zou krijgen. Medewerkers van Epoch beoordelen de output vervolgens handmatig. Een score van 100 procent staat voor de norm die Epoch van zijn werknemers verwacht. De eerste versie, gepubliceerd op 8 oktober, testte zes modellen op 11 taken in vijf categorieën: grafisch ontwerp, Data Insights (korte artikelen over AI-trends), Data Explorers, datacenteronderzoek en onderzoeksopzet. De koplopers, Claude Fable 5.1 en GPT-6 Astra, presteerden betrouwbaar bij duidelijk afgebakende taken en faalden bij de open onderdelen van het werk.

Het nieuwe rapport van Epoch-onderzoeker Kelly Hong test Claude Fable 5.2 en GPT-6.2 Astra, samen met vier andere modellen, op een bijgewerkte reeks taken. Epoch veranderde verschillende zaken tegelijk. Het verving een open benchmarktaak, waarvoor volgens de organisatie het budget te laag was voor veel plausibele richtingen, door een oude werkproef die ooit aan sollicitanten werd gegeven. Het voegde bronnen toe aan de prompts, waaronder een ingekorte versie van het interne Slack-kanaal over datacenters. Ook stapte het over op een beoordelingsschaal van 1 tot 4 per criterium, dichter bij de manier waarop congresartikelen worden beoordeeld.

Het belangrijkste resultaat is een tweedeling. Fable 5.2 en GPT-6.2 Astra delen ongeveer de recordscore op de Epoch Capabilities Index. Op de taken uit echt werk haalde GPT-6.2 Astra gemiddeld 65 procent, 17 punten minder dan Fable 5.2. Geen model voldeed bij enige taak aan de werknemersnorm.

## Waar de modellen een opdrachtnemer evenaarden

De uitzondering is de datacentertaak. Fable 5.2 scoorde 97,5 procent en Opus 5.5 87,5 procent, tegenover 65 procent voor GPT-6.2 Astra. Een perfecte score betekent dat Epoch de output ongewijzigd zou kunnen publiceren. Epoch definieert opdrachtnemersniveau als werk dat zijn analist vergelijkbaar vond met wat opdrachtnemers leveren. Ook dat werk heeft vóór publicatie doorgaans nog aanpassingen nodig.

De resterende gebreken waren van het soort dat een beoordelaar corrigeert. De beeldannotaties van Fable 5.2 waren onvolmaakt en de tekst was te lang. Bij Opus 5.5 waren aanpassingen nodig in de classificatie van apparatuur en ingrijpendere correcties aan de annotaties. Volgens Epoch voldeden beide voor het kernonderzoek aan de kwaliteitsnorm, met geloofwaardige bronnen en goed afgewogen oordelen.

De kostencijfers zijn het deel dat gevolgen heeft voor werk. Opus 5.5 was in iets minder dan 3 uur klaar, tegen lagere kosten dan een opdrachtnemer. Fable 5.2 deed er ongeveer 6,5 uur over en kostte meer dan een opdrachtnemer, in ruil voor het betere resultaat. Epoch schrijft nu te “overwegen om de tijd van opdrachtnemers te verschuiven naar het beoordelen van AI-output en andere onderdelen van onze analyse van AI-datacenters”. Het rapport zegt niet dat een opdrachtnemer werk heeft verloren. Bovendien gaat de taak om één databasevermelding met een gedetailleerde handleiding, niet om een hele functie.

Dezelfde taak laat zien hoe het derde model faalde. De bronnen van GPT-6.2 Astra wezen op verschillende AI-gebouwen op de campus, maar het behandelde er één en verwees naar een gebrek aan expliciet bewijs. Daarna liet het schattingen van rekencapaciteit en chips weg, omdat het voor elk getal waarop die berustten een afzonderlijke bron wilde. Volgens Epoch zou de handleiding het model ertoe hebben gebracht die schattingen wel te maken. Gemini 4 Argon maakte de omgekeerde fout: het nam aan dat elk gebouw Nvidia B200-chips gebruikte, terwijl die slechts voor één gebouw waren bekendgemaakt. Epoch noemt dit fouten die opdrachtnemers geacht worden te vermijden.

## Waar ze nog steeds falen

Buiten de datacentertaak keert het rapport terug naar het patroon van oktober. De modellen hebben moeite om experimenten te ontwerpen, iteratief te werken en te beoordelen welke bevinding belangrijk is.

Bij een taak die was afgeleid van een oude sollicitatieproef moesten modellen met schaakvarianten meten hoe goed AI omgaat met situaties die afwijken van zijn trainingsdata. Elk model gebruikte varianten die al bestaan. Volgens Epoch voerde Gemini 4 Argon zelfs een experiment uit waaruit bleek dat de modellen de gekozen varianten kenden, maar ging het daarna gewoon verder. De verzonnen variant van GPT-6.2 Astra verwisselde alleen de namen van stukken. Claude Opus 5.5 en Fable 5.1 presenteerden een bekend stuk uit het sprookjesschaak, de kameel, als iets nieuws. Het “Kingsgate” van Fable 5.2 speelt precies zoals een bestaande variant met de naam “Midline Invasion”.

Bij een taak over het verbergen van berichten in SVG-afbeeldingen hield Fable 5.2 vast aan zijn eerste coderingsprompt. Die leverde beelden op die het bericht meestal openlijk toonden. Menselijke onderzoekers die de prompt iteratief verbeterden, verkregen werkelijk verborgen coderingen, zoals sterren waarvan de hoogtes voor letters staan. Bij een open Data Insight-taak koos GPT-6.2 Astra een onderwerp dat Epoch te beperkt vond voor zijn publiek: de efficiëntie van tokenisatie van het Chinees in twee specifieke modellen. Epoch zag hier geen betekenisvolle verbetering ten opzichte van GPT-6 Astra, dat het al bekende feit had gekozen dat populaire open modellen mixture-of-expertsarchitecturen gebruiken.

Ook de presentatie schoot tekort. Het schaakrapport van GPT-6.2 Astra opende met een vetgedrukte bevinding die door de eigen latere resultaten werd ondergraven. Volgens Epoch zou zo'n gebrek publicatie tegenhouden, ongeacht de waarde van het onderzoek.

## De modellen beoordelen zichzelf

Epoch voegde een test van zelfbeoordeling toe. Wanneer er menselijke output was die aan de norm voldeed, kreeg het model beide versies zonder labels te zien, samen met de beoordelingsrubric. Elk model gaf de voorkeur aan zijn eigen output, behalve Gemini 4 Argon, dat één keer het menselijke werk koos. Volgens Epoch overdreven de motiveringen kleine gebreken in het menselijke werk en beloonden ze oppervlakkige grondigheid, zoals het aantal uitgevoerde experimenten. Die ene uitzondering van Argon kwam tot de redenering die Epoch zelf zou gebruiken: het menselijke werk voerde een zuiver experiment uit gericht op de kernvraag, terwijl de eigen experimenten er “oppervlakkig formeler” uitzagen. Epoch zegt dat modellen mogelijk aan zijn normen zouden voldoen als ze dit betrouwbaar konden doen, maar dat dit niet de norm was.

## Wat de cijfers kunnen dragen

Epoch noemt zijn eigen beperkingen. Elk model voerde elke taak één keer uit, de beoordeling is handmatig en deels subjectief, en door de gewijzigde opzet zijn de scores slechts grofweg vergelijkbaar met die van oktober. Sommige eerdere modellen werden opnieuw getest en andere niet. De organisatie raadt lezers aan de kwalitatieve bevindingen zwaarder te laten wegen dan de exacte scores en zegt dat de resultaten geen maatstaf zijn voor wat AI in alle soorten werk kan doen. De taken komen van Epoch zelf, worden door Epoch-medewerkers beoordeeld en twee van de drie leidende modellen zijn van Anthropic. Een voetnoot voegt toe dat GPT-6.2 Astra uitsluitend binnen het interne team van Epoch is geëvalueerd en besproken.

Met die beperkingen in gedachten beschrijft het rapport een smalle strook werk waarin iets is verschoven. Een taak met een lange handleiding, publieke bronnen en controleerbare output wordt nu uitgevoerd op een niveau dat een menselijke analist aan een beoordelaar zou doorgeven. Dat geldt niet voor taken die afhangen van het kiezen van de vraag, herkennen dat een resultaat triviaal is of de lezer vertellen wat ertoe doet. Zelfs de output van Opus 5.5, de goedkoopste van de twee goede resultaten, kwam terug met annotaties die ingrijpende correcties nodig hadden. Die correcties bleven het werk van een persoon met het satellietbeeld voor zich.

## Referenties

- Hong, K. (2026). *How good are Fable 5.2 and GPT-6.2 Astra at real work?* Epoch AI. https://epoch.ai/publications/how-good-are-fable-5-2-and-gpt-6-2-astra-at-real-work
- Epoch AI (2026). *Can AI automate Epoch?* https://epoch.ai/publications/can-ai-automate-epoch
