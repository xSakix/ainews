+++
title = "Modelle kennen Zeitregeln, verkennen aber ihre eigene Laufzeit"
slug = "modelle-kennen-zeitregeln-verkennen-eigene-laufzeit"
description = "Sprachmodelle beantworteten bis zu 97,5 % der Fragen zu Zeitregeln richtig und unterschätzten dann ihre Bearbeitungszeit um bis zu 99,5 %. Eine Studie zeigt, warum Agenten trotz Überlegungen zu Zeitplänen bei Warten, Kosten und Koordination schlecht entscheiden können."
tags = ["research", "agents", "models"]
date = 2026-11-12T04:18:00+01:00
draft = false
+++

Ein Ingenieur bittet einen Agenten, einen ausgefallenen Dienst zu untersuchen und die benötigte Zeit zu nennen. Der Agent liest Protokolle, zählt Schritte auf und verspricht eine Antwort in zehn Minuten. Er ist nach Sekunden fertig. Später bekommt derselbe Agent ein etwas genaueres Werkzeug angeboten, das länger warten lässt. Er lehnt es ab, weil er diese Wartezeit behandelt, als existiere sie kaum. Der Ingenieur ist erfunden. Die beiden Fehler spiegeln jedoch Messungen einer neuen Studie darüber wider, wie Sprachmodelle mit Zeit umgehen.

## Regeln ohne Uhr

Ryan Liu und fünf Kollegen von Princeton, Columbia, UC Berkeley und UCLA untersuchten zeitliche Kompetenz als Kette mit vier Gliedern: Zeitwissen, Dauerschätzungen, menschenähnliche Verzerrungen und Entscheidungen, die Zeit gegen Genauigkeit abwägen. Ihr am 7. November eingereichter Preprint untersucht Claude Opus 5, GPT-5.6 Sol und Gemini 3.7 Flash. Die Frage ist, ob Modelle ihr angelesenes Zeitwissen auf eine Dimension anwenden können, die sie nicht unmittelbar erleben.

Diese Unterscheidung ist wichtig, weil ein Sprachmodell das Intervall zwischen zwei Aufrufen nicht durchlebt. Ein Zeitstempel kann im Kontext stehen, doch das Modell spürt keine Minuten vergehen. Selbst autonome Systeme werden gewöhnlich nach einem externen Zeitplan oder Ereignis aktiviert. Die Forscher beschreiben Zeit für Modelle als Information aus zweiter Hand: in Text und Metadaten vorhanden, als kontinuierliches Erlebnis abwesend.

Das erste Experiment gab den Modellen eine faire Gelegenheit, ihr Wissen zu zeigen. Das Team leitete fünf Axiome aus Forschung zu Lernen, Fähigkeitsverlust, Aufgabenwechsel, Ermüdung und Erholung ab. Daraus gewann es Prinzipien wie die Kosten von Unterbrechungen und den Vorteil gebündelter verwandter Arbeit. Der Test nutzte kurze Arbeitsszenarien statt Wissensfragen. Ein Modell musste beurteilen, ob eine veränderte Reihenfolge eine Aufgabe verlängert oder verkürzt.

Die Ergebnisse waren stark. Über Axiome und abgeleitete Sätze hinweg erreichte Claude 92,0 %, GPT 97,5 % und Gemini 96,3 %. Die Antworten blieben auch konsistent, wenn die Forscher Vergleiche umkehrten. Fehler waren meist stabile Überzeugungen statt zufälliger Vermutungen.

Dieser Teil erweitert eine lange Forschungslinie zum formalen zeitlichen Schlussfolgern. James Allens Intervallrahmen von 1983 gab künstlicher Intelligenz eine Möglichkeit, Beziehungen darzustellen: Ein Ereignis liegt vor, während oder nach einem anderen. Die neue Studie fragt etwas anderes. Ein Modell kann diese Beziehungen kennen und dennoch keine verlässliche Größenordnung dafür besitzen, wie lange seine eigene Arbeit dauert.

## Schätzungen ohne Bezug zur Ausführung

Für das zweite Experiment nutzten die Forscher Software- und Forschungsaufgaben aus dem Benchmark Human-Calibrated Autonomy Software Tasks. HCAST enthält menschliche Referenzwerte, die bei Fachkräften unter Bedingungen erhoben wurden, die mit Agentendurchläufen vergleichbar sind. Verwandte Arbeiten von Thomas Kwa und Kollegen nutzen diese Dauern, um Agentenfähigkeit als Zeithorizont zur Aufgabenerfüllung auszudrücken.

Die Modelle sahen vollständige Aufgabenanweisungen und eine Beschreibung des Ausführenden. Sie schätzten eine Bearbeitungszeit und gaben Unsicherheitsintervalle an. Die Forscher verglichen diese Schätzungen anschließend mit protokollierten Dauern von Menschen und Agenten. Ein separater Test nutzte 500 Anfragen aus WildChat. Jedes Modell sagte seine Antwortdauer voraus und antwortete dann, während das System die tatsächliche Laufzeit erfasste. Fünf Wiederholungen je Modell und Anfrage ergaben 7.500 Versuche.

Das zentrale Versagen lag bei der Selbstkalibrierung. Modelle unterschätzten ihre eigene Bearbeitungszeit um bis zu 99,5 % und erkannten nicht zuverlässig, welche Aufgaben länger dauern würden. Sie nutzten nicht bloß menschliche Einheiten für Maschinenarbeit falsch. Auch die relative Reihenfolge misslang, die ein Planungssystem selbst dann benötigt, wenn die genaue Sekundenzahl unwichtig ist.

Schätzungen menschlicher Bearbeitungszeiten waren besser, offenbarten aber eine weitere Schwäche. Die Formulierung eines Ereignisses veränderte das Urteil darüber, wie lange es sich anfühlen würde. Die Modelle reproduzierten einen bekannten menschlichen Framing-Bias und verstärkten ihn um bis zum Faktor 1,3.

Das verbindet Modellverhalten mit dem von Roger Buehler, Dale Griffin und Michael Ross untersuchten Planungsfehlschluss. Menschen erwarten oft einen früheren Abschluss, als vergangene Erfahrungen nahelegen. Das gilt besonders, wenn sie sich auf den Plan der aktuellen Aufgabe statt auf vergleichbare Ergebnisse konzentrieren. Modelle können Beschreibungen dieses Bias aus Text lernen. Die neue Arbeit zeigt, dass Wissen über eine Verzerrung keinen Schutz vor ihr garantiert.

## Warten zählte kaum

Das letzte Experiment wechselte von Schätzungen zu Entscheidungen. Die Forscher boten Optionen an, die längeres Warten gegen höhere Genauigkeit tauschten. Indem sie unter manchen Bedingungen die Dauer angaben, konnten sie eine schlechte Schätzung von einer schwachen Präferenz für Zeitersparnis trennen.

Manche Modelle behandelten große Verzögerungsänderungen als nahezu irrelevant. Beim Antworten konnten sie eine 1.200-fache Verlängerung der Wartezeit ignorieren. Der Fehler blieb selbst bei ausdrücklich genannter Dauer bestehen; die Schätzung allein erklärte ihn also nicht. Die Entscheidungsstrategie selbst bewertete Zeit inkonsistent.

Die Arbeit behauptet nicht, alle Modelle scheiterten an jeder Zeitaufgabe. Ihr erstes Experiment zeigt das Gegenteil. Sie weist auch keine einzelne innere Ursache nach. Die Bewertung umfasst drei Modellfamilien und bestimmte Aufgabenbedingungen. Die Autoren beschreiben zeitliche Kompetenz durch beobachtbare Antworten, nicht durch eine direkte Messung subjektiven Erlebens.

Das praktische Risiko ist enger und leichter erkennbar. Ein Agent kann zwischen Werkzeugen mit unterschiedlichen Latenzen wählen, Arbeit unter anderen Agenten verteilen, laufzeitabhängige Kosten schätzen oder einem Menschen sagen, wann er zurückkommen soll. Ein System, das die Regel zum Bündeln von Aufgaben kennt, kann seine Warteschlange dennoch falsch ordnen. Ein System, das Unterbrechungskosten erklärt, kann weiterhin eine unmögliche Frist versprechen.

Zeitschätzungen sollten deshalb als Vorhersagen behandelt werden, die externe Kalibrierung benötigen. Ein Host kann tatsächliche Dauern aufzeichnen, aufgabenspezifische Verteilungen pflegen und Fristen außerhalb des Modells durchsetzen. Er kann Wartekosten auch ausdrücklich nennen und prüfen, ob sich eine Entscheidung bei steigenden Kosten ändert. Diese Kontrollen ähneln einer allgemeinen Lehre der Agentensicherheit: Messbarer Zustand und Durchsetzung gehören in das umgebende System, statt sich auf eine richtige Erklärung im Text zu verlassen.

Zurück zum erfundenen Ingenieur nach einigen Wochen. Der Agent schreibt weiterhin eine selbstsichere Schätzung. Die Oberfläche stellt ihr aber die mediane Laufzeit vergleichbarer Arbeiten und einen breiten Unsicherheitsbereich gegenüber. Der Planer und nicht das Modell entscheidet, wann abgebrochen oder gewartet wird. Der Ingenieur hat dem Agenten kein Zeitgefühl gegeben. Das System tut lediglich nicht länger so, als sei gewandt über Uhren zu sprechen dasselbe, wie eine zu führen.

## Quellen

- Allen, J. F. (1983). *Maintaining Knowledge about Temporal Intervals*. https://doi.org/10.1145/182.358434
- Buehler, R., Griffin, D., & Ross, M. (1994). *Exploring the “Planning Fallacy”: Why People Underestimate Their Task Completion Times*. https://doi.org/10.1037/0022-3514.67.3.366
- Kwa, T., et al. (2025). *Measuring AI Ability to Complete Long Software Tasks*. https://arxiv.org/abs/2503.14499
- Liu, R., Lee, D., Ai, I. S., Abdulhai, M., Dubey, R., & Griffiths, T. L. (2026). *In Search of Lost Time: Temporal Competence in Large Language Models*. https://arxiv.org/abs/2611.10536
- Rein, D., et al. (2025). *HCAST: Human-Calibrated Autonomy Software Tasks*. https://arxiv.org/abs/2503.17354
