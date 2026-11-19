+++
title = "Lange Gesprächsverläufe machten Modelle beständig falsch"
slug = "lange-gespraechsverlaeufe-machten-modelle-bestaendig-falsch"
description = "Eine Studie mit 100 Gesprächsrunden zeigte, dass der vollständige Chatverlauf die Genauigkeit bei der Zustandsverfolgung von rund 60 auf 10 % senkte. Überprüfte Zusammenfassungen bewahrten die Antworten, während übliche Kontrollverfahren das versagende System oft stabil erscheinen ließen."
tags = ["research", "models"]
date = 2026-11-18T04:00:29+01:00
draft = false
+++

Marta prüft vor der Frühschicht den Assistenten für die Lagerverwaltung. Die Anzeige steht auf Grün. Seine Antworten stimmen miteinander überein, seine Sprache ist ruhig, und die Gesamtbestände haben sich über die letzten fünf Fragen hinweg kaum verändert. Dann vergleicht sie eine Zahl mit dem Bestandsbuch. Der Assistent hat denselben Fehler durch jede Antwort mitgeschleppt.

*Die Szenen am Anfang und am Ende dieses Artikels sind Illustrationen; die Personen darin sind erfunden.*

Ein Preprint von Ali Şenol von der Universität Tarsus untersucht dieses stille Versagen. In Gesprächen mit 100 Runden über veränderliche Budgets, Lagerbestände, Laborbehälter und Projektmeilensteine sank die Modellgenauigkeit innerhalb von zwanzig Runden von etwa 60 auf etwa 10 %, wenn das vollständige Transkript im Kontext blieb. Eine durch einen Solver überprüfte Zustandszusammenfassung hielt die Genauigkeit um mehr als 50 Prozentpunkte höher. Die üblichen Anzeichen geordneten Schlussfolgerns lieferten keine verlässliche Warnung.

## Das Transkript wird Teil des Problems

Lange Gespräche verlangen von einem Modell zwei Aufgaben zugleich. Es muss das aktuelle Problem lösen und entscheiden, was es von allem behalten soll, was es selbst und der Nutzer zuvor gesagt haben. Die zweite Aufgabe wird schwieriger, wenn sich der Zustand ändert, eine frühere Angabe korrigiert wird oder das Modell bereits einen Fehler gemacht hat.

Frühere Arbeiten hatten einen Teil dieses Problems isoliert. In *LLMs Get Lost in Multi-Turn Conversation* zerlegten Philippe Laban und seine Mitautoren vollständige Aufgaben in Teile, die über mehrere Gesprächsrunden eintrafen. Die Modelle legten sich häufig zu früh auf eine Antwort fest. Ihre Leistung sank, obwohl sich das zugrunde liegende Problem nicht verändert hatte. Die Studie nutzte Aufgaben, die aus GSM8K abgeleitet waren, dem von Karl Cobbe und Kollegen 2021 vorgestellten Datensatz mit 8.500 Mathematikaufgaben auf Grundschulniveau.

Şenol stellte zunächst eine engere kausale Frage: Verschlechtert das Beibehalten der eigenen Modellantworten das Endergebnis? Er wählte 48 aufgeteilte Mathematikaufgaben mit vier bis neun Gesprächsrunden aus. GPT-4o-mini, Llama 4 Scout und Mistral 7B erhielten jeweils zwei Varianten. Eine behielt den Dialog bei. Die andere baute aus den vom Nutzer gelieferten Informationen einen neuen Prompt auf und ließ frühere Antworten des Assistenten weg.

Alle 11.382 Modellaufrufe wurden abgeschlossen. GPT-4o-mini löste mit seinen eigenen Antworten im Kontext 33 von 48 Aufgaben und mit einem neu aufgebauten Präfix 43, ein Rückgang um 21 Prozentpunkte. Mistral 7B fiel von 17 richtig gelösten Aufgaben auf drei, also um 29 Punkte. Llama 4 Scout bewegte sich in dieselbe Richtung, doch der Unterschied von zehn Punkten erreichte nicht die statistische Schwelle der Studie.

Mistrals Fehler zeigte sich deutlich. Wenn die früheren Antworten vorhanden waren, erklärte das Modell selbst in der letzten Runde häufig noch, es brauche weitere Informationen. Der neue Prompt enthielt dieselben Fakten und führte zu einer Antwort.

## Hundert Runden mit einem exakten Bestandsbuch

Das erste Experiment endete nach höchstens neun Runden. Es konnte außerdem nicht unterscheiden, ob eine spätere Frage schwieriger war oder ob das längere Gespräch die Leistung beeinträchtigte. Deshalb entwickelte Şenol CDR-Stream, einen Benchmark, in dem jede Runde einen Zustand aktualisiert und eine Frage mit exakter Antwort stellt.

Der Benchmark umfasst vier Arten von Zuständen: ein Budgetbuch, einen Lagerbestand, ein Laborprotokoll und eine Folge von Projektmeilensteinen. Eine Nutzernachricht kann eine Lieferung hinzufügen, einen früheren Eintrag korrigieren oder eine Menge zwischen Orten verschieben. Sie kann ablenkende Sätze enthalten. Gefragt wird nach einer Summe, einer Differenz, der Anzahl oberhalb eines Schwellenwerts, einem Maximum, einem hypothetischen Ergebnis oder einem Anteil.

Ein exakter Solver erzeugt die richtige Antwort für jede Runde. Eine Skala mit zwölf Stufen verändert jeweils eine Quelle der Schwierigkeit, etwa die Zahl der Ereignisse oder die Komplexität einer Aktualisierung. Die Studie kalibrierte diese Skala für jedes Modell getrennt und schrieb die Einstellungen anschließend fest. Dadurch eignet sich das Experiment dazu, den Leistungsabfall innerhalb eines Modells zu messen. Seine Rohwerte sollten jedoch nicht verwendet werden, um die Modelle untereinander zu vergleichen.

GPT-4o-mini, Llama 3 70B und Gemma 3 12B erhielten jeweils dreißig Dialoge mit 100 Runden. In einem Versuchsarm enthielt der Prompt das gesamte Gespräch. Im anderen enthielt er eine überprüfte Zusammenfassung des aktuellen Zustands und die neue Nutzernachricht. Beide Arme verwendeten dieselben Anweisungen und dasselbe Antwortformat.

Die Kurven mit vollständigem Verlauf überlappten fast. Die Genauigkeit begann in den ersten fünf Runden bei etwa 0,6, sank in den Runden sechs bis zwanzig auf ungefähr 0,3 und pendelte sich für die übrigen achtzig Runden zwischen 0,08 und 0,11 ein. Selbst wenn die Fragen auf der einfachsten Stufe blieben, lag die Genauigkeit mit vollständigem Verlauf nach Runde zwanzig nur zwischen 0,10 und 0,14.

Die überprüfte Zusammenfassung veränderte das Ergebnis. Bei denselben einfachen Gesprächen hielt sie die Genauigkeit zwischen 0,82 und 0,86. Über alle fünf Schwierigkeitsverläufe hinweg betrug der durchschnittliche Vorteil 0,521 bei GPT-4o-mini, 0,545 bei Llama 3 und 0,588 bei Gemma 3. Wenn eine Folge von schwierigen zu einfachen Fragen zurückkehrte, erholte sich die Leistung mit Zusammenfassung. Mit vollständigem Verlauf tat sie das nicht.

## Eine stabile Antwort kann ein stabiler Fehler sein

Einem Betreiber steht der exakte Solver des Experiments nicht zur Verfügung. Ein eingesetztes System braucht ein Signal, das anzeigt, wann seine aktuelle Antwort die Realität nicht mehr abbildet. Die Studie prüfte mehrere Kandidaten: Konsistenz zwischen wiederholt erzeugten Antworten, logische Kohärenz, semantische Ähnlichkeit, ein paarweise erhobenes Maß der Antwortbereitschaft sowie Standardverfahren zum Erkennen von Veränderungen in einem Datenstrom.

Keines lieferte modellübergreifend eine robuste Warnung. Im kürzeren Mathematikexperiment hatten die gemessenen Qualitätssignale keinen statistisch nachweisbaren Zusammenhang mit dem abschließenden Scheitern, nachdem die Analyse Gesprächsrunde, offengelegte Informationen und Kontextlänge berücksichtigt hatte. Ein Signal erfasste nur 29 Ausgangsaufgaben. Die Arbeit behauptet deshalb nicht, jeden kleinen Zusammenhang ausgeschlossen zu haben.

Die Studie mit hundert Runden zeigte ein beunruhigenderes Muster. Konsistenz und Kohärenz veränderten sich weit weniger als die Genauigkeit. Die Stabilität stieg, weil die Modelle ähnliche falsche Antworten wiederholten. Ein Kontrollverfahren, das Übereinstimmung belohnt, könnte daher sicherer werden, während die zugrunde liegende Zustandsschätzung schlechter wird.

Şenol grenzt die Reichweite dieser Schlussfolgerung sorgfältig ein. Beide Studien verwenden Arithmetik und exakte Zustandsverfolgung. Das macht Korrektheit beobachtbar, bildet aber nicht jedes offene Gespräch ab. Die Modellgruppen unterscheiden sich zwischen den Experimenten und umfassen nicht die derzeit leistungsfähigsten Spitzenmodelle. Gemma 4 31B war für die geplante Schwierigkeitsskala zu genau. Ein aussagekräftiger Test würde daher schwierigere Aufgaben erfordern und nicht mehr Wiederholungen derselben Aufgaben.

Dem langen Experiment fehlt außerdem eine Vergleichsbedingung, die nur Nutzernachrichten enthält. Es misst somit das Versagen bei vollständigem Verlauf, kann aber keinen genauen Anteil früheren Assistentenantworten, der Kontextlänge oder der wachsenden Last der Zustandsverfolgung zuordnen. Die auf Wiederholungen beruhende Überwachung war nur für GPT-4o-mini vollständig. Mehrere Analysen der Kontrollverfahren waren explorativ und gehörten nicht zu den vorab festgelegten bestätigenden Tests.

## Der Zustand gehört außerhalb des Transkripts

Der Eingriff in der Arbeit ist bescheiden. Er gibt dem Modell kein besseres Gedächtnis. Stattdessen entfällt die Notwendigkeit, die Gegenwart aus dem gesamten Gespräch zu rekonstruieren: Das Modell erhält einen kompakten Zustand, den ein externes Programm geprüft hat.

Diese Architektur trennt Belege von Erzählung. Das Transkript kann für eine spätere Prüfung verfügbar bleiben, während der aktive Prompt das aktuelle Budgetbuch, den Lagerbestand oder den Aufgabenstatus erhält. Şenol schlägt außerdem Prüfungen über getrennte Sitzungen hinweg sowie erneute Abfragen unter veränderten Annahmen vor. Ein Detektor innerhalb eines sich verschlechternden Gesprächsverlaufs erhält möglicherweise nie eine unverfälschte Vergleichsbasis.

Die Arbeit lässt ein schwieriges technisches Problem offen. Ihre Zusammenfassungen kamen von einem exakten Solver. Die meisten realen Systeme haben keinen solchen Solver, und ein Modell, das seine eigene Zustandsdatei schreibt, kann einen Fehler ebenso effizient bewahren wie einen Fakt. Offen bleibt, wie ein System diesen externen Zustand pflegen und überprüfen kann, ohne die Zusammenfassung unbemerkt in eine weitere nicht vertrauenswürdige Antwort zu verwandeln.

Marta öffnet die Zustandsdatei neben dem Chat. Eine Lagerumbuchung steht dort genau einmal, mit dem ursprünglichen Ereignis und seiner Korrektur. Das Transkript enthält weiterhin die fünf übereinstimmenden Antworten des Assistenten. Sie lässt sie im Archiv und schickt das geprüfte Bestandsbuch zusammen mit der nächsten Frage ab.

## Quellen

- Cobbe, K., et al. (2021). *Training Verifiers to Solve Math Word Problems*. https://arxiv.org/abs/2110.14168
- Laban, P., Hayashi, H., Zhou, Y., & Neville, J. (2026). *LLMs Get Lost in Multi-Turn Conversation*. https://arxiv.org/abs/2505.06120
- Şenol, A. (2026). *The Silent Cost of Conversation History in LLM Reasoning*. https://arxiv.org/abs/2611.20071
