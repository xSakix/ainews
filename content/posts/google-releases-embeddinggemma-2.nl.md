+++
title = "Google brengt EmbeddingGemma 2 uit voor multimodaal zoeken"
slug = "google-brengt-embeddinggemma-2-uit-voor-multimodaal-zoeken"
description = "Googles embeddingmodel met 740 miljoen parameters brengt tekst, code, afbeeldingen, video en audio onder in één vectorruimte, met modulaire encoders voor lokale apparaten."
tags = ["models", "tools"]
date = 2026-10-07T04:01:57+02:00
draft = false
+++

Google heeft EmbeddingGemma 2 uitgebracht, een model met open gewichten en 740 miljoen parameters dat tekst, code, afbeeldingen, videobeelden en audio in één gedeelde embeddingruimte plaatst.

De Apache-2.0-gewichten verschenen op 6 oktober met ondersteuning in Transformers, sentence-transformers, llama.cpp, vLLM, Ollama, LM Studio, MLX en Transformers.js. Het model is bedoeld voor het ophalen van informatie en routering, niet voor het genereren van tekst: het zet verschillende soorten invoer om in vectoren die op overeenkomst kunnen worden vergeleken.

## Waarom dit ertoe doet {#why-it-matters}

Een ontwikkelaar die een persoonlijke zoekfunctie op een telefoon of laptop bouwt, kan nu een spraakmemo indexeren en een videofragment terugvinden zonder eerst spraakherkenning, beeldbeschrijving en een afzonderlijk tekstembeddingmodel aan elkaar te koppelen. Dat verwijdert verschillende onderdelen uit het lokaal ophalen van informatie, al hangt het werkelijke nut van het model nog altijd af van de eigen gegevens en het latentiebudget van de gebruiker.

EmbeddingGemma 2 is modulair. Het basismodel voor tekst en code heeft 270 miljoen parameters; beeld voegt 170 miljoen toe en audio 300 miljoen. Alle configuraties projecteren naar 768 dimensies, en Matryoshka-training laat een applicatie vectoren inkorten tot 512, 256 of 128 dimensies om opslag te besparen.

Google zegt dat de gekwantiseerde gewichten voor alleen tekst ongeveer 191 MB actief RAM gebruiken op een Pixel 11 Pro, oplopend tot ongeveer 567 MB voor het volledige model. De context van 8.192 tokens kan volgens Googles verpakkingsschema maximaal 5,5 minuten audio, 29 afbeeldingen of 58 videobeelden bevatten.

De evaluatie van het bedrijf zet MTEB Code op 78,68, tegenover 68,76 voor de eerste EmbeddingGemma. Google claimt ook toonaangevende kwaliteit onder multimodale embeddingmodellen met minder dan één miljard parameters. Dat zijn metingen op de releasedag en geen onafhankelijke reproducties; de modelkaart vormt een betere basis om een specifieke ophaaltaak te vergelijken.

De release deelt een tokenizer en audio-encoderontwerp met Gemma 4, wat dubbele componenten kan verminderen wanneer het embeddingmodel een lokaal generatief model voedt. Google heeft ook voorbeeldapplicaties voor mediazoeken en het terugvinden van videomomenten gepubliceerd.

Het volgende praktische bewijs zal komen van tests op gemengde persoonlijke verzamelingen, waarbij het terugvinden van informatie tussen modaliteiten, indexeringstijd en geheugen belangrijker zijn dan één samengestelde benchmark.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
| --- | --- | --- | --- |
| Google bracht EmbeddingGemma 2 uit op 6 oktober 2026 | GEVERIFIEERD | [Aankondiging van Google](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) | [gewichten en modelkaart](https://huggingface.co/google/embeddinggemma-2) |
| Het model heeft 740 miljoen parameters met modulaire componenten van 270 miljoen voor tekst, 170 miljoen voor beeld en 300 miljoen voor audio | GEVERIFIEERD | [Aankondiging van Google](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) | modelkaart vermeldt de architectuur |
| Gekwantiseerd actief RAM is ongeveer 191 MB voor tekst en 567 MB voor het volledige model op Pixel 11 Pro | VOLGENS HET BEDRIJF | [Aankondiging van Google](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) | geen |
| MTEB Code steeg van 68,76 naar 78,68 | VOLGENS HET BEDRIJF | [Aankondiging van Google](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/) | geen |
| Apache-2.0-gewichten zijn beschikbaar | GEVERIFIEERD | [modelrepository](https://huggingface.co/google/embeddinggemma-2) | repository is toegankelijk |
