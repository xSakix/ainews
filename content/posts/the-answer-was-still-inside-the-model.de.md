+++
title = "Die Antwort war noch im Modell"
slug = "antwort-war-noch-im-modell"
description = "Eine Studie mit 15 Sprachmodellen findet, dass viele Arbeitsgedächtnisfehler nach der Auswahl des richtigen Elements auftreten. Die Modelle behalten dekodierbare Information, geben sie aber nicht aus."
tags = ["research", "models"]
date = 2026-10-16T04:07:00+02:00
draft = false
+++

Ein Modell sieht eine kurze Symbolliste und wird dann durch eine zweite Liste abgelenkt, bevor es das ursprüngliche Ziel nennen muss. Es antwortet mit dem Ablenker. Die naheliegende Diagnose lautet, das erste Symbol sei verschwunden. In dieser illustrativen Szene kann eine interne Sonde das Ziel jedoch weiterhin fast perfekt auslesen. Die Antwort wurde nicht gelöscht. Zwischen dem Behalten und dem Aussprechen ging etwas schief.

Diese Unterscheidung treibt einen neuen Preprint zum Arbeitsgedächtnis von Sprachmodellen an. Seine Autoren testeten 15 Modelle mit 70 Millionen bis 14 Milliarden Parametern auf Aufgaben, die Interferenz erzeugen sollten. Sie fanden, dass Aufmerksamkeitsköpfe häufig das richtige Ziel auswählten, selbst wenn die endgültige Antwort falsch war. Einfache Sonden konnten das Ziel bei vielen Fehlern mit fast perfekter Genauigkeit aus verborgenen Zuständen dekodieren.

Das Ergebnis hinterfragt eine vertraute Abkürzung bei der Modellevaluierung: falsche Ausgabe als Beleg dafür zu behandeln, dass die zugrunde liegende Information fehlt. Die Arbeit trennt stattdessen drei Abläufe, die eine einzelne Genauigkeitszahl zusammenfasst: ein relevantes Element auswählen, seine Identität bewahren und es als Antwort auslesen.

## Ein kontrolliertes Gedächtnisproblem

Arbeitsgedächtnis ist kein Langzeitspeicher. Es ist die vorübergehende Fähigkeit, Information in nutzbarem Zustand zu halten, während anderes Material um Aufmerksamkeit konkurriert. Experimente mit Menschen zeigen häufig, dass das Element teilweise verfügbar bleibt, selbst wenn ein Teilnehmer das falsche nennt. Ähnliche Interferenz kann zwei Erinnerungen schwer unterscheidbar machen, ohne eine davon zu zerstören.

Die Forschenden konstruierten Aufgaben, in denen sie Ziel, konkurrierende Elemente und deren Positionen variieren konnten. Dann betrachteten sie das Modellinnere an den Punkten, an denen das Ziel ausgewählt und weitergetragen werden sollte. Die Modelle umfassten mehrere Größen und Familien. Das ist wichtig, weil ein Muster in einem einzelnen Checkpoint ein architektonischer Zufall statt eines allgemeinen Mechanismus sein kann.

Bei korrekten Versuchen galt die erwartete Geschichte: Aufmerksamkeit konzentrierte sich auf das Ziel, und die letzten Schichten erzeugten das richtige Token. Bei vielen falschen Versuchen galt die erste Hälfte weiterhin. Zielauswählende Köpfe beachteten die richtige Position. Sonden verborgener Zustände behielten genug Information, um das Ziel zu identifizieren. Dennoch spiegelte die Ausgabe einen Konkurrenten wider.

Eine Sonde belegt Dekodierbarkeit, nicht Nutzung. Ein nachträglich trainierter Klassifikator kann Information extrahieren, auf die die eigene Berechnung des Modells nicht zugreifen kann. Die Autoren gingen daher über das Lesen von Zuständen hinaus und griffen in sie ein.

## Die Konkurrenten abschwächen

Der zentrale kausale Test unterdrückte Repräsentationen der Identität von Nichtzielelementen. Der Eingriff verbesserte die als d-prime gemessene Empfindlichkeit in der von einer Interferenzerklärung vorhergesagten Richtung. Schwächere Konkurrenten machten es dem Modell leichter, das gespeicherte Ziel zu berichten.

Das bedeutet nicht, dass jeder Gedächtnisfehler ein Auslesefehler ist. Modelle können ein Element nicht kodieren, es verlieren oder die falsche Position wählen. Die Aussage der Arbeit ist enger: Ein bedeutender Anteil der Fehler tritt auf, während Zielinformation intern verfügbar bleibt, und Verwechslung ähnlicher Repräsentationen kann die endgültige Antwort blockieren.

Die Unterscheidung ist technisch wichtig. Mehr Kontext oder Wiederholung des Ziels greift ein Speicherproblem an. Das kann wenig helfen, wenn das Modell das Ziel bereits hält, es aber nicht von konkurrierendem Inhalt trennen kann. Ein System mit dem zweiten Problem braucht möglicherweise andere Prompts, Zwischenstruktur oder Architekturänderungen, die Identität beim Auslesen schärfen.

Sie ist auch für die Interpretation wichtig. Transformer-Aufmerksamkeit, eingeführt als Mechanismus zum Verknüpfen von Sequenzpositionen, wird oft so untersucht, als entscheide Aufmerksamkeit auf das richtige Token darüber, was das Modell weiß. Hier kann Aufmerksamkeit auf das Ziel zeigen und trotzdem keine korrekte Ausgabe liefern. Umgekehrt bedeutet eine falsche Antwort nicht, dass die Aufmerksamkeit das Ziel verfehlte.

## Menschliche Ähnlichkeit mit Grenzen

Die Autoren beschreiben das Interferenzmuster als menschenähnlich, doch der Vergleich ist funktional statt biologisch. Ein Transformer braucht kein menschliches Gedächtnissystem, um dieselbe Verhaltenstrennung zwischen Verfügbarkeit und Bericht zu zeigen. Ähnliche Fehler können aus sehr unterschiedlicher Mechanik entstehen.

Auch Größe löst das Problem nicht auf. Tests von Modellen mit bis zu 14 Milliarden Parametern zeigen, dass der Effekt jenseits winziger experimenteller Netze besteht. Sie etablieren aber nicht dasselbe Ergebnis bei Spitzenmodellen mit viel mehr Parametern oder proprietärem Nachtraining. Die Aufgaben sind bewusst kontrolliert. Reale Gespräche mischen Abruf, Instruktionsbefolgung, Planung und Generierung so, dass die Ursache eines Fehlers schwerer zu isolieren ist.

Kontrollierte Aufgaben sind jedoch gerade der Zweck. Sie lassen Forschende einen Konkurrenten ändern, eine Repräsentation beobachten und einen Eingriff testen. Die Arbeit bietet eine Methode für eine bessere Frage nach einem Modellfehler: Wurde die Information nie kodiert, ging sie verloren, oder war sie vorhanden, aber dem Ausgabeprozess unzugänglich?

Zurück zur illustrativen Symbolaufgabe. Das Modell nennt das falsche Element, und ein Prüfer markiert einen Fehler. Dieses Urteil ist an der Produktgrenze korrekt. Intern könnte das System jedoch den Großteil der Arbeit erledigt haben. Der nächste Fortschritt kommt vielleicht nicht von mehr Gedächtnis, sondern davon, ihm das Lesen dessen beizubringen, was es bereits behalten hat.

## Quellen

- Vaswani, A., et al. (2017). *Attention Is All You Need*. https://arxiv.org/abs/1706.03762
- *Working Memory Readout Bottlenecks in Language Models* (2026). https://arxiv.org/abs/2610.21176
