+++
title = "bilibili erweitert Index-Translate um lokale Builds"
slug = "bilibili-erweitert-index-translate-lokale-builds"
description = "Die offene Übersetzungsfamilie bietet nun GGUF-, FP8- und NVFP4-Pakete, eine kostenlose kompatible API und vier öffentliche Benchmarks. Die Leistungszahlen bleiben eigene Messungen des Entwicklers."
tags = ["models", "tools"]
date = 2026-10-05T04:01:30+02:00
draft = false
+++

bilibili ergänzte Index-Translate am 3. und 4. Oktober um offizielle quantisierte Builds, eine kostenlose öffentliche Schnittstelle und vier Evaluierungssätze. Die kürzlich veröffentlichten Übersetzungsmodelle wurden damit zu einem praktischeren Paket für lokale und gehostete Nutzung.

Die Familie übersetzt Text zwischen 150 Sprachen und akzeptiert Anweisungen zu Terminologie, Formatierung und Stil. Ihre gewöhnlichen Textmodelle umfassen 2 Milliarden, 9 Milliarden und in der Vorschau 35 Milliarden Parameter. Das größte ist ein Mixture-of-Experts-Modell, das pro Token etwa 3 Milliarden Parameter aktiviert.

Die wichtige Änderung für lokale Nutzer betrifft die Pakete. GGUF-Versionen zielen nun auf llama.cpp, FP8-Builds auf vLLM und NVFP4-Builds auf neuere Blackwell-GPUs. Das Projekt veröffentlicht diese Formate für die Text-, Silbenkontroll- und Langdokumentlinien. Auch die Sprachmodelle für Audio haben quantisierte Pakete. Die GGUF-Repositories enthalten allerdings nur deren Textmodellbasis statt der vollständigen Sprachpipeline.

Der neue gehostete Endpunkt stellt die 35B-A3B-Vorschau über eine mit OpenAIs Chat-API kompatible Schnittstelle bereit. Entwickler können das Modell dadurch testen, ohne zunächst passende Hardware zu organisieren. Das Repository bezeichnet den Endpunkt als kostenlos, verspricht aber weder ein Serviceniveau noch langfristige Preise.

Index-Translate ist mehr als ein Satzübersetzer. Der Client kann JSON- und Markdown-Strukturen bewahren, ein Glossar durchsetzen und einen bestimmten Ton anfordern. Verwandte Pakete übersetzen Sprache, streben eine gewünschte Silbenzahl für Synchronisation an oder führen Kontext durch ein langes Dokument mit. Diese Funktionen behandeln die schwierigen Teile produktiver Übersetzung, die ein allgemeiner Prompt wie „übersetze das“ oft übersieht.

bilibili veröffentlichte außerdem Benchmark-Material für instTrans, MEME, SandGlass und NativeLong samt Evaluierungsskripten. Das macht den Testentwurf prüfbar. Die veröffentlichten Werte sind aber weiterhin eigene Messungen des Entwicklers. Im technischen Bericht erreicht das Vorschaumodell 0,8794 auf FLORES COMET-22 und 76,76 beim WMT26-Richter. Letzterer nutzt GPT-5.6-Sol als Evaluator und sollte daher nicht als unabhängiger menschlicher Vergleich gelesen werden.

Die ursprüngliche Modellfamilie erschien am 30. September. Dies ist keine neue Veröffentlichung eines Basismodells. Die Nachricht ist, dass sie innerhalb von vier Tagen die Bereitstellungsformate, den Testendpunkt und die Evaluierungsartefakte erhielt, die aus einer Modellankündigung etwas machen, das Entwickler tatsächlich ausprobieren können.

## Überprüfung {#verification}

| Behauptung | Einstufung | Primärquelle | Unabhängige Überprüfung |
| --- | --- | --- | --- |
| Öffentliche API und vier Benchmarks am 4. Oktober veröffentlicht; quantisierte Builds am 3. Oktober | VERIFIZIERT | [Projekt-Repository](https://github.com/bilibili/Index-Translate) | keine |
| Textmodelle decken 150 Sprachen ab und unterstützen Vorgaben für Terminologie, Formatierung und Stil | VERIFIZIERT | [Projekt-Repository](https://github.com/bilibili/Index-Translate) | [Modellkarte](https://huggingface.co/IndexTeam/Index-Translate-35B-A3B-preview) |
| GGUF-, FP8- und NVFP4-Pakete sowie ihre dokumentierten Ziel-Laufzeiten | VERIFIZIERT | [Projekt-Repository](https://github.com/bilibili/Index-Translate) | einzelne Paketlinks im Repository aufgeführt |
| Vorschaumodell hat insgesamt 35 Milliarden und etwa 3 Milliarden aktive Parameter | VERIFIZIERT | [Modellkarte](https://huggingface.co/IndexTeam/Index-Translate-35B-A3B-preview) | keine |
| FLORES COMET-22 0,8794 und WMT26-Richter 76,76 | LAUT UNTERNEHMEN | [Technischer Bericht](https://arxiv.org/abs/2609.40181) | keine; Bericht nutzt GPT-5.6-Sol als Richter für WMT26 |
| Neue Pakete machen die Familie praktischer für lokale Tests oder einen gehosteten Endpunkt | ANALYSE | [Projekt-Repository](https://github.com/bilibili/Index-Translate) | Schlussfolgerung aus veröffentlichten Artefakten; Dauerhaftigkeit des Endpunkts nicht belegt |
