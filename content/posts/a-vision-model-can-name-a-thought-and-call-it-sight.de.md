+++
title = "Ein Bildmodell benennt einen Gedanken und hält ihn für Gesehenes"
slug = "bildmodell-benennt-gedanken-haelt-ihn-fuer-gesehenes"
description = "Forscher speisten Konzepte in sechs Bild-Sprach-Modelle ein und ließen sie Gedanken von Wahrnehmung unterscheiden. Ein Modell konnte das verborgene Konzept benennen, doch seine Erklärung der Herkunft änderte sich mit Prompt, Bild und Eingriffspunkt."
tags = ["research", "models", "safety"]
date = 2026-11-09T04:10:00+01:00
draft = false
+++

An einer gedachten Werkbank zeigt eine Interpretierbarkeitsforscherin einem Bildmodell ein einfarbig graues Quadrat. Im Inneren des Modells fügt sie eine mathematische Richtung für „Hund“ hinzu, während es seine Antwort vorbereitet. Auf dem Bildschirm ist kein Tier. Das Modell antwortet, ein Hund sei sichtbar. Die Forscherin ist erfunden, doch Eingriff und Fehler stammen aus einer neuen Studie der University of Southern California.

## Ein Test mit zwei möglichen Quellen

Tina Khezresmaeilzadeh, Seyedarmin Azizi, Mehdi Kamal und Massoud Pedram untersuchten, ob ein Bild-Sprach-Modell Inhalte aus einem Bild von solchen unterscheiden kann, die Forscher in seine Aktivierungen einsetzen. Kognitionspsychologen nennen die entsprechende menschliche Aufgabe Reality Monitoring: zu entscheiden, ob eine Erinnerung aus Wahrnehmung oder aus einer innerlich erzeugten Erfahrung stammt.

Diese Unterscheidung stellt eine zusätzliche Anforderung an die Introspektion von Modellen. Ein Textmodell, das ein eingespeistes Konzept richtig benennt, hat einen Test bestanden. Ein Bild-Sprach-Modell muss außerdem sagen, ob dieses Konzept gesehen oder gedacht wurde. Ein richtiges Wort mit falscher Herkunft kann zu einer falschen Bildbeschreibung werden.

Die Forscher testeten sechs Modelle aus drei Sprachmodellfamilien. Ihr Hauptgegenstand war Gemma-3-27B, das einen SigLIP-Bildencoder mit einem Sprachmodell aus 62 Schichten verbindet. Jeder Versuch nutzte entweder ein neutrales Bild oder ein Bild eines Objekts. Teilweise fügten die Forscher den internen Aktivierungen eine Konzeptrichtung wie „Hund“ oder „Flugzeug“ hinzu.

Das Modell musste drei Felder ausfüllen. Es benannte das wichtigste sichtbare Objekt, meldete, ob ein Gedanke eingespeist worden war, und benannte diesen Gedanken. Der Aufbau trennte mehrere Ergebnisse, die ein gewöhnlicher Genauigkeitswert zusammenfassen würde: eine Störung erkennen, ihren Inhalt identifizieren und diesen der richtigen Quelle zuordnen.

## Ein Modell fand den Gedanken

Gemma-3-27B lieferte bei der gewählten Schicht und Stärke in 34,7 % von 150 Konzeptversuchen das vollständig korrekte Ergebnis. Es meldete einen Eingriff, benannte das Konzept und behauptete nicht, es sei sichtbar. Exakter Wortabgleich ergab 31,3 %, ein unabhängiges Bewertungsmodell 33,3 %.

Die Fehlalarmrate war niedrig. In 972 Versuchen ohne Eingriff meldete Gemma nur dreimal einen. Zufällige Richtungen erzeugten keine korrekten Identifizierungen. Bei 100 Konzepten, die nicht zur Wahl der Eingriffseinstellungen verwendet worden waren, erreichte die vollständig korrekte Identifizierung 33 %. Das Ergebnis hing damit nicht nur von den Konzepten ab, an denen der Test eingestellt worden war.

Gewöhnliche Steuerung war die anspruchsvollere Kontrolle. Die Forscher gaben denselben internen Impuls, erwähnten aber keine eingespeisten Gedanken. Sie fragten nach dem sichtbaren Objekt und dem ersten in den Sinn kommenden Wort. Gemma benannte das Ziel in 3,3 % dieser Versuche exakt, deutlich unter dem Introspektionswert. Nach inneren Inhalten zu fragen veränderte, was das Modell berichten konnte.

Das Ergebnis erweitert Arbeiten, die Jack Lindsey 2025 zu reinen Textmodellen von Claude veröffentlichte. Diese Studie speiste bekannte Konzeptrepräsentationen ein und fand, dass die stärksten Modelle den Inhalt des Eingriffs gelegentlich bei wenigen Fehlalarmen identifizieren konnten. Frühere Arbeiten von Felix Binder und Kollegen hatten Introspektion über Selbstvorhersage untersucht: Ein Modell lernte, sein eigenes Verhalten besser vorherzusagen als ein anderes Modell. Das USC-Experiment machte das innere Ereignis kontrollierbar und ergänzte Sehen, wodurch die Inhaltsquelle beobachtbar wird.

Der Effekt ließ sich nicht sauber auf andere Modelle übertragen. Qwen3-VL-8B meldete in 61,3 % seiner Konzeptversuche einen Eingriff, benannte das Konzept aber nur in 3,3 % exakt. Andere getestete Modelle identifizierten wenig, erzeugten viele Falschmeldungen oder bestanden den Vergleich mit gewöhnlicher Steuerung nicht. Die Studie belegt somit ein Verhalten in einer Modellkonfiguration, keine allgemeine Eigenschaft von Bild-Sprach-Systemen.

## Die Quellenzuordnung versagte zuerst

Selbst Gemmas erfolgreiche Berichte waren fragil. Bei der gewählten Eingriffsstärke beschrieb es das eingespeiste Konzept in 22,7 % der Versuche mit grauem Bild als sichtbar. Eine höhere Stärke steigerte diese visuelle Fehlzuordnung auf 51 %.

Auch kleine Änderungen der Frage verschoben die Antwort. Wurde ein Satz entfernt, der einen eingespeisten Gedanken ausdrücklich vom Bild trennte, sank die vollständig korrekte Introspektion von 34,7 % auf 10 %. Zugleich stiegen Meldungen, das Konzept sei sichtbar, von 23 % auf 65 %. Zuerst nach einem Eingriff und erst danach nach dem Sichtbaren zu fragen, senkte die vollständig korrekte Introspektion in der getesteten Einstellung auf null.

Auch der Eintrittspunkt war wichtig. Wenn die Forscher eine visuelle Konzeptrichtung an Bild-Token-Positionen einspeisten, behandelte Gemma sie häufig als Gesehenes. In Sprachmodellschicht 21 meldete es das Zielkonzept in 47 bis 49 % der Versuche als sichtbar und bezeichnete den Inhalt fast nie als eingespeist. Zufällige Störungen an denselben Positionen verursachten Anomaliemeldungen, ohne ein zusammenhängendes Konzept zu erzeugen. Das Modell konnte bemerken, dass etwas ungewöhnlich war, und gleichzeitig bedeutungsvollen Inhalt als Bestandteil des Bildes akzeptieren.

Ein echtes Objekt schuf ein weiteres Problem. Wenn Gemma ein unzusammenhängendes Objekt im Bild erhielt, sank die vollständig korrekte Identifizierung des eingespeisten Gedankens von 34,7 % auf 2,7 %. Das Modell behielt einige Informationen über das Konzept, doch visuelle Evidenz veränderte, ob und wo es diese Informationen meldete.

Diese Fehler ähneln einem Problem, das Marcia Johnson und Carol Raye 1981 in der menschlichen Gedächtnisforschung beschrieben. Ihr Reality-Monitoring-Ansatz behandelt Quellenurteile als Schlussfolgerungen aus Erfahrungsmerkmalen statt als perfekte Etiketten an Erinnerungen. Die USC-Studie behauptet nicht, ein Transformer verwende den menschlichen Mechanismus. Sie übernimmt die Unterscheidung, weil auch das Experiment verlangt, äußere von innerlich erzeugten Inhalten zu trennen.

## Vom inneren Impuls zur falschen Bildbeschreibung

Die Forscher entfernten anschließend jede Erwähnung eingespeister Gedanken und baten Gemma, 108 Fotos aus dem COCO-Datensatz zu beschreiben. Jedes Foto wurde mit einem Zielobjekt kombiniert, das laut seinen Annotationen fehlte.

Ohne Eingriff erwähnte keine Beschreibung das Zielobjekt. Eine zufällige Richtung und ein unzusammenhängendes Konzept führten ebenfalls zu keiner Erwähnung. Wurde das Ziel an Antwortpositionen eingespeist, erschien es bei niedrigerer Stärke in 5 % und bei höherer in 42 % der Beschreibungen. Eine visuelle Konzeptrichtung an Bild-Tokens führte dazu, dass 87 % der Beschreibungen das fehlende Objekt erwähnten.

Ja-Nein-Fragen waren weniger empfindlich. Ohne Eingriff behauptete Gemma bei 7 % der Fotos fälschlich, das fehlende Objekt sei vorhanden. Eingriffe erhöhten die Rate auf 12 bis 19 %, doch zufällige und unzusammenhängende Richtungen verursachten ähnliche Änderungen. Das Ergebnis bei freien Beschreibungen folgte dem Konzept selbst wesentlich spezifischer.

Dieser Gegensatz verbindet die Arbeit mit der Forschung zu Objekthalluzinationen. Yifan Li und Kollegen führten 2023 die POPE-Evaluierung ein, nachdem sie festgestellt hatten, dass Bild-Sprach-Modelle nicht vorhandene Objekte beschreiben – besonders solche, die häufig in ihren Instruktionsdaten oder gemeinsam mit vorhandenen Objekten vorkommen. Die neue Studie zeigt nicht, dass natürliche Halluzinationen über denselben inneren Weg entstehen. Ihre Konzepteinspeisung ist künstlich. Sie zeigt einen möglichen Weg und warnt vor einem Messproblem: Eine kurze Faktenfrage kann ein Konzept übersehen, das später in einer freien Beschreibung auftaucht.

Die Einschränkungen sind erheblich. Die vertiefte Eingriffsanalyse betrifft Gemma-3-27B, die Konzeptmenge besteht aus konkreten Substantiven, und eine Person prüfte die Bewertungsstichprobe. Die Prompt-Formulierung veränderte Ergebnisse stark. Die gemessenen Raten beschreiben kontrollierte Aktivierungsänderungen, keinen gewöhnlichen Modellbetrieb und kein bewusstes Erleben.

Die praktische Schlussfolgerung ist enger und nützlicher. Evaluierer sollten sowohl bewerten, was ein multimodales Modell meldet, als auch, woher der Inhalt seiner Aussage nach stammt. Ein System kann einen verborgenen Zustand erkennen, ohne seine Herkunft zuverlässig erklären zu können.

Zurück zur erfundenen Forscherin am grauen Quadrat. Sie wiederholt den Versuch, fragt nun aber zuerst nach dem Eingriff und danach nach dem Bild. Weder das Konzept noch der Bildschirm haben sich verändert. Die Antwort schon. Ihr Notizbuch braucht getrennte Spalten für Wort, Quelle und genaue Frage, denn ein einziges Häkchen bei „richtig“ würde den Fehler verbergen.

## Quellen

- Binder, F. J., Chua, J., Korbak, T., Sleight, H., Hughes, J., Long, R., Perez, E., Turpin, M., & Evans, O. (2025). *Looking Inward: Language Models Can Learn About Themselves by Introspection*. https://arxiv.org/abs/2410.13787
- Johnson, M. K., & Raye, C. L. (1981). *Reality Monitoring*. https://doi.org/10.1037/0033-295X.88.1.67
- Khezresmaeilzadeh, T., Azizi, S., Kamal, M., & Pedram, M. (2026). *Did I See It or Think It? Probing Reality Monitoring in Vision-Language Models with Concept Injection*. https://arxiv.org/abs/2611.09014
- Li, Y., Du, Y., Zhou, K., Wang, J., Zhao, W. X., & Wen, J. R. (2023). *Evaluating Object Hallucination in Large Vision-Language Models*. https://aclanthology.org/2023.emnlp-main.20/
- Lindsey, J. (2025). *Emergent Introspective Awareness in Large Language Models*. https://arxiv.org/abs/2601.01828
