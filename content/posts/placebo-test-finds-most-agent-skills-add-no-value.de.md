+++
title = "Placebotest findet keinen Mehrwert bei den meisten Agenten-Skills"
slug = "placebotest-kein-mehrwert-meiste-agenten-skills"
description = "Ein vorab registriertes Experiment vergleicht neun Claude-Code-Skills mit gleich langen neutralen Anweisungen. Zwei sind günstiger als Placebo, einer schlechter und sechs statistisch nicht unterscheidbar."
tags = ["research", "agents", "tools"]
date = 2026-10-07T03:57:57+02:00
draft = false
+++

Die meisten beliebten Skills für Programmieragenten schnitten in einem neuen placebokontrollierten Experiment nicht besser ab als gleich lange neutrale Anweisungen.

Das Projekt skill-placebo testete neun Claude-Code-Skills auf 15 öffentlichen Aufgaben aus SWE-bench Verified, Terminal-Bench 2.1 und OpenThoughts-TBLite. Jeder Skill wurde mit neutralem Text derselben Token-Länge gepaart, der über denselben Mechanismus installiert wurde.

## Warum das wichtig ist {#why-it-matters}

Ein Entwickler, der eine lange Anweisungsdatei hinzufügt, kann ein verändertes Verhalten des Agenten beobachten und es dem darin enthaltenen Verfahren zuschreiben. Dieses Experiment fragt, ob der nützliche Bestandteil tatsächlich der Skill ist oder lediglich der zusätzliche Kontext, die Vorprägung und die damit einhergehende Ausführungsvarianz.

Die Methode wurde vor dem ersten Durchlauf registriert. Claude Opus 5.5 absolvierte 30 Versuche pro Arm, insgesamt 450 aufgezeichnete Versuche. Kosten waren die primäre Zielgröße. Auch die Erfolgsquote der Aufgaben wurde erfasst, mit statistischer Korrektur über die neun Vergleiche hinweg.

Zwei Skills waren günstiger als ihre Placebos: ponytail um 12 % und agent-skills um 5 %. Planning-with-files bestand 80 % seiner Versuche, während sein Placebo alle 30 bestand. Nach der vorab registrierten Entscheidungsregel des Projekts war es damit schlechter. Die anderen sechs Skills waren statistisch nicht von ihren passenden neutralen Texten zu unterscheiden.

Keiner der neun war messbar günstiger als ein Durchlauf ohne Skill. Neutraler Placebotext allein veränderte die Kosten gegenüber der Vergleichsbasis ohne Skill um 2 % bis 16 %. Damit sind Prompt-Länge und scheinbar irrelevanter Kontext Teil der Behandlung und kein harmloser Hintergrund.

## Die Kontrolle verbessert die Frage, nicht die Stichprobengröße

Eine Vergleichsbasis ohne Skill fragt, ob das gesamte Paket die Leistung verändert. Das passende Placebo stellt eine präzisere Frage: ob seine eigentlichen Anweisungen über dieselbe Textmenge hinaus Mehrwert bieten, wenn diese auf dieselbe Weise bereitgestellt wird. Die beiden Vergleiche können ohne Widerspruch unterschiedlich ausfallen.

Das Repository legt die vorab registrierte Methode, Ergebnisse jedes Versuchs und Agentenprotokolle offen. Es dokumentiert auch eine Änderung vom 6. Oktober: Zwei Zeitüberschreitungen, deren Tests später bestanden wurden, wurden gemäß den ursprünglichen Regeln als Fehlschläge gezählt. Dadurch wechselte planning-with-files von „nicht besser“ zu „schlechter“, ohne dass sich die Kosten änderten.

Die Grenzen sind erheblich. Fünfzehn Aufgaben und 30 Versuche pro Arm lassen breite Intervalle für die Erfolgsquote. Der Durchlauf umfasst ein Hauptmodell und einen Ausführungsrahmen, und die gewählten Skills betonen allgemeine Programmierabläufe statt spezialisierten Referenzwissens. Die aktuellen Protokolle belegen außerdem nicht, wie konsequent jeder Skill während eines Durchlaufs aufgerufen wurde.

Eine kleine Codex-Pilotstudie testete nur drei Skills auf fünf Aufgaben und ist ausdrücklich nachrangig. Ihre Ergebnisse sollten weder mit dem Claude-Experiment vermischt noch als Vergleich von Modellfamilien behandelt werden.

Die Erkenntnis zeigt nicht, dass Programmier-Skills nutzlos sind. Sie zeigt, dass Beliebtheit, Länge und ein plausibles Verfahren schlechte Ersatzgrößen für eine passende Kontrolle sind. Der wiederverwendbare Beitrag ist der Versuchsaufbau: die Methode festlegen, der Kontrolle gleich viel Kontext geben, vollständige Protokolle bewahren und Kosten zusammen mit Erfolg messen.

Künftige Versionen können das Ergebnis durch mehr Aufgaben, andere Ausführungsrahmen und eine Kontrolle mit durchmischten Anweisungen stärken, die das semantische Verfahren von allgemeiner Vorprägung trennt.

## Überprüfung {#verification}

| Behauptung | Einstufung | Primärquelle | Unabhängige Überprüfung |
| --- | --- | --- | --- |
| Das Hauptexperiment führte 450 Versuche mit neun Skills und 15 öffentlichen Aufgaben durch | VERIFIZIERT | [skill-placebo-Repository](https://github.com/simonether/skill-placebo) | Methode, Ergebnisse und Protokolle sind öffentlich |
| Zwei Skills schlugen Placebo bei den Kosten, einer war schlechter und sechs nicht besser | LAUT UNTERNEHMEN | [skill-placebo-Ergebnisse](https://github.com/simonether/skill-placebo) | keine; statistische Analyse des Autors |
| Ponytail kostete 12 % und agent-skills 5 % weniger als das passende Placebo | LAUT UNTERNEHMEN | [skill-placebo-Ergebnisse](https://github.com/simonether/skill-placebo) | keine |
| Planning-with-files bestand 80 %, gegenüber 100 % beim Placebo | LAUT UNTERNEHMEN | [skill-placebo-Ergebnisse](https://github.com/simonether/skill-placebo) | Daten jedes Versuchs sind verfügbar |
| Keiner der neun Skills war messbar günstiger als kein Skill | LAUT UNTERNEHMEN | [skill-placebo-Ergebnisse](https://github.com/simonether/skill-placebo) | keine |
| Passende Kontrollen isolieren den Anweisungsinhalt besser als eine Vergleichsbasis ohne Skill | ANALYSE | [Registrierte Methode](https://github.com/simonether/skill-placebo/blob/main/METHOD.md) | Schlussfolgerung aus dem Versuchsaufbau |
