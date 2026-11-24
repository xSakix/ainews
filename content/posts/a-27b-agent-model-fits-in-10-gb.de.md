+++
title = "Agentenmodell mit 27 Milliarden Parametern passt in 10 GB"
slug = "agentenmodell-mit-27-milliarden-parametern-passt-in-10-gb"
description = "Nari Labs komprimierte Qwen3.8-27B von 53,8 GB auf 10,12 GB und erreichte in mehreren langen Agenten-Benchmarks das Niveau der BF16-Ausgangsversion. Das Ergebnis hängt von agentenerzeugten Kalibrierungsdaten und einem spezialisierten Inferenz-Fork ab, was einschränkt, wo die kleineren Dateien laufen können."
tags = ["models", "agents", "research", "hardware"]
date = 2026-11-24T04:21:00+01:00
draft = false
+++

Der Download war auf einer Workstation mit 16 Gigabyte Grafikspeicher abgeschlossen. Ein Modell mit 27 Milliarden Parametern, das normalerweise 53,8 Gigabyte benötigte, lag in einer einzigen 10,12 Gigabyte großen Datei vor. Der Entwickler startete einen Programmieragenten und beobachtete, wie dieser Werkzeuge aufrief, die Ergebnisse las und weiterarbeitete, statt auf halbem Weg abzubrechen.

*Die Szenen am Anfang und am Ende dieses Artikels sind Illustrationen; die Personen darin sind erfunden.*

Nari Labs veröffentlichte am 20. November drei komprimierte Versionen von Alibabas Qwen3.8-27B. Die 3-Bit- und die 2,5-Bit-Datei hielten in den Tests des Labors bei langen Programmier- und Terminalaufgaben mit dem ursprünglichen BF16-Modell Schritt. Die 2-Bit-Datei tat es nicht. Die Veröffentlichung verbindet eine praktische mit einer methodischen Behauptung: Ein Modell könne fast vier Fünftel seines Gewichtsspeichers verlieren, ohne das für Agenten nötige Verhalten einzubüßen – vorausgesetzt, das Komprimierungsverfahren lernt aus Agentenarbeit statt aus gewöhnlichem Text.

## Der falsche Text für die Aufgabe

Bei der Quantisierung werden die hochpräzisen Zahlen in den Gewichten eines Modells durch kleinere Darstellungen ersetzt. Weniger Bit senken Speicherbedarf und Bandbreite, wodurch aus einem Modell, das einen Server braucht, eines werden kann, das auf eine Workstation passt. Der Preis ist eine Annäherung. Jedes komprimierte Gewicht weicht vom Original ab, und diese Fehler können sich aufsummieren, während das Modell eine lange Antwort erzeugt oder viele Schritte durchläuft.

Die meisten Kalibrierungsdatensätze bestehen aus kurzen Textpassagen aus dem Web. Ein Quantisierer nutzt diese Passagen, um zu lernen, welche Fehler ins Gewicht fallen und wie sich eine begrenzte Menge numerischer Werte verteilen lässt. Doyeob Kim, der alleinige Autor des NariQ-Berichts, argumentiert, diese Daten bildeten die Arbeit eines Programmieragenten nicht ab. Ein Agent arbeite mitunter über mehr als 100.000 Token hinweg, wechsle zwischen Schlussfolgern und Werkzeugaufrufen ab und reagiere über viele Durchgänge auf Terminalausgaben.

Dieses Missverhältnis zeigt sich in früheren Ergebnissen. Laut Kims Arbeit erreichen ältere Quantisierungen von Qwen3.8-27B mit drei Bit oder weniger bei den kurzen Mathematikaufgaben in AIME das Niveau von BF16, lösen aber höchstens 72 Prozent so viele DeepSWE-Aufgaben. Ein Modell, das Fakten abruft und isolierte Berechnungen erledigt, kann während eines langen Austauschs mit einem Software-Repository dennoch abdriften.

NariQ tauscht das Kalibrierungsmaterial aus. Es zeichnet Token auf, die das vollständige BF16-Modell während Agentensitzungen erzeugt hat, und steuert mit diesen Ablaufspuren die Auswahl der komprimierten Gewichte. Das Modell sieht damit genau jene Art von Sequenzen, die es später durchhalten muss: Pläne, Werkzeugaufrufe, Beobachtungen und Korrekturen.

## Trellis-Strukturen und Ablaufspuren

Der numerische Unterbau stützt sich auf QTIP, ein 2024 von James Tseng und Kollegen vorgestelltes Verfahren. QTIP kombiniert eine Trellis-kodierte Quantisierung mit einer Inkohärenz-Transformation, um Gewichtsgruppen kompakten Codewörtern zuzuordnen. Das Trellis sucht unter möglichen Sequenzen, statt jedes Gewicht einzeln zu runden.

NariQ verbindet dieses Verfahren mit einer Kalibrierung anhand der Zielaktivität. Der Unterschied zählt, weil ein Quantisierer die durchschnittliche Wahrscheinlichkeit des nächsten Tokens bewahren und gleichzeitig eine kleine Gruppe von Entscheidungen beschädigen kann, die darüber bestimmen, ob ein Agent sich von einem fehlgeschlagenen Befehl erholt. Lange Aufgaben legen genau diese Entscheidungen wiederholt offen.

Die veröffentlichten Dateien umfassen drei, 2,5 und zwei Bit pro Gewicht. Sie belassen den Vision-Tower und den Key-Value-Cache von Qwen3.8-27B in BF16, sodass die genannte Bitbreite die Sprachmodellgewichte beschreibt und nicht jedes Byte, das bei der Inferenz anfällt. Das Basismodell ist ein dichtes Vision-Language-Modell mit 64 Schichten und einer nativen Kontextlänge von 262.144 Token. Es unterstützt eine einstellbare Reasoning-Stufe und behält den Reasoning-Inhalt standardmäßig über mehrere Gesprächsrunden bei.

Nari Labs evaluierte die komprimierten Dateien neben dem 53,8 Gigabyte großen BF16-Checkpoint. Auf DeepSWE v1.1, das 113 dreimal ausgeführte Aufgaben umfasst, erzielte BF16 einen pass@1-Wert von 39,8. Die 3-Bit-Datei kam auf 41,0 und die 2,5-Bit-Datei auf 41,9. Terminal-Bench 2.1 ergab 62,6 für BF16, 63,8 für drei Bit und 60,2 für 2,5 Bit.

Das Muster setzte sich bei den Mathematik-Vergleichstests (Benchmarks) AIME 2025 und 2026 fort. BF16 erreichte 97,7, die 3-Bit-Version 98,3 und die 2,5-Bit-Version 96,5. Bei RealWorldQA, einem Vision-Benchmark, lagen BF16 und die 3-Bit-Version gleichauf bei 82,4. Kleine Abweichungen dieser Größenordnung beweisen nicht, dass die Komprimierung das Modell verbessert; wiederholtes Sampling kann einen Agenten-Benchmark verschieben. Sie stützen jedoch den engeren Schluss, dass die beiden größeren NariQ-Dateien in diesen Tests nicht messbar zurückfielen.

## Die Grenze bei zwei Bit

Die kleinste Datei zeigt, wo der Anspruch endet. Bei zwei Bit pro Gewicht fiel DeepSWE auf 28,6, Terminal-Bench auf 52,4 und AIME auf 86,0 zurück. Die Komprimierung überschritt eine Schwelle, ab der die Kalibrierung das Verhalten des Ausgangsmodells nicht mehr wiederherstellen konnte.

Zudem stammt der Benchmark-Satz vom Entwickler selbst. Nari Labs wählte das Modell, die Kalibrierungsspuren, die Implementierung und die Evaluierungseinstellungen. Der Bericht hat einen einzigen Autor und hat noch kein Peer-Review durchlaufen. Unabhängige Läufe mit anderen Agenten, Repositories und anderer Hardware würden erst zeigen, ob der Gleichstand über die veröffentlichte Tabelle hinaus trägt.

Zwischen einer kleinen Datei und einem leicht zugänglichen Modell liegt noch eine weitere Grenze. NariQ setzt den firmeneigenen Fork von llama.cpp voraus, da das Gewichtsformat und die Kernel nicht im Standardprojekt enthalten sind. Standard-llama.cpp, Ollama und LM Studio können die Dateien nicht laden. Der Fork ist auf Nvidias SM120-Architektur abgestimmt. Nari Labs erklärt, er laufe auf Ampere-, Ada- und Hopper-Karten langsamer, unterstütze weder AMD- noch Intel-GPUs und bleibe auf Apple Metal langsam.

Diese Einschränkung verändert die Bedeutung von „lokal“. Zehn Gigabyte bringen die Gewichte in das Speicherbudget vieler Grafikkarten für Endkunden, doch der Softwarepfad bedient viele dieser Karten bislang nicht gut. Die Modellkarte des unkomprimierten Qwen nennt dagegen etablierte Serving-Frameworks wie Transformers, vLLM und SGLang. Die NariQ-Dateien erkaufen ihre Größe durch den Verzicht auf diese breite Kompatibilität.

## Was die Datei tatsächlich misst

Die Arbeit legt eine andere Bewertung von Modellen mit geringer Bitbreite nahe. Perplexität und kurze Prüfungen sind bequem, weil sie günstig und leicht wiederholbar sind. Sie prüfen jedoch nicht die Schleifen, die einen Agenten nützlich machen: ein Ziel im Blick behalten, Werkzeuge auswählen, Fehlermeldungen lesen und es erneut versuchen. Kalibrierungsdaten können denselben blinden Fleck tragen wie eine Evaluierung.

NariQ macht ein Modell mit 27 Milliarden Parametern nicht universell günstig. Der volle Kontext beansprucht weiterhin Key-Value-Speicher, der Vision-Encoder verbleibt in hoher Präzision, und die Inferenzgeschwindigkeit hängt von Kerneln für ein bestimmtes Gerät ab. Die Arbeit zeigt jedoch, dass Gewichtsspeicher und Agentenkompetenz bei drei oder 2,5 Bit in den getesteten Aufgaben nicht zwangsläufig gemeinsam abfallen müssen.

Zurück an der Workstation erreichte der Agent das Ende seiner Terminalaufgabe. Die 10,12 Gigabyte große Datei hatte von Anfang an gepasst. Ob der nächste Rechner sie ausführen kann, hängt weniger von der Datei ab als von dem Namen auf seinem Grafikchip.

## Quellen

- Kim, D. (2026). *NariQ: Sub-3-Bit Quantization for Long-Horizon Agentic Tasks*. https://arxiv.org/abs/2611.26157
- Nari Labs (2026). *Qwen3.8-27B-NariQ-GGUF model card*. https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF
- Qwen Team (2026). *Qwen3.8-27B model card*. https://huggingface.co/Qwen/Qwen3.8-27B
- Tseng, J., et al. (2024). *QTIP: Quantization with Trellises and Incoherence Processing*. https://arxiv.org/abs/2406.11235
