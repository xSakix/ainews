+++
title = "Cloudflare voegt multimodaal Clef-omni toe"
slug = "cloudflare-voegt-multimodaal-clef-omni-toe"
description = "De nieuwe classifier behoudt Qwen3-Omni's beeld-, audio- en video-invoer, maar geeft getypeerde antwoorden terug in plaats van gegenereerd proza. Cloudflare verlaagde ook Clef-flash' prijs en contextvenster."
tags = ["models", "tools"]
date = 2026-10-12T04:02:37+02:00
draft = false
+++

Cloudflare heeft Clef-omni uitgebracht, een multimodale classifier die tekst, beelden, audio en video accepteert maar getypeerde antwoorden teruggeeft in plaats van gegenereerd proza.

Het model breidt de Clef-classificatiefamilie uit met Qwen3-Omni als basis. Cloudflare bevroor die basis, trainde lichte adapters en voegde een kop toe die invoer in één voorwaartse doorgang rechtstreeks op een door de gebruiker bepaald labelschema afbeeldt.

## Waarom dit ertoe doet {#why-it-matters}

Voor een ontwikkelaar die ondersteuningsberichten sorteert, productfoto's inspecteert of korte clips routeert, biedt Clef-omni één classificatie-interface voor verschillende mediatypen. Dat kan een afzonderlijke transcriptie- of bijschriftfase wegnemen, al heeft Cloudflare geen onafhankelijke vergelijkingen van begin tot eind met zulke pijplijnen gepubliceerd.

Cloudflare zegt dat Clef-omni een mixture-of-experts-model met 30 miljard parameters is dat voor invoer ongeveer 3 miljard parameters activeert. In de Workers AI-metingen van het bedrijf duurde tekstclassificatie ongeveer 130 milliseconden, beelden ongeveer 150 milliseconden en een video van 21 seconden met audio ongeveer 1,5 seconden. Die tijden zijn tests van de aanbieder en variëren met invoergrootte, wachtrijen en uitrol.

Het benchmarkbeeld is gemengd en niet overal beter. Cloudflares tabel plaatst de oudere dichte Clef vóór op verschillende teksttaken, terwijl Clef-omni hem op de BANKING77-intentiedataset nipt overtreft, met 94,8 tegenover 94,2 procent. Het praktische onderscheid van het nieuwe model is zijn invoerbereik, geen algemene claim van hogere tekstnauwkeurigheid.

Cloudflare wijzigde ook de voorwaarden voor Clef-flash. De vermelde invoerprijs daalde van 0,09 naar 0,038 dollar per miljoen tokens, terwijl het contextvenster van 64.000 naar 24.000 tokens daalde. Clef blijft 0,24 dollar per miljoen inputtokens en Clef-omni begint op 0,15 dollar.

De Clef-omni-gewichten zijn onder Apache 2.0 beschikbaar op Hugging Face. De modelkaart noemt ongeveer 35,3 miljard parameters in totaal en zegt dat de huidige aangepaste loader ongeveer 64 GB BF16-geheugen op een GPU van de H200-klasse nodig heeft. Cloudflare zegt dat SGLang-ondersteuning gepland is, maar noemt geen releasedatum.

## Waarop te letten

De open gewichten maken onafhankelijke tests van vertraging, kalibratie en nauwkeurigheid nu mogelijk. Ondersteuning in een gangbare serverengine is relevant voor teams die het model buiten Workers AI willen draaien zonder Cloudflares aangepaste loader te onderhouden.

## Verificatie {#verification}

| Bewering | Label | Primaire bron | Onafhankelijke verificatie |
|---|---|---|---|
| Cloudflare bracht Clef-omni uit met tekst-, beeld-, audio- en video-invoer en getypeerde classificatie-uitvoer | GEVERIFIEERD | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ | https://huggingface.co/Cloudflare/clef-omni |
| Cloudflare meldt ongeveer 130 ms voor tekst, 150 ms voor beelden en 1,5 s voor een audiovisuele clip van 21 seconden | VOLGENS HET BEDRIJF | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ | geen |
| Cloudflares tabel meldt 94,8% op BANKING77 voor Clef-omni en 94,2% voor Clef | VOLGENS HET BEDRIJF | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ | geen |
| Clef-flash kost nu 0,038 dollar per miljoen inputtokens en heeft een contextvenster van 24.000 tokens | GEVERIFIEERD | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ | geen |
| Apache-2.0-gewichten en een aangepaste loader zijn beschikbaar; SGLang-ondersteuning is gepland | GEVERIFIEERD | https://huggingface.co/Cloudflare/clef-omni | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ |
