+++
title = "Nish Tahir kalibriert ein kleines Entscheidungsmodell neu"
slug = "nish-tahir-kalibriert-ein-kleines-entscheidungsmodell-neu"
description = "Ein ausführbares Experiment macht Qwen3-1.7B zum Klassifikator mit einem Durchlauf und zeigt anschließend seine überhöhte Konfidenz. Temperaturskalierung verbessert die Wahrscheinlichkeiten."
tags = ["models", "research", "essays"]
date = 2026-10-11T04:01:06+02:00
draft = false
+++

Der unabhängige Entwickler Nish Tahir hat ein ausführbares Experiment veröffentlicht, das Qwen3-1.7B in ein Entscheidungsmodell mit einem Durchlauf verwandelt und anschließend misst, wie schlecht seine Konfidenz zur tatsächlichen Genauigkeit passt.

Die Methode beschränkt das Ausgabevokabular des Modells auf die Antwort-Token A bis E und liest deren Wahrscheinlichkeiten nach einem Vorwärtsdurchlauf aus. Auf CommonsenseQA meldet Tahir 59,4 % Genauigkeit für das Basismodell und 62,4 % nach einer kurzen Feinabstimmung.

## Warum das wichtig ist {#why-it-matters}

Wer einen Router oder Risikowert entwickelt, muss mehr wissen als nur, welche Option gewonnen hat. Gibt ein Modell 95 % an, liegt aber nur in sieben von zehn Fällen richtig, verhalten sich auf diesem Wert beruhende Schwellen unvorhersehbar. Tahirs Experiment zeigt den vollständigen Weg von Logits zu einem gemessenen Kalibrierungsproblem, mit einem Modell, das klein genug zur Reproduktion ist.

Der Genauigkeitsgewinn ist nicht das aufschlussreichste Ergebnis. Antworten mit einer zugewiesenen Konfidenz zwischen 90 % und 100 % waren nur in etwa 70 % der Fälle richtig. Im Bereich von 80 % bis 90 % lag die Genauigkeit bei rund 40 %. Das Modell unterschied die Möglichkeiten also gut genug, um den Zufall zu schlagen, drückte dabei aber deutlich mehr Sicherheit aus, als seine Ergebnisse rechtfertigten.

Tahir korrigiert die Wahrscheinlichkeiten mit Temperaturskalierung. Die Methode lernt auf zurückgehaltenen Beispielen einen einzelnen Skalar und teilt die Logits vor der Softmax-Operation durch ihn. Eine höhere Temperatur flacht eine übermäßig sichere Verteilung ab, ohne zu verändern, welche Antwort den höchsten Wert erhält.

Damit ist Temperaturskalierung ein Kalibrierungsschritt, keine Verbesserung der Fähigkeiten. Sie kann weder falsche Rangfolgen reparieren noch fehlendes Wissen vermitteln. Ihr Nutzen ist, dass gemeldete 70 % auf Daten, die dem Kalibrierungsdatensatz ähneln, näher an sieben richtigen Fällen von zehn liegen können.

Der Bericht enthält eine kompakte PyTorch-Implementierung und interaktive Demonstrationen. Er macht außerdem eine Gestaltungsentscheidung sichtbar, die viele Produkte für Entscheidungsmodelle verbergen: Das Antwortschema muss im Voraus bekannt sein und sich sauber auf wenige Token abbilden lassen. Eine Aufgabe mit mehrdeutigen Labels, fehlenden Optionen oder mehreren gültigen Antworten durchbricht diese Einfachheit.

Die Ergebnisse stammen von einem kleinen Modell, einem Benchmark und dem Trainingsaufbau des Autors. Die Multiple-Choice-Fragen von CommonsenseQA bilden weder Dokumentenrouting noch Betrugsprüfung oder Werkzeugauswahl ab. Die Kalibrierung kann sich zudem verschieben, wenn sich die Eingabeverteilung ändert. Jede Bereitstellung bräuchte eigene zurückgehaltene Daten und regelmäßige Prüfungen.

Der Artikel ist gerade deshalb nützlich, weil er diese Schwäche berichtet, statt Konfidenzausgaben von vornherein als vertrauenswürdig darzustellen. Code und Demonstrationen sind jetzt verfügbar und geben Praktikern eine kurze Referenz, an der sie größere spezialisierte Entscheidungsmodelle testen können.

## Überprüfung {#verification}

| Behauptung | Einstufung | Primärquelle | Unabhängige Überprüfung |
|---|---|---|---|
| Das Experiment beschränkt Qwen3-1.7B auf Antwort-Token A bis E und liest einen Vorwärtsdurchlauf aus | VERIFIZIERT | https://nishtahir.com/build-your-own-decision-model/ | keine |
| Das Basismodell erreichte 59,4 % und das kurz feinabgestimmte Modell 62,4 % auf CommonsenseQA | LAUT UNTERNEHMEN | https://nishtahir.com/build-your-own-decision-model/ | keine |
| Antworten im Konfidenzbereich von 90 % bis 100 % waren in etwa 70 % der Fälle richtig | LAUT UNTERNEHMEN | https://nishtahir.com/build-your-own-decision-model/ | keine |
| Antworten im Konfidenzbereich von 80 % bis 90 % waren in etwa 40 % der Fälle richtig | LAUT UNTERNEHMEN | https://nishtahir.com/build-your-own-decision-model/ | keine |
| Temperaturskalierung verändert die Schärfe der Wahrscheinlichkeiten, ohne die höchstplatzierte Antwort zu ändern | VERIFIZIERT | https://nishtahir.com/build-your-own-decision-model/ | keine |
