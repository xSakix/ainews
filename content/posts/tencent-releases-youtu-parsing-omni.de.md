+++
title = "Tencent veröffentlicht Youtu-Parsing-Omni"
slug = "tencent-veroeffentlicht-youtu-parsing-omni"
description = "Das Modell mit fünf Milliarden Parametern wandelt Dokumente, Bilder, Audio und Video in ein einheitliches strukturiertes JSON-Format um. Tencent hat Gewichte, Code und einen technischen Bericht veröffentlicht."
tags = ["models", "tools"]
date = 2026-10-10T04:02:41+02:00
draft = false
+++

Tencents Youtu-Labor hat ein Modell mit fünf Milliarden Parametern veröffentlicht, das sechs Medienarten in ein einheitliches strukturiertes JSON-Format überführt.

Youtu-Parsing-Omni akzeptiert Dokumentseiten, natürliche Bilder, Diagramme, geometrische Abbildungen, Audio und Video. Es kann Text, Tabellen, Formeln, Layout-Rahmen, Zeitstempel, Sprachtranskripte, Bildbeschreibungen und Beschreibungen von Kamerabewegungen ausgeben, ohne zwischen separaten Spezialmodellen zu wechseln.

## Warum das wichtig ist {#why-it-matters}

Wer ein Such- oder Dokumentenverarbeitungssystem entwickelt, kann gemischte Medien durch ein lokales Modell schicken und ein vorhersehbares Schema erhalten. Das reduziert die Integrationsarbeit, die gewöhnlich für die Verbindung von Texterkennung, Spracherkennung und Videoverständnis nötig ist.

Tencent hat die Gewichte unter seiner eigenen `youtu-parsing`-Lizenz, ein vLLM-Plugin, Inferenzbeispiele und einen technischen Bericht veröffentlicht. Laut Repository soll Evaluationscode folgen. Die berichteten Benchmarkwerte lassen sich daher allein mit der Veröffentlichung noch nicht reproduzieren.

Das Modell verwendet einen gemeinsamen Encoder für Bilder, Audio und Video. Bei Videos können ausgewählte Schichten jedes Bild auf Audio aus demselben Abschnitt des Clips zugreifen lassen. Das Ausgabeschema deckt sowohl wörtliche Elemente wie Text und Begrenzungsrahmen als auch höherstufige Ausgaben wie Erzählungen und Berichte ab.

Tencent meldet in seiner Tabelle 96,96 auf OmniDocBench 1.6, knapp vor TeleOCR mit 96,91 und PaddleOCR-VL-1.6 mit 96,34. Auf dem breiteren OmniParsingBench nennt Tencent einen Durchschnitt von 75,08, hinter Gemini 3 Pro mit 77,44, aber vor den übrigen getesteten Systemen mit offenen Gewichten. Das sind Messungen des Herausgebers; der Vergleich hängt von der Benchmarkkonfiguration im Bericht ab.

Die Trainingsmethode macht das Schülermodell wiederholt zum Lehrer der nächsten Runde. Inhalts- und Struktur-Token erhalten unterschiedliche Vergleichssignale. Damit sollen sowohl der Inhalt einer Seite als auch die Beziehungen ihrer Elemente erhalten bleiben.

## Was ansteht

Unabhängige Durchläufe benötigen den versprochenen Evaluationscode. Gewerbliche Nutzer müssen zudem die eigene Lizenz prüfen, statt die freizügigen Bedingungen mancher Veröffentlichungen mit offenen Gewichten vorauszusetzen.

## Überprüfung {#verification}

| Behauptung | Einstufung | Primärquelle | Unabhängige Überprüfung |
|---|---|---|---|
| Tencent veröffentlichte Youtu-Parsing-Omni mit fünf Milliarden Parametern, Gewichten, Codebeispielen und technischem Bericht | VERIFIZIERT | https://huggingface.co/tencent/Youtu-Parsing-Omni | https://github.com/TencentYoutuResearch/Youtu-Parsing-Omni |
| Das Modell akzeptiert Dokumente, Bilder, Diagramme, Geometrie, Audio und Video und gibt ein einheitliches JSON-Schema aus | LAUT UNTERNEHMEN | https://huggingface.co/tencent/Youtu-Parsing-Omni | keine |
| Tencent meldet 96,96 auf OmniDocBench 1.6 und 75,08 auf OmniParsingBench | LAUT UNTERNEHMEN | https://huggingface.co/tencent/Youtu-Parsing-Omni | keine |
| Die Veröffentlichung nutzt die eigene youtu-parsing-Lizenz und enthält noch keinen Evaluationscode | VERIFIZIERT | https://huggingface.co/tencent/Youtu-Parsing-Omni | https://github.com/TencentYoutuResearch/Youtu-Parsing-Omni |
