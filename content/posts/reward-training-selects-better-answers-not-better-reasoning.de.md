+++
title = "Belohnungstraining wählt besser, statt besser zu denken"
slug = "belohnungstraining-waehlt-besser-statt-besser-zu-denken"
description = "Eine neue Studie verfolgte jeden Checkpoint im bestärkenden Lernen eines kleinen Modells. Die Genauigkeit stieg, doch das Modell entwickelte keine schärfere interne Repräsentation von Denkfehlern; es wählte Lösungen, die es bereits kannte, besser aus."
tags = ["research", "models"]
date = 2026-11-08T04:18:00+01:00
draft = false
+++

Ein Schüler kann eine Mathematikaufgabe in jedem zweiten Versuch lösen. Ein Lehrer belohnt jede richtige Antwort und sagt nichts zu den einzelnen Schritten. Nach wochenlangem Üben antwortet der Schüler häufiger richtig. Die naheliegende Schlussfolgerung lautet, er habe Mathematik besser gelernt. In diesem gedachten Klassenzimmer findet eine genauere Prüfung jedoch dasselbe Repertoire guter und schlechter Ansätze wie zuvor. Der Schüler ist besser darin geworden, daraus auszuwählen.

## Den gesamten Trainingslauf verfolgen

Diese Unterscheidung steht im Zentrum von *RLVR Sharpens the Pencil, Not the Mind*, einem neuen Preprint von Shreeyam Bangera und Manya Gupta. Die Forscher verfolgen OLMo-2-1B über 13 Checkpoints des bestärkenden Lernens mit überprüfbaren Belohnungen, kurz RLVR. Statt nur das Modell vor und nach dem Training zu vergleichen, untersuchen sie, was sich unterwegs verändert.

RLVR gewann an Bedeutung, weil sich eine richtige Antwort auf eine Mathematik- oder Programmieraufgabe automatisch prüfen lässt. Ein Trainingssystem erzeugt Lösungen, vergibt Belohnungen und erhöht die Wahrscheinlichkeit des Verhaltens, das diese Belohnungen erzielt hat. DeepSeek-R1 zeigte, wie weit dieser Ansatz reichen kann: Sein R1-Zero-Modell entwickelte durch bestärkendes Lernen bessere Mathematik- und Programmierleistungen, ohne vorherige überwachte Feinabstimmung.

Die sichtbaren Leistungsgewinne warfen eine schwierigere Frage auf. Vermittelt Belohnungstraining einem Modell neue Denkfähigkeiten, oder macht es bestehende Fähigkeiten leichter zugänglich? Die zweite Erklärung wird als Schärfung bezeichnet. Ein vortrainiertes Modell kann einen guten Lösungsweg bereits enthalten, ihm aber eine zu geringe Wahrscheinlichkeit zuweisen, um ihn beim ersten Versuch zu nutzen.

Bangera und Gupta nutzen die Offenheit von OLMo, um diese These entlang des Trainingsverlaufs zu prüfen. Ai2 veröffentlicht Zwischenstände des RLVR-Trainings für das Modell mit einer Milliarde Parametern. Die Autoren bewerten diese Checkpoints auf GSM8K, einem Datensatz mit 8.500 mathematischen Textaufgaben auf Grundschulniveau, den Karl Cobbe und Kollegen eingeführt haben.

## Zuverlässigerer Zugriff auf alte Lösungen

Die Genauigkeit beim ersten Versuch steigt von 58,0 % zu Beginn des Trainings auf 61,3 % am Ende. Der Anstieg ist real, aber bescheiden. Aufschlussreicher ist die Messung, bei der das Modell dieselbe Aufgabe 256-mal erhält und geprüft wird, ob irgendeine Antwort eine richtige Lösung enthält. Diese Lösungsabdeckung beginnt bei 94,5 % und endet bei 96,9 %.

Das Basismodell konnte damit schon vor RLVR für fast jede Aufgabe eine gültige Antwort erzeugen. Das Training machte es wahrscheinlicher, dass diese gültigen Wege beim ersten Versuch auftauchten. Es erschloss keinen großen neuen Bereich von Aufgaben, die das Modell erst danach lösen konnte.

Die Lösungsabdeckung zeigt nicht, was das Modell intern repräsentiert. Ein Modell könnte die richtige Antwort bereits gelegentlich erzeugen und während des Trainings dennoch ein besseres Verständnis des Schlussfolgerns entwickeln. Die Forscher prüfen diese Möglichkeit, indem sie drei Arten von Fehlern in dokumentierte Lösungswege einfügen. Anschließend trainieren sie lineare Sonden auf Modellaktivierungen, um die Fehler zu erkennen.

Die Leistung der Sonden bleibt über alle 13 Checkpoints zwischen 0,798 und 0,840 AUROC. Die Schwankung ist kleiner als das Konfidenzintervall. In diesem Test wird das Modell nicht besser darin, intern zwischen schlüssigem Denken und einem eingebauten Fehler zu unterscheiden.

Ein internes Signal verändert sich deutlich. Eine Sonde kann frühe von späten Checkpoints beim Token der endgültigen Antwort mit 0,93 AUROC unterscheiden. Auf Tokens in den Denkschritten angewandt, liegt dieselbe Sonde nahe am Zufallsniveau. Das Training scheint die Entscheidung am Ende der Lösung stärker neu zu ordnen als die Repräsentationen, die während ihrer Konstruktion verwendet werden.

## Was das Ergebnis zeigt und was nicht

Der Titel der Studie zieht eine klare Grenze, doch das Experiment ist eng gefasst. Es untersucht eine Modellfamilie mit einer Milliarde Parametern, einen Mathematik-Benchmark und einen RLVR-Trainingslauf. Lineare Sonden können Informationen übersehen, die in einer für sie nicht dekodierbaren Form vorliegen. GSM8K belohnt eine kurze Endantwort und bildet keine offenen Aufgaben ab, deren Richtigkeit schwer zu prüfen ist.

Die Autoren zeigen auch nicht, dass RLVR niemals neue Denkfähigkeiten hervorbringt. Ihre Befunde stützen eine engere Aussage: In diesem Trainingslauf lässt sich der beobachtete Gewinn besser durch eine verbesserte Auswahl vorhandener Lösungswege erklären als durch eine schärfere interne Repräsentation der getesteten Fehler.

Diese Einschränkung ist wichtig, weil RLVR oft über sein sichtbares Verhalten beschrieben wird. Ein Modell erzeugt längere Ketten, versucht andere Ansätze und gelangt zu mehr richtigen Antworten. Diese Veränderungen können wie neues Verständnis aussehen. Die Checkpoint-Analyse zeigt, dass sich eine Ausgabe verbessern kann, während sich eine Messung des Denkprozesses kaum verändert.

Der Befund verdeutlicht außerdem, warum das Erzeugen mehrerer Antworten nach bestärkendem Lernen nützlich bleibt. Wenn das Wissen eines Modells mehr Lösungen abdeckt, als seine erste Antwort erkennen lässt, legen wiederholte Versuche Fähigkeiten frei, die ein einzelner Durchlauf verfehlt. RLVR verändert die Wahrscheinlichkeitsverteilung dieser Versuche. Es macht die Genauigkeit beim ersten Versuch nicht zu einem vollständigen Maß dessen, was das Modell weiß.

## Den Prozess trainieren

Überprüfbare Endantworten sind attraktiv, weil sie günstig und objektiv sind. Eine Zahl ist richtig oder falsch. Ein Programm besteht seine Tests oder nicht. Die Belohnung muss nicht sagen, welcher Denkschritt half, welche Abkürzung anderswo scheitern wird oder ob das Modell seinen eigenen Fehler erkannte.

Eine bessere Fehlerrepräsentation zu trainieren würde ein Signal erfordern, das näher am Prozess liegt. Das könnten überprüfte Zwischenschritte, gezielt eingebaute irreführende Fehler, Prozessaufsicht oder Aufgaben sein, die gut kalibrierte Selbstkorrektur belohnen. Jede Möglichkeit kostet mehr als die Prüfung einer Endantwort und bringt ihr eigenes Bewertungsproblem mit sich.

Die Studie schreibt keine dieser Methoden vor. Sie liefert eine Diagnosemethode, die spätere Arbeiten wiederverwenden können: Zwischenstände aufbewahren, die Lösungsabdeckung statt nur erster Versuche messen und die Tokens des Denkprozesses getrennt vom Token untersuchen, das die Antwort festlegt. Ein Vorher-Nachher-Wert verliert den Weg, der den Gewinn erklärt.

Diese Lehre reicht über Mathematik hinaus. Agenten erhalten Belohnungen für erledigte Tickets, bestandene Tests oder erfolgreiche Werkzeugaufrufe. Wenn das Training hauptsächlich die Auswahl zwischen bestehenden Verhaltensweisen verbessert, kann der Agent leistungsfähiger wirken, ohne einen fehlerhaften Plan besser zu erkennen. Die Evaluierung braucht dann sowohl Ergebnisse als auch Fehlertests auf Prozessebene.

Zurück zum erfundenen Schüler nach einer weiteren Woche. Die richtigen Antworten kommen nun schneller, und die Kurve des Lehrers steigt. Bevor er zu schwierigerem Stoff übergeht, baut der Lehrer einen plausiblen Fehler in eine ausgearbeitete Lösung ein und bittet den Schüler, ihn zu finden. Die folgende Pause misst etwas, das die Belohnungskurve nicht erfasst hat.

## Quellen

- Ai2. (2025). *OLMo-2-0425-1B-SFT model card*. https://huggingface.co/allenai/OLMo-2-0425-1B-SFT
- Bangera, S., & Gupta, M. (2026). *RLVR Sharpens the Pencil, Not the Mind*. https://arxiv.org/abs/2611.02574
- Cobbe, K., Kosaraju, V., Bavarian, M., et al. (2021). *Training Verifiers to Solve Math Word Problems*. https://arxiv.org/abs/2110.14168
- DeepSeek-AI. (2025). *DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning*. https://arxiv.org/abs/2501.12948
