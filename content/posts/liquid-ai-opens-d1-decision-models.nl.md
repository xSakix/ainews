+++
title = "Liquid AI opent d1-beslismodellen"
slug = "liquid-ai-opent-d1-beslismodellen"
description = "d1-3B met 3,1 miljard parameters en het experimentele d1-omni met 600 miljoen parameters beantwoorden gestructureerde vragen in één voorwaartse doorgang. De gewichten zijn beschikbaar voor lokale uitrol."
tags = ["models", "projects"]
date = 2026-10-08T03:58:31+02:00
draft = false
+++

Liquid AI bracht op 7 oktober open gewichten uit voor twee d1-modellen en brengt daarmee zijn snelle, gestructureerde beslissysteem naar lokale apparaten na een introductie uitsluitend via een API.

De modellen beantwoorden ja-of-nee-, meerkeuze- en scorevragen in één voorwaartse doorgang in plaats van een reeks tokens te genereren. d1-3B met 3,1 miljard parameters accepteert tekst en beelden; het experimentele d1-omni-600M accepteert tekst met beelden of maximaal 30 seconden audio.

Het ontwerp geeft ontwikkelaars een compacte component voor routering, moderatie, classificatie of rangschikking wanneer een vrij geformuleerd antwoord niet nodig is. Eén invoertoestand kan meerdere benoemde vragen bevatten en het model geeft de bijbehorende beslissingen samen terug, zonder de vertraging en variabele formulering van tokengeneratie.

Liquid meldt dat d1-3B één vraag beantwoordde in 8 milliseconden op een RTX 4090, 30 milliseconden op een Apple M5 Pro en 50 milliseconden op een Jetson Orin Nano. Dat zijn eigen metingen van het bedrijf. Zijn gepubliceerde tabel geeft d1-3B ook een gemiddelde score van 82,9 over zeven openbare tekstdatasets, terwijl het kleinere model 78,4 scoorde.

De twee releases bedienen verschillende hardware. d1-3B gebruikt Liquids beeld-taalmodel met alleen een decoder als basis en heeft een contextvenster van 32.768 tokens. d1-omni-600M combineert een bidirectionele tekstencoder met afzonderlijke beeld- en audio-encoders, met een contextvenster van 16.384 tokens. Liquid beschrijft het kleinere model als een vroege onderzoeksrelease en publiceert daarvoor geen vertragingsmetingen.

Beide repositories gebruiken de LFM Open License in plaats van een standaard permissieve softwarelicentie. Het laden van de modellen vereist momenteel Transformers 5.14 of later en voert door de repository geleverde Python uit via `trust_remote_code=True`, een instelling die aanleiding geeft om de gedownloade code vóór gebruik te beoordelen.

De gewichten, modelkaarten en demo zijn nu beschikbaar op Hugging Face. Liquid biedt ook GGUF- en 8-bitvarianten voor gewichten en activaties, die d1-3B gemakkelijker testbaar maken op beperkte machines terwijl zijn beslis-API nog nieuw is.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
|---|---|---|---|
| Liquid AI bracht op 7 oktober 2026 gewichten voor d1-3B en d1-omni-600M uit | GEVERIFIEERD | [Liquid AI-release](https://huggingface.co/blog/LiquidAI/open-d1) | [d1-3B-modelkaart](https://huggingface.co/LiquidAI/d1-3B) |
| d1-modellen beantwoorden gestructureerde vragen in één voorwaartse doorgang zonder uitvoertokens te genereren | GEVERIFIEERD | [Liquid AI-release](https://huggingface.co/blog/LiquidAI/open-d1) | geen |
| d1-3B accepteert tekst en beelden; d1-omni-600M accepteert tekst met beelden of audio | GEVERIFIEERD | [Liquid AI-release](https://huggingface.co/blog/LiquidAI/open-d1) | [d1-omni-600M-modelkaart](https://huggingface.co/LiquidAI/d1-omni-600M) |
| Liquid meldt 8 ms op RTX 4090, 30 ms op Apple M5 Pro en 50 ms op Jetson Orin Nano | VOLGENS HET BEDRIJF | [Liquid AI-release](https://huggingface.co/blog/LiquidAI/open-d1) | geen |
| Liquid meldt gemiddelde tekstbenchmarkscores van 82,9 voor d1-3B en 78,4 voor d1-omni-600M | VOLGENS HET BEDRIJF | [Liquid AI-release](https://huggingface.co/blog/LiquidAI/open-d1) | geen |
| Laden vereist Transformers 5.14 of later en `trust_remote_code=True` | GEVERIFIEERD | [Liquid AI-release](https://huggingface.co/blog/LiquidAI/open-d1) | [d1-3B-modelkaart](https://huggingface.co/LiquidAI/d1-3B) |
