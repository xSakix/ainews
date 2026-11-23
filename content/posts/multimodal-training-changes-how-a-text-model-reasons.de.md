+++
title = "Multimodales Training verändert das Schlussfolgern von Textmodellen"
slug = "multimodales-training-veraendert-text-schlussfolgern"
description = "Forschende fanden eine Richtung im verborgenen Zustandsraum, die multimodale Modelle bei einigen rein textbasierten Raumaufgaben nutzen. Ihr Entfernen beeinträchtigte die Navigation, ließ formale Logik aber oft unberührt – und zeigt, warum eine auslesbare Repräsentation nicht unbedingt vom Modell genutzt wird."
tags = ["research", "models"]
date = 2026-11-16T04:05:26+01:00
draft = false
+++

Leila steht an einer weißen Tafel in einem leeren Seminarraum und schreibt eine Route von Hand auf: nach Norden blicken, rechts abbiegen, gehen, erneut abbiegen. Sie schickt ausschließlich diese Wörter an ein Modell. Es liefert eine Antwort. Dann entfernt sie eine schmale Richtung aus dessen internem Zustand und wiederholt den Test. Die Route, die leicht gewirkt hatte, zerfällt.

*Die Szenen am Anfang und am Ende dieses Artikels sind Illustrationen; die Personen darin sind erfunden.*

Ein Team der Nanyang Technological University und der Singapore Management University berichtet über eine Variante dieses Eingriffs über zehn Konfigurationen aus sechs multimodalen Modellfamilien hinweg. Ihr am 11. November veröffentlichtes Preprint (Vorabveröffentlichung) identifiziert eine Richtung im Raum der verborgenen Zustände, die visuelle und textuelle Repräsentationen trennt. Als die Forschenden die Projektion des Modells auf diese Richtung während der reinen Text-Inferenz entfernten, sank die räumliche Leistung häufig, während formale Logik erhalten blieb. Das Ergebnis liefert Belege dafür, welche Repräsentation ein Modell nutzt, und behauptet nicht, dass es vor seinem inneren Auge ein Bild sehe.

## Eine Richtung, die eine Route trägt

Qi Zhang, Bohan Wang, Qianru Sun und Hanwang Zhang nennen den Effekt „emergentes bildgeprägtes Denken“. Das vorsichtige Wort ist geprägt. Ihre Experimente legen kein inneres Bild offen. Sie zeigen, dass visuell-sprachliches Training eine Repräsentation einführte oder verstärkte, die einige Modelle später heranzogen, obwohl die Eingabe gar kein Bild enthielt.

Die Forschenden begannen mit einer Differenz der Mittelwerte. In einem Repräsentationsraum, in dem sich visuelle und textuelle Signale vergleichen ließen, berechneten sie den mittleren Zustand jeder Modalität und bildeten die normierte Richtung dazwischen. Der Aufbau variierte je nach Architektur. Chameleon teilt sich ein Vokabular für Bild- und Text-Token, während Qwen3-VL kontinuierliche visuelle Merkmale in ein Sprach-Grundmodell einspeist. BAGEL und Janus-Pro besitzen getrennte Pfade für visuelles Verstehen und Generierung, sodass jeder Pfad eine eigene Richtung erhielt.

Zur Inferenzzeit zog das Team die Projektion jedes verborgenen Zustands auf diese Richtung ab. Der Eingriff wurde nach ausgewählten Decoder-Blöcken angewendet. Alle Evaluierungs-Prompts bestanden ausschließlich aus Text. Aus der Eingabe wurde nichts Visuelles entfernt, weil dort kein Bild und kein visuelles Token vorhanden war.

Das deutlichste Ergebnis lieferte Chameleon-7B. Das Entfernen der Richtung in einer einzelnen Schicht senkte die Genauigkeit bei der Navigationsaufgabe von BIG-Bench Hard um 27,6 Prozentpunkte. Die Genauigkeit bei booleschen Ausdrücken stieg um 5,6 Punkte, was einen Abstand von 33,2 Punkten zwischen den beiden Veränderungen ergab. Die Richtung hob sich zudem von normgleichen Zufallsrichtungen ab, und der Schaden konzentrierte sich auf eine kleine Gruppe von Schichten, statt sich gleichmäßig im Netz zu verteilen.

Diese Paarung ist aufschlussreich, weil BIG-Bench Hard als Sammlung von 23 Aufgaben entworfen wurde, die Sprachmodellen schwerfielen. Sowohl Navigation als auch das Auswerten boolescher Ausdrücke können mehrere Schritte verlangen, legen jedoch unterschiedliche Arbeitsrepräsentationen nahe. Eine in Worten beschriebene Route lässt sich als Abfolge von Positionen und Drehungen anlegen. Ein boolescher Ausdruck lässt sich nach formalen Regeln vereinfachen.

## Von der Korrelation zum Eingriff

Interpretierbarkeitsforschung beginnt oft mit einer Sonde (Probe): Man trainiert einen einfachen Klassifikator, um eine Eigenschaft aus verborgenen Zuständen auszulesen. Yonatan Belinkovs Überblick über Sondierungsmethoden erklärt sowohl deren Reiz als auch ihre zentrale Schwäche. Wenn ein Klassifikator eine Eigenschaft auslesen kann, beweist das noch nicht, dass das ursprüngliche Modell sich darauf stützt.

Die neue Arbeit stellt diese Unterscheidung in den Mittelpunkt des Experiments. Sie fragt, ob das Entfernen einer Kandidatenrepräsentation gezielt jenes Verhalten verändert, das davon abhängen sollte. Dieser Ansatz schließt an frühere Arbeiten zu Othello-GPT an, in denen Kenneth Li und Kollegen eine interne Brettrepräsentation fanden und anschließend in sie eingriffen, um Vorhersagen legaler Züge zu steuern. In beiden Fällen ist die entscheidende Frage anspruchsvoller als das bloße Vorhandensein von Information: Verändert ein Eingriff in die Repräsentation die Antwort auf die erwartete Weise?

Über neun Konfigurationen mit einer positiven Vision-Language-Achse hinweg fanden die Autoren einen selektiven kausalen Effekt. Die Lage hing von der Architektur ab. Er trat früh in Chameleon und Qwen3-VL auf, später in Liquid sowie in späteren Schichten des Generierungspfads von BAGEL und Janus-Pro. Zu den externen Vergleichstests (Benchmarks) zählten bAbI, SpartQA und StepGame. Die Effekte ballten sich tendenziell bei räumlichen Aufgaben, während Allgemeinwissen und Mathematik sich weniger veränderten; die Studie berichtet jedoch über eine wichtige Ausnahme: Der Haupteingriff bei BAGEL beschädigte auch GSM8K und LogiQA stark, sodass diese Ergebnisse keine saubere Aussage zum räumlichen Transfer stützen.

Der Vergleich mit reinen Text-Grundmodellen fügt eine weitere Einschränkung hinzu. Die Chameleon-Richtung beeinflusste LLaMA-7B kaum, was die Sicht stützt, dass multimodales Training ein neues nutzbares Gerüst einführte. In der Qwen-Familie war ein verwandtes Gerüst bereits im Textmodell vorhanden. Multimodales Training schien es zu verstärken und den Eingriff selektiver zu machen. Die Studie schlägt daher keinen universellen Schalter für visuelles Denken über alle Modelle hinweg vor.

## Was die Generierung hinzufügt

BAGEL und Janus-Pro erlaubten den Forschenden, zwei Pfade innerhalb vereinheitlichter Systeme zu vergleichen. Diese Modelle nutzen ein gemeinsames Sprach-Grundmodell, wickeln visuelles Verstehen und Bildgenerierung jedoch über unterschiedliche Pfade ab. Der Generierungspfad lieferte einen kompakten, eindimensionalen kausalen Hebel: Das Entfernen seiner Richtung störte gezielt das räumliche Schlussfolgern. Auch der Verständnispfad enthielt räumliche Information, die eine Sonde dekodieren konnte, doch das Entfernen seiner entsprechenden Richtung erzeugte nicht denselben selektiven Effekt. Größere Eingriffe in ganze Unterräume stellten ihn ebenfalls nicht her.

Das ist die nützlichste Warnung der Studie. Eine Repräsentation kann leicht auslesbar sein und dennoch nicht der Mechanismus sein, der eine Antwort antreibt. Die Autoren beschreiben drei Prüfungen, um den Unterschied aufzuklären: wie konzentriert das Signal ist, ob die auslesbare Richtung mit der kausal wirksamen übereinstimmt und ob das Experiment den richtigen semantischen Kontrast und die richtige Schicht gewählt hat.

Die letzte Prüfung rettete ein scheinbares Scheitern bei Chameleon-30B. Eine Achse, die aus der Embedding-Tabelle oder aus synthetischen Token-Folgen geschätzt wurde, wirkte nicht kausal. Als das Team die Achse neu aufbaute, indem es echte Bilder durch den eigenen Tokenizer und den vollständigen multimodalen Pfad des Modells schickte, drehte sich die Richtung und wurde in mittleren und hinteren Blöcken stark kausal. In einem mittleren Block fiel die Navigation um 33,6 Punkte, während sich die Genauigkeit bei booleschen Ausdrücken um weniger als einen Punkt veränderte. Der Träger hatte sich verschoben, und die erste Messung hatte an der falschen Stelle gesucht.

## Die Grenzen der Aussage

Die Studie ist für eine mechanistische Intervention breit angelegt, doch ihre Autoren benennen mehrere Grenzen. Sie prüft lineare und niedrigrangige Entfernungen und kann daher nichtlineare oder verteilte Mechanismen übersehen. Ihre Aufgabenbatterie erfasst ausgewählte Formen räumlichen Schlussfolgerns, nicht jede Art von Kognition. Chameleon-7B lag bei mentaler Rotation, Papierfalten und Perspektivübernahme auf oder unter Zufallsniveau, sodass die Belege aus diesen Aufgaben von Qwen3-VL-Modellen stammen, die von vornherein leistungsfähig genug waren.

Der Träger war zudem nicht ausschließlich räumlich. Lange Folgen nicht-räumlicher Zustandsaktualisierungen überschnitten sich teilweise mit ihm. Ein Test mit Qwen3-VL-8B bestand die Prüfung auf Richtungsspezifität, beeinträchtigte jedoch einige Kontrollaufgaben mit geringem Raumbezug und kehrte damit den erwarteten Gradienten über die Aufgaben um. Öffentliche Unsicherheit über die Trainingsdaten von Qwen begrenzt zudem Aussagen darüber, wann genau sein Gerüst entstanden ist.

Frühere Evaluierungen hatten bereits gezeigt, dass Vision-Language-Modelle beim räumlichen Schlussfolgern anfällig bleiben. Jiayu Wang und Kollegen stellten fest, dass das Hinzufügen eines Bildes multimodale Modelle hinter reine Sprachmodelle zurückwerfen konnte, besonders wenn textuelle Hinweise eine Abkürzung boten. Die neue Arbeit widerspricht diesem Befund nicht. Sie verengt die Frage von der Gesamtleistung auf interne Abhängigkeit: Ein Modell kann bei einer Aufgabe schlecht abschneiden und dennoch eine durch visuelles Training geprägte Repräsentation verwenden – oder eine Repräsentation enthalten, die es kausal nicht nutzt.

Der Eingriff der Autoren belegt Notwendigkeit unter den getesteten Bedingungen. Er zeigt nicht, wie die Richtung geschrieben wird, welche Schaltkreise sie lesen oder ob das Modell so etwas wie eine mentale Szene konstruiert. Diese Fragen gehen über eine eindimensionale Subtraktion hinaus.

An der Tafel stellt Leila die entfernte Projektion wieder her. Derselbe Text läuft durch dasselbe Modell, und die Route hält wieder. Auf der Wand erscheint keine Karte. Die einzige sichtbare Veränderung ist die Antwort.

## Quellen

- Belinkov, Y. (2022). *Probing Classifiers: Promises, Shortcomings, and Advances*. https://aclanthology.org/2022.cl-1.7/
- Li, K., Hopkins, A. K., Bau, D., Viégas, F., Pfister, H., & Wattenberg, M. (2023). *Emergent World Representations: Exploring a Sequence Model Trained on a Synthetic Task*. https://openreview.net/forum?id=DeG07_TcZvT
- Suzgun, M., Scales, N., Schärli, N., Gehrmann, S., Tay, Y., Chung, H. W., Chowdhery, A., Le, Q., Chi, E., Zhou, D., & Wei, J. (2023). *Challenging BIG-Bench Tasks and Whether Chain-of-Thought Can Solve Them*. https://aclanthology.org/2023.findings-acl.824/
- Wang, J., Ming, Y., Shi, Z., Vineet, V., Wang, X., Li, Y., & Joshi, N. (2024). *Is A Picture Worth A Thousand Words? Delving Into Spatial Reasoning for Vision Language Models*. https://proceedings.neurips.cc/paper_files/paper/2024/hash/89cc5e613d34f90de90c21e996e60b30-Abstract-Conference.html
- Zhang, Q., Wang, B., Sun, Q., & Zhang, H. (2026). *Emergent Vision-Shaped Thinking in Text-Only Reasoning through Multimodal Training*. https://arxiv.org/abs/2611.14942
