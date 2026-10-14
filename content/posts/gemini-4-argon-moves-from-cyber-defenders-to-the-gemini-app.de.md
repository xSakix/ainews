+++
title = "Gemini 4 Argon kommt von Cyberverteidigern in die Gemini-App"
slug = "gemini-4-argon-von-cyberverteidigern-in-gemini-app"
description = "Dreizehn Tage nachdem Google Gemini 4 Argon nur einem geschlossenen Kreis von Cyberverteidigern gezeigt hatte, öffnet es sein Spitzenmodell für zahlende Gemini-App-Abonnenten und Entwickler. Google verspricht klarere Antworten; unabhängige Ranglisten führen das Modell einmal auf Platz eins und einmal auf Platz acht."
tags = ["models", "tools", "safety"]
date = 2026-10-13T22:54:03+02:00
draft = false
+++

Eine Buchhalterin in Brno hat drei Lieferantenverträge, ein aus einer Buchhaltungssoftware exportiertes Hauptbuch, das jedes tschechische diakritische Zeichen verstümmelt, und einen Kunden, der bis Mittwoch einen Abstimmungsvermerk will. Am Dienstagabend öffnet sie die Gemini-App, tippt aus Gewohnheit auf das Modellmenü und findet einen Namen, der morgens noch nicht da war: 4 Argon, neben 3.1 Pro und 3.8 Flash. Sie fügt alles ein und ergänzt eine eigene Zeile: keine Einleitung und keine Zusammenfassung dessen, was ich gerade mitgeteilt habe. Niemand, auf den diese Beschreibung passt, wurde für diesen Artikel interviewt. Sie ist eine Skizze der Abonnentin, um die Google nun wirbt, der Person, die seine Versionshinweise beim „Analysieren eines komplexen Finanzberichts“ oder „Erstellen einer Präsentation aus verstreuten Quellen“ zeigen.

## Zwei Wochen vom geschlossenen Programm zur App

Am 13. Oktober begann Google laut Versionshinweisen der App, Gemini 4 Argon „weltweit für Google-AI-Pro- und Ultra-Abonnenten in der Gemini-App“ bereitzustellen. Am selben Tag wurde das Modell in der Gemini API als gemini-4-argon allgemein verfügbar, in Google AI Studio und Android Studio geöffnet und in Googles Antigravity-Programmierwerkzeugen für Ultra-Abonnenten und berechtigte Gemini-Enterprise-Kunden eingeführt. Pro- und Ultra-Abonnenten können es auch im AI Mode der Google-Suche wählen, berichtete 9to5Google. Kostenlose Nutzer und Abonnenten des günstigeren AI-Plus-Tarifs haben es noch nicht, merkte Android Police an; sein Rezensent, ein Pro-Abonnent, wartete noch darauf, dass das Modell erschien.

Dreizehn Tage zuvor war der Kreis viel kleiner. Als Koray Kavukcuoglu, Senior Vice President bei Google DeepMind und Googles leitender KI-Architekt, Argon am 30. September ankündigte, ging das Modell nur an „eine Gruppe vertrauenswürdiger Cyberverteidiger“ in Googles Fairwind Program. Google erklärte, es beteilige sich am freiwilligen Verfahren der US-Regierung für Modellzugang vor Veröffentlichung und werde weiter an Schutzmechanismen arbeiten, bevor es Argon „so bald wie möglich für Entwickler, Unternehmen und Verbraucher“ öffne, beginnend mit zahlenden API-Kunden und Ultra-Abonnenten. Die Veröffentlichung am Dienstag ging eine Tarifstufe weiter und schloss Pro ein.

Fairwind ist kaum älter als das Modell. Four Flynn, Googles Vice President für Sicherheit und Datenschutz, führte es am 2. September als Programm mit begrenztem Zugang für Regierungen, Betreiber kritischer Infrastruktur und Sicherheitsunternehmen ein, aufgebaut um ein kleineres Spezialmodell, Gemini 3.8 Flash Cyber, und das Patch-Werkzeug CodeMender. Teilnehmer verpflichten sich, den Zugang auf ihre Sicherheits-, Vorfallreaktions- oder Penetrationstestteams zu beschränken. Google erklärt, mehr als 650 Partner nähmen teil.

## Was sich laut Google für die schreibende Person verändert hat

Die App-Ankündigung ist kurz und betrifft überwiegend den Stil. Argon, schreibt Google, „beantwortet Fragen direkter mit weniger Einschränkungen, wiederholt sich nicht häufiger als nötig und verzichtet in den Antworten auf Klischees“. Bei längeren Aufgaben „hält es über den Stand auf dem Laufenden, indem es seinen Fortschritt häufiger und effektiver mitteilt“. Laut 9to5Google erklärt Google auch, Argon befolge Stilanweisungen zuverlässiger als jedes frühere Gemini-Modell.

Weitere Änderungen kamen gleichzeitig. Ein Schalter im Hauptchatfenster wechselt nun von Chat zu Aufgaben, einem Modus, in dem Gemini laut Google weiterarbeiten kann, „selbst wenn man nicht am Computer sitzt“. Mehr als 40 externe Dienste, darunter Instacart, OpenTable, Adobe und Shopify, lassen sich verbinden, wobei laut Versionshinweisen die meisten nur auf Englisch in den USA funktionieren. Auf einem Mac befindet sich Antigravitys agentische Programmieroberfläche nun in der Gemini-App: Der Nutzer genehmigt den Plan eines Programmieragenten, kehrt zum Chat zurück und wird benachrichtigt, wenn der Agent im Hintergrund den Code erstellt und getestet hat.

Hinter der Verbraucherwerbung steht die Aussage, die Google im September zu langer Arbeit machte. Argons Ausgabegrenze stieg von 64.000 auf eine Million Token, was dem Modell laut Google Raum gebe, „Hunderttausende Token in einem einzigen Verlauf zu erzeugen“. Die Entwicklerdokumentation ist präziser: standardmäßig 65.536 Ausgabe-Token und bis zu 1.048.576 in einem Modus namens Long Decode, innerhalb eines gemeinsamen Eingabe- und Ausgabefensters derselben Größe.

## Wo die externen Ranglisten es einordnen

Googles eigene Zahlen sehen Argon bei 77,9 % auf DeepSWE v1.1, einem Test langer Softwareentwicklungsaufgaben, bei 51,3 % auf Zapiers AutomationBench und bei 91,7 % auf dem Langvideo-Benchmark LVBench. Auf CWE-bench v1, der prüft, ob ein Modell Sicherheitslücken reparieren kann, liegt Argon laut Google mit 68 % gemeinsam auf Platz eins. Das sind Anbieterzahlen. VentureBeat merkte an, dass Anthropics Claude Opus 5.5 auf Terminal-Bench 4.0, der Programmierung über Kommandozeilenwerkzeuge misst, 66,4 % erreichte, „gegenüber Argons 57,4 %“.

Zwei unabhängige Ranglisten sind sich uneinig, wie weit Argon vorn liegt. Vals AI, dessen Index Finanz-, Programmier-, Rechts- und Steueraufgaben nach dem Anteil jedes Sektors am US-BIP gewichtet, führte Argon am 13. Oktober mit 68,90 % auf Platz eins, vor Claude Sonnet 5.5 mit 67,04 und Claude Opus 5.5 mit 66,97. Artificial Analysis gab Argons Einstellung mit hohem Reasoning-Aufwand 53 Punkte auf seinem Intelligence Index und Platz acht unter den 216 aufgeführten Modellen. Der Vorsprung in der Vals-Tabelle beträgt weniger als zwei Punkte, und bei Artificial Analysis führt Argon überhaupt nicht.

Die Seite von Artificial Analysis nennt eine Zahl, die schlecht zum Versprechen weniger Wörter passt. Zur Absolvierung des Index erzeugte Argon 110 Millionen Ausgabe-Token gegenüber einem Median von 85 Millionen, was die Seite „etwas wortreich“ nennt. Die Antwort, die ein Abonnent liest, und die Arbeit zu ihrer Erzeugung werden getrennt gemessen; Googles Versprechen betrifft die erste.

## Schutzmechanismen für die öffentliche Version

Google hat mehr über seine Schutzmechanismen gesagt als externe Tester über das Modell. Der Einführungsbeitrag erklärt, Argon sei darauf ausgelegt, Hilfe bei Cyberangriffen sowie chemischen, biologischen, radiologischen und nuklearen Waffen zu verweigern. Google beobachte die internen Aktivierungen auf Missbrauchssignale, und ein separates System lese Argons Gedankenkette und Aktionen und könne es stoppen, wenn es über die Absicht des Nutzers hinauszugehen versuche. Für vertrauenswürdige Verteidiger und die eigenen Teams veröffentlicht Google Argon nach eigenen Angaben „ohne Cyber-Schutzmechanismen“. Abonnenten erhalten die geschützte Version.

Regierungen sahen sich das Modell vor der breiteren Veröffentlichung an. Neben dem von Google beschriebenen US-Verfahren erklärte der britische KI-Minister Kanishka Narayan am 12. Oktober in London, Wissenschaftler des AI Security Institute führten „nun strenge Evaluierungen der neuesten Modellgenerationen durch“, und nannte darunter Googles Gemini, berichtete der Guardian. Der Bericht sagt nicht, welche Version. Weder er noch Googles Ankündigungen nennen die Ergebnisse der Prüfer oder ob das Modell infolgedessen verändert wurde.

## Der Preis und die Arbeit, für die Argon gedacht ist

Entwickler zahlen bis zum 30. November einführend 2 Dollar pro Million Eingabe-Token und 10 Dollar pro Million Ausgabe-Token; zwischengespeicherte Eingabe ist 95 % günstiger. Ab dem 1. Dezember verdoppelt sich laut VentureBeat und 9to5Google der Preis auf 4 und 20 Dollar.

Der Beitrag des Antigravity-Teams enthält einen Satz, der die Einführung einordnet. „Während Argon für die schwierigsten Probleme ausgelegt ist“, heißt es, „freuen wir uns ebenso auf künftige Modelle, die als alltägliche Begleiter für ein noch breiteres Spektrum von Entwicklern dienen können.“ Er stellt Argon an das lange, teure Ende der Arbeit und überlässt die Alltagsnutzung Modellen, die Google noch nicht veröffentlicht hat.

Die Belege, die Google für dieses lange Ende anbietet, kommen aus dem Unternehmen. Es erklärt, mehr als 100.000 Menschen bei Alphabet nutzten Argon monatlich in einer internen Antigravity-Version, und über vier Wochen sei die Menge agentengeschriebenen Codes um 35 % gestiegen, während Rücknahmen nach der Einreichung von Code um 30 % gesunken seien. In einem Beispiel prüfte Argon eine Reihe von Zugriffskontrolländerungen und fand vier kritische Sicherheitsfehler in Code, den zwei frühere Spitzenmodelle geprüft und für fehlerfrei erklärt hatten. Google nennt keines der Modelle und hat die Prüfung nicht veröffentlicht; dies sind eigene Berichte über eigene Arbeit.

Zurück in Brno erhält die für diese Geschichte erfundene Buchhalterin ihren Vermerk in vier kurzen Absätzen, ohne einleitendes Kompliment und ohne Wiederholung des Eingefügten. Sie prüft die Summen dennoch Zeile für Zeile gegen das Hauptbuch, so wie sie es tat, als das Menü noch bei 3.1 Pro endete.

## Quellen

- Artificial Analysis. (2026). *Gemini 4 Argon (High): Intelligence, Performance & Price Analysis*. https://artificialanalysis.ai/models/gemini-4-argon
- Bhatia, S. (2026). *Gemini 4 Argon is here, and Google says it'll finally cut down on the AI fluff*. Android Police. https://www.androidpolice.com/gemini-4-argon-available-pro-ultra-subscribers/
- Flynn, F. (2026). *Proactive cyber defense for governments and enterprises*. Google. https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/
- Franzen, C. (2026). *Google makes Gemini 4 Argon broadly available with limited-time low API pricing of $2/$10 per 1M token*. VentureBeat. https://venturebeat.com/technology/google-makes-gemini-4-argon-broadly-available-with-limited-time-low-api-pricing-of-2-10-per-1m-token
- Google. (2026). *Gemini 4 Argon comes to the Gemini app*. https://blog.google/innovation-and-ai/products/gemini-app/gemini-4-argon-availability/
- Google. (2026). *Gemini 4 Argon is now available for developers*. https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-4-argon/
- Google. (2026). *Gemini Apps' release updates & improvements*. https://gemini.google/release-notes/
- Google AI for Developers. (2026). *Gemini 4 Argon*. https://ai.google.dev/gemini-api/docs/models/gemini-4-argon
- Google AI for Developers. (2026). *Gemini API release notes*. https://ai.google.dev/gemini-api/docs/changelog
- Google Antigravity Team. (2026). *Gemini 4 Argon in Google Antigravity*. https://antigravity.google/blog/gemini-4-argon-in-google-antigravity
- Kavukcuoglu, K. (2026). *Gemini 4 Argon: our next era of frontier intelligence*. Google. https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/
- Li, A. (2026). *Gemini app rolling out Gemini 4 Argon to AI Pro and AI Ultra*. 9to5Google. https://9to5google.com/2026/10/13/gemini-app-4-argon/
- Milmo, D. (2026). *Cyber-attack similar to OpenAI Medicare breach seems likely in UK, says minister*. The Guardian. https://www.theguardian.com/technology/2026/oct/12/cyber-attack-like-openai-medicare-breach-seems-likely-in-uk-says-minister
- Vals AI. (2026). *Vals Index*. https://www.vals.ai/benchmarks/vals_index
