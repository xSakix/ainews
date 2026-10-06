+++
title = "4MT-VLM: visiemodellen verliezen locaties na rotatie"
slug = "4mt-vlm-visiemodellen-verliezen-locaties-na-rotatie"
description = "Een preprint past een klinische test voor ruimtelijk geheugen aan voor 16 visietaalmodellen. Alle herkennen een landschap vanuit de bestudeerde hoek, maar de meeste vervallen tot gokken zodra de camera beweegt."
tags = ["research", "models"]
date = 2026-10-06T04:02:31+02:00
draft = false
+++

Visietaalmodellen herkennen een landschap vanuit de hoek waarin ze het voor het eerst zagen, maar de meeste kunnen het niet aanwijzen zodra de camera beweegt. Dat blijkt uit 4MT-VLM, een nieuwe benchmark die is aangepast van een klinische test voor ruimtelijk geheugen.

Markus Frey van Fraunhofer IAIS, een Duits instituut voor toegepast onderzoek, gaf 16 open en gesloten modellen de puzzel die bij menselijke patiënten wordt gebruikt: bestudeer een met de computer weergegeven landschap met vier bergtoppen en vind het vervolgens tussen vier vergelijkbare landschappen die vanuit een nieuwe hoek worden getoond. Een menselijke vrijwilliger loste ongeveer vier van de vijf gedraaide opgaven op. De meeste modellen deden het niet beter dan gokken.

## Waarom dit ertoe doet {#why-it-matters}

Een robotica-engineer die een visietaalmodel als ogen van een mobiele robot gebruikt, heeft precies deze vaardigheid nodig: een kamer herkennen nadat de robot zich heeft omgedraaid. De preprint vindt dat grotere modellen noch gedetailleerdere instructies die vaardigheid leveren.

## Herkenning blijft overeind, rotatie mislukt

De benchmark past de Four Mountains Test aan, die clinici gebruiken omdat scores dalen bij schade aan de hippocampus en in een vroeg stadium van de ziekte van Alzheimer. Kleuren, texturen en belichting veranderen bij elke opgave tussen de studieafbeelding en de testafbeeldingen. Daardoor is zelfs een opgave zonder rotatie niet op te lossen door pixels te vergelijken. Frey behandelt de nauwkeurigheid op die ongedraaide opgaven als controle of een model de locatie überhaupt kan herkennen.

De modellen slagen voor die controle en falen vervolgens bij de rotatie. GPT-5.6 Luna van OpenAI beantwoordde elke ongedraaide opgave correct, maar slechts 31 procent van de gedraaide opgaven, waarbij gokken één op vier oplevert. Over alle 16 modellen samen was 135 graden de slechtste hoek: de nauwkeurigheid zakte daar duidelijk onder het kansniveau.

Een halve draai van 180 graden, de grootste verandering, scoorde beter dan 135 graden. Frey interpreteert dat als een teken dat de modellen een beeldtruc gebruiken, zoals vergelijken met een spiegelbeeld van de scène, en geen interne kaart draaien. De menselijke vergelijking komt van één deelnemer. Dat volstaat om te laten zien dat de taak oplosbaar is, maar niet om een menselijk gemiddelde te geven.

## Grotere modellen herkennen meer, maar draaien niet beter

Schaal verbeterde de herkenning en liet de rotatieprestaties gelijk. Binnen Alibaba's Qwen2.5-VL-familie, van 3 miljard tot 72 miljard parameters, steeg de nauwkeurigheid zonder rotatie van 30 naar 75 procent, terwijl de nauwkeurigheid met rotatie op of onder het kansniveau bleef. De InternVL3.5-familie herhaalde het patroon van 1 miljard tot 38 miljard parameters. Van 14 modellen met open gewichten tot 235 miljard parameters beantwoordde geen enkel meer dan 31 procent van de gedraaide opgaven correct, en een “denkende” variant scoorde hetzelfde als zijn standaardtegenhanger.

Instructies dichtten de kloof niet. Frey testte Qwen2.5-VL-32B met zes prompts, waaronder expliciete procedures zoals het landschap van recht boven voorstellen of de opvallendste bergtop als anker gebruiken. Bij alle zes bleef het model onder het kansniveau.

## Meer afstand tussen foute antwoorden onthult een grove kaart

Het meest informatieve experiment veranderde alleen de foute antwoorden. Frey mat in meters hoe ver de bergtoppen van twee landschappen uit elkaar liggen na de best mogelijke rotatie. Vervolgens tekende hij de drie afleiders opnieuw met verder afwijkende indelingen, terwijl het doel en de hoeken identiek bleven.

De dichtstbijzijnde afleider van ongeveer 7 meter naar ongeveer 31 meter afstand verplaatsen, bracht Gemini 3.8 Flash van Google bij gedraaide opgaven van 39 naar 85 procent en GPT-5.6 Luna van 31 naar 55 procent. Geen enkel open model verbeterde in statistisch betekenisvolle mate.

Dat is het bewijs van het artikel dat frontiermodellen enig besef van de indeling hebben, maar alleen met lage resolutie. Een model zonder kaart zou niet profiteren van meer afstand tussen de afleiders, en een model met een kaart op menselijk niveau zou geen 30 meter scheiding nodig hebben. Het effect lijkt op een stad herkennen vanuit een vliegtuigraam, maar de eigen straat niet.

De fouten wijzen in dezelfde richting. Iemand die verkeerd antwoordt, kiest doorgaans de afleider waarvan de indeling het dichtst bij het doel ligt. De foute antwoorden van de modellen waren bijna gelijk verdeeld over nabije en verre afleiders, alsof de indeling geen rol speelde bij de keuze.

## Een synthetische test van één auteur

De landschappen zijn synthetische weergaven, en Frey merkt op dat pretraining op vergelijkbare gerenderde scènes sommige modellen zou kunnen bevoordelen. Het aantal parameters van gesloten modellen is niet bekendgemaakt; het bewijs over schaal berust dus alleen op open modellen. De preprint, op 30 september 2026 op arXiv geplaatst, heeft één auteur en linkt niet naar code of een dataset.

Frey zegt dat meer menselijke deelnemers worden getest. Dat zal een passende vergelijkingsgroep bieden voor de score van 82 procent die de vrijwilliger op gedraaide opgaven behaalde.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
| --- | --- | --- | --- |
| 4MT-VLM past de Four Mountains Test aan; 500 opgaven over 100 gegenereerde landschappen, 16 modellen getest | GEVERIFIEERD | [Preprint van Frey](https://arxiv.org/abs/2609.39238) | geen; eigen benchmark van de auteur |
| Het uiterlijk wordt bij elke hoek opnieuw bepaald tussen studie- en testafbeeldingen | GEVERIFIEERD | [Preprint van Frey](https://arxiv.org/abs/2609.39238) | geen; methodebeschrijving |
| Eén menselijke deelnemer beantwoordde 100% van de ongedraaide en 82% van de gedraaide opgaven correct | VOLGENS HET BEDRIJF | [Preprint van Frey](https://arxiv.org/abs/2609.39238) | geen; slechts één deelnemer |
| GPT-5.6 Luna: 100% zonder rotatie, 31% met rotatie; kansniveau is 25% | VOLGENS HET BEDRIJF | [Preprint van Frey](https://arxiv.org/abs/2609.39238) | geen |
| Gezamenlijke nauwkeurigheid bij 135 graden is 15,0% (48/320), onder het kansniveau; 23% bij 180 graden | VOLGENS HET BEDRIJF | [Preprint van Frey](https://arxiv.org/abs/2609.39238) | geen |
| Modellen gebruiken een beeldtruc, zoals vergelijken met een spiegelbeeld | ANALYSE | [Preprint van Frey](https://arxiv.org/abs/2609.39238) | interpretatie van het 135/180-gradenpatroon door de auteur |
| Qwen2.5-VL van 3 miljard tot 72 miljard parameters: zonder rotatie 30% tot 75%, met rotatie 29%, 31%, 18%, 20% | VOLGENS HET BEDRIJF | [Preprint van Frey](https://arxiv.org/abs/2609.39238) | geen |
| Geen model met open gewichten (1 miljard tot 235 miljard parameters) overschrijdt 31% met rotatie; de denkende variant evenaart de instructievariant op 19% met rotatie | VOLGENS HET BEDRIJF | [Preprint van Frey](https://arxiv.org/abs/2609.39238) | geen |
| Zes instructiestijlen laten Qwen2.5-VL-32B op 13,8% tot 23,8% staan, allemaal onder het kansniveau | VOLGENS HET BEDRIJF | [Preprint van Frey](https://arxiv.org/abs/2609.39238) | geen |
| Mediane afstand tot de dichtstbijzijnde afleider van 6,8 m naar 31,4 m: Gemini 3.8 Flash van 39% naar 85%, GPT-5.6 Luna van 31% naar 55% | VOLGENS HET BEDRIJF | [Preprint van Frey](https://arxiv.org/abs/2609.39238) | geen |
| Geen open model verandert significant bij meer afstand tussen de afleiders | VOLGENS HET BEDRIJF | [Preprint van Frey](https://arxiv.org/abs/2609.39238) | geen |
| Modelfouten zijn 30/37/33 verdeeld over de dichtstbijzijnde, middelste en verste afleider; de mens koos de dichtstbijzijnde bij 10 van de 14 fouten | VOLGENS HET BEDRIJF | [Preprint van Frey](https://arxiv.org/abs/2609.39238) | geen |
| Frontiermodellen hebben een grove representatie van de indeling | ANALYSE | [Preprint van Frey](https://arxiv.org/abs/2609.39238) | gevolgtrekking uit het resultaat met afleiderafstanden |
| Preprint van één auteur geplaatst op 30 september 2026; auteur bij Fraunhofer IAIS; geen code of data gekoppeld | GEVERIFIEERD | [arXiv-vermelding](https://arxiv.org/abs/2609.39238) | arXiv-metadata en e-maildomein van de auteur |
| Meer menselijke deelnemers worden geëvalueerd | VOLGENS HET BEDRIJF | [Preprint van Frey](https://arxiv.org/abs/2609.39238) | geen |
