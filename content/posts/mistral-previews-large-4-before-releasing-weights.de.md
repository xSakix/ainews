+++
title = "Mistral stellt Large 4 vor der Gewichtsveröffentlichung vor"
slug = "mistral-stellt-large-4-vor-gewichtsveroeffentlichung-vor"
description = "Mistral hat den API-Zugang zu seinem multimodalen Modell mit einer Billion Parametern geöffnet und den 27. Oktober für die offenen Gewichte angesetzt. Architektur- und Benchmark-Angaben bleiben damit vorläufig."
tags = ["models", "business"]
date = 2026-10-07T04:00:57+02:00
draft = false
+++

Mistral hat eine öffentliche API-Vorschau auf Mistral Large 4 geöffnet und die herunterladbaren Gewichte des Modells für den 27. Oktober angekündigt.

Das französische Unternehmen beschreibt das Modell als multimodales Mixture-of-Experts-Modell, das von Grund auf in seinen europäischen Rechenzentren trainiert worden sei. Es akzeptiert Text und Bilder, unterstützt mehr als 160 Sprachen und hat ein Kontextfenster von einer Million Token.

## Warum das wichtig ist {#why-it-matters}

Eine Organisation, die ein selbst gehostetes europäisches Modell erwägt, kann Large 4 jetzt testen, die versprochenen Gewichte aber noch nicht prüfen oder einsetzen. Diese Lücke macht es zu einer Vorschau mit einem zugesagten Liefertermin statt zu einer abgeschlossenen Veröffentlichung offener Gewichte.

Mistrals Ankündigung nennt insgesamt eine Billion Parameter und 49 Milliarden aktive Parameter pro Token. Die Dokumentation nennt dagegen insgesamt 1,05 Billionen, 52 Milliarden aktive Parameter und einen Bild-Encoder mit 1,6 Milliarden Parametern. Der Unterschied könnte auf Rundung oder eine geänderte Konfiguration zurückgehen. Mistral hat aber keinen technischen Bericht veröffentlicht, der die Zahlen miteinander in Einklang bringt.

Das Unternehmen betont die Cybersicherheit. Es meldet 82 % im Teil „Reproduzieren, dann Beheben“ von CyberGym-E2E, 93 % auf Cybench und 61,7 % auf DeepSWE v1.1. Einige Evaluierungen nennen externe Anbieter, doch der zusammengestellte Vergleich und die meisten zentralen Aussagen stehen in Mistrals eigenen Veröffentlichungsmaterialien.

Vor dem Erscheinen der Gewichte sollen laut Mistral Cybersicherheitsspezialisten und Behörden eine Version mit reduzierter Moderation testen. Das Unternehmen argumentiert, gewöhnliche sicherheitsbedingte Ablehnungen könnten defensive Arbeit behindern. Die Vorschau soll diesen Zielkonflikt untersuchen.

Die API-Preise beginnen bei 1,36 Dollar pro Million Eingabe-Token und 4,18 Dollar pro Million Ausgabe-Token. Mistral Studio bietet Modi mit und ohne Reasoning an. Lizenz und endgültige Anforderungen für den Einsatz bleiben bis zur Veröffentlichung der Gewichte unbekannt.

Der entscheidende Termin ist der 27. Oktober. Modellkarte, technischer Bericht, Lizenz und herunterladbare Dateien werden zeigen, ob das öffentliche Artefakt dem Umfang und den Fähigkeiten der Vorschau entspricht.

## Überprüfung {#verification}

| Behauptung | Einstufung | Primärquelle | Unabhängige Überprüfung |
| --- | --- | --- | --- |
| Mistral öffnete eine API-Vorschau auf Large 4 und setzte die Gewichte für den 27. Oktober an | VERIFIZIERT | [Mistral-Ankündigung](https://mistral.ai/news/mistral-large-4/) | [Mistral-Dokumentation](https://docs.mistral.ai/models/mistral-large-4) |
| Die Ankündigung nennt insgesamt 1 Billion und 49 Milliarden aktive Parameter | VERIFIZIERT | [Mistral-Ankündigung](https://mistral.ai/news/mistral-large-4/) | die Dokumentation nennt andere Zahlen |
| Die Dokumentation nennt insgesamt 1,05 Billionen, 52 Milliarden aktive Parameter und einen Bild-Encoder mit 1,6 Milliarden Parametern | VERIFIZIERT | [Mistral-Dokumentation](https://docs.mistral.ai/models/mistral-large-4) | keine |
| Das Modell erreichte 82 % auf CyberGym-E2E im Teil Reproduzieren-dann-Beheben, 93 % auf Cybench und 61,7 % auf DeepSWE v1.1 | LAUT UNTERNEHMEN | [Mistral-Ankündigung](https://mistral.ai/news/mistral-large-4/) | benannte Prüfer bestätigen nicht unabhängig den gesamten Vergleich |
| Die API kostet 1,36 Dollar für Eingaben und 4,18 Dollar für Ausgaben pro Million Token | VERIFIZIERT | [Mistral-Dokumentation](https://docs.mistral.ai/models/mistral-large-4) | aktuelle Dokumentation |
