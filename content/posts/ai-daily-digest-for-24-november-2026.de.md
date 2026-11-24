+++
title = "KI-Tagesüberblick – 24. November 2026"
slug = "ki-tagesueberblick-24-november-2026"
description = "China setzt KI in 15 Regionen bei Sozialversicherungsdiensten ein, während Singapur seine Wachstumsprognose wegen der Nachfrage nach KI-Elektronik anhob. Aleph Alpha veröffentlichte ein offenes deutsch-englisches Reasoning-Modell, und eine 10-GB-Quantisierung hielt auf mehreren Agenten-Benchmarks mit dem 54-GB-Ausgangsmodell Schritt."
tags = ["models", "research", "agents", "business"]
date = 2026-11-24T03:58:39+01:00
draft = false
+++

## Die wichtigsten Meldungen

**China meldet, KI habe in einer Provinz sieben Millionen Sozialversicherungsfälle bearbeitet.**

Ein Bericht der Internationalen Arbeitsorganisation (ILO) untersucht 45 Einsätze in 15 Regionen auf Provinzebene. 47 Prozent verbessern die Dienstleistungserbringung, 33 Prozent unterstützen die Verwaltung, und der Rest entfällt auf Risikoprüfung oder Entscheidungsunterstützung.

Im Pekinger Bezirk Haidian bearbeiteten automatisierte Systeme im Jahr 2024 mehr als 70.000 Vorgänge und steigerten die Bearbeitungseffizienz gegenüber manueller Arbeit um mehr als 80 Prozent. Die Prüfsysteme der Provinz Guangdong erledigten bis Juli 2025 mehr als sieben Millionen Fälle in 34 Diensten und sparten mehr als 640.000 Arbeitsstunden ein.

Die Fälle wurden gemeinsam mit dem chinesischen Arbeitsministerium ausgewählt und bilden keine repräsentative Stichprobe. Die ILO erklärt, Menschen sollten weiterhin über Leistungsansprüche und Arbeitsunfälle entscheiden, während Offline-Angebote für Menschen mit digitalen Hürden bestehen bleiben müssten.

Quelle: https://www.ilo.org/resource/news/ai-transforming-social-security-services-china-new-ilo-report-finds

**Singapur hob seine Wachstumsprognose für 2026 auf rund 6 Prozent an, da die Nachfrage nach KI-Elektronik die Exporte steigerte.**

Die Wirtschaft wuchs im dritten Quartal im Jahresvergleich um 6,1 Prozent. Behörden führten einen Großteil dieser Stärke auf Elektronik im Zusammenhang mit dem KI-Investitionszyklus zurück und erhöhten ihre Prognose für das Gesamtjahr.

Für 2027 flacht der Ausblick auf 2,5 bis 4,5 Prozent ab. Dieser Abstand ist für eine Exportwirtschaft bedeutsam, deren Halbleiter- und Serverlieferungen inzwischen von anhaltenden Rechenzentrumsausgaben im Ausland abhängen; es handelt sich um eine amtliche Prognose, nicht um ein Maß für die KI-Produktivität innerhalb singapurischer Unternehmen.

Quellen: https://asia.nikkei.com/economy/singapore-gdp-grows-6.1-in-q3-as-ai-demand-stays-strong, https://www.bloomberg.com/news/articles/2026-11-24/singapore-raises-gdp-growth-outlook-to-around-6-on-ai-boom

**Aleph Alpha veröffentlichte Kolibri 1.1 mit 75 Milliarden Parametern und 262.144 Token nativem Kontext.**

Das deutsch-englische Reasoning-Modell unter Apache-2.0-Lizenz aktiviert 3,44 Milliarden Parameter pro Token. Seine Gewichte belegen rund 77,6 GB, sodass die dünn besetzte Architektur eher den Rechenaufwand als den Speicherbedarf senkt.

Aleph Alpha meldet nach dem Post-Training einen Vergleichstest-Durchschnitt (Benchmark) von 73,2 gegenüber 66,6 bei Kolibri 1.0, während Qwen3.8 Flash Next in derselben Tabelle 80,1 erreicht. Die Modellkarte empfiehlt, bei schwierigen Aufgaben höchstens das native Kontextfenster auszuschöpfen, obwohl die Implementierung auf rund eine Million Token erweitert werden kann.

Quelle: https://huggingface.co/Aleph-Alpha/Kolibri-1.1

**Nari Labs komprimierte Qwen3.8-27B von 53,8 GB auf 10,12 GB, ohne auf drei seiner Benchmarks Boden zu verlieren.**

NariQ nutzt eine Trellis-kodierte Post-Training-Quantisierung, die anhand von Programmieragenten-Spuren kalibriert wurde. Die 3-Bit-Version des Labors erreichte 41,0 Punkte auf DeepSWE gegenüber 39,8 für BF16, 63,8 gegenüber 62,6 auf Terminal-Bench sowie 98,3 gegenüber 97,7 bei AIME 2025–26.

Die kleinere 2-Bit-Version fiel in diesen Tests auf 28,6, 52,4 und 86,0 Punkte zurück. Zudem erfordern die Dateien den llama.cpp-Fork von Nari Labs, der auf Nvidias SM120-Architektur abgestimmt ist, auf älteren Nvidia-Karten und Metal langsamer läuft und weder AMD- noch Intel-GPUs unterstützt.

Quelle: https://huggingface.co/nari-labs/Qwen3.8-27B-NariQ-GGUF

**Zwei Drittel von 58 Anthropic-Kunden gaben an, KI habe ihre Neueinstellungen verringert.**

Das Ökonomie-Team von Anthropic führte 66 Interviews bei US-Unternehmenskunden. Nur zwei Unternehmen hatten eine Stelle durch Automatisierung abgebaut und fünf hatten Beschäftigte entlassen, die sich gegen KI sperrten, während zehn mehr Personal einstellten, vor allem für Implementierung und IT-Support.

Der Effekt zeigte sich häufiger bei Neueinstellungen: Zwei Drittel berichteten, weniger einzustellen, und rund ein Drittel dieser Gruppe verkleinerte Bereiche über natürliche Fluktuation. Neun verringerten die Arbeit externer Auftragnehmer. Von 100 ausreichend detailliert beschriebenen, mit KI erstellten Softwarelösungen automatisierten 80 manuelle Arbeit und 20 ersetzten zugekaufte Software.

Die Stichprobe ist klein, nicht zufällig gezogen und auf eigene Kunden des Anbieters beschränkt. Die Bewertungen des Nutzens waren überwiegend qualitativ und beruhten auf Selbstauskünften statt auf Messungen in kontrollierten Studien.

Quelle: https://www.anthropic.com/research/working-with-ai

## Neue Modelle und Veröffentlichungen

**Ant Group veröffentlichte Ling-3.2-air mit 124 Milliarden Parametern unter der MIT-Lizenz.** Das Modell aktiviert 5,5 Milliarden Parameter und kombiniert 35 Linear-Attention-Schichten mit sieben Gated-Attention-Schichten. Der Herausgeber meldet eine Kriterien-Bestehensquote von 87,7 Prozent in seinem Rechts-Benchmark, doch nur 0,8 Prozent der Stichproben erfüllten nach einer Prüfung auf wesentliche Halluzinationen sämtliche Kriterien; ein technischer Bericht liegt der Modellkarte nicht bei.

Quelle: https://huggingface.co/inclusionAI/Ling-3.2-air

**Tencent veröffentlichte fünf Vision-Language-Modelle der Reihe WeMM-Ecom für den Onlinehandel.** Die Größen reichen von 0,8 Milliarden Parametern bis zu einem Mixture-of-Experts-Modell mit 35 Milliarden Parametern, das 3 Milliarden Parameter aktiviert. Tencent meldet über 28 E-Commerce-Benchmarks einen Zugewinn von 3,92 Punkten gegenüber der Basis Qwen3.5, über 64 allgemeine Benchmarks jedoch nur 0,17 Punkte; diese Werte stammen aus BF16 und nicht aus den neuen quantisierten Varianten.

Quelle: https://huggingface.co/tencent/WeMM-Ecom-35B-A3B-GPTQ

**AI Singapore ergänzte sein 9-Milliarden-Modell SEA-LION um einen spekulativen 2-Milliarden-Parameter-Decoder.** Der Herausgeber maß bei Parallelität eins das 2,26- bis 3,08-Fache an Token pro Sekunde, ausgehend von einem Basiswert nahe 195 Token pro Sekunde. Bei Parallelität 16 schrumpft der Vorteil auf höchstens das 1,5-Fache und könnte bei 32 verschwinden, sodass es sich eher um ein Werkzeug zur Latenzsenkung bei geringer Last als für hohen Durchsatz handelt.

Quelle: https://huggingface.co/aisingapore/Qwen-SEA-LION-v5-9B-SpecDecoder

**Anthropic stellt Claude Opus 4.5 am 22. Januar 2027 ein und öffnete Enterprise Frontier Safeguards als Beta.** Die Schutzmechanismen bewahren Zero Data Retention und speichern zugleich verschlüsselte Kopien von Prompts und Antworten für Sicherheitsprüfungen im eigenen Cloud-Konto des Kunden. Teams, die auf `claude-opus-4-5-20251101` festgelegt sind, haben rund zwei Monate Zeit für den Umstieg auf Opus 5.5.

Quelle: https://platform.claude.com/docs/en/release-notes/api

**Nutzer der Gemini API können nun gezielt für einzelne Seiten, Zellen und Medienabschnitte statt für ganze Dateien bezahlen.** File Slicing funktioniert über alle Gemini-4-Modelle hinweg und ergänzt native Uploads für Office- und OpenDocument-Formate. Vercel maß beim Überfliegen extrahierter PDF-Texte den 14-fach geringeren Token-Verbrauch; LiteLLM maß 67 Prozent weniger Token für ein PDF und 33 Prozent weniger für eine Arbeitsmappe – beides Partnerangaben ohne Preise oder numerische Dateigrenzen.

Quelle: https://blog.google/innovation-and-ai/technology/developers-tools/file-slicing-controls/

## Forschung

**Eine Prüfung verifizierte über sechs mehrstufige Benchmark-Suiten hinweg nur 29,3 Prozent der Aufgaben.** Zwei Autoren überprüften 749 Aufgaben aus acht Benchmarks sowie 767 öffentliche Modellevaluierungen. Bestätigte Mängel verweigerten regelkonformen Lösungen in 71,7 Prozent der Fälle die Anerkennung, während die übrigen Abkürzungen zuließen; gepatchte Container senkten bestätigte Laufzeit-Umgehungen von 14,7 auf 2,7 Prozent. Dies ist der erste Meilenstein einer laufenden Überprüfung der Autoren, deren Verfahren festlegt, was als verifiziert gilt.

Quelle: https://arxiv.org/abs/2611.27622

**Eine Methode auf Basis von Reasoning-Graphen trennt originalgetreue Gedankengänge von effizienten.** Die Autoren messen, ob semantische Stützung die Vorhersage eines Modells erklärt und ob die Schritte auf einem Pfad zur Antwort bleiben. Untreue und Ineffizienz korrelierten nur schwach oder uneinheitlich mit der Korrektheit, und gezieltes Fine-Tuning verbesserte jede Eigenschaft ohne Genauigkeitsverlust; das Abstract nennt keine Effektstärken, und das Ergebnis hängt von der Graphkonstruktion der Autoren ab.

Quelle: https://arxiv.org/abs/2611.27100

**Vierzehn Sprachmodelle bildeten bei der Wahl zwischen Optionen ein Muster aus Kompression und anschließendem Vergleich aus.** Über zwölf Benchmarks hinweg verdichteten mittlere Schichten den Prompt in einen Niedrigrang-Engpass, und spätere Schichten weiteten ihn wieder zu einer Vergleichsgeometrie aus. Niedrigrang-Eingriffe nahe diesem Engpass veränderten spätere Präferenzen, doch das von einem einzelnen Autor verfasste NeurIPS-Papier belegt das Muster über seine eigene Kovarianzmethode.

Quelle: https://arxiv.org/abs/2611.26874

**Synthetische Umfrageteilnehmende bildeten nur 0,4 bis 10,5 Prozent der menschlichen Präferenzvariation ab.** Drei offene Modellfamilien spielten politische Entscheidungen von 1.991 chilenischen, 843 französischen und 434 brasilianischen Erwachsenen nach. Keine der 27 Bedingungen traf zugleich individuelle Entscheidungen, Bevölkerungsheterogenität und politische Gliederung; eine geänderte Reihenfolge der Vorschläge veränderte 12,3 bis 31,2 Prozent der Modellentscheidungen.

Quelle: https://arxiv.org/abs/2611.28383

**Schnelle Entscheidungsmodelle sparten Zeit, ließen sich aber wesentlich leichter vergiften.** Vier Modelle erreichten über 1.440 synthetische Browser-Aufgabenpaare im Schnitt 91 Prozent Genauigkeit ohne Manipulation, während Two-Shot-Kommentareinschleusungen eine Angriffserfolgsquote von 81,2 Prozent erzielten. Bei 48 abgeglichenen Aufgaben beantwortete eine kurze Gedankenkette 95,83 Prozent der vergifteten Eingaben korrekt gegenüber 38,54 Prozent bei der schnellen Variante – bei 1,94 Sekunden statt 0,29 Sekunden. Ein separates System-1-Modell mit 4 Milliarden Parametern meldet auf drei Benchmarks um 75 bis 91 Prozent niedrigere Episodenkosten, testete jedoch keine manipulierten Eingaben.

Quellen: https://arxiv.org/abs/2611.27679, https://arxiv.org/abs/2611.23751

**Manche Interpretierbarkeitstests können ein Merkmal bescheinigen, das das Modell gar nicht wie behauptet nutzt.** Die Arbeit konstruiert „Parasiten-Merkmale“ (parasite features), die eine Richtung zur Unterscheidung von Eingaben mit einer weiteren Richtung zur Steuerung von Ausgaben kombinieren und so einen Test auf kausale Abstraktion über unverbundene Pfade bestehen. Experimente zeigen dieses Versagen bei syntaktischer Kongruenz und zweistelliger Addition; das Ergebnis ist eine Warnung aus zwei Aufgaben, kein Ersatzverfahren.

Quelle: https://arxiv.org/abs/2611.26711

**Ein Hirnzustands-Benchmark ergab, dass die Vorhersage von Reizen nicht bedeutet, dass ein Modell den inneren Zustand einer Betrachterin oder eines Betrachters verfolgt.** Reine Reiz-Encoder erreichten eine Vorhersagekorrelation von 0,320, lagen beim State-Maß des Benchmarks aber bei null. Das Zwei-Zeitskalen-Modell der Autoren erzielte eine Korrelation von 0,349 sowie 5,5 Prozent bei State, 16 Prozent bei Forecast und 20,3 Prozent bei Updating, wobei die absolute State-Leistung gering blieb.

Quelle: https://arxiv.org/abs/2611.28508

**Die meisten erfolgreichen Äquivalenztests für Menschensimulationen in einer Prüfung hätte auch ein Nulleffekt-Modell bestanden.** In einer Neuanalyse von 70 Experimenten entfielen bei einer Spanne von plus/minus 0,20 Standardabweichungen 72 Prozent der bestandenen Tests von GPT-4 auf Nullreferenz-Treffer. Eine vorab registrierte Claude-Simulation bestand drei Absichtsziele, verschob Normüberzeugungen aber um 0,065 Standardabweichungen gegenüber 0,351 bei Menschen; das Papier weist auf nachträgliche Ergänzungen in einem Teil seiner Analyse hin.

Quelle: https://arxiv.org/abs/2611.27186

**Ein Adapter fester Kapazität lernte, was er behalten und wann er vergessen soll.** Ein Controller weist Erinnerungen innerhalb eines LoRA-Adapters unabhängige Zerfallsraten zu und erreichte auf den synthetischen Nutzerverläufen der Autoren 86 Prozent der Orakel-Leistung. Eine verwandte Studie fand, dass das Mischen kurzer und langer Verläufe stabile Regeln mit weniger Token vermitteln kann, doch stammen beide Ergebnisse aus künstlich erzeugten Welten.

Quellen: https://arxiv.org/abs/2611.25235, https://arxiv.org/abs/2611.28613

**Ein zweiter KI-Partner brachte beim Brainstorming mehr Ideen, verringerte jedoch den menschlichen Beitrag.** Die Laborstudie (N=168) verglich Gruppen mit zwei Agenten mit menschlichen Paaren; erst der zweite Agent erhöhte die Ausdifferenzierung innerhalb einer Sitzung. Die Aufgabe war eng gefasst, und das Ergebnis für einen einzelnen Agenten ließ sich nicht verallgemeinern. Quelle: https://arxiv.org/abs/2611.26663

**Ein spezialisiertes Verhaltensmodell und zwei Prüfstudien kommen zu gegensätzlichen Befunden, was gute synthetische Personen erfordern.** Chiron, trainiert auf 288.307 Datensätzen und 1.411.750 Entscheidungen, meldet um bis zu 28,4 Prozent bessere individuelle Vorhersagen als führende Modelle sowie um 82,2 bis 94,3 Prozent geringere Fehler bei den Effektstärken. Die Prüfung synthetischer Öffentlichkeiten fand stark verengte Variation, während die Äquivalenzprüfung ergab, dass viele scheinbare Übereinstimmungen auch Nulleffekte akzeptieren; alle nutzen von den Autoren ausgewählte Aufgaben.

Quellen: https://arxiv.org/abs/2611.24830, https://arxiv.org/abs/2611.28383, https://arxiv.org/abs/2611.27186

## Arbeit und Wirtschaft

**Börsennotierte Unternehmen mit höherer gemessener Agenten-Exponierung schrieben später weniger Stellen unterhalb der Senior-Ebene aus.** Ein Arbeitspapier verknüpft rund zwei Billiarden Modell-Token mit 34,8 Millionen Stellenanzeigen. Ein Anstieg seines börsenbasierten Exponierungsmaßes um eine Standardabweichung ging nach sechs Monaten mit einem um 2,11 Prozent niedrigeren Wachstum der Stellenausschreibungen und nach neun Monaten mit 3,20 Prozent einher; das Ergebnis bezieht sich auf Ausschreibungen, nicht auf Entlassungen, und leitet die Exponierung aus Marktreaktionen ab.

Quelle: https://arxiv.org/abs/2611.27210

**Claude Ship erweitert Programmieragenten vom Schreiben von Code auf dessen Prüfung und Freigabe.** Laut Anthropic haben sich die zusammengeführten Pull Requests zwischen Juni und September mehr als verdoppelt, während der Anteil rückgängig gemachter Änderungen um mehr als 40 Prozent gesunken sei – ohne Nenner oder Vergleichsgruppe zu nennen. Code Review ist allgemein verfügbar, während PR Steward und Approvals in der Beta bleiben; Administratoren können die abgerechneten Token-Ausgaben deckeln.

Quelle: https://claude.com/resources/articles/introducing-claude-ship

**Ein Wirtschaftsmodell zeigt, dass langsame „Schwachstellen“-Aufgaben (Weak-Link-Aufgaben) explosionsartige Gewinne durch sich rasch verbesserndes Kapital bremsen können.** Das NBER-Arbeitspapier schätzt, dass die Produktivität bei kapitalkomplementären Aufgaben rund fünf Prozentpunkte pro Jahr schneller steigt als bei Arbeitsaufgaben. Sein starkes gesamtwirtschaftliches Wachstumsergebnis hängt von Aufgabensubstitution und Engpässen im Modell ab und beschreibt daher eher einen Mechanismus als eine Prognose.

Quelle: https://www.nber.org/papers/w36050

**AlphaFold2 verlagerte Experimente in der Strukturbiologie hin zu Proteinen nahe bekannten Beispielen.** Ein NBER-Papier verfolgt 530.471 Proteine und stellt fest, dass verlässliche Vorhersagen Experimente an bekannten Proteinen und nahen Verwandten vermehrten, Versuche an weit entfernten Erststrukturen jedoch verringerten. Die Studie misst, worauf Forschende ihre Experimente richteten, nicht den späteren wissenschaftlichen Wert dieser Entscheidungen.

Quelle: https://www.nber.org/papers/w36045

## Prompting-Techniken

**Ein an OWASP ausgerichteter Prompt-Block verringerte Scanner-Funde in KI-generierten Webanwendungen um rund ein Drittel.** Einhundert Spezifikationen wurden viermal mit Claude Code und Codex umgesetzt und ergaben 6.721 gesichtete Befunde. Das Inzidenzratenverhältnis betrug 0,65 bei einem 95-Prozent-Intervall von 0,60 bis 0,71, doch verdoppelte der Block die angegebenen Abhängigkeiten, und Scanner-Funde sind keine nachgewiesenen Exploits.

Quelle: https://arxiv.org/abs/2611.28408

**Die Anweisung, abgerufene Texte zu überprüfen, brachte Modelle dazu, häufiger falsche Antworten zu übernehmen.** FutureBench testete 3.629 Fragen auf sechs Modellen. Ein Hinweis, dass Passagen irreführen können, stellte 82,5 bis 98,9 Prozent der korrekten Antworten wieder her, die der normale Verify-Prompt verdrängt hatte, bei weniger als einem Punkt Veränderung auf wahren Passagen; das Ergebnis stammt aus einer einzelnen Benchmark-Familie zweier Autoren.

Quelle: https://arxiv.org/abs/2611.23601

## Was Leute bauen

**Gall hält ein Mixture-of-Experts-Modell mit 26 Milliarden Parametern auf einem MacBook Air mit 24 GB Arbeitsspeicher lauffähig, indem es das Modell nach jeder Antwort entlädt.** Die Rust- und Metal-Engine speichert den Gesprächszustand, fällt im Leerlauf auf 32–57 MB Speicher zurück und lädt einen warmen Zustand in rund 0,1 Sekunden neu. Ihr Autor maß auf einem M2 Air rund 20 Token pro Sekunde bei kurzem Kontext und 16 bei 29.900 Token; die Modellqualität und die beworbene Einstellung für 100.000 Token wurden nicht evaluiert.

Quelle: https://github.com/ltrgoddard/gall

**OCRia-nano-1 zerlegt Dokumente mit 8,1 Millionen Parametern auf einer CPU.** LlamaIndex meldet 59,2 Punkte auf ParseBench-2 und 27,8 Seiten pro Sekunde auf 16 virtuellen CPUs. Bei Diagrammen erreicht das Modell jedoch nur 3,1 Punkte gegenüber 77,4 für sein Lehrermodell mit 4 Milliarden Parametern, und die Gewichte unterliegen einer eigenen Lizenz, die größere kommerzielle Nutzer einschränkt.

Quelle: https://huggingface.co/llamaindex/OCRia-nano-1

**OpenToolSearch nutzt zwei Modelle mit je 0,6 Milliarden Parametern zur Auswahl aus großen Werkzeugkatalogen.** Sein Reranker erreicht einen nDCG@10 von 70,8 auf dem öffentlichen ToolRet und 89,0 auf dem eigenen Datensatz der Autoren bei angegebenen 0,19 Dollar pro 1.000 Suchanfragen und 0,10 Sekunden Median-Latenz. Wettbewerber schneiden in beiden Tests besser ab, und die Autoren empfehlen, einem Modell bei höchstens rund 200 Werkzeugen die vollständige Liste direkt zu übergeben.

Quelle: https://github.com/ai3inc/opentoolsearch

**CubePod stellt Programmieragenten persistente Kata-microVM-Sandboxen bereit.** Das E2B-kompatible Kubernetes-Projekt beansprucht Zuweisungen aus einem Warm-Pool in unter 50 Millisekunden sowie knotenübergreifende Wiederaufnahmen oder Copy-on-Write-Forks in etwa einer Sekunde. Für diese Zahlen gibt es keine veröffentlichte Messmethode, und der Betrieb erfordert Kata Containers samt einem Block-Storage-Treiber. Quelle: https://github.com/cubeplexai/cubepod

**Zwei kleine Werkzeuge sichern Agenten-Abhängigkeiten an unterschiedlichen Stellen ab.** mcpwatch friert Beschreibungen von MCP-Werkzeugen ein und blockiert veränderte Werkzeuge zur Laufzeit, doch sind seine Sicherheitsnoten keine Garantien und sein Fingerabdruck-Verfahren ist nicht dokumentiert. slop-deps prüft Importe gegen 4.179 Paketnamen und Paketregister, einschließlich Tippfehler- und Homoglyphenprüfungen; sein Zeitbeispiel mit 142 Dateien ist nur illustrativ, und seine gesamte Codebasis wurde von Agenten unter menschlicher Leitung geschrieben.

Quellen: https://www.mcpwatch.io, https://github.com/viditx/slop-deps

**Terminal Tasks Open veröffentlicht 30 Aufgaben und eine Prüfung von Mängeln in einem größeren Benchmark.** Der Autor meldet Fehler in 23 von 66 Aufgaben von Terminal-Bench 4.1 und ordnet rund 52 Prozent von 980 fehlgeschlagenen Agentendurchläufen als Overfitting, 31 Prozent als Fehleinschätzung und 9 Prozent als Fehlbedienung ein. Der Prüfer entwickelte zugleich den Ersatz-Benchmark und vertreibt eine Evaluierungspipeline, während die Kategorien seine eigenen sind.

Quelle: https://vetto.ai/companies/terminal-tasks-v2/

## Lesenswert

**Hugging Face zeigt, wie ein Agenten-Benchmark eine Abkürzung statt der eigentlichen Aufgabe belohnen kann.** Ein Skript lieferte bei allen acht Raman-Spektrum-Aufgaben das richtige Defektverhältnis, ohne Peaks anzupassen, weshalb die Autoren Prüfungen für einzelne Peaks ergänzen mussten. gpt-oss-120b bestand 11 von 24 Durchläufen und anschließend 13, als sich lediglich der Inferenz-Anbieter änderte; drei stärkere Modelle bestanden alle 24, sodass der kleine angepasste Satz sie nicht nach Leistung ordnen kann.

Quelle: https://huggingface.co/blog/agentic-evals

**Ein von AMD unterstützter Test ersetzte einen DRAM-Pool für den Agenten-KV-Cache bei nahezu gleichem Durchsatz durch NVMe.** Mit Kimi-K3 auf 16 MI355X-GPUs blieben drei Parallelitätstests innerhalb von einem Prozent des DRAM-Werts, während die Cache-Trefferquote 96 Prozent der Durchsatzschwankungen über 42 Durchläufe erklärte. Die NVMe-Laufwerke würden ihre spezifizierte Schreiblebensdauer in rund 5,5 Monaten aufbrauchen, wenn bei 96 Sitzungen jeder Block gespeichert würde, und die meisten Vergleiche waren Einzeldurchläufe mit rund 2,5 Prozent Rauschen.

Quelle: https://vllm.ai/blog/2026-11-23-skip-the-dram-tier

**Gemini-4-Agententeams fanden günstigere Quantenschaltkreise und bewiesen jedes Ergebnis in Lean.** Google DeepMind meldet 11,8-fach geringere Rechenkosten für eine Fusionssimulation, 2,5-fach geringere bei Cytochrom P450 und 290-fach geringere bei einer Arcsin-Routine. Menschen wählten die Probleme aus und überwachten sie, und die entstandenen Schaltkreise übersteigen weiterhin die wahrscheinliche Kapazität früher fehlerkorrigierter Quantencomputer.

Quelle: https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification/

**Anthropic veröffentlichte eine von KI verfasste Behauptung, dass sich VP von VNP unterscheide, samt Lean-Beweis, aber ohne menschliche mathematische Begutachtung.** Dem Repository zufolge prüft ein unabhängiger Kernel die formalen Aussagen mit Standardaxiomen. Nichts prüft maschinell, ob diese Aussagen mit den Behauptungen des Papiers übereinstimmen, und das Projekt bezeichnet sich selbst als nicht gepflegten Schnappschuss; die Frage P gegen NP wird damit nicht geklärt.

Quelle: https://github.com/anthropics/formal-math/tree/main/vp-vnp

## Hacker News

**GLM-5.4 machte geschleifte Transformer-Schichten zum zweiten Architekturtrend innerhalb einer Woche.** Laut Z.ai werden gemeinsam genutzte Schichten mehrfach durchlaufen, um ohne zusätzliche Parameter effektiv mehr Tiefe zu gewinnen, und Simon Willison vergleicht die Idee mit Inkling 2 Mini von Thinking Machines. Sein praktischer Test bestand aus einem einzigen Bild-Prompt, die Gewichte sind nicht offen, und die zugänglichen Quellen nannten weder Parameterzahl noch formale Benchmarks; der Hacker-News-Diskussionsfaden erreichte 1.075 Punkte.

Quellen: https://simonwillison.net/2026/Nov/23/glm-54/, https://news.ycombinator.com/item?id=50609685

## YouTube

**Dex Horthy von Factory schlägt zwölf Kontrollmechanismen für von Agenten erstellte Software vor.** Der englischsprachige Vortrag auf der AI Engineer behandelt Planung, Druck zwischen Phasen, Feature-Flags, Evaluierungen und Agenten, die ihre eigene Arbeit testen. Laut Horthy erzielt das beste Modell rund 16 Prozent auf der Slop Code Bench, ohne die Aufgabenanzahl zu nennen; Factory verkauft Programmieragenten, sodass die Regeln eher Anbieterpraxis als ein kontrolliertes Ergebnis darstellen.

Quelle: https://www.youtube.com/watch?v=-NFMsM2y0Vk

**Der Stanford-Kurs CS312 fordert Studierende auf, Trainingsergebnisse vorab vorherzusagen.** Sein achtschichtiges Modell mit 30 Millionen Parametern trainiert auf einer GPU in rund zehn Minuten, sodass Experimente zu Lernraten und Architekturen günstig genug für die Lehre bleiben. Die Zusammenfassung stammt aus der englischsprachigen Videobeschreibung und nicht aus einem Transkript. Quelle: https://www.youtube.com/watch?v=JLcCYvUawsM

## Kurz notiert

**Derselbe Sicherheitsmonitor verpasste je nach Erzeugung der Angriffe 0,2 Prozent oder 23 Prozent erfolgreicher Attacken.** Das britische AI Security Institute testete einen früheren Produktivmonitor von OpenAI gegen Angriffe mehrerer Strategien; ein Durchlauf mit bestärkendem Lernen verschob die Verpassensquote von 0,5 auf 20,8 Prozent. Es handelt sich um einen einzelnen Aufbau, doch zeigt er, dass synthetische Monitorwerte ohne Begründung, weshalb die Angriffsstrategie künftige Angriffe abbildet, nicht für sich stehen können.

Quelle: https://www.aisi.gov.uk/blog/attack-policy-selection-can-make-monitor-evaluations-misleading

**OpenAI und Cisco veröffentlichten Shirudo, um einen Exploit-Pfad in einem laufenden Linux-Dienst vor dem Einspielen eines Patches zu blockieren.** Seine signierten eBPF-Schutzschilde erfordern eine Freigabe durch Betreiber und hinterlassen ein TPM-gestütztes Protokoll. Ein kontrollierter Anbietertest stoppte Java4Shell gegen Elasticsearch ohne Neustart; der Beitrag nennt keine Leistungs- oder Einsatzkennzahlen, und der Schild bleibt eine Übergangsmaßnahme.

Quelle: https://openai.com/index/introducing-shirudo

**Die CISA nahm eine Path-Traversal-Lücke in MONAI Label in ihren Katalog ausgenutzter Schwachstellen auf.** Über CVE-2026-133968 kann ein nicht authentifizierter Angreifer außerhalb des Datenspeichers des medizinischen Bildgebungsservers schreiben und möglicherweise Code ausführen; für US-Bundesbehörden galt eine Behebungsfrist bis zum 26. November. Quelle: https://nvd.nist.gov/vuln/detail/CVE-2026-133968

**Die Vereinigten Staaten setzten verbundene Unternehmen von Megaspeed sowie eine Alibaba-Tochter in Singapur auf ihre Entity List.** Die Beschränkung blockiert Käufe moderner Chips, während Behörden mutmaßliche Umleitungen von Nvidia-Chips nach China prüfen; Megaspeed bestreitet entsprechende Lieferungen. Quelle: https://www.bloomberg.com/news/articles/2026-11-24/us-blacklists-alibaba-owned-company-in-setback-to-ai-ambitions

**Oregon und Virginia verklagten mit Elon Musk verbundene Unternehmen wegen sexualisierter Grok-Bilder.** Die Bundesstaaten werfen ihnen vor, Schutzmechanismen hätten Bilder realer Personen einschließlich Kindern nicht verhindert, während X erklärt, jede Ausgabe werde geprüft; das Briefing hatte keinen Zugang zu den Klageschriften, sodass die beantragten Maßnahmen unbestätigt bleiben. Quelle: https://arstechnica.com/tech-policy/2026/11/states-sue-spacex-to-stop-grok-from-generating-child-sex-images-revenge-porn/

## Wirtschaft in Kürze

Amazon kaufte die Chip-Optimierungssoftware und das Team von Decart für Berichten zufolge 7,5 Milliarden Dollar; die Unternehmen veröffentlichten keinen Benchmark für die Software. Quelle: https://www.theregister.com/ai-and-ml/2026/11/23/amazon-scoops-up-ai-accelerator-tech-to-keep-chips-busy-at-all-times/5311754

Der Verwaltungsrat der University of Michigan genehmigte mit sieben zu einer Stimme ein Rechenzentrum mit Los Alamos im Wert von 1,25 Milliarden Dollar, während die örtliche Gemeinde ein sechsmonatiges Moratorium für neue elektrische Infrastruktur aufrechterhält. Quelle: https://www.404media.co/ypsilanti-michigan-data-center-vote/

## Was ansteht

Anthropic stellt Claude Opus 4.5 am 22. Januar 2027 ein. Die Behebungsfrist der CISA für MONAI Label endet am 26. November, und für den 15. Dezember ist ein technisches Webinar zu Shirudo angesetzt.
