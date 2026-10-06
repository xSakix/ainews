+++
title = "Signalen van zekerheid sturen modellen meer dan bekwaamheid"
slug = "signalen-van-zekerheid-sturen-modellen-meer-dan-bekwaamheid"
description = "Een gecontroleerd onderzoek vindt dat één zin met zekerheid of twijfel sterk kan veranderen of een redeneermodel een tool aanroept. De veranderingen richten zich echter zelden op problemen waarbij hulp nodig is."
tags = ["research", "agents"]
date = 2026-10-05T04:00:30+02:00
draft = false
+++

Vertel een redeneermodel “Ik ben zeker van mijn antwoord” en het vraagt minder snel een tool om hulp. Vertel hetzelfde model “Ik twijfel aan mijn antwoord” op hetzelfde punt in hetzelfde redeneertraject en het delegeert vaker. Het opvallende is niet dat taal gedrag verandert, maar dat die verandering weinig verband houdt met de vraag of het model het probleem zonder hulp kan oplossen.

Rohit Saxena en Utkarsh Upadhyay noemen deze eigenschap “nudgeability”, oftewel stuurbaarheid door kleine aansporingen. Hun preprint test of taal die zekerheid uitdrukt de keuze van een model kan sturen om rechtstreeks te antwoorden of een tool aan te roepen. Afzonderlijk testen ze of die sturing terechtkomt bij de problemen waarbij de tool echt nuttig is.

Dat onderscheid is van belang voor agents. Een systeem kan sterk reageren op een onzekerheidssignaal en toch tijd en geld verspillen aan toolaanroepen voor gemakkelijke vragen, terwijl het moeilijke vragen zelfverzekerd zelf houdt. Meer delegeren is niet noodzakelijk beter delegeren.

## Eén zin, twee contrafeitelijke uitvoeringen

Het experiment begint met een identiek probleem, dezelfde prompt en hetzelfde door het model gegenereerde begin van de redenering. Op een vaste grens voegen de onderzoekers één van twee zinnen in de eerste persoon toe, die zekerheid of twijfel uitdrukken. Het model kan daarna verder redeneren voordat het beslist te antwoorden of te delegeren. Doordat alles vóór de ingevoegde zin gelijk blijft, isoleert het verschil tussen het paar het effect van de zin.

Het onderzoek omvat negen redeneermodellen met open gewichten uit de Qwen-, Gemma- en GLM-families op MuSiQue en StrategyQA, plus grotere DeepSeek- en MiniMax-modellen die door aanbieders worden gehost. De primaire uitvoeringen gebruiken greedy decoding, met aanvullende experimenten met sampling en controles.

Over de experimenten met open gewichten verandert omschakelen van zekerheid naar twijfel het delegeren met een mediaan van 20,6 procentpunt. De grotere gehoste modellen verschuiven met 53 tot 70 procentpunt. Een controle waarbij de tekst wordt afgebroken en opnieuw gegenereerd zonder één van beide zinnen heeft bij de mediaan nauwelijks effect. Het redeneerblok direct na de zin afsluiten behoudt de richting van het effect.

Deze resultaten laten een sterk causaal aangrijpingspunt voor sturing zien. Ze laten niet zien dat de modellen hun eigen onzekerheid hebben ontdekt.

## Gevoeligheid is geen zelfkennis

Om te testen of de gedragsomslagen nuttig zijn, vergelijken de auteurs ze met de bekwaamheid van elk model zonder hulp. Een goede omslag stuurt een probleem dat het model fout zou beantwoorden naar de tool, of laat een probleem dat het kan oplossen bij het model. Slechts een mediaan van 42 procent van de veroorzaakte omslagen is goed gericht. Dat is een verbetering van twee procentpunt tegenover het willekeurig selecteren van hetzelfde aantal problemen.

Eenvoudig gezegd lijkt het geïnjecteerde zekerheidssignaal meer op een instructie dan op een uitlezing van zelfkennis. Het verschuift de toegangspoort voor toolgebruik sterk, maar die poort onderscheidt “Ik heb hulp nodig” slechts zwak van “Ik kan dit aan”. Het experiment levert de zekerheidszin bewust van buitenaf aan; het test niet of een model zelf een goed gekalibreerd signaal kan genereren.

## Wat agentbouwers moeten meten

De praktische les is voor elk reflectief beleid voor toolgebruik twee cijfers te rapporteren: hoe sterk het beleid gedrag verandert en hoe goed die veranderingen op echte behoefte zijn gericht. Een routeringsingreep die alleen het aantal toolaanroepen verhoogt, kan succesvol lijken terwijl hij slechts latentie toevoegt. Een ingreep die aanroepen onderdrukt, kan efficiënt lijken terwijl hij zelfverzekerde fouten laat bestaan.

De auteurs waarschuwen ook dat hun taken en ingreep beperkt zijn. Het artikel stelt niet vast hoe een agent in productie zich gedraagt met veel tools, veranderende kosten of adversariële instructies. De code is voor publicatie toegezegd en niet bij de preprint beschikbaar. De bijdrage is een heldere diagnose: voordat de uitgesproken zekerheid van een model wordt vertrouwd om toegang tot sterkere tools te beheren, moet worden gecontroleerd of die zekerheid bekwaamheid voorspelt in plaats van alleen gedrag aan te sturen.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
| --- | --- | --- | --- |
| Het ontwerp voegt zekerheid of twijfel toe op dezelfde grens in een identiek begin van de redenering | GEVERIFIEERD | [Preprint](https://arxiv.org/abs/2609.34572) | geen |
| Negen redeneermodellen met open gewichten uit Qwen, Gemma en GLM, plus gehoste DeepSeek- en MiniMax-modellen | GEVERIFIEERD | [Preprint](https://arxiv.org/abs/2609.34572) | geen |
| Mediane verschuiving in delegeren van 20,6 procentpunt bij open modellen en 53–70 procentpunt bij gehoste modellen | VOLGENS HET BEDRIJF | [Preprint](https://arxiv.org/abs/2609.34572) | geen; experimenten van de auteurs |
| Mediaan van 42 procent goed gerichte omslagen, twee procentpunt boven vergelijkbare willekeurige selectie | VOLGENS HET BEDRIJF | [Preprint](https://arxiv.org/abs/2609.34572) | geen; experimenten van de auteurs |
| Taal die zekerheid uitdrukt gedraagt zich meer als stuurinput dan als bewijs van zelfkennis van het model | ANALYSE | [Preprint](https://arxiv.org/abs/2609.34572) | interpretatie consistent met het resultaat van de auteurs over de gerichtheid |
| Code is nog niet beschikbaar | GEVERIFIEERD | [Preprint](https://arxiv.org/abs/2609.34572) | verklaring over reproduceerbaarheid zegt dat vrijgave bij publicatie is gepland |
