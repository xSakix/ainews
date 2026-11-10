+++
title = "Fable 5.2 senkt den Preis, doch Reasoning bestimmt die Rechnung"
slug = "fable-5-2-preis-reasoning-bestimmt-rechnung"
description = "Anthropic senkte den Preis von Claude Fable 5.2 um ein Fünftel, doch ein unabhängiger Index maß bei maximaler Reasoning-Stufe die höchsten Kosten pro Aufgabe unter 73 Modellen. Der Unterschied liegt im Token-Verbrauch, und Anthropics eigene Diagramme zeigen, dass die Reasoning-Einstellung darüber entscheidet."
tags = ["models", "business"]
date = 2026-11-10T03:25:07+01:00
draft = false
+++

Dieser Montag ist erfunden, aus Veröffentlichungsunterlagen zusammengesetzt und nicht aus einem Tagebuch übernommen. Eine Plattformleiterin eines mittelgroßen Softwareunternehmens liest, Anthropic habe den Preis seines Spitzenmodells um ein Fünftel gesenkt. Sie tut, wozu die Ankündigung einlädt. Sie ändert den Modellnamen in der Agentenkonfiguration ihres Teams, setzt den Effort-Parameter auf den höchsten Wert und lässt über Nacht vierzig Repository-Audits laufen. Am Morgen ist der Stapel fertig, und sie will nur eines öffnen: die Rechnung. Die sieht nicht so aus wie die gelesene Überschrift.

Die Überschrift war korrekt. Am 9. November veröffentlichte Anthropic Claude Fable 5.2 und dessen Zwillingsmodell Claude Mythos 5.2 für 8 Dollar pro Million Eingabe-Token und 40 Dollar pro Million Ausgabe-Token, gegenüber 10 und 50 Dollar bei den 5.1-Versionen. Auch die unabhängige Zahl, die am selben Tag erschien, ist korrekt. Artificial Analysis, das einen anbieterübergreifenden Intelligenzindex veröffentlicht, ließ Fable 5.2 mit maximaler Einstellung laufen und setzte es mit 65 Punkten bei der Intelligenz auf Platz eins von 74 Modellen und bei den Kosten mit 26,54 Dollar pro Indexaufgabe auf Platz 73 von 73. Beide Zahlen beschreiben dasselbe Modell. Was sie trennt, ist die Menge verbrauchter Token.

## Was die Preisliste sagt

Anthropics Dokumentation führt die neuen Tarife klar auf. Cache-Lesezugriffe kosten 0,20 Dollar pro Million Token, Stapelverarbeitung kostet die Hälfte des Grundpreises, und ein optionaler Schnellmodus, der bis zu 2,5-mal schneller generiert, kostet 16 Dollar für Eingabe und 80 Dollar für Ausgabe. Das Unternehmen erklärt außerdem, das Modell produziere Ausgaben bis zu 30 % schneller als Fable 5.1. TechCrunch merkt an, Fable sei nun günstiger als sein wichtigster Rivale. Fortune verortet Fable 5.2 preislich 20 % unter OpenAIs GPT-6 Astra, das mit 10 und 50 Dollar gelistet ist; zwischengespeicherte Eingaben kosten 20 Cent gegenüber einem Dollar bei Astra.

Mythos 5.2 hat denselben Preis. Anthropic bezeichnet beide als dasselbe zugrunde liegende Modell. Fable wird mit Schutzmechanismen für Cyber- und Biologierisiken ausgeliefert und steht allen Kunden offen, während Mythos an Organisationen geht, die in die Cyber Verification und Life Sciences Verification Programs des Unternehmens aufgenommen wurden. Der Preis ist gleich. Der Zugang nicht.

## Was der Index gemessen hat

Artificial Analysis berechnet die Kosten pro Aufgabe aus den Preisen für Eingabe, Cache-Treffer, Cache-Schreibzugriffe, Schlussfolgern und Antwort-Token, geteilt durch die Zahl der Aufgaben und gewichtet über die neun Evaluierungen des Index. Auf dieser Grundlage erzeugte Fable 5.2 mit maximaler Reasoning-Stufe 275 Millionen Ausgabe-Token, während der Median vergleichbarer Modelle bei 72,8 Millionen liegt. Es benötigte 46,4 Minuten pro Aufgabe gegenüber einem Median von 12,7 sowie 216 Sekunden bis zum ersten Antwort-Token. Die Zusammenfassung der Website nennt das Modell „besonders teuer“ und „sehr wortreich“.

Die Rechnung ist kurz. Der gelistete Ausgabepreis beträgt 40 Dollar gegenüber einem Median von 10 Dollar, also das Vierfache, und die Token-Zahl liegt etwa beim 3,8-Fachen des Medians. Eine Rechnung ist Preis mal Menge, und Fable 5.2 liegt bei dieser Einstellung in beiden Größen hoch. Die Grenzen müssen benannt werden: Dies sind die Aufgaben von Artificial Analysis, nicht die der Leser, und die Zahl gilt für eine einzige Reasoning-Stufe.

## Der Regler, auf den Anthropic verweist

Anthropic bestreitet nicht, dass die Reasoning-Stufe zählt. Laut Einführungsseite ist Medium die Voreinstellung in den Claude-Apps und Claude Code; auf Medium erledige Fable 5.2 schwierige Aufgaben mit weniger Token als 5.1. In frühen Tests auf FrontierCode 2.0, einem Benchmark dafür, ob Open-Source-Maintainer die Codeänderungen eines Modells übernehmen würden, erreichte Fable 5.2 auf High 45,3 % gegenüber 45,5 % für Opus 5.5 auf Max, für ungefähr die Hälfte der Kosten pro Aufgabe. Auf Perplexitys Datensammlungsbenchmark WANDR erreicht Medium den Bestwert von Opus 5.5 für etwa 40 % der Kosten. Auf Humanity's Last Exam gelingt Low dies für weniger als ein Zehntel. Auf Xhigh erreicht das Modell 49,1 % auf FrontierCode, den höchsten Wert aller veröffentlichten Modelle, die Anthropic testete.

All dies sind Diagramme des Anbieters aus frühen Tests. Sie zeigen, dass dasselbe Modell abhängig von einem einzigen Parameter an sehr unterschiedlichen Punkten einer Kostenkurve liegt. Diese Lesart stützt auch die unabhängige Zahl. Die Dokumentation ist deutlich darin, wo Fable hingehört: Für die meisten Arbeitslasten mit dem neuesten Opus-Modell beginnen und zu Fable wechseln, wenn Evaluierungen mit Opus auf höheren Reasoning-Stufen weiterhin nicht „die Anforderungen erfüllen“.

## Wie die Rechnung hierhin kam

Anthropic hat Preise schon früher so dargestellt. In der Ankündigung von Claude Opus 5.5 vom 22. September hieß es, das Modell arbeite bei den meisten Tätigkeiten auf dem Niveau von Fable 5.1 und koste bei typischen Arbeitslasten 40 % weniger als Opus 5. Der Token-Preis lag mit 4 und 20 Dollar pro Million um 20 % niedriger; laut Unternehmen stammte der Rest der Ersparnis aus einem geringeren Token-Verbrauch pro Aufgabe. Eine Rechnung ist auch nach Anthropics eigener Darstellung ein Tarif mal eine Menge.

Gergely Orosz, Autor von The Pragmatic Engineer, veranschaulichte diesen Effekt in einer Ausgabe vom 20. Oktober. Er sprach mit Menschen aus 27 Arbeitsstätten über KI-Ausgaben pro Entwickler, einer selbst ausgewählten, überwiegend anonymen Stichprobe. Er berichtet, die Ausgaben hätten im Juni und Juli ihren Höhepunkt erreicht und sich für Unternehmen mit API-Tarifen ungefähr halbiert. Die meisten nannten dafür eine Mischung aus Opus 5.5 und offenen Modellen als Grund. Ein Entwickler gab im September 2.200 Dollar für Opus 5 aus und erwartet mit Opus 5.5 die Hälfte. Orosz hörte außerdem, dass bei mehreren Unternehmen subventionierte Abonnements auslaufen, was ihre Rechnungen auf das Fünf- bis Zehnfache erhöhen könnte.

Fable 5.2 kommt in diese Rechnung hinein. Ein Käufer, der zur Halbierung der Rechnung auf Opus 5.5 wechselte, hat nun eine höhere Klasse, deren Token-Preis gefallen ist und deren Kosten pro Aufgabe von einer Einstellung abhängen, die die meisten Menschen nicht ändern.

## Einführungsangebote und wer den Test bezahlt

In der ersten Woche bekommen Abonnenten den Preis nicht zu spüren. Anthropics Hilfezentrum erklärt, Pro-Tarife und Standard-Team-Lizenzen erhielten vom 9. bis 16. November alle Fable-Modelle innerhalb ihrer Wochenlimits, bis zu 50 % dieser Limits, sowie eine Rücksetzung des Limits. Max- und Ultra-Tarife erhalten je nach Dauer des bezahlten Kontos eine bis drei Rücksetzungen; ungenutzte Rücksetzungen verfallen am 8. März 2027. Die Angebote sind für Abonnements formuliert, über API-Konten sagt die Seite nichts.

## Noch einmal die Rechnung

Zurück am erfundenen Montag sieht sich die Leiterin den Audit-Stapel an und findet an den Ergebnissen nichts auszusetzen. Was ihr fehlt, ist ein Vergleich. Der nächste Test, den sie schreibt, ist unspektakulär: dieselben vierzig Repositories auf High, dann auf Medium, jeweils mit Kosten und Zahl der akzeptierten Befunde daneben. Ob die günstigeren Durchläufe genug finden, kann keine Einführungsseite für ihr Team entscheiden. Auch die gelesene Dokumentation sagt das. Das Modell wird pro Million Token bepreist. Ihre Prüfung wird pro Repository bepreist.

## Quellen

- Anthropic (2026). *Introducing Claude Fable 5.2 and Claude Mythos 5.2*. https://www.anthropic.com/claude-fable-and-mythos-5-2
- Anthropic (2026). *Introducing Claude Opus 5.5*. https://www.anthropic.com/news/claude-opus-5-5
- Anthropic (2026). *Claude Fable 5.2 launch offers*. Claude Help Center. https://support.claude.com/en/articles/17506494-claude-fable-5-2-launch-offers
- Anthropic (2026). *What's new in Claude Fable 5.2*. Claude Platform Docs. https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2
- Artificial Analysis (2026). *Claude Fable 5.2 (Max): Intelligence, Performance & Price Analysis*. https://artificialanalysis.ai/models/claude-fable-5-2
- Brandom, R. (2026). *Anthropic releases new Mythos and Fable models amid RSI concerns*. TechCrunch. https://techcrunch.com/2026/11/09/anthropic-releases-new-mythos-and-fable-models-amid-rsi-concerns/
- Forlini, E. (2026). *Anthropic debuts Claude Fable, Mythos 5.2 models, priced 20% below OpenAI's GPT-6 Astra*. Fortune. https://fortune.com/2026/11/09/anthropic-debuts-updated-claude-fable-and-mythos-models-undercutting-price-of-openais-gpt-6-astra-by-up-to-80/
- Orosz, G. (2026). *What's the ROI of software engineers' spending on AI?* The Pragmatic Engineer. https://newsletter.pragmaticengineer.com/p/whats-the-roi-of-software-engineers
