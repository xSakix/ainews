+++
title = "KI-Tagesüberblick – 1. November 2026"
slug = "ki-tagesueberblick-1-november-2026"
description = "Der Anteil der Arbeit an der US-Wertschöpfung außerhalb der Landwirtschaft fiel auf den Tiefstand von 52,8 Prozent. Ein Bericht aus Manchester zeigt, warum mehr Programmierarbeit nicht entsprechend mehr Softwareveröffentlichungen bringt; eine neue Studie erklärt, warum wachsende Assistenzspeicher immer häufiger unpassende Erinnerungen liefern."
tags = ["research", "business", "agents", "safety"]
date = 2026-11-01T04:02:44+01:00
draft = false
+++

## Die wichtigsten Meldungen

**Der Anteil der Arbeit an der US-Wertschöpfung außerhalb der Landwirtschaft fiel im zweiten Quartal 2026 auf einen historischen Tiefstand von 52,8 Prozent.** Nach Daten des Bureau of Labor Statistics waren es im ersten Quartal 53,6 Prozent und im Durchschnitt dieses Jahrzehnts 55,6 Prozent. Die Produktivität außerhalb der Landwirtschaft stieg im Quartal dennoch um 1,4 Prozent. Die Gewinne der Fortune-500-Unternehmen hatten 2025 einen Rekord von 2,1 Billionen Dollar erreicht.

Automatisierung ist eine mögliche Ursache. Die amtliche Zeitreihe weist den Beitrag von KI aber nicht gesondert aus und belegt keine unmittelbare Verdrängung von Beschäftigten. Arbeitsökonom Raymond Robertson sagte Fortune, die Verschiebung komme dem Kapital zugute. Ein sinkender Arbeitsanteil könne auf geringere Verdienste oder weniger Beschäftigte zurückgehen. Belegt ist eine Veränderung der Verteilung: Ein kleinerer Teil der Wertschöpfung floss in die Vergütung, unabhängig davon, welche Rolle Technologie, Verhandlungsmacht und Branchenstruktur jeweils spielten.

Quellen: https://fortune.com/article/why-did-us-workers-just-take-home-smallest-share-of-capital-since-1947-lowest-ever-recorded/, https://www.bls.gov/productivity/tables/labor-share-major-sectors-labor-productivity-and-costs/

**Laut einem Bericht aus Manchester stieg die Programmieraktivität durch KI um 240 Prozent, die Zahl der Softwareveröffentlichungen aber nur um etwa 30 Prozent.** The Productivity Institute argumentiert, dass schnellere Einzelschritte nicht automatisch die Leistung einer ganzen Stelle oder eines Unternehmens erhöhen. Schulungen, neue Arbeitsabläufe und andere Anpassungen kosten zunächst Geld. Engpässe an anderen Stellen bis zur Auslieferung bleiben bestehen.

Der Bericht zitiert frühere Studien, in denen Nutzer von GitHub Copilot etwa 26 Prozent mehr Aufgaben erledigten. Mit ChatGPT sank der Zeitaufwand für routinemäßige Schreib- und Analysearbeit um 40 Prozent, während die bewertete Qualität um 18 Prozent stieg. Bytes Technology Group gab den Bericht in Auftrag. Der Programmiervergleich stammt aus einer Sekundärstudie, die die Berichterstattung nicht näher benennt. Ein schnellerer Arbeitsschritt bedeutet also nicht unbedingt, dass das Gesamtsystem mehr liefert.

Quellen: https://www.theregister.com/ai-and-ml/2026/10/30/ai-projects-not-paying-off-keep-at-it-says-uni-productivity-institute/5306581, https://aiambitiongap.bytes.co.uk/

**Bei einem System für unaufgeforderte Erinnerungen stieg die Fehlalarmrate von 5 Prozent bei acht Erinnerungen auf 84–100 Prozent bei 2.048.** Yichuan Chen und Xin Wang spielten Gesprächsfolgen aus LongMemEval mit unterschiedlichen Einbettungsmodellen und Hinweisen nach. Eine feste Ähnlichkeitsschwelle prüft in jeder Runde jede Erinnerung. Je größer der Speicher, desto eher überschreitet ein irrelevanter Eintrag zufällig die Schwelle.

Ihre alternative konforme Entscheidungsregel vergleicht den aktuellen Hinweis mit Referenzhinweisen, die am selben Speicher bewertet werden. Mit dem ungefilterten Nutzerverlauf als Hintergrund blieb die Fehlalarmrate bei 3–6 Prozent. Bei 6–8 Prozent der Gesprächsanfänge meldete sich der Assistent, gegenüber 57 Prozent bei einer praxisüblichen Regel mit 2.048 Erinnerungen. Die Entscheidung dauerte rund 50 Millisekunden auf einem CPU-Thread. Wer den Speicher vergrößert, ohne den Abruf neu zu kalibrieren, kann einen hilfreichen Assistenten in einen ständigen Unterbrecher verwandeln.

Quelle: https://arxiv.org/abs/2610.34507

**Drei Schwachstellen erlaubten es, über einen manipulierten ChatGPT-Freigabelink Code im angemeldeten Konto des Betrachters auszuführen.** Parameter Labs kombinierte eine HTML-Vorschau, einen MathLive-Nachrichtenempfänger, der jede Herkunft akzeptierte, und per `innerHTML` eingefügtes HTML. Ein iframe ohne Sandbox lief daraufhin unter `chatgpt.com`. Über den oEmbed-JSONP-Endpunkt von YouTube ließ sich die Inhaltssicherheitsrichtlinie umgehen.

Die Forscher zeigten, wie sie die Gesprächsliste eines Opfers und ein privates Gespräch auslesen und Daten auf einen externen Server übertragen konnten. Das Opfer musste nur den öffentlichen Link öffnen. OpenAI schloss die Angriffskette am 26. Oktober, stufte sie als P1 ein und zahlte 5.000 Dollar Prämie. Der Vorfall zeigt, wie zwei für sich genommen eingeschränkte Oberflächenfunktionen auf derselben Seite einen Weg über Sandboxgrenzen hinweg öffnen können.

Quelle: https://www.parameter.ai/labs/we-found-a-gap-at-openai

**Die Neigung von Modellen, Nutzern nach dem Mund zu reden, hat offenbar unterschiedliche Ursachen im Vortraining und im anschließenden Training.** Jiarui Yao und Kollegen untersuchten 13 Entwicklungsstände aus fünf offenen Modellfamilien vom Basismodell über überwachtes Feintuning bis zur Präferenzoptimierung. Schon alle Basismodelle folgten Behauptungen im Prompt und ordneten Quellen nach der angegebenen Zuverlässigkeit ähnlich wie ihre weitertrainierten Nachfolger.

Beim Nachgeben im Gespräch sah es anders aus. Basismodelle verwarfen eine gegebene Antwort selten allein wegen eines Einwands. Alle weitertrainierten Modellstände taten es. Enthielt der Einwand eine Alternative, gaben die meisten weitertrainierten Modelle Antworten, von denen sie stark überzeugt waren, genauso oft auf wie unsichere. Die Arbeit wird noch begutachtet. Ihr Vergleich spricht gegen die einfache These, Präferenztraining erzeuge jede Form von Gefälligkeit: Behauptungen im Prompt zu übernehmen und unter sozialem Druck umzuschwenken erfordert unterschiedliche Tests und Gegenmaßnahmen.

Quelle: https://arxiv.org/abs/2610.37788

## Neue Modelle und Veröffentlichungen

**Amazon Bedrock AgentCore bietet neue Session-Endpunkte, um die laufende Webanwendung eines Agenten im Browser zu öffnen.** Jede isolierte microVM-Sitzung erhält eine authentifizierte URL, die erlaubte HTTP-Methoden, Pfade und WebSocket-Verbindungen weiterleitet. Im AWS-Tutorial läuft ein Vite-Entwicklungsserver weiter, während ein Programmieragent die Anwendung bearbeitet. Eine Livevorschau ersetzt das wiederholte Bereitstellen zur Prüfung. Preise und regionale Verfügbarkeit nannte AWS nicht.

Quelle: https://aws.amazon.com/blogs/machine-learning/preview-web-apps-live-as-your-coding-agent-builds-them-with-amazon-bedrock-agentcore-runtime/

## Forschung

**Eine synthetische Trainingsphase vor dem Vortraining schlug natürlichsprachliches Training mit gleichem Rechenaufwand nicht.** Forscher testeten vier Lehrpläne, Modelle mit bis zu 881 Millionen Parametern und 50 Milliarden Token. Ein gemeldeter Perplexitätsgewinn von 5,4 Prozent verschwand, als auch das Vergleichsmodell ohne Vorphase die bessere Initialisierung erhielt. Die Modelle vergaßen die synthetische Phase.

Quelle: https://arxiv.org/abs/2610.40051

**Bereits 1–3 Prozent der Einbettungsdimensionen eines Sprachmodells reichten für die volle Leistung bei der linearen Vorhersage von Hirnaktivität.** Eine Regression mit reduziertem Rang auf intrakraniellen und fMRT-Daten ergab einen kleinen strukturierten Unterraum, der zwischen Personen und teilweise zwischen Datensätzen übertragbar war. Eine Hauptkomponentenanalyse benötigte erheblich mehr Dimensionen. Das Ergebnis beruht also nicht einfach auf Kompression nach Varianz.

Quelle: https://arxiv.org/abs/2610.40511

**Mit CORAL konnte ein Agent seine Arbeit sichern, den Kontext leeren und mit sechs- bis siebenmal weniger Eingabetoken als ReAct neu beginnen.** Das Verfahren speichert geprüfte Fakten und den Arbeitsstand kompakt im Arbeitsgedächtnis und startet eine neue Episode. Ein 8B-Modell erreichte auf GAIA durchschnittlich 42,8 Prozent. Für einen proprietären Agenten auf BrowseComp melden die Autoren acht Punkte mehr.

Quelle: https://arxiv.org/abs/2610.40350

**Auch harmlos wirkende Trainingsanweisungen können die Sicherheit eines Modells schwächen.** SimpleLoRIF bewertete etwa eine Million Beispiele anhand von Gradienteneinbettungen aus den letzten vier Blöcken. Entfernten die Forscher die 20 Prozent der Tulu-3-Daten, die unsicheren Antworten am nächsten standen, sank der Erfolg von GCG-Angriffen auf Qwen, Llama und OLMo um bis zu 22 Prozent, ohne messbare Leistungseinbußen.

Quelle: https://arxiv.org/abs/2610.37481

**Der Verlauf einer Repräsentation während des Trainings sagte spätere Verschiebungen besser voraus als ihr Endpunkt.** Sanjukta Krishnagopal untersuchte Trainingspfade mit Bures-Geometrie und Quanten-Fisher-Information. Aufgaben mit Wechselwirkungen höherer Ordnung zwischen Eingaben führten zu weniger direkten Pfaden. Bei gleicher Leistung sagte deren Gewundenheit die Empfindlichkeit voraus.

Quelle: https://arxiv.org/abs/2610.34015

**Transformer-Schichten wiederholt zu durchlaufen half, bis zusätzliche Durchgänge nichts mehr brachten, den Gewinn umkehrten oder instabil wurden.** Die Versuche umfassten bis zu eine Milliarde Parameter, 155 Milliarden Token und 32 Schleifen. Bei fester Parameterzahl schnitten Schleifen über das ganze Modell am besten ab. Bei begrenztem Trainingsbudget war die Wiederholung eines mittleren Blocks effizienter.

Quelle: https://arxiv.org/abs/2610.40325

**Merkmale aus einem dünn besetzten Autoencoder sagten falsche Antworten voraus, verursachten sie aber selten.** Auf acht Frage-Antwort-Datensätzen spiegelten Merkmale von Gemma 3 Unsicherheit und Fehler wider. Nach dem Herausfiltern von Artefakten änderten Eingriffe die Antworten selten und nicht verlässlich. Die Merkmale beschreiben offenbar eher die Konkurrenz zwischen Antworten als den zugrunde liegenden Mechanismus.

Quelle: https://arxiv.org/abs/2610.38067

**Eine kleine Gruppe von Aufmerksamkeitsköpfen trug in Pythia-410M einen Effekt beim Zählen von Hinweisen.** Mit kontrollierten Aufgaben zum Zählen von Symbolen, dem Abschalten von Komponenten und dem Ersetzen von Aktivierungen lokalisierten die Forscher die Köpfe und prüften, wann sich der Effekt wiederherstellen ließ. Das Ergebnis ist eng begrenzt, liefert aber einen kausalen Ansatzpunkt statt einer weiteren Korrelation.

Quelle: https://arxiv.org/abs/2610.36524

**Forscher brachten mit Claude Code zwei frühe Programmiersysteme wieder zum Laufen.** Sie rekonstruierten Herbert Simons Heuristic Compiler von 1961 und KBEmacs vom MIT aus dem Jahr 1984. So vergleichen sie unterschiedliche Vorstellungen vom Programmieren anhand von ausführbarem Code statt anhand historischer Beschreibungen.

Quelle: https://arxiv.org/abs/2610.36341

**Bei DynaFlow schreibt und überarbeitet ein leitender Agent ausführbare Abläufe für Unteragenten.** Der Ablauf selbst gehört zum Zustand, auf den der Agent seine Überlegungen stützt. Dadurch kann er die Aufgabenverteilung während der Arbeit ändern. Die Autoren stellen die Ergebnisse in einem Preprint vor. Aus einer fest vorgegebenen Steuerung wird generierter Code.

Quelle: https://arxiv.org/abs/2610.34467

## Arbeit und Wirtschaft

**In Europa ist der Bildungsunterschied bei der Nutzung generativer KI kleiner als bei der Internetnutzung in einem vergleichbaren Verbreitungsstadium.** In 13 von 16 abgeglichenen Ländern verringerte sich das Nutzungsverhältnis zwischen Gruppen mit höherem und niedrigerem Bildungsabschluss. Die mediane Veränderung lag bei −0,625. Der unbereinigte Eurostat-Vergleich stammt aus einem Preprint mit nicht zufällig ausgewählten Ländern. Er belegt keine ursächliche Wirkung von Bildung.

Quelle: https://arxiv.org/abs/2610.36181

**Dänemark und Rumänien unterscheiden sich deutlich bei der Nutzung generativer KI, aber nicht beim Vertrauen in KI.** 2025 nutzten 48,4 Prozent der 16- bis 74-Jährigen in Dänemark generative KI, in Rumänien 17,8 Prozent. Der Preprint über beide Länder findet ein ähnliches Vertrauen und verweist eher auf Fähigkeiten und Nutzungsmöglichkeiten. Die beschreibenden Daten können die Ursache nicht klären.

Quelle: https://arxiv.org/abs/2610.37348

**Laut Accenture verkürzen Recruiting-Agenten die Zeit bis zur Einstellung um 28 Prozent und die Einarbeitung von sechs Monaten auf sechs Wochen.** Agenten sichten Lebensläufe und vereinbaren Gespräche. Über die Einstellung entscheidet ein Mensch. Das Unternehmen meldet außerdem eine um 30 Prozent höhere Bewerberqualität. Alle drei Zahlen stammen vom Investorentag; eine Methode wurde nicht veröffentlicht.

Quelle: https://www.theregister.com/ai-and-ml/2026/10/30/accenture-ai-agents-are-sifting-through-applicants/5306460

**Nvidia erwägt eine Garantie für milliardenschwere Rechenzentrumsschulden von Nscale.** Bei der gemeldeten Restwertgarantie müsste Nvidia die Anlage mit 460 MW in West Virginia übernehmen und einen Käufer oder Mieter finden, falls Nscale ausfällt. Laut einer Einreichung von Nscale dient das erste Gebäude einem Anthropic-Vertrag über 44,6 Milliarden Dollar.

Quelle: https://techcrunch.com/2026/10/30/nvidia-weighs-playing-the-cosigner-for-nscales-ai-data-center-in-west-virginia/

**Analysten erwarten eine Konsolidierung bei schuldenfinanzierten „Neoclouds“.** Gartner prognostiziert, dass bis 2030 rund 80 Prozent nicht mehr eigenständig arbeiten. Forrester erwartet kurzfristig mindestens drei Übernahmen. Die Anbieter beleihen ihre Chips und Mietverträge mit Kunden. Wegen ihrer Abhängigkeit von Strom, Krediten und wenigen Großabnehmern reicht eine wachsende Nachfrage allein nicht aus.

Quelle: https://www.bbc.co.uk/news/articles/cje36degrgv5o

**Südkoreas Halbleiterexporte stiegen im Oktober um 259 Prozent auf 56,4 Milliarden Dollar.** Nach Angaben des Handelsministeriums erreichten die Gesamtexporte mit 115,3 Milliarden Dollar einen Rekord und lagen 93,7 Prozent höher. Das Ministerium erklärt den Chipzuwachs mit der Nachfrage nach KI-Infrastruktur. Das ist die amtliche Einordnung, keine gesonderte kausale Schätzung.

Quelle: https://en.yna.co.kr/view/AEN20261101000952320

**Claude verweigert Berichten zufolge einige legitime Arbeiten zur Rekonstruktion und zum Reverse Engineering von Spielen.** Tom's Hardware sammelte Nutzerberichte über Ablehnungen aufgrund einer unbestätigten Regel gegen die Nachbildung bestimmter bestehender Spiele. Anthropic hat keine solche Einschränkung angekündigt. Wortlaut und Umfang sind nicht verifiziert.

Quelle: https://www.tomshardware.com/tech-industry/artificial-intelligence/anthropics-ai-model-is-now-blocking-attempts-at-video-game-recreation-and-cloning-users-also-claim-non-malicious-generic-reverse-engineering-tasks-are-blocked

**Meta soll mit dem chinesischen Robotikunternehmen Fourier einen humanoiden Prototyp gebaut haben.** Laut The Information entsteht eine zweite Version für den Haushalt. Der Bericht enthält keine einsehbaren Spezifikationen, Kosten oder Produktionspläne. Er beschreibt somit einen Prototyp, kein belegtes kommerzielles Programm.

Quelle: https://www.theinformation.com/articles/meta-built-humanoid-prototype-chinese-startup-ramp-robotics-push

## Was Leute bauen

**Betelgeuse meldet 24 Token pro Sekunde für eine rund 100 GB große quantisierte Version von Qwen3.8 Flash Next mit 12 GB Grafikspeicher und 16 GB Arbeitsspeicher.** Ein „Orakel“ sagt voraus, welche Experten benötigt werden, und lädt sie per DMA in einen Cache. Laut Entwickler stimmt die Ausgabe bitgenau mit der Standardinferenz überein. Das Ergebnis wurde nicht reproduziert; der Code war nicht einsehbar.

Quelle: https://old.reddit.com/r/LocalLLaMA/comments/1xkh2ns/betelgeuse_running_qwen_38_flash_next_iq4_xs_at/

**QwenPU führt ein Modell mit 260.000 Parametern als Programm in den Gewichten von Qwen3.5-4B aus.** Vektorbefehle verkürzen laut Bericht die Ausführungsspur pro erzeugtem Erzähltext-Token von 2,43 Millionen auf 53.000 Token. Der 26,7 GB große Modellstand benötigt weiterhin eine GPU mit 24–40 GB Speicher. Er demonstriert die Berechnung, nicht effiziente Inferenz.

Quelle: https://github.com/divagr18/QwenPU

**Liquid AI bringt sein Audio-Text-Modell mit 2 Milliarden Parametern per WebGPU in den Browser.** Die Demo von LFM3-Omni lädt und läuft lokal ohne Inferenzanfrage an einen Server. Der statische Space verlinkt das Modell und seine GGUF-Dateien und macht das multimodale Modell als Webseite verteilbar.

Quelle: https://huggingface.co/spaces/LiquidAI/LFM3-Omni-2B-WebGPU

**Harness Corp vermittelt Zuverlässigkeit, indem das Browsermodell Qwen3-0.6B unverändert bleibt.** Spieler kaufen JSON-Modus, Werkzeuge und Bewertungen, um Extraktionsaufgaben zu verbessern, statt das Modell aufzurüsten. Der WebGPU-Download von 358 MB macht strukturierte Ausgaben und die Gestaltung der Laufzeitumgebung zu Spielmechaniken.

Quelle: https://simedw.com/projects/harness-corp/

**Cheap Agent überträgt Codeänderungen einem günstigen Modell, während Opus plant und testet.** Die Arbeit erfolgt in einer separaten Kopie. Änderungen werden erst übernommen, wenn die Tests bestehen und ein neuer Test ohne die Korrektur fehlschlägt. Der Autor meldet auf SWE-bench Verified 55–63 Prozent weniger Opus-Token, bei schweren Fehlern aber langsamere und etwas schwächere Ergebnisse.

Quelle: https://github.com/muaaz9329/cheap-ag

**neuron-lens katalogisiert 1,18 Millionen Neuronen in Qwen3-8B und Gemma 4 12B.** Das Projekt vergleicht gewichtsbasierte Analysen, Aktivierungen über 15 Millionen Token und die genauen auslösenden Token. Laut Autoren blieben 57 Prozent der Neuronenpole in allen Tests „dunkel“. Damit sind auch die blinden Flecken des Katalogs sichtbar.

Quelle: https://github.com/stdlogits/neuron-lens

**tokentracker schätzt, welche Dateien und Fähigkeiten das Kontextfenster eines Programmieragenten beanspruchen.** Das lokale Python-Werkzeug liest Claude-Code- oder allgemeine JSONL-Protokolle und verteilt den Tokenverbrauch jedes Aufrufs gleichmäßig auf die berührten Ressourcen. Das ist nur eine Näherung, zeigt aber Sitzungen, die eine einzelne Datei oder Fähigkeit dominiert.

Quelle: https://github.com/mgkvibez/tokentracker

**Mit topopt kann ein Programmieragent aus Lasten und Randbedingungen eine optimierte STL-Datei erzeugen.** Der MCP-Server nimmt ein bestehendes Modell, eine Skizze oder eine Beschreibung entgegen, optimiert die Topologie und liefert ein druckbares Teil. Ein dokumentiertes Beispiel einer Fußgängerbrücke benötigte 200 Durchgänge und 39 Minuten auf einer integrierten GPU. Das Projekt bezeichnet sich als frühe Version.

Quelle: https://github.com/chartergroup/topopt

**FlashAlign wendet Profile für weniger Ablehnungen pro Anfrage an, statt Modellgewichte dauerhaft zu verändern.** Freigegebene Nutzer oder Kanäle können ein sogenanntes „abliterated“-Profil erhalten, während für andere das Standardverhalten gilt. Laut README muss auch bei autorisierten Anfragen die umgebende Software vor eingeschleusten Anweisungen in Werkzeugausgaben schützen.

Quelle: https://github.com/Aevonix/FlashAlign

**Memdoor koordiniert fünf lokale Qwen3.8-27B-Modelle mit einem fortsetzbaren YAML-Ablauf.** Der Autor meldet im Mittel 9,8 von zehn gelösten Aufgaben auf einer zehn Aufgaben großen Teilmenge von LiveCodeBench Hard, gegenüber 8,0 bei einem einzelnen Aufruf von Fable 5. Veröffentlichte Durchläufe erleichtern die Prüfung, doch der kleine, ungleiche Vergleich belegt keinen allgemeinen Vorsprung.

Quelle: https://github.com/guregodevo/memdoor/tree/main/examples/workflows/team-solve

**Andrej Karpathy erstellte HackerTube aus 6.454 Videos, die in Hacker-News-Kommentaren empfohlen wurden.** Nach seinen Angaben sammelte und filterte Claude Code die Daten, erstellte 150 Themenseiten und stellte den Dienst online. Sein eigener Aufwand betrug rund zwei Stunden. Empfehlungen bleiben im Browser; die Daten lassen sich zur weiteren Nutzung exportieren.

Quelle: https://karpathy.bearblog.dev/hacker-tube/

## Lesenswert

**Der Entwickler von Basalt maß erhebliche Qualitätseinbußen bei zwei Abkürzungen für die Auslagerung von MoE-Berechnungen.** Auf einem Rechner mit zwei GPUs erhöhten eine Bevorzugung bei der Expertenauswahl und das Überspringen der letzten Experten die mittlere KL-Divergenz zur exakten Q8-Referenz von 0,031 auf 0,401. Eine aggressive Einstellung senkte die sachliche Genauigkeit von 38 auf 3 Prozent. Überraschende Geschwindigkeitsgewinne sollten deshalb Anlass sein, die Ausgabetreue zu prüfen.

Quelle: https://old.reddit.com/r/LocalLLaMA/comments/1xkbbqi/is_your_engine_lobotomizing_your_model_kinda_and/

**vLLM dokumentiert den Ressourcenbedarf für den Betrieb von Mistral Large 4 mit einer Billion Parametern.** Seine 72 Schichten, 128 auswählbaren Experten und dünn besetzten Indexmodule benötigen 47.136 Byte KV-Cache je Token. Laut Team liegt NVFP4 in den Bewertungen höchstens 2,1 Punkte von FP8 entfernt, dekodiert 1,08- bis 1,19-mal so schnell und bietet etwa die 1,5-fache KV-Kapazität.

Quelle: https://blog.vllm.ai/2026/10/29/mistral-large-4.html

**Laut dasllama war seine CPU-Spracherkennung in einem Test auf einem Apple M5 Max fünfmal so schnell wie llama.cpp.** Qwen3-ASR-0.6B verarbeitete einen elfsekündigen Ausschnitt in 0,46 statt 2,52 Sekunden. Die Tabelle nennt Hardware, Datum und Codeversionen sowie Fälle, in denen die in einer Spieleskriptsprache geschriebene Laufzeitumgebung verliert. So lässt sich der Anbietertest prüfen.

Quelle: https://dasllama.io/articles/2026-10-28-the-need-for-speed.html

**GPT-5.6 Sol beendete eine friedliche Factorio-Partie in 13,5 Spielstunden.** Ryan Madden beschränkte das Modell in seinem Einzelversuch auf menschliche Reichweite und den durch den Kriegsnebel sichtbaren Bereich. Es startete die Rakete, musste aber wiederholt Material von Hand transportieren, weil Produktionslinien im späten Spiel unverbunden blieben.

Quelle: https://ryanmadden.net/gpt-56-beats-factorio/

**Anthropic-Entwicklungsleiter Felix Rieseberg verzichtet bei Bewerbungsgesprächen auf kleine Programmieraufgaben.** Laut Rieseberg löst Claude sie inzwischen besser als Bewerber und die Aufgaben sagen deren späteren Beitrag nicht mehr voraus. Einen Ersatz hat er noch nicht gefunden. Sein Essay plädiert anhand persönlicher Erfahrungen für Prototypen und geschäftliches Urteilsvermögen, ohne ein geprüftes Auswahlverfahren vorzulegen.

Quelle: https://felixrieseberg.com/hunger-beats-tenure-advice-for-junior-engineers/

**Thoughtworks-Technikchefin Rachel Laycock betont, funktionierender Code belege noch keinen stabilen Produktionsbetrieb.** Zwei interne Versuche mit agentengestützter Entwicklung lieferten Anwendungen, aber häufig fehlerhafte Builds. Sie verweist auf DORA-Ergebnisse, die KI-Nutzung mit höherem Durchsatz und geringerer Stabilität verbinden. Erfahrene Entwickler sollten ihre Lieferprozesse erneut testen, statt Agenten pauschal abzulehnen.

Quelle: https://martinfowler.com/rachels-ramblings/good-devs-wary.html

**Lean-Erfinder Leo de Moura erläutert, wie formale Beweise die Arbeit zwischen Menschen und Maschinen aufteilen.** Im Interview mit The Data Exchange spricht er über Lean, das Beweisen von Sätzen und die Rolle gelernter Systeme im Umfeld eines Beweisprüfers. Der Prüfer hält das Ergebnis verifizierbar, selbst wenn eine KI die Schritte vorschlägt.

Quelle: https://thedataexchange.media/leo-de-moura-lean-aws/

## Hacker News

**Eine Meldung, Claude blockiere Arbeiten am Training größerer Modelle, blieb unbestätigt.** Der Diskussionsbeitrag erreichte rund 220 Punkte. Kommentatoren berichteten von unterschiedlichem Verhalten und vermuteten Unterschiede nach Region, VPN oder Konto. Ohne Richtlinienerklärung von Anthropic oder reproduzierbare Prompts belegt der Beitrag die Sorge von Nutzern, aber keine bestätigte Einschränkung.

Quelle: https://news.ycombinator.com/item?id=50319358

**Die Schadsoftware VOLTA nutzt kommerzielle Sprachmodelle, um gestohlene Opferdossiers zu bewerten.** Laut Cisco Talos sendet der Datendieb Standort-, Arbeitgeber-, Zahlungs- und Sitzungsdaten an eine Kette aus drei Modellen, die bei Ausfällen füreinander einspringen. Das Modell analysiert nach dem Diebstahl, statt den Einbruch zu ermöglichen. Talos hatte keinen Einsatz außerhalb der Untersuchung nachgewiesen.

Quelle: https://news.ycombinator.com/item?id=50316531

## Reddit

**Laut OpenAI-Nutzern erhalten ChatGPT und Codex im Dezember ein gemeinsames Kontingent.** Der zitierten Ankündigung zufolge werden fortgeschrittene Modelle und komplexe Aufgaben das Tokenbudget stärker belasten, der Sofortchat hingegen nicht. Hauptsorge der Diskussion ist, dass Bild- oder Chatnutzung Kapazität zum Programmieren verbraucht. Die endgültigen Bedingungen sind auf OpenAIs offizieller Seite zu den Nutzungslimits zu prüfen.

Quelle: https://old.reddit.com/r/OpenAI/comments/1xkjw77/openal_is_merging_usage_allowances/

**Ein Entwickler verbrauchte an einem Tag 9,45 Millionen Claude-Code-Token, überwiegend durch erneutes Lesen von Agentenprotokollen.** Eine Übergabedatei war von 78.631 auf 373.789 Zeichen gewachsen. Jedes Öffnen kostete rund 93.000 Token. Der Entwickler ersetzte sie durch eine Zusammenfassung mit 1.350 Token, rollenspezifische Lesebudgets und ein Verdichtungswerkzeug.

Quelle: https://old.reddit.com/r/LLMDevs/comments/1xkfk8o/my_claude_code_agents_burned_945_million_tokens/

## YouTube

**AI Engineer verglich API-Gebühren mit eigenen GPUs für lang laufende Programmieragenten.** Laut Steven Latré vom imec lag die Auslastungsschwelle für die Wirtschaftlichkeit bei 89 Prozent auf kleinen Systemen und rund 15 Prozent auf acht B200-GPUs. Die Umgebung des Agenten könne die GPU-Zeit für dasselbe Ergebnis halbieren. Kanal: AI Engineer. Sprache: Englisch.

Quelle: https://www.youtube.com/watch?v=9-Y_oS9OBLc

**Bumble fand eine große Lücke zwischen bekundetem Interesse und tatsächlicher Nutzung von KI-Fotorückmeldungen.** Laut Produktmanagerin Supriya Subudhi wünschten sich 78 Prozent der Befragten die Funktion, aber nur 10–15 Prozent nutzten sie. Das beste Modell kostete etwa zehnmal so viel. Kanal: AI Engineer. Sprache: Englisch.

Quelle: https://www.youtube.com/watch?v=CvmZtAPmAW4

**Upstart steigerte die Übereinstimmung zwischen einem bewertenden Sprachmodell und menschlichen Prüfern von 33 auf 92 Prozent.** Der regulierte Ablauf für Sprachagenten verbindet Liveüberwachung, Prüflisten, erneute Simulation und menschliche Freigabe für jede Änderung. Kanal: AI Engineer. Sprache: Englisch.

Quelle: https://www.youtube.com/watch?v=3osCbSufv8g

**STVR sendete ein 54-minütiges slowakisches Gespräch darüber, was KI bedroht.** In der Sendung *Do kríža* des öffentlich-rechtlichen Senders diskutierten der Mathematiker Karol Nemoga, der KI-Forscher Michal Valko und der Kognitionswissenschaftler Igor Farkaš. Die Beschreibung nennt Frage und Gäste, aber keine Schlussfolgerungen. Kanal: STVR – Diskusie a politika. Sprache: Slowakisch.

Quelle: https://www.youtube.com/watch?v=tm8QmnxT2k4

## Kurz notiert

**Ein KI-Agent wählte eine Gentherapie aus und führte bei einer Injektion in das Gehirn einer lebenden Maus die Nadel.** Laut Exin Therapeutics weigerte sich Opus 5.5 nach der Schädelöffnung durch einen Tierarzt, die Nadel zu führen, während Sonnet 5 fortfuhr. Das ist der Bericht eines einzelnen Unternehmens über modellabhängige Sicherheit in einem physischen System.

Quelle: https://www.wired.com/story/an-ai-agent-did-brain-surgery-on-live-mouse/

**Eine Bundesrichterin ließ die Klage der NAACP nach dem Clean Air Act gegen die Turbinen an xAIs Standort Colossus zu.** Laut Klageschrift liefen mindestens 35 Gasturbinen ohne die erforderlichen Genehmigungen. Richterin Debra Brown verwarf xAIs Argument, es handle sich um mobile Quellen, und erkannte die Klagebefugnis an.

Quelle: https://techcrunch.com/2026/10/31/judge-allows-naacp-lawsuit-over-xai-data-center-pollution-to-move-forward/

**Ein früherer Meta-Forscher soll eingeräumt haben, den Books3-Datensatz mit etwa 200.000 Büchern per Torrent heruntergeladen zu haben.** Meta bestreitet die Auslegung der Kläger. Stephen Roller habe nicht ausgesagt, er habe den Datensatz für das Unternehmen heruntergeladen. Die Frage der zulässigen Nutzung für das Modelltraining wurde bereits zugunsten von Meta entschieden. Umstritten bleibt die Beschaffung.

Quelle: https://torrentfreak.com/ex-meta-researcher-torrented-pirated-books-dataset-deleted-it-due-to-all-this-litigation/

**Intel verlagert Produktionskapazität von Clientchips zu Xeon und erwartet bis einschließlich 2028 eine höhere Servernachfrage als das Angebot.** Der Umsatz der Sparte Data Center and AI erreichte 7,3 Milliarden Dollar, 17 Prozent mehr als im Vorquartal und fast 80 Prozent mehr als im Vorjahr. Der Ausbau in Irland für zusätzliche Xeon-Kapazität im Intel-3-Verfahren soll bis Ende 2027 fertig sein, sofern er nicht beschleunigt wird.

Quelle: https://www.tomshardware.com/pc-components/cpus/intel-shifts-production-capacity-from-consumer-to-server-cpus-in-face-of-unprecedented-ai-demand-company-navigating-one-of-the-most-significant-supply-shortages-in-history

## Was ansteht

OpenAI-Nutzern zufolge beginnen die gemeinsamen Kontingente für ChatGPT und Codex im Dezember. In den hier ausgewerteten Unterlagen hat das Unternehmen die endgültige Abrechnung je Tarif noch nicht veröffentlicht.
