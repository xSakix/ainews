+++
title = "Cockroach Labs gibt Programmieragenten klinische Rollen"
slug = "cockroach-labs-gibt-programmieragenten-klinische-rollen"
description = "MOLT Sinai leitet Softwarearbeit durch spezialisierte Agenten, verpflichtende Pläne und kritische Gegenprüfung. Das Unternehmen meldet sieben Rücknahmen in fünf Monaten."
tags = ["agents", "tools", "essays"]
date = 2026-10-11T04:03:06+02:00
draft = false
+++

Cockroach Labs hat eine Pipeline für Programmieragenten beschrieben, die Softwareprobleme wie Krankenhauspatienten behandelt: mit spezialisierten Rollen und verpflichtender Prüfung, bevor die Umsetzung beginnt.

Das System namens MOLT Sinai läuft über GitHub Actions. Labels übertragen den Zustand zwischen einem Triage-Agenten, einer diagnostischen Aufarbeitung, einem Fellow, der eine Behandlung vorschlägt, einem Review Attending, der den Plan angreift, und einer Entlassungsphase. Die Autoren geben an, das System habe in fünf Monaten mehr als eine Million Zeilen mit sieben Rücknahmen verarbeitet.

## Warum das wichtig ist {#why-it-matters}

Wer die Pflege eines Repositorys verantwortet und Änderungen an einen Agenten delegiert, braucht mehr als ein leistungsfähiges Modell: Der Prozess muss den Umfang wahren, Entscheidungen sichtbar machen und schwache Pläne stoppen, bevor sie zu Code werden. MOLT Sinai übersetzt diese Anforderungen in Workflow-Zustände und schriftliche Skills, statt auf einen langen Prompt oder das Gedächtnis eines Agenten zu vertrauen.

Seine stärkste Regel betrifft den Ablauf: kein Code vor einem Plan und kein Plan ohne Prüfung. Der Review Attending wird angewiesen, Fehler zu suchen, statt reflexartig zu kooperieren. Verlässt die Arbeit den genehmigten Umfang, gilt die weitere Regel „Nicht improvisieren“; der Agent muss anhalten und neu planen. Tests dürfen nicht abgeschwächt werden, nur damit eine Änderung besteht.

Adam Storm und Rafi Shamim, Entwickler bei Cockroach Labs, berichten von 27 zusammengeführten Pull Requests und 55 Rückgaben durch Prüfer. Sie beschreiben, wie sie in weniger als zwei Tagen für 4.172 Dollar an Modell-Token-Kosten eine Db2-Migrationsquelle ergänzten. Ihr Vergleich mit einer neunmonatigen Oracle-Integration für rund 160.000 Dollar veranschaulicht den behaupteten Unterschied, ist aber keine kontrollierte Produktivitätsstudie unter gleichen Bedingungen.

Die Architektur fügt bewusst Bürokratie hinzu. Jede Übergabe verbraucht Token und Zeit; laut den Autoren könne die Pipeline langsamer und teurer sein als ein Schwarm. Ihr Ziel ist nicht maximale Parallelität, sondern ein überprüfbarer Weg vom Issue zum zusammengeführten Code und eine klar getrennte Verantwortung für jede Stufe.

Die übertragbare Idee ist kleiner als die Krankenhausmetapher: Zustand außerhalb des Chats speichern, einen ausdrücklichen Plan verlangen, Autor und Kritiker trennen und Abbruchbedingungen in den Agentenanweisungen festhalten. Diese Kontrollen lassen sich übernehmen, ohne jede Rolle nachzubilden.

Cockroach Labs veröffentlichte den Workflow als technischen Erfahrungsbericht, nicht als unabhängige Evaluation. Der nächste Beleg wären Daten auf Repository-Ebene, die ähnliche Aufgaben unter dieser Pipeline und gewöhnlichen menschlichen oder agentischen Abläufen vergleichen, einschließlich Prüfzeit, Fehlerschwere und Arbeit, die nie zusammengeführt wurde.

## Überprüfung {#verification}

| Behauptung | Einstufung | Primärquelle | Unabhängige Überprüfung |
|---|---|---|---|
| MOLT Sinai nutzt GitHub Actions, Labels und rollenspezifische Agenten, um Issues durch einen gestuften Workflow zu führen | VERIFIZIERT | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | keine |
| Der Workflow verlangt einen genehmigten Plan vor dem Code und weist Agenten bei verändertem Umfang zur Neuplanung an | VERIFIZIERT | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | keine |
| Cockroach Labs meldet 27 zusammengeführte Pull Requests, 55 Rückgaben und sieben Rücknahmen in fünf Monaten | LAUT UNTERNEHMEN | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | keine |
| Die Db2-Migrationsquelle benötigte weniger als zwei Tage und 4.172 Dollar an Token-Kosten | LAUT UNTERNEHMEN | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | keine |
| Die Autoren sagen, das System erhöhe Zeitaufwand, Kosten und Bürokratie gegenüber einem Schwarm | VERIFIZIERT | https://www.cockroachlabs.com/blog/experiment-running-hospital-code/ | keine |
