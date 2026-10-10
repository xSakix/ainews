+++
title = "Warm Compaction hergebruikt cache voor agentgeheugen"
slug = "warm-compaction-hergebruikt-cache-voor-agentgeheugen"
description = "De Hermes Agent-plugin met Apache-2.0-licentie laat het hoofdmodel een gecacht gespreksvoorvoegsel samenvatten. In zijn tests vermindert dat herhaalde promptverwerking."
tags = ["agents", "tools"]
date = 2026-10-09T04:01:06+02:00
draft = false
+++

Een nieuwe Hermes Agent-plugin comprimeert lange gesprekken door het hoofdmodel een promptvoorvoegsel te laten samenvatten dat de inferentieserver al heeft gecacht.

Warm Compaction stuurt het laatste verzoek van de agent opnieuw, voegt alleen de nieuwere gespreksregels toe en sluit af met een overdrachtsinstructie. Het model geeft een gestructureerde Markdown-samenvatting terug die de oudere geschiedenis vervangt, terwijl een recent slotdeel letterlijk behouden blijft.

**Waarom dit ertoe doet:** Contextcompressie vereist meestal dat het gesprek nogmaals uitgebreid wordt gelezen. Voor een ontwikkelaar die lange agentsessies draait, kan hergebruik van de voorvoegselcache van de server zowel de wachttijd als het risico verminderen dat een kleinere, afzonderlijke samenvatter een belangrijke instructie weglaat.

De plugin gebruikt gedocumenteerde Hermes Agent-interfaces en vereist geen patch van de host. Hij ondersteunt handmatige en automatische compressie, draait op Python 3.10 of later en is uitgebracht onder Apache 2.0. Installatie bestaat uit een Hermes-plugincommando, gevolgd door het selecteren van `warm_compaction` als contextengine.

Het snelheidsvoordeel hangt af van hetzelfde hoofdmodel en een inferentieserver die gecachte promptblokken kan hergebruiken. De auteur noemt gehoste API's met promptcaching, vLLM, SGLang, TensorRT-LLM, llama.cpp, MLX, Ollama en LM Studio als mogelijke routes, maar meldt alleen directe tests op een NVIDIA DGX-systeem en LM Studio. Een verzoek naar een ander llama.cpp-slot kan bijvoorbeeld de cache missen.

Het project bevat bewijsbestanden voor tien synthetische sessies van ongeveer 105.000 tokens. In die tests was de mediane samenvattingstijd van Warm Compaction 16,8 seconden, tegenover 43,5 seconden voor `hermes-lcm` en 78,5 seconden voor de ingebouwde compressor. Het behield 59 van de 60 geteste feiten; de twee vergelijkingssystemen behielden er 43 en 50. Dit zijn resultaten van de auteur uit één synthetische werklast en de drie engines gebruikten verschillende modellen.

Het ontwerp bevat foutafhandeling. Als het warme verzoek niet kan worden uitgevoerd of niet door de uitvoercontroles komt, roept de plugin de aanvullende samenvattingsroute van Hermes aan. Als ook die faalt, schrijft hij een samenvatting in een vast formaat en behoudt hij de nieuwste eerdere samenvatting als geciteerde tekst. Een geannuleerde poging laat de geschiedenis ongewijzigd.

Hermes-versies bieden mogelijk uiteindelijk een ingebouwde optie voor warme overdracht. De plugin controleert op die mogelijkheid en kan gebruikers ernaar verwijzen, maar blijft afzonderlijk te selecteren. De repository, instellingen en het bewijs zijn beschikbaar op [GitHub](https://github.com/Elevatormusic/hermes-warm-compaction).

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
|---|---|---|---|
| Warm Compaction verstuurt een gecacht voorvoegsel opnieuw en voegt nieuwe regels en een overdrachtsinstructie toe | GEVERIFIEERD | [Repository](https://github.com/Elevatormusic/hermes-warm-compaction) | geen |
| De plugin gebruikt gedocumenteerde Hermes-API's en heeft een Apache-2.0-licentie | GEVERIFIEERD | [Repository](https://github.com/Elevatormusic/hermes-warm-compaction) | geen |
| De versnelling vereist hetzelfde model en een werkende voorvoegselcache | GEVERIFIEERD | [Repository](https://github.com/Elevatormusic/hermes-warm-compaction) | geen |
| Mediane compressie duurde 16,8 seconden in tien synthetische sessies | VOLGENS HET BEDRIJF | [Repository](https://github.com/Elevatormusic/hermes-warm-compaction) | geen |
| De plugin behield 59 van de 60 geteste feiten | VOLGENS HET BEDRIJF | [Repository](https://github.com/Elevatormusic/hermes-warm-compaction) | geen |
| Mislukte warme verzoeken gebruiken aanvullende terugvalroutes en vervolgens een vast formaat | GEVERIFIEERD | [Repository](https://github.com/Elevatormusic/hermes-warm-compaction) | geen |
