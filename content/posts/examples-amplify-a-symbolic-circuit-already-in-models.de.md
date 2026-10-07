+++
title = "Beispiele verstärken einen vorhandenen symbolischen Schaltkreis"
slug = "beispiele-verstaerken-vorhandenen-symbolischen-schaltkreis"
description = "Eine Interpretierbarkeitsstudie findet denselben Weg für Abstraktion, Induktion und Abruf schon vor dem Genauigkeitsanstieg durch wenige Beispiele. Demonstrationen scheinen vorhandene Mechanismen zu stärken statt einen neuen Algorithmus aufzubauen."
tags = ["research", "models"]
date = 2026-10-05T03:59:30+02:00
draft = false
+++

Wenn ein Sprachmodell aus mehreren Beispielen in seinem Prompt ein Muster lernt, kann es wirken, als habe es spontan ein neues Verfahren zusammengesetzt. Eine mechanistische Studie der unabhängigen Forscherin Melissa Wessel bietet für eine Familie symbolischer Aufgaben eine andere Erklärung: Das Verfahren ist bereits im Modell vorhanden, und Beispiele verstärken schrittweise das hindurchfließende Signal.

Der Preprint verfolgt einen dreistufigen Schaltkreis in Prompts mit null bis zehn Demonstrationen. Er findet denselben Kernweg bei schlechter und bei fast perfekter Genauigkeit. Die Köpfe erscheinen nicht plötzlich, sobald das Modell das Muster „versteht“. Ihr kausaler Beitrag wächst.

Das ist ein eng begrenztes Experiment und keine allgemeine Theorie des Lernens im Kontext. Es verwandelt aber eine ansprechende Metapher — Beispiele wecken latente Mechanismen — in etwas, in das Forscher eingreifen und das sie testen können.

## Von Token zu Variablen und zurück

Die Aufgabe verwendet abstrakte Drei-Token-Muster wie ABA oder ABB. Die Token sind beliebig, sodass das Modell sich nicht auf ihre gewöhnliche Bedeutung stützen kann. Es muss erschließen, welche Position in die Antwort kopiert werden soll.

Frühere Arbeit identifizierte drei Stufen. Köpfe zur symbolischen Abstraktion übersetzen konkrete Token in Variablen. Köpfe zur symbolischen Induktion arbeiten auf dem abstrakten Muster. Abrufköpfe wandeln die vorhergesagte Variable zurück in das erforderliche Token. Wessel verfolgt diese Struktur in Gemma 2-2B, Llama 3.1-8B und Qwen 3-4B und ändert dabei nur die Zahl der Demonstrationen.

In Gemma 2-2B beginnt die Genauigkeit mit einem Beispiel bei 17 %, erreicht mit vier 93 % und mit zehn 99 %. Die kausale Mediationsanalyse erkennt die drei Stufen aber bereits bei einem Beispiel. Die wichtigen Köpfe bleiben größtenteils zwischen benachbarten Prompt-Längen bestehen. Der kausale Beitrag eines einzelnen Kopfes wächst zwischen einem und zehn Beispielen um bis zum Achtfachen.

Die Interpretation ist quantitativ statt architektonisch: Zusätzliche Beispiele verstärken einen bestehenden Weg, statt einen völlig anderen einzubeziehen.

## Das Signal zwischen Prompts verschieben

Erkennung allein kann Korrelation mit Mechanismus verwechseln. Deshalb verschiebt das Paper auch interne Aktivierungen zwischen Durchläufen. Aktivierungen aus zehn Beispielen in einen Prompt mit einem Beispiel einzusetzen hebt Gemmas Genauigkeit von 17 % auf 88 %. Bei null Beispielen hebt das Ersetzen der Induktions- und Abrufstufen die Genauigkeit eines Musters von 1 % auf 56 %. Zufällige Köpfe außerhalb des Schaltkreises lassen sie unter 1 %.

Der anschaulichste Eingriff nutzt einen „Funktionsvektor“, eine feste Aktivierung aus Köpfen, die die kausale Analyse identifiziert hat. Ihn bei null Beispielen einzufügen hebt die Genauigkeit auf der ABA-Regel von 1 % auf 86 %. Werden die nachgelagerten Abrufköpfe entfernt, fällt diese Wiederherstellung auf 13 %.

Diese Abhängigkeit ist entscheidend. Der Vektor wirkt weder als eigenständige Antwort noch als allgemeiner Impuls für das Netzwerk. Er kann die Induktionsstufe weitgehend ersetzen, weil die späteren Abrufmechanismen weiterhin verfügbar sind, um seine Ausgabe zu lesen.

## Ein nützliches Ergebnis in einem kleinen Bereich

Die Studie lässt Lernen im Kontext weniger wie das Schreiben eines neuen Programms während der Inferenz erscheinen und mehr wie eine Eingabe für ein im Training eingebettetes Programm. Falls sich diese Sicht verallgemeinert, würden die Grenzen eines Modells mit wenigen Beispielen davon abhängen, welche Schaltkreise seine Gewichte enthalten und ob ein Prompt auf sie zugreifen kann.

Das Paper zeigt nicht, dass alle Demonstrationen so funktionieren. Die zentrale Aufgabe ist im Wesentlichen eine kleine relationale Tabelle mit einer Kopieroperation. Ein Analogietest mit Buchstabenfolgen findet eine ähnliche Topologie, wird aber nicht über jedes Modell oder mit dem vollständigen Programm zur Aktivierungsersetzung wiederholt. Die Analysemethode wählt außerdem Komponenten, die zwei Regeln unterscheiden. Sie könnte daher gemeinsame Infrastruktur übersehen.

Am stärksten ist das Ergebnis als konkreter Mechanismus für eine einfache Fähigkeit: Beispiele können einen stabilen symbolischen Weg verstärken, lange bevor das Verhalten verrät, dass dieser Weg vorhanden ist.

## Überprüfung {#verification}

| Behauptung | Einstufung | Primärquelle | Unabhängige Überprüfung |
| --- | --- | --- | --- |
| Die Studie verfolgt Abstraktions-, Induktions- und Abrufstufen in Gemma 2-2B, Llama 3.1-8B und Qwen 3-4B | VERIFIZIERT | [Preprint](https://arxiv.org/abs/2609.36265) | keine |
| Gemmas Genauigkeit steigt von 17 % mit einem Beispiel auf 99 % mit zehn; der Beitrag pro Kopf wächst bis zum Achtfachen | LAUT UNTERNEHMEN | [Preprint](https://arxiv.org/abs/2609.36265) | keine; Experimente der Autorin |
| Aktivierungsersetzung aus zehn Beispielen hebt die Genauigkeit mit einem Beispiel auf 88 %, und Ersetzung ohne Beispiele hebt 1 % auf 56 % | LAUT UNTERNEHMEN | [Preprint](https://arxiv.org/abs/2609.36265) | keine; Experimente der Autorin |
| Funktionsvektor-Injektion hebt die ABA-Genauigkeit ohne Beispiele von 1 % auf 86 %; nach Abrufablation fällt sie auf 13 % | LAUT UNTERNEHMEN | [Preprint](https://arxiv.org/abs/2609.36265) | keine; Experimente der Autorin |
| Demonstrationen verstärken für diese Aufgaben einen vorhandenen Schaltkreis statt einen neuen zu bauen | ANALYSE | [Preprint](https://arxiv.org/abs/2609.36265) | Interpretation kausaler Eingriffe im Paper |
| Verallgemeinerung auf reichhaltigeres abstraktes Schlussfolgern bleibt offen | VERIFIZIERT | [Preprint](https://arxiv.org/abs/2609.36265) | genannte Einschränkung |
