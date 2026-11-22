+++
title = "Google verkürzt Wartezeiten zwischen Trainingsclustern"
slug = "google-verkuerzt-wartezeiten-zwischen-trainingsclustern"
description = "Beim Training eines Modells mit 32 Milliarden Parametern ließ Google zwei TPU-Gruppen kleinere Datenpakete austauschen. Trotz simulierter Bandbreitenbegrenzung blieb die Dauer eines Trainingsschritts stabil, doch die Kosten beim Einsatz über reale Rechenzentren hinweg bleiben offen."
tags = ["research", "hardware", "models"]
date = 2026-11-22T06:29:30+01:00
draft = false
+++

Googles Ingenieure begrenzten die Bandbreite zwischen zwei Gruppen von TPUs. Bei 10 Gigabit pro Sekunde dauerte ein Schritt im herkömmlichen datenparallelen Training 55,11 Sekunden. Dasselbe Modell benötigte nur 5,76 Sekunden pro Schritt, wenn die Gruppen im Hintergrund kleinere Aktualisierungen austauschten.

Für das im November veröffentlichte Experiment testete Google Qwen3-32B auf zwei TPU-v5p-32-Slices. Beide waren über ein schnelles Netz verbunden. Mit der Verkehrssteuerung von Linux simulierte das Team die begrenzte Bandbreite, die zwischen zwei Beschleunigergruppen zur Verfügung stehen kann. So blieben Hardware und Modell gleich, während die Forscher variierten, wie viele Daten über die Verbindung fließen konnten.

## Wenn die Verbindung das Tempo vorgibt

Beim üblichen datenparallelen Training erhält jede Gruppe eine Kopie des Modells und einen anderen Stapel von Trainingsbeispielen. Die Gruppen berechnen Gradienten, die angeben, wie die Modellparameter zu ändern sind. Anschließend führen sie die Gradienten zusammen, damit die Modellkopien synchron bleiben. In einem schnellen Netz kann dieser Austausch teilweise während der Berechnung stattfinden. Dauert die Übertragung länger als die Berechnung, mit der sie sich überlappen lässt, müssen die Beschleuniger warten.

Google schätzt, dass bei seinem datenparallelen Aufbau in jedem Schritt etwa 65,5 Gigabyte über die Verbindung flossen. Bei voller Bandbreite benötigte das Referenzverfahren etwa 5,6 Sekunden pro Schritt, bei 30 Gigabit pro Sekunde waren es 19,41 Sekunden. Das Modell und der Rechenaufwand pro Schritt blieben gleich. Die zusätzliche Zeit entfiel größtenteils auf die Übertragung der Aktualisierungen.

Dieses Problem wollten Arthur Douillard und seine Kollegen mit ihrer ursprünglichen DiLoCo-Arbeit lösen. In ihrer Studie zum Training von Sprachmodellen mit C4 ließen sie acht Gruppen abschnittsweise unabhängig voneinander trainieren und ihre Aktualisierungen regelmäßig zusammenführen. Nach eigenen Angaben erzielten sie in diesem speziellen Experiment das gleiche Ergebnis wie beim vollständig synchronen Training und übertrugen dabei nur ein Fünfhundertstel der Daten. Da sich der Versuchsaufbau vom neuen MaxText-Benchmark unterscheidet, messen die beiden Angaben zur Verringerung des Datenverkehrs unterschiedliche Dinge.

## Die Übertragung anders verteilen

Beim ursprünglichen DiLoCo blieb am Ende jedes Abschnitts ein Problem. Die weniger aufwendigen Schritte liefen mit voller Geschwindigkeit, doch dann mussten die Gruppen das gesamte Modell auf einmal synchronisieren. Bei der Begrenzung auf 10 Gigabit pro Sekunde in Googles neuem Benchmark benötigte herkömmliches DiLoCo durchschnittlich 7,55 Sekunden pro Schritt. Die regelmäßigen Pausen blieben. Bei einem Trainingssystem, das die meiste Zeit ausgelastet ist, können solche wiederkehrenden Unterbrechungen erheblich zur durchschnittlichen Schrittdauer beitragen.

Die 2025 erschienene Arbeit zu Streaming DiLoCo änderte den Zeitplan. Statt das gesamte Modell in einem Vorgang zu übertragen, tauschen die Gruppen nacheinander einzelne Teile aus. Während die Übertragung läuft, können die nächsten Trainingsschritte bereits beginnen. Die Arbeit untersuchte außerdem, wie sich die ausgetauschten Daten quantisieren lassen, sodass zu ihrer Darstellung weniger Bits nötig sind. Entscheidend ist der Unterschied zwischen der über den gesamten Lauf übertragenen Datenmenge und der Menge, die das System auf einmal zu senden versucht.

Im MaxText-Experiment teilte das Team Qwen3-32B in 65 Fragmente. Eine Gruppe konnte weitertrainieren, während die Host-CPUs im Hintergrund rund ein Gigabyte Daten für ein Fragment synchronisierten. Über 65 Schritte sank der Verkehr zwischen den Slices von 4.258,8 Gigabyte bei herkömmlicher Datenparallelität auf 67 Gigabyte mit Streaming DiLoCo. Die durchschnittliche Schrittdauer lag sowohl bei 30 als auch bei 10 Gigabit pro Sekunde bei 5,76 Sekunden. Ohne Bandbreitenbegrenzung benötigten alle drei Verfahren ungefähr gleich viel Zeit pro Schritt.

## Das Experiment maß mehr als den Datenverkehr

Auch ein Modell, das weniger Zeit mit Warten verbringt, kann am Ende des Trainings schlechter abschneiden. Wenn die Recheneinheiten ihre Gewichte unabhängig aktualisieren, sieht jede Einheit eine andere Folge von Gewichten. Google hob Modelle mit einer Mischung von Experten hervor. Dort entscheidet ein Router, welche Teile des Modells ein Token verarbeiten. Lernen die Router zu lange unabhängig voneinander, können sie dazu übergehen, ähnliche Beispiele an unterschiedliche Experten zu schicken.

Das MaxText-Team verglich den Validierungsverlust bei Läufen über 4.000 Schritte für zwei solcher Modelle, Qwen3-30B-A3B und Gemma4-26B-A4B. Die Streaming-Läufe hätten laut Team ebenso gut oder geringfügig besser abgeschnitten als die synchrone Referenz. Im Qwen-Lauf passte das Team die Synchronisierung während der ersten rund 800 Schritte an. Das Ergebnis erfasst, wie gut die Modelle im untersuchten Zeitraum zurückgehaltene Daten vorhersagten. Wie viel Abstimmung bei anderen Modellen und längeren Läufen nötig wäre, bleibt offen.

Für Teams, die sich Rechenkapazität an mehreren Standorten sichern müssen, stellen sich zwei getrennte Fragen. Kann der Trainingslauf weiterrechnen, während Aktualisierungen übertragen werden? Und was kostet es, ein vorgegebenes Qualitätsniveau zu erreichen, wenn im Netz reale Latenzen, Ausfälle und konkurrierender Datenverkehr hinzukommen, die das Experiment nicht nachgebildet hat? Der Durchsatzvergleich nutzte ein dichtes Modell und zwei Beschleunigergruppen. Die Qualitätsmessungen beantworten über eine begrenzte Zahl von Schritten eine andere Frage. Für reale Standorte nennt Google weder einen Kostenvergleich noch die Zeit bis zum Erreichen eines angestrebten Verlustwerts.

Die Ingenieure hatten zunächst eine Verbindung gedrosselt, die den Datenverkehr sonst bewältigt hätte. Mit aktiver Begrenzung benötigte das herkömmliche datenparallele Verfahren fast 50 zusätzliche Sekunden pro Schritt. Streaming DiLoCo schloss einen Schritt mit und ohne Begrenzung in nahezu derselben Zeit ab.

## Quellen

- Douillard, A., Feng, Q., Rusu, A. A., et al. (2023). *DiLoCo: Distributed Low-Communication Training of Language Models*. https://arxiv.org/abs/2311.08105
- Douillard, A., Donchev, Y., Rush, K., et al. (2025). *Streaming DiLoCo with overlapping communication: Towards a Distributed Free Lunch*. https://arxiv.org/abs/2501.18512
- Khatwani, M., Zuo, C., Fallen, N., et al. (2026). *Distributed LLM Training Across Metros: Streaming DiLoCo in MaxText*. https://developers.googleblog.com/distributed-llm-training-across-metros-streaming-diloco-in-maxtext/
