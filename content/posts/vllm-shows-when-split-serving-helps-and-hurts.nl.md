+++
title = "vLLM toont wanneer gescheiden inferentie helpt en hindert"
slug = "vllm-toont-wanneer-gescheiden-inferentie-helpt-en-hindert"
description = "Een praktische gids meet de afweging bij het scheiden van promptverwerking en tokengeneratie. Hoge latenties verbeteren onder belasting, maar het verplaatsen van het werkgeheugen van het model vertraagt het eerste token."
tags = ["essays", "tools", "hardware"]
date = 2026-10-06T04:04:31+02:00
draft = false
+++

Promptverwerking scheiden van tokengeneratie kan een modelserver onder belasting stabiliseren, maar de overdracht van het werkgeheugen kan de eerste reactie vertragen, meldt het team van vLLM.

Het open-sourceproject voor inferentie testte “disaggregated serving”, waarbij één GPU de prefill-fase afhandelt en een andere de decode-fase. Prefill leest de prompt en bouwt de key-value-cache op; decode gebruikt die cache om tokens te genereren. De gids verplaatst ook de tokenisatie en het ontleden van uitvoer naar een front-end zonder GPU.

Voor een beheerder die lange prompts verwerkt, biedt het ontwerp een keuze tussen twee soorten vertraging. De fasen scheiden voorkomt dat een grote prompt de generatie voor andere gebruikers onderbreekt, maar de cache moet tussen workers worden overgedragen voordat het decoderen begint.

In de test van vLLM met twee GPU's, Qwen2.5-7B en prompts van 8.000 tokens steeg het 99e percentiel van de tijd tussen gegenereerde tokens bij de gecombineerde opzet van 23 milliseconden naar 169 milliseconden bij 0,4 verzoeken per seconde. De gescheiden opzet hield die tijd tussen 25 en 52 milliseconden.

Hetzelfde experiment liet de kosten zien. Ongeveer 470 MB cache per prompt verplaatsen duurde circa 1,3 seconden, en de mediane tijd tot het eerste token bedroeg 2,2 seconden, tegenover 0,7 seconden wanneer beide fasen één worker deelden. De L40S-GPU's hadden geen NVLink en geen rechtstreekse peer-to-peeroverdracht. Het resultaat beschrijft daarom een bewust ongunstig transportpad en niet elke uitrol.

De beslisregel van de auteurs is praktisch: controleer eerst de GPU-topologie en bekijk vervolgens de meetwaarden voor cacheoverdracht bij de beoogde promptlengte en het beoogde aantal verzoeken per seconde. Scheiding is vooral aantrekkelijk wanneer prefill het decoderen herhaaldelijk verstoort of wanneer de twee fasen anders moeten schalen. Een licht belaste server kan de overdrachtskosten dragen zonder nuttige isolatie te winnen.

De gids haalt grotere resultaten van AMD en het llm-d-project aan, maar die tests gebruiken andere modellen, accelerators en clustergroottes. Ze ondersteunen het potentieel van de architectuur, geen algemeen toepasbaar versnellingscijfer.

De instructies richten zich op vLLM 0.30.0 of later en bevatten afzonderlijke renderer- en derendererdiensten. Het team zegt dat er nog lacunes in de integratie zijn, waardoor de controles op topologie en overdracht een voorwaarde zijn en geen optimalisatie na de uitrol.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
| --- | --- | --- | --- |
| vLLM documenteert afzonderlijke diensten voor prefill, decode en een front-end zonder GPU | GEVERIFIEERD | [vLLM-gids](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | openbare vLLM-configuratie en opdrachten |
| Bij 0,4 verzoeken/s bereikte het p99 van de tijd tussen tokens bij gezamenlijke verwerking 169 ms, terwijl gescheiden verwerking op 25–52 ms bleef | VOLGENS HET BEDRIJF | [vLLM-gids](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | geen; test uitgevoerd door het project |
| Een prompt van 8.000 tokens leverde ongeveer 470 MB cache en circa 1,3 s overdrachtstijd op | VOLGENS HET BEDRIJF | [vLLM-gids](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | geen |
| De mediane tijd tot het eerste token was 2,2 s bij gescheiden verwerking tegenover 0,7 s bij gezamenlijke verwerking | VOLGENS HET BEDRIJF | [vLLM-gids](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | geen |
| De test gebruikte twee L40S-GPU's zonder NVLink of peer-to-peeroverdracht | GEVERIFIEERD | [vLLM-gids](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | testconfiguratie vermeld door de auteurs |
| De gids richt zich op vLLM 0.30.0 of later | GEVERIFIEERD | [vLLM-gids](https://vllm.ai/blog/2026-09-29-disaggregated-serving-guide) | versievereiste in de gids |
