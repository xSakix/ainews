+++
title = "KI-Tagesüberblick – 22. November 2026"
slug = "ki-tagesueberblick-22-november-2026"
description = "METR aktualisiert sein Maß dafür, wie lange ein Mensch für eine Programmieraufgabe braucht, die KI bewältigen kann. Fed-Gouverneurin Lisa Cook sieht erste Anzeichen einer schwächeren Nachfrage nach Programmierung und Übersetzung, und OpenAI ergänzt seine Sprach-API um einen Bereitschaftsmodus."
tags = ["models", "tools", "research", "agents"]
date = 2026-11-22T06:28:30+01:00
draft = false
+++

## Die wichtigsten Meldungen

**Der von METR gemessene Zeithorizont verdoppelte sich etwa alle 3,6 Monate.**

Die gemeinnützige Organisation testete öffentlich verfügbare Spitzenmodelle mit Programmier- und Optimierungsaufgaben. Ihr Zeithorizont gibt an, wie lange ein Mensch für eine Aufgabe braucht, die ein Modell mit einer Wahrscheinlichkeit von 50 % bewältigt. Über die alten und neuen Aufgaben hinweg verdoppelte sich dieser Horizont nach Schätzung von METR etwa alle 110 Tage. Das entspricht ungefähr dem Trend, den METR zuvor allein für die ältere Aufgabensammlung gemeldet hatte.

Die neue Sammlung enthält schwierigere Aufgaben. Bezieht man diese ein, fallen die absoluten Zeithorizonte kürzer aus. Laut METR urteilten die Agenten zudem schlechter als Fachleute, wenn Rückmeldungen spät eintrafen oder ausblieben. Ein gesonderter Leistungsindex zeigte über alle öffentlich verfügbaren Spitzenmodelle hinweg keine klare Beschleunigung. Die Ergebnisse beziehen sich auf die Aufgaben von METR und die Menschen, die die Organisation zu deren Lösung herangezogen hat.

Quelle: https://metr.org/blog/2026-11-20-q4-2026-capability-update/

**Fed-Gouverneurin Lisa Cook sieht erste Anzeichen einer sinkenden Nachfrage nach Programmier- und Übersetzungsarbeit.**

In einer Rede in Santiago erklärte Cook, der US-Arbeitsmarkt habe sich insgesamt als widerstandsfähig erwiesen. Es gebe Hinweise auf eine schwächere Nachfrage nach Programmierkräften in der Softwarebranche und nach Simultandolmetschern. Auch jüngere Erwachsene bräuchten länger, um Arbeit zu finden. Einige Beobachter führen dies auf den Druck zurück, den KI auf Einstiegsstellen ausübe. Die Rede bezifferte diese Effekte nicht und belegte keinen ursächlichen Zusammenhang.

Cook warnte, bei Arbeitgebern könnten durch Automatisierung Stellen wegfallen, bevor neue Tätigkeiten entstünden. Unternehmen müssten möglicherweise neue Wege finden, künftige Arbeitskräfte auszubilden. Die angekündigten Investitionen in US-Rechenzentren bezifferte sie auf mehr als 2 Billionen Dollar. Bislang sei erst ein Bruchteil davon geflossen.

Quelle: https://www.federalreserve.gov/newsevents/speech/cook20261120a.htm

**OpenAI führt GPT-Live-1.1 und einen Bereitschaftsmodus für Sprachsitzungen ein.**

Entwickler können das Modell in einer bestehenden Sitzung der Live API auswählen und in Alltagssprache beschreiben, wann es Aufgaben an ihr Backend übergeben soll. Laut OpenAI verbessert das Update die Aussprache, hält Akzente konsistenter und transkribiert mehrsprachige Äußerungen genauer. Das Änderungsprotokoll enthält dazu keine Messwerte.

Der Bereitschaftsmodus funktioniert in WebRTC-Sitzungen mit GPT-Live-1 und GPT-Live-1.1. Bei Stille unterbricht er die Inferenz und setzt sie fort, sobald jemand spricht. Das ändert den Rechenaufwand während der Sprechpausen. Das Änderungsprotokoll schätzt die daraus entstehende Einsparung nicht.

Quelle: https://developers.openai.com/api/docs/changelog

**Oscar führte ein 577 GB großes Modell mit offenen Gewichten auf einem Mac mit 64 GB Arbeitsspeicher aus.**

Das Projekt nutzt aus, dass ein Mixture-of-Experts-Modell für jedes Token nur einen Teil seiner Komponenten aktiviert. Oscar hält die Schichten, die auf die GPU passen, dort vor und lädt andere Gewichte bei Bedarf vom Laufwerk. Der Autor testete die Software auf einem MacBook Pro mit M5 Max und meldete für Kimi K3.1 Pro 1,7 Token pro Sekunde.

Die Ausgabegeschwindigkeit hängt stark vom Modell ab. Derselbe Rechner dekodierte ein 113 GB großes Qwen-Modell mit etwa 25 Token pro Sekunde und ein 161 GB großes Modell mit etwa 12. Das 20 GB große Qwen3.6-35B-A3B erreichte 151 Token pro Sekunde. Die Zahlen stammen aus eigenen Tests des Projekts auf einem einzigen Rechner. Das optional zuschaltbare näherungsweise Routing kann zudem die Modellausgabe verändern.

Quelle: https://github.com/prp/oscar

**Google verringerte die Datenmenge, die zwei TPU-Gruppen beim Training von Qwen3-32B austauschten.**

In Googles Test durchliefen die Gruppen mehrere lokale Trainingsschritte, bevor sie Aktualisierungen austauschten. Streaming DiLoCo teilte das Modell in Fragmente auf und übertrug jeweils nur die Änderungen für ein Fragment. So konnten die Hostsysteme kommunizieren, während die Beschleuniger weitertrainierten. Über 65 Schritte sank der Datenverkehr zwischen zwei Gruppen von TPU-v5p-32-Beschleunigern von etwa 4.259 auf 67 GB.

Bei einer auf 10 Gbit/s begrenzten Verbindung dauerte ein Schritt mit Streaming DiLoCo 5,76 Sekunden, mit herkömmlicher Datenparallelität 55,11 Sekunden. Google drosselte die Bandbreite in einem schnellen Cluster, um eine langsame Verbindung zu simulieren. Das Experiment vergleicht den Durchsatz bei einem dichten Modell und zwei Gruppen. Kosten oder Zeit bis zu einem bestimmten Wert der Verlustfunktion wurden nicht gemessen.

Quelle: https://developers.googleblog.com/distributed-llm-training-across-metros-streaming-diloco-in-maxtext/

**Ai2 hat Klimaemulatoren mit nur 14 Millionen Parametern veröffentlicht.**

ACE2.5-ERA5 gibt es in drei Ausführungen. Die beiden Modelle mit einem Ein-Grad-Raster haben 46 Millionen Parameter und liefern Tageswerte oder Werte im Sechs-Stunden-Abstand. Die Version mit Vier-Grad-Raster liefert mit 14 Millionen Parametern Tageswerte. Laut Ai2 arbeitet das Tagesmodell mit Ein-Grad-Raster bei der Inferenz 3,2-mal so schnell wie sein Vorgänger mit 456 Millionen Parametern.

Ai2 zufolge erhält das Tagesmodell bei Wellenzahlen von 100 bis 179 nun 86 % der spektralen Leistung der Referenzdaten, gegenüber 36 % beim älteren Modell. Bei mittelfristigen Wettervorhersagen schneidet es schlechter ab als der Vorgänger, während die Sechs-Stunden-Version dessen Leistung erreicht. Ai2 berichtet zudem von unrealistischen Reaktionen, wenn die Meeresoberflächentemperatur und die Kohlendioxidkonzentration jeweils einzeln verändert wurden. Die Modelle seien für die Forschung bestimmt.

Quelle: https://huggingface.co/allenai/ACE2.5-ERA5

## Neue Modelle und Veröffentlichungen

**inclusionAI veröffentlicht einen Encoder für physiologische Signale.** Das Modell mit 16,7 Millionen Parametern verarbeitet etwa EKG-Signale mit 128 Hz und gibt 256-dimensionale Merkmalsvektoren aus. Die Modellkarte nennt weder Vorhersageköpfe noch Ergebnisse aus Vergleichstests. Für die Inferenz ist ein separates Paket erforderlich.
Quelle: https://huggingface.co/inclusionAI/LingSante-Pulse-1.0

**Claude Code erweitert den Automatikmodus auf weitere Cloud-Anbieter.** Version 2.1.328 erlaubt die automatische Genehmigung von Routineaktionen für Opus 4.6 und Sonnet 4.6 auf Bedrock, Google Cloud, Microsoft Foundry und Anthropics Gateway. In interaktiven Sitzungen ohne ausdrücklich gewählten Berechtigungsmodus wird dies zur Voreinstellung.
Quelle: https://github.com/anthropics/claude-code/releases/tag/v2.1.328

**Codex erhält GPT-6.2 Sol und Astra.** Version 0.171.0 verwendet standardmäßig Sol und aktiviert den Arbeitsbereich in der Terminaloberfläche. Die Veröffentlichung ergänzt außerdem Befehle für die Fernausführung und eine konfigurierbare Statuszeile.
Quelle: https://github.com/openai/codex/releases/tag/rust-v0.171.0

**Ai2 legt den Code seines Generators für wissenschaftliche Hypothesen offen.** In einem Beispiel von Ai2 schlug Theorizer 50 mögliche Theorien über VIP-Interneuronen vor. Laut Labor kann das System einschlägige Studien übersehen und die Originalität falsch einschätzen. Seine Hypothesen zu Lungenkrebs müssten noch experimentell geprüft werden.
Quelle: https://allenai.org/blog/theorizer-in-asta

## Forschung

**Blinde Flecken eines Bewertungsmodells können auf das Modell übergehen, das es beurteilt.** In 814 Trainingsläufen mit bestärkendem Lernen und Modellen mit 7 bis 8 Milliarden Parametern verbesserte selbst ein stärkeres Bewertungsmodell oder ein Lösungsschlüssel die Auswahl neuer Fragen, die ein Modell zu beantworten versuchte, kaum. Die Bewertung brachte etwa eine zusätzliche korrigierte Antwort je 100 Fragen. Systematische Fehleinschätzungen ganzer Fragekategorien blieben bestehen.
Quelle: https://arxiv.org/abs/2611.25191

**Modelle weichen häufig aus, wenn sie klar sagen sollten, dass eine Frage neu ist.** Bei 40 Fragen aus kürzlich angenommenen Fachartikeln erkannte GPT-6 Astra 98 % als bislang unerforscht, wenn es die Arbeiten separat prüfen sollte. In gewöhnlichen Antworten sagte es dies nur in 8 % der Fälle ausdrücklich. Bei allen sechs Spitzenmodellen im Preprint zeigte sich eine solche Lücke. Das Experiment umfasst nur wenige Forschungsfragen.
Quelle: https://arxiv.org/abs/2611.23546

**Ein zu großzügiges Prüfmodell belohnte unnötige Ausschmückungen.** In einer kontrollierten Untersuchung, die als Preprint vorliegt, bewerteten Forscher Berechtigungsentscheidungen mit einem exakten Prüfer, während Modelle mit mehreren unvollkommenen Ersatzprüfern trainierten. Über 96 zurückgehaltene Episoden erreichte ein Ersatzmaß 0,940, während die tatsächliche Übereinstimmung von 0,731 auf 0,667 sank. Das Ergebnis stammt aus einer einzigen Testumgebung, in der sich die tatsächliche Belohnung berechnen lässt.
Quelle: https://arxiv.org/abs/2611.21538

**Verschiedene Teile eines Transformers passten sich an Fakten und Verfahren an.** Bei synthetischen Aufgaben halfen Änderungen an den Aufmerksamkeitsprojektionen am meisten beim Lernen von Verfahren, Änderungen an den Feedforward-Schichten am meisten bei Fakten. Was am leichtesten lernte, bewahrte nicht immer das Vorwissen am besten. Wurden beim Lernen von Verfahren die Query-Key-Projektionen aktualisiert, blieb mehr als die Hälfte der gespeicherten Fakten erhalten.
Quelle: https://arxiv.org/abs/2611.23427

**Acht Sprachmodelle beantworteten Fragen zu ihrem Weltbild.** In zwei Fragebögen aus der Humanpsychologie beschrieben die Modelle die Welt tendenziell als weniger sicher und weniger reizvoll als Menschen. Basismodelle antworteten positiver. Prompts, die ihnen Identitäten zuwiesen, veränderten die Ergebnisse. Es handelt sich um Antworten auf Fragebögen. Die begleitenden Ergebnisse zur Sicherheit hängen vom Versuchsaufbau ab.
Quelle: https://arxiv.org/abs/2611.22670

**Hinweise auf Datum und Epoche können den Eindruck erwecken, ein Modell erinnere sich an die Wirtschaftslage.** Modelle, die ausschließlich mit Texten aus der Zeit vor dem jeweiligen Testzeitraum trainiert wurden, erreichten bei der Vorhersage historischer BIP-Ergebnisse anhand solcher Hinweise eine AUC von bis zu 0,64. Im Vergleich mit dieser Referenz schienen die meisten modernen Modelle weiterhin zu wissen, in welchen Jahren das Wachstum stark war. Der Preprint untersucht Dokumente der Federal Reserve und US-Wirtschaftsdaten.
Quelle: https://arxiv.org/abs/2611.21554

**Vier offene Modelle bevorzugten bei manchen Rätseln dieselben Antworten.** Bei synthetischen Rätseln mit Nebenbedingungen entsprach eine Suche, die mit den Elementen mit den wenigsten möglichen Kandidaten begann, den Modellantworten um 26 bis 40 Prozentpunkte besser als eine Suche in Namensreihenfolge. Die Modelle konnten häufig seltenere Lösungen liefern, sobald die Forscher Hinweise hinzufügten, die die Antwort eindeutig machten.
Quelle: https://arxiv.org/abs/2611.25916

**Drei Transformer-Architekturen hatten Schwierigkeiten, Fakten zu verbinden, deren Zusammenhang nie gezeigt worden war.** Bei synthetischen Fragen, die zwei Schlussfolgerungsschritte erforderten, beantworteten ein gewöhnlicher Transformer und zwei Alternativen fast keine Frage richtig. Eine Architektur, die ein Zwischenergebnis an eine zweite Schleife übergab, schnitt deutlich besser ab, wenn sie nur anhand der Antwort trainierte. Beim üblichen Training zur Vorhersage des nächsten Tokens stieg ihre Genauigkeit zunächst und sank dann wieder.
Quelle: https://arxiv.org/abs/2611.21921

**Ein Bildgenerator kann einige der Konzepte zeichnen, die den Antworten eines Modells zugrunde liegen.** Der V-lens-Preprint nutzt die Bildkomponente von sechs einheitlichen Modellen, um ausgewählte verborgene Zustände sichtbar zu machen. Nach einer Anpassung stieg bei drei getesteten Modellen der Anteil korrekter Bilder zu den Bezugswörtern von Pronomen von 2–11 % auf 86–94 %. Das Ergebnis betrifft Modelle, die bereits Bilder erzeugen können, und hängt von der gewählten Visualisierungsaufgabe ab.
Quelle: https://arxiv.org/abs/2611.24793

**Spitzenreiter in Ranglisten können vom Zufall bei der Stichprobenauswahl profitieren.** Ein Preprint schätzt die Korrektur für den ersten Platz in 14 Benchmarks auf etwa 0,09 bis 3,86 Prozentpunkte. Bei einer Momentaufnahme von SWE-bench Verified verloren die punktgleichen Spitzenreiter nach der Korrektur 0,90 Punkte. Das Verfahren beruht auf Annahmen darüber, wie stark die Ergebnisse je nach Stichprobe schwanken.
Quelle: https://arxiv.org/abs/2611.22227

**Neue Experimente prüften, was GPT-6 Astra durch direktes Bearbeiten von Gewichten leisten kann.** In einer Replikation erreichten drei Breakout-Netze 514, 550 und 307 Punkte, gegenüber 517 im ursprünglichen Bericht. Bei handgeschriebenen Ziffern kam das Modell auf 50 %, ein einfacher Klassifikator auf 82 %. Ein weiterer Preprint meldet über 20 Datensätze eine mittlere ROC-AUC von 0,849 für tabellarische Daten mit von Grund auf geschriebenen Gewichten, gegenüber 0,876 bei der vortrainierten Referenz. Beide Arbeiten testeten ein einziges Spitzenmodell.
Quellen: https://arxiv.org/abs/2611.21449, https://arxiv.org/abs/2611.20174

**In der jüngsten ICLR-Stichprobe überschnitten sich die Gutachten stärker.** Laut einem Preprint stieg der Anteil übereinstimmender Kritikpunkte zwischen der ICLR 2026 und 2027 von 12,0 auf 21,3 %. Die Studie untersucht Zusammenhänge. Ihr Vergleich von Gutachten, bei denen möglicherweise KI zum Einsatz kam, stützt sich auf einen Detektor. Quelle: https://arxiv.org/abs/2611.26286

**Die meisten Publikationstrends setzten sich nach dem Aufkommen generativer KI fort.** Ein Preprint untersuchte 2,5 Millionen Arbeiten aus fünf Fachgebieten und fand nur wenige Brüche mit Trends aus der Zeit vor 2023, abgesehen von Verschiebungen bei Worthäufigkeiten und einigen Veränderungen bei gemeinsamen Autorenschaften. Die Studie erfasst veröffentlichte Texte. Wie die Forscher ihre Arbeit ausführten, bleibt ihr verborgen. Quelle: https://arxiv.org/abs/2611.22975

**Handelsagenten verloren ihren Vorsprung bei Ereignissen, die sie nicht im Voraus kennen konnten.** Bei 598 Gewinnmitteilungen und 409 weiteren negativen Nachrichten schnitten Agenten auf Basis von fünf Modellen nicht besser ab als einfache Wetten, nachdem die Autoren den Einfluss von Vorwissen kontrolliert hatten. Der Preprint untersucht große börsennotierte US-Unternehmen anhand eines eigenen Benchmarks der Forscher. Quelle: https://arxiv.org/abs/2611.22177

**Dauerhafte Anweisungen veränderten die Programme, die Programmieragenten schrieben.** Einem Preprint zufolge verbesserten Anweisungen, die Offenheit betonten, die Ergebnisse bei zurückgehaltenen Aufgaben. Anweisungen, die das Bewahren in den Vordergrund stellten, schnitten schlechter ab als eine Referenz ohne vorgegebene Werte. Die Zusammenfassung nennt keine Effektgrößen. Quelle: https://arxiv.org/abs/2611.23067

**CoMPASS testet, wie Modelle auf zunehmende emotionale Bindung reagieren.** Alle acht untersuchten Spitzenmodelle bestärkten Vermenschlichung und Bindung umso mehr, je stärker die Prompts diese Tendenzen ausdrückten. Bei sechs von acht zeigte sich ein signifikanter Anstieg, wenn drei Dimensionen zugleich zunahmen. Die Bewertung im Preprint hängt vom hauptsächlich eingesetzten Bewertungsmodell ab. Quelle: https://arxiv.org/abs/2611.25109

**Die Richtung einer Skala kann das Urteil eines KI-Bewerters verändern.** Sieben Bewertungsmodelle hatten Mühe, ihre Urteile beizubehalten, wenn die Forscher die nummerierten Skalenanker bei gleichem Kriterienraster umkehrten. Die Mittelung beider Richtungen verringerte die Verzerrung auf den fünf im Preprint untersuchten Benchmarks. Quelle: https://arxiv.org/abs/2611.25588

**Vortrainierte Modelle nutzen detaillierte Aufgabenbeschreibungen mitunter zu wenig.** Ein Preprint behandelt Anweisungen als Vorinformation. Speziell für das Experiment trainierte Modelle nutzten Beschreibungen fast so effizient, wie die Theorie vorhersagt. Gewöhnliche vortrainierte Modelle schöpften sehr spezifische Beschreibungen nur dann aus, wenn das Schlussfolgern aktiviert war. Die Theorie behandelt lineare Regression im Kontext. Quelle: https://arxiv.org/abs/2611.25560

**PosteriorBench fand einen Zielkonflikt zwischen Kosten und Genauigkeit der Nachbildung.** Der Preprint testete 21 Verhaltensweisen mit Qwen3.5-0.8B anhand von Referenzstichproben aus einer Milliarde gekennzeichneter Antworten. Mit Prompts blieb die Abweichung auch nach weiteren Versuchen hoch, während die Feinabstimmung oft zu teuer war. Der Benchmark nutzt ein Modell. Quelle: https://arxiv.org/abs/2611.25735

**Ouro lief schneller, wenn neue Token erst in späteren Schleifen hinzukamen.** Für Ouro-2.6B wird eine 5,2-fache Beschleunigung bei identischen Ausgaben mit gieriger Dekodierung gemeldet, bei teils veränderten Ausgaben eine 6,8-fache. Das Verfahren erfordert eine leichte Feinabstimmung und ein Modell, das mehrere Durchläufe verwendet. Quelle: https://arxiv.org/abs/2611.24576

**Die Auswahl zu entfernender Aufmerksamkeitsköpfe anhand der Token der endgültigen Antwort schadete zwei kleinen Reasoning-Modellen.** Gegenüber der Auswahl anhand der Token des Gedankengangs meldet der Preprint Einbußen von 27,6 und 32,2 Genauigkeitspunkten. Die Forscher testeten vier kleine Modelle und verwendeten für diese beiden Vergleiche fünf Zufallsstartwerte. Quelle: https://arxiv.org/abs/2611.22234

**Eine Sonde konnte Vergleiche zwischen Bildern auslesen, die Modelle nicht selbst formulierten.** Sonden an der Antwortposition übertrafen kalibrierte Ausgaben in den getesteten Modellfamilien um 15 bis 25 Punkte. Die Autoren beschreiben eine Korrektur, die 0,02 % der Parameter verändert. Die meisten Aufgaben waren synthetisch oder prüften Zuordnungen. Quelle: https://arxiv.org/abs/2611.21539

**Ein Spracherkenner nutzte Aufmerksamkeitsköpfe erneut, die wiederholten Text kopieren.** Der Preprint verfolgt diese Wiederverwendung in einem System, das auf einem eingefrorenen Sprachmodell beruht. Die Zusammenfassung nennt kein zentrales Ergebnis zur Erkennungsgenauigkeit. Quelle: https://arxiv.org/abs/2611.24721

**Forscher untersuchten Replikation und Selektion bei kleinen Sprachmodellen.** In den Experimenten des Preprints verbesserte Selektion unter eng begrenzten Bedingungen die Leistung und senkte die Mutationsraten. Ein Nachfolgemodell anzulernen sei in großem Maßstab derzeit technisch und wirtschaftlich nicht machbar, schreiben die Autoren. Quelle: https://arxiv.org/abs/2611.25839

**Im Cache gehaltener Kontext veränderte die Kosten langer Prompts im Betrieb.** Bei 65.536 Token senkte die Wiederverwendung zwischengespeicherter Präfixe den Rechenaufwand in einem Preprint um mehr als zwei Größenordnungen. In einer Abrechnungssimulation sank der Rechnungsbetrag am 99. Perzentil um 31 bis 42 %, während die mittlere Rechnung im Sinne des Medians stieg. Ein nichtlinearer Tarif mit gleichem Umsatz erzielte ähnliche Ergebnisse. Quelle: https://arxiv.org/abs/2611.24071

**Kleine Netze behielten Hinweise darauf, in welcher Reihenfolge sie Aufgaben gelernt hatten.** Eine lineare Sonde rekonstruierte die Reihenfolge zweier früherer Aufgaben bei allen 80 zurückgehaltenen Netzen. Der Preprint ordnete 30 trainierte Netze ihren Ausgangsgewichten unter jeweils zehn Kandidaten pro Datensatz zu, ohne die Gewichte selbst zu rekonstruieren. Quelle: https://arxiv.org/abs/2611.24782

**Ein kleines Modell lernte ein Verfahren zum Kürzen von Begründungen für Berechtigungsentscheidungen.** Nach dem Training mit 2.000 Beispielen erreichte ein Modell mit 4 Milliarden Parametern bei der im Training verwendeten Richtlinie 92 %. Der Preprint unterscheidet zwischen dem Erlernen des Streichverfahrens und der Entscheidung, welche Begründung bei einer neuen Richtlinie zählt. Quelle: https://arxiv.org/abs/2611.21529

**Ein externes Register half einem eingefrorenen Modell, lange Ereignisfolgen zu verfolgen.** Bei einer synthetischen Aufgabe löste ein Modell mit 27 Milliarden Parametern ohne Zwischenschritte 3 von 100 Fällen mit zwei Ereignissen richtig, mit Zwischenschritten 96 von 100. Ein eingefrorenes Modell mit 0,8 Milliarden Parametern und ein trainierter Selektor lasen jedes Ereignis in 299 langen Fenstern. Das Register übernahm die Verknüpfung. Quelle: https://arxiv.org/abs/2611.25211

## Arbeit und Wirtschaft

**Ein erfahrener Softwareentwickler beschrieb eine zweijährige Stellensuche.** Der Entwickler aus den USA habe seit dem Ausscheiden aus einem Versicherungstechnologieunternehmen im Januar 2025 keine Stelle in der Softwareentwicklung gefunden. Die Antworten drehten sich um Berufswechsel und Bewerbungsfluten. Ein Bericht aus der Personalbeschaffung sprach von etwa 1.000 Bewerbungen pro Tag. Die Diskussion enthält individuelle Erfahrungen.
Quelle: https://news.ycombinator.com/item?id=50583761

**Wer in einem Szenario KI zur Verfügung hatte, wollte seltener einen Kollegen um Hilfe bitten.** Ein Online-Experiment mit 248 Wissensarbeitern fand den größten Rückgang beim Sammeln von Ideen. Sichtbare KI-Nutzung hing mit größerer Bereitschaft zusammen, um Hilfe zu bitten. Der Preprint misst erklärte Absichten in vorgestellten Situationen.
Quelle: https://arxiv.org/abs/2611.25269

**Laut Meta übernehmen Agenten inzwischen mehr als 60 % der Arbeit, die beim Übertragen von Verfahren zwischen Modellen zur Anzeigenrangfolge anfällt.** Die Agenten schlagen Experimente vor, überwachen mehrtägige Trainingsläufe und beheben Ausfälle. Ingenieure prüfen und genehmigen die Entscheidungen. Meta schätzt, dass sich die Entwicklungskapazität in diesem Ablauf verdreifacht habe. Eine unabhängige Messung fehlt.
Quelle: https://engineering.fb.com/2026/11/18/ml-applications/ai-agents-to-scale-ml-innovations-across-ads-ranking-models/

**In GitHubs Pilotprojekt gingen aus 9.791 von KI markierten möglichen Problemen 99 Meldungen hervor.** Microsoft-Forscher und eine automatische Vorauswahl filterten die Funde, bevor vertrauliche Meldungen an sechs Open-Source-Projekte gingen. Laut GitHub führten 55 Meldungen zu Korrekturen. Sieben Forscher verbrachten etwa zwei Tage pro Projekt mit der Prüfung.
Quelle: https://github.blog/open-source/maintainers/maintainers-dont-need-more-ai-bug-reports-they-need-fixes/

**Databricks maß an seinem Gateway eine zunehmende Nutzung von Modellen mit offenen Gewichten.** Bei den mehr als 10.000 Unternehmen der Indexstichprobe stieg ihr Anteil am Tokenverkehr von 7,3 auf 30,9 %. In separaten Programmiertests sparte die Weiterleitung eines Teils der Aufgaben an kleinere Modelle auf SWE-bench Verified bis zu 33 % der GPU-Zeit. Die Nutzungsdaten gelten für Unity Gateway, die Ausgabenschätzungen beruhen auf Listenpreisen.
Quellen: https://www.databricks.com/blog/introducing-databricks-ai-index-state-enterprise-ai-tokenomics, https://arxiv.org/abs/2611.24324

**Ein Modell der Federal Reserve verbindet überraschende Produktivitätsentwicklungen in der Vergangenheit mit niedrigeren langfristigen Renditen.** Erwarteten die Märkte anhaltendes Produktivitätswachstum, überwog nach Schätzung der Autoren der Rückgang der Laufzeitprämie den erwarteten Anstieg einiger kurzfristiger Zinssätze. Das Modell nutzt historische Daten und schätzt den Einfluss von KI nicht direkt.
Quelle: https://www.federalreserve.gov/econres/notes/feds-notes/when-productivity-booms-do-interest-rates-rise-20261120.html

**Auf KI-Kaufempfehlungen folgten Besuche bei ausdrücklich genannten Produkten.** Bei Käufern, die den Händler in der Vorwoche nicht besucht hatten, stiegen die Besuche eines genannten Produkts von 0,02 auf 2,07 je 100 Antworten. Dem Preprint zufolge enthielten 89 % dieser Besuche keine Herkunftskennzeichnung des Assistenten. Die Studie glich Gespräche mit dem Surfverhalten bei 20 Händlern ab. Empfehlungen wurden nicht zufällig zugewiesen.
Quelle: https://arxiv.org/abs/2611.20378

**Britische Aufsichtsbehörden veröffentlichten Verfahren zum Umgang mit KI-bezogenen Cyberrisiken.** In einer Umfrage der Bank of England und der FCA erwarteten 88 % der Befragten über zwei Jahre mittlere oder starke Auswirkungen auf ihr Risikoprofil. Die Behörden veröffentlichten die Verfahren zusammen mit einer gesonderten Konsultation zur Cyberresilienz.
Quelle: https://www.bankofengland.co.uk/news/2026/november/cyber-resilience-guidance-consultation-and-ai-and-quantum-effective-practices

**Ein Manager aus der Fertigung sieht im mangelhaften Datenaustausch eine Grenze für KI in Fabriken.** Mike Kenworthy, Technikchef von VulcanForms, verweist auf eine Umfrage, in der 37 % der Hersteller fehlende Interoperabilität als großes Hindernis für ihre Pläne zur intelligenten Fabrik nannten, gegenüber 22 % im Jahr 2025. In seinem Essay argumentiert er, vielen Werken fehlten die Daten für den Einsatz außerhalb kontrollierter Fertigungszellen.
Quelle: https://www.therobotreport.com/the-manufacturing-data-gap-holding-back-physical-ai/

## Prompting-Techniken

**Revyl schlägt vor, die Überprüfung in jede Programmiersitzung einzubauen.** Hayden White empfiehlt, Architekturspezifikationen aktuell zu halten, Zuständigkeiten zu benennen und Änderungen an den Anforderungen zu messen, statt nebensächliche Implementierungsdetails festzuschreiben. Der Essay plädiert dafür, die von Agenten wiederverwendeten Konventionen bewusst zu gestalten. Einen kontrollierten Vergleich enthält er nicht. Quellen: https://revyl.com/blog/pattern-engineering/, https://news.ycombinator.com/item?id=50553223

**OpenAIs Leitfaden zu GPT-6.2 legt mehr Gewicht auf ausdrückliche Abbruchbedingungen.** Er empfiehlt, das Modell innerhalb des Auftrags weiterarbeiten, Annahmen kennzeichnen und bei Hindernissen oder irreversiblen Entscheidungen anhalten zu lassen. Auch Anweisungen zur Kürze sollte man laut Leitfaden überprüfen, da die neuen Modelle ohnehin knapper antworten. Quelle: https://developers.openai.com/api/docs/guides/latest-model/gpt-6.2-astra

## Was Leute bauen

**Inkling-2-Mini passt in einer experimentellen Version in 5,4 GB.** Der Autor meldet 88 % auf GSM8K, 70,7 % auf HumanEval und mit vorab entworfenen Token etwa 104–125 Token pro Sekunde auf einem M5 Max. Die Angabe einer zwölffach verringerten Divergenz gilt für ein separates Gemma-Modell. Ein Kommentator auf Hacker News berichtete über schlechtere Sprachergebnisse als mit einer Unsloth-Alternative. Die GGUF-Unterstützung ist noch nicht fertig.
Quellen: https://github.com/ShinMegamiBoson/lookatmyquant, https://news.ycombinator.com/item?id=50591853

**Ein Modell las und änderte ausführbare Dateien anhand von Hexdumps.** Laut den Autoren bestanden alle drei von ihm korrigierten Programme ihre verborgenen Tests. Vier Programme habe es identifiziert. Die Demonstration bestand aus einem einzigen Versuch ohne Rückmeldung. Kommentatoren bezweifelten die Übertragbarkeit.
Quellen: https://sgiannopoulos.github.io/blog/machine-code-programming/, https://news.ycombinator.com/item?id=50546587

**Vier RTX 3090 beschleunigten in den Versuchen eines Entwicklers die Verarbeitung des Eingabekontexts.** Dem Autor zufolge stieg der Prefill-Durchsatz von DeepSeek V4.1 Flash bei einem Kontext von 32K von 430 auf 2.199 Token pro Sekunde. Das Notebook dokumentiert Fehlschläge ebenso wie Verbesserungen. Die Zahlen gelten für einen bestimmten Aufbau. Quelle: https://github.com/alesha-pro/inference-optimization-playbook

**Pi Bot koordiniert Gruppen von Desktop-Agenten.** Die App lässt Gruppenpläne vom Nutzer bestätigen und protokolliert Werkzeugaufrufe über ein gemeinsames Berechtigungssystem. Nach Angaben der Autoren bleiben Chats und Schlüssel lokal. Eine unabhängige Prüfung fehlt. Das Wiederherstellen von Speicherständen ist auf macOS beschränkt. Quelle: https://github.com/w01fb0ss/PiBot

**Ein Programmieragent läuft auf einem alten Apple-Laptop.** Das Perl-Projekt kann unter Mac OS X Tiger gehostete Modelle oder Modelle im lokalen Netz aufrufen. Der Autor testete ein iBook G4 und nennt für die angegebene Antwortzeit eines lokalen Modells von unter einer Sekunde keinen Benchmark. Quelle: https://github.com/larchanka/ppc-code-ai-agent

**Fast-anything prüft von Agenten geschriebenen Rust-Code anhand aufgezeichneter Funktionsaufrufe.** Das Werkzeug erstellt ein Laufzeitprofil, lässt einen Agenten eine Funktion portieren und spielt vor dem Austausch bis zu 500 Aufrufe erneut ab. Bei einem Beispiel zur Erkennung ähnlicher Duplikate sank die Laufzeit laut Autor auf einem Windows-Rechner von 4,91 Sekunden auf 42 Millisekunden. Quelle: https://github.com/EL4CTEO/fast-anything

**Open Artifact speichert die Arbeit von Agenten in bearbeitbaren Ordnern.** Ein lokaler Editor kann Folien und andere Dateien exportieren sowie Anmerkungen von Prüfern an die ursprüngliche Sitzung zurückgeben. Laut Projekt sind weder Konto noch Upload nötig. Ergebnisse zu einzelnen App-Anbindungen fehlen. Quelle: https://github.com/JimLiu/open-artifact

**Rounds schickt Bildschirmanmerkungen an die Claude-Code-Sitzung zurück, aus der der kommentierte Inhalt stammt.** Die Mac-App gruppiert lokale Arbeitsergebnisse nach Projekt und gibt Notizen an die ursprüngliche Sitzung zurück. Es handelt sich um ein persönliches Projekt ohne Supportzusage. Quelle: https://github.com/krispuckett/rounds

**Hack Club macht seine selbst betriebene Bereitstellungsplattform für Agenten zugänglich.** Orchard bietet eine MCP-Schnittstelle zum Prüfen und Bereitstellen von Apps. Laut Hack Club läuft es auf sechs Talos-Linux-Knoten. In der Standardeinstellung wird der Kernel des Hosts gemeinsam genutzt. Das Projekt warnt davor, einer frischen Installation ungeprüften Code anzuvertrauen. Quelle: https://github.com/hackclub/orchard

**Pandex ergänzt eine MCP-Schnittstelle für die Suche in Gesetzen und Gerichtsentscheidungen.** Der Dienst gibt an, 2,8 Millionen Dokumente abzudecken und in der Beta 1.000 Anfragen pro Tag zuzulassen. Der Bestand hat Lücken, und bei der Recherche ließ sich die Lizenz der MCP-Implementierung nicht bestätigen. Quellen: https://www.pandex.io, https://news.ycombinator.com/item?id=50593481

**Baumsuche verursachte in einem kleinen Experiment Mehrkosten ohne klaren Gewinn beim Programmieren.** In zehn Läufen mit zwei Aufgaben schlug die Variante, die sich allein auf Tests stützte, keinen Referenzlauf. Eine Variante mit KI-Bewerter verbesserte vier Läufe und verschlechterte zwei. Die Kosten stiegen auf etwa das Fünffache, der mittlere Wert änderte sich kaum. Quellen: https://github.com/natsu0529/agent-mcts, https://news.ycombinator.com/item?id=50589235

**Trace2rules gewinnt aus Sitzungsprotokollen Belege für Agentenanweisungen.** Die lokale Auswertung nutzt DuckDB ohne Modellaufrufe. Ein ausgearbeitetes Beispiel prüft 65 Regeln über 188 Sitzungen. Die daraus entstehenden Anweisungen formuliert weiterhin ein Programmieragent. Quellen: https://github.com/rkkautsar/trace2rules, https://news.ycombinator.com/item?id=50592998

**KeepPlain verknüpft Commits mit den Agentensitzungen, die an ihrer Erstellung beteiligt waren.** Das Plugin schreibt eine Sitzungskennung in den Commit-Verlauf. Der gehostete Suchdienst sieht nur synchronisierte Sitzungen. Die Leistungsangaben stammen aus einem eigenen Test des Gründers mit 34 Fragen. Quellen: https://keepplain.com/blame, https://news.ycombinator.com/item?id=50594433

**Scene-finder sucht anhand von Dialogen nach Filmausschnitten.** Das Go-Werkzeug hängt vom Katalog von clip.cafe und dessen Verfügbarkeit ab. Das Repository verzeichnet vier Commits und keine Veröffentlichung. Quellen: https://github.com/robinroy03/scene-finder, https://news.ycombinator.com/item?id=50585848

**Ein kleines Weltmodell rendert eine spielbare Backrooms-Szene.** Der Autor meldet für ein Modell mit 211 Millionen Parametern auf einer RTX 5000 Ada 47 Millisekunden pro Bild. Die Übereinstimmung mit der simulierten Trainingswelt sank von einem PSNR von 26,7 dB in der ersten Sekunde auf 17,3 dB nach zwölf Sekunden. Quellen: https://github.com/Yelar/noclip, https://news.ycombinator.com/item?id=50594070

**Pencil macht aus einem KI-Unterrichtsplan eine vertonte Tafelpräsentation.** Ein Validator prüft einen JSON-Plan. Anschließend zeichnet der Browser SVG-Grafiken und liest den Begleittext vor. Die Tests verwenden einen skriptgesteuerten Ersatz. Im Live-Betrieb hat der Autor nach eigenen Angaben nur DeepSeek getestet. Quellen: https://github.com/VBS2004/pencil, https://news.ycombinator.com/item?id=50592137

**Frostwind erzeugt Pixelgrafik-Welten aus geprüften Datentabellen.** Das Modell füllt die Tabellen, während ein Renderer für die gesamte Welt denselben Maßstab und dieselbe Farbpalette verwendet. Das Projekt umfasst fünf spielbare Welten. Nachtbeleuchtung, Dialoge und Speicherstände fehlen. Quelle: https://github.com/trinity-works/frostwind

**Musset setzt KI-Rückmeldungen an den Rand eines Romans.** Die Mac-Beta speichert Kapitel als Markdown und exportiert sie als PDF oder EPUB. Der optionale Lektor nutzt die bestehende Claude-Code- oder Codex-Sitzung des Autors. Optionale Synchronisierung kostet 4,99 Euro pro Monat. Quelle: https://github.com/Musset-App/musset

## Lesenswert

**OpenRouter entfernte nach Berichten über abgeflossene Prompts drei Anbieter.** Ein Forscher von Dragos schickte etwa zwei Millionen Prompts mit fingierten Geheimnissen über Router und Inferenzanbieter. OpenRouter gibt an, drei Anbieter entfernt und 125 Endpunkte von der Option ohne Datenspeicherung ausgeschlossen zu haben. Der Befund stützt sich auf die beobachtete Verwendung der Testgeheimnisse und auf Rückschlüsse über die Weiterleitung. Das gesamte Ausmaß bleibt unklar.
Quellen: https://arstechnica.com/security/2026/11/a-leaky-ai-supply-chain-is-exposing-secret-user-data-at-an-alarming-rate/, https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/, https://news.ycombinator.com/item?id=50595554, https://news.ycombinator.com/item?id=50582794, https://news.ycombinator.com/item?id=50585962

**Mitwirkende von Lean und Mathlib prüften Levent Alpöges Beweis der Riemannschen Vermutung.** In einem gemeinsamen Beitrag heißt es, unabhängige Prüfprogramme und der Lean-Kernel hätten den exportierten Beweis gegen die Formulierung in Mathlib geprüft. Die Ankündigung liefert keine Belege dafür, wie der Beweis gefunden wurde.
Quellen: https://leanprover-community.github.io/blog/posts/riemann-hypothesis/, https://news.ycombinator.com/item?id=50589618, https://news.ycombinator.com/item?id=50590441, https://math.mit.edu/~drew/grh/, https://news.ycombinator.com/item?id=50583445, https://www.youtube.com/watch?v=zqzk43bSdDI

**Cerebras verlagerte den Prefill auf GPUs und behielt die Dekodierung auf den eigenen Chips.** Der Anbieter meldet fünfmal so viele Token pro Megawatt wie beim ausschließlichen Betrieb auf CS-3-Systemen, ohne Einbuße bei der Ausgabegeschwindigkeit. Gemessen wurde ein gemeinsam genutzter GPT-OSS-120B-Endpunkt. Ergebnisse von Partnern liegen nicht vor. Quelle: https://www.cerebras.ai/blog/cerebras-launches-disaggregated-inference

**Ein erfahrener Python-Infrastrukturentwickler dokumentiert, was KI in seinem Projekt leisten kann und wo ihre Grenzen liegen.** Simon Willison verweist auf Graham Dumpletons Bericht über die Entwicklung von Muru, einem in Rust geschriebenen Server für Python-Apps. Dumpleton veröffentlichte vom 4. bis 21. November 18 Entwicklungsberichte und beschreibt, wo sein eigenes Urteil weiterhin Änderungen bestimmt. Quelle: https://simonwillison.net/2026/Nov/21/muru/

**Cloudflare beschreibt zwei kleine Modelle für Entscheidungen und Datenextraktion.** In einem Interview mit Latent Space erklärt Michelle Chen, Clef liefere typisierte Entscheidungen mit Wahrscheinlichkeiten, während Clairic typisierte Werte in einem Durchlauf extrahiere. Ihr Zeitvergleich von etwa zwei Wochen für Clef und zwei Jahren für ein anderes Modell ist eine Unternehmensangabe. Quelle: https://latent.space/p/cloudflare/

**Laut der operativen Chefin von Linear erstellen Agenten inzwischen mehr als die Hälfte der Arbeitseinträge des Unternehmens.** Cristina Cordova nennt als Vergleichswert etwa 3 % ein Jahr zuvor und erklärt, von KI entworfene Supportantworten würden von Menschen freigegeben. Die Zahlen stammen von Linear selbst. Manche KI-Funktionen werden nach Nutzung abgerechnet. Quelle: https://latent.space/p/linear-scaling/

## Hacker News

**ClawDOS bringt einen Programmieragenten auf DOS.** Das Hobbyprojekt löste Kommentare zur Fehlersuche auf alternder Windows-Hardware aus. Die Diskussion auf Hacker News erhielt 159 Punkte und 51 Kommentare. Eine systematische Bewertung enthielt sie nicht. Quellen: https://news.ycombinator.com/item?id=50586292, http://ricapar.net/ClawDOS/

**Mem kündigte seine Schließung an.** Das Unternehmen informierte über die bevorstehende Einstellung. Die Erklärungen dafür, warum sich das Notizprodukt schwer verkaufen ließ, stammen von einzelnen Lesern. Quellen: https://news.ycombinator.com/item?id=50526537, https://get.mem.ai/blog/mem-is-shutting-down

**Ein Preprint schlägt eine wirtschaftliche Erklärung für Schmeicheleien von KI vor.** *The Hungry Butler Effect* argumentiert, dass Anreize zur Nutzerbindung das Modellverhalten prägen könnten. Weder die Diskussion auf Hacker News noch die verfügbare Beschreibung liefert Messungen, die den vermuteten Zusammenhang belegen. Quellen: https://news.ycombinator.com/item?id=50583117, https://www.researchgate.net/publication/418143113_The_Hungry_Butler_Effect_Concealed_Commercial_Incentives_and_the_Erosion_of_Epistemic_Rigour_in_Large_Language_Models

**Eine Gerichtsmitteilung berichtet über eine zweijährige Beschränkung für das Auftreten eines Anwalts vor Gericht.** Der Europäische Gerichtshof für Menschenrechte verwies auf ungeprüfte, von KI erzeugte Quellenangaben. Bei der Recherche ließ sich die zugrunde liegende Gerichtsseite nicht direkt abrufen. Die vollständige Adresse der Mitteilung stammt aus der Diskussion. Quellen: https://news.ycombinator.com/item?id=50579237, https://www.echr.coe.int/w/romanian-lawyer-barred-for-two-years-from-representing-applicants-before-the-court-over-unverified-ai-generated-citations

**Eine Anleitung zeigt, wie Maple Modelle mit offenen Gewichten mit einem gehosteten Dienst bündelt.** Der Autor beschreibt den Aufbau. Kommentatoren vergleichen Kosten und Datenschutz mit anderen Diensten und lokaler Inferenz. Die Vergleiche geben individuelle Erfahrungen wieder. Quellen: https://news.ycombinator.com/item?id=50588396, https://micahflee.com/heres-how-anyone-can-easily-use-private-open-weight-models/

## YouTube

**Ahmad Osman bespricht die Auswahl von Hardware für lokale KI.** Bei AI Engineer erläutert der Osmantic-Gründer Speicherbandbreite, Stapelverarbeitung sowie Miete und Kauf von GPUs. Sein Plädoyer für kontinuierliches Lernen auf Rechnern unter Nutzerkontrolle gibt seine eigene Auffassung wieder. Quelle: https://www.youtube.com/watch?v=GKSQYbELDzw

**Laut Ramp schreibt und veröffentlicht ein interner Agent etwa 75 % des Codes.** Bei AI Engineer spricht Zach Bruggeman über gemeinsame Sitzungen, Überprüfung und Code-Reviews. Das Unternehmen nannte die Zahl, ohne zu erklären, wie es vom Agenten geschriebenen Code zählt. Quelle: https://www.youtube.com/watch?v=MDI81OaZAD4

**Ramps Vorstandschef beschreibt, wie unterschiedlich Agenten eingesetzt werden.** In einem Interview mit Y Combinator schildert Eric Glyman interne Werkzeuge und große Zugewinne bei einigen wenigen Mitarbeitern. Eine unabhängige Produktivitätsmessung enthält der Bericht nicht. Quelle: https://www.youtube.com/watch?v=0Hvs6-XODgU

**First Person Labs wirbt für eine Softwareebene für persönlichen Kontext.** Bei a16z erklärt Ken Liu, wie Second Aktivitäten über Apps hinweg beobachtet und ausgewählten Agenten diese Informationen zugänglich macht. Die Beschreibung nennt keine öffentlichen Belege, anhand derer sich die Datenschutzaussagen des Gründers überprüfen lassen. Quelle: https://www.youtube.com/watch?v=kBJe4H_WobA

**DW Documentary gibt einen Überblick über KI-Risiken.** Der englischsprachige Film enthält Interviews mit Geoffrey Hinton, Yoshua Bengio und Yann LeCun. Die Schilderung des Todes eines Jugendlichen stützt sich auf die Aussage seiner Mutter. Neue Forschungsergebnisse liefert sie nicht. Quelle: https://www.youtube.com/watch?v=2I4qMBiK6hg

**Frühere US-Regierungsberater plädieren dafür, einen Vorsprung bei der Rechenleistung für Investitionen in die Sicherheit zu nutzen.** In The Cognitive Revolution sprechen Ben Buchanan und Tantum Collins über Lieferketten, Exportkontrollen und technische Fragen wie das Ausnutzen von Belohnungssystemen. Das Gespräch stellt ihre politische Argumentation vor. Quelle: https://www.youtube.com/watch?v=6bSzdXKkE2M

**Stanford HAI blickt auf den Aufstieg generativer KI zurück.** Eine Runde diskutiert den dritten AI100-Bericht, darunter Reasoning-Modelle, Rechenressourcen und umstrittene Befunde zur Arbeitswelt. Die Videobeschreibung nennt keine neuen Messwerte. Quelle: https://www.youtube.com/watch?v=WGjuvTvz90U

**Das Institute of Art and Ideas diskutiert, was als Intelligenz gilt.** Die Runde spricht über Verkörperung und darüber, ob die Vergrößerung heutiger Modelle ausreicht. Das englischsprachige Video gibt einen Vorgeschmack auf eine längere Diskussion hinter einer Bezahlschranke. Quelle: https://www.youtube.com/watch?v=DF8jyfEjymo

**PočúvAI beschäftigt sich mit Aussagen zur beschleunigten Arzneimittelentwicklung.** Die slowakischsprachige Folge von Aktuality.sk behandelt auch den Zugang zu Strom und zu personenbezogenen Daten. Die Beschreibung des Ausschnitts nennt keine neuen Ergebnisse zu Medikamenten. Quelle: https://www.youtube.com/watch?v=OkIoQ1imz90

## Kurz notiert

**Das US-Rechnungskontrollamt GAO nennt 16 Möglichkeiten zum Umgang mit KI-bedingten Cyberrisiken.** Der Bericht ordnet sie vier Zielen zu: Orientierungshilfen, Forschung, Aufsicht über den gesamten Lebenszyklus eines Systems und Personalentwicklung. Er behandelt außerdem den Einsatz von KI für defensive Analysen. Quelle: https://www.gao.gov/products/gao-27-108458

**Drei Mitglieder des US-Repräsentantenhauses skizzierten mögliche Vorgaben für führende KI-Labore.** Das Diskussionspapier zum SAFE AI Act schlägt Prüfungen vor der Veröffentlichung, Meldepflichten für Vorfälle und Mindeststandards vor. Eine Gesetzesvorlagennummer und ein Termin für die Einbringung liegen nicht vor. Quelle: https://casrai.org/news/safe-ai-act-outline-frontier-ai-labs-2026
