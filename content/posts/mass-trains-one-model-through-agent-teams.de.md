+++
title = "MASS trainiert ein Modell mithilfe von Agententeams"
slug = "mass-trainiert-ein-modell-mithilfe-agententeams"
description = "Sakana AI und UC Berkeley nutzen ein Modell, um Multiagenten-Arbeitsabläufe zu entwerfen, auszuführen und zu bewerten, und trainieren dieses Modell anschließend mit den besten Teamausgaben."
tags = ["research", "agents"]
date = 2026-10-12T03:58:37+02:00
draft = false
+++

Sakana AI und UC Berkeley haben MASS vorgestellt, eine Trainingsmethode, bei der ein Modell sich verbessert, indem es Agententeams entwirft, ihre Arbeit bewertet und aus den besten Ergebnissen lernt.

Der Preprint zielt auf Forschungsaufgaben, deren Antworten sich nicht mit einem Compiler oder einer exakten Lösung prüfen lassen. Statt einen Multiagenten-Arbeitsablauf von Hand festzulegen, schreibt dasselbe zugrunde liegende Modell Rollen, Anweisungen, Ausgabeverträge und Aufrufreihenfolge, führt das entstehende Team aus und bewertet Antwortkandidaten.

## Warum das wichtig ist {#why-it-matters}

Für ein Team, das Forschungsagenten baut, ist der Entwurf des Arbeitsablaufs gewöhnlich ein weiteres manuelles Prompt-Engineering-Projekt. MASS macht diesen Entwurf zu einem Teil des Trainings und entfernt anschließend beim Einsatz die Multiagentenmechanik, sodass das verbesserte Einzelmodell antworten kann, ohne für den gesamten Suchprozess zu bezahlen.

Die Methode hat zwei Schleifen. In der inneren Schleife schlägt ein Arbeitsablaufoptimierer schriftliche Teamstrukturen vor, und eine Ausführungskomponente führt sie aus. Eine Bewertungskomponente wählt stärkere Ausgaben aus Aufgaben ohne automatische Referenzlösung. In der äußeren Schleife wird das Modell mit diesen ausgewählten Teamdurchläufen feinabgestimmt und zum Ausgangspunkt einer weiteren Runde.

Die Autoren vergleichen den Prozess mit Selbstspiel, doch der Gegner ist kein anderer Spieler. Das Modell schafft zunehmend anspruchsvolle Formen der Zusammenarbeit für Kopien seiner selbst und übernimmt anschließend das beste Verhalten in einen Checkpoint. Die Teamtopologie ist daher ein vorübergehendes Trainingsgerüst statt einer dauerhaften Anforderung für den Inferenzbetrieb.

## Die Auswahlqualität ist die entscheidende Abhängigkeit

MASS ist auf modellbasierte Urteile angewiesen, weil seinen Zielforschungsfragen ein deterministisches Orakel fehlt. Die Arbeit nutzt separate Spitzenmodelle, darunter GPT-5.5 und Claude Opus 4.8, als zurückgehaltene Prüfer für die Evaluierung. Sakana berichtet, das trainierte Modell verbessere seine bewertete Antwortqualität und nutze dabei weniger Ausgabe-Token als die Multiagententeams, die sein Trainingsmaterial erzeugten.

Diese Belege stammen weiterhin aus Sprachmodellbewertungen selbst. Ein Prüfer kann ausgefeilte, vertraute oder wortreiche Antworten bevorzugen, ohne zu messen, ob eine Forschungsaussage wahr ist. Zurückgehaltene Prüfer verringern direkte Überanpassung an einen einzelnen Bewerter, liefern aber keine faktischen Referenzdaten. Das Ergebnis ist am besten als Verbesserung unter dem Bewertungsprotokoll der Arbeit zu lesen.

Das Trainingsverfahren versucht, den Zusammenbruch auf einen einzelnen zufällig erfolgreichen Arbeitsablauf zu begrenzen. Jede Generation führt ein Champion-Turnier 18-mal durch und behält die besten 16 Teamspuren für die Feinabstimmung. Der Optimierer kann Rollenbeschreibungen, Kommunikationsreihenfolge und Ausgabeformate ändern und hat damit mehr Freiheit als bei der Auswahl zwischen wenigen festen Prompts.

Der Entwurf mit einem gemeinsamen Modell begrenzt auch die Aussage. Ausführung, Optimierung und Bewertung sind Rollen einer Modellfamilie statt eines Marktes unabhängig spezialisierter Systeme. Das macht rekursive Verbesserung leichter der Trainingsschleife zuzuordnen, lässt aber offen, ob heterogene Teams andere Strategien entdecken würden.

## Der Arbeitsablauf verschwindet nach dem Training

Das klarste praktische Merkmal ist die Destillation in das Basismodell. Ein Nutzer des eingesetzten Modells muss weder das 18-fache Turnier wiederholen noch den endgültigen Teamgraphen pflegen. Der zusätzliche Rechenaufwand konzentriert sich auf Datengenerierung und Training, während die Inferenz das entstandene Modell direkt nutzt.

Die Arbeit und Projektbeschreibung sind öffentlich und erlauben eine genauere Prüfung von Prompts und Evaluierungsentwurf. Unabhängige Reproduktion muss testen, ob die Verbesserungen bei anderen Prüfern, Faktenprüfung und Aufgaben außerhalb des Forschungssets der Autoren bestehen bleiben.

## Überprüfung {#verification}

| Behauptung | Einstufung | Primärquelle | Unabhängige Überprüfung |
|---|---|---|---|
| MASS nutzt ein Modell als Arbeitsablaufoptimierer, Ausführungs- und Bewertungskomponente und stimmt es dann mit ausgewählten Teamdurchläufen fein ab | VERIFIZIERT | https://arxiv.org/abs/2610.12176 | https://pub.sakana.ai/mass/ |
| Die innere Schleife durchsucht schriftliche Teamrollen, Anweisungen, Ausgabeverträge und Aufrufreihenfolgen | VERIFIZIERT | https://arxiv.org/abs/2610.12176 | https://pub.sakana.ai/mass/ |
| Die Autoren melden nach dem Training höhere bewertete Qualität bei weniger Ausgabe-Token | LAUT UNTERNEHMEN | https://pub.sakana.ai/mass/ | keine |
| GPT-5.5 und Claude Opus 4.8 dienen in der berichteten Evaluierung als zurückgehaltene externe Prüfer | VERIFIZIERT | https://arxiv.org/abs/2610.12176 | keine |
| Modellbasierte Bewertung stellt faktische Richtigkeit nicht unabhängig fest | ANALYSE | https://arxiv.org/abs/2610.12176 | keine |
