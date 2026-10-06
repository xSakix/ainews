+++
title = "Modellen adresseren feiten op volgorde van vermelding"
slug = "modellen-adresseren-feiten-op-volgorde-van-vermelding"
description = "Een preprint vindt een gedeelde interne richting die taalmodellen naar het eerste, tweede of latere feit in een passage wijst. Een vraag langs die richting verschuiven kan veranderen welk feit het model ophaalt."
tags = ["research", "models"]
date = 2026-10-06T04:08:31+02:00
draft = false
+++

Taalmodellen lijken feiten in een passage deels te vinden aan de hand van de volgorde waarin die feiten zijn vermeld, volgens een nieuw onderzoek naar interpreteerbaarheid.

Yufa Zhou testte Qwen-, Gemma- en Llama-modellen op korte lijsten met feitelijke uitspraken, gevolgd door vragen. De interne vraagtoestanden van de modellen vormden een herhaalbaar patroon voor het eerste, tweede en latere feit, ook wanneer de namen en onderwerpen veranderden.

## Waarom dit ertoe doet {#why-it-matters}

Voor een onderzoeker die wil begrijpen hoe een model informatie ophaalt, levert het resultaat een concreet mechanisme op, in plaats van nog een correlatie tussen activaties en antwoorden. Dezelfde interne richting kon experimenteel worden verschoven, waardoor een vraag over één feit een ander feit uit de passage ophaalde.

Het artikel noemt deze posities “feitadressen”. Neem een context waarin staat dat Alice een appel eet en Bob een peer. Een vraag over Alice en een vraag over Bob verschillen binnen het model langs een richting die samenhangt met de volgorde waarin de feiten zijn vermeld. Toen de onderzoeker de richting van het eerste naar het tweede feit toevoegde aan een vraag over het eerste feit, antwoordde het model vaak met de inhoud van het tweede.

Die ingreep is het sterkste bewijs van het onderzoek. Een classifier kan veel patronen in verborgen toestanden ontdekken zonder te laten zien dat een model ze gebruikt. Het antwoord veranderen door het voorgestelde adres te veranderen, biedt causale steun voor het mechanisme, al gebruiken de tests gecontroleerde feitenlijsten in plaats van lange, natuurlijke documenten.

Bij 64 nieuwe woordverzamelingen selecteerde de ingreep het bedoelde feit in ongeveer vijf op de zes gevallen voor Qwen, ongeveer de helft voor Gemma en ongeveer één op de drie voor Llama. De exacte percentages waren respectievelijk 84,1 procent, 53,9 procent en 36,2 procent. Die verschillen laten zien dat de richting tussen modelfamilies werd gedeeld, maar niet in elke familie even betrouwbaar was.

## De adressen nemen weinig interne ruimte in

Zhou meldt dat de feitadressen in een deelruimte met lage rang liggen. Eenvoudig gezegd hebben de modellen geen afzonderlijke, losstaande richting nodig voor elke mogelijke positie; een kleine verzameling richtingen beschrijft een groot deel van het volgordepatroon.

Het eerstgenoemde feit was voor de modellen ook gemakkelijker te bereiken dan latere feiten. Dat lijkt op een primacy-effect in het menselijke geheugen, maar het experiment stelt niet vast dat mensen en transformers hetzelfde mechanisme gebruiken. Het identificeert een meetbare asymmetrie in de geteste modellen.

Het patroon verscheen in lagen voorbij het midden van het model en bij groottes van 1,5 miljard tot 32 miljard parameters. Checkpoints uit de training suggereerden dat het vroeg ontstond en niet pas na uitgebreide instructietraining. De code die bij de preprint is vrijgegeven, maakt de gecontroleerde ingrepen inzichtelijk.

De beperkte opzet is ook de belangrijkste beperking. Lijsten met eenvoudige feiten isoleren de volgorde helder, terwijl echte prompts koppen, herhaalde verwijzingen, tools en tegenstrijdige uitspraken bevatten. Het artikel laat zien dat de volgorde van vermelding onder gecontroleerde omstandigheden als adres kan dienen; het laat niet zien dat die volgorde het ophalen van informatie in gewone agenttranscripten domineert.

Zhou diende de preprint op 1 oktober 2026 in. Het volgende bewijs zal moeten komen van het reproduceren van de ingreep op minder regelmatige documenten en van tests die nagaan of een andere documentstructuur dezelfde interne richtingen verandert.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
| --- | --- | --- | --- |
| Vraagtoestanden zijn bij Qwen, Gemma en Llama georganiseerd volgens de volgorde van feiten | VOLGENS HET BEDRIJF | [Preprint van Zhou](https://arxiv.org/abs/2610.00910) | geen; resultaat uit een preprint |
| Het toevoegen van een ordinale vector kan een vraag naar een ander feit leiden | VOLGENS HET BEDRIJF | [Preprint van Zhou](https://arxiv.org/abs/2610.00910) | geen; experiment van de auteur |
| Overdracht naar 64 woordverzamelingen bereikte 84,1 procent voor Qwen, 53,9 procent voor Gemma en 36,2 procent voor Llama | VOLGENS HET BEDRIJF | [Preprint van Zhou](https://arxiv.org/abs/2610.00910) | geen |
| Feitadressen liggen in een deelruimte met lage rang en geven het eerste feit een voordeel | VOLGENS HET BEDRIJF | [Preprint van Zhou](https://arxiv.org/abs/2610.00910) | geen |
| Het patroon verschijnt bij 1,5 miljard tot 32 miljard parameters en vormt zich vroeg in de pretraining | VOLGENS HET BEDRIJF | [Preprint van Zhou](https://arxiv.org/abs/2610.00910) | geen |
| Code voor reproductie is openbaar | GEVERIFIEERD | [Repository voor de volgorde van vermelding](https://github.com/MasterZhou1/order-of-mention) | repository beschikbaar |
