+++
title = "Cloudflare ergänzt multimodales Clef-omni"
slug = "cloudflare-ergaenzt-multimodales-clef-omni"
description = "Der neue Klassifikator behält Qwen3-Omnis Bild-, Audio- und Videoeingaben bei und liefert typisierte Antworten statt erzeugter Prosa. Cloudflare senkte außerdem den Preis und verkleinerte das Kontextfenster von Clef-flash."
tags = ["models", "tools"]
date = 2026-10-12T04:02:37+02:00
draft = false
+++

Cloudflare hat Clef-omni veröffentlicht, einen multimodalen Klassifikator, der Text, Bilder, Audio und Video akzeptiert, aber typisierte Antworten statt erzeugter Prosa liefert.

Das Modell erweitert die Clef-Klassifikationsfamilie mit Qwen3-Omni als Basis. Cloudflare fror diese Basis ein, trainierte leichtgewichtige Adapter und ergänzte einen Kopf, der eine Eingabe in einem einzigen Vorwärtsdurchlauf direkt auf ein nutzerdefiniertes Labelschema abbildet.

## Warum das wichtig ist {#why-it-matters}

Für Entwickler, die Supportnachrichten sortieren, Produktfotos prüfen oder kurze Clips zuordnen, bietet Clef-omni eine gemeinsame Klassifikationsschnittstelle für mehrere Medientypen. Das kann eine separate Transkriptions- oder Bildbeschriftungsstufe überflüssig machen, wobei Cloudflare keine unabhängigen Ende-zu-Ende-Vergleiche mit solchen Verarbeitungsketten veröffentlicht hat.

Cloudflare erklärt, Clef-omni sei ein Mixture-of-Experts-Modell mit 30 Milliarden Parametern, das für eine Eingabe rund 3 Milliarden Parameter aktiviere. In den Workers-AI-Messungen des Unternehmens dauerte Textklassifikation rund 130 Millisekunden, die Verarbeitung von Bildern rund 150 Millisekunden und die eines 21-sekündigen Videos mit Audio rund 1,5 Sekunden. Diese Zeiten sind Anbietertests und variieren mit Eingabegröße, Warteschlangen und Bereitstellung.

Das Benchmark-Bild ist gemischt statt durchgehend besser. Cloudflares Tabelle sieht das ältere dichte Clef bei mehreren Textaufgaben vorn, während Clef-omni beim Intent-Datensatz BANKING77 knapp führt: 94,8 % gegenüber 94,2 %. Der praktische Unterschied des neuen Modells liegt in seiner Eingabebreite, nicht in einem allgemeinen Anspruch auf höhere Textgenauigkeit.

Cloudflare änderte auch die Bedingungen für Clef-flash. Sein angegebener Eingabepreis sank von 0,09 auf 0,038 Dollar pro Million Token, während das Kontextfenster von 64.000 auf 24.000 Token schrumpfte. Clef bleibt bei 0,24 Dollar pro Million Eingabe-Token, und Clef-omni startet bei 0,15 Dollar.

Die Clef-omni-Gewichte sind unter Apache 2.0 auf Hugging Face verfügbar. Die Modellkarte nennt insgesamt rund 35,3 Milliarden Parameter und erklärt, der aktuelle benutzerdefinierte Loader benötige etwa 64 GB BF16-Speicher auf einer GPU der H200-Klasse. Cloudflare erklärt, SGLang-Unterstützung sei geplant, nennt aber kein Veröffentlichungsdatum.

## Was ansteht

Die offenen Gewichte ermöglichen jetzt unabhängige Latenz-, Kalibrierungs- und Genauigkeitstests. Unterstützung in einer gängigen Inferenz-Engine wird für Teams wichtig sein, die das Modell außerhalb von Workers AI betreiben wollen, ohne Cloudflares eigenen Loader zu pflegen.

## Überprüfung {#verification}

| Behauptung | Einstufung | Primärquelle | Unabhängige Überprüfung |
|---|---|---|---|
| Cloudflare veröffentlichte Clef-omni mit Text-, Bild-, Audio- und Videoeingaben sowie typisierten Klassifikationsausgaben | VERIFIZIERT | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ | https://huggingface.co/Cloudflare/clef-omni |
| Cloudflare meldet rund 130 ms für Text, 150 ms für Bilder und 1,5 s für einen 21-sekündigen audiovisuellen Clip | LAUT UNTERNEHMEN | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ | keine |
| Cloudflares Tabelle meldet 94,8 % auf BANKING77 für Clef-omni und 94,2 % für Clef | LAUT UNTERNEHMEN | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ | keine |
| Clef-flash kostet nun 0,038 Dollar pro Million Eingabe-Token und hat ein Kontextfenster von 24.000 Token | VERIFIZIERT | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ | keine |
| Apache-2.0-Gewichte und ein benutzerdefinierter Loader sind verfügbar; SGLang-Unterstützung ist geplant | VERIFIZIERT | https://huggingface.co/Cloudflare/clef-omni | https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ |
