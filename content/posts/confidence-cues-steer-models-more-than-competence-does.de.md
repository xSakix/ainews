+++
title = "Zuversichtssignale steuern Modelle stärker als Kompetenz"
slug = "zuversichtssignale-steuern-modelle-staerker-als-kompetenz"
description = "Eine kontrollierte Studie findet, dass ein Satz voller Zuversicht oder Zweifel stark verändern kann, ob ein Reasoning-Modell ein Werkzeug aufruft. Die Änderungen treffen aber selten die Probleme, bei denen Hilfe nötig ist."
tags = ["research", "agents"]
date = 2026-10-05T04:00:30+02:00
draft = false
+++

Der Satz „Ich bin mir meiner Antwort sicher“ macht ein Reasoning-Modell weniger geneigt, ein Werkzeug um Hilfe zu bitten. Der Satz „Ich bin mir meiner Antwort unsicher“ beim selben Modell an derselben Stelle derselben Reasoning-Spur lässt es häufiger delegieren. Bemerkenswert ist, wie wenig diese sprachlich ausgelöste Verhaltensänderung damit zusammenhängt, ob das Modell das Problem ohne Hilfe lösen kann.

Rohit Saxena und Utkarsh Upadhyay nennen diese Eigenschaft „nudgeability“. Ihr Preprint testet, ob Zuversicht ausdrückende Sprache die Entscheidung eines Modells steuern kann, direkt zu antworten oder ein Werkzeug aufzurufen. Getrennt davon prüft er, ob diese Steuerung die Probleme trifft, bei denen das Werkzeug tatsächlich nützlich ist.

Diese Trennung ist für Agenten wichtig. Ein System kann stark auf ein Unsicherheitssignal reagieren und dennoch Zeit und Geld für Werkzeugaufrufe bei einfachen Fragen verschwenden, während es schwierige Fragen zuversichtlich selbst behält. Mehr Delegation ist nicht unbedingt bessere Delegation.

## Ein Satz, zwei kontrafaktische Durchläufe

Das Experiment beginnt mit identischem Problem, Prompt und vom Modell erzeugtem Reasoning-Präfix. An einer festen Grenze fügen die Forscher einen von zwei Ich-Sätzen ein, die Zuversicht oder Zweifel ausdrücken. Das Modell kann dann weiter schlussfolgern, bevor es entscheidet, ob es antwortet oder delegiert. Weil alles vor dem eingefügten Satz konstant bleibt, isoliert der paarweise Unterschied dessen Wirkung.

Die Studie umfasst neun Reasoning-Modelle mit offenen Gewichten aus den Familien Qwen, Gemma und GLM auf MuSiQue und StrategyQA sowie größere, von Anbietern bereitgestellte DeepSeek- und MiniMax-Modelle. Die Hauptdurchläufe nutzen gieriges Decodieren, ergänzt um Experimente mit stichprobenbasiertem Decodieren und Kontrollen.

Über die Experimente mit offenen Gewichten hinweg verändert der Wechsel von Zuversicht zu Zweifel die Delegation im Median um 20,6 Prozentpunkte. Die größeren gehosteten Modelle bewegen sich um 53 bis 70 Punkte. Eine Kontrolle mit Abschneiden und Neugenerieren ohne einen der beiden Sätze bleibt im Median fast wirkungslos. Den Reasoning-Block unmittelbar nach dem Satz zu schließen erhält die Richtung des Effekts.

Diese Ergebnisse zeigen eine starke kausale Steuerungsmöglichkeit. Sie zeigen nicht, dass die Modelle ihre eigene Unsicherheit entdeckt haben.

## Empfindlichkeit ist keine Selbsterkenntnis

Um zu testen, ob die Verhaltenswechsel nützlich sind, vergleichen die Autoren sie mit der Kompetenz jedes Modells ohne Hilfe. Ein guter Wechsel schickt ein Problem, das das Modell falsch lösen würde, an das Werkzeug oder lässt ein lösbares Problem beim Modell. Nur im Median 42 % der ausgelösten Wechsel sind gut gezielt. Das sind zwei Punkte mehr als bei zufälliger Auswahl derselben Zahl von Problemen.

Einfach gesagt ähnelt das eingefügte Zuversichtssignal eher einer Anweisung als einem Ablesen von Selbsterkenntnis. Es verschiebt die Schwelle zur Werkzeugnutzung stark. Diese unterscheidet aber nur schwach zwischen „Ich brauche Hilfe“ und „Ich kann das bewältigen“. Das Experiment liefert den Zuversichtssatz absichtlich von außen. Es testet nicht, ob ein Modell selbst ein gut kalibriertes Signal erzeugen kann.

## Was Agentenentwickler messen sollten

Die praktische Lehre lautet, für jede reflexive Werkzeugstrategie zwei Zahlen zu berichten: wie stark sie das Verhalten verändert und wie gut die Änderungen den tatsächlichen Bedarf treffen. Ein Routing-Eingriff, der nur die Werkzeugaufrufrate erhöht, kann erfolgreich erscheinen und lediglich Latenz hinzufügen. Einer, der Aufrufe unterdrückt, kann effizient wirken und zugleich selbstsichere Fehler bewahren.

Die Autoren warnen außerdem vor der engen Reichweite ihrer Aufgaben und ihres Eingriffs. Das Paper belegt nicht, wie ein Produktionsagent mit vielen Werkzeugen, wechselnden Kosten oder adversarialen Anweisungen handelt. Sein Code ist zur Veröffentlichung versprochen und noch nicht mit dem Preprint verfügbar. Der Beitrag ist eine klare Diagnose: Bevor die erklärte Zuversicht eines Modells den Zugang zu stärkeren Werkzeugen steuert, muss geprüft werden, ob sie Kompetenz vorhersagt statt lediglich Verhalten anzuweisen.

## Überprüfung {#verification}

| Behauptung | Einstufung | Primärquelle | Unabhängige Überprüfung |
| --- | --- | --- | --- |
| Der Aufbau fügt Zuversicht oder Zweifel an derselben Grenze eines identischen Reasoning-Präfixes ein | VERIFIZIERT | [Preprint](https://arxiv.org/abs/2609.34572) | keine |
| Neun Reasoning-Modelle mit offenen Gewichten aus Qwen, Gemma und GLM sowie gehostete DeepSeek- und MiniMax-Modelle | VERIFIZIERT | [Preprint](https://arxiv.org/abs/2609.34572) | keine |
| Mediane Delegationsänderung um 20,6 Punkte bei offenen und 53–70 Punkte bei gehosteten Modellen | LAUT UNTERNEHMEN | [Preprint](https://arxiv.org/abs/2609.34572) | keine; Experimente der Autoren |
| Im Median 42 % gut gezielte Wechsel, zwei Punkte über einer gleich großen Zufallsauswahl | LAUT UNTERNEHMEN | [Preprint](https://arxiv.org/abs/2609.34572) | keine; Experimente der Autoren |
| Zuversichtssprache wirkt eher wie eine Steuereingabe als wie ein Beleg für Selbsterkenntnis des Modells | ANALYSE | [Preprint](https://arxiv.org/abs/2609.34572) | Interpretation im Einklang mit dem Zielgenauigkeitsergebnis der Autoren |
| Code ist noch nicht verfügbar | VERIFIZIERT | [Preprint](https://arxiv.org/abs/2609.34572) | Reproduzierbarkeitsangabe plant Freigabe bei Veröffentlichung |
