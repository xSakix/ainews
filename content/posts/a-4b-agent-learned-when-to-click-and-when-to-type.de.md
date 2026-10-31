+++
title = "Ein 4B-Agent lernt, wann er klickt und wann er tippt"
slug = "ein-4b-agent-lernt-wann-er-klickt-und-wann-er-tippt"
description = "Microsofts offenes Modell Mage-VL-Cowork bedient Bildschirm und Terminal. Sein Trainingsverfahren zeigt, warum es mehr bringen kann, die Werkzeuge des Lehrermodells zu beschränken und kurze Erfolgswege zu belohnen, als eine weitere Schnittstelle hinzuzufügen."
tags = ["models", "agents", "research"]
date = 2026-10-31T04:03:07+01:00
draft = false
+++

Eine Analystin soll in einer Tabelle zwei Kopfbereiche zusammenführen, ein Diagramm einfügen und die Datei im Format `.xlsx` erhalten. Die Analystin ist erfunden, die Entscheidung nicht: Soll sie sich Zelle für Zelle durch die Menüs arbeiten oder eine Shell öffnen und die Arbeitsmappe mit Python bearbeiten? Ein fähiger Computeragent sollte schon vor dem ersten Klick wissen, welcher Weg zur Aufgabe passt.

## Eine Strategie, zwei Handlungsmöglichkeiten

Microsofts Mage-Team hat Mage-VL-Cowork veröffentlicht. Das Modell mit 4,74 Milliarden Parametern steht unter der Lizenz Apache-2.0. Es kann einen grafischen Desktop bedienen oder in einer Bash- und Python-Umgebung arbeiten, die zwischen Befehlen aktiv bleibt. Die Entscheidung überlässt es keinem externen System. In jeder Runde bestimmt dasselbe Bild-Sprach-Modell, ob eine der elf Bildschirmaktionen oder ein Terminalbefehl zur Aufgabe passt.

Der Unterschied klingt gering. Er bestimmt aber, wie der Agent sein Kontextfenster nutzt und wie unmittelbar er seine Arbeit überprüfen kann. Ein Bildschirmfoto kann Tausende Token beanspruchen. Eine lange Folge von Mausbewegungen ahmt mitunter nur ungenau nach, was eine Softwarebibliothek präzise erledigt. Umgekehrt sieht das Terminal weder eine ungespeicherte Zeichenfläche noch ein Dialogfenster oder den vorübergehenden Zustand einer Anwendung. Das Modell braucht beide Kanäle und muss zwischen ihnen wählen können.

Das Mage-Team meldet für OSWorld-Verified eine Erfolgsquote von 66,04 Prozent, gemittelt über zwei Durchläufe mit jeweils 361 Aufgaben und höchstens 50 Schritten. Die einzelnen Durchläufe ergaben 65,33 und 66,75 Prozent. Menschen erreichen in der Vergleichstabelle des Teams 72,4 Prozent. GPT-5.4-mini kommt bei denselben Aufgaben und derselben Schrittgrenze in einem Durchlauf auf 69,6 Prozent. Unter den verglichenen Modellen mit offenen Gewichten liegt ScaleCUA-Qwen3.5-9B mit 68,7 Prozent vorn. Für Mage-VL-Cowork beansprucht das Team also nicht die Gesamtführung, sondern das beste Ergebnis unter den Modellen der 4B-Klasse.

Die Messungen stammen von Microsoft und wurden nicht unabhängig reproduziert. Das Repository enthält die Testaufgaben, den Code des Agenten und die Startskripte. Damit lässt sich die Aussage besser überprüfen als anhand einer einzelnen Zahl auf der Modellkarte.

## Warum das Lehrermodell Werkzeuge abgeben musste

Die Arbeit am Training begann schon bei den Beispielen, von denen das Modell lernen sollte. Selbst ein leistungsfähiges Lehrermodell mit Zugriff auf alle Schnittstellen lieferte nicht automatisch eindeutige Vorlagen. Mehrere Wege überschnitten sich und gaben dem Schüler unterschiedliche Vorgehensweisen vor: Derselbe Schritt ließ sich über den Barrierefreiheitsbaum, durch direkte Desktopautomatisierung oder mit einem Klick nach Sicht erledigen.

Das Team verglich zwei Arbeitsumgebungen für das Lehrermodell anhand von 672 eigens für den Test zurückgehaltenen Aufgaben, die mehrere Anwendungen erforderten. In der gewählten Umgebung erhielt GPT-5.4 grafische Werkzeuge und Programmierwerkzeuge. Das Team entfernte Hilfsmittel mit überlappenden Funktionen, darunter `xdotool` und Auszüge aus den Barrierefreiheitsdaten, und installierte Bibliotheken für Tabellen, Dokumente, Präsentationen, PDFs und Bilder vor. So löste das Lehrermodell 92,0 Prozent der Aufgaben in durchschnittlich 25 Schritten. Die Umgebung mit zusätzlichen Barrierefreiheitsdaten kam auf 89,6 Prozent in 35,33 Schritten.

Nach der Destillation wurde der Abstand größer. Ein 4B-Schülermodell, das aus Beispielen der reduzierten Umgebung gelernt hatte, erreichte 37,6 Prozent. Beim Schüler, dessen Beispiele aus der Umgebung mit mehr Werkzeugen stammten, waren es 25,1 Prozent. Die mittlere Schrittzahl sank von 39,40 auf 30,91. Beide Ergebnisse stammen vom selben Forschungsteam. Der Vergleich zeigt dennoch ein konkretes Problem: Ein Spitzenmodell kann redundante Wahlmöglichkeiten mit zusätzlichen Schritten auffangen. Ein kleines Schülermodell übernimmt die Verwirrung.

Auch bei der Datenerzeugung setzte das Team auf wiederverwendbare Strukturen. Mage-CUA-Forge erzeugte 293.806 Aufgaben für 6.915 elementare Fertigkeiten und behielt 318.837 hybride Handlungsabläufe. Statt einen Agenten jede Umgebung neu aufbauen zu lassen, erstellte das System für jede Fertigkeit einmalig wiederverwendbare Abläufe und Routinen zur Vorbereitung der jeweiligen Anwendung. Bei gleichem Generierungsmodell sank die Zahl der Token pro Aufgabe laut Team von 1,276 Millionen auf 85.000. Die laufenden Kosten pro Aufgabe fielen von 0,906 auf 0,158 Dollar.

Hier entstehen synthetische Trainingsdaten im industriellen Maßstab. Ihr Wert hängt davon ab, ob die Vorbereitungsroutinen funktionieren und die Aufgabenbeschreibungen und Bewertungskriterien stimmen. Laut Repository erstrecken sich 38,24 Prozent der erzeugten Aufgaben über mehrere Anwendungen. Rund 68 Prozent der Aktionen in den Abläufen entfallen auf die grafische Oberfläche und 32 Prozent auf das Terminal.

## Erst spezialisieren, dann zusammenführen

Mage-VL-Cowork baut auf einem Zwischenstand von Mage-VL auf, nicht auf einem bereits für grafische Bedienung oder Programmierung spezialisierten Modell. Das Training erfolgt in fünf Stufen: visuelle Verweise auf dem Bildschirm verorten, mehrstufige grafische Aufgaben lösen, programmieren und im Terminal arbeiten, beide Wege durch überwachtes Feintuning verbinden und schließlich online mit Belohnungen weiterlernen.

Die Reihenfolge ist entscheidend. Das Modell lernt erst, beide Kanäle zu beherrschen, und danach, zwischen ihnen zu wählen. Nach der gemeinsamen überwachten Trainingsstufe erreichte es bei OSWorld-Verified 55,84 Prozent. Online-Verstärkungslernen steigerte den Wert auf 66,04 Prozent. Gleichzeitig sank die mittlere Zahl der Modellaufrufe von 21,57 auf 18,77 und die Zahl der Ausgabetoken pro Aufgabe von 7.374 auf 5.499.

Die Belohnung brachte den Agenten nicht einfach dazu, es länger zu versuchen. Sie verkürzte die erfolgreichen Wege. Das Team vergab die Belohnungen anhand überprüfbarer Ergebnisse bei 1.988 Aufgaben; pro Aktualisierung standen 768 Plätze für Episoden bereit. Das Verstärkungslernen beanspruchte nominell mehr Rechenarbeit als jede andere einzelne Stufe, obwohl es nach Rechnung des Teams nur 3,5 Prozent des Trainingsplans ausmachte.

Bei langen Desktopsitzungen entsteht ein weiteres Problem: Bildschirmfotos können das Kontextfenster füllen, bevor die Arbeit beendet ist. Mage-VL-Cowork behält die drei jüngsten Bildschirmfotos und vier vollständige Antworten des Assistenten. Ältere Runden fasst es in je einer Zeile zusammen, die die Aktion beschreibt. So bleiben die jüngsten sichtbaren Veränderungen und ein komprimiertes Protokoll früherer Arbeit erhalten.

Der aktive Kontext umfasst 32.768 Token, obwohl die Architektur mehr unterstützt. Bei jedem Schritt gibt das Modell seine Überlegungen, eine kurze Zusammenfassung der Aktion und einen Werkzeugaufruf aus. Dadurch können frühere Überlegungen entfallen, ohne dass die Aufzeichnung der Aktionen verloren geht.

## Wo der Benchmark endet

OSWorld wurde entwickelt, um Agenten in echten Anwendungen und bei Aufgaben im Betriebssystem zu testen, statt auf isolierten Websites. Mit dem überprüften Aufgabensatz arbeiten die automatischen Bewerter zuverlässiger. Ein Benchmark gibt aber weiterhin die Umgebung, die installierte Software und die Erfolgskontrollen vor. Er zeigt nicht, was passiert, wenn ein Agent auf einen persönlichen Passwortspeicher, ein unberechenbares Netzwerk oder ein Dokument mit feindseligen Anweisungen trifft.

Microsofts eigene Einsatzempfehlungen spiegeln diese Lücke wider. Das Modell kann beliebige Shellbefehle ausführen und einen Desktop bedienen. Deshalb empfiehlt das Team virtuelle Maschinen oder Container, die sich nach Gebrauch verwerfen lassen, keine persönlichen Zugangsdaten, eingeschränkte ausgehende Netzwerkverbindungen und eine menschliche Bestätigung vor unumkehrbaren Aktionen. Das Modell wurde für die Forschung veröffentlicht, nicht für den Produktivbetrieb.

Die Größe von 4B bedeutet auch nicht, dass das Gesamtsystem genügsam ist. Für das Sprachmodelltraining über alle fünf Stufen meldet das Team nominell 7,79 ZettaFLOPs an Rechenarbeit. Beim Verstärkungslernen kamen 32 NVIDIA-B200-GPUs und 1.120 CPU-Sandboxplätze zum Einsatz. Um das BF16-Modell bereitzustellen, sind allein für die beiden Gewichtsdateien rund 9,48 GB nötig. Der Speicherbedarf der Laufzeitumgebung und des Desktops kommt hinzu.

Am überzeugendsten ist die Veröffentlichung als Beitrag zur Trainingsmethode. Die Entwickler schränkten die Auswahl des Lehrermodells ein, bauten Aufgaben auf wiederverwendbaren Fertigkeiten auf und trainierten beide Handlungskanäle getrennt. Erst danach belohnten sie das Modell dafür, überprüfbare Arbeit mit weniger Aufrufen abzuschließen.

Zurück zur fiktiven Analystin. Das Diagramm gehört weiterhin in die grafische Anwendung, wo sich sein Aussehen beurteilen lässt. Für das Zusammenführen von Zellen eignet sich Python, weil sich die Dateistruktur dort präzise ändern und prüfen lässt. Die entscheidende Handlung findet statt, bevor sich eines der Werkzeuge öffnet: Das Modell wählt einen Weg. Diese Wahl gehört nun zu einer Strategie, die jeder untersuchen kann.

## Quellen

- Microsoft Mage Team. (2026). *Mage: A Lightweight, Research-Friendly Multimodal Model Family*. https://github.com/microsoft/Mage
- Microsoft Mage Team. (2026). *Mage-VL-Cowork: A Full Training Recipe to Learn Hybrid Computer Use from Evolved Harnesses*. https://github.com/microsoft/Mage/blob/main/assets/mage_vl_cowork_tech_report.pdf
- Microsoft. (2026). *Mage-VL-Cowork model card*. https://huggingface.co/microsoft/Mage-VL-Cowork
- Xie, T., et al. (2024). *OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments*. https://arxiv.org/abs/2404.07972
- Yang, S., et al. (2026). *Mage-VL: An Efficient Codec-Native Streaming Multimodal Foundation Model*. https://arxiv.org/abs/2607.24904
