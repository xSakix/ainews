+++
title = "Ein kleiner kognitiver Kern fordert psychologische Blackboxen heraus"
slug = "kleiner-kognitiver-kern-fordert-psychologische-blackboxen"
description = "Zwei Forscher verbanden einige etablierte Ideen zu Gedächtnis, Kontext und Vorhersagefehlern zu einem Modell menschlicher Entscheidungen. CORE übertraf vergleichbare neuronale Prädiktoren in 137 Experimenten und hielt seine internen Abläufe dabei untersuchbar."
tags = ["research", "models"]
date = 2026-10-14T04:02:33+02:00
draft = false
+++

Eine Teilnehmerin sitzt allein in einem Psychologielabor. Ein Symbol erscheint, dann ein weiteres. Sie errät, hinter welcher Tür eine Belohnung liegt, erinnert sich an die letzte Überraschung und verändert langsam ihre Strategie. Diese Teilnehmerin ist erfunden, doch jede kleine Handlung gehört zu den experimentellen Beobachtungen hinter einem neuen Modell, das Millionen solcher Entscheidungen erklären will, ohne die Erklärung in einem neuronalen Netz zu verstecken.

## Viele Experimente, eine Erklärung

Marcel Binz und Eric Schulz vom Institute for Human-Centered AI bei Helmholtz Munich haben COntextual Retrieval and Encoding, kurz CORE, entwickelt. Ihr Preprint verbindet eine kleine Menge etablierter kognitiver Prinzipien in einem Rechenmodell und passt es dann gemeinsam an 7.036.442 menschliche Entscheidungen aus 137 Experimenten und 80.452 experimentellen Sitzungen an.

Der Anspruch geht über die Vorhersage einer Aufgabe hinaus. Die Psychologie hat Erklärungen für Assoziation, Vorhersagefehler, hierarchische Repräsentation, Erinnerungsabruf und Vergessen gesammelt, die oft in getrennten experimentellen Traditionen geprüft wurden. CORE fragt, wie viel der Verhaltensbeobachtungen diese Ideen erklären können, wenn sie unter einem gemeinsamen Satz von Mechanismen zusammenarbeiten müssen.

Seine Struktur ist eine Hierarchie episodischer Erinnerungen. Vorhersagefehler werden in diese Erinnerungen geschrieben. Der Kontext bestimmt, was kodiert wird, welche Erinnerungen abgerufen werden und wie sie verblassen. Diese Abläufe sind als Komponenten ausgedrückt, deren Rollen ein Forscher untersuchen kann, statt als uneingeschränktes Sequenzmodell, das nur auf Fehlerminimierung trainiert wurde.

Die Autoren vergleichen CORE mit einem Transformer vergleichbarer Konfiguration und mit Centaur, einem Basismodell menschlicher Kognition, das eine große Zusammenarbeit unter der Leitung von Binz vorstellte. Centaur stimmte ein Sprachmodell auf Psych-101 fein ab, einem Datensatz mit mehr als zehn Millionen Entscheidungen in 160 Experimenten. Es zeigte, dass ein großes Vorhersagesystem über Rahmengeschichten, Aufgabenänderungen und unbekannte Bereiche hinweg generalisieren konnte. Es machte auch den bekannten Preis von Basismodellen deutlich: Die Vorhersage wurde breit, während der gelernte Mechanismus schwer als psychologische Theorie zu formulieren blieb.

CORE kehrt diesen Zielkonflikt um. In der neuen Arbeit erreicht es eine niedrigere prädiktive negative Log-Likelihood als der vergleichbare Transformer: 262.572 gegenüber 329.043. Gegen Centaur lautet der Vergleich 262.572 gegenüber 389.151. CORE ist besser als der Transformer in allen 62 Studien, die für diesen Vergleich auf Studienebene genutzt wurden, und besser als Centaur in 47.

Diese Zahlen bedeuten nicht, dass CORE den menschlichen Geist erfasst hat. Sie vergleichen Vorhersagen innerhalb eines bestimmten zusammengestellten experimentellen Korpus. Sie zeigen aber, dass ein interpretierbares Modell nicht gezwungen war, Vorhersagereichweite zu opfern, nur weil seine Teile psychologische Bedeutungen hatten.

## Woran sich das Modell erinnert

Die Hierarchie ist wichtig, weil eine Entscheidung von Ereignissen auf unterschiedlichen Skalen abhängen kann. Ein jüngster Fehler kann die nächste Antwort verändern. Eine Folge verwandter Versuche kann eine lokale Situation etablieren. Ein Wechsel im Experiment kann ältere Erfahrung weniger relevant machen, selbst wenn sie gespeichert bleibt.

CORE behandelt diese Effekte durch kontextabhängige Kodierung und Abruf. Vorhersagefehler aktualisieren das Gedächtnis, statt nur eine einzelne Wertschätzung zu verändern. Das Modell kann eine Episode abrufen, wenn die aktuelle Situation ihr ähnelt, während sein Vergessensprozess Erfahrung geringer gewichtet, wenn sich der Kontext entfernt.

Dieser Entwurf erzeugt interne Spuren, die aus etablierten Theorien bekannt sind. Die Autoren berichten von Signaturen Bayes'schen Lernens in den latenten Variablen von CORE: Seine Aktualisierung reagiere auf Unsicherheit in einer Weise, die mit probabilistischer Inferenz verbunden sei. Sie finden auch Signaturen der Ereignissegmentierung. Das bedeutet, die interne Organisation des Modells spiegelt Grenzen zwischen Situationen wider, statt den gesamten Strom als einheitlich zu behandeln.

Das Ergebnis erweitert ein Forschungsprogramm, das dieselben Autoren aus der entgegengesetzten Richtung verfolgt haben. 2023 zeigten Binz und Schulz, dass auf psychologischen Experimenten feinabgestimmte Sprachmodelle traditionelle kognitive Modelle in zwei Entscheidungsbereichen übertreffen und Informationen über einzelne Teilnehmer enthalten konnten. Ihre Arbeit zu meta-gelernter Kognition argumentierte, Lernalgorithmen könnten Bayes-optimales Verhalten annähern und dabei begrenzte Rechenleistung sowie andere realistische Beschränkungen berücksichtigen.

Diese Systeme fragten, wie weit allgemeine Methoden des maschinellen Lernens in Richtung menschlichen Verhaltens gelangen könnten. CORE fragt, wie weit eine kompakte psychologische Theorie in Richtung der Vorhersagereichweite maschinellen Lernens gelangen kann. Beide Richtungen treffen sich nun auf einem Teil derselben Daten.

## Effekte reproduzieren statt benennen

Vorhersage ist nur ein Teil des Tests. Die Autoren simulieren CORE unter den experimentellen Bedingungen und fragen, ob es die in den Studien berichteten Verhaltenseffekte reproduziert. Es reproduziert 75 % davon.

Das ist eine strengere Anforderung, als eine durchschnittliche Entscheidungshäufigkeit zu treffen. Ein Effekt kann Anpassung, Verzerrung, Reihenfolge, Unsicherheit oder eine Veränderung nach einer Kontextgrenze betreffen. Ihn zu reproduzieren erfordert, dass sich das Verhalten des Modells in die relevante Richtung bewegt, wenn sich die experimentelle Manipulation ändert.

Das fehlende Viertel ist ebenso wichtig wie die erfolgreichen drei Viertel. Ein einheitliches Modell wird wissenschaftlich nützlich, wenn seine Fehler zeigen, wo der vorgeschlagene Kern unvollständig ist. Ein Blackbox-Prädiktor kann ein weiteres Muster aufnehmen, ohne Forschern zu sagen, welche Theorie sich verändert hat. Ein interpretierbares System erzwingt eine klarere Entscheidung: den Abruf überarbeiten, einen Mechanismus ergänzen, die Hierarchie verändern oder akzeptieren, dass das Phänomen außerhalb der Erklärung liegt.

Die Breite der Arbeit schafft auch Risiken. Experimente unterscheiden sich in Anweisungen, Antwortformaten, Teilnehmerpopulationen und analytischen Konventionen. Gemeinsame Anpassung kann Mechanismen bevorzugen, die gemeinsame Strukturen erklären, während sie ungewöhnliche glättet. Eine gesamte Likelihood kann eine schwache Erklärung eines kleinen, aber wichtigen Bereichs verbergen. Die Autoren berichten daher Vergleiche auf Studienebene und simulierte Effekte, nicht nur einen aggregierten Wert.

CORE ist zudem ein Preprint. Seine Aussagen, Implementierungsentscheidungen und Datensatzharmonisierung haben das Peer-Review nicht abgeschlossen. Das Korpus ist nach Maßstäben der experimentellen Psychologie groß, bleibt aber eine ausgewählte Sammlung von Aufgaben, die gemeinsam dargestellt und angepasst werden können. Menschliches Leben außerhalb eines Labors umfasst Sprache, soziale Beziehungen, Emotion und verkörpertes Handeln, die nicht auf sieben Millionen diskrete Entscheidungen verdichtet sind.

## Eine Theorie, die falsch sein kann

Der wichtigste Beitrag des Modells könnte methodischer Art sein. Die Kognitionswissenschaft musste oft zwischen einem transparenten Modell, das ein Paradigma erklärt, und einem allgemeinen Prädiktor wählen, der wenig über Mechanismen aussagt. CORE liefert Belege dafür, dass sich diese Grenze verschieben kann.

Das beseitigt neuronale Modelle oder Basismodelle nicht. Centaur liefert eine starke prädiktive Vergleichsbasis und kann über natürlichsprachliche Aufgabenbeschreibungen generalisieren. Ein kompaktes Modell kann solche Systeme als Konkurrenten, Datengeneratoren oder Entdeckungswerkzeuge nutzen. Entscheidend ist, welche Aussage jedes unterstützt. Ein Prädiktor zeigt, dass Verhalten vorausgesehen werden kann. Eine kognitive Theorie nennt die Abläufe, die es ihrer Ansicht nach erzeugt haben.

Weil CORE diese Abläufe nennt, können Forschende in sie eingreifen. Sie können kontextabhängiges Vergessen entfernen, die Gedächtnishierarchie abflachen oder verändern, wie Vorhersagefehler geschrieben werden, und dann bestimmen, welche Experimente scheitern. Sie können auch ein vorgeschlagenes Prinzip ergänzen und testen, ob es sich über die gesamte Sammlung hinweg seinen Platz verdient, statt nur eine handverlesene Aufgabe zu verbessern.

Zurück zur vorgestellten Teilnehmerin vor zwei Türen. Ihre nächste Entscheidung kann nun durch ein großes undurchsichtiges Modell vorhergesagt oder anhand einer Erinnerung an Überraschungen rekonstruiert werden, geordnet nach Kontext und mit der Möglichkeit zu verblassen. Das erste kann recht haben. Das zweite gibt dem Wissenschaftler etwas anderes: eine präzise Erklärung, die das nächste Experiment widerlegen kann.

## Quellen

- Binz, M., Dasgupta, I., Jagadish, A., Botvinick, M., Wang, J. X., & Schulz, E. (2023). *Meta-Learned Models of Cognition*. https://arxiv.org/abs/2304.06729
- Binz, M., et al. (2024). *Centaur: a foundation model of human cognition*. https://arxiv.org/abs/2410.20268
- Binz, M., & Schulz, E. (2023). *Turning large language models into cognitive models*. https://arxiv.org/abs/2306.03917
- Binz, M., & Schulz, E. (2026). *A small cognitive core explains human behavior at scale*. https://arxiv.org/abs/2610.13603
