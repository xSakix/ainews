+++
title = "OpenTPU führt lokale Modelle auf einer 300-Dollar-FPGA-Karte aus"
slug = "opentpu-lokale-modelle-300-dollar-fpga-karte"
description = "Das Apache-lizenzierte Projekt veröffentlicht Beschleunigerentwurf, Compiler, Simulator und Host-Werkzeuge. Der gemessene Durchsatz zeigt ein kleines, durch Speicher begrenztes System statt eines GPU-Ersatzes."
tags = ["hardware", "projects", "models"]
date = 2026-10-07T03:58:57+02:00
draft = false
+++

OpenTPU hat einen vollständigen KI-Beschleuniger-Stack veröffentlicht, der moderne Sprachmodelle auf einer Kintex-7-FPGA-Karte für etwa 300 Dollar ausführt.

Das Repository unter Apache-2.0 enthält SystemVerilog-Hardware, einen Befehlssatz, einen bitgenauen Simulator, eine Kernel-Sprache samt Compiler, Profiling-Werkzeuge und Host-Software. Sein Wert liegt in der Nachvollziehbarkeit: Dieselbe kleine Codebasis reicht von Python-Modellkerneln bis zu den Signalen auf einer physischen PCIe-Platine.

## Warum das wichtig ist {#why-it-matters}

Entwickler, die Inferenzhardware kennenlernen, können jeden Taktzyklus und Speichertransfer verfolgen, ohne einen Rechenzentrumsbeschleuniger zu benötigen. Die entstehende Maschine ist langsam gegenüber heutigen GPUs, doch ihre Grenzen machen den Engpass ungewöhnlich sichtbar.

OpenTPU meldet 30,7 erzeugte Token pro Sekunde für ein Qwen3-0.6B-Modell mit vier Bit und 82,1 für LFM2.5-230M, jeweils einschließlich Host-Aufwand. Größere dichte Modelle sinken in den aufgeführten Konfigurationen auf 12,03 Token pro Sekunde für Qwen3.5-2B und 3,75 für Gemma 4 E4B.

Beim Decodieren erreicht die Karte 82 % bis 94 % des Spitzendurchsatzes ihrer beiden DDR3-Kanäle von 17,1 GB/s. Damit begrenzt die Speicherbandbreite die Leistung, nicht die Matrixarithmetik. Eine systolische Einheit mit vier Spalten hilft beim Verarbeiten von Prompts stärker als beim Erzeugen einzelner Token.

Modelle, die größer als die 4 GiB der Karte sind, können Mixture-of-Experts-Gewichte aus dem Host-Speicher streamen. Das Repository meldet 10,6 Token pro Sekunde für LFM2.5-8B-A1B und 3,95 für Qwen3.5-35B-A3B. Letzteres überträgt dabei 153 MB pro Token über PCIe. Das sind die eigenen Messungen des Projekts, doch Skripte, datierte Builds und Messbedingungen sind öffentlich.

Die Beschreibung „von KI entwickelt“ erfordert Sorgfalt. Laut Projekt erzeugte ein von Menschen gesteuerter Agentenablauf große Teile des Entwurfs und der Optimierung. Das zeigt aber kein autonomes System, das selbst beschließt, eigene Hardware zu bauen. Das konkrete Ergebnis ist der veröffentlichte Stack und die gemeldete bitgenaue Übereinstimmung zwischen Platine und Simulator.

Die nächsten Tests liegen nahe: die veröffentlichten Bitstreams auf derselben Platine reproduzieren, Leistungsaufnahme und Latenz mit günstigen GPUs vergleichen und prüfen, ob externe Mitwirkende die Architektur ändern können, ohne die Gleichwertigkeit mit dem Simulator zu beeinträchtigen.

## Überprüfung {#verification}

| Behauptung | Einstufung | Primärquelle | Unabhängige Überprüfung |
| --- | --- | --- | --- |
| OpenTPU veröffentlicht Hardware, ISA, Simulator, Compiler und Host-Werkzeuge unter Apache-2.0 | VERIFIZIERT | [OpenTPU-Repository](https://github.com/FeSens/openTPU) | Dateien und Lizenz sind zugänglich |
| Qwen3-0.6B erreicht 30,7 Token/s nach tatsächlicher Laufzeit und LFM2.5-230M 82,1 in Vier-Bit-Konfigurationen | LAUT UNTERNEHMEN | [OpenTPU-Messungen](https://github.com/FeSens/openTPU) | keine |
| Das Decodieren nutzt 82 % bis 94 % des DDR3-Spitzendurchsatzes von 17,1 GB/s | LAUT UNTERNEHMEN | [OpenTPU-Messungen](https://github.com/FeSens/openTPU) | keine |
| Qwen3.5-35B-A3B erreicht 3,95 Token/s und streamt dabei 153 MB pro Token | LAUT UNTERNEHMEN | [OpenTPU-Messungen](https://github.com/FeSens/openTPU) | keine |
| Die Karte reproduziert die Token des Simulators bitgenau | LAUT UNTERNEHMEN | [OpenTPU-Repository](https://github.com/FeSens/openTPU) | öffentliche Tests vorhanden; keine unabhängige Hardware-Reproduktion gefunden |
| „Von KI entwickelt“ belegt keine autonome Hardwareentwicklung | ANALYSE | [OpenTPU-Repository](https://github.com/FeSens/openTPU) | die Unterscheidung folgt aus dem dokumentierten, von Menschen gesteuerten Ablauf |
