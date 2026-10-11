+++
title = "H2O.ai brengt H2O-Lightning-31B uit"
slug = "h2o-ai-brengt-h2o-lightning-31b-uit"
description = "Het beslismodel met open gewichten beantwoordt afgebakende vragen in één voorwaartse doorgang en geeft waarschijnlijkheden terug. De sterkste snelheids- en nauwkeurigheidscijfers komen uit H2O.ai's eigen tests."
tags = ["models", "tools"]
date = 2026-10-11T04:06:06+02:00
draft = false
+++

H2O.ai heeft H2O-Lightning-31B uitgebracht, een model met open gewichten dat afgebakende beslisvragen beantwoordt met waarschijnlijkheden in plaats van vrij proza te genereren.

Het model is gebaseerd op Gemma 4 31B-it en accepteert tekst plus maximaal vier beelden. De interface omvat keuzes, ja-of-nee-vragen en geordende scores en geeft één resultaat terug in één voorwaartse doorgang. H2O.ai publiceerde de gewichten, modelkaart en servercode op Hugging Face.

## Waarom dit ertoe doet {#why-it-matters}

Voor een ontwikkelaar die een grote chatbot gebruikt om tickets te routeren, records te beoordelen of een tool te selecteren, kan beperkte uitvoer verschillende kwetsbare stappen wegnemen: om JSON vragen, die ontleden, verkeerd gevormde antwoorden afwijzen en opnieuw vragen. Een waarschijnlijkheid maakt ook zichtbaar hoe dicht de keuze bij een alternatief lag, al is die alleen nuttig wanneer het model voor de bedoelde data is gekalibreerd.

H2O.ai meldt dat het model met 31 miljard parameters 212 van de 231 openbare JevBench-vragen correct beantwoordde. In zijn beeldevaluatie scoorde het gefinetunede model 88,4 procent over 1.877 vragen, tegenover 88,0 procent voor de bevroren Gemma-basis. Het onzekerheidsinterval van de modelkaart omvat geen verbetering, zodat dat beeldresultaat geen betrouwbare winst ten opzichte van het basismodel aantoont.

Het bedrijf meldt ook een mediane vertraging van ongeveer 25 milliseconden bij het laden van het model in FP8 op één NVIDIA H100. Dat cijfer komt uit zijn eigen opstelling, met voorvoegselcaching uitgeschakeld, en de kaart geeft geen meting voor kleinere GPU's. De gepubliceerde bfloat16-bestanden beslaan samen ongeveer 63 GB vóór runtime-overhead.

De release draait op ongewijzigd vLLM 0.30.0 achter H2O.ai's `/v1/systemone`-compatibiliteitslaag. Lange records worden niet volledig verwerkt: een ophaalfase kort ze vóór inferentie in tot 3.000 tokens. Die grens is relevant omdat een beslissing alleen het bewijs kan weerspiegelen dat de ophaalstap behoudt.

De gewichten vallen onder Apache 2.0 naast Googles Gemma-voorwaarden. H2O.ai's kennisgeving wijst specifiek op Gemma's gebruiksverboden voor geautomatiseerde beslissingen die individuele rechten raken, zodat de open bestanden niet elke uitrol toestaan.

H2O.ai actualiseerde ook zijn eerdere verwante model met 4 miljard parameters met herziene vertragingsmetingen en een GGUF-pakket voor llama.cpp. De release met 31 miljard parameters is nu beschikbaar via de Hugging Face-modelpagina; onafhankelijke tests van vertraging, kalibratie en taakkwaliteit zijn nog niet gepubliceerd.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
|---|---|---|---|
| H2O.ai bracht H2O-Lightning-31B uit met gewichten, een modelkaart en servercode | GEVERIFIEERD | https://huggingface.co/h2oai/h2o-lightning-31b | geen |
| Het model ondersteunt afgebakende beslissingen met tekst en beelden en geeft waarschijnlijkheden terug in één voorwaartse doorgang | GEVERIFIEERD | https://huggingface.co/h2oai/h2o-lightning-31b | geen |
| Het scoorde 212 van de 231 JevBench-items en ongeveer 25 ms mediane vertraging op één H100 | VOLGENS HET BEDRIJF | https://huggingface.co/h2oai/h2o-lightning-31b | geen |
| Zijn beeldevaluatie toonde geen statistisch betrouwbare winst ten opzichte van de bevroren Gemma-basis | GEVERIFIEERD | https://huggingface.co/h2oai/h2o-lightning-31b | geen |
| Gemma-voorwaarden beperken geautomatiseerde beslissingen die individuele rechten raken | GEVERIFIEERD | https://huggingface.co/h2oai/h2o-lightning-31b | geen |
