+++
title = "EasyCommand übersetzt Englisch lokal in Bash"
slug = "easycommand-uebersetzt-englisch-lokal-bash"
description = "Das Open-Source-Kommandozeilenwerkzeug bindet llama.cpp ein und liefert zwei kleine, feinabgestimmte Modelle. Sein Autor veröffentlichte außerdem den Trainingssatz mit 401.975 Paaren und den Benchmark-Code."
tags = ["projects", "models", "tools"]
date = 2026-10-06T04:06:31+02:00
draft = false
+++

EasyCommand wandelt englische Anfragen mit einem kleinen, auf einer CPU laufenden Modell in Bash-Befehle um. Prompt und vorgeschlagener Befehl bleiben auf dem Rechner des Nutzers.

Entwickler Max Trivedi veröffentlichte die Kommandozeilenanwendung `ec`, zwei Modellfamilien und einen Datensatz mit 401.975 deduplizierten Anfrage-Befehl-Paaren. Die Anwendung bindet llama.cpp ein, zeigt ihren vorgeschlagenen Befehl vorab an und kann vor der Ausführung um Bestätigung bitten.

Für Entwickler, die gelegentlich eine Erinnerung an Shell-Befehle benötigen, entfernt die lokale Ausführung einen API-Aufruf aus einem sensiblen Teil des Arbeitsablaufs. Dafür tragen sie selbst die Verantwortung: Das Projekt warnt, dass ein plausibler Befehl trotzdem falsch sein kann, und empfiehlt, zunächst den Vorschaumodus zu verwenden.

Die veröffentlichten Modelle basieren auf Qwen2.5-Coder-1.5B-Instruct und Qwen3-0.6B. Beide erscheinen als GGUF-Dateien für lokale Inferenz, zusammengeführte BF16-Modellstände und LoRA-Adapter für weiteres Training. Modelle und Datensatz stehen unter Apache 2.0, Anwendung und Benchmark-Code unter MIT.

Trivedi erklärt, das Modell mit 1,5 Milliarden Parametern habe in einer aktualisierten Version des Englisch-zu-Shell-Benchmarks ALFA 212 von 300 Aufgaben gelöst, gegenüber 191 beim früheren nl2sh-System. Das ist ein vom Autor durchgeführter Vergleich mit unterschiedlichen Modellprompts und Einstellungen, kein unabhängiges Ranglistenergebnis.

Die Veröffentlichung ist ungewöhnlich nützlich, weil sie neben dem Modell auch seine Schwachstellen umfasst. Laut Trivedi reproduziert der flache Datensatz nicht die historische Gewichtung des Trainings und hat keine offizielle Testaufteilung. Er empfiehlt, ganze Aufgabenfamilien zurückzuhalten, statt Paraphrasen zufällig aufzuteilen. Andernfalls könnten nahezu identische Befehle in Training und Evaluierung gelangen.

Das Ziel ist GNU/Linux-Bash statt jeder Shell oder jedes Betriebssystems. Das Repository von EasyCommand ist jetzt öffentlich. Der Autor bittet Nutzer um Tests, die unzuverlässige Übertragung und fehlende Befehlsabdeckung sichtbar machen.

## Überprüfung {#verification}

| Behauptung | Einstufung | Primärquelle | Unabhängige Überprüfung |
| --- | --- | --- | --- |
| EasyCommand läuft lokal, bindet llama.cpp ein und zeigt Befehle vor der Ausführung an | VERIFIZIERT | [Projektbeschreibung](https://dirac.run/posts/easycommand) | [öffentliches Repository](https://github.com/dirac-run/ec) |
| Die Veröffentlichung enthält 401.975 deduplizierte Englisch/Bash-Paare | VERIFIZIERT | [Projektbeschreibung](https://dirac.run/posts/easycommand) | Datensatz aus dem Repository verlinkt |
| Die Modelle leiten sich von Qwen2.5-Coder-1.5B und Qwen3-0.6B ab | VERIFIZIERT | [Projektbeschreibung](https://dirac.run/posts/easycommand) | Modellartefakte aus dem Repository verlinkt |
| Das Modell mit 1,5 Milliarden Parametern erreichte 212/300 gegenüber 191/300 bei nl2sh | LAUT UNTERNEHMEN | [Projektbeschreibung](https://dirac.run/posts/easycommand) | keine; Benchmark des Autors |
| Modelle und Daten stehen unter Apache-2.0, Anwendung und Benchmark-Code unter MIT | VERIFIZIERT | [Projektbeschreibung](https://dirac.run/posts/easycommand) | Lizenzdateien des Repositorys |
| Der Datensatz hat keine offizielle Testaufteilung und bewahrt die historische Gewichtung nicht | LAUT UNTERNEHMEN | [Projektbeschreibung](https://dirac.run/posts/easycommand) | Offenlegung des Autors |
