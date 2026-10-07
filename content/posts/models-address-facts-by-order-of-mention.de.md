+++
title = "Modelle adressieren Fakten nach der Reihenfolge ihrer Erwähnung"
slug = "modelle-adressieren-fakten-reihenfolge-erwaehnung"
description = "Ein Preprint findet eine gemeinsame interne Richtung, die Sprachmodelle zum ersten, zweiten oder späteren Fakt einer Passage führt. Eine Frage entlang dieser Richtung zu verschieben kann ändern, welchen Fakt das Modell abruft."
tags = ["research", "models"]
date = 2026-10-06T04:08:31+02:00
draft = false
+++

Sprachmodelle scheinen Fakten in einer Passage teilweise anhand der Reihenfolge zu finden, in der diese erwähnt wurden. Das berichtet eine neue Interpretierbarkeitsstudie.

Yufa Zhou testete Qwen-, Gemma- und Llama-Modelle mit kurzen Listen faktischer Aussagen und anschließenden Fragen. Die internen Fragezustände der Modelle bildeten ein wiederholbares Muster für den ersten, zweiten und spätere Fakten, selbst wenn Namen und Themen wechselten.

## Warum das wichtig ist {#why-it-matters}

Für Forscher, die den Informationsabruf innerhalb eines Modells verstehen wollen, liefert das Ergebnis einen konkreten Mechanismus statt einer weiteren Korrelation zwischen Aktivierungen und Antworten. Dieselbe interne Richtung ließ sich experimentell verschieben. Dadurch rief eine Frage zu einem Fakt einen anderen Fakt aus der Passage ab.

Das Paper nennt diese Positionen „Faktenadressen“. Ein Beispielkontext sagt, Alice esse einen Apfel und Bob eine Birne. Eine Frage zu Alice und eine zu Bob unterscheiden sich im Modell entlang einer Richtung, die mit der Reihenfolge der Erwähnung der Fakten zusammenhängt. Als der Forscher die Richtung vom ersten zum zweiten Fakt zu einer Frage nach dem ersten hinzufügte, antwortete das Modell häufig mit dem Inhalt des zweiten.

Dieser Eingriff ist der stärkste Beleg der Studie. Ein Klassifikator kann viele Muster in verborgenen Zuständen entdecken, ohne zu zeigen, dass ein Modell sie nutzt. Die Antwort durch Ändern der vorgeschlagenen Adresse zu verändern stützt den Mechanismus kausal. Die Tests nutzen allerdings kontrollierte Faktenlisten statt langer natürlicher Dokumente.

Über 64 neue Wortsätze hinweg wählte der Eingriff bei Qwen in etwa fünf von sechs Fällen den beabsichtigten Fakt aus, bei Gemma in ungefähr der Hälfte und bei Llama in etwa einem von drei Fällen. Die genauen Quoten betrugen 84,1 %, 53,9 % und 36,2 %. Diese Unterschiede zeigen, dass die Richtung über Modellfamilien hinweg vorhanden, aber nicht in jeder gleich zuverlässig war.

## Die Adressen belegen einen kleinen internen Raum

Zhou berichtet, die Faktenadressen lägen in einem Unterraum niedrigen Rangs. Vereinfacht bedeutet das: Die Modelle benötigen nicht für jede mögliche Position eine separate, unverbundene Richtung. Eine kleine Gruppe von Richtungen beschreibt einen Großteil des Reihenfolgemusters.

Den zuerst erwähnten Fakt konnten die Modelle außerdem leichter erreichen als spätere Fakten. Das ähnelt einem Primäreffekt beim menschlichen Erinnern. Das Experiment belegt aber nicht, dass Menschen und Transformer denselben Mechanismus nutzen. Es identifiziert eine messbare Asymmetrie in den getesteten Modellen.

Das Muster erschien in Schichten im späteren mittleren Bereich und bei Größen von 1,5 Milliarden bis 32 Milliarden Parametern. Während des Trainings gespeicherte Modellstände deuteten darauf hin, dass es sich früh bildet und nicht erst nach umfangreicher Feinabstimmung auf Anweisungen entsteht. Der mit dem Preprint veröffentlichte Code macht die kontrollierten Eingriffe nachvollziehbar.

Der enge Versuchsaufbau ist zugleich die Hauptgrenze. Listen einfacher Fakten isolieren die Reihenfolge sauber. Echte Prompts enthalten dagegen Überschriften, wiederholte Verweise, Werkzeuge und widersprüchliche Aussagen. Das Paper zeigt, dass die Erwähnungsreihenfolge unter kontrollierten Bedingungen als Adresse dienen kann. Es zeigt nicht, dass diese Reihenfolge den Abruf in gewöhnlichen Agententranskripten dominiert.

Zhou reichte den Preprint am 1. Oktober 2026 ein. Die nächsten Belege werden aus Reproduktionen des Eingriffs mit weniger regelmäßigen Dokumenten und Tests kommen, ob eine veränderte Dokumentstruktur dieselben internen Richtungen verändert.

## Überprüfung {#verification}

| Behauptung | Einstufung | Primärquelle | Unabhängige Überprüfung |
| --- | --- | --- | --- |
| Fragezustände sind in Qwen, Gemma und Llama nach Faktenreihenfolge organisiert | LAUT UNTERNEHMEN | [Zhou-Preprint](https://arxiv.org/abs/2610.00910) | keine; Preprint-Ergebnis |
| Das Hinzufügen eines ordinalen Vektors kann eine Frage zu einem anderen Fakt umleiten | LAUT UNTERNEHMEN | [Zhou-Preprint](https://arxiv.org/abs/2610.00910) | keine; Experiment des Autors |
| Der Transfer über 64 Wortsätze erreichte 84,1 % bei Qwen, 53,9 % bei Gemma und 36,2 % bei Llama | LAUT UNTERNEHMEN | [Zhou-Preprint](https://arxiv.org/abs/2610.00910) | keine |
| Faktenadressen belegen einen Unterraum niedrigen Rangs und bevorzugen den ersten Fakt | LAUT UNTERNEHMEN | [Zhou-Preprint](https://arxiv.org/abs/2610.00910) | keine |
| Das Muster erscheint bei 1,5 Milliarden bis 32 Milliarden Parametern und bildet sich früh im Vortraining | LAUT UNTERNEHMEN | [Zhou-Preprint](https://arxiv.org/abs/2610.00910) | keine |
| Code zur Reproduktion ist öffentlich | VERIFIZIERT | [Order-of-mention-Repository](https://github.com/MasterZhou1/order-of-mention) | Repository verfügbar |
