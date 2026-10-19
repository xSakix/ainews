+++
title = "Mehr Schlussfolgern verringert Modellverzerrungen nicht"
slug = "mehr-schlussfolgern-verringert-modellverzerrungen-nicht"
description = "Eine Studie mit 12.350 Aufrufen fand keinen verlässlichen Rückgang bei sechs kognitiven Verzerrungen, wenn Modelle mehr Reasoning-Token nutzten. Ein direkter Prompt half beim Ankereffekt."
tags = ["research", "models"]
date = 2026-10-09T04:02:06+02:00
draft = false
+++

Mehr Zeit zum Schlussfolgern verringerte die Anfälligkeit von Sprachmodellen für Prompts mit kognitiven Verzerrungen nicht zuverlässig. Das zeigt eine neue Studie mit sieben Modellen und 12.350 API-Aufrufen.

Obada Kraishan von der Texas Tech University variierte das Reasoning-Budget von Modellen von Anthropic, OpenAI, DeepSeek und Qwen. Er maß, wie sich ihre Antworten änderten, wenn ein Entscheidungsszenario einen irrelevanten Anker, eine Rahmung oder eine frühere Festlegung enthielt. Keines wurde bei steigendem tatsächlichem Reasoning-Token-Verbrauch durchgehend weniger empfindlich.

**Warum das wichtig ist:** Wer für ein Entscheidungsunterstützungssystem mehr Reasoning-Budget wählt, bezahlt zusätzliche Berechnung. Diese Ergebnisse besagen, dass die zusätzliche Berechnung keine gemessene Verzerrung zuverlässig verbesserte, obwohl Reasoning-Modelle auf Nutzer oft überlegter wirken.

## Die Studie maß tatsächlich erfolgtes Denken

Das Experiment nutzte 30 gepaarte Szenarien zu Ankereffekt, Framing, Verlustaversion, Eskalation des Festhaltens an Entscheidungen, Verfügbarkeit und Bestätigungsfehler. Jedes Paar enthielt dieselben entscheidungsrelevanten Informationen, doch eine Version ergänzte das Merkmal, das menschliche Urteile verschieben sollte. Zehn wiederholte Stichproben je Bedingung erlaubten, die Änderung der gewählten Optionen zu messen.

Das Panel aus sieben Modellen paarte Reasoning- und Nicht-Reasoning-Versionen innerhalb von vier Familien. Angeforderte Reasoning-Obergrenzen betrugen null, 1.024, 4.096 und 8.192 Token, wobei die verfügbaren Kombinationen nach Anbieter variierten. Kraishan protokollierte tatsächlich verbrauchte Token, weil die API-Einstellung oft nicht in eine entsprechende Denkmenge übersetzt wurde.

Diese Unterscheidung war wichtig. Das Anthropic-Modell erhöhte mit der Obergrenze seinen mittleren Reasoning-Verbrauch, blieb aber deutlich unter den höheren Limits. OpenAIs getestetes Modell nutzte oberhalb von null fast dieselbe Menge, während DeepSeek-R1 und Qwen3 gelegentlich eine angeforderte Grenze von 1.024 Token überschritten. Die Hauptanalyse betrachtete deshalb den tatsächlichen Verbrauch als Dosis.

Reasoning-Modelle waren nicht zuverlässig weniger verzerrt als ihre Vergleichsmodelle. Die Unterschiede tendierten in allen vier Familien sogar zu etwas höherer Anfälligkeit; die zusammengefasste Schätzung war aber zu unsicher für diese stärkere Aussage. Wichtiger für die Kernfrage: Kein Modell zeigte einen statistisch verlässlichen Rückgang bei höherem Reasoning-Token-Verbrauch.

Der Befund ist eng begrenzt. Die Testbatterie enthielt fünf Aufgaben für jede von sechs Verzerrungen, alle aus Managemententscheidungen. Einige Familienvergleiche nutzten Geschwistermodelle, statt Reasoning bei identischen Gewichten ein- und auszuschalten. Getestet wird Verhalten unter kontrollierten Prompts, nicht die Richtigkeit offener Arbeitsentscheidungen.

## Der Ankereffekt reagierte auf eine direkte Anweisung

Der Ankereffekt war die einzige getestete Verzerrung, die Modelle konsistent in dieselbe Richtung bewegte wie gewöhnlich Menschen. Eine Zahl im Prompt zog die Schätzungen aller sieben Modelle zu sich. Vier weitere Kategorien tendierten in die Gegenrichtung, während Verfügbarkeit keinen zuverlässigen Effekt zeigte.

Bei den fünf Ankeraufgaben ergänzte der Autor einen Satz, der das Modell aufforderte, den Anker vor der Antwort erneut zu nennen. Der Ankereffekt sank bei jeder Aufgabe. Das Gesamtergebnis verfehlte die Signifikanzschwelle der Studie knapp. Es ist deshalb eine vielversprechende Beobachtung statt bestätigter Gegenmaßnahme; zusätzliches Reasoning allein erzeugte aber keinen vergleichbaren Rückgang.

Dieser Kontrast ist das praktischste Ergebnis der Arbeit. Eine gezielte Anweisung kann ändern, welche Informationen das Modell verarbeitet; mehr Reasoning-Budget gibt dem bestehenden Prozess nur mehr Raum. Das Experiment beweist nicht, dass erneutes Nennen von Zahlen über fünf Prompts hinaus generalisiert. Es zeigt aber, warum Recheneinstellungen und Verzerrungskontrollen getrennt bewertet werden sollten.

Der Preprint wurde am 7. Oktober eingereicht und bei IEEE CogMI 2026 angenommen. Der Autor veröffentlichte die eingefrorene Prompt-Batterie, Token-Aufzeichnungen je Aufruf und Analysecode im [Anchored-Minds-Repository](https://github.com/obadaKraishan/anchored-minds), sodass das Ergebnis an neueren Modellen und größeren Aufgabensätzen getestet werden kann.

## Überprüfung {#verification}

| Behauptung | Einstufung | Primärquelle | Unabhängige Überprüfung |
|---|---|---|---|
| Die Studie führte 12.350 Aufrufe über sieben Modelle in vier Familien aus | LAUT UNTERNEHMEN | [Arbeit](https://arxiv.org/abs/2610.10049) | [Code und Daten](https://github.com/obadaKraishan/anchored-minds) |
| Sie nutzte 30 Szenarien zu sechs kognitiven Verzerrungen | LAUT UNTERNEHMEN | [Arbeit](https://arxiv.org/abs/2610.10049) | [Code und Daten](https://github.com/obadaKraishan/anchored-minds) |
| Angeforderte Obergrenzen und tatsächlicher Reasoning-Verbrauch unterschieden sich je Anbieter | LAUT UNTERNEHMEN | [Arbeit](https://arxiv.org/abs/2610.10049) | [Code und Daten](https://github.com/obadaKraishan/anchored-minds) |
| Kein getestetes Modell zeigte bei mehr Reasoning-Token einen zuverlässigen Rückgang der Verzerrungsstärke | LAUT UNTERNEHMEN | [Arbeit](https://arxiv.org/abs/2610.10049) | keine |
| Reasoning-Modelle waren nicht zuverlässig weniger verzerrt als Familienvergleichsmodelle | LAUT UNTERNEHMEN | [Arbeit](https://arxiv.org/abs/2610.10049) | keine |
| Der Ankereffekt verlief bei allen sieben Modellen in der menschlichen Richtung | LAUT UNTERNEHMEN | [Arbeit](https://arxiv.org/abs/2610.10049) | keine |
| Den Anker erneut zu nennen senkte den Effekt bei allen fünf Aufgaben, verfehlte aber die Signifikanzschwelle | LAUT UNTERNEHMEN | [Arbeit](https://arxiv.org/abs/2610.10049) | keine |
| Die Arbeit wurde bei IEEE CogMI 2026 angenommen und veröffentlichte Code und Daten | VERIFIZIERT | [Arbeit](https://arxiv.org/abs/2610.10049) | [Repository](https://github.com/obadaKraishan/anchored-minds) |
