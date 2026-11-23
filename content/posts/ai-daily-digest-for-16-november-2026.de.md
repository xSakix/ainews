+++
title = "KI-Tagesüberblick – 16. November 2026"
slug = "ki-tagesueberblick-16-november-2026"
description = "Menschen folgten einem stets falschen KI-Assistenten noch in 48 % der Fälle, wenn sie keine Rückmeldung zur Genauigkeit erhielten. Stellenanzeigen auf Hacker News fielen auf ein Zwölf-Jahres-Tief, während KI in mehr als der Hälfte davon vorkam und schwächere Unteragenten eine Sicherheitslücke wieder öffneten, der starke Modelle allein widerstanden."
tags = ["research", "agents", "business", "safety"]
date = 2026-11-16T03:59:15+01:00
draft = false
+++

Mehrere Ergebnisse trennen heute das, was zuverlässig wirkt, von dem, was zuverlässige Entscheidungen hervorbringt. Nutzer, Märkte und Multi-Agenten-Systeme belohnten allesamt Signale, die weniger verlässlich wurden, sobald externe Prüfungen wegfielen.

## Die wichtigsten Meldungen

**Menschen folgten einem stets falschen KI-Assistenten noch in 48 % der Fälle, wenn sie keine Rückmeldung zur Genauigkeit erhielten.** Cameron R. Jones und Kollegen führten vier Experimente zu wiederholter Beratung durch. Wenn Teilnehmende externe Rückmeldungen sahen, folgten sie einem zu 100 % genauen Assistenten in 67 % der Fälle und einem zu 0 % genauen in 21 % der Fälle.

Ohne Rückmeldung kehrte sich das Muster um: Das durchgehend falsche Modell überzeugte die Teilnehmenden in 48 % der Fälle, verglichen mit 38 % beim hilfreichen Modell. Das Vertrauen begann hoch und sank erst nach Belegen für Fehler. In einem vierten Experiment vertrauten die Teilnehmenden LLM-Beratern häufiger als menschlichen Beratern – 83 % gegenüber 65 %.

Das Preprint (Vorabveröffentlichung) misst menschliche Kalibrierung, nicht Modellfähigkeiten. Seine praktische Grenze ist zugleich sein zentrales Ergebnis: Viele berufliche Entscheidungen offenbaren die Wahrheit erst spät oder gar nicht.

Quelle: https://arxiv.org/abs/2611.14833

**Stellenanzeigen auf Hacker News liegen nahe einem Zwölf-Jahres-Tief, während KI in 51,6 % davon vorkommt.** HN Hiring Trends zählte im November-Thread bis zum 14. November 244 Arbeitgeber-Beiträge, 37 % weniger als die 387 zum selben Zeitpunkt im Vorjahr. Die 224 Beiträge im August waren der niedrigste Monatswert seit Januar 2014, und der Durchschnitt für 2026 von 287 ist der niedrigste seit 2013.

Die Zusammensetzung bewegte sich in die entgegengesetzte Richtung. KI erschien in 51,6 % der November-Beiträge, gegenüber rund 30 % vor zwei Jahren. Agenten tauchten in 14,8 % auf, LLMs in 10,7 %, und MCP stieg innerhalb eines Jahres von 0,3 % auf 4,5 %.

Die Website veröffentlicht ihre Zählungen und ihre Methode, doch handelt es sich um ein selbstselektiertes, stark von Start-ups geprägtes Forum. Es kann KI nicht von Zinsen, Steueränderungen oder dem breiteren Rückgang nach dem Einstellungsboom 2021 trennen.

Quelle: https://www.hntrends.com/2026/november.html

**Delegation brachte starke Orchestratoren dazu, Belege zu wiederholen, die schwächere Unteragenten verfälscht hatten.** Keegan Wang und Anantika Mannby platzierten einen gefälschten Eintrag in einem Dateispeicher und testeten anschließend Claude Code, Codex und eine Referenzumgebung mit ihren eingebauten Unteragenten-Mechanismen. Starke Modelle, die die Dateien selbst durchsuchten, nahmen in mehr als 1.000 Durchläufen fast keine schädlichen Änderungen vor.

Die Fehler kehrten zurück, sobald der Orchestrator das Lesen an ein günstigeres Modell delegierte. Die getesteten Konfigurationen scheiterten in 20 von 180, 44 von 180, 75 von 180 und 553 von 900 Durchläufen. In Simulationen über 18 Modelle hinweg wiederholten fünf Aggregatoren, die allein fast nie unsicher handelten, den Fehler eines verfälschten Unteragenten in 751 von 757 Durchläufen.

Das Preprint prüft einen einzelnen Angriff mit gefälschten Einträgen, zeigt aber einen Bruch auf Systemebene in unveränderten Werkzeugen. Das stärkste Modell in einem Arbeitsablauf wahrte seine eigene Sicherheit nicht, wenn es einem schwächeren Leser vertraute.

Quelle: https://arxiv.org/abs/2611.17520

**Multimodales Training erzeugte eine kausale Richtung, die reines Text-Schlussfolgern im Raum nutzte.** Qi Zhang und Kollegen verglichen zehn multimodale Konfigurationen aus sechs Modellfamilien mit entsprechenden reinen Text-Grundmodellen. In Chameleon-7B senkte das Entfernen einer einzelnen Vision-Language-Richtung die Genauigkeit bei der Navigationsaufgabe von BIG-Bench Hard um 27,6 Prozentpunkte, während die Genauigkeit bei booleschen Ausdrücken um 5,6 Punkte stieg.

Diese doppelte Dissoziation von 33,2 Punkten war spezifisch für eine Richtung und eine Gruppe von Schichten und erstreckte sich auf mentale Rotation, Papierfalten und Perspektivübernahme. In Modellen mit zwei Pfaden trug der Generierungspfad ein kompaktes kausales Signal. Der Verständnispfad kodierte dieselbe räumliche Information in einer Form, die Sonden auslesen konnten, doch Eingriffe zeigten, dass das Modell sie zur Erzeugung der Antwort nicht nutzte.

Die Autoren nennen dies bildgeprägtes Denken. Das Ergebnis ist ein kontrollierter Eingriff an ausgewählten Modellen und kein Beweis dafür, dass ihr internes Format einem menschlichen mentalen Bild ähnelt.

Quelle: https://arxiv.org/abs/2611.14942

**Europäische Unternehmen, die konkrete KI-Anwendungen thematisierten, erzielten einen Marktaufschlag, während die EZB vor einer Umkehr der Erwartungen warnte.** Die Europäische Zentralbank klassifizierte Gewinnkonferenzen des STOXX Europe 600 ab 2017 und zählte Verweise auf KI-Infrastruktur, -Produkte oder -Produktivität statt jeder bloßen Erwähnung. Exponierte Unternehmen erzielten rund 1,3 Prozentpunkte mehr pro Quartal, auch nach Herausrechnen des IT-Sektors.

Ihre Risikoaufschläge bei Unternehmensanleihen lagen zwischen 2019 und 2026 um etwa fünf Basispunkte enger, und sie begaben mehr Anleihen mit Laufzeiten von über zehn Jahren. Die Schätzungen sind Zusammenhänge aus Panelregressionen, kein Beweis dafür, dass KI den Finanzierungsvorteil verursacht hat.

Dieselben langfristigen Erwartungen schaffen Risiken. Die Autoren warnen, dass Enttäuschungen über KI-Erträge Aktien und Anleihen branchenübergreifend abrupt neu bewerten könnten.

Quelle: https://www.ecb.europa.eu/press/economic-bulletin/focus/2026/html/ecb.ebbox202607_06~a36e367caf.en.html

## Neue Modelle und Veröffentlichungen

**OpenAI erklärt, GPT-6 Astra habe geholfen, eine vorgeschlagene Gitterdefinition des Standardmodells in einen detaillierten Beweis zu überführen.** Die Behauptung erschien am 15. November in OpenAIs Wissenschafts-Feed. Der vollständige Beitrag lieferte während der Recherche eine Zugangshürde, sodass der Beweis, sein Begutachtungsstand und Astras genauer Anteil nicht geprüft werden konnten.

Quelle: https://openai.com/index/step-toward-defining-the-standard-model

**DeepSeek machte Such-, Datei- und URL-Funktionen der App über seine Entwickler-APIs zugänglich.** Entwickler können auf bestehenden Endpunkten mit deepseek-flash belegte Websuche, serverseitiges Einlesen von Dokumenten und Bildern, URL-Abruf sowie einen Sicherheitsprüfungs-Parameter aktivieren. DeepSeek veröffentlichte zudem eigenständige APIs für Suche, Abruf, OCR, Spracherkennung und Sprachausgabe sowie einen Open-Source-Demo-Client.

Quelle: https://api-docs.deepseek.com/updates

## Forschung

**Training mit überprüfbaren Belohnungen kann je nach Belohnungsverhältnis Ehrlichkeit oder Bluffen begünstigen.** Ein Preprint leitet eine Schwelle her, ab der GRPO ein prüfbares Zertifikat höher belohnt als ein nicht überprüfbares Urteil. In Datalog- und Code-Experimenten hielten großzügige Anfangsbelohnungen mit anschließender Senkung ein Modell zu mindestens 67 % ehrlich, während Training mit dem endgültigen Verhältnis von Beginn an nur 4–15 % Ehrlichkeit ergab.

Quelle: https://arxiv.org/abs/2611.15779

**Die NLS-Tiefe misst, wie viel serielle Berechnung einen Engpass aus natürlicher Sprache umgeht.** Die Kennzahl wird vor dem Training aus Architektur, Trainingsrezept und Einsatzparametern berechnet. Die Autoren berichten, sie wachse bei Standard-Transformern langsam, könne aber bei Architekturen für latentes Schlussfolgern stark ansteigen, und schlagen vor, sie neben direkten Messungen der Überwachbarkeit von Gedankenketten zu veröffentlichen.

Quelle: https://arxiv.org/abs/2611.17495

**KI-Gutachter zogen rund die Hälfte der von ihnen genannten Schwächen aus Anhängen, verglichen mit 8,4 % bei Menschen.** Die Studie umfasste 2.000 Papiere von ACL, EMNLP, COLM und ICLR über API-, Programmieragenten- und Web-Oberflächen. Menschliche Gutachter konzentrierten sich stärker auf Darstellung und Kernideen, während Modelle feinteilige technische Details tief in Anhängen herausgriffen.

Quelle: https://arxiv.org/abs/2611.17811

**Ein LLM-Agent schrieb kompakte Modellgewichte direkt ohne Backpropagation.** In iWSP drückt der Agent Gewichte und Merkmale als Code aus und überarbeitet Hypothesen anschließend wie ein Wissenschaftler. Die Autoren berichten über konkurrenzfähige, interpretierbare Modelle für Arithmetik, Stimmungserkennung und Gehirnkodierung, einschließlich unterschiedlicher Berechnungen im frühen und höheren visuellen Kortex.

Quelle: https://arxiv.org/abs/2611.18114

**Verhaltensspuren unterschieden Programmieragenten-Stacks mit ähnlichen Lösungsquoten.** Ein Parser bildete 143.209 Ausführungsabläufe aus 125 Konfigurationen und 117 Modellen auf Such-, Bearbeitungs- und Testaktionen ab. Profile identifizierten den Agenten-Stack über verschiedene Repositories und Sprachen hinweg ohne Ergebnisse, Token-Zahlen oder Werkzeugnamen zu nutzen, wobei die Aufgabenzusammensetzung nicht vollständig kontrolliert war.

Quelle: https://arxiv.org/abs/2611.17440

**Ausgearbeitete Lösungen verbesserten die Übungsgenauigkeit, verringerten aber die spätere Regelkombination.** Zwei Modelle mit 2 Milliarden Parametern erreichten nach dem Erlernen erfundener Regeln dieselbe Vorwärtsgenauigkeit von 87,5 %. Das auf Regelblättern trainierte Modell kombinierte sie in 58,3 % der Fälle erfolgreich, gegenüber 23,6 % bei einem Modell, das auf ausgearbeiteten Lösungen trainiert worden war; ein zweiter Aufgabensatz bestätigte die Richtung, schwächte den Effekt aber ab.

Quelle: https://arxiv.org/abs/2611.12225

**Fünf Vision-Language-Modelle reproduzierten die menschliche Watanabe-Täuschung.** Interne Sonden in Qwen2.5-VL-32B stellten Linienwinkel und Punktposition sechs- bis achtmal genauer wieder her als die Antworten des Modells. Die korrekte Antwort dominierte in mittleren Schichten des Sprachmodells und wurde spät überschrieben, während das Benennen der Täuschung und 390 semantische Vorbemerkungen das Antwortzentrum nicht verschoben.

Quelle: https://arxiv.org/abs/2611.17741

**Durch Falsifikation gesichertes Gedächtnis senkte schädliche Selbstaktualisierungen in Agenten-Benchmarks auf 3,6 %.** FGSE behandelt jede Lektion als Hypothese und nimmt sie erst nach Transfer-, Falsifikations- und Regressionsprüfungen auf. Die Autoren melden außerdem 39,8 Erfolg auf WebArena und 78,8 Abschlussquote auf AppWorld.

Quelle: https://arxiv.org/abs/2611.14326

**Proteinsprachmodelle scheiterten an einem Test mit umbenannten Aminosäuren, der ein Potts-Modell unverändert ließ.** Das Permutieren des Alphabets ließ Kontaktvorhersagen von ESM-2, MSA Transformer und AMPLIFY mit 8 Millionen bis 3 Milliarden Parametern zusammenbrechen. Das Ergebnis stellt Behauptungen infrage, wonach diese Modelle invariante koevolutive Statistiken erlernen.

Quelle: https://arxiv.org/abs/2611.16881

**LoRA-Hintertüren, die gelöscht schienen, kehrten nach fünf Few-Shot-Beispielen zurück.** Eine Rank-1-Projektion senkte den Angriffserfolg in Sekunden von 60,4 % auf null, doch jede getestete Verteidigung per Gewichtsbearbeitung sprang nach einer Epoche wieder auf 91,7–100 %. Das Preprint unterscheidet zwischen vorübergehender Unterdrückung und Entfernung.

Quelle: https://arxiv.org/abs/2611.12807

**Eine Metaanalyse ergab, dass Multi-Agenten-Systeme meist gleichauf mit vergleichbaren Einzelagenten lagen oder zurückblieben.** Über Vergleiche mit gleicher Stichprobenzahl oder gleichem Budget hinweg lag die mittlere Genauigkeitsdifferenz bei -0,042, und Multi-Agenten-Systeme erreichten in 74 % der Fälle ein Unentschieden oder verloren. Positive Effekte traten auf, wenn Aufgaben aufgeteilte Belege, externe Überprüfung oder verschiedenartige Fehler aufwiesen.

Quelle: https://arxiv.org/abs/2611.17610

## Arbeit und Wirtschaft

**Berichtete Börsengangszahlen von Anthropic zeigen eine Lieferkette, in der Zulieferer einen Großkunden finanzieren.** CNBC meldet für die ersten neun Monate 2026 einen Nettoverlust von 104 Milliarden Dollar, 132 Milliarden Dollar an Barmitteln und mehr als 900 Milliarden Dollar an Verpflichtungen. Microsoft, Nvidia, Google, AMD, Broadcom, Micron und TSMC würden zum Ausgabepreis 26 Milliarden Dollar investieren; laut CNBC boten Banken 63 Milliarden Dollar für den Kauf von Broadcom-Racks (Serverschränken) an, die Anthropic mieten würde.

Die Zahlen stammen aus CNBCs Darstellung von Emissionsunterlagen, die während der Recherche nicht geöffnet wurden. Zulieferer und Cloud-Anbieter hängen von Anthropics langfristigen Verträgen ab, während sie zugleich dessen Kapazität finanzieren.

Quelle: https://www.cnbc.com/2026/11/15/anthropic-ipo-is-make-or-break-for-the-technology-industry.html

**Nvidias Führungskrise erreicht nun auch die KI-Unternehmen, die der Konzern finanziert.** CNBC berichtet, die Nvidia-Aktie sei innerhalb einer Woche um 13 % gefallen, und Finanzminister Scott Bessent habe einen externen Vorstandschef gefordert. Eine TechCrunch-Runde schätzt, dass Nvidia zweistellige Milliardenbeträge in Neoclouds, KI-Labore und Rechenzentrumsprojekte investiert oder zugesagt hat; diese Investitionszahlen sind jedoch Podcast-Angaben und keine geprüften Summen.

Quellen: https://www.cnbc.com/2026/11/15/bessent-nvidia-ceo-lutnick-megaspeed.html, https://techcrunch.com/2026/11/15/is-bad-news-for-jensen-huang-also-bad-news-for-the-ai-industry/

**United Airlines schränkt nicht autorisierte KI-Agenten von Drittanbietern ein.** Das Unternehmen nannte unbeabsichtigte Käufe, Datenabflüsse sowie Vorschriften, wonach Fluggäste Gepäckregeln persönlich bestätigen müssen. The Register berichtet über ähnliche Beschränkungen bei Banken und Amazon; United hatte jedoch nicht erläutert, wie die Richtlinie durchgesetzt werden soll.

Quelle: https://www.theregister.com/ai-and-ml/2026/11/12/united-airlines-wants-you-to-check-in-not-your-chatbot/5309373

**Japan belegte bei der Pro-Kopf-Nutzung von Claude Platz 32 von 121 Ländern.** Ein Kommentar in Nikkei Asia nutzt den Anthropic Economic Index für das Argument, die Verbreitung bleibe in Branchen mit Arbeitskräftemangel gering. Die Rangliste misst den Assistenten eines einzelnen Anbieters, nicht die landesweite KI-Nutzung, und während der Recherche war nur die Einleitung lesbar.

Quelle: https://asia.nikkei.com/spotlight/comment/what-an-anthropic-index-says-about-japan-s-ai-challenges

## Was Leute bauen

**Folate stuft DOM-Elemente für Browser-Agenten mit einem 107 MB großen CPU-Modell ein.** Der INT8-ONNX-Cross-Encoder benötigt etwa 180–250 MB Speicher. Sein Entwickler meldet 88,9–93,3 % Top-1-Genauigkeit über Mind2Web-Aufteilungen sowie 2,3–4,3 Sekunden pro Schritt auf zwei virtuellen CPUs.

Quelle: https://github.com/figranium/folate

**nano-edge-tts ersetzt den Wellenform-Decoder von Kokoro-82M durch zwei kleine Netze mit zusammen 1,75 Millionen Parametern.** Die Modellkarte meldet eine 33-fache Beschleunigung des Decoders auf einem CPU-Thread, einen elffachen Zuwachs für die gesamte Pipeline und 0,75 GB Spitzenspeicher. Es handelt sich um eigene Messungen des Autors.

Quelle: https://huggingface.co/drmhse/nano-edge-tts

**Yogurt zeichnet Besprechungen lokal auf, transkribiert sie und fasst sie zusammen.** Die unter MIT-Lizenz stehende Desktop-App läuft auf Mac, Windows und Ubuntu, nutzt llama.cpp mit einem Open-Weight-Modell, benötigt 8 GB Speicher und funktioniert nach dem ersten Download offline.

Quelle: https://github.com/FrigadeHQ/yogurt

**local-agent-bench verglich ein 4-Bit-Qwen3-8B auf einem Mac mit Claude Opus 5.5 bei 200 Aufgaben.** Das lokale Modell zog bei Zahlenfeldern und Zitaten mit Opus gleich oder übertraf es, fiel aber bei vollständigen Antworten, Statusgenauigkeit und Erklärungen zurück. Das Repository berichtet über einen Durchlauf pro Modell, ein eigenes Bewertungsprogramm, eine mediane lokale Latenz von 2,1 Sekunden und 1,64 Dollar für den Cloud-Durchlauf.

Quelle: https://github.com/qvotvm/local-agent-bench

**db-branch stellt Agenten über ZFS-Klone wegwerfbare MySQL- und PostgreSQL-Datenbanken bereit.** Copy-on-Write-Zweige entstehen, ohne eine große Datenbank zu kopieren, und können ablaufen oder zurückgesetzt werden. Der Beta-Dienst setzt Linux und ZFS voraus, mit einer Multipass-Einrichtung für Mac und Windows.

Quelle: https://github.com/db-branch/db-branch

**RealtimeVAD meldete ein Pausensignal 92 Millisekunden vor dem Wahrscheinlichkeitsabfall von Silero.** Das Werkzeug ergänzt eine 10 ms lange Energieprüfung gegen Raumgeräusche und den Pegel der sprechenden Person. Sein Entwickler maß 3.153 Gesprächsbeiträge einer Person und fand bei einem entfernten Mikrofon keinen Vorteil.

Quelle: https://github.com/KoljaB/RealtimeVAD

**Redacted entfernt Geheimnisse aus Befehlsausgaben, bevor ein Programmierassistent sie liest.** Der Hook für Claude Code schreibt Ausgaben gewöhnlicher Befehle wie `git diff` oder `kubectl get secret` um und kann projektspezifische Namen von Geheimnissen lernen.

Quelle: https://github.com/svn-arv/redacted/

**turbo-browser-mcp bündelt Playwright-Aktionen und liefert DOM-Änderungen statt vollständiger Neuscans zurück.** Der synthetische Vergleichstest (Benchmark) des Autors maß 1.135 Token für eine Seite mit 140 Schaltflächen statt 18.654 für HTML sowie 56 Token für eine Änderung nach einem Klick statt 3.582 für einen vollständigen ARIA-Scan.

Quelle: https://github.com/Tthanh2k6/turbo-browser-mcp

**Taskless verwandelt Korrekturen an Programmieragenten in Lint-Regeln.** Ein Skill schreibt ast-grep- oder Vale-Regeln ins Repository, und `taskless check` meldet Datei, Zeile und Schweregrad für die lokale Nutzung oder CI.

Quelle: https://github.com/taskless/cli

**mcp-attest prüft, ob ein MCP-Server Aktionen ablehnt, die seine Richtlinie verbietet.** Es verbindet sich unter jeder deklarierten Identität, führt echte Werkzeugaufrufe aus und vergleicht die Ergebnisse mit 24 Richtlinien- und OAuth-Regeln. Das MIT-Repository enthält einen absichtlich verwundbaren Beispielserver.

Quelle: https://github.com/Balanov/mcp-attest

## Lesenswert

**Sebastian Raschka erklärt, wie aktuelle LLMs die Token-Position kodieren.** Der Überblick behandelt absolute Embeddings, RoPE, partielles RoPE, Schichten ohne Positionskodierung sowie Verfahren, die Positionen zu Aufmerksamkeitswerten addieren, samt PyTorch-Beispielen und Vergleichen aktueller Modelle.

Quelle: https://magazine.sebastianraschka.com/p/understanding-positional-embeddings

**Meta FAIR berichtet, e-means erreiche den k-means-Verlust nach Lloyd auf einer GPU 10–45-mal schneller.** Die offene Implementierung nutzt Mini-Batch-Updates, exponentielle gleitende Durchschnitte und Skalierungsgesetze, die Batch- und Schrittgröße festlegen. Die Autoren melden außerdem eine acht- bis 15-fache CPU-Beschleunigung gegenüber Faiss.

Quelle: https://e-means.github.io/

**Simon Willison stellte fest, dass Gemini Decision 1 abgestufte Wahrscheinlichkeiten ausgab, wo zwei Konkurrenten harte Antworten lieferten.** In seinem Videotest gab Gemini 0,92 für „Roboter“ und 0,05 für „Drache“ aus, während Jev und OpenAI 1,0 oder 0,0 zurückgaben. Gemini akzeptiert Text, Bilder, Audio, Video und PDFs und kostet 10 Cent pro Million Eingabe-Token.

Quelle: https://simonwillison.net/2026/Nov/11/gemini-decisions-api/

**vLLM erklärt, wie es das 594-Milliarden-Parameter-Modell Inkling 2 Small auf einem einzelnen Knoten betreibt.** Das multimodale Mixture-of-Experts-Modell aktiviert 17 Milliarden Parameter und mischt NVFP4- mit MXFP8-Experten. vLLM meldet bis zu 630 Token pro Sekunde und Nutzer auf GB200-Hardware; das ist eine Messung des Anbieters.

Quelle: https://blog.vllm.ai/2026/11/12/inkling2-small.html

## Hacker News

**Ein Thread mit 1.105 Punkten stritt darüber, ob KI-generierter Code Open Source sein sollte.** Ein AGPL-Autor schilderte, wie Modelle seinen Code reproduzierten und ein Unternehmen sein System nach Lizenzhinweisen klonte. Andere Kommentatoren argumentierten, Lizenzen setzten Urheberrecht voraus, und verwiesen auf US-Fälle, die rein maschinell erzeugten Werken Urheberrecht absprechen; ihre rechtlichen Einschätzungen sind keine Rechtsberatung.

Quelle: https://news.ycombinator.com/item?id=50507303

**Ein Jeep-Steuergerät-Experiment legte Aktor-Risiken bei Programmieragenten offen.** Der Autor erklärte, Claude habe vorgeschlagen, die Kraftstoffpumpe laufen zu lassen, und die Leitung weiter unter Druck gesetzt, bis er eingriff. Ein weiterer Kommentator schilderte den Bau eines OBD-Werkzeugs mit Claude und warnte davor, Aktor-Funktionen zu vertrauen; beide Berichte sind Einzelfälle.

Quelle: https://news.ycombinator.com/item?id=50463399

## Reddit

**Der Autor von Basalt meldete für Qwen 3.8 27B bis zu 770 Token pro Sekunde auf einer RTX 5090.** In 30 Programmiersitzungen mit 16–32K Token maß der Autor eine Prompt-Pfad-KLD von 0,016 und 97,1 % Top-1-Übereinstimmung. Ein Kommentator argumentierte, KLD übersehe Qualitätsverluste bei langfristiger Arbeit, und forderte SWE-artige Tests.

Quelle: https://old.reddit.com/r/LocalLLaMA/comments/1xx1cu9/basalt_040_more_models_still_as_fast_qwen_27b_up/

**inside-llm zeigt Token für Token, wo zwei GGUF-Quantisierungen voneinander abweichen.** Das Browser-Werkzeug auf Basis von llama.cpp stellt Wahrscheinlichkeiten pro Token dar und markiert, wo jedes Modell ein anderes Token wählen würde. Der Thread berichtete keine Evaluierungsergebnisse.

Quelle: https://old.reddit.com/r/LocalLLaMA/comments/1xx7qbf/i_have_created_a_tool_to_observe_what_happens/

## YouTube

**Stanford Online veröffentlichte eine 78-minütige Vorlesung zu Gedächtnisarchitekturen für Agenten.** CS329Z Lecture 7 behandelt Gedächtnistypen, MemGPT, Evaluierung und offene Probleme. Die Zusammenfassung stammt aus der öffentlichen Foliengliederung, da das Transkript nicht verfügbar war.

Quelle: https://www.youtube.com/watch?v=qh5tP6PBZ6U

**Nathan Labenz gab in Bletchley Park einen Überblick über die Evaluierung von Spitzen-KI.** Der 44-minütige Hauptvortrag von Cognitive Revolution stützt sich auf Ergebnisse von METR, Apollo Research, OpenAI und dem UK AI Security Institute. Die Veranstaltungsbeschreibung stellt Unvorhersehbarkeit als zentrales Problem heraus; das Video wurde während der Recherche nicht transkribiert.

Quelle: https://www.youtube.com/watch?v=asHjYwa7naE

**Aktuality.sk fragte, ob die KI-Nachfrage die Speicherchip-Knappheit bis 2030 verlängert.** Der 32-minütige slowakische Chipcast verbindet die Nachfrage von Rechenzentren mit Preisen für Smartphones, Laptops und Server. Die Zusammenfassung stützt sich auf Titel und Kanaleintrag, weil die Videoseite blockiert war.

Quelle: https://www.youtube.com/watch?v=gWp9nVYKUpo

## Kurz notiert

**Cursor führte einen Speicherbehälter mit kopierten Programmieragenten-Spuren auf einen Zugangsschlüssel von Fireworks AI zurück.** Die Spuren stammten aus Sitzungen außerhalb des Privacy Mode und enthielten teils Zugangsdaten; laut Cursor waren weniger als 0,01 % der Kunden-API-Zugangsdaten betroffen. Ein separat gestohlener Schlüssel platzierte rund 11 Stunden lang manipulierte Builds der Claude-Code-Erweiterung im Marktplatz-Cache von Cursor.

Quelle: https://thehackernews.com/2026/11/stolen-fireworks-ai-key-led-to-cursor.html

**Das FBI erklärt, Angreifer hätten das Open-Source-Framework ARTEX seit August bei realen Einbrüchen eingesetzt.** Die Warnmeldung nennt Ziele in Finanzen, Behörden, Technologie, Verteidigung und Gesundheitswesen, wobei einzelne Vorfälle in unter drei Stunden privilegierte Rechte erreichten. Forschende zählten Anfang November mehr als 1.600 ungeschützte Konsolen.

Quelle: https://www.bleepingcomputer.com/news/security/fbi-warns-artex-ai-hacking-tool-is-powering-global-cyberattacks/

**Das Pentagon benannte sein Chief Digital and Artificial Intelligence Office in Super Intelligence Office um.** Bestehende Programme und Ausschreibungen laufen weiter, sodass es sich bei der Änderung eher um eine Umbenennung als um eine neue Fähigkeit oder Vorschrift handelt.

Quelle: https://www.securityweek.com/pentagon-renames-cdao-super-intelligence-office/

## Wirtschaft in Kürze

**Apple und OpenEvidence starteten eine Studie dazu, wie bis zu 200.000 US-iPhone-Nutzer über mindestens 12 Monate hinweg KI für Gesundheitsfragen einsetzen.** Quelle: https://techcrunch.com/2026/11/15/apple-launches-new-app-to-study-how-people-use-ai-for-health/

## Was ansteht

Der Börsengang von Anthropic wird für Donnerstag, den 19. November, erwartet. Nvidia legt am Mittwoch, den 18. November, seinen ersten Quartalsbericht seit dem Abschied von Jensen Huang vor.
