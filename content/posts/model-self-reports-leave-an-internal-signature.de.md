+++
title = "Modellselbstauskünfte hinterlassen eine interne Signatur"
slug = "modellselbstauskuenfte-hinterlassen-interne-signatur"
description = "Eine kontrollierte Studie zeigt, dass zutreffende Berichte über gelernte Präferenzen mehr der entscheidungsrelevanten Berechnung wiederverwenden. Der Befund legt in engen Grenzen einen White-Box-Test der Fundierung nahe."
tags = ["research", "models"]
date = 2026-10-10T04:01:41+02:00
draft = false
+++

Modelle, die ihre eigenen gelernten Präferenzen korrekt beschrieben, verwendeten mehr der internen Berechnung ihrer Entscheidungen wieder als konfabulierende Modelle, berichtet ein neuer Preprint.

David Atkinson und David Bau von der Northeastern University schufen zusammen mit Dillon Plunkett von Eleos AI Research fiktive Figuren mit verborgenen Präferenzen und trainierten Qwen3-Modelle, in deren Namen zu entscheiden. Die Modelle wurden nie darauf trainiert, diese Präferenzen zu erklären. So konnte das Team untersuchen, ob zutreffende Selbstauskünfte von selbst entstehen.

## Warum das wichtig ist {#why-it-matters}

Wer in der Interpretierbarkeitsforschung die Aussage eines Modells über seinen eigenen Zustand bewertet, steht meist vor einem Zirkelschluss: Die Aussage klingt plausibel, doch der Zustand selbst lässt sich womöglich nicht prüfen. Dieses Experiment liefert bekannte Referenzwerte und findet einen strukturellen Unterschied zwischen zutreffenden und unzutreffenden Berichten.

Die fiktiven Präferenzen waren einfache Regeln aus fünf Zahlen für Merkmale wie Entfernung zum Stadtzentrum und Zimmergröße. Ein Modell sah Optionspaare und lernte, welche seine zugewiesene Figur wählen würde. Separate Prompts forderten anschließend die Präferenzgewichte der Figur als Zahlen an.

In einigen Läufen entstanden schließlich korrekte Berichte, obwohl die Trainingsdaten nur Entscheidungen enthielten. Das ist wichtig, weil das Modell keine im Training gezeigte Erklärung bloß nachahmen konnte. Es musste seine gelernte Entscheidungsregel in Sprache umsetzen.

## Dieselben Gewichte tragen Wahl und Bericht

Die Autoren nutzten anschließend Attribution Patching. Die Methode schätzt, welche Adapterkomponenten zu einer bestimmten Ausgabe beitragen. Sie verglichen das Muster für eine Entscheidung mit dem Muster für den Bericht über die verborgene Präferenz.

Zutreffende Adapter hatten zwischen diesen Mustern eine durchschnittliche Ähnlichkeit von 0,34, unzutreffende dagegen 0,08. Das Unsicherheitsintervall der Autoren für den Unterschied schloss null aus. Einfach ausgedrückt: Korrekt berichtende Modelle nutzten tendenziell mehr derselben hinzugefügten Schaltkreise zum Handeln und zur Beschreibung dessen, was die Handlung leitete.

Schichtexperimente wiesen in dieselbe Richtung. Ein Qwen3-Modell mit 14 Milliarden Parametern, das über alle 40 Schichten trainiert wurde, lernte die Entscheidungen, berichtete aber schlecht über seine Präferenzen. Auf ungefähr das erste Viertel bis die erste Hälfte des Netzwerks beschränktes Training ergab deutlich getreuere Berichte. Training nur späterer Schichten reproduzierte den Effekt nicht. Die Autoren deuten das als Verlagerung von Präferenzinformationen in Schichten, die vorhandene Verbalisierungsmechanismen erreichen können.

Die Belege sind mechanistisch, nicht verhaltensbezogen: Der Test muss die Formulierung des Berichts nicht verstehen. Grundsätzlich könnte derselbe Vergleich bei einem verschleierten Bericht oder einer unbekannten Sprache funktionieren, sofern die relevanten internen Komponenten zugänglich sind.

### Die Studie ergab außerdem

Größere Qwen3-Modelle lernten häufiger getreue Selbstauskünfte als kleinere Varianten. Einige kleine Modelle entwickelten trotz guter Entscheidungen negativ korrelierte Berichte. Eine Replikation mit Gemma 4 fand bei größeren Konfigurationen sowohl Adapter mit hoher als auch mit geringer Berichtstreue. Innerhalb eines gemeinsamen Modells war die Beziehung zwischen Attributionsähnlichkeit und Berichtstreue über Figuren hinweg positiv, aber schwach.

Der Befund liefert keinen Introspektionsdetektor für eingesetzte Modelle. Die Präferenzregeln waren konstruiert, linear und nur fünfdimensional. Die Experimente veränderten leichte Adapter statt vollständiger Modellgewichte, und die Ähnlichkeitswerte der zutreffenden und unzutreffenden Gruppen überlappten. Hohe Ähnlichkeit stützte in diesem Aufbau Berichtstreue; ein niedriger Wert bewies aber weder Täuschung noch Konfabulation.

Der Preprint wurde am 5. Oktober 2026 eingereicht. Der klarste nächste Schritt ist die Prüfung, ob dieselbe interne Wiederverwendung auftritt, wenn Modelle reichhaltigere gelernte Strategien beschreiben, deren tatsächliche Grundlagen weiterhin unabhängig messbar sind.

## Überprüfung {#verification}

| Behauptung | Einstufung | Primärquelle | Unabhängige Überprüfung |
|---|---|---|---|
| Die Studie trainierte LoRA-Adapter auf verborgene lineare Präferenzen und beobachtete korrekte Selbstauskünfte ohne entsprechendes überwachtes Training | LAUT UNTERNEHMEN | https://arxiv.org/abs/2610.07186 | keine |
| Zutreffende Adapter erreichten durchschnittlich 0,34 Attributionsähnlichkeit, unzutreffende 0,08 | LAUT UNTERNEHMEN | https://arxiv.org/abs/2610.07186 | keine |
| Training nur früher Schichten verbesserte die Selbstauskunft in Qwen3-14B, Training nur später Schichten nicht | LAUT UNTERNEHMEN | https://arxiv.org/abs/2610.07186 | keine |
| Die Methode trennt Gruppen mit überlappenden Werten und wurde an Adaptern in kontrollierter Umgebung getestet | VERIFIZIERT | https://arxiv.org/abs/2610.07186 | keine |
| Die Arbeit wurde am 5. Oktober 2026 von Atkinson, Plunkett und Bau eingereicht | VERIFIZIERT | https://arxiv.org/abs/2610.07186 | keine |
