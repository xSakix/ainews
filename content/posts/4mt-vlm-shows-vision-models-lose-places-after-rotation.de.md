+++
title = "4MT-VLM: Visuelle Modelle verlieren Orte nach einer Drehung"
slug = "4mt-vlm-visuelle-modelle-verlieren-orte-nach-drehung"
description = "Ein Preprint passt einen klinischen Test des räumlichen Gedächtnisses für 16 Vision-Language-Modelle an. Alle erkennen eine Landschaft aus dem betrachteten Winkel, doch die meisten raten nur noch, sobald sich die Kamera bewegt."
tags = ["research", "models"]
date = 2026-10-06T04:02:31+02:00
draft = false
+++

Vision-Language-Modelle erkennen eine Landschaft aus dem Winkel, aus dem sie sie zuerst gesehen haben. Sobald sich die Kamera bewegt, können die meisten sie jedoch nicht mehr auswählen. Das zeigt 4MT-VLM, ein neuer Benchmark auf Basis eines klinischen Tests des räumlichen Gedächtnisses.

Markus Frey vom deutschen Institut für angewandte Forschung Fraunhofer IAIS gab 16 offenen und geschlossenen Modellen die Aufgabe, die auch menschliche Patienten erhalten: eine computergenerierte Landschaft mit vier Gipfeln betrachten und sie dann unter vier ähnlichen Landschaften aus einem neuen Blickwinkel finden. Ein menschlicher Freiwilliger löste etwa vier von fünf Versuchen mit Drehung. Die meisten Modelle waren nicht besser als Raten.

## Warum das wichtig ist {#why-it-matters}

Ein Robotikingenieur, der ein Vision-Language-Modell als Augen eines mobilen Roboters nutzt, benötigt genau diese Fähigkeit: einen Raum erkennen, nachdem sich der Roboter umgedreht hat. Laut Preprint liefern sie weder größere Modelle noch ausführlichere Anweisungen.

## Erkennen funktioniert, Drehen nicht

Der Benchmark passt den Four Mountains Test an. Kliniker nutzen ihn, weil die Werte bei Schäden am Hippocampus und in der frühen Alzheimer-Krankheit sinken. Farben, Texturen und Beleuchtung ändern sich bei jedem Versuch zwischen dem Lernbild und den Testbildern. Selbst ein Versuch ohne Drehung lässt sich daher nicht durch Pixelabgleich lösen. Frey nutzt die Genauigkeit bei diesen ungedrehten Versuchen als Prüfung, ob ein Modell den Ort überhaupt erkennen kann.

Die Modelle bestehen diese Prüfung und scheitern dann an der Drehung. OpenAIs GPT-5.6 Luna beantwortete jeden ungedrehten Versuch richtig, aber nur 31 % der gedrehten, bei denen Raten eine von vier Antworten trifft. Über alle 16 Modelle hinweg war der schlechteste Winkel 135 Grad. Dort lag die Genauigkeit deutlich unter Zufallsniveau.

Eine halbe Drehung um 180 Grad, die größte Änderung, erzielte bessere Werte als 135 Grad. Frey wertet das als Hinweis auf einen Bildtrick, etwa den Vergleich mit einem Spiegelbild der Szene, statt auf das Drehen einer internen Karte. Der menschliche Vergleich stammt von nur einem Teilnehmer. Das reicht, um die Lösbarkeit zu zeigen, aber nicht für einen menschlichen Durchschnitt.

## Größere Modelle erkennen mehr, drehen aber nicht besser

Die Größe verbesserte das Erkennen und ließ die Leistung bei Drehungen unverändert. In Alibabas Qwen2.5-VL-Familie mit 3 bis 72 Milliarden Parametern stieg die Genauigkeit ohne Drehung von 30 auf 75 %, während sie mit Drehung auf oder unter Zufallsniveau blieb. Die InternVL3.5-Familie wiederholte das Muster von 1 bis 38 Milliarden Parametern. Unter 14 Modellen mit offenen Gewichten bis zu 235 Milliarden Parametern beantwortete keines mehr als 31 % der gedrehten Versuche richtig. Eine „denkende“ Variante erreichte denselben Wert wie ihr Standardpendant.

Anweisungen schlossen die Lücke nicht. Frey führte Qwen2.5-VL-32B mit sechs Prompts aus, darunter ausdrückliche Verfahren wie die Vorstellung der Anordnung von direkt oben oder die Orientierung am markantesten Gipfel. Alle sechs ließen es unter Zufallsniveau.

## Weiter entfernte falsche Antworten zeigen eine grobe Karte

Das aufschlussreichste Experiment änderte nur die falschen Antworten. Frey maß in Metern, wie weit die Gipfel zweier Landschaften nach der bestmöglichen Drehung auseinanderliegen. Anschließend zeichnete er die drei Ablenkungsbilder mit weiter entfernten Anordnungen neu, während Ziel und Winkel identisch blieben.

Den nächstgelegenen Ablenker von etwa 7 auf etwa 31 Meter zu entfernen hob Googles Gemini 3.8 Flash bei gedrehten Versuchen von 39 auf 85 % und GPT-5.6 Luna von 31 auf 55 %. Kein offenes Modell verbesserte sich statistisch bedeutsam.

Das ist der Beleg des Papers dafür, dass Spitzenmodelle eine gewisse Vorstellung von der Anordnung besitzen, allerdings nur mit niedriger Auflösung. Ein Modell ohne Karte könnte vom Abstand der Ablenker nicht profitieren. Ein Modell mit einer Karte auf menschlichem Niveau bräuchte keine 30 Meter Trennung. Der Effekt ähnelt dem Erkennen einer Stadt aus einem Flugzeugfenster, ohne die eigene Straße zu erkennen.

Die Fehler weisen in dieselbe Richtung. Ein Mensch, der falsch antwortet, wählt meist den Ablenker, dessen Anordnung dem Ziel am nächsten liegt. Die falschen Antworten der Modelle verteilten sich fast gleichmäßig auf nahe und ferne Ablenker, als spiele die Anordnung bei der Wahl keine Rolle.

## Ein synthetischer Test eines einzelnen Autors

Die Landschaften sind synthetische Renderings. Frey merkt an, dass Vortraining auf ähnlich gerenderten Szenen manche Modelle begünstigen könnte. Die Parameterzahlen geschlossener Modelle sind nicht offengelegt. Die Belege zur Skalierung beruhen daher allein auf offenen Modellen. Der am 30. September 2026 auf arXiv veröffentlichte Preprint hat einen Autor und verlinkt weder Code noch Datensatz.

Laut Frey werden weitere menschliche Teilnehmer getestet. Das wird dem Wert des Freiwilligen von 82 % bei gedrehten Versuchen eine angemessene Vergleichsgruppe geben.

## Überprüfung {#verification}

| Behauptung | Einstufung | Primärquelle | Unabhängige Überprüfung |
| --- | --- | --- | --- |
| 4MT-VLM passt den Four Mountains Test an; 500 Versuche mit 100 erzeugten Landschaften, 16 Modelle getestet | VERIFIZIERT | [Frey-Preprint](https://arxiv.org/abs/2609.39238) | keine; eigener Benchmark des Autors |
| Das Erscheinungsbild wird bei jedem Winkel zwischen Lern- und Testbildern neu gezogen | VERIFIZIERT | [Frey-Preprint](https://arxiv.org/abs/2609.39238) | keine; Methodenbeschreibung |
| Ein menschlicher Teilnehmer beantwortete 100 % der ungedrehten und 82 % der gedrehten Versuche richtig | LAUT UNTERNEHMEN | [Frey-Preprint](https://arxiv.org/abs/2609.39238) | keine; nur ein Teilnehmer |
| GPT-5.6 Luna: 100 % ungedreht, 31 % gedreht; Zufallsniveau ist 25 % | LAUT UNTERNEHMEN | [Frey-Preprint](https://arxiv.org/abs/2609.39238) | keine |
| Zusammengefasste Genauigkeit bei 135 Grad beträgt 15,0 % (48/320), unter Zufallsniveau; 23 % bei 180 Grad | LAUT UNTERNEHMEN | [Frey-Preprint](https://arxiv.org/abs/2609.39238) | keine |
| Modelle nutzen einen Bildtrick wie Spiegelabgleich | ANALYSE | [Frey-Preprint](https://arxiv.org/abs/2609.39238) | Interpretation des 135/180-Grad-Musters durch den Autor |
| Qwen2.5-VL von 3B bis 72B: ungedreht 30 % bis 75 %, gedreht 29 %, 31 %, 18 %, 20 % | LAUT UNTERNEHMEN | [Frey-Preprint](https://arxiv.org/abs/2609.39238) | keine |
| Kein Modell mit offenen Gewichten (1B bis 235B) überschreitet gedreht 31 %; die denkende Variante erreicht wie instruct gedreht 19 % | LAUT UNTERNEHMEN | [Frey-Preprint](https://arxiv.org/abs/2609.39238) | keine |
| Sechs Anweisungsstile lassen Qwen2.5-VL-32B bei 13,8 % bis 23,8 %, alle unter Zufallsniveau | LAUT UNTERNEHMEN | [Frey-Preprint](https://arxiv.org/abs/2609.39238) | keine |
| Medianer Abstand zum nächsten Ablenker von 6,8 m auf 31,4 m: Gemini 3.8 Flash von 39 % auf 85 %, GPT-5.6 Luna von 31 % auf 55 % | LAUT UNTERNEHMEN | [Frey-Preprint](https://arxiv.org/abs/2609.39238) | keine |
| Kein offenes Modell verändert sich bei größerem Ablenkerabstand signifikant | LAUT UNTERNEHMEN | [Frey-Preprint](https://arxiv.org/abs/2609.39238) | keine |
| Modellfehler verteilen sich mit 30/37/33 auf nächsten, mittleren und fernsten Ablenker; der Mensch wählte bei 10 von 14 Fehlern den nächsten | LAUT UNTERNEHMEN | [Frey-Preprint](https://arxiv.org/abs/2609.39238) | keine |
| Spitzenmodelle besitzen eine grobe Repräsentation der Anordnung | ANALYSE | [Frey-Preprint](https://arxiv.org/abs/2609.39238) | Schlussfolgerung aus dem Ergebnis zum Ablenkerabstand |
| Preprint eines einzelnen Autors vom 30. September 2026; Autor bei Fraunhofer IAIS; kein Code und keine Daten verlinkt | VERIFIZIERT | [arXiv-Eintrag](https://arxiv.org/abs/2609.39238) | arXiv-Metadaten und E-Mail-Domain des Autors |
| Weitere menschliche Teilnehmer werden evaluiert | LAUT UNTERNEHMEN | [Frey-Preprint](https://arxiv.org/abs/2609.39238) | keine |
