+++
title = "Telegrammstil spart Token bei Agentenübergaben"
slug = "telegrammstil-spart-token-bei-agentenuebergaben"
description = "Ein öffentlicher Benchmark zeigt, dass eine Anweisung mehrere Modelle maschinenlesbare Aufzeichnungen mit ungefähr halb so vielen Ausgabe-Token schreiben lässt. Während aktiven Denkens versagt die Technik."
tags = ["agents", "research", "tools"]
date = 2026-10-10T03:58:41+02:00
draft = false
+++

Die Anweisung, im Telegrammstil zu schreiben, verkürzte die Ausgaben von Sprachmodellen um rund 40 % bis 49 %. Andere Modelle konnten die aufgezeichneten Fakten mit vergleichbarer Genauigkeit wiedergeben.

Der unabhängige Entwickler Travis Smith testete die Anweisung an 50 Passagen und etwa 1.300 Fragen. Sie fordert das Modell auf, Artikel und Füllwörter wegzulassen, abzukürzen, jeden Fakt, jede Zahl und jeden Eigennamen zu erhalten und kleinzuschreiben, damit Großbuchstaben die Tokenzahl nicht erhöhen.

## Warum das wichtig ist {#why-it-matters}

Wer Agenten entwickelt, zahlt einmal, wenn ein Modell eine Erinnerung schreibt, und erneut, wenn ein anderes sie liest. Nach Abschluss der Arbeit komprimierte Maschinennotizen können sowohl die Ausgabekosten als auch den durch wiederholte Übergaben belegten Kontext reduzieren.

Der Benchmark trennt Schreiben und Lesen. Gemma 4, Qwen3.8 und GLM-5.3-Flash schrieben verdichtete Aufzeichnungen. Modelle mehrerer Familien beantworteten fest verankerte Fragen entweder anhand dieser Aufzeichnungen oder gewöhnlicher Zusammenfassungen. Smith veröffentlichte das Testframework, eingefrorene Ergebnisprotokolle und ein ausführbares Notebook.

Das klarste Ergebnis lieferten die schreibenden Modelle. Gemma benötigte rund 40 % weniger abgerechnete Ausgabe-Token, Qwen und GLM etwa 49 % weniger. Lesende Modelle erreichten mit komprimierten Aufzeichnungen das 0,99- bis 1,10-Fache ihrer Genauigkeit bei gewöhnlichen Zusammenfassungen. Vier Leserfamilien erhielten kein ausgearbeitetes Stilbeispiel. Das legt nahe, dass die Konvention bereits aus Trainingsdaten bekannt war.

## Kompression gehört hinter das Denken

Die Platzierung veränderte das Ergebnis. Modelle, die Antworten direkt im Telegrammstil formulieren sollten, behielten nur etwa vier Fünftel ihrer üblichen Genauigkeit. Wurde der Inhalt erst festgelegt und dann zu einer Aufzeichnung komprimiert, erreichte oder übertraf das nachgelagerte Auslesen die normale Zusammenfassung leicht.

Das eignet die Technik für Notizarchive, Agentengedächtnisse und Übergaben. Für nutzerseitige Antworten oder Schritte, in denen das Modell noch entscheidet, was es sagen soll, passt sie schlecht. Der komprimierte Text bleibt für Menschen lesbar, ist aber bewusst weniger angenehm als gewöhnliche Prosa.

Verpflichtendes Reasoning verursachte einen weiteren Fehlerfall. GPT-5-mini erzeugte laut Ergebnisprotokoll des Autors weniger sichtbare Token, gab aber ungefähr dreimal mehr für verborgenes Denken aus. Das Schreiben wurde insgesamt teurer. Teams müssen deshalb die tatsächliche Abrechnung des Anbieters prüfen, statt nur Zeichen oder sichtbare Token zu zählen.

Smith maß auch einen Hin- und Rückweg, bei dem komprimierter Text wieder zu Prosa erweitert wurde. Das gespeicherte Ergebnis blieb kleiner als eine gewöhnliche Zusammenfassung. Der zusätzliche Modellaufruf verbrauchte aber mehr Token, als beim ersten Schreiben gespart wurden. Wiederholtes günstiges Lesen kann diese Kosten ausgleichen, ein Ablauf mit einmaligem Schreiben und Lesen möglicherweise nicht.

Die historische Rahmung ist vielleicht nicht entscheidend. Smith führte nicht die strenge Kontrolle durch, maximale Kürze ohne Erwähnung des Telegrammstils zu verlangen. Das Experiment stützt daher die praktische Anweisung, belegt aber nicht, dass der Telegrammstil selbst den Gewinn verursacht.

Das Ergebnis bleibt außerdem ein Benchmark des Autors. Seine Stärken sind ungewöhnlich gut überprüfbare Materialien und familienübergreifende Tests. Seine Grenze ist, dass Passagen, Fragen und Bewerter eine bestimmte Art faktischer Aufzeichnung definieren. Code, mathematische Herleitungen und Gesprächsgedächtnisse können sich anders komprimieren lassen.

Das veröffentlichte Notebook lässt sich jetzt auf produktive Agentenprotokolle anwenden. So können Teams Aufgabenerfolg und vom Anbieter abgerechnete Token am eigenen Datenverkehr vergleichen.

## Überprüfung {#verification}

| Behauptung | Einstufung | Primärquelle | Unabhängige Überprüfung |
|---|---|---|---|
| Telegrammstil-Anweisungen reduzierten abgerechnete Ausgabe-Token bei Gemma, Qwen und GLM um etwa 40–49 % | LAUT UNTERNEHMEN | https://fiveminutesforward.com/post/2026-10-04-telegraph-test/ | keine |
| Familienübergreifende Leser rekonstruierten Fakten mit dem 0,99- bis 1,10-Fachen der Genauigkeit normaler Textzusammenfassungen | LAUT UNTERNEHMEN | https://fiveminutesforward.com/post/2026-10-04-telegraph-test/ | keine |
| Direktes Formulieren im Telegrammstil senkte die Genauigkeit auf etwa das 0,81-Fache der normalen Kontrolle | LAUT UNTERNEHMEN | https://fiveminutesforward.com/post/2026-10-04-telegraph-test/ | keine |
| GPT-5-minis verpflichtendes Reasoning hob im Test des Autors die Einsparung sichtbarer Token auf | LAUT UNTERNEHMEN | https://fiveminutesforward.com/post/2026-10-04-telegraph-test/ | keine |
| Testframework, eingefrorene Ergebnisprotokolle und Notebook sind öffentlich | VERIFIZIERT | https://github.com/Travis42/telegraph-test | keine |
| Die Methode eignet sich am besten für feststehende maschinenlesbare Aufzeichnungen statt für aktives Denken | ANALYSE | https://fiveminutesforward.com/post/2026-10-04-telegraph-test/ | keine |
