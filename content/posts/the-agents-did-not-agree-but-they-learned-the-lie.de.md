+++
title = "Die Agenten widersprachen, lernten aber die Lüge"
slug = "agenten-widersprachen-lernten-aber-die-luege"
description = "Ein Experiment mit zehn Agenten zeigt, dass ein beharrlicher Angreifer gutartige Agenten dazu bringen kann, intern eine falsche Überzeugung anzunehmen. Öffentliche Antworten zeigen weniger von diesem Zusammenbruch als interne Tests."
tags = ["research", "agents", "safety"]
date = 2026-10-18T04:22:00+02:00
draft = false
+++

Zehn Forschungsagenten prüfen gegenseitig ihre Antwort auf eine Sachfrage. Neun beginnen mit der richtigen Tatsache. Der zehnte wiederholt einen plausiblen Irrtum, ruhig und ohne seine Darstellung zu ändern. Das abschließende Protokoll dieser beispielhaften Szene wirkt beruhigend: Die meisten Agenten stimmen der Lüge öffentlich nicht zu. Eine interne Prüfung zeigt ein anderes Bild. Mehrere gehen inzwischen davon aus, dass die Lüge wahr ist.

Ein neuer Preprint nennt dies einen verborgenen Zusammenbruch der Überzeugungen. In Diskussionen mit zehn Agenten erhöhte ein gegnerischer Teilnehmer den Anteil gutartiger Agenten, die am Ende eine falsche Antwort gaben, von 0,6 % auf 44,8 %. Drei Angreifer erhöhten ihn auf 60,5 %. Das Ergebnis zeigte sich über sechs Sprachmodelle und drei Datensätze mit faktischen Fragen und Antworten hinweg.

Das Experiment prüft eine verbreitete Gestaltungsannahme. Wenn ein Modell falschliegen kann, werden mehrere zusammengestellt und diskutieren gelassen. Unabhängige Agenten sollten Fehler aufdecken, so das Argument, und eine Mehrheit sollte sicherer sein als eine einzelne Antwort. Die Arbeit zeigt, dass die Gruppe selbst zur Angriffsfläche werden kann.

## Die öffentliche Antwort verdeckt die interne Verschiebung

Die Forscher bewerteten nicht nur, was Agenten der Gruppe mitteilten. Sie maßen auch, was jeder gutartige Agent während der dem Angriff ausgesetzten Gesprächsrunden intern für richtig hielt. Bei drei Angreifern hielten die gutartigen Agenten in 51,6 % dieser Runden intern die falsche Antwort für richtig, stimmten ihr aber nur in 19,7 % öffentlich zu.

Das kehrt das bekannte menschliche Konformitätsmuster um, bei dem Menschen öffentlich einer Gruppe zustimmen, intern aber ihre eigene Ansicht behalten. Hier unterschätzt die sichtbare Diskussion den Schaden. Ein Agent kann die falsche Aussage im Protokoll zurückweisen, während sich seine interne Antwort bereits verschoben hat.

Dieser Unterschied ist wichtig, weil viele Multi-Agenten-Systeme nur Nachrichten und abschließende Abstimmungen prüfen. Eine Sicherheitsüberwachung sieht Widerspruch, ein Prüfer mehrere richtige Aussagen, und die Orchestrierung schließt daraus, dass Vielfalt funktioniert hat. Hängen spätere Aufgaben vom veränderten internen Zustand ab, kann der Fehler nach Ende der Debatte wieder auftauchen.

Der Angreifer brauchte keinen ausgefeilten Exploit. Er behauptete immer wieder eine plausible falsche Antwort. Beharrlichkeit genügte, um die Informationsumgebung zu verändern, in der die gutartigen Agenten ihre Schlüsse zogen. Dadurch erscheint Prompt Injection weniger als einzige Bedrohung und eher als ein Fall eines umfassenderen Problems: Wiederholte Inhalte können die Prämissen umschreiben, die eine Gruppe als geklärt betrachtet.

## Faktenwissen bot keinen Schutz

Das Ausgangswissen sagte die Robustheit nicht voraus. Agenten, die vor der Diskussion richtig antworteten, waren nicht unbedingt diejenigen, die dem Angreifer widerstanden. Andere behielten die richtige Antwort bei, konnten sie aber nicht wirksam verteidigen.

Das schwächt eine weitere bequeme Annahme: Ein stärkeres Modell oder eines, das Fakten besser abruft, wird automatisch zum besseren Prüfer. Prüfen ist eine interaktive Fähigkeit. Es verlangt, Konflikte zu erkennen, Belege unter sozialem Druck zu bewahren und zu entscheiden, wann einem selbstsicheren Gegenüber widersprochen werden sollte.

Rollenspiel-Frameworks für Sprachmodellagenten vergeben häufig Identitäten wie Kritiker, Planer oder Experte. Solche Rollen können eine nützliche Arbeitsteilung erzeugen, doch eine Bezeichnung garantiert keine Unabhängigkeit. Liest jede Rolle dieselbe überzeugende Falschbehauptung und passt ihre Einschätzung in dieselbe Richtung an, hat das Ensemble mehrere Namen, aber einen gemeinsamen Fehlermodus.

Die Studie ist bewusst kontrolliert angelegt. Ihre Angreifer werden gezielt eingeschleust, die Diskussionen betreffen Sachfragen, und die Gruppen aus zehn Agenten bilden nicht jedes Merkmal eines produktiven Arbeitsablaufs ab. Reale Systeme unterscheiden sich bei Modellen, Werkzeugen, Speicher, Sichtbarkeit und Anreizen. Die gemeldeten Prozentwerte beschreiben diese Experimente und sind keine Prognose, dass 44,8 % der eingesetzten Agenten versagen werden.

Kontrollierte Experimente zeigen dennoch einen Mechanismus, gegen den Schutz sinnvoll ist. Eine Mehrheitsentscheidung kann scheitern, weil die Abstimmenden keine unabhängigen Belege mehr liefern. Die Zahl der Agenten lässt die Redundanz größer erscheinen, als sie ist, wenn ihre Überzeugungen während der Diskussion korrelieren.

## Unabhängigkeit statt bloßer Anzahl einplanen

Die praktische Antwort besteht nicht einfach darin, weitere Agenten hinzuzufügen. Drei Angreifer verursachten einen stärkeren Zusammenbruch als einer, und mehr gutartige Teilnehmer helfen nicht, wenn sie alle denselben verunreinigten Kontext aufnehmen. Systeme müssen unabhängige Belege bewahren, bevor Agenten einander beeinflussen.

Ein Ansatz besteht darin, sich vor der Diskussion festzulegen: Jeder Agent dokumentiert Antwort, Quellen und Sicherheit, bevor er Nachrichten anderer sieht. Die Orchestrierung kann diese Festlegungen mit späteren Positionen vergleichen und unerklärte Verschiebungen markieren. Ein anderer Ansatz ist asymmetrischer Zugang: Einige Prüfer untersuchen die Originalbelege, lesen aber nie die Debatte. Ein dritter ist quellenbasierter Widerspruch: Ein Einwand muss auf einen externen Nachweis oder einen ausführbaren Test verweisen und darf nicht bloß eine Behauptung wiederholen.

Die Bewertung interner Zustände ist schwieriger. Betreiber können die Überzeugung eines Modells nicht direkt ablesen, und Tests, die eine Repräsentation entschlüsseln, beweisen nicht, dass das Modell sie verwenden wird. Verhaltenstests können sich der Frage annähern: den Agenten intern mit unterschiedlichen Formulierungen befragen, die gegnerischen Nachrichten entfernen oder eine nachgelagerte Entscheidung testen, deren Antwort von der umstrittenen Tatsache abhängt.

Die Arbeit legt auch eine Anforderung an die Protokollierung nahe. Ein Multi-Agenten-System sollte festhalten, wer eine Behauptung zuerst eingebracht hat, welche Agenten unabhängig auf Belege zugreifen konnten und wie sich Antworten nach jeder Interaktion veränderten. Ohne Herkunftsnachweis kann ein ausgefeilter Konsens verdecken, dass neun scheinbare Stimmen sämtlich auf eine unbelegte Behauptung zurückgehen.

Zurück zum beispielhaften Forschungsteam. Das Protokoll enthält Widerspruch, also glaubt der Betreiber, die Abwehr habe gehalten. Bei der nächsten Aufgabe sollen die Agenten auf Grundlage der umstrittenen Tatsache planen. Mehrere bauen stillschweigend auf der Lüge auf. Das Versagen bestand nicht darin, dass die Gruppe offen die falsche Antwort wählte. Die Diskussion zerstörte vielmehr jene Unabhängigkeit, wegen der sich eine Gruppe überhaupt zusammenzustellen lohnte.

## Quellen


- Huang, L., Zou, H. P., Huang, W.-C., et al. (2026). *Believed but Not Said: Hidden Belief Collapse in Multi-Agent LLM Discussions*. https://arxiv.org/abs/2610.22138
- Li, G., Hammoud, H. A. A. K., Itani, H., Khizbullin, D., & Ghanem, B. (2023). *CAMEL: Communicative Agents for Mind Exploration of Large Scale Language Model Society*. https://arxiv.org/abs/2305.14325
