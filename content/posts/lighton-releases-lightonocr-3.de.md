+++
title = "LightOn veröffentlicht LightOnOCR-3"
slug = "lighton-veroeffentlicht-lightonocr-3"
description = "Die Apache-2.0-Modellfamilie kombiniert Transkription, Layout-Rahmen, Bildbeschreibungen und Diagrammextraktion in Modellen, die klein genug für lokalen Betrieb sind."
tags = ["models", "tools"]
date = 2026-10-09T04:04:06+02:00
draft = false
+++

Das französische KI-Unternehmen LightOn hat LightOnOCR-3 veröffentlicht, eine Familie von Dokumentenmodellen mit offenen Gewichten, die Text, Seitenstruktur, Bildbeschreibungen und Diagrammdaten in einem Durchlauf ausgeben können.

Die Familie erscheint mit 0,8 Milliarden, 1 Milliarde und 4 Milliarden Parametern unter Apache 2.0. Ein leerer Prompt erzeugt eine herkömmliche Transkription; der Prompt `grounding` ergänzt beschriftete Bereiche mit Koordinaten, beschreibt Bilder und verwandelt Diagramme in HTML-Tabellen.

**Warum das wichtig ist:** Wer eine private Dokumentenpipeline entwickelt, kann diese Modelle prüfen und lokal betreiben, statt Seiten an einen gehosteten Dienst zu schicken oder separate Systeme für OCR, Layouterkennung und Diagrammextraktion zu verbinden.

LightOn behielt für das 1B-Modell die frühere Architektur bei. Diese Variante ist damit ein direktes Upgrade bestehender LightOnOCR-2-Einsätze. Die kleinere und größere Version nutzen die Qwen3.5-Vision-Language-Architektur. LightOn veröffentlichte außerdem Konvertierungs- und Visualisierungswerkzeuge, Modellgewichte und die Skripte zur Reproduktion seiner Benchmarkwerte.

Das stärkste Hauptergebnis stammt aus LightOns eigenen Tests. Sein 4B-Modell erreichte 86,3 auf dem 512-seitigen olmOCR-Benchmark, 1,3 Punkte hinter Infinity Parser Pro mit 35,1 Milliarden Parametern und einen halben Punkt vor dem anderen 4B-Modell Chandra 2. Der Vergleich ist nützlich, weil die Modelle unter einer gemeinsamen Bereitstellungskonfiguration liefen. Er bleibt jedoch eine Herstellerevaluierung, und Ausgabenormalisierung kann OCR-Werte erheblich verändern.

Die strukturierte Ausgabe ist bewusst kompakt. Laut LightOn erzeugten die Versionen mit 0,8 und 4 Milliarden Parametern auf denselben Seiten 9–14 % weniger Token als zwei konkurrierende Parser und lieferten zugleich Rahmen und Bildbeschreibungen. Bei der jeweils bevorzugten Benchmarkauflösung hatte die 1B-Version mit 2,7 Sekunden auf einer NVIDIA H100 die niedrigste gemeldete Einzelseitenlatenz.

Die Trainingsdarstellung ist für einen Veröffentlichungsbeitrag ungewöhnlich detailliert. LightOn beschreibt die Kombination mehrerer Detektoren, das Verwerfen mehrdeutiger Seitenannotationen und ein großes Bildmodell zur Beschriftung von Abbildungen. Das Benchmarkrepository enthalte auch Nachverarbeitungsregeln. Diese sind wichtig, weil gleichwertige Fußnoten oder Formeln je nach Formatierung unterschiedliche Editierdistanzwerte erhalten können.

Alle drei Gewichte, eine Demo und der unterstützende Code sind jetzt über [LightOns Veröffentlichungsbeitrag](https://huggingface.co/blog/lightonai/lightonocr-3) verfügbar. Unabhängige Tests müssen zeigen, wie zuverlässig Diagrammwerte und Rahmen bei Dokumenten außerhalb von LightOns Bewertungssätzen bleiben.

## Überprüfung {#verification}

| Behauptung | Einstufung | Primärquelle | Unabhängige Überprüfung |
|---|---|---|---|
| LightOn veröffentlichte drei LightOnOCR-3-Varianten unter Apache 2.0 | VERIFIZIERT | [Veröffentlichungsbeitrag](https://huggingface.co/blog/lightonai/lightonocr-3) | [4B-Modellkarte](https://huggingface.co/lightonai/LightOnOCR-3-4B) |
| Der Grounding-Modus liefert beschriftete Rahmen, Bildbeschreibungen und Diagrammtabellen | VERIFIZIERT | [Veröffentlichungsbeitrag](https://huggingface.co/blog/lightonai/lightonocr-3) | keine |
| Das 1B-Modell behält die vorherige Architektur; 0,8B und 4B verwenden Qwen3.5 VLM | VERIFIZIERT | [Veröffentlichungsbeitrag](https://huggingface.co/blog/lightonai/lightonocr-3) | keine |
| LightOn veröffentlichte Gewichte, Hilfsprogramme und Skripte zur Benchmarkreproduktion | VERIFIZIERT | [Veröffentlichungsbeitrag](https://huggingface.co/blog/lightonai/lightonocr-3) | [4B-Modellkarte](https://huggingface.co/lightonai/LightOnOCR-3-4B) |
| Das 4B-Modell erreichte 86,3 auf olmOCR-Bench | LAUT UNTERNEHMEN | [Veröffentlichungsbeitrag](https://huggingface.co/blog/lightonai/lightonocr-3) | keine |
| Ausgewählte Modelle erzeugten 9–14 % weniger Token als benannte Konkurrenten | LAUT UNTERNEHMEN | [Veröffentlichungsbeitrag](https://huggingface.co/blog/lightonai/lightonocr-3) | keine |
| Das 1B-Modell hatte 2,7 Sekunden Einzelseitenlatenz auf einer H100 | LAUT UNTERNEHMEN | [Veröffentlichungsbeitrag](https://huggingface.co/blog/lightonai/lightonocr-3) | keine |
