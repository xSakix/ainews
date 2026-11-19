+++
title = "KI-Tagesüberblick – 19. November 2026"
slug = "ki-tagesueberblick-19-november-2026"
description = "KI-Antworten haben einem langjährigen Berlin-Ratgeber 70 bis 75 % seiner Besuche genommen, während Indeed keine breite KI-Jobapokalypse erkennt. Ein KI-Codeprüfer erhöht die Arbeitslast der Betreuer, und Video-Weltmodelle scheitern an einem grundlegenden Test dauerhafter Zustände."
tags = ["research", "models", "agents", "business"]
date = 2026-11-19T04:03:00+01:00
draft = false
+++

## Die wichtigsten Meldungen

**Laut All About Berlin haben Googles KI-Antworten die Besuche um 70 bis 75 % reduziert.** Nicolas Bouliane betreibt den praktischen Ratgeber seit 2017 und lebt seit 2020 davon. Nach sieben Jahren Wachstum ließen Google AI Overviews die Besuche auf etwa ein Viertel des früheren Niveaus sinken. Eine Aktualisierung vom 18. November berichtet, der Rückgang habe sich fortgesetzt.

Die Website beantwortet Fragen zu Visa, Wohnungen und anderen Bereichen des Lebens in Berlin. Google kann nun eine Antwort oberhalb des Links anzeigen, der die Informationen geliefert hat. Dadurch besuchen weniger Leser die Quelle. Mit den Besuchen sinken Werbe- und Affiliate-Einnahmen, doch die Kosten für Recherche und Pflege der Inhalte bleiben beim Ratgeber.

Quelle: https://nicolasbouliane.com/blog/death-by-ai

**Indeed erkennt keine breite KI-Jobapokalypse, obwohl sich der Anteil der Stellenanzeigen mit KI-Bezug auf 7,2 % verdoppelt hat.** Der Indikator der Stellenplattform stieg von 3,6 % der Anzeigen im September 2025 auf 7,2 % ein Jahr später. Die Zahl der Unternehmen mit mindestens einer KI-bezogenen Anzeige wuchs um 44 %. Dennoch bezeichneten 31 % der befragten Beschäftigten die Einführung bei ihrem Arbeitgeber weiterhin als gering oder nicht vorhanden.

Die regelmäßige Nutzung am Arbeitsplatz stieg von 36 auf 42 %. Diese Nutzer schätzten die wöchentliche Zeitersparnis durch KI auf 2,1 Stunden, gegenüber 2,3 Stunden in der früheren Befragung. Laut Indeed wuchs die US-Produktivität seit Ende 2019 durchschnittlich um 2,1 % jährlich und damit ungefähr im langfristigen Tempo. Die Plattform findet keine verbreiteten Entlassungen, die allein durch KI verursacht wurden. Negative Arbeitgeberbewertungen erwähnten Arbeitsplatzunsicherheit 3,8-mal und Entlassungen 7,1-mal häufiger.

Quelle: https://hiringlab.indeed.com/2026/11/18/there-is-no-ai-jobpocalypse/

**Der automatische Prüfer von GitHub Copilot erhöhte zunächst die Zahl der Pull Requests und die Arbeitslast der Betreuer, später beschleunigte er menschliche Reviews.** Ein Preprint nutzt die Einführung von Copilot Reviewer im Jahr 2025 als natürliches Experiment. Nach dem Start erhielten Projekte deutlich mehr Pull Requests, und die Betreuer hatten zunächst mehr statt weniger Arbeit.

Menschliche Beiträge gingen später zurück, während der Anstieg der Pull Requests von Bots anhielt. Die Betreuer prüften menschliche Arbeit schneller, doch von Bots erzeugte Pull Requests brauchten weiterhin länger bis zur Prüfung und Übernahme. Das Ergebnis trennt zwei Effekte, die übergreifende Produktivitätszahlen oft vermischen: Unterstützung kann eine einzelne Prüfung beschleunigen und zugleich mehr Material erzeugen, das dieselben Personen prüfen müssen.

Quelle: https://arxiv.org/abs/2611.22793

**Google veröffentlichte Gemini 4 Neon für 3 Dollar pro Million Eingabe-Token und 15 Dollar pro Million Ausgabe-Token.** Zwischengespeicherte Eingaben kosten 0,15 Dollar pro Million Token, ein Rabatt von 95 %. Das Modell akzeptiert ein Kontextfenster von einer Million Token. Neon liegt preislich über Carbon und Argon und richtet sich an anspruchsvolle Agenten- und Programmieraufgaben.

Google meldet einen Artificial Analysis Intelligence Index von 61, den zweiten Platz bei Vals mit 70,9 % und 56,3 % bei AutomationBench. Außerdem habe Neon gegenüber Carbon die Kosten pro abgeschlossener Aufgabe bei der standardmäßig hohen Reasoning-Stufe um 32 % gesenkt. In Googles Antigravity-Umgebung erhöhte eine Änderung am Agentenaufbau Neons Ergebnis bei SWE-sweep mini von 12,8 auf 39 %. Alle diese Vergleiche stammen aus Messungen von Google.

Quelle: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/

**Elf Video-Weltmodelle schnitten bei einem Test dauerhafter Zustände schlechter ab als zufällige Auswahl.** Der Flip Test gibt einem Modell zwei Startbilder, die sich in einer Eigenschaft unterscheiden, führt von beiden aus dieselbe Handlung aus und fragt, ob die entstandenen Videos unterschiedlich sein sollten. Die Studie umfasst 1.680 Ausgangsbilder, 25 Aufgaben und mehr als 21.000 Durchläufe in simulierten und realen Szenen.

Das beste System, Gemini Omni Flash 1.1, erreichte eine paarweise Genauigkeit von 18,3 % gegenüber einer Zufallsreferenz von 25 %. Die Modelle änderten ihre Ausgabe bei irrelevanten Unterschieden ungefähr ebenso häufig wie bei entscheidenden. Als die Forscher ausdrücklich den Zustand maßen, statt nur Pixel zu beurteilen, stieg das beste Ergebnis auf 73,7 %. Das deutet darauf hin, dass die Hauptschwäche in der Zustandsrepräsentation liegt und nicht in der sichtbaren Videoqualität.

Quelle: https://arxiv.org/abs/2611.19822

## Neue Modelle und Veröffentlichungen

**Google machte Genie 4 über Project Genie öffentlich zugänglich.** Das System verwandelt ein Bild oder einen Text-Prompt in eine interaktive generierte Welt, durch die sich der Nutzer bewegen kann. Zugang und Demonstrationen kommen von Google. Das Unternehmen stellt die Veröffentlichung als Experiment dar, nicht als Spiel-Engine mit festen Regeln.

Quelle: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/genie-4-now-available-project-genie/

**Microsoft veröffentlichte Aion 1.0, ein Modell mit 2,3 Milliarden Parametern für den Einsatz auf Endgeräten.** Die auf Anweisungen abgestimmten Gewichte sind auf Hugging Face verfügbar. Microsofts Modellkarte liefert die Ergebnisse der Vergleichstests, der Benchmarks, sowie die Nutzungsbedingungen.

Quelle: https://huggingface.co/microsoft/Aion-1.0-Instruct-2.3B

**Google eröffnete eine Warteliste für Stitch Loop, einen Agenten, der Anwendungsoberflächen und Code bearbeitet.** Das Produkt verbindet visuelle Gestaltung und Implementierung in einer fortlaufenden Schleife, statt nur einen einzelnen Entwurf zu erzeugen. Die Angaben zu Verfügbarkeit und Leistung stammen weiterhin von Google selbst.

Quelle: https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-loop/

**Tencent veröffentlichte Hy4 flash mit offenen Gewichten.** Das Hugging-Face-Repository enthält Gewichte, Konfiguration und Nutzungshinweise. Tencent berichtet über die Modellleistung; unabhängige Ergebnisse liegen im Veröffentlichungsmaterial noch nicht vor.

Quelle: https://huggingface.co/tencent/Hy4-flash

**Nvidia brachte RTX-Spark-Desktoprechner für lokale KI-Arbeit in den Verkauf.** Die kompakten Systeme verbinden eine RTX-GPU mit einem Softwarepaket auf Workstation-Niveau, um Modelle am Schreibtisch statt über eine gehostete API auszuführen. Spezifikationen und Leistungsangaben stammen von Nvidia.

Quelle: https://blogs.nvidia.com/blog/rtx-spark-desktop-local-ai-available-now/

## Forschung

**Eine Methode, die Neuronen zu Gemeinschaften gruppiert, fand wiederverwendbare Recheneinheiten in Netzwerken.** Der Preprint behandelt Verbindungen und gemeinsame Aktivierung als Graphen und identifiziert anschließend Gruppen, die bei verschiedenen Eingaben gemeinsam mitwirken. Die Autoren argumentieren, diese Gruppen böten eine stabilere Analyseeinheit als einzelne Neuronen.

Quelle: https://arxiv.org/abs/2611.23112

**Die Lernregel veränderte, wie viele Neuronen denselben durch Grokking erlernten Algorithmus umsetzten.** Die Forscher trainierten Netzwerke bis zum Übergang vom Auswendiglernen zur Verallgemeinerung und verglichen dann ihre internen Schaltkreise. Modelle konnten dieselbe Funktion lernen und dabei die Arbeit unterschiedlich auf Neuronen verteilen.

Quelle: https://arxiv.org/abs/2611.19477

**Agenten entdeckten ohne ausdrückliche Anweisung Wege, ihre eigene Leistung zu verbessern.** Die Experimente gaben den Agenten Rückmeldungen und die Möglichkeit, ihr Vorgehen zu ändern. Die daraus entstandenen Strategien entwickelten sich während wiederholter Arbeit, nicht aus einem von Hand geschriebenen Plan zur Selbstverbesserung.

Quelle: https://arxiv.org/abs/2611.23219

**LLM-Handelsagenten erzielten Erträge durch Marktrisiko statt beständiger Überrenditen.** Der Preprint zerlegt Erträge in Beta, die Vergütung für eingegangenes Marktrisiko, und Alpha, die darüber hinausgehende Leistung. Nach dieser Bereinigung verschwanden die Gewinne der Agenten weitgehend.

Quelle: https://arxiv.org/abs/2611.19530

**Eine Prüfung ergab, dass die meisten als neu beworbenen Architekturmerkmale offener Modelle zuvor schon anderswo erschienen waren.** Die Autoren verfolgten Komponenten zurück und verglichen Aussagen zur Veröffentlichung mit früheren Arbeiten und Implementierungen. Ihr Ergebnis betrifft die Herkunft von Entwurfsentscheidungen, nicht die Leistungsfähigkeit der daraus entstandenen Modelle.

Quelle: https://arxiv.org/abs/2611.20003

**Lineare Sonden ohne Regularisierung wählten häufig Merkmale aus, die das zugrunde liegende Modell nicht nutzte.** Eine Sonde konnte aus einer Repräsentation ein Label vorhersagen und sich dabei auf eine Richtung stützen, die für die Entscheidung des Modells keine kausale Rolle spielte. Das Papier testet Regularisierung und Eingriffe als Kontrollen dagegen, auslesbare Informationen mit einem Nachweis tatsächlicher Berechnung gleichzusetzen.

Quelle: https://arxiv.org/abs/2611.20371

**On-Policy-Distillation veränderte das Verhalten eines Agenten mitunter auf schädliche Weise.** Training auf Abläufen, die die aktuelle Strategie erzeugt, kann die Nachahmung verbessern und zugleich die erhaltenen Verhaltensweisen einschränken oder verschieben. Der Preprint berichtet über Fehler, die allein am Distillationsziel nicht sichtbar waren.

Quelle: https://arxiv.org/abs/2611.19244

**Laut Anthropic half Claude, zwei offene Probleme der Physik schwarzer Löcher zu lösen.** Forscher nutzten das Modell, um mathematische Argumente durchzuarbeiten, und prüften die Ergebnisse anschließend im üblichen Forschungsprozess. Anthropic stellt die Fälle als Zusammenarbeit von Menschen und Modell dar, nicht als autonome Entdeckung.

Quelle: https://www.anthropic.com/research/claude-black-hole-physics

**Centered Ablation machte Eingriffe entlang bestimmter Richtungen stabiler.** Die Methode entfernt eine Richtung relativ zu einer zentrierten Referenz, statt Aktivierungen zu einem beliebigen Ursprung zu zwingen. Laut den Autoren verringert dies unbeabsichtigte Veränderungen beim Test kausaler Hypothesen über Repräsentationen.

Quelle: https://arxiv.org/abs/2611.20148

**Das Ausweichverhalten von Agenten wirkte über Grenzen zwischen Tätigkeiten hinweg fort.** Die Forscher fanden, dass eine in einem Aufgabenteil erlernte oder gewählte Ausweichstrategie bestehen bleiben konnte, nachdem der Agent zu einem anderen Teil gewechselt war. Das erschwert Bewertungen, die jeden Werkzeugaufruf oder jede Phase isoliert betrachten.

Quelle: https://arxiv.org/abs/2611.19886

## Arbeit und Wirtschaft

**KI veränderte, wer in den USA juristische Arbeit erledigt, ohne bislang die Gesamtbeschäftigung zu senken.** Ein Preprint verknüpft die KI-Exposition juristischer Aufgaben mit Veränderungen der beruflichen Zusammensetzung. Er findet eine Umverteilung zwischen Rollen, bevor sich ein klarer Rückgang der Beschäftigtenzahl zeigt.

Quelle: https://arxiv.org/abs/2611.23354

**Stellenanzeigen im Bereich maschinelles Lernen räumten Zusammenarbeit und Kommunikation mehr Gewicht ein, als enge technische Anforderungslisten vermuten lassen.** Die Studie analysierte Fähigkeiten, die Arbeitgeber neben Kenntnissen im maschinellen Lernen verlangten. Laut den Autoren hängt die Einführung von Systemen von der Abstimmung mit Menschen außerhalb der Modellierungsfunktion ab.

Quelle: https://arxiv.org/abs/2611.18915

**KPMG sagt, mehr als 100 Agenten hätten Wirtschaftsprüfern geholfen, bessere Fragen zu stellen.** Der Bericht beschreibt Agenten, die Belege abrufen und vergleichen, während Menschen für Schlussfolgerungen verantwortlich bleiben. Es handelt sich um KPMGs berichtete Erfahrung, veröffentlicht in einem Wirtschaftsmagazin, nicht um eine kontrollierte Evaluierung.

Quelle: https://europeanbusinessmagazine.com/ai-agents-better-questions-kpmg/

**Gemini 4 Neon kostet pro Token mehr als Googles Modelle Carbon und Argon.** Neon kostet 3 Dollar pro Million Eingabe-Token und 15 Dollar pro Million Ausgabe-Token, zwischengespeicherte Eingaben 0,15 Dollar. Teams zahlen damit einen Aufpreis für das Modell, das Google für anspruchsvollere Agentenarbeit positioniert.

Quelle: https://ai.google.dev/gemini-api/docs/pricing

**Epoch schätzt, dass sich Anthropics auf ein Jahr hochgerechnete Rechenausgaben 40 Milliarden Dollar nähern.** Die Schätzung extrapoliert aus Signalen zu Infrastruktur und Modelltraining, statt auf einer Finanzmitteilung des Unternehmens zu beruhen. Sie verortet die Kosten für Spitzenkapazitäten in einer Größenordnung, die nur wenige Unternehmen finanzieren können.

Quelle: https://epoch.ai/data-insights/anthropic-openai-compute-spend-growth

**Die Europäische Zentralbank nannte schuldenfinanzierte KI-Bewertungen als Risiko für die Finanzstabilität.** Ihre Analyse verbindet teure Infrastruktur, Kreditaufnahme und hohe Erwartungen am Aktienmarkt. Enttäuschende Erträge könnten sich daher sowohl über Kreditgeber als auch über öffentliche Märkte ausbreiten.

Quelle: https://www.ecb.europa.eu/press/pr/date/2026/html/ecb.pr261118~83c5c60158.en.html

**Teilnehmer der Federal-Reserve-Sitzung führten enttäuschende Erträge aus KI-Investitionen als Abwärtsszenario auf.** Das Protokoll behandelt dies als Risiko, nicht als Prognose. Die Sorge ist, dass schwächere Erträge Investitionen verringern und Vermögenswerte neu bewerten könnten, deren Preise rasche Produktivitätsgewinne voraussetzen.

Quelle: https://www.federalreserve.gov/newsevents/pressreleases/monetary20261118a.htm

**Epoch schätzt, dass die Kapazität für Agenteninferenz in einem Jahr auf das 4,6-Fache gewachsen ist.** Die Kennzahl erfasst Rechenleistung für lange, wiederholte Modellaufrufe statt für eine einzelne Antwort. Wachstum in diesem Tempo erhöht die Zahl gleichzeitig betreibbarer Agenten bei den Anbietern.

Quelle: https://epoch.ai/data-insights/agentic-inference-capacity-growth

**Die weltweite Roboterdichte erreichte 152 Einheiten je 10.000 Beschäftigte im verarbeitenden Gewerbe.** Die International Federation of Robotics verwendet installierte Industrieroboter und die Beschäftigung im verarbeitenden Gewerbe als Bezugsgröße im Nenner. Die nationalen Durchschnittswerte unterscheiden sich weiterhin stark von diesem globalen Wert.

Quelle: https://ifr.org/downloads/press_docs/DE-2026-NOV-12-IFR_Pressemeldung_Roboterdichte.pdf

## Was Leute bauen

**Eine PlayStation 5 lud ein Mixture-of-Experts-Modell mit 125 Milliarden Parametern laufend von ihrer SSD nach.** Das Projekt betreibt Qwen3.8 Flash Next in 16 GB gemeinsamem Speicher, indem es Gewichte bei Bedarf von NVMe überträgt. Der Autor meldet 49 bis 57 generierte Token pro Sekunde und stellt einen Kontext mit 120.000 Token in etwa einer Sekunde wieder her, statt ihn in 418 Sekunden neu zu berechnen.

Quelle: https://github.com/LaRazaDelSol/AIEngineOnSmallUniMem

**milo-pointer leitet etwa 70 % der Schritte eines Smartphone-Agenten durch ein lokales Modell mit 149 Millionen Parametern.** Die Kaskade übergibt schwierigere Schritte an ein größeres gehostetes Modell. Der Autor meldet Kosten von 2,82 Dollar pro 1.000 Aufgaben gegenüber 9,54 Dollar bei einer reinen Opus-Konfiguration, bei vergleichbaren Aufgabenergebnissen. Die Messungen stammen aus dem Projekt.

Quelle: https://github.com/chayworks/milo-pointer

**smoothstone lässt ein kleines Modell geprüfte, druckbare 3D-Teile aus 16 OpenSCAD-Rezepten zusammensetzen.** Die Verarbeitungskette beschränkt die Generierung auf bekannte geometrische Operationen und validiert die Ausgabe. Der Autor berichtet von 39 korrekten Ergebnissen in 40 Versuchen mit LFM3-1.7B, gegenüber keinem in 15 Versuchen direkter Generierung.

Quelle: https://github.com/baney75/smoothstone

**inside-llm macht Token-Wahrscheinlichkeiten, Sampling-Filter und Abweichungen durch Quantisierung sichtbar.** Mit dem Werkzeug lässt sich untersuchen, wie sich mögliche Token in jeder Phase verändern. Eine optionale Logit-Linse zeigt außerdem, wie Zwischenschichten mögliche nächste Token einstufen.

Quelle: https://github.com/manuelgscom/inside-llm

**Replica erstellt Copy-on-Write-Arbeitsbereiche für Programmieragenten in etwa 100 Millisekunden.** Der Autor meldet auf einem M1 Max ungefähr 958 Millisekunden für eine gewöhnliche Kopie und 3,96 Sekunden für einen frischen Klon. Der Vergleich umfasst ein Projekt und einen Rechner.

Quelle: https://github.com/gabrielvfonseca/replica

**rust-anything prüft schrittweise Neufassungen in Rust gegen aufgezeichnetes Verhalten.** Das Projekt spielte 38.251 erfasste Aufrufe ohne Abweichung erneut ab und meldet Beschleunigungen bis zum Faktor 20. Der Autor weist darauf hin, dass der Zusatzaufwand kleine Funktionsaufrufe verlangsamen kann.

Quelle: https://github.com/erkamyaman/rust-anything

**Signet erfasst Belege sowie Prüf- und Freigabestatus für Agenten und Skills.** Das Register nutzt SHACL-Validierung, signierte Datenhüllen und Merkle-Nachweise und behält einen menschlichen Freigabeschritt bei. Es ist eine Grundlage für Governance, kein autonomer Richter.

Quelle: https://github.com/therandomsecurityguy/signet

**DeepMind veröffentlichte Robotik-Skills für Programmieragenten.** Das Plugin lässt einen Agenten Steuerungen schreiben, sie in MuJoCo testen und anschließend freigegebenen Code auf physische Roboterarme übertragen. Das Repository liefert den Ablauf und Beispiele.

Quelle: https://github.com/google-deepmind/robotics-antigravity-plugin

## Lesenswert

**Anthropic erklärt, wie sich Sicherheitsbewertungen entwickeln lassen, die dauerhaft das beabsichtigte Verhalten messen.** Der technische Leitfaden behandelt Bedrohungsmodelle, Aufgabenkonstruktion, Bewerter und Kontrollen, die verhindern, dass ein Benchmark zu einem einfacheren Ersatzmaß abdriftet. Er versteht die Bewertung als gepflegtes Instrument, nicht als feste Sammlung von Prompts.

Quelle: https://www.anthropic.com/engineering/building-strong-safety-evaluations

**Expert Streaming betreibt ein Mixture-of-Experts-Modell mit 180 Milliarden Parametern auf einem Mac mit 32 GB Speicher.** Die Implementierung hält inaktive Experten außerhalb des Hauptspeichers und überträgt sie, wenn das Routing sie auswählt. Geringerer Speicherbedarf wird mit Speicherzugriffen und Latenz erkauft.

Quelle: https://huggingface.co/blog/moe-expert-streaming

**Gemessene Fine-Tuning-Läufe dauerten länger, als Schätzungen allein anhand der FLOPs vorhersagten.** Der Bericht trennt arithmetischen Durchsatz vom Laden der Daten, Kommunikation und Orchestrierung. Die Methode nutzt beobachtete Läufe, um Schätzungen zu verbessern, bevor ein Team Hardware reserviert.

Quelle: https://huggingface.co/blog/Dharma-AI/predicting-fine-tuning-time

**Ein Reverse Engineer entwickelte ein Belegprotokoll für die Arbeit mit Sprachmodellen.** Der Ablauf erfasst Hypothesen, Experimente und widerlegende Ergebnisse, damit ein Agent nicht wiederholt denselben Weg neu entdeckt. Der Artikel demonstriert die Methode an Reverse-Engineering-Aufgaben, statt sie als automatisierte Lösung darzustellen.

Quelle: https://www.slowchronicle.com/posts/llm-assisted-reverse-engineering

## Hacker News

**Entwickler berichteten, dass sich die Latenz von Gemini 4 Carbon in Agentenabläufen aufsummiert.** Einzelne Pausen, die im Chat akzeptabel erscheinen, verursachen größere Kosten, wenn ein Agent viele Modellaufrufe nacheinander ausführt. Der Thread besteht aus Praxisberichten, nicht aus einem kontrollierten Benchmark.

Quelle: https://news.ycombinator.com/item?id=50541790

## YouTube

**Die Entwickler von Terminal-Bench erklärten, wie Labore Agenten an echter Terminalarbeit testen.** Der englischsprachige Vortrag behandelt die Konstruktion von Aufgaben, reproduzierbare Umgebungen und Bewerter, die das Ergebnis statt der Erklärung des Agenten prüfen. Er erörtert auch, wie die Wahl der Ausführungsumgebung den Modellscore beeinflussen kann.

Quelle: https://www.youtube.com/watch?v=7GW-9ug2nvw

**Eine Stanford-Vorlesung zerlegte KI-Kosten in Token, Energie und Modellwahl.** Die englischsprachige Veranstaltung zeigt, wie das Profil der Arbeitslast und Entscheidungen zur Bereitstellung die Rechnung verändern. Sie behandelt den Modellnamen als einen Faktor der Kosten, nicht als die gesamte Berechnung.

Quelle: https://www.youtube.com/watch?v=U92J5mCDLMc

**Daniel Susskind argumentierte, Kinder sollten lernen, KI kritisch zu nutzen, statt sie zu meiden.** Das englischsprachige Interview trennt Unterstützung von dem Urteilsvermögen, das zur Bewertung einer Antwort nötig ist. Die Empfehlungen sind Susskinds Argumentation, keine Wirkungsstudie.

Quelle: https://www.youtube.com/watch?v=nZvsuU0-F5Y

## Kurz notiert

**KI-gestützte Sicherheitsteams fanden kritische Schwachstellen in der HTTP/2-Verarbeitung von NGINX.** Wiz beschreibt Fehler, die zur Ausführung fremden Codes aus der Ferne führen können, und nennt betroffene Konfigurationen und Korrekturen. Die Forscher nutzten KI bei der Untersuchung, während Schwachstellen und Patches mit herkömmlicher Sicherheitsarbeit geprüft wurden.

Quelle: https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities

**Angreifer kaperten Microsofts Python-Paket für ein Agenten-Framework auf PyPI.** Die bösartige Version verbreitete Schadsoftware unter einem vertrauenswürdigen Paketnamen. Nutzer des Pakets sollten Microsofts Maßnahmen zur Behebung befolgen und installierte Versionen prüfen.

Quelle: https://www.theregister.com/security/2026/11/18/microsofts-official-python-agent-framework-hijacked-to-distribute-malware/5310858

**KI-gestützte Forschung fand einen kritischen Base64-Fehler in OpenJDK.** Oracle veröffentlichte eine Korrektur für den Fehler, der Anwendungen Dritter betreffen kann, die von der verwundbaren Implementierung abhängen. Die Entdeckungsmethode ändert nichts daran, dass betroffene Java-Installationen aktualisiert werden müssen.

Quelle: https://www.theregister.com/security/2026/11/18/oracle-reveals-fix-this-asap-grade-java4shell-bug-that-allows-attacks-on-many-third-party-apps/5310661

**CreditNirvana legte Daten von 6,6 Millionen Konten und 315.000 Gesprächsaufzeichnungen offen.** Der Dienst unterstützt KI-basiertes Inkasso. Damit betrifft der Vorfall sowohl strukturierte Finanzdaten als auch Gespräche. Wired berichtet die Zahlen aus dem offengelegten System.

Quelle: https://www.wired.com/story/ai-debt-collection-service-exposed-66-million-accounts-and-315000-call-recordings/

**Waymo setzte nach Maßnahmen kalifornischer Behörden fahrerlose Autobahnfahrten aus.** Der Eingriff folgte auf Vorfälle auf Autobahnen und nimmt einen Bereich mit höherem Tempo aus dem Angebot, während das Problem bearbeitet wird. Er beendet nicht Waymos fahrerlosen Betrieb bei niedrigerem Tempo.

Quelle: https://www.theregister.com/security/2026/11/18/california-tells-waymo-to-take-the-next-exit-after-freeway-mishaps/5310841

**Mehr Banken machen Kunden für Handlungen haftbar, die sie an KI-Agenten delegieren.** Die Bedingungen verlagern Betrugs- und Fehlerrisiken, wenn ein Kunde einem Agenten Kontozugriff gewährt. Dadurch kann ein Nutzer weniger Schutz haben als bei einer unautorisierten Transaktion ohne eine solche Delegation.

Quelle: https://techcrunch.com/2026/11/18/more-banks-says-customers-using-ai-agents-are-on-their-own-even-if-they-get-hacked/

## Wirtschaft in Kürze

**Anthropic setzte den Preis seines Börsengangs auf 83 Dollar je Aktie fest.** Quelle: https://www.anthropic.com/news/anthropic-prices-initial-public-offering
