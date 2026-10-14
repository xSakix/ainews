+++
title = "H2O.ai veröffentlicht H2O-Lightning-31B"
slug = "h2oai-veroeffentlicht-h2o-lightning-31b"
description = "Das Entscheidungsmodell mit offenen Gewichten beantwortet begrenzte Fragen in einem Vorwärtsdurchlauf und liefert Wahrscheinlichkeiten. Seine stärksten Geschwindigkeits- und Genauigkeitszahlen stammen aus eigenen Tests von H2O.ai."
tags = ["models", "tools"]
date = 2026-10-11T04:06:06+02:00
draft = false
+++

H2O.ai hat H2O-Lightning-31B veröffentlicht, ein Modell mit offenen Gewichten, das begrenzte Entscheidungsfragen mit Wahrscheinlichkeiten beantwortet, statt frei formulierte Prosa zu erzeugen.

Das Modell basiert auf Gemma 4 31B-it und akzeptiert Text sowie bis zu vier Bilder. Seine Schnittstelle umfasst Auswahlmöglichkeiten, Ja-Nein-Fragen und geordnete Bewertungen und liefert ein Ergebnis in einem einzigen Vorwärtsdurchlauf. H2O.ai veröffentlichte Gewichte, Modellkarte und Inferenzcode auf Hugging Face.

## Warum das wichtig ist {#why-it-matters}

Für Entwickler, die einen großen Chatbot zur Ticketverteilung, Datensatzbewertung oder Werkzeugauswahl nutzen, kann beschränkte Ausgabe mehrere fragile Schritte entfernen: JSON per Prompt verlangen, es parsen, fehlerhafte Antworten verwerfen und erneut fragen. Eine Wahrscheinlichkeit zeigt auch, wie knapp die Wahl war, ist aber nur nützlich, wenn das Modell für die vorgesehenen Daten kalibriert ist.

H2O.ai berichtet, das Modell mit 31 Milliarden Parametern habe 212 von 231 öffentlichen JevBench-Fragen richtig beantwortet. In der Bildevaluierung erreichte das feinabgestimmte Modell 88,4 % über 1.877 Fragen, verglichen mit 88,0 % für die eingefrorene Gemma-Basis. Das Unsicherheitsintervall der Modellkarte schließt keine Verbesserung ein; dieses Bildergebnis etabliert daher keinen verlässlichen Gewinn gegenüber dem Basismodell.

Das Unternehmen meldet auch rund 25 Millisekunden mediane Latenz, wenn das Modell in FP8 auf einer NVIDIA H100 geladen wird. Die Zahl stammt aus der eigenen Konfiguration mit deaktiviertem Präfixcache, und die Karte bietet keine Messung für kleinere GPUs. Die veröffentlichten bfloat16-Dateien umfassen vor Laufzeitmehrbedarf rund 63 GB.

Die Veröffentlichung läuft auf unverändertem vLLM 0.30.0 hinter H2O.ais `/v1/systemone`-Zwischenschicht. Lange Datensätze werden nicht vollständig verarbeitet: Eine Abrufstufe kürzt sie vor der Inferenz auf 3.000 Token. Diese Grenze ist wichtig, weil eine Entscheidung nur die Belege widerspiegeln kann, die der Abrufschritt bewahrt.

Die Gewichte tragen Apache 2.0 neben Googles Gemma-Bedingungen. H2O.ais Hinweis verweist ausdrücklich auf Gemmas Verbote automatisierter Entscheidungen, die individuelle Rechte betreffen. Die offenen Dateien machen daher nicht jeden Einsatz zulässig.

H2O.ai aktualisierte auch das frühere 4B-Schwestermodell mit überarbeiteten Latenzmessungen und einem GGUF-Paket für llama.cpp. Die 31B-Veröffentlichung ist jetzt über die Hugging-Face-Modellseite verfügbar; unabhängige Tests zu Latenz, Kalibrierung und Aufgabenqualität wurden noch nicht veröffentlicht.

## Überprüfung {#verification}

| Behauptung | Einstufung | Primärquelle | Unabhängige Überprüfung |
|---|---|---|---|
| H2O.ai veröffentlichte H2O-Lightning-31B mit Gewichten, Modellkarte und Inferenzcode | VERIFIZIERT | https://huggingface.co/h2oai/h2o-lightning-31b | keine |
| Das Modell unterstützt begrenzte Text-Bild-Entscheidungen und liefert Wahrscheinlichkeiten in einem Vorwärtsdurchlauf | VERIFIZIERT | https://huggingface.co/h2oai/h2o-lightning-31b | keine |
| Es erreichte 212 von 231 JevBench-Aufgaben und rund 25 ms mediane Latenz auf einer H100 | LAUT UNTERNEHMEN | https://huggingface.co/h2oai/h2o-lightning-31b | keine |
| Seine Bildevaluierung zeigte keinen statistisch verlässlichen Gewinn gegenüber der eingefrorenen Gemma-Basis | VERIFIZIERT | https://huggingface.co/h2oai/h2o-lightning-31b | keine |
| Gemma-Bedingungen beschränken automatisierte Entscheidungen mit Auswirkungen auf individuelle Rechte | VERIFIZIERT | https://huggingface.co/h2oai/h2o-lightning-31b | keine |
