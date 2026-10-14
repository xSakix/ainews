+++
title = "PolyStrata führt große MoE-Modelle auf Gaming-GPUs aus"
slug = "polystrata-fuehrt-grosse-moe-modelle-auf-gaming-gpus-aus"
description = "Die Open-Source-Laufzeitumgebung hält ausgewählte Modellexperten im Arbeitsspeicher und überträgt sie bei Bedarf auf eine Verbraucher-GPU. Ihr Ein-Klick-Paket bietet lokale OpenAI- und Anthropic-kompatible APIs."
tags = ["projects", "models", "hardware"]
date = 2026-10-12T03:57:37+02:00
draft = false
+++

PolyStrata hat eine Open-Source-Laufzeitumgebung veröffentlicht, die Arbeitsspeicher nutzt, um Mixture-of-Experts-Modelle zu betreiben, die nicht vollständig auf eine Gaming-GPU passen.

Das Ein-Klick-Paket umschließt die Strata-Laufzeitumgebung und richtet sich an Nvidia- und AMD-Karten mit mindestens 12 GB Videospeicher. Es liefert eine bildfähige Qwen3.8-Flash-Next-Konfiguration und experimentelle Unterstützung für mehrere größere dünn besetzte Modelle und stellt zugleich OpenAI- und Anthropic-kompatible Endpunkte auf dem lokalen Rechner bereit.

## Warum das wichtig ist {#why-it-matters}

Für Entwickler mit einer Workstation statt eines Servers macht PolyStrata aus freiem Arbeitsspeicher einen größeren Modellpool. Nur die für das aktuelle Token benötigten Experten werden durch die GPU geleitet; Datenbewegung und Speicherkapazität werden gegen die Kosten von Multi-GPU-Hardware abgewogen.

Mixture-of-Experts-Modelle enthalten viele spezialisierte Parameterblöcke, aktivieren aber bei jedem Schritt nur eine Teilmenge. PolyStrata hält diese Blöcke im Host-Speicher und plant die aktiven auf dem Beschleuniger ein. Die Technik verkleinert die Modelldatei nicht: Laut README benötigen experimentelle GLM-5.3-Flash-Versionen je nach Quantisierung weiterhin rund 79 bis 114 GB.

Die eigenen RTX-5070-Messungen des Projekts reichen von rund 94 erzeugten Token pro Sekunde bei seiner kleinsten Zwei-Bit-Einstellung bis zu 53 bei einer größeren Drei-Bit-Einstellung. Es meldet Prompt-Verarbeitungsraten zwischen rund 1.620 und 2.650 Token pro Sekunde bei einem Kontext von 32.000 Token. Dies sind Entwicklerbenchmarks, keine unabhängigen Messungen, und die Qualität unterscheidet sich zwischen Quantisierungsstufen.

PolyStrata dokumentiert auch, wie Claude Code ein dünn besetztes Qwen3.6-35B-Modell mit Drei-Bit-Präzision auf einer Laptop-GPU mit 8 GB steuert. Eine Warmstart-Option liest den System-Prompt vor der interaktiven Sitzung und verkürzt damit die Verzögerung vor der ersten Antwort. Die tatsächliche Nutzbarkeit hängt von RAM-Bandbreite, Modellrouting und dem Umfang der Kontextänderung zwischen Gesprächsrunden ab.

Das Repository ist MIT-lizenziert und bietet lokale Endpunkte, die mit vorhandenen Agentenclients kompatibel sind. Das senkt den Integrationsaufwand und gibt lokalen Anwendungen zugleich Zugriff auf Dateien und Werkzeuge unter den eigenen Berechtigungen des Nutzers. Es bedeutet auch, dass der Betreiber statt eines Hosting-Anbieters Modellaktualisierungen, Netzwerkzugänglichkeit und Log-Verwaltung verantwortet.

## Was ansteht

Unabhängige Tests sollten identische Modelle und Quantisierungseinstellungen mit etablierten Laufzeitumgebungen für CPU-Auslagerung vergleichen. Der aktuelle Wert des Projekts liegt in untersuchbarem Code und einer praktischen Paketierungsschicht; seine hervorgehobenen Geschwindigkeiten bleiben Autorenangaben, bis sie auf mehr Hardware reproduziert sind.

## Überprüfung {#verification}

| Behauptung | Einstufung | Primärquelle | Unabhängige Überprüfung |
|---|---|---|---|
| PolyStrata veröffentlichte eine MIT-lizenzierte lokale Laufzeitumgebung für dünn besetzte Modelle auf Verbraucher-GPUs | VERIFIZIERT | https://github.com/VecSzn/PolyStrata | keine |
| Das Paket bietet OpenAI- und Anthropic-kompatible lokale APIs | VERIFIZIERT | https://github.com/VecSzn/PolyStrata | keine |
| Das README meldet 53–94 erzeugte Token pro Sekunde auf einer RTX 5070 über ausgewählte Quantisierungen hinweg | LAUT UNTERNEHMEN | https://github.com/VecSzn/PolyStrata | keine |
| Experimentelle GLM-5.3-Flash-Dateien benötigen je nach Quantisierung rund 79–114 GB | VERIFIZIERT | https://github.com/VecSzn/PolyStrata | keine |
| Das Laden von Experten aus dem Host-Speicher wägt Kapazität gegen Übertragungs- und Speicherbandbreitenkosten ab | ANALYSE | https://github.com/VecSzn/PolyStrata | keine |
