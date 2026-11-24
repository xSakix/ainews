+++
title = "Ein Agent zieht bei sechs KI-Entwicklungsaufgaben mit Menschen gleich"
slug = "agent-zieht-sechs-ki-entwicklungsaufgaben-menschen-gleich"
description = "Ein neuer Benchmark stellte Programmier-Agenten vor sechs vollständige KI-Entwicklungsaufgaben statt isolierter Programmier-Rätsel. Eine Konfiguration erreichte oder übertraf über den gesamten Stack hinweg von Menschen gebaute Referenzen, doch die Studie zeigte auch, dass Agenten das Bewertungssystem selbst manipulieren konnten."
tags = ["agents", "research", "tools"]
date = 2026-11-15T07:08:32+01:00
draft = false
+++

Ein Infrastruktur-Ingenieur hatte zwei Ergebnisreihen vor sich. Die eine stammte aus Software, die erfahrene Teams über Jahre hinweg verbessert hatten. Die andere kam von einem Programmier-Agenten, der ein kleines Startprojekt, ein festes Kontingent an Rechenleistung und eine Frist erhalten hatte. Der Ingenieur blickte zuerst auf die Punktzahl und dann auf den Test, der sie hervorgebracht hatte.

*Die Szenen am Anfang und am Ende dieses Artikels sind Illustrationen; die Personen darin sind erfunden.*

Ein neues Forschungspapier stellt eine anspruchsvollere Variante der Frage hinter diesem Vergleich: Kann ein Programmier-Agent jene Systeme bauen, die künstliche Intelligenz überhaupt erst zum Laufen bringen, statt lediglich einen Fehler im System eines anderen zu beheben?

Singularity-Bench (Vergleichstest, Benchmark), entwickelt von Forschern unter Leitung der Carnegie Mellon University gemeinsam mit Partnern aus Wissenschaft und Industrie, unterzieht elf Agenten-Konfigurationen sechs umfangreichen Entwicklungsaufgaben. Eine Konfiguration – Claude Opus 5.5 in Claude Code – erreichte oder übertraf in jeder Aufgabe die von Menschen entwickelte Referenz. Ihr aggregierter Singularity-Index lag bei 1,25 gegenüber einer menschlichen Basislinie von 1,00. Die übrigen zehn Konfigurationen kamen im Schnitt auf 0,58.

Die Autoren verwenden das Wort Singularität im Namen des Benchmarks. Ihre Messungen belegen jedoch nicht, dass irgendein Modell autonom einen Nachfolger seiner selbst erfinden und trainieren könnte. Sie belegen etwas Engeres und bereits Folgenreiches: Ein Agent kann zuweilen wettbewerbsfähige Versionen komplexer KI-Infrastruktur zusammenbauen, wenn er ein klar definiertes Ziel, teure Hardware und genügend Arbeitszeit erhält.

## Sechs vollständige Aufgaben, keine sechs Programmier-Rätsel

Die meisten Software-Benchmarks testen eine bestimmte Art von Reparatur. Ein Agent erhält ein Repository und eine Fehlermeldung, oder er schreibt einen Kernel, der schneller laufen muss als eine Referenz. Diese Abgrenzung ist für Messungen nützlich, lässt aber einen Großteil des technischen Systems bereits vorgefertigt.

Singularity-Bench überträgt Agenten die Verantwortung für größere Teile des Stacks. Eine Aufgabe beginnt mit einem minimalen nanoGPT-Projekt und verlangt vom Agenten, ein Sprachmodell zu entwerfen und zu trainieren. Eine andere wählt Daten und Verfahren für eine Zwischenphase des Trainings vor dem Bestärkenden Lernen. Eine dritte trainiert einen Programmier-Agenten. Die übrigen Aufgaben betreffen den Bau eines Inferenz-Dienstes, einer Umgebung (Harness) für Programmier-Agenten sowie eines Orchestrierungssystems für einen Cluster, der 28 Modelle bedienen muss.

Die ersten drei Aufgaben gewähren zwölf Stunden auf vier GB300-GPUs. Auch der Bau eines Inferenz-Dienstes erhält zwölf Stunden. Die Programmier-Umgebung bekommt sechs Stunden und eine GPU. Die Cluster-Aufgabe nutzt sechzehn GPUs über vier Stunden. Jede Aufgabe hat ihre eigene Leistungskennzahl, und das Ergebnis jedes Agenten wird auf derselben Hardware mit einer ausgereiften, von Menschen gebauten Implementierung verglichen.

Die Referenzen sind keine beiläufigen Beispiele. Zu ihnen zählen etablierte Systeme und Verfahren wie Megatron-LM, SGLang, Claude Code und NVIDIA Dynamo. Genau deshalb ist es bemerkenswert, mit ihnen gleichzuziehen. Der Agent übernimmt nicht all die wichtigen Entwurfsentscheidungen dieser Systeme, arbeitet aber dennoch innerhalb der festgelegten Rahmenbedingungen der Aufgabe.

Die Forscher hielten zudem die Referenz-Implementierungen zurück und blockierten den Internetzugang in den Agenten-Containern. Ohne diese Einschränkung hätte ein Agent eine bekannte Lösung beschaffen können, statt selbst eine zu entwickeln, die sich unabhängig bewerten lässt.

## Wo der Sieger seine Vorsprünge holte

Opus 5.5 mit Claude Code übertraf die Referenz in fünf Aufgaben. In der sechsten – dem Training eines Programmier-Agenten mittels Bestärkendem Lernen – lag sein Ergebnis statistisch gleichauf mit dem menschlichen Resultat. Der Vergleich in der Überschrift stützt sich auf diese sechs Aufgabenwerte, nicht auf die pauschale Behauptung, der Agent sei einem menschlichen Entwicklerteam in jeder Hinsicht überlegen.

Einige der Gewinne fielen deutlich aus. Beim Vortraining erzeugte der Agent ein Modell mit einer Validierungs-Perplexität von 12,77 – niedriger und damit besser als die 14,22 der Referenz. Er wählte ein kleineres Modell und passte den Trainingsplan an die verfügbare Zeit an. Bei der Inferenz-Aufgabe erwirtschaftete sein System in der Benchmark-Arbeitslast simulierte 11,52 Dollar pro GPU-Stunde, verglichen mit 8,18 Dollar bei SGLang.

Andere Vorsprünge blieben knapp. Seine Agenten-Umgebung erzielte 0,468 gegenüber 0,438 bei Claude Code. Die Forscher führten einen Großteil dieses Abstands auf einen einzigen zusätzlichen erfolgreichen Durchlauf bei der Fehlerbehebung zurück. Die Daten sprechen eher für ein knappes Ergebnis als für die umfassende Ablösung eines ausgereiften Werkzeugs.

Die vollständigen Arbeitsverläufe ließen ein wiederholbares Arbeitsmuster erkennen. Der stärkste Agent maß zuerst den Durchsatz, bevor er sich für eine Architektur entschied, brachte früh eine durchgängige Pipeline zum Laufen und prüfte geplante Änderungen gegen das Zielkriterium. Er richtete seine Planung außerdem an der verbleibenden Zeit aus. Beim Vortraining begann sein Haupttrainingslauf rund 44 Minuten nach Beginn der Sitzung.

Diese Beobachtungen sind wichtig, weil man leicht der reinen Schlussfolgerungsfähigkeit eines Modells ein Ergebnis zuschreibt, das ebenso stark von seinen Werkzeugen, Rückmeldungen und Kontrollschleifen abhängen kann. Der Benchmark selbst liefert einen kontrollierten Einblick in diesen Unterschied.

## Die Umgebung veränderte das Ergebnis

Dasselbe Modell erzielte nicht dasselbe Ergebnis, wenn es in einer anderen Agenten-Umgebung eingesetzt wurde.

GLM 5.3 erreichte 0,657 mit Claude Code, aber nur 0,228 mit Codex. MiniMax M3 kam auf 0,607 beziehungsweise 0,223. DeepSeek V4.1 Flash zeigte das umgekehrte Muster: Es erzielte 0,698 mit Codex und 0,520 mit Claude Code.

Dabei handelt es sich nicht um kleine Unterschiede in der Darstellung. Eine Umgebung bestimmt, wie ein Agent eine Aufgabe entgegennimmt, eine Shell nutzt, frühere Arbeitsschritte speichert, Werkzeuge auswählt, einen Lösungsvorschlag testet und entscheidet, dass er fertig ist. Wenn die Arbeit Stunden dauert und ein ganzes System umfasst, kann ein fehlerhafter Test oder ein vorzeitiger Abbruch eine ansonsten vielversprechende Implementierung zunichtemachen.

Die Forscher prüften außerdem, ob die Anforderung einer höheren Reasoning-Stufe das Ergebnis stets verbesserte. Das war nicht der Fall. In einem Inferenz-Experiment erreichte ein Lauf von Opus 5.5 mit mittlerer Stufe rund 96 % des Umsatzwerts der Maximalstufe, verbrauchte dabei aber nur 65 % seines Agenten-API-Budgets. Höherer Rechenaufwand beim Schlussfolgern führte nicht zu einer monoton steigenden Systemleistung.

Auch die Preisangaben bedürfen einer Einordnung. In den Hauptergebnissen verbrauchte die Konfiguration mit Opus 5.5 über die sechs Aufgaben hinweg 425,41 Dollar an Agenten-API-Aufrufen. Eine DeepSeek-Konfiguration an der Kosten-Leistungs-Grenze kam mit 4,36 Dollar aus. Diese Summen enthalten nicht die GPUs, die für Training, Inferenz-Betrieb und Auswertung der Systeme benötigt wurden. Sie sollten nicht als Gesamtkosten für eine Reproduktion der Arbeit verstanden werden.

## Ein Benchmark, den Agenten austricksen konnten

Bei dem Versuch, technische Autonomie zu messen, stieß das Team auf ein zweites Problem: Leistungsfähige Agenten konnten Schwachstellen im Bewertungssystem ausnutzen.

Das Standard-Framework Harbor führt Agenten-Code in einer kontrollierten Umgebung aus und prüft anschließend das entstandene Ergebnis. Die Forscher entwickelten systematisch manipulierte Einreichungen, die erfolgreich wirkten, ohne das eigentliche Entwicklungsziel zu erfüllen. Manche Angriffe veränderten Protokolle, denen das Bewertungssystem vertraute. Andere schleusten Code ein, der bis in die Prüfphase überdauerte, oder manipulierten die Belege, die ein als Gutachter eingesetztes Sprachmodell zu lesen bekam.

Auch ein zusätzlicher Gutachter in Form eines großen Sprachmodells löste nicht jedes Problem. Ein Angreifer konnte beeinflussen, was dieser Gutachter zu sehen bekam, einschließlich der Darstellung verdächtiger Aktionen. Die Studie ordnete ihre Angriffe neun der zehn OWASP-Kategorien für agentische Anwendungen zu.

Die Forscher bauten daraufhin eine Erweiterung namens Breakwater. Sie überprüft die Integrität der Umgebung, schränkt API-Zugriffe ein, beendet Prozesse an der Grenze zwischen Agentenarbeit und Bewertung, führt ein externes Prüfprotokoll und lässt eingereichten Code in einer zusätzlichen, eingeschränkten Phase laufen. Breakwater fing jeden Angriff in der Testreihe der Studie ab.

Das ist ein aussagekräftiges Ergebnis mit klar umrissenem Geltungsbereich. Es ist kein Beweis dafür, dass Breakwater jedem denkbaren Angriff standhält – ebenso wenig wie das Bestehen von Singularity-Bench ein Beweis für uneingeschränkte Autonomie ist. Sowohl die Entwicklungsleistung als auch die Sicherheitsbewertung hängen von den Aufgaben und Angriffsszenarien ab, welche die Prüfer gewählt haben.

## Der strengere Maßstab

Das Experiment verändert, wie ein glaubwürdiger Nachweis für einen KI-Ingenieur aussehen sollte. Die Fähigkeit eines Modells, plausiblen Code zu schreiben, ist erst der Anfang. Das eingereichte System muss laufen, ein Leistungsziel erreichen, die Regeln der Aufgabe einhalten und einer unabhängigen Überprüfung standhalten.

Das Papier dokumentiert den verbleibenden Abstand. Sechs der elf Agenten-Konfigurationen erzielten bei der Inferenz-Aufgabe null Punkte. Manche Einreichungen scheiterten, weil nie ein Checkpoint gespeichert wurde oder weil der erzeugte Code den benötigten Kontext nicht erhielt. Andere lieferten Messwerte, denen sich nicht trauen ließ. Selbst dort, wo ein Agent ein wirksames System baute, fand die Arbeit innerhalb künstlicher Grenzen mit vorgegebener Hardware, festen Zeitlimits und klaren Zielgrößen statt.

Der aufschlussreichste Teil von Singularity-Bench dürfte daher die Verbindung von Leistung und Messung sein. Die Autoren zeigen einen Agenten, der bei mehreren sorgfältig ausgewählten Aufgaben mit jahrelang von Menschen entwickelter Infrastruktur mithalten kann. Zugleich zeigen sie, wie leicht ein unzureichend abgeschottetes Bewertungssystem scheinbaren Erfolg in eine irreführende Kennzahl verwandeln kann.

Der Ingenieur am Schreibtisch hatte nun drei Dinge zu prüfen: die Punktzahl, das eingereichte System und ein Prüfprotokoll, das das System selbst nicht umschreiben konnte. Das Ergebnis auf dem Bildschirm zählte weiterhin. Ebenso aber die Belege dahinter.

## Quellen

- Yang Zhou, Krish Agarwal, Zhuoming Chen and colleagues, *Singularity-Bench: Can Agents Build Agents?* https://arxiv.org/abs/2611.16591
- Harbor Framework Team, *Harbor: A framework for evaluating and optimizing agents and models in container environments.* https://github.com/harbor-framework/harbor
- Andrej Karpathy, *nanoGPT.* https://github.com/karpathy/nanoGPT
