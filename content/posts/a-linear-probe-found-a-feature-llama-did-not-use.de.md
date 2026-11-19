+++
title = "Eine lineare Sonde fand ein Merkmal, das Llama nicht nutzte"
slug = "lineare-sonde-fand-ein-merkmal-das-llama-nicht-nutzte"
description = "Eine lineare Sonde konnte Geburtsjahre aus Llama-2-7B auslesen, doch eine Änderung entlang der gefundenen Richtung veränderte die Antwort kaum. Eine neue Studie führt dies auf Aktivierungsrichtungen mit geringer Varianz zurück und zeigt, wie Regularisierung ein kausal aussagekräftigeres Merkmal finden kann."
tags = ["research", "models"]
date = 2026-11-19T04:03:00+01:00
draft = false
+++

Ein Forscher tippte den Namen einer Person ein, die in den 1930er-Jahren geboren worden war, und übernahm dann ein internes Signal von jemandem, der fünfzig Jahre später zur Welt gekommen war. Die Sonde zeigte an, dass sie wisse, wo das Modell das Jahr speicherte. Das Modell machte weiter, als hätte sich nichts geändert.

*Die Szenen am Anfang und am Ende dieses Artikels sind Illustrationen; die Personen darin sind erfunden.*

Dieser gescheiterte Eingriff steht im Mittelpunkt eines Preprints von Karl Vilhelmsson Emneby, Julian Yocum und Cameron Allen. Ihr Ergebnis zieht eine klare Grenze zwischen Informationen, die sich aus einem neuronalen Netz auslesen lassen, und solchen, die das Netz tatsächlich nutzt. Eine gewöhnliche lineare Sonde konnte Geburtsjahre aus den Aktivierungen von Llama-2-7B vorhersagen. Doch ein Eingriff entlang der von ihr gewählten Richtung bot nicht mehr Kontrolle, als das Modell unverändert zu lassen. Eine regularisierte Sonde gab etwas Vorhersagegenauigkeit auf und fand eine Richtung, die die Ausgabe veränderte.

## Auslesen heißt nicht nutzen

Eine lineare Sonde ist bewusst einfach gehalten. Forscher sammeln die internen Aktivierungen eines Modells, versehen sie mit Zielwerten und passen eine lineare Abbildung zwischen beiden an. Wenn diese Abbildung eine Eigenschaft wie Stimmung, Ort oder Geburtsjahr vorhersagt, lässt sich die Eigenschaft aus dieser Schicht linear dekodieren.

Diese Technik hat Sonden zu einem Standardinstrument der Interpretierbarkeitsforschung gemacht. Ihre Einfachheit scheint zu begrenzen, was sie entdecken können. Eine erfolgreiche lineare Auslesung kann wie ein klarer Einblick in die Berechnungen eines Modells wirken.

Bei diesem Schluss war schon immer Vorsicht geboten. Eine Repräsentation kann ein Signal enthalten, das spätere Schichten ignorieren. Sie kann auch eine korrelierte Größe enthalten, die den vom Forscher vergebenen Zielwert vorhersagt, ohne die ihr zugeschriebene Rolle zu erfüllen. Die neue Arbeit stellt eine engere Frage: Warum kann die genaueste Regressionssonde eine besonders schlechte Richtung für Eingriffe finden, und kann ein bekanntes statistisches Strafmaß helfen?

Die Autoren definieren die Treue eines Eingriffs durch einen Austausch. Dazu nehmen sie eine Aktivierung aus einer Basiseingabe und ersetzen ihre Komponente entlang der vorgeschlagenen Merkmalsrichtung durch die entsprechende Komponente einer Quelleingabe. Wenn die Richtung die behauptete Variable trägt, sollte sich die Modellausgabe auf den Wert zubewegen, der zur Quelle gehört. Der Vorhersagefehler zeigt, ob eine Sonde die Variable auslesen kann. Der Interventionsfehler zeigt, ob eine Änderung dieses ausgelesenen Werts das Modell wie erwartet verändert.

Das sind unterschiedliche Prüfungen.

## Ein verborgener Prozess mit bekannter Antwort

Das erste Experiment verwendet Mess3, einen verborgenen Markow-Prozess mit drei latenten Zuständen. Ein kleiner Transformer mit vier Schichten und einer Breite von 64 lernt, das nächste Symbol des Prozesses vorherzusagen. Weil der Prozess exakt definiert ist, können die Forscher nach jeder Eingabefolge den korrekten Überzeugungszustand sowie die Ausgabe berechnen, die auf einen Eingriff folgen sollte.

Dieser Versuchsaufbau erweitert die Arbeit von Adam Shai und Kollegen. Sie zeigten, dass sich aus dem Residualstrom eines Transformers die Geometrie der Überzeugungszustände verborgener Prozesse rekonstruieren lässt, einschließlich der komplexen Struktur von Mess3. Ihre lineare Regression rekonstruierte diese Geometrie aus Aktivierungen. Die neue Studie fragt, ob die wiedergewonnenen Richtungen auch die Vorhersage des Transformers steuern.

Die gewöhnliche Methode der kleinsten Quadrate funktionierte beim Auslesen gut und beim Steuern schlecht. Der Grund liegt in der Division, die den Kern der Regression bildet. In der Basis, die aus den Hauptkomponenten des Aktivierungsraums besteht, hängt das Gewicht jeder Komponente von ihrer Kovarianz mit der Zielgröße ab, geteilt durch ihre Varianz. Eine Komponente, die nur sehr wenig schwankt, kann daher schon bei geringer Kovarianz ein hohes Gewicht erhalten.

Das Ergebnis mit Mess3 macht diesen Effekt sichtbar. Eine Komponente mit einer Varianz nahe 10 hoch minus 18 trug 91,5 % der quadrierten Gewichte der unregularisierten Sonde. Die Sonde hatte sich auf eine Richtung konzentriert, die kaum variierte. Sie konnte diese Richtung nutzen, um ihren eigenen Anpassungsfehler zu verringern. Doch der Austausch entlang dieser Richtung bewirkte nicht die beabsichtigte Änderung der Transformer-Ausgabe.

Die Ridge-Regression verändert den Divisor, indem sie einen Strafterm addiert. Das dämpft die hohen Gewichte, die die gewöhnliche Methode der kleinsten Quadrate Komponenten mit niedriger Varianz zuweist. Mit steigendem Strafterm verbesserte sich zunächst die Treue des Eingriffs; im Sprachmodellexperiment nahm sie anschließend wieder ab. Die Regularisierung machte nicht einfach jede stark schwankende Richtung zu einem kausalen Merkmal. Sie veränderte, welche Hinweise die Sonde bevorzugte.

## Geburtsjahre im Inneren von Llama

Das zweite Experiment wechselt von einem kleinen System mit exakter Lösung zu Llama-2-7B. Es knüpft an frühere Arbeiten von Benjamin Heinzerling und Kentaro Inui an, die Richtungen fanden, in denen numerische Eigenschaften monoton kodiert sind. Durch ihre Eingriffe konnten sie ein Sprachmodell dazu bringen, frühere oder spätere Geburtsjahre auszugeben.

Emneby und seine Kollegen verwendeten 8.000 Prompts über Menschen, die zwischen 1900 und 1999 geboren wurden. Sie passten Sonden an den Residualstrom der achten Schicht an, jeweils am letzten Token eines Personennamens. Bei jedem Eingriff verschoben sie die Basisaktivierung entlang einer vorgeschlagenen Richtung zur Aktivierung einer Quellperson hin. Anschließend bestimmten sie das erwartete Jahrzehnt anhand der Wahrscheinlichkeiten, die das Modell den zehn möglichen Jahrzehntziffern zuwies.

Die unregularisierte Sonde hatte mit 0,0671 den besten Vorhersageverlust auf den Anpassungsdaten. Ihr Interventionsverlust betrug 13,7 und entsprach damit exakt dem Ergebnis ohne Eingriff. Die Richtung ließ sich auslesen, blieb aber wirkungslos.

Eine Ridge-Sonde mit einem Strafterm von 10.000 hatte einen schlechteren Vorhersageverlust von 0,251, senkte den Interventionsverlust jedoch auf 7,07. Distributed Alignment Search, eine von Atticus Geiger und Kollegen entwickelte Methode, die Repräsentationen direkt aus kausalen Eingriffen lernt, erreichte 6,42. Die Ridge-Richtung lag 26,3 Grad von der Richtung entfernt, die die anhand von Eingriffen trainierte Methode gefunden hatte. Die gewöhnliche Sonde lag 84,7 Grad daneben.

Die regularisierte Richtung war nicht einfach die Achse mit der größten Schwankung im Aktivierungsraum. Ihre Varianz betrug 3,83, während die erste Hauptkomponente eine Varianz von 25.570 hatte. Ridge ignorierte diese dominante Komponente weitgehend. Der nützliche Bereich lag zwischen den schwachen Korrelationen, die gewöhnliche Regression verstärkte, und der größten Bewegung in der Schicht.

## Eine Prüfung, keine Garantie

Die Arbeit liefert einen Mechanismus für eine bestimmte Art des Sondenversagens und einen praktischen Ansatz dagegen. Wenn ein Merkmal gesucht wird, das das Modell aktiv nutzt, können Forscher Sonden mit unterschiedlichen Straftermen anpassen und anhand separat zurückgehaltener Eingriffe zwischen ihnen auswählen. Ein hoher Dekodierungswert allein beantwortet nur die Frage, ob die Information ausgelesen werden kann.

Die Aussagekraft der Ergebnisse ist klar begrenzt. Die Theorie behandelt Regression mit kontinuierlichen Zielgrößen, während viele Sonden logistische Klassifikatoren verwenden. Das Ergebnis zum Sprachmodell stammt aus einer einzigen Schicht eines einzigen Modells und betrifft eine einzige numerische Eigenschaft. Selbst die beste Ridge-Sonde ließ einen erheblichen Interventionsfehler übrig. Die Mathematik erklärt, wie die gewöhnliche Methode der kleinsten Quadrate Richtungen mit geringen Schwankungen verstärken kann. Sie beweist nicht, dass Ridge-Regression eine kausale Richtung findet.

Auch der Vergleich mit Distributed Alignment Search weist eine wichtige Asymmetrie auf. Diese Methode lernt aus den Ergebnissen von Eingriffen, während die Ridge-Sonden weiterhin anhand der Dekodierbarkeit lernen. Die Interventionsdaten dienen erst nach der Anpassung der Sonden dazu, den Strafterm auszuwählen. Die Nähe ihrer Richtungen zeigt, dass Regularisierung eine prädiktive Sonde in diesen Experimenten zu einer kausal nützlichen Richtung führen kann. Dadurch werden die beiden Lernziele jedoch nicht identisch.

Am Arbeitsplatz versuchte der Forscher den Austausch erneut. Diesmal war sich die Sonde beim ausgelesenen Geburtsjahr weniger sicher. Das vom Modell ausgegebene Jahrzehnt verschob sich.

## Quellen

- Emneby, K. V., Yocum, J., & Allen, C. (2026). *Pretty Linear Liars: Unregularized Probes Favor Intervention-Unfaithful Features*. https://arxiv.org/abs/2611.20371
- Geiger, A., Wu, Z., Potts, C., Icard, T., & Goodman, N. (2024). *Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations*. https://proceedings.mlr.press/v236/geiger24a.html
- Heinzerling, B., & Inui, K. (2024). *Monotonic Representation of Numeric Attributes in Language Models*. https://aclanthology.org/2024.acl-short.18/
- Shai, A. S., Marzen, S. E., Teixeira, L., Gietelink Oldenziel, A., & Riechers, P. M. (2024). *Transformers Represent Belief State Geometry in Their Residual Stream*. https://arxiv.org/abs/2405.15943
