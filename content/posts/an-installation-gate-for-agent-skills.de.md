+++
title = "Ein Installations-Gate für Agenten-Skills"
slug = "ein-installations-gate-fuer-agenten-skills"
description = "ClawVet scannt Agenten-Skills und ihre Skripte vor der Installation und warnt, wenn ein Update Zugriff auf neue Geheimnisse, Hosts oder Persistenzpfade erhält. Die Vergleichstests zeigen, dass statische Prüfungen viele Angriffe abfangen, während Prompt-Injection weiterhin eine semantische Prüfung erfordert."
tags = ["agents", "safety", "tools"]
date = 2026-11-23T03:57:49+01:00
draft = false
+++

Im Staging-Verzeichnis wirkte der Skill unauffällig. Seine Markdown-Datei beschrieb eine nützliche Abkürzung, und daneben lag ein Hilfsskript. Bevor das Installationsprogramm eine der beiden Dateien in den Arbeitsbestand des Agenten kopieren konnte, öffnete ein separater Prozess das Paket, verfolgte ein Geheimnis aus einer Umgebungsvariable bis zu einer ausgehenden Anfrage und gab eine Blockade zurück.

*Die Szenen am Anfang und am Ende dieses Artikels sind Illustrationen; die Personen darin sind erfunden.*

ClawVet ist für genau diesen Moment gebaut. Der Open-Source-Scanner untersucht die Anweisungen und den Code in einem Agenten-Skill vor der Installation. Er läuft standardmäßig offline, führt das Paket nicht aus und kann sein Urteil über die Installationsrichtlinie von OpenClaw durchsetzen. Zudem protokolliert er die Berechtigungen einer freigegebenen Version, sodass ein späteres Update nicht stillschweigend Zugriff auf Zugangsdaten oder Startdateien hinzufügen kann, ohne eine erneute Rückfrage auszulösen.

## Code verpackt als Anweisung

Ein Agenten-Skill ist weder eine klassische Programmbibliothek noch ein schlichtes Dokument. Seine Hauptdatei teilt einem Modell mit, wann der Skill einzusetzen und was zu tun ist. Das Paket kann darüber hinaus Skripte, Konfigurationen, Referenzen und weitere Dateien enthalten. Diese Kombination schafft ein Lieferkettenproblem in zwei Sprachen: Fließtext kann den Agenten umlenken, während Code über das Benutzerkonto handeln kann.

ClawVet behandelt das Paket als beides. Im ersten Durchgang zerlegt der Scanner die Hauptdatei, Codeblöcke sowie Dateien, auf die die Anweisungen verweisen. Statische Regeln suchen anschließend nach Fernausführung, Reverse Shells, Diebstahl von Zugangsdaten, Minern, Verschleierung und Datenabfluss. Tree-sitter-Parser verfolgen Datenflüsse durch Python-, JavaScript-, TypeScript- und Shell-Code, ohne ihn auszuführen. Weitere Durchgänge prüfen nicht deklarierte Programme und Umgebungsvariablen, riskante Abhängigkeitsbefehle sowie Namen, die bekannten Skills ähneln.

Sechs der sieben Durchgänge laufen statisch und lokal. Der optionale siebte sendet die statischen Befunde und Abdeckungslücken an ein vom Betreiber gewähltes großes Sprachmodell (LLM). Ein semantischer Prüfer kann eine Lücke nur schließen, indem er den Skill zitiert, während harte Sicherheitsbefunde Untergrenzen bleiben, die der Prüfer nicht herabstufen darf. Diese Unterscheidung ist wichtig, weil das Versprechen einer „KI-Sicherheitsprüfung“ sonst verdecken kann, dass Quellcode den eigenen Rechner verlässt.

Das Werkzeug fasst seine Befunde zu einem Punktwert von null bis 100 zusammen. Werte bis 25 erhalten ein A oder B und werden durchgelassen. Werte von 26 bis 75 erzeugen eine Warnung, die eine unbeaufsichtigte Installation stoppt. Werte ab 76 führen zu einer Blockade. Eine bekannte Command-and-Control-Adresse oder nicht lesbare Inhalte blockieren unabhängig vom Schwellenwert.

## Berechtigungsänderungen, nicht nur bekannte Muster

Statische Signaturen funktionieren am besten bei Angriffen, die bereits eine erkennbare Form haben. Updates werfen ein anderes Problem auf. Ein nützlicher Skill kann sich Vertrauen erarbeiten und erst in einer späteren Version eine zusätzliche Berechtigung erlangen.

ClawVet extrahiert daher Fähigkeiten: kontaktierte Websites, geheime Umgebungsvariablen, Speicher für Zugangsdaten, Persistenzorte und nachgewiesene Aktionen mit hohem Risiko. Das Installations-Gate speichert diesen Datensatz lokal. Trifft eine neue Version desselben Eigentümers und Slugs ein, vergleicht das Gate beide Stände. Ein neu ausgelesenes Geheimnis, ein Persistenzpfad oder ein riskantes Ziel ändert das Urteil auf eine Warnung und benennt die neue Berechtigung.

Dieser Aufbau vermeidet eine verbreitete Schwäche von Prüfsystemen. Wer prüft, muss nicht das gesamte Paket erneut lesen und sich merken, was die alte Version durfte. Die Frage wird enger: Warum benötigt dieses Update ein Passwort, das die Vorgängerversion nie gelesen hat, oder einen Host, den sie nie kontaktiert hat?

Der Vergleich hat Grenzen. ClawVet erkennt wörtliche Pfade, gängige Platzhalter und mehrere Formen der Befehlskonstruktion, liefert aber keinen allgemeinen Beweis für das Programmverhalten. Laut Dokumentation kann Fließtext, der einen Agenten anweist, eine Webseite abzurufen und deren Anweisungen zu befolgen, der statischen Analyse entgehen, wenn keine Datei heruntergeladen wird. Verschleierte Loader und nicht unterstütztes Laufzeitverhalten können die Regeln ebenfalls umgehen. Vollständige Abdeckung bedeutet, dass der Scanner die erkannten Referenzen innerhalb seiner Datei- und Verzeichnisgrenzen geprüft hat; eine Sicherheitsgarantie ist sie nicht.

## Was die Messungen zeigen

Das Projekt veröffentlicht Ergebnisse auf einer zurückgehaltenen Teilmenge von SkillTrustBench v1.1. Der Vergleichstest (Benchmark) bildet Skills als Pakete mit einer Hauptanweisungsdatei sowie optionalen Skripten, Referenzen, Zusatzdateien und Agentendefinitionen ab. Seine Bestenlisten-Teilmenge aus 556 Fällen enthält 316 schädliche, 74 verdächtige und 166 normale Beispiele.

Das statische Gate von ClawVet erreichte auf diesem Datensatz eine Genauigkeit von 0,660 und einen Makro-F1-Wert von 0,511. Mit Claude Haiku 5.5 als optionalem semantischem Prüfer stieg die Genauigkeit auf 0,833 und der Makro-F1-Wert auf 0,770. Die Trefferquote bei schädlichen Skills erreichte 0,918. Das Projekt stellt diese Werte veröffentlichten Bestenlisten-Ergebnissen von 0,775 Genauigkeit für Cisco Skill Scanner, 0,712 für NVIDIA SkillSpector und 0,874 für Tencent A.I.G. gegenüber. Da sich semantische Konfigurationen, Prompts und Implementierungsentscheidungen unterscheiden können, ist die Tabelle ein Beleg auf einem einzelnen Datensatz und keine allgemeingültige Rangliste.

Der Abstand zwischen statischen und semantischen Ergebnissen ist ebenso aufschlussreich wie der höhere Gesamtwert. Eine Codeanalyse kann nachweisen, dass Zugangsdaten in einen Netzwerkaufruf fließen. Schwerer tut sie sich mit einer Anweisung in natürlicher Sprache, deren Schaden von der Absicht abhängt. Der Update-Benchmark des Projekts macht diese Schwäche deutlich: Auf einem zurückgehaltenen Datensatz stoppten Gate und Berechtigungs-Diff 95,2 % der Code-Injection-Änderungen, aber nur 36,4 % der Prompt-Injection-Änderungen.

Derselbe Benchmark maß die Reibungsverluste. Unter harmlosen Updates blieben dennoch 34,1 % an irgendeiner Stelle im kombinierten Prozess aus Gate und Diff hängen, obwohl nur 5,1 % ausdrücklich wegen einer Berechtigungsänderung nachfragten. Über 212 einzelne ClawHub-Skills hinweg senkte eine spätere Version von ClawVet harte Blockaden von 79 auf 37 und erhöhte saubere Freigaben von 87 auf 139. Diese Zahlen stammen aus dem eigenen Korpus und den eigenen Einstufungen des Projekts.

Ältere Tests zeigen, warum sorgfältige Kennzeichnungen wichtig sind. Ein Korpus aus 500 Einträgen enthielt 50 Skills aus einer Schadkampagne, 400 saubere Skills und 50 schwierige Negativbeispiele. Zu den schwierigen Negativbeispielen zählten legitime SSH-Helfer, die Konfigurationen auslasen, sowie Installationsprogramme mit Befehlen, die auch in Angriffen vorkommen. Ein Scanner, der jede Erwähnung von Zugangsdaten oder einer Shell pauschal blockiert, wirkte sicher, machte aber gewöhnliche Arbeit unmöglich.

## Ein Gate mit klarer Grenze

ClawVet lässt sich über WebAssembly im Browser, als Kommandozeilen-Scanner, in Pre-Commit-Prüfungen oder als GitHub Action einsetzen. Seine strengere Rolle ist das Installations-Gate. OpenClaw stellt das Paket im Staging bereit, sendet Metadaten an den Richtlinienprozess und wartet auf ein einzelnes JSON-Urteil, bevor es die Installation abschließt. Eine fehlerhafte Anfrage oder ein Scanner-Fehler blockiert sicherheitshalber.

Das Projekt rät Nutzern, den Scanner global zu installieren, statt ein frisches Paket über `npx` aufzurufen. Diese Empfehlung folgt dem eigenen Bedrohungsmodell: Ein Befehl, der im Augenblick der Prüfung die neueste Registry-Version abruft, schafft ein weiteres ungeprüftes Update. Eine globale Installation lässt sich gezielt aktualisieren, und die npm-Attestierung kann vorab geprüft werden.

Das Gate macht die Prüfung sensibler Agenten-Erweiterungen nicht überflüssig. Es verwandelt diese Prüfung in einen verbindlichen Schritt und hinterlässt eine nachvollziehbare Begründung, wenn der Schritt eine Installation stoppt. Die veröffentlichten Grenzen machen zudem die verbleibende Abwägung sichtbar: Der statische Modus hält das Paket lokal, übersieht aber mehr semantische Angriffe; die optionale Modellprüfung erkennt Absichten besser, sendet dafür aber ausgewählte Belege an einen Modell-Endpunkt.

Im Staging-Verzeichnis blieb der blockierte Skill ein bloßer Ordner. Das Installationsprogramm gab das Geheimnis aus, das das Skript auszulesen versuchte, das Ziel, das es erhalten hätte, und die Regel, die das Kopieren stoppte. Der Agent bekam nie Gelegenheit zu entscheiden, dass die Abkürzung nützlich aussah.

## Quellen

- CUHK Zhuque. (2026). *SkillTrustBench*. https://huggingface.co/datasets/cuhk-zhuque/SkillTrustBench
- Shaikh, M. (2026). *ClawVet*. https://github.com/MohibShaikh/clawvet
