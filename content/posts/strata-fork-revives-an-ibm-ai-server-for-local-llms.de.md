+++
title = "Strata-Fork belebt einen IBM-KI-Server für lokale LLMs"
slug = "strata-fork-belebt-ibm-ki-server-lokale-llms"
description = "Ein hardwarespezifischer Fork führt Qwen3.8-Flash-Next auf zwei POWER9-Prozessoren und vier V100-GPUs aus. Er zeigt, was modellbewusste Optimierung aus einem System von 2018 zurückgewinnen kann."
tags = ["projects", "hardware", "models"]
date = 2026-10-05T03:58:30+02:00
draft = false
+++

Ein Community-Entwickler hat die Strata-Inferenz-Engine an IBMs AC922 angepasst. Dieser Server von 2018 verbindet seine zwei POWER9-Prozessoren direkt mit vier Nvidia-V100-Beschleunigern mit jeweils 16 GB. Das Ergebnis ist weniger ein allgemeiner Ersatz für llama.cpp als eine Fallstudie dazu, die Topologie einer ungewöhnlichen Maschine für ein modernes Mixture-of-Experts-Modell zu nutzen.

Der Fork führt ein quantisiertes Qwen3.8-Flash-Next aus, ein Modell mit 125 Milliarden Parametern, dessen dünne Aktivierung nur einen kleinen Teil der Experten pro Token einschaltet. Strata hält häufig verwendete Experten auf den GPUs und den vollständigen Expertensatz im Systemspeicher. Das passt zum AC922, dessen CPUs und GPUs NVLink-2.0-Verbindungen mit hoher Bandbreite teilen, statt nur über gewöhnliches PCIe zu kommunizieren.

Der Entwickler ergänzte einen Speicherbereich mit gesperrten Seiten pro CPU-Sockel, platzierte Experten unter Berücksichtigung der nicht einheitlichen Speicheranordnung und ließ eine sonst ungenutzte Peer-GPU Daten über ihren eigenen NVLink abrufen. Weitere Änderungen umfassen FP16-Kernel für Volta-Tensorkerne, Aufteilung von Schichten in einer Pipeline sowie POWER9-spezifische Vektor- und Thread-Verarbeitung.

Auf vier V100 erreichen die eigenen Messungen des Projekts beim Lesen eines Prompts mit 135.000 Token einen Spitzenwert von 7.357 Token pro Sekunde. Ein Prompt mit 252.000 Token wird mit 7.089 Token pro Sekunde verarbeitet und benötigt 35,5 Sekunden. Gierige Generierung erreicht 113 Token pro Sekunde auf JSON, 103 auf Code und 84 auf Fließtext. Bei wiederverwendetem Kontext von 252.000 Token erscheint das erste Folgetoken nach 0,26 Sekunden. Die Generierung läuft anschließend mit 60 Token pro Sekunde.

Diese Zahlen sind Messungen des Entwicklers auf einem spezialisierten Server, kein übertragbarer Benchmark. Die Prompt-Verarbeitungsgeschwindigkeit variiert stark mit der Prompt-Länge. Der erzeugte Texttyp verändert die Decodiergeschwindigkeit. Das Repository beschreibt den Fork als experimentell und vom ursprünglichen Strata-Projekt nicht unterstützt.

Dennoch veranschaulicht das Projekt einen zunehmend nützlichen Ansatz für lokale Inferenz: um ein bestimmtes Modell und eine bestimmte Speicherhierarchie herum optimieren, statt von einer allgemeinen Engine gleiche Behandlung jeder Maschine zu verlangen. Der AC922 ist alte, stromhungrige Unternehmenshardware, doch seine CPU-GPU-Verbindungen sind weiterhin ungewöhnlich leistungsfähig. Ein Modell mit Tausenden Experten gibt diesen Verbindungen nützliche Arbeit.

Der Code steht unter Stratas MIT-Lizenz auf dem `ac922`-Branch des Forks, mit Hinweisen zu Build, Qualität und Benchmarks. Manche Änderungen könnten später ins ursprüngliche Projekt gelangen. Der unmittelbare Wert ist jedoch nachvollziehbare Technik für Besitzer von Hardware, die gängige Inferenzprojekte selten ansprechen.

## Überprüfung {#verification}

| Behauptung | Einstufung | Primärquelle | Unabhängige Überprüfung |
| --- | --- | --- | --- |
| Fork zielt auf AC922 mit zwei POWER9-CPUs, vier V100-GPUs mit 16 GB und NVLink 2.0 | VERIFIZIERT | [Repository](https://github.com/eelgaev/Strata-AC922) | keine |
| NUMA-bewusste Expertenplatzierung, pro Sockel Speicherbereiche mit gesperrten Seiten, Peer-GPU-Abrufe und Volta/POWER9-Kernel | VERIFIZIERT | [Repository](https://github.com/eelgaev/Strata-AC922) | Code und technische Hinweise vorhanden; nicht unabhängig ausgeführt |
| Prefill-Spitze von 7.357 Token/s und 7.089 Token/s bei 252.000 Token | LAUT COMMUNITY | [Repository](https://github.com/eelgaev/Strata-AC922) | keine; Benchmark des Entwicklers |
| Decodieren erreicht 113 Token/s auf JSON und 84 auf Fließtext | LAUT COMMUNITY | [Repository](https://github.com/eelgaev/Strata-AC922) | keine; Benchmark des Entwicklers |
| Fork ist experimentell und vom ursprünglichen Projekt nicht unterstützt | VERIFIZIERT | [Repository](https://github.com/eelgaev/Strata-AC922) | ausdrücklicher Repository-Hinweis |
| Hardwarespezifische Inferenz kann einer älteren spezialisierten Speichertopologie neuen Wert geben | ANALYSE | [Repository](https://github.com/eelgaev/Strata-AC922) | Schlussfolgerung aus Implementierung und Messungen |
