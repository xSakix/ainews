+++
title = "KI fand 9.791 mögliche Fehler, 99 Meldungen erreichten die Projekte"
slug = "ki-fand-9791-moegliche-fehler-99-meldungen-fuer-projekte"
description = "GitHub und Microsoft prüften in einem Pilotprojekt sechs Open-Source-Projekte mit KI und meldeten den Verantwortlichen nur Funde, die eine Vorauswahl und eine Prüfung von Hand bestanden hatten. 55 der 99 gemeldeten Fehler sind behoben, und das Projekt zeigt, wer den Aufwand für die Auswahl trug."
tags = ["safety", "community", "tools"]
date = 2026-11-22T03:14:11+01:00
draft = false
+++

Zwei Personen betreuen ImageMagick. Im Pilotprojekt erhielten sie 22 Sicherheitsmeldungen. Eine davon sah aus wie ein Fall, den sie schon kannten. Die Zusammenfassung machte deutlich, dass es sich um einen anderen Fehler handelte, und verwies auf die genauen Codezeilen. Nach 15 Minuten hatten die Verantwortlichen eine Korrektur veröffentlicht. Normalerweise brauche man für einen Sicherheitshinweis „im Durchschnitt etwa 30 Minuten bis eine Stunde, um ihn zu lesen, zu verstehen und eine Korrektur zu schreiben“, sagte ein Mitglied des ImageMagick-Teams später.

Das ist eine kleine Zeitersparnis, von der diejenigen berichten, die sie erzielt haben. Sie steht am Ende eines Verfahrens, das mit einer weit größeren Zahl begann.

## Wie der Versuch ablief

Am 17. November beschrieben Ashley Wolf und Gregg Cochran von GitHub ein gemeinsames Pilotprojekt mit Microsoft für sechs Open-Source-Projekte: AutoGPT, Caddy, Express, FastMCP, ImageMagick und Netty. Microsofts Prüfsystem Codename MDASH untersuchte zusammen mit dem Modell MAI Cyber jede Codebasis und schlug für seine Funde Korrekturen vor. Die Ergebnisgrafik nennt für die sechs Projekte insgesamt 9.791 mögliche Fehler.

Keiner dieser Funde ging direkt an die Projektverantwortlichen. Ein vom GitHub Security Lab entwickelter KI-Agent entfernte Duplikate, prüfte die Stichhaltigkeit und behielt Fehler mit gravierenden Auswirkungen. Anschließend kontrollierten Forscher aus Microsofts FORGE Lab jeden verbliebenen Fund von Hand. Sieben von ihnen verbrachten damit etwa zwei Tage pro Projekt. Über GitHubs vertraulichen Meldeweg für Schwachstellen erreichten die Verantwortlichen schließlich 99 Berichte, jeweils mit einem Machbarkeitsnachweis und einem Korrekturvorschlag. Damit kam auf ungefähr hundert ursprüngliche Funde eine Meldung.

Die Projektverantwortlichen entschieden, was sie wann behoben. Bis zum 15. November hatten sie für 55 der Meldungen eine Korrektur erstellt. 14 dieser Korrekturen waren bereits in einer veröffentlichten Version enthalten. Das Caddy-Team behob innerhalb einer Woche alle 22 gemeldeten Fehler. Das AutoGPT-Team hatte gerade eine neue Prüffunktion ausgeliefert, die nicht funktionierte. Drei Tage später traf die Meldung ein und verwies auf die richtige Zeile. Innerhalb eines Tages schrieb das Team eine Korrektur, die in weniger als einer Woche im Produktivbetrieb war.

## Die Flut an Meldungen

Das Pilotprojekt reagiert auf eine Entwicklung, von der Projektverantwortliche seit zwei Jahren berichten. In einem Beitrag vom 26. Januar kündigte curl-Projektleiter Daniel Stenberg an, das Prämienprogramm für Sicherheitslücken zum 31. Januar einzustellen. Der Niedergang des Programms habe in der zweiten Jahreshälfte 2024 schleichend begonnen und sich „2025 massiv beschleunigt“, als es zu einer „Explosion minderwertiger KI-Meldungen“ gekommen sei. Vor 2025 hätten sich mehr als 15 % der Einsendungen als Sicherheitslücken bestätigt. 2025 sei die Quote auf unter 5 % gefallen: „Nicht einmal jede zwanzigste war echt.“

Über fast sieben Jahre hatte das Programm für 87 bestätigte Schwachstellen mehr als 100.000 Dollar ausgezahlt. Stenberg bezeichnete es bis zum Einsetzen der Meldeflut als Erfolg. Er beendete die Zahlungen, um den Anreiz für „frei erfundene Lügen“ zu beseitigen, und verwies Hinweisgeber auf GitHubs vertraulichen Meldeweg, denselben wie im Pilotprojekt. Die von ihm veröffentlichten HackerOne-Zahlen für das vergangene Jahr zeigten bei curl einen starken Anstieg der eingehenden Meldungen, während die Zahlen bei Ruby, Node und Rails stabil blieben oder leicht sanken. Über den Grund könne man vorerst nur weiter spekulieren, schrieb er.

Zum Kern des Problems zitiert GitHub Christian Grobmeier, der Log4j mitbetreut: Die KI, die Open Source verteidigt, müsse besser sein als die KI, die angreift. GitHub selbst schreibt, KI habe das Auffinden möglicher Schwachstellen „schnell und billig“ gemacht. Sie zu beheben erfordere weiterhin menschliches Urteil, und bei Open Source liege diese Entscheidung bei den Projektverantwortlichen. Ein Mitglied des Netty-Teams formulierte es so: „Schwachstellen zu finden ist nicht mehr unser Engpass. Schwierig ist es, sie zu beheben.“

## Was die Auswahl kostete

Die Zahlen des Pilotprojekts zeigen, wo der Aufwand anfiel. Das Modell lieferte Tausende mögliche Funde zu einem Preis, den der Beitrag nicht nennt. Um daraus 99 Meldungen zu gewinnen, brauchte es einen KI-Agenten für die Vorauswahl und anschließend sieben Forscher, die etwa zwei Tage an jedem Projekt arbeiteten. GitHub schreibt ausdrücklich: „Der Versuch funktionierte, weil Menschen bei jedem Schritt sorgfältig gearbeitet haben. Und diese Arbeit lässt sich bislang nicht ohne Weiteres ausweiten.“

Der Aufwand verlagerte sich also. Bisher las ein Projektverantwortlicher die Ausgabe eines Scanners und entschied, welche Funde echt waren. Im Versuch las ein Microsoft-Team sie zuerst und leitete nur weiter, was die Prüfung bestanden hatte. Daraus leitet GitHub eine Regel für alle ab, die fremden Code mit KI untersuchen: jeden Fund mit den bereits bekannten Problemen und den Sicherheitsrichtlinien des Projekts abgleichen, ihn vertraulich melden, eine Korrektur vorschlagen und den Verantwortlichen die Entscheidung über das Tempo überlassen.

GitHub nennt selbst mehrere Gründe, das Ergebnis mit Vorsicht zu lesen. Sechs Projekte seien „eine kleine Stichprobe“. Alle sechs haben am GitHub Secure Open Source Fund teilgenommen, der jedes Projekt mit 10.000 Dollar und Sicherheitsschulungen unterstützt. Sie standen also bereits mit dem Unternehmen in Verbindung, das ihnen nun weitere Hilfe anbietet. Die Erkenntnisse beruhen auf dem, was diese Projekte mitteilen wollten. Die Zahl von 55 behobenen Fehlern bei 99 Meldungen ist eine Momentaufnahme. Sie sagt nichts darüber aus, was aus den 44 offenen Meldungen wird oder wie viel Zeit sie beanspruchen. Der Beitrag nennt auch nicht, wie viele der 9.791 Funde falsch oder doppelt waren oder wie viele echte Fehler bei der Vorauswahl möglicherweise verloren gingen.

## Wie es weitergeht

GitHub will nach eigenen Angaben allen früheren Teilnehmerprojekten KI-Sicherheitsprüfungen anbieten, bei denen die Funde vor der Meldung geprüft werden. Außerdem sollen die Teilnehmer GitHub Copilot Max erhalten. Die Erfahrungen aus dem Versuch sollen in die vertraulichen Schwachstellenmeldungen und die Sicherheitshinweise einfließen. Ergänzend schreibt GitHub, Projektverantwortliche müssten CI-Tests in privaten Forks ausführen können und Zugang zu Modellen mit Cybersicherheitsfähigkeiten haben, damit sie einen Machbarkeitsnachweis vor und nach der Korrektur testen könnten.

Auch das Modell hinter den Prüfungen ändert sich. Am Tag des GitHub-Beitrags kündigte Microsoft MAI Cyber 2 Flash an. Im Versuch kam noch das Vorgängermodell zum Einsatz. Microsoft zufolge erreicht das neue Modell im CyberGym-E2E-Benchmark 92,3 % gegenüber 91,5 % für GPT-6 Astra, bei weniger als 2 % der Kosten pro Aufgabe. In den unternehmenseigenen Tests blieben 92 von 905 Aufgaben unberücksichtigt. Ab Mitte Dezember soll es ausschließlich in Microsofts Sicherheitsprodukten verfügbar sein, darunter MDASH. Günstigere Prüfungen bedeuten mehr Funde. Nach der Rechnung des Pilotprojekts muss sich für jeweils hundert weitere Funde weiterhin ein Mensch mit dem Ergebnis befassen.

Eine Bemerkung aus dem AutoGPT-Team gegen Ende des GitHub-Beitrags weist in dieselbe Richtung. Funktionen auszuliefern werde immer einfacher. Wer künftig Software betreue, werde sich „wahrscheinlich daran entscheiden, wem genug daran liegt, sich um die Sicherheit zu kümmern“. Für das ImageMagick-Team bestand der Versuch aus 22 Meldungen, einer davon, die vertraut wirkte, und einer Viertelstunde.

## Quellen

- Microsoft AI. (2026). *Introducing MAI Cyber 2 Flash: Leading security. Lower cost*. https://microsoft.ai/news/introducing-mai-cyber-2-flash/
- Stenberg, D. (2026). *The end of the curl bug-bounty*. https://daniel.haxx.se/blog/2026/01/26/the-end-of-the-curl-bug-bounty/
- Wolf, A., & Cochran, G. (2026). *Maintainers don't need more AI bug reports. They need fixes.* GitHub Blog. https://github.blog/open-source/maintainers/maintainers-dont-need-more-ai-bug-reports-they-need-fixes/
