+++
title = "Cloudflare senkt KI-Prüfkosten durch eine Cache-Korrektur"
slug = "cloudflare-senkt-ki-pruefkosten-durch-cache-korrektur"
description = "Cloudflares KI-Codeprüfer wurde mit besseren Modellen teurer. Das Unternehmen senkte die Durchschnittskosten um 68 % und die mediane Latenz um fast zwei Drittel, musste dann aber nachweisen, dass der günstigere Prüfer nicht einfach aufgehört hatte, Probleme zu finden."
tags = ["agents", "tools", "business"]
date = 2026-10-20T04:05:28+02:00
draft = false
+++

Eine Ingenieurin existiert nur für diesen Absatz. Ihr Merge Request enthält eine kleine Änderung an einem weltweit genutzten Dienst. Sie überträgt ihn um 16:12 Uhr. Sieben automatische Prüfer werden aktiv, lesen dieselben Anweisungen, untersuchen überlappende Teile des Repositorys und schicken fast drei Millionen Token durch die Modelle, bevor ein Koordinator entscheidet, was er ihr mitteilt. Die Prüfung kommt vier Minuten später an. Sie kostet mehr als doppelt so viel wie dasselbe System im Frühjahr.

## Die Rechnung stieg ohne Neuentwurf

Cloudflare baute ein solches System für die eigenen Ingenieure. Ryan Skidmore, Systemingenieur des Unternehmens, beschrieb die ursprüngliche Architektur im April 2026: Bis zu sieben Spezialagenten prüften Sicherheit, Leistung, Codequalität, Dokumentation, Veröffentlichungen und interne Standards. Ein Koordinator entfernte doppelte Befunde und entschied, ob ein Merge Request freigegeben wurde. Im ersten Monat habe das System laut Cloudflare 131.246 Prüfläufe für 48.095 Merge Requests in 5.169 Repositorys abgeschlossen. Eine Prüfung kostete durchschnittlich 1,19 Dollar.

Ende August lag der Durchschnitt bei etwa 2,46 Dollar. Cloudflare hatte das System nicht durch ein aufwendigeres ersetzt. Der Koordinator delegierte weiterhin an Spezialisten, und dieselben Risikostufen bestimmten, ob eine Änderung leicht oder vollständig geprüft wurde. Das Unternehmen hatte die Modelle gewechselt und die Gespräche wachsen lassen.

Die Kostenreihe stieg stetig: 1,22 Dollar pro Prüfung im März, 1,44 Dollar im Juni, 1,74 Dollar im Juli und 2,32 Dollar im August, bereinigt um die Mischung der Prüfstufen. Mehr Änderungen fielen in die teure Stufe. Laut Cloudflare verursachte jedoch die Modellwahl den größten Teil des Anstiegs. Die Umstellung aller Prüfer auf Anthropic-Modelle verteuerte einen Auftrag von 1,38 auf 2,03 Dollar. Ein Prüfer für interne Standards stieg von etwa 25 auf 88 Cent pro Lauf.

Die Modelle erledigten zudem mehr Arbeit. Die Token pro Prüfung stiegen von 0,91 Millionen auf 2,99 Millionen und damit auf mehr als das Dreifache, obwohl sich die gesamte Cache-Trefferquote von 85,7 auf 97 % verbesserte. Ein hoher Prozentsatz hatte einen größeren Nenner verdeckt.

## Der teure Präfix

Unmittelbar vor der Optimierung entfielen etwa 23 % der Prüfausgaben auf Ausgabe-Token. Cache-Schreibvorgänge verbrauchten 43 %, Lesevorgänge weitere 34 %. Das meiste Geld ging an bereits gesehenen oder bald erneut benötigten Kontext.

Anthropics Prompt-Cache verwendet übereinstimmende Inhalte am Anfang einer Anfrage erneut. Die veröffentlichten Preise verdeutlichen die Abwägung: Das Schreiben eines fünf Minuten gültigen Cache-Eintrags kostet das 1,25-Fache des normalen Eingabetarifs, das Lesen ein Zehntel. Wiederverwendung lohnt sich nur, wenn spätere Anfragen vor Ablauf des Eintrags mit demselben Präfix beginnen.

Cloudflares Prüfer schienen dafür ideal. Ihre Werkzeugdefinitionen und Agentenanweisungen enthielten 11.000 bis 21.000 Token, die über Repositorys hinweg identisch waren. Dennoch fand die erste Anfrage einer Sitzung nur in 14 bis 26 % der Fälle einen gecachten Präfix.

Die Reihenfolge war falsch. OpenCode v1 hatte einen Repository-spezifischen Umgebungsblock einschließlich Arbeitsverzeichnis und Datum in denselben Systemblock wie die gemeinsamen Anweisungen eingefügt. Die Cache-Grenze lag hinter beiden. Eine Sitzung in einem Repository konnte den von einer anderen geschriebenen Präfix nicht wiederverwenden, weil veränderliche Angaben vor der Grenze standen.

Cloudflare teilte den Systeminhalt an einer Markierung und stellte das gemeinsame Material voran. Die Wiederverwendung bei der ersten Anfrage stieg anschließend auf 91 bis 99,5 %. Zudem starteten die drei wichtigsten Prüfer gleichzeitig, bevor einer den gemeinsamen Präfix fertig schreiben konnte. Das Team ließ den zweiten und dritten bis zu 20 Sekunden auf den Beginn der ersten Antwort warten und tauschte so eine kleine Verzögerung gegen etwa neun Cent Ersparnis pro Prüfer.

Diese technische Änderung brachte die größte einzelne Senkung. Sie machte dennoch weniger als die Hälfte der gesamten Einsparung aus.

## Modelle, die früher aufhören

Cloudflare testete außerdem Modelle und Reasoning-Stufen, statt die teuerste Kombination für die sicherste zu halten. Codeänderungen erklärten 65 Cent der im Beitrag gemessenen Senkung um 1,67 Dollar; Modell- und Reasoning-Änderungen 1,06 Dollar. Skidmore weist darauf hin, dass diese schrittweisen Vergleiche kein kontrolliertes Experiment waren.

Neuere Modelle benötigten weniger Aufrufe. In einem zweieinhalbtägigen Vergleichstest kostete Sonnet 5.5 pro Codequalitätsprüfung 62 % weniger als Sonnet 5, bei Leistungsprüfungen 58 % und bei Sicherheitsprüfungen 47 % weniger, trotz identischer Tokenpreise. Auf mittlerer Reasoning-Stufe tätigte der Codequalitätsagent 1,7 statt 6,2 Modellaufrufe. Mehr als die Hälfte seiner Läufe endete nach einem Aufruf, ohne eine weitere Repository-Datei zu öffnen.

Das wirkte effizient und gefährlich. Ein Prüfer, der weniger liest, kann billig fertig werden, weil er den Fehler übersieht.

Cloudflare verglich hohe und mittlere Reasoning-Stufe. Die hohe kostete pro Codequalitätsprüfung 61 % mehr und lieferte 58 % mehr kritische Befunde oder Warnungen. Der Unterschied betrug etwa zwei Cent pro Prüfung. Das Team stellte diesen Agenten wieder auf hoch und beließ die anderen Spezialisten bis zu weiteren Tests auf mittel.

Weniger Aufrufe verkürzten die Wartezeit. Die mediane Prüfung sank von vier Minuten neun Sekunden auf eine Minute 32 Sekunden. Das 99. Perzentil fiel von 15 Minuten 20 Sekunden auf vier Minuten 41 Sekunden. Prüfungen über fünf Minuten gingen von 37,9 auf 0,7 % zurück.

## Prüfen, was verschwunden ist

Die absolute Zahl schwerwiegender Befunde sank nach den Änderungen. Die Codequalität lieferte 40 % weniger kritische Befunde und Warnungen, Sicherheit 56 % und Leistung 71 % weniger. Cloudflare versuchte, beseitigtes Rauschen von übersehenen Problemen zu trennen.

Zunächst prüfte das Unternehmen, ob Ingenieure beim nächsten Push die markierten Zeilen änderten. Vor der Optimierung reagierten Autoren auf 34 % der ernsten Codequalitätsbefunde, danach auf 59 %. Befunde wurden seltener, führten aber eher zu einer Änderung: 132 aufgegriffene Befunde pro 1.000 Prüfungen nach den Änderungen gegenüber 145 zuvor. Laut Cloudflare liegt dieser Unterschied innerhalb der Fehlermarge. Über alle vier Prüfer stieg die Kennzahl von 229 auf 321 pro 1.000.

Zweitens bewerteten Modelle zweier Anbieter eine verblindete Stichprobe von 657 Befunden. Ein drittes entschied bei Uneinigkeit. Wichtige Codequalitätsbefunde pro Prüfung blieben nahe 0,3, während kleinere, doppelte und nicht überprüfbare Befunde abnahmen. Übertriebene Schweregrade gingen deutlicher zurück: Die Bewerter hielten vor den Änderungen 0,46 kritische Befunde oder Warnungen pro Prüfung für zu schwer eingestuft, danach 0,14.

Die Belege entlasteten nicht jeden Prüfer. Auf mittlerer Stufe verlor die Leistungsprüfung etwa 64 % ihrer wichtigen Befunde, entsprechend einem übersehenen wichtigen Problem je 24 vollständigen Prüfungen. Sicherheit verlor ungefähr ein Viertel, wobei diese Schätzung nicht statistisch signifikant war. Laut Cloudflare enthielten die Stichproben nur 35 bis 66 Befunde pro Gruppe, das Zeitfenster nach der Änderung dauerte einen Tag, und Modellbewerter sind unvollkommen. Dass ein Ingenieur markierte Zeilen ändert, belegt zudem eine Handlung, nicht deren Richtigkeit.

## Kosten sind ein Evaluierungsergebnis

Das fertige System kostet durchschnittlich 77 Cent pro Prüfung statt 2,43 Dollar während seiner beiden teuersten Wochen. Etwa 40 % der Ersparnis kamen aus dem Code, der Rest aus Modellen und Reasoning-Stufen. Neben den Kosten verbesserte sich die Zuverlässigkeit: Prüfungen ohne abschließendes Urteil sanken von 0,79 auf 0,27 %, Wiederholungsversuche des Sicherheitsagenten von 3,5 auf 0,04 %.

Cloudflares umfassendere Lehre ist weniger einfach als „Prompt-Caching nutzen“. Das Unternehmen untersuchte genau die erste beim Anbieter ankommende Anfrage, änderte den stabilen Präfix, maß jede Konfigurationsänderung und bewertete anschließend die verschwundenen Befunde. Ein günstigerer Agent könnte ein bereinigtes System bedeuten, ein schwächeres oder beides in verschiedenen Teilen derselben Pipeline.

Zurück zur erfundenen Ingenieurin um 16:12 Uhr. Der überarbeitete Prüfer erreicht sie, bevor sie den Merge Request verlassen hat. Er hat einmal für Anweisungen bezahlt, die seine Kollegen wiederverwenden können. Er meldet weniger Warnungen. Ihre Aufgabe ist zu wissen, ob die Stille auf beseitigte Wiederholungen oder auf ein Modell zurückgeht, das nicht nachsehen wollte. Cloudflare sparte das Geld erst, nachdem es einen Weg gebaut hatte, diese Ergebnisse auseinanderzuhalten.

## Quellen


- Anthropic. (2026). *Pricing*. https://docs.anthropic.com/en/docs/about-claude/pricing
- Skidmore, R. (2026). *Cutting our inference bill by 68% by being obsessive about optimization*. https://blog.cloudflare.com/obsessive-inference-optimization/
- Skidmore, R. (2026). *Orchestrating AI Code Review at scale*. https://blog.cloudflare.com/ai-code-review/
