+++
title = "Reflection stellt Beam vor der Gewichtsveröffentlichung vor"
slug = "reflection-stellt-beam-vor-gewichtsveroeffentlichung-vor"
description = "Das Mixture-of-Experts-Modell mit 501 Milliarden Parametern ist nur über einen Vorabzugang verfügbar. Laut Reflection folgen Gewichte, technischer Bericht und Entwicklerwerkzeuge später im Oktober."
tags = ["models", "agents"]
date = 2026-10-06T04:09:31+02:00
draft = false
+++

Reflection AI hat Beam angekündigt, ein Modell mit 501 Milliarden Parametern für Programmierung und Agentenarbeit. Entwickler können seine Gewichte aber noch nicht prüfen oder ausführen.

Das kalifornische KI-Unternehmen beschreibt Beam als dünn aktiviertes Mixture-of-Experts-Modell: Es speichere 501 Milliarden Parameter, aktiviere aber 23 Milliarden pro Token. Der Vorabzugang erfordert eine Anmeldung. Gewichte, Lizenz, Modellkarte, technischer Bericht und Entwicklerwerkzeuge stehen noch aus.

Für Entwickler, die ein offenes Modell auswählen, ist der Unterschied wichtig. Ein Modell mit offenen Gewichten lässt sich mit privaten Arbeitslasten testen, verändern und einsetzen, ohne vom Dienst des Herstellers abhängig zu sein. Eine Ankündigung und eine Benchmark-Tabelle ermöglichen diese Prüfungen noch nicht.

Reflection erklärt, Beam sei auf 23,8 Billionen Token trainiert worden. Anschließend seien vier Wochen lang mehr als 100 Millionen Reinforcement-Learning-Rollouts auf 10.500 NVIDIA-GB300-GPUs ausgeführt worden. Diese Zahlen beschreiben einen ungewöhnlich großen Trainingslauf. Das Unternehmen hat aber den technischen Bericht noch nicht veröffentlicht, der zur Prüfung der Datenmischung oder des Evaluierungsaufbaus nötig ist.

Die eigene Tabelle des Labors gibt Beam Werte von 80,9 auf SWE-bench Verified und 80,1 auf Terminal-Bench 2.1. Sie zeigt Beam auf den meisten aufgeführten Tests außerdem hinter Kimi K3, GLM-5.3 und Qwen 3.8-Max. Reflections Hauptvergleich betrifft die Effizienz: Beam erreiche laut Unternehmen mit drei- bis viermal weniger Inferenzrechenaufwand vergleichbare Ergebnisse wie GLM-5.2, auf Grundlage seiner eigenen Schätzung der Gleitkommaoperationen.

Diese Aussage könnte für Teams, die lange Agentensitzungen bezahlen, wichtiger sein als ein knapper Benchmark-Vorsprung. Dünne Aktivierung verringert den Rechenaufwand pro Token. Das vollständige Modell benötigt allerdings weiterhin genug Speicher und Infrastruktur, um Hunderte Milliarden Parameter zu speichern und bereitzustellen.

Laut Reflection durchläuft Beam abschließende Sicherheitstests. Das Unternehmen plant, Gewichte, technischen Bericht, Modellkarte und Entwicklerartefakte später im Oktober 2026 zu veröffentlichen. Einen konkreten Veröffentlichungstag hat es nicht genannt.

## Überprüfung {#verification}

| Behauptung | Einstufung | Primärquelle | Unabhängige Überprüfung |
| --- | --- | --- | --- |
| Reflection kündigte Beam an und öffnete die Anmeldung zum Vorabzugang | VERIFIZIERT | [Reflection-Ankündigung](https://reflection.ai/blog/introducing-beam) | für die Handlung des Unternehmens nicht nötig |
| Beam hat insgesamt 501 Milliarden Parameter und 23 Milliarden aktive Parameter pro Token | LAUT UNTERNEHMEN | [Reflection-Ankündigung](https://reflection.ai/blog/introducing-beam) | keine; Gewichte und Bericht stehen aus |
| Das Training nutzte 23,8 Billionen Token und mehr als 100 Millionen RL-Rollouts auf 10.500 GB300-GPUs für vier Wochen | LAUT UNTERNEHMEN | [Reflection-Ankündigung](https://reflection.ai/blog/introducing-beam) | keine |
| Beam erreichte 80,9 auf SWE-bench Verified und 80,1 auf Terminal-Bench 2.1 | LAUT UNTERNEHMEN | [Reflection-Ankündigung](https://reflection.ai/blog/introducing-beam) | keine |
| Reflection schätzt vergleichbare Ergebnisse wie GLM-5.2 bei drei- bis viermal weniger Inferenzrechenaufwand | LAUT UNTERNEHMEN | [Reflection-Ankündigung](https://reflection.ai/blog/introducing-beam) | keine |
| Gewichte, Bericht, Modellkarte und Entwicklerartefakte sind für später im Oktober 2026 versprochen | VERIFIZIERT | [Reflection-Ankündigung](https://reflection.ai/blog/introducing-beam) | für den genannten Zeitplan nicht nötig |
