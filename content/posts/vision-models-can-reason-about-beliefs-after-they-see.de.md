+++
title = "Bildmodelle verstehen Überzeugungen, wenn sie klar sehen"
slug = "bildmodelle-verstehen-ueberzeugungen-wenn-sie-klar-sehen"
description = "Sieben Bild-Sprach-Modelle verloren mehr als 20 Punkte, als Aufgaben zu falschen Überzeugungen von Text auf Bilder umgestellt wurden. Eine kontrollierte Studie zeigte, dass die Wahrnehmung statt des letzten Schlussfolgerungsschritts den größten Teil der Lücke verursachte."
tags = ["research", "models"]
date = 2026-11-10T04:04:14+01:00
draft = false
+++

Ein Kind sieht eine kurze Szene auf einem Bildschirm. Ein roter Ball liegt in einer Schublade. Eine Figur geht weg, eine andere legt den Ball in eine Kiste. Als die erste Figur zurückkommt, weiß das Kind, dass sie in der Schublade suchen wird. Nun ersetzt ein Bild-Sprach-Modell das Kind. Das Modell kann eine falsche Überzeugung anhand von Text erklären, doch das bewegte Objekt auf dem Bildschirm verändert seine Antwort. Diese Szene dient der Veranschaulichung: Sie beschreibt die Art von Aufgabe, die eine neue Studie isoliert.

## Die visuelle Lücke

Mohamed Rayan Barhdadi, Syed Talal Wasim, Juergen Gall und ihre Kollegen testeten sieben Bild-Sprach-Modelle an Aufgaben zu falschen Überzeugungen. Ihr Preprint, der für den Bereich Evaluations and Datasets der NeurIPS 2026 angenommen wurde, berichtet von mehr als 159.000 API-Aufrufen in einem Protokoll mit fünf Bedingungen. Modelle, die bei Textversionen nahezu menschliches Leistungsniveau erreichten, verloren mehr als 20 Prozentpunkte, wenn dasselbe zugrunde liegende Problem visuell dargestellt wurde.

Tests zu falschen Überzeugungen haben in der Psychologie eine lange Geschichte. Sie prüfen, ob eine Versuchsperson die Realität vom Wissen einer anderen Person über diese Realität trennen kann. Im Standardschema wird ein Gegenstand bewegt, während eine Figur abwesend ist. Für die richtige Antwort muss die Versuchsperson vorhersagen, was die Figur glaubt, obwohl sie selbst weiß, wo sich der Gegenstand tatsächlich befindet.

Neuere Sprachmodelle schneiden bei Textversionen häufig gut ab. Michal Kosinski evaluierte elf Sprachmodelle an vierzig eigens entworfenen Aufgaben zu falschen Überzeugungen und berichtete, eine GPT-4-Version von 2023 habe 75 % davon gelöst. Ein separater Vergleich von James Strachan und Kollegen ergab, dass manche Sprachmodelle bei mehreren Theory-of-Mind-Tests menschliche Leistungen erreichten oder übertrafen. Beide Arbeiten warnten zugleich, eine richtige Antwort belege nicht, dass ein Modell auf dieselbe Weise wie ein Mensch über mentale Zustände nachdenke. Auswendig gelernte Muster, die Aufgabenstruktur und sprachliche Hinweise bleiben alternative Erklärungen.

Die visuelle Umgebung fügt eine weitere Abhängigkeit hinzu. Bevor ein Modell darüber nachdenken kann, was eine Figur glaubt, muss es die Figuren, Gegenstände, Orte und Veränderungen erkennen, die diese Überzeugung bestimmen. Eine falsche Antwort kann deshalb aus dem sozialen Schlussfolgern, der Wahrnehmung oder deren Verbindung entstehen. Ein einzelner Wert kann diese Fehler nicht auseinanderhalten.

## Fünf Ansichten desselben Problems

Barhdadi und Kollegen entwickelten fünf Bedingungen, die das Ziel des Schlussfolgerns beibehalten und zugleich Qualität und Form der Wahrnehmungsgrundlage verändern. Beim entscheidenden Eingriff erhielten die Modelle korrekte Beschreibungen der Szene. Mit dieser Unterstützung verschwand ein großer Teil der Lücke zwischen Text und Bild. Dieselbe Korrektur trat nicht ein, wenn automatische Parser die Beschreibungen erzeugten, selbst wenn darunter führende Bild-Sprach-Modelle waren.

Dieser Gegensatz lokalisiert den unmittelbaren Engpass. Die Modelle konnten eine genaue symbolische Darstellung der Szene häufig nutzen, um auf die Überzeugung der abwesenden Figur zu schließen. Sie scheiterten, wenn sie diese Darstellung selbst aus Pixeln erzeugen mussten. Bessere Prompts bei der abschließenden Frage würden Informationen nicht zurückholen, die die visuelle Vorverarbeitung bereits übersehen oder verzerrt hatte.

Das Fehlermuster stützt dieselbe Schlussfolgerung. Sechzig Prozent der Fehler bei falschen Überzeugungen zeigten eine Bevorzugung der Realität: Das Modell nannte den tatsächlichen Ort des Gegenstands statt des Orts, an den sich die abwesende Figur erinnern würde. Das ähnelt einem Unvermögen, zwei Repräsentationen getrennt zu halten. Die eine beschreibt die aktuelle Szene, die andere die Szene, die die Figur zuletzt gesehen hat.

Diese Bevorzugung der Realität kann wie ein Fehler im sozialen Schlussfolgern wirken, weil die abschließende Antwort die Perspektive der Figur ignoriert. Die kontrollierten Bedingungen zeigen, dass das Modell möglicherweise nie eine brauchbare Darstellung dieser Perspektive aufgebaut hat. Wenn ein Parser angibt, eine Figur habe die Verlagerung gesehen, oder den Moment ihres Weggehens übersieht, erhält der spätere Schlussfolgerungsschritt das falsche Problem.

Die Unterstützung der Autoren durch korrekte Szenenbeschreibungen dient der Diagnose und ist keine unmittelbar einsetzbare Lösung. Reale Systeme erhalten selten perfekte Szenenbeschreibungen. Ein Assistent, der einen Arbeitsplatz beobachtet, ein Roboter, der in der Nähe von Menschen handelt, oder ein Lernsystem, das einer Vorführung folgt, muss entscheiden, welche Ereignisse jede Person gesehen hat. Diese Systeme können nicht voraussetzen, dass ein Mensch das Video bereits in genau die relevanten Fakten übersetzt hat.

## Ein Benchmark für die Grenze

Frühere visuelle Theory-of-Mind-Benchmarks zeigten bereits, dass multimodale Systeme mit Absichten, Überzeugungen und irreführenden Darstellungen Schwierigkeiten haben. Das neue Protokoll trennt Sehen und Schlussfolgern schärfer. Es fragt, ob das Modell das Schlussfolgerungsproblem lösen kann, wenn die Wahrnehmung konstant gehalten wird, und misst dann, was sich mit veränderter Wahrnehmungsunterstützung ergibt.

Diese Trennung ist für die Entwicklung wichtig. Ein Team, das einen Fehler bei falschen Überzeugungen beobachtet, könnte längere Schlussfolgerungsketten oder ein größeres Sprachmodell ergänzen. Die Studie legt einen anderen ersten Test nahe: dem System eine überprüfte Szenenrepräsentation geben. Wird die Antwort richtig, sollte sich die Arbeit auf Objektverfolgung, Ereignisanalyse und perspektivenspezifisches Gedächtnis richten. Bleibt der Fehler bestehen, braucht die Komponente für das Schlussfolgern über Überzeugungen Aufmerksamkeit.

Das Ergebnis begrenzt auch weitreichende Aussagen über die soziale Intelligenz von Maschinen. Textbenchmarks können belegen, dass ein Modell ein geschriebenes Szenario einer erwarteten Antwort zuordnet. Sie belegen nicht, dass das System das relevante Szenario aus einer sich verändernden physischen Welt erschließen kann. Ein Modell, das nach dem Lesen eines klaren Absatzes über die Überzeugung einer anderen Person spricht, hat erst die zweite Hälfte der Aufgabe erledigt.

Die Arbeit stellt Code und Daten bereit, sodass sich ihre Bedingungen erweitern lassen. Der berichtete Vergleich von sieben Modellen bleibt ein begrenzter Labortest. Er misst weder jedes visuelle Modell noch jede Form sozialer Schlussfolgerung oder die Leistung in unkontrollierten Videos. Der Preprint wurde nicht im Rahmen einer Fachzeitschrift begutachtet, auch wenn die Annahme für den Konferenzbereich einen formellen Rahmen bietet.

Zurück zum beispielhaften Kind und dem bewegten Ball. Ein Entwickler gibt dem Modell eine zusätzliche Zeile: Die erste Figur ging weg, bevor der Ball bewegt wurde. Das Modell sagt nun die Schublade voraus. Sein Schlussfolgern wirkt besser, obwohl sich der Mechanismus dafür möglicherweise überhaupt nicht verändert hat. Das fehlende Stück war das Ereignis, das das Modell nicht gesehen hatte.

## Quellen

- Barhdadi, M. R., Wasim, S. T., Gall, J., Serpedin, E., & Kurban, H. (2026). *Perception, Not Reasoning, Limits Visual Theory of Mind*. https://arxiv.org/abs/2611.10694
- Kosinski, M. (2024). *Evaluating large language models in theory of mind tasks*. https://doi.org/10.1073/pnas.2405460121
- Strachan, J. W. A., Albergo, D., Borghini, G., Pansardi, O., Scaliti, E., Gupta, S., Saxena, K., Rufo, A., Panzeri, S., Manzi, G., Graziano, M. S. A., & Becchio, C. (2024). *Testing theory of mind in large language models and humans*. https://doi.org/10.1038/s41562-024-01882-z
